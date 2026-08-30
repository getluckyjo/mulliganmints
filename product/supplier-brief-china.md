# Supplier brief and sample evaluation — Suntak Foods Manufacturing Co., Ltd

*Status: samples of tins and mints inbound. This document carries what we need
from them, what we ask for next, and how we score what arrives.*

---

## 1. Where we are

**We have a price.** Suntak quoted on 29 August 2026
(`quotes/suntak-quotation-2026-08-29.pdf`), valid 30 days — so it lapses
**28 September 2026**.

| | Quoted |
| --- | --- |
| **FOB Shantou** | **USD 0.465 per tin** |
| Product | 35g sugar-free STRONG PEPPERMINT in a classic hinged tin |
| Tin | **96 × 61.5 × 21 mm** |
| Mints | 1g round tablets, 13.5mm dia — **35 per tin** |
| Shelf life | 24 months |
| Packing | 12 tins/display box, 8 boxes/carton = 96/carton |
| Carton | 41.5 × 22.5 × 21.0 cm, 0.02 CBM, 7.6 kg gross |
| Container | 1,400 cartons = **134,400 tins per 20GP** |
| Production | **60 days** after artwork confirmed **and** deposit received |
| Payment | **50% T/T deposit in advance, balance before shipment from factory** |
| Samples | Tin USD 250/design · OEM formula USD 200/flavour |
| Embossing | USD 300 mould charge **per embossed position** |
| LCL | USD 200 handling charge if the order totals under USD 5,000 |

### What that changed in the plan

**The packing spec matched our model exactly** — 96 per carton, 1,400 cartons
per 20GP, 60-day production. Nothing to revise there.

Two things moved against us:

1. **FOB is USD 0.465, not the USD 0.44 we estimated** — 5.7% higher. Landed
   cost per tin goes from R9.58 to **R10.29** including wastage.
2. **Payment is 50/50, not the 30/70 we assumed**, and the balance falls due
   *before the goods leave the factory* rather than against the bill of lading.
   More cash out, earlier.

Together those take cumulative five-year EBITDA from R18.25m to **R16.65m** and
push the month-19 low point down to **R574,000**. The plan still works. It has
less slack than it had.

## 2. The MOQ — answered, and it sets the launch decision

**Suntak's MOQ is 800 kg of candy per recipe.** At 35 g of candy per tin:

| | |
| --- | --- |
| 800 kg ÷ 35 g | **22,857 tins** |
| Rounded to whole 96-tin cartons | **22,944 tins** (239 cartons, 803 kg) |
| As a share of a 20GP | 17% per flavour |
| FOB cost per flavour | USD 10,669 ≈ **R170,700** |

It is a batch minimum on a recipe, so it applies **per flavour**. Worth confirming
with Damita in one line, because it is the difference between a R231,000 and a
R681,000 launch order.

### What that means for the launch

We sell 24,520 tins in the whole of year one. Each flavour we launch with is
another 22,944 tins bought before a single one has been sold:

| | First order | Cash out | Years of Y1 demand | Min cash | Verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| **1 flavour — peppermint only (chosen)** | 22,944 | **R231k** | **0.9x** | R574k | **Chosen** |
| 2 flavours | 45,888 | R463k | 1.9x | R574k | Fine |
| 3 flavours — the earlier plan | 68,832 | R681k | 2.8x | R449k | Affordable |
| *For reference: a full 20GP* | 134,400 | R1.33m | 5.5x | −R57k | Insolvent |

*(Reproduce with `python3 finance/model/sensitivity_moq.py`.)*

**The good news: the pre-seed covers all three flavours.** This is not the crisis
it looked like before the MOQ was known.

> **Decided: we launch with strong peppermint only** (decision 0006). One flavour
> buys almost exactly one year of demand for R231,000 instead of nearly three
> years for R681,000, and it is the only flavour Suntak has actually quoted.
> Flavours two and three get chosen on 90-day sell-through and added at a reorder
> around month 9.

**The judgement call is how many untested bets to place at once.** Three flavours
means committing R681,000 to three flavour guesses before we have a single day of
sell-through data. Mints carry a 24-month shelf life, so a flavour that does not
move is roughly **R236,000 of stock that expires** — and we would not find out
which one until month 12 or later.

