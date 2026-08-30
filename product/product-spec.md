# Product specification

*Working spec, v0.2 — updated against the Suntak quotation of 29 August 2026
(`quotes/suntak-quotation-2026-08-29.pdf`). Remaining "TBC" items are confirmed
against the physical samples when they land. This document becomes the master
spec attached to the supply agreement.*

---

## 1. Product

| | |
| --- | --- |
| Product | Sugar-free pressed mints |
| Net weight | **35g** per tin |
| Format | Pressed tablet ("compressed mint") |
| Sugar | Sugar-free — must test at **<0.5g/100g** to carry the claim under R146 |
| Sweetener | **TBC — decision required.** The quote says "sugar free" but does not name the sweetener. See §5 |
| Strength | High menthol/peppermint oil loading. Quoted as "STRONG PEPPERMINT" — confirm on samples that their "strong" is our strong. |
| Tablet | **1g per tablet, round, 13.5mm diameter → 35 tablets per tin** [SOURCE: quote] |
| Shelf life | **24 months** [SOURCE: quote] |
| Allergens | To be confirmed and declared. Confirm the line is free of nut cross-contamination. |

### Launch flavours

Three SKUs. **Not four.** Adding a flavour before the first three are selling is
the most expensive mistake available to us.

| SKU | Flavour | Rationale |
| --- | --- | --- |
| 1 | **Peppermint — extra strong** | The hero. This is the product. |
| 2 | **Spearmint** | The softer entry point; broadens the buyer base |
| 3 | **TBC — third flavour** | Candidates: aniseed, liquorice, wintergreen, honey-lemon. Decide on samples. Aniseed and liquorice both index strongly in the heritage strong-mint category (Fisherman's Friend's SA range carries both). |

**We launch with SKU 1, strong peppermint, only** — see
`docs/decisions/0006-launch-single-flavour.md`. Each flavour is its own 800 kg
batch: **22,944 tins, about R231,000**. Three at launch would have been R681,000
of stock against year-one demand of 24,520, with a 24-month shelf life. Spearmint
and the third flavour stay on this spec as planned line extensions, chosen on
90-day sell-through and added at a reorder around month 9. Suntak has in any case
only quoted strong peppermint.

## 2. Tin

| | |
| --- | --- |
| Type | Hinged-lid rectangular tin, printed tinplate ("classic tin can") |
| Dimensions | **96 × 61.5 × 21 mm** [SOURCE: quote] — **this unblocks PJ Offner's packaging artwork.** Still request the flat dieline with bleed and safe areas. |
| Printing | Offset on tinplate. Confirm spot colour count, whether an emboss is available, and whether a matte or gloss varnish is offered. |
| Finish | Decision required: matte reads more premium, gloss survives handling better |
| Food contact | Interior lacquer must be food-grade and compliant with SA and EU food-contact requirements. **Obtain certification.** |

### Questions for the supplier before artwork starts

1. Exact tin dieline — flat artwork template with bleed and safe areas
2. Maximum spot colours; is CMYK process available on tinplate?
3. Is embossing or debossing on the lid available, and at what tooling cost?
4. Matte vs gloss varnish options
5. Minimum type size that reproduces reliably
6. Tooling and plate charges, and whether they are refunded against volume

## 3. Packing

Per the Suntak specification sheet:

| | |
| --- | --- |
| Tins per display box | **12** |
| Display boxes per carton | **8** |
| **Tins per carton** | **96** |
| Carton cube | 0.02 CBM |
| Carton gross weight | 7.8 kg |
| Cartons per pallet | 90 |
| **Cartons per 20ft container** | **1,400** |
| **Tins per 20ft container** | **134,400** |

The **display box is the most important piece of retail collateral in the
business.** It is what sits on a pro shop counter and does the selling. It must be
designed as a display unit — front panel visible, tins presented, brand readable
from a metre away — not as a shipping carton with a logo on it.

## 4. Labelling

Full requirements in `legal/compliance-checklist-sa.md`. The label must carry:

- Product name and description
- Net weight (35g / 35g ℮)
- Full ingredient list in descending order
- **Sweetener declaration** — specific, by name, per R733/2012
- Nutritional information table
- Allergen declaration
- **Country of origin** — stated plainly and correctly
- Importer/distributor name and SA address
- Batch code and best-before date
- Barcode (GS1 South Africa — must be registered)

Two things to plan for now rather than discover later:

- **The "sugar-free" claim requires laboratory verification and a re-test every
  three years** under R146.
- **Draft R3337 proposes a mandatory front-of-pack warning logo for products
  containing artificial sweeteners.** If it is promulgated and we have used an
  artificial sweetener, we will need that logo on the tin. Leave physical room
  for it in the artwork, and let it inform the sweetener decision below.

## 5. The sweetener decision — needs making before artwork

This is a genuine fork, and it is a brand decision as much as a technical one.

| Option | Pros | Cons |
| --- | --- | --- |
| **Xylitol** | Natural-derived, dental benefit, clean taste, no artificial-sweetener warning logo under draft R3337 | More expensive; cooling effect interacts with mint flavour; laxative threshold requires a warning above certain intakes; **toxic to dogs** — relevant when the tin lives in a golf bag |
| **Sorbitol / isomalt** | Cheap, standard for pressed mints, good tablet integrity | Polyol laxative warning may apply |
| **Steviol glycosides** | Natural, no warning logo, clean label story | Aftertaste that is hard to hide even behind strong mint; usually needs a bulking agent anyway |
| **Aspartame / acesulfame-K** | Cheapest, strongest sweetness, technically simplest | **Almost certainly triggers the front-of-pack warning logo under draft R3337.** Consumer sentiment against artificial sweeteners is moving the wrong way. |

**Recommendation: xylitol or a xylitol/isomalt blend**, subject to cost and to
the samples tasting right. It keeps the label clean, avoids the artificial
sweetener warning logo, and gives us a dental-health story we can use without
making a medicinal claim. Confirm cost impact with the supplier — this may be
several US cents per tin, which is material at our margins.

## 6. Sample evaluation

When the Suntak samples arrive, score both the tins and the mints. Template in
`product/supplier-brief-china.md` §5. Do not skip this: it is the last cheap
moment to change the product.

## 7. Open decisions

| # | Decision | Blocks | Owner |
| --- | --- | --- | --- |
| 1 | ~~Tin dimensions~~ — **answered: 96 × 61.5 × 21 mm.** Flat dieline still needed | PJ Offner artwork | Supplier |
| 2 | ~~How many flavours at launch~~ — **decided: peppermint only** (0006). Which flavour comes second is now a month-9 decision, made on sell-through. | Reorder at ~month 9 | Johannes |
| 3 | Sweetener | Formula, label, cost, artwork | Johannes + supplier |
| 4 | Matte vs gloss | Artwork | Johannes + PJ |
| 5 | 35g vs a smaller premium format | Price architecture, everything | Johannes |

On #5: 35g is the supplier's standard and it is the right place to start. Worth
knowing that Altoids is 50g and Fisherman's Friend is 25g, so 35g sits between
them and needs no defending. Revisit only if the samples make the tin feel wrong
in the hand.
