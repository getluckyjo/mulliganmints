# The plan — prove it here, licence it everywhere

> **This is the plan of record**, adopted in
> [decision 0008](../docs/decisions/0008-bootstrap-route.md) and reshaped by
> [0009](../docs/decisions/0009-distributor-led.md). The fully funded alternative
> is kept as a scale comparator in [`5-year-plan.md`](5-year-plan.md).

*One R1m raise. No growth round. **A distributor with a sales team covers golf
clubs and bars from day 1**; DTC stays ours. The brand is licensed globally
rather than exported. Figures generated from `finance/model/assumptions.py`,
scenario `bootstrap`. Rebuild with `cd finance/model && python3 build_outputs.py`.*

---

> ## ⚠ One thing to resolve before this goes in a dataroom
> **Month-12 cash is R16,432.** The distributor-led ramp buys far more stock in
> year 1 than a direct plan would, and trade finance does not arrive until month
> 13. Two fixes:
>
> | | Minimum cash |
> | --- | ---: |
> | R1m, trade finance month 13 *(as modelled)* | **R16,432** ⚠ |
> | **R1m, trade finance month 10** | **R249,718** |
> | R1.25m, trade finance month 13 | R266,432 |
>
> **Getting the facility three months earlier is worth as much as R250,000 of
> equity and costs nothing.** With a distributor selling from month 7 there is a
> real trading record and landed stock to secure against by month 10. Tracked as
> R-18 in the risk register.

---

## The deal

**R1m for 10% of the equity, plus the R1m returned out of R1 from every tin sold,
until repaid.**

| | |
| --- | --- |
| Cash in | R1,000,000, once, at the start |
| Equity | 10% — permanent. Founders 80%, PJ Offner 10%. |
| Repayment | R1 per tin, from the first sale |
| Tins required | 1,000,000 — **repaid in month 50** |
| Dividends | None until capital is repaid, then 50% of profit above a R1.5m cash buffer |

## Why R1m is enough

**Break-even is about 4,500 tins a month.** The model turns EBITDA-positive in
**month 10**. A business that breaks even there does not need R15m; it needs
enough to buy stock and survive its first year.

Three things make the small raise sufficient:

1. **A distributor's sales team from day 1.** Their feet, their routes, their
   existing relationships. We pay R4.25 a tin for it and avoid a field force we
   could never have afforded.
2. **Get Lucky Golf Club's access to 30 courses and 600+ promotions a year.**
   The golf channel starts warm, and the sampling engine is already paid for.
   A tin in a golfer's hand costs R10.29 and converts better than advertising.
3. **Branding, packaging, website and content cost nothing in cash.** PJ Offner
   takes 10% equity for the identity; the founders build the rest.

## The numbers

| ZAR | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| **Tins sold** | 22,275 | 145,110 | 287,775 | 463,480 | 638,005 |
| Revenue — golf clubs | 252,000 | 1,481,760 | 2,460,780 | 3,343,916 | 3,933,500 |
| Revenue — bars | 190,969 | 1,623,234 | 4,228,907 | 8,282,763 | 13,152,203 |
| Revenue — DTC | 63,000 | 396,900 | 694,575 | 972,405 | 1,276,282 |
| **Licensing** | — | — | **300,000** | **1,200,000** | **2,280,000** |
| **Net revenue** | **505,969** | **3,501,894** | **7,684,262** | **13,799,084** | **20,641,984** |
| Gross profit | 276,752 | 1,982,603 | 4,803,141 | 9,421,416 | 14,558,866 |
| Gross margin | 55% | 57% | 63% | 68% | 71% |
| Operating costs | (452,844) | (1,208,606) | (2,393,026) | (3,775,285) | (5,340,630) |
| **EBITDA** | **(176,092)** | **773,997** | **2,410,115** | **5,646,131** | **9,218,236** |
| EBITDA margin | — | 22% | 31% | 41% | **45%** |
| Trade finance interest @ 17% | — | (81,965) | (159,136) | (238,633) | (315,308) |
| Tax | (2,967) | (136,336) | (607,764) | (1,460,024) | (2,403,790) |
| **Net profit** | **(179,059)** | **555,696** | **1,643,215** | **3,947,473** | **6,499,137** |

**Cumulative five-year EBITDA R17.87m. Net profit R12.47m.**

> **On that 45% year-5 EBITDA margin.** It is at the very top of what a branded
> FMCG business earns, and it needs three things to go right at once: the
> distributor delivering the outlet counts, licensing arriving on schedule, and a
> cost base with no field force. **A conservative read of years 4 and 5 is
> 30–35%.** Treat the difference as the value of the distributor-plus-licensing
> model, not as an operating assumption.

### Cashflow

| ZAR | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Receipts from customers (incl VAT) | 367,317 | 3,675,755 | 8,259,752 | 14,972,615 | 22,657,384 |
| Payments to supplier | (814,353) | (1,729,847) | (2,722,258) | (4,077,941) | (5,154,826) |
| Import duty & clearing | (147,387) | (403,273) | (656,610) | (1,023,384) | (1,315,699) |
| Operating costs paid | (452,844) | (1,208,606) | (2,393,026) | (3,775,285) | (5,340,630) |
| **Trade finance drawn** | — | **1,493,184** | **2,365,208** | **3,570,927** | **4,529,367** |
| **Trade finance repaid** | — | **(862,765)** | **(2,051,988)** | **(3,183,845)** | **(4,333,194)** |
| **Investor revenue share (R1/tin)** | **(22,275)** | **(145,110)** | **(287,775)** | **(463,480)** | **(81,360)** |
| VAT settled | 88,941 | (145,003) | (483,443) | (930,347) | (1,470,916) |
| Tax paid | (2,967) | (136,336) | (607,764) | (1,460,024) | (2,403,790) |
| Investor capital | 1,000,000 | — | — | — | — |
| **Net cashflow** | **16,432** | **456,034** | **1,262,959** | **3,390,602** | **3,521,459** |
| **Closing cash** | **16,432** ⚠ | **472,466** | **1,735,425** | **5,126,028** | **8,647,487** |
| *Investor capital outstanding* | *977,725* | *832,615* | *544,840* | *81,360* | *nil* |

