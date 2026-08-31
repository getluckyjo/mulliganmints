# The funded plan — scale comparator, not the plan of record

> **This is no longer the plan.** [Decision 0008](../docs/decisions/0008-bootstrap-route.md)
> adopted the bootstrap route: **R1m, once**, golf and bars only, brand licensed
> globally rather than exported. See [`bootstrap-plan.md`](bootstrap-plan.md).
>
> This document is kept as the answer to *"what would it take to go faster?"* —
> R15.5m of capital, national retail, export inventory, and roughly half the
> company. It reaches R43.6m of year-5 revenue at a **lower** EBITDA margin than
> the bootstrap route, and it is the option to revisit if the 90-day pilot beats
> plan materially.

*Narrative accompaniment to [`outputs/model-summary.md`](outputs/model-summary.md).
All figures base case, ZAR, excluding VAT.*

---

## 1. The shape of it

| | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tins sold | 24,520 | 183,100 | 554,640 | 1,136,725 | 1,790,588 |
| Net revenue | R0.62m | R4.71m | R13.28m | R26.78m | R43.63m |
| Gross margin | 59% | 63% | 63% | 63% | 65% |
| EBITDA | −R1.46m | −R0.43m | R0.53m | R5.41m | R12.59m |
| EBITDA margin | — | — | 4% | 20% | 29% |
| Closing cash | R1.46m | R12.04m | R10.15m | R13.00m | R22.41m |

Cumulative five-year EBITDA: **R16.7m.**

**First sale is month 7, not month 1.** Months 1–6 are brand, samples,
trademark, artwork, the first production order and shipping. The model enforces
the sequence rather than assuming it: no purchase order can be placed before PJ
Offner has delivered production-ready packaging artwork (month 2) and the label
has cleared its R146 review (month 3), and the order-to-shelf lead time is four
months on top of that. An investor will ask why revenue starts in month 7 — the
answer is that it cannot start earlier, and a plan that showed it starting
earlier would be wrong.

Three phases, and they are genuinely different businesses:

- **Years 1–2 — prove it.** Golf clubs and bars, direct, in one or two provinces.
  Roughly 250 outlets by the end of year 1. The output of this phase is not
  profit; it is *evidence*: sell-through per outlet per month, by channel, by
  month, in writing.
- **Year 3 — scale it.** National retail listings, distributors take over the bar
  trade, first export container. The year the business stops being a project.
- **Years 4–5 — licence it.** Export at volume, and the brand starts earning
  money without shipping anything.

## 2. Unit economics — the whole business on one line

| ZAR per tin | |
| --- | ---: |
| **FOB Shantou (USD 0.465 @ 16.00)** — quoted | **7.44** |
| Sea freight | 0.47 |
| Marine insurance | 0.04 |
| **Import duty — 25% of FOB customs value** | **1.86** |
| Clearing and inland | 0.28 |
| **Landed cost** | **10.08** |
| Plus 2% wastage allowance | **10.29** |
| | |
| Net price, golf & bars direct | **24.25** |
| **Gross profit** | **13.96 (58%)** |
| Less logistics and commission | (2.08) |
| **Contribution per tin** | **11.88 (49%)** |

The FOB line is now a real quote, not an estimate — Suntak Foods, 29 August
2026, valid 30 days. It came in **5.7% above** the USD 0.44 we had modelled.
Freight and clearing per tin are higher than the earlier table because the first
order is a quarter-container and carries the LCL penalty.

A club buys a 12-tin display box for **R291 ex-VAT** and sells it for **R540
including VAT**. That is a clean, explainable proposition on a pro shop counter.

**Note the duty line.** At 25% of FOB, import duty is R1.86 of a R10.08 landed
cost — 18% of what the product costs us. Every US cent negotiated off the FOB
price is worth 1.25 cents of landed cost. Negotiating the supplier price is
worth 25% more than it looks — which is exactly why the 2.5 US cents Suntak came
in above our estimate cost R1.6m of cumulative EBITDA, not R1.3m.

## 3. Break-even — the number to argue about

At the month-12 cost base:

- Fixed costs (salaries + overheads): **R122,500/month**
- Marketing: **R63,333/month**
- Contribution per direct tin: **R11.88**

**Break-even is ~15,600 tins a month** including marketing, or ~10,300 excluding
it. At 38 tins per outlet per month that is roughly **410 active outlets.**

The year-1 plan exits with about 250. So break-even lands in **month 21** — early
year 2, not year 1. The model agrees: first EBITDA-positive month is 21.

**This is the most important sanity check in the plan.** If venues sell through
at half the modelled rate, break-even needs twice the outlets, and no amount of
marketing spend fixes it — it is an arithmetic problem, not a demand problem.
Which is exactly why the 90-day pilot measures sell-through per outlet before we
spend anything else.

## 4. Capital

| Round | Month | Amount | For |
| --- | ---: | ---: | --- |
| **Pre-seed** | 1 | **R3.5m** | Brand, first production runs, SA proof of concept |
| **Seed** | 20 | **R12.0m** | National retail rollout, distributor network, export entry |

