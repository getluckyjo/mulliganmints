# Channel strategy — South Africa

*How we get tins into hands. Sources in [`sources.md`](sources.md).*

> **Scope note.** [Decision 0008](../docs/decisions/0008-bootstrap-route.md)
> adopted the bootstrap route, which stops the ladder at bars and DTC. **National
> retail and export are out of the plan** — the global route is licensing, not
> shipping. The retail and export sections below are kept because the analysis
> stands and they are the channels to reopen if the pilot beats plan, but they
> are not funded and not scheduled.

---

## 1. The channel ladder

We deliberately enter through the hardest, smallest, highest-margin channel and
work outward. That order is not sentiment — it is how brand permission is built.

```
YEAR 1              YEAR 2              YEAR 3 ONWARD
Golf clubs      →   + Bars & pubs   →   + Brand licensing, territory by territory
(direct)            (direct)            (no inventory, no working capital)
+ DTC
                    ── not in the plan: national retail, export ──
```

Every step down the ladder trades margin for reach:

| Channel | Net to us | Gross margin | Status |
| --- | ---: | ---: | --- |
| Direct to consumer | R35.00 | 71% | **In the plan.** Highest margin, best data |
| Golf clubs (direct) | R24.25 | 58% | **In the plan.** The brand engine. |
| Bars (direct) | R24.25 | 58% | **In the plan.** |
| Bars (via distributor) | R18.00 | 43% | Not in the plan — we keep the margin |
| Grocery & pharmacy | R21.00 | 51% | **Out.** R1.4m of listing fees, 65-day terms |
| Export FOB SA | R15.50 | 34% | **Out.** We licence the brand instead |

## 2. Channel one — golf clubs

### The universe

| | |
| --- | --- |
| Affiliated golf clubs in SA | **~460** (GolfRSA) |
| Registered golfers | **139,496** (2024, up from 136,923 in 2023) |
| Rounds played | **4.2 million** in 2024, +0.81% year on year |
| Busiest month | March (410,509 rounds), then December, January, February |
| Busiest club | Country Club Johannesburg — 72,914 rounds across two courses |
| Serviceable universe (our estimate) | **~300** clubs with a pro shop doing real traffic |

### Why this channel first

**It is small enough to actually win.** Three hundred clubs is a list. It fits on
a spreadsheet. A single rep can physically visit every club in Gauteng in a month.
You cannot say that about the bar trade or about retail.

**The buyer is not a category manager.** A club pro decides what goes on the
counter, and decides in one conversation. There is no listing fee, no planogram,
no six-month review cycle.

**4.2 million rounds is 4.2 million occasions.** At one tin per 100 rounds — a
deliberately conservative rate — that is 42,000 tins a year from the golf channel
alone before any brand awareness exists.

**And it is where the story gets made.** Every piece of content, every photograph,
every bit of the brand's evidence comes from this channel. It is a marketing
budget disguised as a sales channel.

### The plan

| | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Active clubs (exit) | 110 | 220 | 280 | 295 | 300 |
| Tins per club per month | 32 | 38 | 44 | 50 | 55 |

32 tins a month is roughly **one tin a day per club.** That is the number to
challenge in the pilot. If a club cannot sell one tin a day, the model does not
work — and we will know that within 90 days, for R30,000 of stock.

### How it sells in the club

Three placements, in order of value:

1. **Pro shop counter** — a 12-tin display box next to the till. Impulse at the
   point of paying for the round.
2. **Halfway house** — same display, higher intent.
3. **Cart / starter** — sampling, not selling. This is where the tin gets into
   the fourball's hands and the joke gets told for us.

Plus the two we should chase deliberately: **corporate golf days** (branded tins
in the goodie bag — a high-volume, high-margin, low-effort order) and **club
championship / member's day** stock.

## 3. Channel two — bars, pubs and restaurants

### The universe

