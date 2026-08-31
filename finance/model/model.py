"""
Mulligan Mints — 60-month P&L, cashflow and funding model.

Drives everything off assumptions.py. Nothing here should need editing to
change the plan; change the assumptions instead.

Usage:  from model import run;  r = run("base")
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import assumptions as A


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def year_of(month: int) -> int:
    """1-indexed model year for a 1-indexed month."""
    return (month - 1) // 12 + 1


def month_in_year(month: int) -> int:
    """1..12 position within the model year."""
    return (month - 1) % 12 + 1


def inflate(base: float, rate: float, month: int) -> float:
    """Compound an annual rate over whole model years."""
    return base * (1 + rate) ** (year_of(month) - 1)


def usdzar(month: int) -> float:
    return A.USDZAR_YEAR_1 * (1 + A.ZAR_DEPRECIATION_PA) ** (year_of(month) - 1)


def fob_usd_for_annual_volume(annual_units: float) -> float:
    for ceiling, price in A.FOB_USD_CURVE:
        if annual_units <= ceiling:
            return price
    return A.FOB_USD_CURVE[-1][1]


def ramp(month: int, start_month: int, end_of_year_values: list[float]) -> float:
    """
    Linear month-by-month ramp of an outlet count.

    end_of_year_values[y-1] is the count standing at the last month of year y.
    Before start_month the count is zero; between start_month and the end of
    that year we ramp from zero to that year's exit number.
    """
    if month < start_month:
        return 0.0
    y = year_of(month)
    j = month_in_year(month)
    target = end_of_year_values[y - 1]
    prev = end_of_year_values[y - 2] if y > 1 else 0.0

    start_y = year_of(start_month)
    if y == start_y and prev == 0.0:
        # partial first year: ramp from the start month to that year's exit
        span = 12 - month_in_year(start_month) + 1
        step = j - month_in_year(start_month) + 1
        return target * step / span
    return prev + (target - prev) * j / 12


def annual_price_factor(month: int) -> float:
    return (1 + A.PRICE_INCREASE_PA) ** (year_of(month) - 1)


# ---------------------------------------------------------------------------
# purchase orders
# ---------------------------------------------------------------------------

LEAD_MONTHS = int(round(
    A.PRODUCTION_LEAD_MONTHS + A.SHIPPING_TRANSIT_MONTHS + A.CLEARING_MONTHS
))  # 4

# Guards. These encode the timing relationships that are easy to break by
# editing one number in assumptions.py and forgetting its consequences.
# The first sale cannot precede the first order plus the pipeline, and no
# order can be placed before there is artwork to print.
assert A.EARLIEST_PO_MONTH >= A.ARTWORK_READY_MONTH, (
    f"First PO (month {A.EARLIEST_PO_MONTH}) cannot precede artwork "
    f"(month {A.ARTWORK_READY_MONTH})"
)
assert A.FIRST_SALE_MONTH >= A.EARLIEST_PO_MONTH + LEAD_MONTHS, (
    f"FIRST_SALE_MONTH is {A.FIRST_SALE_MONTH}, but the first PO cannot be "
    f"placed before month {A.EARLIEST_PO_MONTH} and takes {LEAD_MONTHS} months "
    f"to land — the earliest possible sale is month "
    f"{A.EARLIEST_PO_MONTH + LEAD_MONTHS}"
)


@dataclass
class PurchaseOrder:
    order_month: int
    arrive_month: int
    units: int
    fob_zar_total: float = 0.0
    freight_zar: float = 0.0
    insurance_zar: float = 0.0
    duty_zar: float = 0.0
    clearing_zar: float = 0.0
    customs_value_zar: float = 0.0      # FOB — the SA duty base
    landed_zar_total: float = 0.0

    @property
    def landed_per_unit(self) -> float:
        return self.landed_zar_total / self.units if self.units else 0.0


def cost_a_purchase_order(units: int, order_month: int, arrive_month: int,
                          annual_units: float, fob_mult: float) -> PurchaseOrder:
    """
    Build the full landed-cost stack for one order.

    SA duty on HS 1704 is levied on the FOB customs value, so freight and
    insurance sit outside the duty base but inside landed cost.
    """
    po = PurchaseOrder(order_month, arrive_month, units)
    rate = usdzar(order_month)

    fob_usd = fob_usd_for_annual_volume(annual_units) * fob_mult
    po.customs_value_zar = units * fob_usd * rate
    po.fob_zar_total = po.customs_value_zar

    # Sub-container orders lose the container economics.
    lcl_penalty = 1.35 if units < 60_000 else 1.0
    containers = units / A.UNITS_PER_20FT
    po.freight_zar = A.FREIGHT_USD_PER_20FT * containers * rate * lcl_penalty
    po.clearing_zar = A.CLEARING_ZAR_PER_20FT * containers * lcl_penalty
    po.insurance_zar = po.fob_zar_total * A.MARINE_INSURANCE_PCT_OF_FOB
    po.duty_zar = po.customs_value_zar * A.IMPORT_DUTY_PCT

    po.landed_zar_total = (po.fob_zar_total + po.freight_zar + po.insurance_zar
                           + po.duty_zar + po.clearing_zar)
    return po


# ---------------------------------------------------------------------------
# the model
# ---------------------------------------------------------------------------

@dataclass
class Result:
    scenario: str
    months: list[int] = field(default_factory=list)
    rows: dict = field(default_factory=dict)
    purchase_orders: list = field(default_factory=list)

    def series(self, key):
        return self.rows[key]

    def annual(self, key):
        s = self.rows[key]
        return [sum(s[(y - 1) * 12: y * 12]) for y in range(1, 6)]

    def annual_last(self, key):
        s = self.rows[key]
        return [s[y * 12 - 1] for y in range(1, 6)]


def _unit_demand(month: int, mult: float, sc: dict | None = None) -> dict[str, float]:
    """
    Units demanded per channel in a given month, before the stock constraint.

    Callable past the horizon: replenishment has to look ~8 months ahead, so
    beyond month 60 we hold year-5 run-rates flat rather than dropping to zero.
    """
    sc = sc or {}
    off = set(sc.get("channels_off", []))
    outlets_ov = sc.get("outlets_override", {})
    rate_ov = sc.get("rate_override", {})

    y = min(year_of(month), 5)
    out: dict[str, float] = {}

    for name in ("golf", "bars"):
        c = A.CHANNELS[name]
        if name in off:
            out[name] = 0.0
            continue
        plan = outlets_ov.get(name, c["outlets_end_of_year"])
        rates = rate_ov.get(name, c["units_per_outlet_month"])
        outlets = ramp(min(month, A.HORIZON_MONTHS), A.FIRST_SALE_MONTH, plan)
        outlets = min(outlets, c["universe"])
        out[name] = outlets * rates[y - 1] * mult

    d = A.CHANNELS["dtc"]
    dtc_plan = sc.get("dtc_override", d["units_per_month_by_year"])
    out["dtc"] = (dtc_plan[y - 1] * mult
                  if month >= A.FIRST_SALE_MONTH and "dtc" not in off else 0.0)

    r = A.CHANNELS["retail"]
    if "retail" in off:
        out["retail"] = 0.0
    else:
        plan = outlets_ov.get("retail", r["outlets_end_of_year"])
        rates = rate_ov.get("retail", r["units_per_outlet_month"])
        outlets = ramp(min(month, A.HORIZON_MONTHS), r["start_month"], plan)
        out["retail"] = outlets * rates[y - 1] * mult

    e = A.CHANNELS["export"]
    if "export" in off or month < e["start_month"]:
        out["export"] = 0.0
    else:
        annual = sc.get("export_override", e["units_by_year"])[y - 1] * mult
        # spread over the months of that year in which we actually export
        active = 12 - (month_in_year(e["start_month"]) - 1) if y == year_of(e["start_month"]) else 12
        out["export"] = annual / active

    return out


def run(scenario: str = "base") -> Result:
    sc = A.SCENARIOS[scenario]
    vol_mult = sc["volume_multiplier"]
    price_mult = sc["net_price_multiplier"]
    fob_mult = sc["fob_multiplier"]

    N = A.HORIZON_MONTHS
    R = Result(scenario=scenario, months=list(range(1, N + 1)))

    keys = [
        "units_golf", "units_bars", "units_dtc", "units_retail", "units_export",
        "units_total",
        "rev_golf", "rev_bars", "rev_dtc", "rev_retail", "rev_export",
        "rev_licensing", "revenue",
        "cogs", "gross_profit",
        "opex_salaries", "opex_marketing", "opex_logistics", "opex_commission",
        "opex_overheads", "opex_setup", "opex_npd", "opex_total",
        "ebitda", "finance_cost", "tax_charge", "net_profit",
        "cash_tf_draw", "cash_tf_repay", "tf_outstanding",
        "cash_investor_repay", "investor_outstanding",
        "cash_in_sales", "cash_out_supplier", "cash_out_duty_clearing",
        "cash_out_opex", "cash_vat", "cash_tax", "cash_funding",
        "net_cashflow", "closing_cash",
        "stock_units", "stock_value", "debtors", "headcount",
    ]
    for k in keys:
        R.rows[k] = [0.0] * N

    # forecast total annual units up-front (drives the FOB volume curve)
    annual_units_forecast = [0.0] * 6
    for m in range(1, N + 1):
        annual_units_forecast[year_of(m)] += sum(_unit_demand(m, vol_mult, sc).values())

    stock_units = 0.0
    stock_value = 0.0
    open_orders: list[PurchaseOrder] = []
    all_orders: list[PurchaseOrder] = []

    receivable_schedule = [0.0] * (N + 120)   # cash landing by month
    vat_output_accrued = 0.0
    vat_input_accrued = 0.0
    assessed_loss = 0.0
    tax_accrued_unpaid = 0.0
    cash = 0.0

    # Trade finance: an import facility that advances a share of each stock
    # payment and is repaid out of the sale proceeds a few months later.
    tf = sc.get("trade_finance")
    tf_book: list[tuple[int, float]] = []   # (repay_month, principal)

    # Investor revenue share: a fixed rand amount per tin sold, paid until the
    # agreed capital sum has been returned. It is a repayment of capital, not an
    # operating cost, so it sits below EBITDA and hits cash only.
    inv = sc.get("investor_repayment")
    inv_repaid = 0.0

    for m in range(1, N + 1):
        y = year_of(m)
        i = m - 1

        # ---------------- goods arriving this month ----------------
        # Arrivals are booked BEFORE sales. LEAD_MONTHS already rounds the true
        # 3.5-month order-to-shelf time up to 4 and already contains the customs
        # and Port Health allowance, so holding landed stock back for a further
        # full month would charge the plan 5 months for a 3.5-month pipeline.
        arriving = [po for po in open_orders if po.arrive_month == m]
        for po in arriving:
            stock_units += po.units * (1 - A.STOCK_WASTAGE_PCT)
            stock_value += po.landed_zar_total
            open_orders.remove(po)

        # ---------------- demand, capped by available stock ----------------
        demand = _unit_demand(m, vol_mult, sc)
        wanted = sum(demand.values())
        available = stock_units
        fill = 1.0 if wanted <= available else (available / wanted if wanted else 0.0)
        sold = {k: v * fill for k, v in demand.items()}
        units_sold = sum(sold.values())

        for k in ("golf", "bars", "dtc", "retail", "export"):
            R.rows[f"units_{k}"][i] = sold[k]
        R.rows["units_total"][i] = units_sold

        # ---------------- revenue ----------------
        pf = annual_price_factor(m) * price_mult
        dist_share = sc.get("distributor_share", A.DISTRIBUTOR_SHARE_OF_BARS_BY_YEAR)[y - 1]
        revenue = 0.0
        domestic_revenue = 0.0
        for k in ("golf", "bars", "dtc", "retail", "export"):
            if k == "bars":
                # blended price: part sold direct to venues, part to distributors
                direct_units = sold[k] * (1 - dist_share)
                dist_units = sold[k] * dist_share
                rev = (direct_units * A.CHANNELS[k]["net_price_y1"] * pf
                       + dist_units * A.DISTRIBUTOR_NET_PRICE_BARS * pf)
                lag_days = (A.CHANNELS[k]["debtor_days"] * (1 - dist_share)
                            + A.DISTRIBUTOR_DEBTOR_DAYS * dist_share)
            else:
                rev = sold[k] * A.CHANNELS[k]["net_price_y1"] * pf
                lag_days = A.CHANNELS[k]["debtor_days"]

            R.rows[f"rev_{k}"][i] = rev
            revenue += rev
            if k != "export":
                domestic_revenue += rev

            lag = int(round(lag_days / 30.0))
            receivable_schedule[m + lag] += rev * (1 + (A.VAT_RATE if k != "export" else 0.0))

        # licensing income
        lic = 0.0
        lic_table = sc.get("licensing")
        if lic_table is True:
            lic_table = A.LICENSING
        elif lic_table is False or lic_table is None:
            lic_table = {}
        if y in lic_table:
            spec = lic_table[y]
            lic = (spec["signing_fees"]
                   + spec["licensee_net_sales"] * A.LICENSING_ROYALTY_PCT) / 12.0
            receivable_schedule[m + 2] += lic          # royalties settle quarterly-ish
        R.rows["rev_licensing"][i] = lic
        revenue += lic
        R.rows["revenue"][i] = revenue

        # ---------------- cost of goods ----------------
        unit_cost = (stock_value / stock_units) if stock_units else 0.0
        cogs = units_sold * unit_cost
        stock_units -= units_sold
        stock_value -= cogs
        R.rows["cogs"][i] = cogs
        R.rows["gross_profit"][i] = revenue - cogs

        # ---------------- replenishment ----------------
        # Stock on hand plus stock already on the water has to carry us from
        # next month all the way to the end of the cover window of the order we
        # are placing now -- i.e. through the whole lead time, not just from the
        # arrival date. Forgetting the pipeline months is how importers stock out.
        arrive = m + LEAD_MONTHS
        cover_end = arrive + int(math.ceil(A.TARGET_FORWARD_COVER_MONTHS))
        future_need = sum(
            sum(_unit_demand(mm, vol_mult, sc).values())
            for mm in range(m + 1, cover_end)
        )
        on_order = sum(po.units for po in open_orders)
        gap = future_need - (stock_units + on_order)
        if gap > 0 and m <= N and m >= A.EARLIEST_PO_MONTH:
            units = max(A.MIN_ORDER_UNITS, gap)
            units = int(math.ceil(units / A.ORDER_ROUNDING_UNITS) * A.ORDER_ROUNDING_UNITS)
            po = cost_a_purchase_order(
                units, m, arrive, annual_units_forecast[min(year_of(arrive), 5)] or 1, fob_mult
            )
            open_orders.append(po)
            all_orders.append(po)

        R.rows["stock_units"][i] = stock_units
        R.rows["stock_value"][i] = stock_value

        # ---------------- operating costs ----------------
        # Hires are deferred in weaker scenarios and pulled forward in stronger
        # ones -- a plan that hires the base case into a bear market is not a
        # forecast, it is a fantasy.
        delay = sc.get("hire_delay_months", 0)
        plan = sc.get("headcount", A.HEADCOUNT)
        active = [(start, role, cost) for start, role, cost in plan if m >= start + delay]
        if sc.get("headcount_is_cumulative_draw"):
            # Rows whose role starts with the same prefix before " (" are the
            # same person's pay stepping up — take the latest, do not stack.
            latest: dict[str, tuple[int, str, float]] = {}
            for start, role, cost in active:
                key = role.split(" (")[0]
                if key not in latest or start > latest[key][0]:
                    latest[key] = (start, role, cost)
            active = list(latest.values())
        salaries = sum(inflate(cost, A.OPEX_INFLATION_PA, m) for _s, _r, cost in active)
        R.rows["headcount"][i] = len(active)
        R.rows["opex_salaries"][i] = salaries

        if y == 1:
            months_live = 12 - A.FIRST_SALE_MONTH + 1
            y1_total = sc.get("marketing_y1_total", A.MARKETING_Y1_TOTAL)
            marketing = (y1_total * sc.get("marketing_multiplier", 1.0)
                         / months_live) if m >= A.FIRST_SALE_MONTH else 0.0
        else:
            marketing = revenue * sc.get("marketing_pct", A.MARKETING_PCT_OF_REVENUE)[y - 1]
        listing = (0.0 if sc.get("no_listing_fees") else
                   sum(fee for mm, _lbl, fee in A.RETAIL_LISTING_FEES if mm == m))
        marketing += listing
        R.rows["opex_marketing"][i] = marketing

        bulk_units = sold["export"] + sold["bars"] * dist_share
        logistics = (
            (units_sold - bulk_units) * inflate(A.LOGISTICS_ZAR_PER_UNIT, A.OPEX_INFLATION_PA, m)
            + bulk_units * inflate(A.LOGISTICS_ZAR_PER_UNIT_EXPORT, A.OPEX_INFLATION_PA, m)
        )
        R.rows["opex_logistics"][i] = logistics

        direct_venue_rev = R.rows["rev_golf"][i] + R.rows["rev_bars"][i] * (1 - dist_share)
        commission = direct_venue_rev * A.SALES_COMMISSION_PCT
        R.rows["opex_commission"][i] = commission

        npd = revenue * sc.get("npd_pct", A.NPD_PCT_OF_REVENUE)[y - 1]
        export_dev = R.rows["rev_export"][i] * A.EXPORT_DEV_PCT_OF_EXPORT_REVENUE[y - 1]
        # Licensing carries no COGS and no working capital, but it is not free:
        # trademark filings in each territory, agreements, licensee search,
        # travel and quality audits all land before the first royalty does.
        lic_cost = sc.get("licensing_costs", {}).get(y, 0.0) / 12.0
        R.rows["opex_npd"][i] = npd + export_dev + lic_cost

        overheads = (sum(inflate(v, A.OPEX_INFLATION_PA, m) for v in A.OVERHEADS_MONTHLY.values())
                     * sc.get("overhead_multiplier", 1.0)
                     if m >= A.OVERHEADS_START_MONTH else 0.0)
        R.rows["opex_overheads"][i] = overheads

        setup = sum(cost for mm, _item, cost in sc.get("setup_costs", A.SETUP_COSTS) if mm == m)
        R.rows["opex_setup"][i] = setup

        opex = (salaries + marketing + logistics + commission + overheads
                + setup + npd + export_dev + lic_cost)
        R.rows["opex_total"][i] = opex

        ebitda = revenue - cogs - opex
        R.rows["ebitda"][i] = ebitda

        # supplier: 30% deposit on order, 70% against bill of lading
        supplier_out = 0.0
        for po in all_orders:
            if po.order_month == m:
                supplier_out += po.fob_zar_total * A.SUPPLIER_DEPOSIT_PCT
            if po.order_month + A.PRODUCTION_LEAD_MONTHS == m:
                supplier_out += po.fob_zar_total * (1 - A.SUPPLIER_DEPOSIT_PCT)
                supplier_out += po.freight_zar + po.insurance_zar
        R.rows["cash_out_supplier"][i] = supplier_out

        duty_clearing = sum(po.duty_zar + po.clearing_zar for po in arriving)
        R.rows["cash_out_duty_clearing"][i] = duty_clearing

        # ---------------- trade finance ----------------
        tf_draw = tf_repay = tf_interest = 0.0
        if tf:
            stock_spend = supplier_out + duty_clearing
            if m >= tf["start_month"] and stock_spend > 0:
                tf_draw = stock_spend * tf["advance_pct"]
                tf_book.append((m + tf["repay_months"], tf_draw))
            due = [(rm, pr) for rm, pr in tf_book if rm == m]
            tf_repay = sum(pr for _rm, pr in due)
            tf_book = [(rm, pr) for rm, pr in tf_book if rm != m]
            outstanding = sum(pr for _rm, pr in tf_book) + tf_repay
            tf_interest = outstanding * tf["rate_pa"] / 12.0
        R.rows["cash_tf_draw"][i] = tf_draw
        R.rows["cash_tf_repay"][i] = -tf_repay
        R.rows["tf_outstanding"][i] = sum(pr for _rm, pr in tf_book)
        R.rows["finance_cost"][i] = tf_interest

        # ---------------- tax ----------------
        # Interest is deductible, so tax bites after finance costs.
        # SA assessed losses may offset at most 80% of taxable income.
        taxable = ebitda - R.rows["finance_cost"][i]
        charge = 0.0
        if taxable > 0:
            usable = min(assessed_loss, taxable * 0.80)
            assessed_loss -= usable
            charge = (taxable - usable) * A.CORPORATE_TAX_RATE
        else:
            assessed_loss += -taxable
        R.rows["tax_charge"][i] = charge
        R.rows["net_profit"][i] = ebitda - R.rows["finance_cost"][i] - charge
        tax_accrued_unpaid += charge

        # ---------------- cashflow ----------------
        cash_in = receivable_schedule[m]
        R.rows["cash_in_sales"][i] = cash_in

        # opex paid in the month, plus input VAT on the VATable share
        opex_cash = opex
        R.rows["cash_out_opex"][i] = opex_cash

        # VAT: output on domestic sales; input on import ATV and local costs.
        vat_output_accrued += domestic_revenue * A.VAT_RATE
        import_atv = sum((po.customs_value_zar * 1.10 + po.duty_zar) for po in arriving)
        vatable_opex = (marketing + logistics + overheads + setup) * 0.90
        vat_input_accrued += import_atv * A.VAT_RATE + vatable_opex * A.VAT_RATE
        vat_payment = 0.0
        if m % 2 == 0:                                    # 2-monthly VAT period
            vat_payment = vat_output_accrued - vat_input_accrued
            vat_output_accrued = vat_input_accrued = 0.0
        R.rows["cash_vat"][i] = -vat_payment

        # provisional tax in months 6 and 12 of each fiscal year
        tax_payment = 0.0
        if month_in_year(m) in (6, 12) and tax_accrued_unpaid > 0:
            tax_payment = tax_accrued_unpaid
            tax_accrued_unpaid = 0.0
        R.rows["cash_tax"][i] = -tax_payment

        # ---------------- investor revenue share ----------------
        inv_pay = 0.0
        if inv and m >= inv.get("start_month", A.FIRST_SALE_MONTH):
            remaining = inv["total"] - inv_repaid
            if remaining > 0:
                # Optional step-down: the per-tin rate drops once an agreed
                # share of the capital has been returned. Units in the month
                # that straddles the threshold are split across both rates so
                # the step happens at the right rand, not the right month.
                step_at = inv.get("step_down_at_pct")
                rate_hi = inv["per_tin"]
                rate_lo = inv.get("per_tin_after", rate_hi)
                if step_at is None or inv_repaid >= inv["total"] * step_at:
                    rate = rate_hi if step_at is None else rate_lo
                    inv_pay = min(units_sold * rate, remaining)
                else:
                    to_step = inv["total"] * step_at - inv_repaid
                    units_at_hi = min(units_sold, to_step / rate_hi)
                    inv_pay = units_at_hi * rate_hi
                    inv_pay += (units_sold - units_at_hi) * rate_lo
                    inv_pay = min(inv_pay, remaining)
                inv_repaid += inv_pay
        R.rows["cash_investor_repay"][i] = -inv_pay
        R.rows["investor_outstanding"][i] = (inv["total"] - inv_repaid) if inv else 0.0

        funding = sum(amt for mm, _lbl, amt in sc.get("funding_rounds", A.FUNDING_ROUNDS) if mm == m)
        R.rows["cash_funding"][i] = funding

        net_cf = (cash_in - supplier_out - duty_clearing - opex_cash
                  - vat_payment - tax_payment + funding
                  + tf_draw - tf_repay - tf_interest - inv_pay)
        R.rows["net_cashflow"][i] = net_cf
        cash += net_cf
        R.rows["closing_cash"][i] = cash

        R.rows["debtors"][i] = sum(receivable_schedule[m + 1: m + 4])

    assert all(po.order_month >= A.EARLIEST_PO_MONTH for po in all_orders), (
        "a purchase order was placed before the artwork gate"
    )
    R.purchase_orders = all_orders
    return R


def funding_need(scenario: str = "base") -> dict:
    """Peak cash deficit if no funding were injected — the true capital need."""
    r = run(scenario)
    cash, trough, trough_month = 0.0, 0.0, 0
    for i, m in enumerate(r.months):
        cash += r.rows["net_cashflow"][i] - r.rows["cash_funding"][i]
        if cash < trough:
            trough, trough_month = cash, m
    return {
        "peak_deficit": -trough,
        "peak_month": trough_month,
        "min_closing_cash": min(r.rows["closing_cash"]),
        "min_closing_month": r.rows["closing_cash"].index(min(r.rows["closing_cash"])) + 1,
    }
