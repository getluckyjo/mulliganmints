# Dataroom — structure and build plan

*How the investor dataroom is organised, what goes in each folder, what does not
go in at all, and what still has to be created before it opens.*

---

## The principle

**A R1m raise does not need a 200-document dataroom.** It needs about twenty
documents that answer, in order: what is this, is the market real, can these two
people do it, do the numbers work, what could go wrong, and what am I buying.

Anything that does not answer one of those questions makes the room harder to
read, not more convincing.

**The files live in this repository and are published from it.** Do not maintain
a second copy — the numbers change, and a stale dataroom is worse than a thin
one. Export to the room when a document is final, and re-export when the model
is rebuilt.

## The structure

```
00  Start here
01  The opportunity
02  The plan
03  The numbers
04  Product & supply
05  Brand
06  Team & track record
07  The deal
08  Legal, IP & risk
```

### 00 · Start here

| Document | Source | Status |
| --- | --- | --- |
| One-page summary | `docs/00-one-pager.md` | ✅ Ready |
| Investor narrative — the full argument | `pitch/investor-narrative.md` | ✅ Ready |
| Index and reading order | `dataroom/index.md` | ✅ Ready |

*If someone reads only one document it will be the one-pager. If they read two,
the second is the narrative. Everything else is evidence for those two.*

### 01 · The opportunity

| Document | Source | Status |
| --- | --- | --- |
| Market analysis | `research/01-market-analysis.md` | ✅ Ready |
| Competitor landscape | `research/02-competitor-landscape.md` | ✅ Ready |
| Channel strategy — South Africa | `research/03-channel-strategy-sa.md` | ✅ Ready |
| The global licensing route | `research/04-global-opportunity.md` | ✅ Ready |
| Sources — every external figure cited | `research/sources.md` | ✅ Ready |

*`sources.md` is worth more than it looks. Most decks assert; being able to click
through to where every number came from is unusual and it builds trust fast.*

### 02 · The plan

| Document | Source | Status |
| --- | --- | --- |
| The plan — five years | `finance/bootstrap-plan.md` | ✅ Ready |
| Go-to-market | `gtm/go-to-market.md` | ✅ Ready |
| Sales & distribution strategy | `gtm/sales-and-distribution-strategy.md` | ✅ Ready |
| 90-day launch plan | `gtm/launch-plan-90-day.md` | ✅ Ready |
| Pricing and trade terms | `gtm/pricing-and-trade-terms.md` | ✅ Ready |

### 03 · The numbers

| Document | Source | Status |
| --- | --- | --- |
| **Five-year model (workbook)** | `finance/outputs/mulligan-mints-5yr-model.xlsx` | ✅ Ready |
| Model summary | `finance/outputs/model-summary.md` | ✅ Ready |
| The funded alternative — scale comparator | `finance/5-year-plan.md` | ⚠️ Appendix only |

*The workbook carries the Assumptions, Unit economics, monthly P&L and cashflow,
Scenarios, Purchase orders and Exit sheets. It is the single most examined
document in the room — make sure the version in the room matches the last
rebuild.*

*On the funded alternative: including it proves we know what scale would cost. It
also invites "so why aren't you asking for that?" **Recommendation: appendix,
not front of room.***

> **On scenarios — get this right or the room reads backwards.** The workbook now
> carries five: **plan of record**, **bootstrap bear**, and then *funded base*,
> *funded bear*, *funded bull*. The last three belong to the R15m plan and carry
> grocery and export channels the bootstrap route deliberately switches off.
> **Bootstrap bear is this plan's downside; funded bear is not.** An investor who
> compares the plan against funded bear will read the downside as barely below
> the plan, which is false. The Scenarios sheet now says so on the sheet itself —
> do not remove that note.

### 04 · Product & supply

| Document | Source | Status |
| --- | --- | --- |
| Product specification | `product/product-spec.md` | ✅ Ready |
| Supplier quotation — Suntak, 29 Aug 2026 | `product/quotes/suntak-quotation-2026-08-29.pdf` | ⚠️ See note |
| Physical samples | — | ❌ Inbound |
| Product photography | — | ❌ Needs brand first |
| Second supplier quote | — | ❌ Not obtained |

> **On the Suntak quote.** It shows our exact landed cost. In a competitor's
> hands that is genuinely useful intelligence. **Consider holding it in an
> "on request" tier** rather than open in the room, and share it once someone is
> in real diligence. The unit economics table in the model tells the story
> without exposing the supplier's pricing.

### 05 · Brand

| Document | Source | Status |
| --- | --- | --- |
| Creative brief to PJ Offner | `brand/brand-brief-pj-offner.md` | ✅ Ready |
| Verbal identity and tone | `brand/naming-and-verbal-identity.md` | ✅ Ready |
| **Brand identity and packaging** | — | ❌ **PJ, 8 weeks** |
| Brand guidelines | — | ❌ PJ, with the identity |

*This folder is the weakest in the room until PJ delivers, and it is the folder
an investor will most want to see. **Do not open the dataroom before the identity
lands** — a mint brand with no brand is a hard read.*

### 06 · Team & track record

| Document | Source | Status |
| --- | --- | --- |
| Team and track record | `dataroom/06-team.md` | ⚠️ Drafted — needs founder confirmation |
| Founder headshots and LinkedIn links | — | ❌ To supply |
| Get Lucky access agreement | — | ❌ Nothing in writing |

