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
| Capital ask | **Two routes.** Funded: R3.5m pre-seed then R12m by month 20. Bootstrap: **R1m for 10% equity plus R1/tin until repaid**, with trade finance from year 2 — see `finance/bootstrap-plan.md` |
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

## The business in six numbers

| | |
| --- | --- |
| Landed cost per tin | **R10.29** (Suntak quote, 29 Aug 2026) |
| Net price per tin, golf & bars | **R24.25** (RSP R45 incl VAT) |
| Gross margin, direct channels | **58%** |
| **Break-even** | **~2,700 tins/month** — EBITDA-positive in month 11 |
| Year 5 | **R11.9m revenue · R4.5m EBITDA at 38%** |
| **Capital required** | **R1,000,000, once** |

**The plan is the bootstrap route** —
[`finance/bootstrap-plan.md`](finance/bootstrap-plan.md), adopted in
[decision 0008](docs/decisions/0008-bootstrap-route.md). One R1m raise: 10%
equity plus R1 from every tin until repaid, with trade finance carrying stock
from year 2. Golf clubs, bars and DTC in South Africa — no national retail, no
export — and the brand **licensed** globally rather than shipped. Licensing is
51% of year-5 EBITDA. Founders keep 80%.

The fully funded alternative (R3.5m then R12m, reaching R43.6m of year-5 revenue)
stays modelled in [`finance/5-year-plan.md`](finance/5-year-plan.md) as the scale
comparator. It is not the plan.

Full detail: [`finance/outputs/model-summary.md`](finance/outputs/model-summary.md)
and the workbook at `finance/outputs/mulligan-mints-5yr-model.xlsx`.

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
