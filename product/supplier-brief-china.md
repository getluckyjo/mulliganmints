# Supplier brief and sample evaluation — Suntak Foods Manufacturing Co., Ltd

*Status: samples of tins and mints inbound. This document carries what we need
from them, what we ask for next, and how we score what arrives.*

---

## 1. Where we are

Suntak has quoted a standard specification: 35g sugar-free mints in a regular
hinged tin, 12 tins per display box, 8 boxes per carton, 1,400 cartons per 20ft
container. Samples of both the tins and the mints are on their way.

**We do not yet have a price.** Everything financial in this repository uses an
estimated FOB of **USD 0.44 per tin at launch volume**, derived from published
OEM ranges. That number is the single largest uncontrolled variable in the plan.
Replacing it with a real quote is the highest-value thing we can do this month.

## 2. What we need from Suntak — the RFQ

### Pricing
1. **FOB price per tin** at 30,000 / 50,000 / 100,000 / 250,000 / 500,000 annual
   units, per SKU and blended
2. **MOQ per SKU** and total MOQ across three SKUs
3. **Tooling, plate and setup charges** — and whether they are refunded against
   volume
4. Price impact of the sweetener options in `product-spec.md` §5
5. Price impact of emboss, matte varnish, and additional spot colours
6. Price validity period and the mechanism for raw material price movement

### Specification
7. Full **tin dieline** with bleed and safe areas — this blocks the brand work
8. Exact tin dimensions and weight
9. Tablet count per tin and tablet dimensions
10. Full ingredient declaration and nutritional data **per 100g and per serving**
11. Confirmed shelf life and storage conditions
12. Allergen statement and cross-contamination controls on the line
13. Menthol / peppermint oil loading — and whether they can go stronger than
    standard. **We want this genuinely strong.**

### Compliance — non-negotiable
14. **Certificate of Analysis** for the production batch
15. **Food-grade certification for the tin's interior lacquer**, compliant with SA
    and EU food contact requirements
16. Factory certifications: HACCP, ISO 22000, BRC or equivalent
17. Confirmation they can produce to a label meeting SA R146 requirements
18. Health certificate / free sale certificate for export to South Africa

### Commercial
19. Payment terms — we have modelled 30% deposit, 70% against bill of lading
20. Production lead time from artwork approval to goods ready
21. Nominated port and whether they quote FOB or CIF
22. Whether they will hold safety stock of tins against a rolling forecast

## 3. What we should be careful about

- **Do not let the supplier's reference artwork influence the brand.** The
  quotation sheet's "Always Fresh" design is a spec illustration. It is not a
  design reference and PJ Offner should not see it as one.
- **Get a second quote.** One supplier is not a supply chain. Quote at least two
  other manufacturers on the same specification before committing to tooling.
  The published OEM landscape has hundreds of capable Chinese suppliers, several
  with MOQs low enough for a pilot.
- **Duty is levied on the FOB customs value**, so every dollar saved on FOB saves
  us 1.25 rand-equivalents of landed cost, not 1.00. Negotiating FOB is worth
  25% more than it looks.
- **Sub-container orders lose the container economics.** Our first order of
  30,000 tins is 313 cartons — about a quarter of a 20ft. LCL freight and
  clearing carry roughly a 35% penalty per unit, which the model accounts for.
  Worth asking whether consolidating the first two orders into one shipment is
  cheaper overall.

## 4. Ordering plan (base case)

| PO | Placed | Arrives | Units | Notes |
| --- | --- | --- | --- | --- |
| 1 | **Month 3** | Month 7 | 30,000 | MOQ floor. Launch stock. |
| 2 | Month 6 | Month 10 | 30,000 | |
| 3 | Month 9 | Month 13 | 30,000 | |
| 4 | Month 11 | Month 15 | 30,000 | |

**The first PO cannot be placed before month 3, and that gate is real.** Nothing
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

## 5. Sample evaluation scorecard

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

## 6. Before any money moves

- [ ] Second and third supplier quotes obtained on the same spec
- [ ] Factory certifications received and verified
- [ ] Food-grade lacquer certification received
- [ ] Trademark filed in South Africa (`legal/ip-trademark-strategy.md`)
- [ ] Label reviewed against R146 by a compliance consultant
- [ ] Import requirements confirmed with a clearing agent
- [ ] Payment terms and Incoterms agreed in writing
- [ ] Supply agreement signed, with the product spec attached as a schedule