> **This was the emptiest folder and it is the most important one.** At
> pre-revenue an investor is backing two people, not a spreadsheet. Two marketing
> executives, one with a beverage brand that sold 10m+ units across five
> countries and a golf activation platform already running 600 promotions a year
> across 30 courses — that is the strongest single asset in this raise.
>
> **The draft is written but it is not publishable yet.** Andrew's section is a
> template, not a profile, and every biographical claim carries a `[CONFIRM]`
> tag. Both founders must sign it off before the room opens — an invented CV in a
> dataroom is unrecoverable.

### 07 · The deal

| Document | Source | Status |
| --- | --- | --- |
| Deal terms, cap table, use of funds, exit | `dataroom/07-deal-terms.md` | ✅ Ready |
| Exit analysis — full waterfall | In the model workbook, "Exit" sheet | ✅ Ready |
| Subscription agreement | — | ❌ Only once terms are agreed |

*These used to live inside longer documents. They are now standalone — an
investor should be able to find the terms without reading a plan to get to them.
The cap table is **81% founders / 9% PJ Offner / 10% investor**: PJ takes 10%
first and is not anti-diluted, so this round dilutes him pro rata.*

### 08 · Legal, IP & risk

| Document | Source | Status |
| --- | --- | --- |
| Risk register | `ops/risk-register.md` | ✅ Ready |
| Decision log | `docs/decisions/` | ✅ Ready |
| IP and trademark strategy | `legal/ip-trademark-strategy.md` | ✅ Ready |
| SA compliance checklist | `legal/compliance-checklist-sa.md` | ✅ Ready |
| PJ Offner term sheet — signed | `legal/term-sheet-pj-offner.docx` | ⚠️ Drafted, unsigned |
| Company registration (CIPC) | — | ❌ Not incorporated |
| Trademark filing receipt | — | ❌ Not filed |
| **Distributor agreement or LOI** | — | ❌ **Nothing in writing** |
| Trade finance indicative term sheet | — | ❌ Not obtained |
| Get Lucky access agreement | — | ❌ Nothing in writing |

> **Include the risk register and the decision log.** Most founders would not.
> Eighteen scored risks with named mitigations, and nine decision records showing
> what was considered and rejected, say something about how this business is run
> that no amount of narrative can. It is a differentiator for a first raise.

## What does not go in the room

| | Why |
| --- | --- |
| `CLAUDE.md` | Internal working notes |
| `legal/pj-offner-deal-notes.md` | Internal — negotiating position on PJ's deal |
| `legal/pj-offner-covering-email.md` | Internal draft |
| **`product/supplier-brief-china.md`** | **Contains our negotiating position with Suntak** — where to push back on payment terms, what to ask for. Do not publish this. |
| `finance/model/*.py` | Model source. Available on request — it impresses a technical investor — but not in the room by default. |
| `finance/README.md`, `docs/decisions/README.md` | Internal navigation |

## The gap register

Ranked by what blocks the room opening.

| # | Gap | Owner | Blocks opening? |
| --- | --- | --- | --- |
| 1 | **Brand identity and packaging** | PJ Offner, ~8 weeks | **Yes** — a mint brand needs a brand |
| 2 | **Distributor agreement or LOI** | Johannes | **Yes** — it is the entire route to market and nothing is in writing |
| 3 | **Team page confirmed and signed off** — Andrew's section written, every `[CONFIRM]` verified | Johannes + Andrew | **Yes** — drafted at `dataroom/06-team.md`, not publishable until confirmed |
| 4 | ~~Deal terms, cap table, use of funds as standalone documents~~ | — | ✅ Done — `dataroom/07-deal-terms.md` |
| 5 | Company registered with CIPC | Johannes | Strongly advised |
| 6 | Trademark filed — SA classes 30 and 25 | Johannes | Strongly advised — file before publishing the brand anywhere |
| 7 | PJ term sheet signed | Johannes + PJ | Advised |
| 8 | Trade finance indicative term sheet | Johannes | No, but R-18 depends on it |
| 9 | Physical samples and product photography | Suntak, then PJ | No — but bring tins to every meeting |
| 10 | Get Lucky access on a written footing | Johannes | No — but an investor will ask, and the team page says so out loud |
| 11 | Founder headshots and LinkedIn links | Johannes + Andrew | No — but the room currently has no faces in it |
| 12 | Second supplier quote | Johannes | No — mitigates R-11 |

**Only one of the three blockers is a waiting task.** The brand waits on PJ; the
distributor LOI and the team sign-off are this week's work.

## Mechanics

**Use a view-only shared Drive folder, not a paid VDR.** At R1m a virtual
dataroom with watermarking and audit trails signals the wrong thing — it reads as
process theatre. A clean Drive folder with view-only links, one folder per
section, numbered so they sort correctly.

**Track who has access and when you granted it.** A simple sheet. It matters
later when you are trying to remember who saw which version.

**No NDA for the main room.** For a raise this size, asking friendly investors to
sign an NDA before they can read a one-pager costs more in goodwill than it
protects. Hold the supplier quote and any signed agreements behind a request
instead.

**Version the model.** The workbook is rebuilt whenever assumptions change.
Date-stamp the file in the room and re-export after every rebuild — an investor
finding two different year-5 numbers is the fastest way to lose a room.
