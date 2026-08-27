# Finance

## Layout

```
model/
  assumptions.py     ← every number lives here. Change this, not the spreadsheet.
  model.py           ← the 60-month engine: P&L, cashflow, inventory, VAT, tax
  build_outputs.py   ← renders the workbook and the markdown summary
outputs/
  mulligan-mints-5yr-model.xlsx    ← 9-sheet workbook (generated)
  model-summary.md                 ← the same numbers in markdown (generated)
5-year-plan.md       ← the narrative: what the numbers mean and where they break
```

## Rebuilding

```bash
pip install openpyxl
cd finance/model && python3 build_outputs.py
```

Both files in `outputs/` are generated. **Never edit them by hand** — the next
rebuild overwrites your changes and, worse, silently desynchronises the numbers
quoted across the rest of the repository.

## What the model does

- 60 monthly periods across five channels plus a licensing line
- Landed cost built properly: FOB → freight → insurance → **25% duty on the FOB
  customs value** → clearing, with a volume-based FOB curve and an LCL penalty
  on sub-container orders
- Inventory driven by a reorder policy with a 4-month order-to-shelf lead time
  and 3.5 months of forward cover — stock-outs are modelled, not assumed away
- Supplier payments split 30% on order / 70% against bill of lading
- Debtor days by channel; VAT accrued and settled two-monthly; company tax with
  assessed-loss carry-forward capped at 80% of taxable income
- Three scenarios that flex volume, price, FOB cost **and the hiring plan** —
  because a bear case that hires the base-case headcount is not a forecast

## Reading the outputs

Start with `outputs/model-summary.md`. The workbook has the detail: monthly P&L,
monthly cashflow, the purchase order schedule, and a funding sheet.

## Health warnings

1. **FOB cost is an estimate** (USD 0.44/tin at launch volume). The Suntak quote
   replaces it. A 10c/tin miss moves year-5 gross profit by roughly R3m.
2. **Sell-through per venue is an estimate** (32 tins/club/month rising to 55).
   No external benchmark exists. The 90-day pilot replaces it.
3. **Year 4–5 EBITDA margins of 26–31% are at the top of what a branded
   confectionery business earns.** They depend on the distributor transition
   working and on the licensing line arriving. A more conservative read of years
   4 and 5 is 20–25%. Treat the difference as the value of the licensing thesis,
   not as an operating assumption.