Launching with strong peppermint only is the conservative read: it is the hero
product, it is the only flavour Suntak has actually quoted, it ties up R231,000
instead of R681,000, and it buys almost exactly one year of demand. Flavours two
and three can then be chosen on evidence rather than instinct, at a second order
placed around month 9.

Against that: three flavours gives a golf club a proper display, makes the range
look like a brand rather than a trial, and a single-SKU display box is a weaker
proposition on a pro shop counter. It is a real trade-off, not an obvious call.

**The model is set to a single launch flavour** (`LAUNCH_FLAVOURS = 1` in
`assumptions.py`). Change that one number to re-run the plan on a wider launch.

## 3. What we still need from Suntak — the RFQ

### Pricing — mostly still open
1. **Volume breaks.** We have one price at one volume. Ask for FOB per tin at
   30,000 / 60,000 / 134,400 / 250,000 / 500,000 annual units. Our model
   extrapolates the higher tiers from this single quote and that is a guess.
2. ~~MOQ~~ — answered: **800 kg of candy per recipe = 22,944 tins per flavour.**
   Confirm in writing that it is per flavour and not a total across the order.
3. **Price for spearmint and the third flavour.** Only strong peppermint is quoted.
4. ~~Tooling and plate charges~~ — answered: USD 250/tin design, USD 200/OEM
   flavour, USD 300 per embossed position. Still ask whether these are refunded
   against volume.
5. Price impact of the sweetener options in `product-spec.md` §5
6. Price impact of matte varnish and additional spot colours
7. ~~Price validity~~ — answered: 30 days, so **this quote lapses 28 September
   2026.** Ask what it takes to hold it, and what the mechanism is for raw
   material price movement after that.

### Specification
8. Full **tin dieline** with bleed and safe areas — this still blocks the brand work
9. ~~Tin dimensions~~ — answered: 96 × 61.5 × 21 mm
10. ~~Tablet count~~ — answered: 1g tablets, 13.5mm dia, 35 per tin
11. Full ingredient declaration and nutritional data **per 100g and per serving** —
    including **which sweetener**, which the quote does not name and which we
    need before the label can be drafted
12. ~~Shelf life~~ — answered: 24 months. Confirm storage conditions.
13. Allergen statement and cross-contamination controls on the line
14. Menthol / peppermint oil loading — and whether they can go stronger than
    their standard. **We want this genuinely strong**, and "STRONG PEPPERMINT"
    on a quote sheet is not a specification.

### Compliance — non-negotiable
14. **Certificate of Analysis** for the production batch
15. **Food-grade certification for the tin's interior lacquer**, compliant with SA
    and EU food contact requirements
16. Factory certifications: HACCP, ISO 22000, BRC or equivalent
17. Confirmation they can produce to a label meeting SA R146 requirements
18. Health certificate / free sale certificate for export to South Africa

### Commercial
20. **Payment terms — push back.** They want 50% deposit and the balance before
    the goods leave the factory. Ask for 30/70 with the balance against the bill
    of lading. That single change is worth roughly R60,000 of working capital on
    a 30,000-unit order and considerably more later.
21. ~~Production lead time~~ — answered: 60 days after artwork **and** deposit.
    Note it starts on the deposit, so a slow payment is a slow delivery.
22. ~~Port~~ — answered: FOB **Shantou** (not Shanghai or Shenzhen, which is
    what our freight estimate was based on). Confirm sailing schedules and
    whether Shantou needs transhipment to Durban or Cape Town.
23. Whether they will hold safety stock of tins against a rolling forecast — this
    is how we get the 60-day production window down.

## 4. What we should be careful about

- **Do not let the supplier's reference artwork influence the brand.** The
  quotation sheet's "Always Fresh" design is a spec illustration. It is not a
  design reference and PJ Offner should not see it as one.
- **Get a second quote.** One supplier is not a supply chain, and we now have a
  real specification to quote against — 35g, 96 × 61.5 × 21 mm tin, 1g tablets,
  96 per carton. Put it to at least two other manufacturers before committing to
  tooling. The published OEM landscape has hundreds of capable Chinese suppliers,
  several with MOQs low enough for a pilot. Do this **before 28 September**, so
  the comparison is live while the Suntak quote still stands.
