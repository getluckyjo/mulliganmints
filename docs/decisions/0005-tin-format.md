# 0005 — 35g tin as the launch format

**Date:** August 2026 · **Status:** Provisional — confirm on samples

## Context

The supplier's standard specification is a 35g sugar-free mint in a regular
hinged tin, 12 per display box, 96 per carton, 134,400 per 20ft container.

## Comparison

| | Weight | SA price | Per gram |
| --- | ---: | ---: | ---: |
| Fisherman's Friend | 25g bag | R28.99 | R1.16 |
| **Mulligan Mints** | **35g tin** | **R45.00** | **R1.29** |
| Altoids | 50g tin | R60–80 grey import | R1.20–1.60 |

## Decision

Launch at 35g. It sits between the two reference brands and needs no defending —
a per-gram price only 11% above Fisherman's Friend, with the premium carried by
the format and the brand rather than by the gram.

## Status: provisional

Confirm on the physical samples. Two things could change it:

1. **The tin feels wrong in the hand.** If 35g is bulky in a pocket or rattles in
   a golf bag, a smaller tin is better.
2. **Sell-through comes in below ~20 tins/club/month in the pilot.** A R45 price
   point may simply be wrong, and a smaller tin at R30 is a real alternative —
   see the decision gates in `gtm/launch-plan-90-day.md`.

## Consequences

- Everything in `finance/model/assumptions.py` is priced off this format.
  Changing it changes the whole cost stack and the price architecture.
- The decision must be final before PJ Offner produces packaging artwork and
  before tooling charges are paid.
