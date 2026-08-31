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

## The deal

**R1m for 10% of the equity, plus the R1m returned out of R1 from every tin sold,
until repaid.**

| | |
| --- | --- |
| Cash in | R1,000,000, once, at the start |
| Equity | 10% — permanent. **Founders 81%, PJ Offner 9%, investor 10%** (PJ dilutes pro rata). |
| Repayment | R1 per tin, from the first sale |
| Tins required | 1,000,000 — **repaid in month 50** |
| Dividends | None until capital is repaid, then 50% of profit above a R1.5m cash buffer |

## Why R1m is enough

**Break-even is about 3,750 tins a month.** The model turns EBITDA-positive in
**month 9**, and the lowest cash balance across five years is **R300,273**. A business that breaks even there does not need R15m; it needs
enough to buy stock and survive its first year.

Three things make the small raise sufficient:

1. **A distributor's sales team from day 1.** Their feet, their routes, their
   existing relationships. We pay R4.25 a tin for it and avoid a field force we
   could never have afforded.
2. **Get Lucky Golf Club's access to 30 courses and 600+ promotions a year.**
   The golf channel starts warm, and the sampling engine is already paid for.
   A tin in a golfer's hand costs R10.29 and converts better than advertising.
3. **The distributor warehouses the stock.** We take delivery of a container and
   move it once, to one address. They hold it, pick it and deliver to every
   outlet. No 3PL storage, no pick-and-pack, no courier to hundreds of venues —
   and **one invoiced customer instead of three hundred**, which removes the
   credit control, route accounting and field-sales software a direct model
   needs. Logistics run at **R0.20 a tin** rather than R1.35, and overheads at
   30% of a conventional base.
4. **Branding, packaging, website and content cost nothing in cash.** PJ Offner
   takes 10% equity for the identity; the founders build the rest.
5. **Trade finance from the third order**, placed in month 8 — by then the
   distributor has been selling since month 7 and two shipments have landed and
   cleared. That timing is what makes R1m sufficient.

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
| Operating costs | (398,675) | (1,103,690) | (2,243,763) | (3,566,536) | (5,066,166) |
| **EBITDA** | **(121,923)** | **878,913** | **2,559,378** | **5,854,881** | **9,492,700** |
| EBITDA margin | — | 25% | 33% | 42% | **46%** |
| Trade finance interest @ 17% | (18,215) | (95,732) | (159,136) | (238,633) | (315,308) |
| Tax | (4,224) | (178,033) | (648,065) | (1,516,387) | (2,477,896) |
| **Net profit** | **(143,475)** | **612,897** | **1,752,177** | **4,099,861** | **6,699,496** |

**Cumulative five-year EBITDA R18.66m. Net profit R13.02m.**

> **On that 46% year-5 EBITDA margin.** It is at the very top of what a branded
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
| Operating costs paid | (398,675) | (1,103,690) | (2,243,763) | (3,566,536) | (5,066,166) |
| **Trade finance drawn** | **451,506** | **1,493,184** | **2,365,208** | **3,570,927** | **4,529,367** |
| **Trade finance repaid** | **(127,575)** | **(1,186,696)** | **(2,051,988)** | **(3,183,845)** | **(4,333,194)** |
| **Investor revenue share (R1/tin)** | **(22,275)** | **(145,110)** | **(287,775)** | **(463,480)** | **(81,360)** |
| VAT settled | 88,941 | (145,003) | (483,443) | (930,347) | (1,470,916) |
| Tax paid | (4,224) | (178,033) | (648,065) | (1,516,387) | (2,477,896) |
| Investor capital | 1,000,000 | — | — | — | — |
| **Net cashflow** | **368,634** | **175,141** | **1,351,771** | **3,514,808** | **3,584,586** |
| **Closing cash** | **368,634** | **543,775** | **1,895,546** | **5,410,354** | **8,994,940** |
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

By year 5 licensing is **24% of EBITDA** on 11% of revenue — no inventory, no
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
| Dividend in year 5 (10% of R3.35m declared) | R334,975 |
| 10% equity at exit — year-5 EBITDA R9.49m | see below |

### Exit at month 60

Equity value = enterprise value + surplus cash − trade finance − capital owed.

| Multiple | Equity value | Founders (81%) | After CGT | PJ (9%) | Investor (10%) | IRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **4x** | 44,594,487 | 36,121,534 | **29,619,658** | 4,013,504 | 4,459,449 | 49% |
| **6x** | 63,579,887 | 51,499,709 | **42,229,761** | 5,722,190 | 6,357,989 | 58% |
| **8x** | 82,565,288 | 66,877,883 | **54,839,864** | 7,430,876 | 8,256,529 | 65% |

Founders' CGT at 18% effective, holding personally
([0007](../docs/decisions/0007-hold-shares-personally.md)).

**Every multiple is an estimate and nobody has offered anything.** This is
arithmetic on top of a plan whose volumes are still assumptions — a way of seeing
how value is shared, not a valuation.

## If sell-through comes in at half

Every number above rests on tins per outlet per month, and nobody has that
benchmark. So the model carries a downside built on this plan's own structure —
`bootstrap_bear` — where the distributor's sell-through lands at **55% of plan**,
smaller orders lose the volume tiers on the FOB curve, the distributor pushes us
on price, hires slip a year and marketing is cut to what the cash allows.

| ZAR | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tins sold | 12,251 | 79,810 | 158,276 | 254,914 | 350,903 |
| Revenue | 267,152 | 1,849,000 | 3,898,891 | 6,652,316 | 9,695,128 |
| EBITDA | (227,995) | 536,001 | 1,095,845 | 1,911,292 | 2,779,223 |
| Net profit | (238,024) | 414,104 | 730,467 | 1,282,366 | 1,879,286 |
| Closing cash | 479,829 | 701,413 | 1,201,509 | 2,217,409 | 4,096,208 |

**The business survives on the same R1m.** The lowest cash balance is R453,865 in
month 15 — higher than the plan's own R300,273, because a slower business buys
less stock. It is EBITDA-positive from month 12, and cumulative five-year EBITDA
is R6.09m against the plan's R18.66m.

**What the downside costs is time, not the company.** Two things go:

- **Licensing disappears entirely.** Nobody licenses a brand that has not proved
  it moves, and licensing is 24% of year-5 EBITDA in the plan. This is the real
  cost of a slow start — not the lost SA margin, the lost licence.
- **The investor is not repaid inside five years.** At R1 a tin, R143,845 of the
  R1m is still outstanding at month 60, and because capital is not repaid **no
  dividend is ever declared.**

That is the honest shape of it: a business that survives and grows on a slower
clock, an investor who waits longer and forgoes the dividend, and a global
licensing story that has to wait for proof it did not get in year 2.

**Note on the other scenarios.** The workbook also carries *funded base*, *funded
bear* and *funded bull*. Those belong to the R15m plan in `finance/5-year-plan.md`
and they carry grocery and export channels this route deliberately switches off.
`bootstrap_bear` is this plan's downside; funded bear is not.

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

**The plan rests on trade finance arriving with the third order**, placed in
month 8. If a bank will not lend until year 2, month-12 cash falls to R16,432 and
the raise has to be R1.25m. **Get an indicative term sheet before committing to
the R1m number.**

**One customer is now most of our debtor book.** The admin saving from a single
invoiced client is real, and so is the concentration: if the distributor does not
pay, there are no other receivables to fall back on. Credit-check them properly
and consider credit insurance on the balance.

**Year-5 EBITDA of 46% is at the top of the credible range.** 30–35% is the
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
