"""
Exit analysis — what a sale at the end of year 5 is worth, and to whom.

    python3 exit_analysis.py

The model runs to month 60 and stops. This adds the event the model does not
contain: a sale of the company at that point, run through the waterfall the
shareholders agreement would actually follow.

Nothing here is a forecast. It is arithmetic on top of a plan whose volumes are
still assumptions, at multiples nobody has offered.
"""
from __future__ import annotations

import assumptions as A
import model as M

SCENARIO = "bootstrap"

# Equity splits after the R1m round.
FOUNDERS_PCT = 0.80
PJ_PCT = 0.10
INVESTOR_PCT = 0.10

# SA capital gains tax on a share disposal. Inclusion rate x marginal rate:
#
#   Individual        40% x 45%  = 18.0%   <- cheapest
#   Trust (retained)  80% x 45%  = 36.0%
#   Company           80% x 27%  = 21.6%, then 20% dividends tax to extract
#                                  => ~37.3% all-in
#
# A trust matches 18% only via the conduit principle (s25B): the gain must be
# VESTED IN RESIDENT BENEFICIARIES in the same year of assessment, and since
# 1 March 2025 flow-through applies to resident beneficiaries only. Left in the
# trust, or vested in a non-resident, it is 36%.
# [SOURCE: SARS CGT tables; s25B Income Tax Act. Confirm with a tax adviser.]
CGT_EFFECTIVE_INDIVIDUAL = 0.18
CGT_EFFECTIVE_TRUST_RETAINED = 0.36
CGT_EFFECTIVE_COMPANY = 0.216

# Multiples to test. A South African SME trades at 4-6x EBITDA; a branded
# consumer business with growth at 6-10x; a strategic buyer who wants the brand
# itself can pay more. All [EST] — nobody has offered anything.
EBITDA_MULTIPLES = [4, 6, 8, 10]

# A sale is priced cash-free and debt-free with a normal level of working
# capital left in the business. The buyer will not simply hand over the whole
# cash balance -- they will peg the working capital the business needs to keep
# trading, and only the excess counts as surplus cash to the sellers.
# Pegged here at two months of year-5 operating costs. [EST]
WORKING_CAPITAL_PEG_MONTHS = 2


def waterfall(multiple: float, scenario: str = SCENARIO) -> dict:
    r = M.run(scenario)
    y5 = 4

    ebitda = r.annual("ebitda")[y5]
    cash = r.annual_last("closing_cash")[y5]
    trade_finance = r.annual_last("tf_outstanding")[y5]
    investor_residual = r.annual_last("investor_outstanding")[y5]

    # The buyer leaves normalised working capital in the business; only cash
    # above that peg is surplus and accrues to the sellers.
    wc_peg = r.annual("opex_total")[y5] / 12.0 * WORKING_CAPITAL_PEG_MONTHS
    surplus_cash = max(0.0, cash - wc_peg)

    enterprise_value = ebitda * multiple
    # Equity value = EV plus surplus cash, less what the company owes.
    equity_value = enterprise_value + surplus_cash - trade_finance - investor_residual

    founders = equity_value * FOUNDERS_PCT
    pj = equity_value * PJ_PCT
    investor_equity = equity_value * INVESTOR_PCT

    # The investor is also repaid the capital still outstanding at exit.
    investor_total_at_exit = investor_equity + investor_residual
    repaid_over_plan = A.SCENARIOS[scenario]["investor_repayment"]["total"] - investor_residual

    return {
        "multiple": multiple,
        "ebitda": ebitda,
        "enterprise_value": enterprise_value,
        "cash": cash,
        "wc_peg": wc_peg,
        "surplus_cash": surplus_cash,
        "trade_finance": trade_finance,
        "investor_residual": investor_residual,
        "equity_value": equity_value,
        "founders_gross": founders,
        "founders_net": founders * (1 - CGT_EFFECTIVE_INDIVIDUAL),
        "pj_gross": pj,
        "investor_equity": investor_equity,
        "investor_total_at_exit": investor_total_at_exit,
        "investor_repaid_over_plan": repaid_over_plan,
        "investor_all_in": investor_total_at_exit + repaid_over_plan,
    }