**Inventory dominates the raise, not startup costs.** The money buys tins before
anyone buys them from us. From year 2 the bank funds that at 17% and the equity
stays in the business.

## Route to market

**A distributor covers golf clubs and bars from day 1.** We sell at **R20.00 a
tin**; they sell to the venue at R24.25, which retails at R45 — an **18%
distributor margin**, thin because Get Lucky's access means we hand them warm
outlets rather than asking them to prospect cold. DTC stays ours at R35.

| Exit of year | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Golf clubs | 120 | 200 | 260 | 285 | 300 |
| Tins per club per month | 30 | 36 | 40 | 44 | 46 |
| Bars | 150 | 450 | 900 | 1,400 | 1,800 |
| Tins per bar per month | 15 | 17 | 19 | 21 | 23 |
| DTC per month | 300 | 900 | 1,500 | 2,000 | 2,500 |

Rates sit **below** what a founder-serviced outlet would deliver. A distributor
rep carries hundreds of lines and will not merchandise ours the way we would.
Reach is bought with depth — see [0009](../docs/decisions/0009-distributor-led.md).

**Headcount:** neither founder draws anything in year 1. R15,000 each from month
13, R25,000 from month 25, R35,000 from month 37. A trade marketing and key
accounts manager from month 31 to run the distributor relationship; a brand and
content lead from month 49. **No field reps — the distributor has the feet.**

## The licensing engine

| | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: |
| Territories live | 1 | 3 | 5 |
| Signing fees | 300,000 | 600,000 | 600,000 |
| Licensee net sales | — | 10,000,000 | 28,000,000 |
| Royalty at 6% | — | 600,000 | 1,680,000 |
| **Licensing revenue** | **300,000** | **1,200,000** | **2,280,000** |
| Licensing costs | (180,000) | (240,000) | (280,000) |

By year 5 licensing is **25% of EBITDA** on 11% of revenue — no inventory, no
COGS, no working capital.

> **Licensing is zero-inventory, not zero-input.** Trademarks must be registered
> in each territory before a licensee signs, agreements drafted, licensees found
> and travelled to, quality audited. That is **R820,000 across years 2–5**, and it
> lands before most of the royalties do.

**What a licensee is buying**, and what the SA years exist to build: registered
trademarks in their territory, PJ Offner's brand book, a proven product
specification, and documented sell-through by channel and by month.

> **The distributor now holds that sell-through data.** Contract for it
> explicitly — a licensee will want to see it, and "our distributor has it" is
> not an answer. Tracked as R-17.

## The investor's return

| | |
| --- | ---: |
| Capital returned at R1 a tin | R1,000,000 by **month 50** |
| Dividend in year 5 (10% of R3.25m declared) | R324,957 |
| 10% equity at exit — year-5 EBITDA R9.22m | see below |

### Exit at month 60

Equity value = enterprise value + surplus cash − trade finance − capital owed.

| Multiple | Equity value | Founders (80%) | After CGT | PJ (10%) | Investor (10%) | IRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **4x** | 43,103,433 | 34,482,747 | **28,275,852** | 4,310,343 | 4,310,343 | 49% |
| **6x** | 61,539,906 | 49,231,925 | **40,370,178** | 6,153,991 | 6,153,991 | 57% |
| **8x** | 79,976,378 | 63,981,103 | **52,464,504** | 7,997,638 | 7,997,638 | 64% |

Founders' CGT at 18% effective, holding personally
([0007](../docs/decisions/0007-hold-shares-personally.md)).

**Every multiple is an estimate and nobody has offered anything.** This is
arithmetic on top of a plan whose volumes are still assumptions — a way of seeing
how value is shared, not a valuation.

## What we would rather say up front

**The riskiest number is one nobody in the world has.** Tins per outlet per month
has no published benchmark. Get Lucky's 30 courses make the *access* real; they
do not make the *rate* real.

**The cost side is quoted; the revenue side is not.** R0.465 FOB, 25% duty,
800 kg minimum, 60-day production — all on a real supplier quote. Not one rand of
revenue is.

**One distributor holds every outlet we have.** If they deprioritise us among the
hundreds of lines they carry, we have no field force to fall back on. Contract
minimum performance and the data. Tracked as R-17.

**Month-12 cash is R16,432.** See the box at the top. This is fixable and it is
not yet fixed.

**Year-5 EBITDA of 45% is at the top of the credible range.** 30–35% is the
conservative read.

## What R1m actually buys

Four numbers that do not currently exist anywhere:

1. Tins sold per outlet per month
2. Reorder rate by channel
3. Sell-through by placement — pro shop counter vs halfway house vs bar
4. Cost to acquire an outlet

Plus a registered brand, a proven supply chain, roughly 270 active outlets by the
end of year one, and the sell-through evidence a global licensee will want before
signing anything.
