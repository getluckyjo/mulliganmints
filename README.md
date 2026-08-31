# Mulligan Mints

**Like it never happened.**

A strong pressed mint in a tin. Irish-inflected heritage brand, modern golf-culture
edge. Proving the concept through golf courses and bars across South Africa, then
taking the brand global by licence or by export.

---

## Where things stand

| | |
| --- | --- |
| Stage | Pre-launch. Research complete, brand not yet commissioned, no stock ordered. |
| Product | 35g sugar-free pressed mints in a printed hinged tin (supplier spec in `product/`) |
| Supplier | Suntak Foods (Shantou, China) — **quoted USD 0.465/tin FOB, 29 Aug 2026, valid 30 days**. Samples inbound. |
| Brand | PJ Offner engaged for **10% equity, not a fee** — brief in `brand/brand-brief-pj-offner.md`, terms in `legal/term-sheet-pj-offner.md` |
| Capital ask | **Two routes.** Funded: R3.5m pre-seed then R12m by month 20. Bootstrap: **R1m for 10% equity plus R2/tin until repaid**, with trade finance from year 2 — see `finance/bootstrap-plan.md` |
| Next decisions | See `docs/decisions/` |

## Repository map

```
docs/          One-pager, decision log
research/      Market, competitors, channels, global route — with sources
brand/         Creative brief for PJ Offner, verbal identity, asset store
product/       Product & packaging spec, supplier brief and sample evaluation
finance/       The 5-year model (Python) and its outputs (xlsx + markdown)
gtm/           Go-to-market, 90-day launch plan, pricing and trade terms
legal/         SA compliance checklist, IP strategy, PJ Offner term sheet
pitch/         Investor narrative
ops/           Risk register
```

## The business in six numbers (base case)

| | |
| --- | --- |
| Landed cost per tin | **R10.29** (Suntak quote, 29 Aug 2026) |
| Net price per tin, golf & bars | **R24.25** (RSP R45 incl VAT) |
| Gross margin, direct channels | **58%** |
| Break-even | **~15,600 tins/month** — around month 21 |
| Year 5 revenue | **R43.6m** on 1.79m tins |
| Capital required | **R3.5m** pre-seed + **R12m** growth round |

Full detail: [`finance/outputs/model-summary.md`](finance/outputs/model-summary.md)
and the workbook at `finance/outputs/mulligan-mints-5yr-model.xlsx`.

**There is a second route, and it is the stronger one.**
[`finance/bootstrap-plan.md`](finance/bootstrap-plan.md) models a single **R1m
raise — 10% equity plus R2 from every tin until the R1m is repaid** — with trade
finance carrying stock from year 2. Golf and bars in South Africa, no retail, no
export, and the brand **licensed** globally rather than shipped. EBITDA-positive
in year 2, **R11.9m of revenue and R4.5m of EBITDA by year 5** at a 38% margin,
with **80% of the company retained**. Licensing is 51% of year-5 EBITDA. The two
plans are identical for the first 12 months, so the choice does not have to be
made yet.

## Rebuilding the numbers

```bash
pip install openpyxl
cd finance/model && python3 build_outputs.py
```

All assumptions live in `finance/model/assumptions.py`. Change them there —
never in the spreadsheet.

## The two numbers that decide everything

1. ~~Supplier FOB price per tin.~~ **Answered: USD 0.465 FOB Shantou**, 5.7%
   above the USD 0.44 we had modelled. Re-costed through the whole plan.
2. **Sell-through per venue per month.** Modelled at 32 tins in year 1 rising to
   55. Still unverified — no benchmark for it exists anywhere. The first 90 days
   of real venue data replaces it.

And one new one, which arrived with the quote:

3. ~~How many flavours to launch with.~~ **Decided: strong peppermint only**
   (decision 0006). The MOQ is 800 kg of candy per recipe — 22,944 tins,
   R231,000 a flavour — so a single-SKU launch buys almost exactly one year of
   demand instead of nearly three. Flavours two and three get chosen on real
   sell-through.