Public data here is poor. Stats SA's food-and-beverage survey draws from a
sampling frame of **5,178 formal enterprises**, and that frame counts restaurants
and coffee shops far better than it counts bars. There is no published national
count of on-consumption liquor licences — licensing is provincial and the data is
not consolidated.

**Our working number: ~2,500 metro premium on-consumption outlets** we could
plausibly service. It is an estimate, flagged as one, and it should be replaced
with a real list built from the first distributor conversation.

### The plan

| | Y1 | Y2 | Y3 | Y4 | Y5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Active outlets (exit) | 140 | 450 | 900 | 1,300 | 1,600 |
| Tins per outlet per month | 20 | 22 | 25 | 28 | 30 |
| Share served by distributors | 0% | 15% | 45% | 70% | 80% |

### The distributor transition — and why it is non-negotiable

By year 5 the plan services roughly **3,000 outlets**. You cannot do that with
five reps; the arithmetic of 600 outlets per rep does not work in any FMCG
business. So from year 2 the bar trade moves progressively onto third-party
distributors, and we accept **R18.00 instead of R24.25** per tin for the
privilege.

That single decision costs about R6 a tin and is why year 5 gross margin lands at
67% rather than 72%. It is modelled explicitly
(`DISTRIBUTOR_SHARE_OF_BARS_BY_YEAR` in `assumptions.py`) because a plan that
ignores it is a plan that either overstates margin or understates headcount.

**Golf stays direct forever.** It is 300 outlets, it is the brand, and it is
worth the cost to serve.

## 4. Channel three — grocery and pharmacy retail *(out of the plan)*

> Not funded and not scheduled under decision 0008. Kept as the analysis to
> revisit if the pilot beats plan and a growth round is raised.

Would enter month 19 at the earliest. Not before.

**Why not earlier.** Retail is where challenger brands go to die early. Listing
fees, promotional grids, 60–75 day terms and returns will consume a pre-seed
round before a brand has any pull. We go to a Checkers or Clicks buyer only once
we can put golf-channel sell-through data and a real social audience on the table.

**Modelled cost of entry** (in `RETAIL_LISTING_FEES`): R180k for a regional pilot
chain in month 19, then R450k, R450k and R320k for national grocery and pharmacy
accounts. That is **R1.4m of listing investment** across the plan, and it is real
money that first-time plans routinely forget.

**Economics.** RSP R42.99, retailer takes ~32%, trade spend and co-op advertising
~13%, leaving us **R21.00**. Debtor terms 65 days — the working capital hit is as
significant as the margin hit.

The natural first doors, in order: **Dis-Chem and Clicks** (they already sell
Fisherman's Friend at R28.99, they understand a premium mint, and the pharmacy
front-of-store is an impulse environment), then **Checkers** (Sixty60 is a
genuinely useful launch surface for a giftable tin), then **Spar** (store-level
decisions make regional pilots easy).

## 5. Channel four — direct to consumer

Small in volume, disproportionate in value.

- **R35.00 net per tin** — our highest margin by a distance.
- It is the only channel where we own the customer data.
- It is where the merch, the multi-packs, the gift boxes and the corporate orders
  live.
- It is the proof-of-demand artefact a retail buyer actually respects.

Modelled at 400 tins/month in year 1 rising to 4,000 by year 5. Deliberately
conservative — it is a lever we can pull harder if content lands.

## 6. What we are deliberately not doing

- **No forecourt or convenience at launch.** Wrong price point, wrong impulse,
  and the trade terms are brutal.
- **No mass advertising.** Ever, probably. Altoids took 25% of the US market
  without it.
- **No airline, hotel or hospitality amenity channel in the first three years.**
  It is a real opportunity for a tin brand, and it is a distraction until the
  core works.
- **No SKU proliferation.** **One flavour at launch** — strong peppermint. Each
  additional flavour is a separate 800 kg batch: 22,944 tins and R231,000 of
  stock against a 24-month shelf life. Flavour two gets chosen on 90-day
  sell-through, not on instinct. The temptation to add a second before the first
  is selling is the most expensive mistake available to us.
