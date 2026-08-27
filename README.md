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
| Supplier | Suntak Foods Manufacturing Co., Ltd (China) — samples of tins and mints inbound |
| Brand | PJ Offner engaged for **10% equity, not a fee** — brief in `brand/brand-brief-pj-offner.md`, terms in `legal/term-sheet-pj-offner.md` |
| Capital ask | R3.5m pre-seed, then R12m growth round by month 20 |
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
| Landed cost per tin | **R9.58** |
| Net price per tin, golf & bars | **R24.25** (RSP R45 incl VAT) |
| Gross margin, direct channels | **60%** |
| Break-even | **~14,000 tins/month** — around month 21 |
| Year 5 revenue | **R43.6m** on 1.79m tins |
| Capital required | **R3.5m** pre-seed + **R12m** growth round |

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

1. **Supplier FOB price per tin.** Modelled at $0.44 at launch volume. Unverified.
   The Suntak quote replaces it.
2. **Sell-through per venue per month.** Modelled at 32 tins in year 1 rising to 55.
   Unverified. The first 90 days of real venue data replaces it.

Everything else in this repository is downstream of those two.