def investor_irr(multiple: float, scenario: str = SCENARIO) -> float:
    """Annualised IRR on the investor's R1m, including the exit."""
    r = M.run(scenario)
    w = waterfall(multiple, scenario)
    flows = [0.0] * 62
    flows[1] = -1_000_000.0
    for i, m in enumerate(r.months):
        flows[m] += -r.rows["cash_investor_repay"][i]
        flows[m] += r.rows["dividend_to_investor"][i]
    flows[60] += w["investor_total_at_exit"]

    lo, hi = -0.9, 1.0
    for _ in range(300):
        mid = (lo + hi) / 2
        npv = sum(cf / ((1 + mid) ** t) for t, cf in enumerate(flows))
        if npv > 0:
            lo = mid
        else:
            hi = mid
    return (1 + lo) ** 12 - 1


def rands(v):
    return f"R{v:,.0f}"


if __name__ == "__main__":
    r = M.run(SCENARIO)
    print(f"EXIT AT MONTH 60 — scenario '{SCENARIO}'\n")
    print(f"  Year-5 EBITDA            {rands(r.annual('ebitda')[4])}")
    print(f"  Year-5 revenue           {rands(r.annual('revenue')[4])}")
    print(f"    of which licensing     {rands(r.annual('rev_licensing')[4])}"
          f"  ({r.annual('rev_licensing')[4]/r.annual('revenue')[4]*100:.0f}% of revenue)")
    w0 = waterfall(EBITDA_MULTIPLES[0])
    print(f"  Cash at bank             {rands(r.annual_last('closing_cash')[4])}")
    print(f"    less working capital   ({rands(w0['wc_peg'])})"
          f"   ({WORKING_CAPITAL_PEG_MONTHS} months of opex, left in the business)")
    print(f"    surplus cash           {rands(w0['surplus_cash'])}")
    print(f"  Trade finance owed       ({rands(r.annual_last('tf_outstanding')[4])})")
    print(f"  Investor capital owed    ({rands(r.annual_last('investor_outstanding')[4])})")
    print()

    hdr = (f"{'Multiple':<10}{'Enterprise':>14}{'Equity value':>15}"
           f"{'Founders (80%)':>17}{'after CGT':>13}{'PJ (10%)':>12}"
           f"{'Investor':>12}{'IRR':>7}")
    print(hdr)
    print("-" * len(hdr))
    for mult in EBITDA_MULTIPLES:
        w = waterfall(mult)
        print(f"{str(mult)+'x':<10}{rands(w['enterprise_value']):>14}"
              f"{rands(w['equity_value']):>15}{rands(w['founders_gross']):>17}"
              f"{rands(w['founders_net']):>13}{rands(w['pj_gross']):>12}"
              f"{rands(w['investor_total_at_exit']):>12}"
              f"{investor_irr(mult)*100:>6.0f}%")

    print()
    print("Investor 'all-in' includes the capital returned at R1 a tin over the plan:")
    for mult in EBITDA_MULTIPLES:
        w = waterfall(mult)
        print(f"  {mult}x: {rands(w['investor_repaid_over_plan'])} repaid over 5 years"
              f" + {rands(w['investor_total_at_exit'])} at exit"
              f" = {rands(w['investor_all_in'])} on R1,000,000")

    print()
    print("CROSS-CHECK — what a buyer might value instead of EBITDA:")
    rev = r.annual("revenue")[4]
    lic = r.annual("rev_licensing")[4]
    print(f"  1.0x revenue                {rands(rev * 1.0)}")
    print(f"  1.5x revenue                {rands(rev * 1.5)}")
    print(f"  10x the licensing royalty   {rands(lic * 10)}   (brand-only valuation)")
    print()
    print("HOLDING STRUCTURE — effective CGT on the founders' share:")
    w6 = waterfall(6)
    g = w6["founders_gross"]
    for label, rate in [("Individuals (as modelled)", CGT_EFFECTIVE_INDIVIDUAL),
                        ("Trust, gain vested in resident beneficiaries", CGT_EFFECTIVE_INDIVIDUAL),
                        ("Trust, gain retained in the trust", CGT_EFFECTIVE_TRUST_RETAINED),
                        ("Company, before extracting the cash", CGT_EFFECTIVE_COMPANY)]:
        print(f"  {label:<46} {rate*100:>5.1f}%   nets {rands(g*(1-rate))} at 6x")
    print("  Holding personally is the cheapest. A trust only matches it, never beats it.")
    print()
    print("All multiples are estimates. Nobody has offered anything.")