### Why R3.5m and not R2.5m

The model was first run with a R2.5m pre-seed. It went **cash-negative in month
24** — the business ran out of money three months before the growth round could
plausibly close. The unfunded peak cash deficit in the base case is **R5.57m in
month 33.**

R3.5m is what it takes to reach a fundable milestone without a bridge.

### Use of the pre-seed

| | |
| --- | --- |
| Trademark, artwork, content, website, launch event | R388k |
| First production order (FOB, freight, insurance) | R226k |
| Import duty and clearing on the first order | R61k |
| Salaries, months 1–12 | R522k |
| Marketing, months 1–12 | R380k |
| Overheads and logistics, months 1–12 | R528k |
| **Second and third production orders + working capital buffer** | **balance** |

**PJ Offner takes 10% of the company instead of a fee** for the brand identity,
packaging and guidelines, and carries his own costs — see
`legal/term-sheet-pj-offner.md`. That takes the entire R150,000 brand line out of
a round where cash is the binding constraint. The brand remains the single
highest-leverage asset in the plan: it is what a licensee buys in year 4.

### The tightest point in the plan

The base case's lowest cash balance is **R574,000 in month 19** — immediately
before the growth round lands. That is roughly three weeks of runway.

**The growth round must be *closed* by month 19, which means started by month
14.** Not "we'll raise when we need it". Month 14.

## 5. Scenarios

| | Bear | Base | Bull |
| --- | ---: | ---: | ---: |
| Volume vs base | 45% | 100% | 155% |
| Year 5 revenue | R17.70m | R43.63m | R68.59m |
| Year 5 EBITDA | −R0.19m | R12.59m | R25.70m |
| Year 5 EBITDA margin | −1% | 29% | 37% |
| Cumulative 5-yr EBITDA | −R5.92m | R16.65m | R43.82m |
| First EBITDA-positive year | never | 3 | 2 |
| Unfunded peak cash deficit | R8.60m | R5.57m | R3.36m |

The scenarios flex volume, price, supplier cost **and the hiring plan** — in the
bear case hires slip six months, marketing is cut 45% and overheads are held 20%
leaner, because that is what an operator would actually do.

### What the bear case is telling us

Bear is not "a bit slower". It is **a different business**: EBITDA-negative for
**all five years**, cumulatively −R5.92m, needing R8.60m of capital that it
cannot service. On the quoted supplier price it no longer reaches break-even
inside the plan at all.

The honest reading: **if venue sell-through lands at half the plan, do not raise
the growth round.** Hold headcount flat, stay in golf and DTC where margins are
60–73%, run it as a profitable niche brand at 200,000 tins a year, and take the
licensing route later off a smaller but real base. That is a decent outcome. It
is not a venture outcome, and the plan should say so out loud rather than pretend
the downside is just a slower version of the upside.

## 6. Where the model is most likely to be wrong

Ranked by how much damage each one does:

1. **Sell-through per outlet.** Everything scales off it. No external benchmark
   exists. **±50% here is ±R20m of year-5 revenue.**
2. **Which second flavour, and when.** We launch with strong peppermint only
   (decision 0006). The MOQ is 800 kg of candy per recipe — **22,944 tins per
   flavour, R231,000 a time** — so each flavour added is a real commitment made
   against a 24-month shelf life. Adding the wrong one is ~R236,000 of stock
   that expires. Choose it on the 90-day sell-through data, not on instinct.
   ~~FOB cost~~ is now quoted at USD 0.465 and no longer a guess, though the
   volume breaks above 150,000 units a year are still extrapolated from that one
   price point.
3. **Rand.** Modelled at 16.00 depreciating 4% a year. We buy in dollars and sell
   in rand, so a sharp depreciation hits COGS immediately and price increases lag
   by a year. A move to R20/USD adds roughly R1.75 to landed cost — more than a
   year of price increases.
4. **Retail entry cost.** R1.4m of listing fees is modelled. Real listing costs
   at a national grocer can be higher, and returns and promotional grids can eat
   more than the 13% trade spend assumed.
5. **Year 4–5 EBITDA margin.** 26–31% is at the top of the range for branded
   confectionery. It depends on the distributor transition working and on the
   licensing line arriving. **Treat 20–25% as the conservative read.**

## 7. What we are not modelling

Deliberate omissions, so nobody thinks they were missed:

- **Merchandise.** Caps, towels, ball markers. Real revenue for a brand like
  this, and excluded because it is speculative.
- **Debt or trade finance.** Import finance against confirmed orders would
  materially reduce the equity requirement and should be explored before the
  growth round.
- **Contract manufacture in South Africa.** Would remove 25% duty and the freight
  line entirely, at the cost of higher unit conversion cost and a large minimum
  run. Worth modelling seriously once annual volume passes ~500,000 tins.
- **Any exit.** No terminal value, no multiple. The question of what the brand is
  worth belongs in `pitch/investor-narrative.md`, not in the operating model.