- **Duty is levied on the FOB customs value**, so every dollar saved on FOB saves
  us 1.25 rand-equivalents of landed cost, not 1.00. Negotiating FOB is worth
  25% more than it looks.
- **Sub-container orders lose the container economics.** Our first order of
  30,000 tins is 313 cartons — about a quarter of a 20ft. LCL freight and
  clearing carry roughly a 35% penalty per unit, which the model accounts for.
  Worth asking whether consolidating the first two orders into one shipment is
  cheaper overall.

## 5. Ordering plan (base case)

Single-flavour launch — one 800 kg batch per order:

| PO | Placed | Arrives | Units | Notes |
| --- | --- | --- | --- | --- |
| 1 | **Month 3** | Month 7 | 22,944 | 1 × MOQ. Launch stock, ~1 year of Y1 demand. |
| 2 | Month 5 | Month 9 | 22,944 | Still on forecast — placed before launch |
| 3 | Month 8 | Month 12 | 22,944 | First order placed on real sell-through |
| 4 | Month 10 | Month 14 | 22,944 | Candidate slot for flavour two |

Order sizes are whole multiples of the 22,944-tin batch, because you cannot buy
1.4 batches of candy.

**Note the freight consequence.** A single-flavour order is 17% of a container,
so early shipments carry the LCL penalty — the model applies roughly 35% on
freight and clearing until order sizes pass 60,000 units around month 24. That is
about R100,000 across the plan, and it is the real cost of the single-SKU launch.
Worth asking Suntak whether consolidating two batches into one shipment is
cheaper than two quarter-container sailings.

**The first PO cannot be placed before month 3, and that gate is real.**
Suntak's 60-day clock starts on artwork confirmation *and* deposit, which is
exactly the gate the model enforces. Nothing
can be printed until PJ Offner has delivered production-ready packaging artwork
(month 2, week 6 of his 8-week schedule) and the label has been reviewed against
R146. Printing 30,000 tins to an unreviewed label is not a risk worth taking to
save a month. The model enforces this rather than assuming it away.

Order-to-shelf lead time is modelled at **4 months**: 2 months production,
1 month transit (18–28 days China to Durban/Cape Town), 0.5 months clearing and
Port Health. Target forward cover is 3.5 months. Month 3 plus four months is why
the first sale is in **month 7**.

That lead time is the reason working capital is tight in months 15–20. Every week
we can take out of it is cash back on the balance sheet — and the two weeks most
easily won are at the front, by having the dieline in hand before PJ starts so
artwork and tooling can run in parallel.

## 6. Sample evaluation scorecard

Score every sample 1–5. Do it with at least three people, at least one of whom
plays golf regularly and at least one of whom does not.

### The mints

| Criterion | Score | Notes |
| --- | --- | --- |
| Strength on first contact | | Is it *actually* strong? This is the product. |
| Strength duration | | How long does the effect last? |
| Flavour quality | | Clean peppermint, or chemical? |
| Aftertaste | | Especially relevant if sweetened with stevia |
| Tablet integrity | | Does it crumble in the tin? |
| Dissolve time | | Should last a hole, not a swing |
| Mouthfeel | | Smooth or chalky |
| Size in the mouth | | |

### The tin

| Criterion | Score | Notes |
| --- | --- | --- |
| Weight and feel in the hand | | Does it feel premium or cheap? |
| Hinge action | | Opens one-handed? Stays shut in a bag? |
| Print quality | | Sharpness, colour density, registration |
| Rattle | | A tin that rattles in a backswing is a problem |
| Size in a pocket | | |
| Would you keep it empty? | | **The question that matters** |
| Stackability on a counter | | |
| Durability | | Drop it. Sit on it. Leave it in a hot car. |

### The verdict

- [ ] Proceed as specified
- [ ] Proceed with changes (list them)
- [ ] Re-sample
- [ ] Find another supplier

## 7. Before any money moves

- [ ] Second and third supplier quotes obtained on the same spec
- [ ] Factory certifications received and verified
- [ ] Food-grade lacquer certification received
- [ ] Trademark filed in South Africa (`legal/ip-trademark-strategy.md`)
- [ ] Label reviewed against R146 by a compliance consultant
- [ ] Import requirements confirmed with a clearing agent
- [ ] Payment terms and Incoterms agreed in writing
- [ ] Supply agreement signed, with the product spec attached as a schedule
