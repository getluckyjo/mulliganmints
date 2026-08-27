# Deal notes — PJ Offner

**Internal. Do not send to PJ.** Background for Johannes before signing the term
sheet at `term-sheet-pj-offner.md`.

---

## What 10% actually costs

The model budgeted **R150,000 cash** for the brand identity. Ten percent of the
company is worth considerably more than that on paper.

On the plan's own funding assumptions — R3.5m pre-seed at, say, a R14m pre-money
valuation — **10% is about R1.4m of paper value.** Roughly nine times the cash
alternative.

That is not automatically a bad deal, and it is worth being clear about why:

**In favour**
- **It costs no cash in the year cash is the binding constraint.** R150k is 4% of
  the pre-seed round, and months 15–20 are the tightest in the plan.
- PJ carries real risk. The shares may be worth nothing, and he is paid last.
- A designer with equity behaves differently from a designer with an invoice.
  He answers the phone in year three when a licensee needs the brand book
  extended.
- **The brand is the asset.** The year-4 licensing line is 95% margin and needs no
  working capital. Having the person who built the brand invested in that outcome
  is worth something real.

**Against**
- 10% is a lot for a defined, one-off deliverable. Founders regret this more often
  than they regret paying cash.
- It is permanent. Cash is a transaction; equity is a relationship with everyone
  who comes after.
- Every future investor sees a 10% holder who is not operating in the business.
  It gets asked about.

**The honest summary: it is a defensible trade, and it is a generous one.** The
term sheet is built so that generosity buys the right things — vesting, clean IP,
and clarity that future work is paid.

## The four things to hold firm on

**1. IP assignment as a condition of the final tranche.** Non-negotiable, and the
term sheet explains why openly rather than hiding it in legalese. Without clean
title there is no licensing business, which is most of the value in years 4 and 5.
This protects PJ's 10% as much as it protects yours.

**2. Vesting.** The shares are issued on day one — PJ is a real shareholder
immediately, which is what he is negotiating for — but the company can buy back
the unvested portion for R1 if the work stops. Without this, a wordmark delivered
in week three costs you a tenth of the company.

**3. No dilution protection.** PJ dilutes alongside you, round for round. The
illustrative table in clause 7 shows him at ~5.8% after two rounds. **Show him
that table before he signs, not after.** A shareholder who is surprised by
dilution in year two is a problem you created in year one.

**4. Future work is paid.** This deal covers the brief. New flavour artwork,
campaigns, a packaging refresh, licensee collateral — all separate and paid. Get
this in writing now, while everyone is friendly.

## What you can give away cheaply

These cost almost nothing and matter a lot to a designer:

- **Attribution.** Credit him properly, everywhere. It is free.
- **Portfolio rights** from launch. He needs the work in his book.
- **Right of first refusal** on future design work for three years. You would
  probably use him anyway.
- **Pre-emptive rights.** He almost certainly will not exercise them, and offering
  them signals you are treating him as a real shareholder.

## Where PJ will probably push back

| He asks for | Reasonable response |
| --- | --- |
| All 10% vesting on signature | No. Offer to raise tranche 1 from 20% to 25–30% instead. |
| Anti-dilution protection | No. Nobody except institutional investors gets this, and giving it would poison the pre-seed. |
| A board seat | No at 10%. Offer observer status at an annual shareholder update. |
| Shorter lock-up than 24 months | Negotiable. 12–18 months is fine if it matters to him. |
| Narrower restraint | It is already narrow — pressed mints only. Hold it. |
| A small cash component too | Reasonable to consider. See below. |

## If 10% feels like too much on reflection

Three alternatives, in order of how much they change the deal:

1. **7.5% plus R75,000 cash.** Splits the difference. Costs 2% of the pre-seed.
2. **10% with a buy-back right** — the company may repurchase 3–5% at fair market
   value within 24 months. Gives you a way to tidy the cap table before a Series A
   if you need to.
3. **10% with a larger scope.** If he is getting a tenth of the company, the brief
   could reasonably include the launch campaign, the first year's social
   templates, and a packaging refresh — turning a one-off into a two-year
   relationship for the same equity.

**Option 3 is the one worth thinking about.** It does not reduce what PJ gets. It
increases what you get for the same price, and it is an easier conversation than
asking him to take less.

## Consequences for the model

`finance/model/assumptions.py` has been updated: the two R75,000 PJ Offner cash
lines are removed and replaced with a R25,000 disbursements allowance for fonts,
stock, proofs and printing.

- Setup costs fall from **R558,000 to R433,000**
- The pre-seed requirement is unchanged at R3.5m — the saved cash goes into the
  working capital buffer, which is where the plan is tightest

**Not modelled:** the 10% dilution itself. The model forecasts the business, not
the cap table. The dilution table in clause 7 of the term sheet is the right place
for that, and it is illustrative.

## Before you sign

- [ ] Trade mark clearance searches run — **before PJ starts**, not after
      (`ip-trademark-strategy.md` §3). Finding a blocking mark after R1.4m of
      equity has moved is an expensive way to learn.
- [ ] Company incorporated with CIPC
- [ ] Your own tax advice on section 8C, and tell PJ to get his — the tax lands on
      him, and it lands when restrictions lift rather than when he has cash
- [ ] An attorney reviews the definitive documents. The term sheet is written to
      be signable and clear; the Subscription and Shareholders Agreement is not
      something to draft yourself.
- [ ] Show PJ the dilution table and talk him through it in person
