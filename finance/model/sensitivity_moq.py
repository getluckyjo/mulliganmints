"""
MOQ sensitivity — the biggest unknown left on the Suntak quote.

Suntak priced USD 0.465/unit against an inquiry of 134,400 units (one 20GP) and
noted only that the quote "is based on the MOQ of one item" and that below MOQ
the price is "slightly higher". The MOQ is never stated.

That matters enormously. The plan sells 24,520 tins in year 1. If the minimum
order is a full container we buy five and a half years of year-one demand before
we have sold a single tin.

    python3 sensitivity_moq.py
"""
import copy
import importlib

import assumptions as A

# Suntak's MOQ is 800 kg of candy. At 35 g of candy per tin that is 22,857
# tins, or 22,944 rounded up to whole 96-tin cartons (239 cartons, 803 kg).
# Candy MOQs are batch minimums on a recipe, so it is almost certainly PER
# FLAVOUR — confirm that with Damita, because it is the whole decision.
MOQ_TINS_PER_FLAVOUR = 22_944

CASES = [
    (MOQ_TINS_PER_FLAVOUR,     "Launch with 1 flavour (peppermint only)"),
    (MOQ_TINS_PER_FLAVOUR * 2, "Launch with 2 flavours"),
    (MOQ_TINS_PER_FLAVOUR * 3, "Launch with 3 flavours (the current plan)"),
    (134_400,                  "For reference: one full 20GP"),
]


def run_case(moq):
    A.MIN_ORDER_UNITS = moq
    # You cannot buy 1.4 batches of candy. Orders come in whole multiples of the
    # batch minimum, so the reorder rounding IS the MOQ — leaving it at the
    # generic 10,000 rounds 22,944 up to 30,000 and hides the thing we are testing.
    A.ORDER_ROUNDING_UNITS = moq
    import model
    importlib.reload(model)
    r = model.run("base")
    n = model.funding_need("base")
    po = r.purchase_orders[0]
    # cash out on the first order: deposit + balance + freight/insurance + duty + clearing
    first_order_cash = (po.fob_zar_total + po.freight_zar + po.insurance_zar
                        + po.duty_zar + po.clearing_zar)
    # months of year-1 demand bought in that first order
    y1_units = r.annual("units_total")[0]
    return {
        "moq": moq,
        "first_po_units": po.units,
        "first_po_cash": first_order_cash,
        "years_of_y1_demand": po.units / y1_units if y1_units else 0,
        "peak_deficit": n["peak_deficit"],
        "min_cash": n["min_closing_cash"],
        "min_month": n["min_closing_month"],
        "y1_closing_stock": r.annual_last("stock_units")[0],
    }


if __name__ == "__main__":
    original = (A.MIN_ORDER_UNITS, A.ORDER_ROUNDING_UNITS)
    rows = []
    for moq, label in CASES:
        rows.append((label, run_case(moq)))
    A.MIN_ORDER_UNITS, A.ORDER_ROUNDING_UNITS = original

    print(f"{'Scenario':<42} {'1st PO':>9} {'Cash out':>11} {'x Y1 demand':>12} "
          f"{'Min cash':>11} {'Peak deficit':>13}")
    print("-" * 102)
    for label, d in rows:
        flag = "" if d["min_cash"] > 0 else "   << INSOLVENT"
        print(f"{label:<42} {d['first_po_units']:>9,} R{d['first_po_cash']:>10,.0f} "
              f"{d['years_of_y1_demand']:>11.1f}x R{d['min_cash']:>10,.0f} "
              f"R{d['peak_deficit']:>12,.0f}{flag}")

    print()
    print("Read: 'x Y1 demand' is how many years of year-one sales the first")
    print("order buys. Anything above ~2x means the pre-seed is funding dead")
    print("stock rather than the business — and mints have a 24-month shelf")
    print("life, so stock bought in month 3 expires in month 27.")
    print()
    print("The pre-seed is R{:,.0f}. Any row with a negative or near-zero minimum".format(
        A.FUNDING_ROUNDS[0][2]))
    print("cash needs either a bigger round, a smaller MOQ, or a different supplier.")
