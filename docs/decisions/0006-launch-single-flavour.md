# 0006 — Launch with strong peppermint only

**Date:** August 2026 · **Status:** Accepted

## Context

Suntak's minimum order is **800 kg of candy per recipe**. At 35 g of candy per
tin that is 22,857 tins, or **22,944 rounded up to whole 96-tin cartons**. It is a
batch minimum on a recipe, so it applies per flavour.

The plan of record was three launch flavours. That would mean a **68,832-tin
launch order costing R681,000** — against year-one demand of about 24,500 tins.

## Options

| | First order | Cash out | Years of Y1 demand |
| --- | ---: | ---: | ---: |
| **1 flavour — strong peppermint** | 22,944 | R231k | 0.9x |
| 2 flavours | 45,888 | R463k | 1.9x |
| 3 flavours | 68,832 | R681k | 2.8x |

The R3.5m pre-seed covers all three. Affordability was not the constraint.

## Decision

**Launch with strong peppermint only.** Flavours two and three are chosen on real
sell-through data and added at a reorder, not guessed at before launch.

## Why

- **It buys almost exactly one year of demand.** 22,944 tins against ~24,500 in
  year one. Three flavours buys 2.8 years before we know anything.
- **It is the only flavour Suntak has actually quoted.** Spearmint and a third
  flavour are unpriced and each carries a USD 200 sample charge.
- **Mints have a 24-month shelf life.** A flavour that does not move is roughly
  **R236,000 of stock that expires**, and we would not find out which one until
  month 12 or later.
- **It is the hero product.** The brand's whole promise is that the mint is
  genuinely strong. Strong peppermint *is* the proposition; spearmint is a
  line extension.
- **R450,000 of pre-seed stays liquid** in the phase where cash is tightest.

## What we give up

**A single-SKU display box is a weaker proposition on a pro shop counter.** A
three-flavour display looks like a brand; twelve identical tins look like a
trial. This is a real cost and it is the main argument against.

Two things mitigate it:

1. **The 12-tin display box is designed to be a hero unit**, not a range unit —
   one flavour presented well rather than three presented thinly.
2. **PJ still designs the full flavour-coding system**, so flavours two and three
   drop in without a redesign when the evidence arrives.

We also lose some breadth in the pitch: "one flavour" reads smaller than "a
range". The counter is that it reads *disciplined*, and the reasoning above is
the answer to the question.

## Consequences

- `LAUNCH_FLAVOURS = 1` in `finance/model/assumptions.py`
- Launch order 68,832 → **22,944 tins**; cash out R681k → **R231k**
- Month-19 low point improves from R449,000 to **R574,000**
- Supplier sample costs drop about R20,000 — one tin design and one formula
  rather than three
- **PJ's scope changes**: tin artwork for one SKU at launch, but the full
  flavour-coding system still delivered. The term sheet is updated accordingly
  and is not yet signed.
- Early reorders are quarter-container shipments and carry the LCL freight
  penalty until volume passes ~60,000 units per order around month 24

## Revisit when

- 90-day sell-through data exists (`gtm/launch-plan-90-day.md`). The second
  flavour should be chosen then, on evidence.
- If clubs consistently ask for a second flavour before that, take the signal —
  a reorder at month 9 can carry it.
