"""
Mulligan Mints — model assumptions.

SINGLE SOURCE OF TRUTH for the 5-year plan. Every number below carries a
[SOURCE] (researched, cited in research/sources.md) or an [EST] (our estimate,
with the reasoning). Change numbers here, never in model.py.

Currency: South African Rand (ZAR), excluding VAT unless stated.
Horizon:  60 months. Month 1 = the month the company is capitalised.
"""

# ---------------------------------------------------------------------------
# 0. Timing and macro
# ---------------------------------------------------------------------------

HORIZON_MONTHS = 60
MONTH_ONE_LABEL = "2026-10"          # [EST] assumed funding close

# The artwork gate. Production cannot start before there is artwork to print,
# so the first purchase order is gated on PJ Offner's delivery, not on the
# funding date. Sequence:
#   Month 1  funding closes, company registered, trademark filed, PJ kicks off,
#            supplier dieline requested
#   Month 2  PJ delivers production-ready packaging artwork (week 6 of 8);
#            label content drafted and reviewed for R146 compliance alongside
#   Month 3  approved artwork and label to the supplier, plates made,
#            FIRST PURCHASE ORDER PLACED
#   Month 7  goods land, clear Port Health, first sales
ARTWORK_READY_MONTH = 2               # [EST] PJ's 8-week schedule, artwork at week 6
EARLIEST_PO_MONTH = 3                 # [EST] no PO before artwork + label sign-off
FIRST_SALE_MONTH = 7                  # = EARLIEST_PO_MONTH + order-to-shelf lead time

# USD/ZAR. Spot was ~15.93 on 2026-08-25. [SOURCE: TradingEconomics]
# We plan at 16.00 and depreciate 4%/yr — the rand's long-run drift against
# the dollar. Understating this is the classic importer's modelling error.
USDZAR_YEAR_1 = 16.00
ZAR_DEPRECIATION_PA = 0.04

CPI_PA = 0.045                        # [SOURCE] SARB target midpoint band
OPEX_INFLATION_PA = 0.060             # [EST] wage + logistics run above CPI
PRICE_INCREASE_PA = 0.050             # [EST] annual list price increase

VAT_RATE = 0.15                       # [SOURCE] SARS
CORPORATE_TAX_RATE = 0.27             # [SOURCE] SARS company rate
# Small Business Corporation rates could apply in Y1-Y2 but we model the flat
# rate for conservatism.

# ---------------------------------------------------------------------------
# 1. Product and landed cost
# ---------------------------------------------------------------------------
# Base SKU: 35g sugar-free pressed mint, hinged printed tin.
# Supplier carton spec (Suntak quote sheet):
#   12 tins/display box, 8 boxes/carton = 96 tins/carton
#   0.02 CBM/carton, 7.8 kg gross, 1,400 cartons per 20ft = 134,400 tins
UNITS_PER_DISPLAY_BOX = 12
BOXES_PER_CARTON = 8
UNITS_PER_CARTON = UNITS_PER_DISPLAY_BOX * BOXES_PER_CARTON       # 96
CARTONS_PER_20FT = 1400                                           # [SOURCE] Suntak quotation
UNITS_PER_20FT = UNITS_PER_CARTON * CARTONS_PER_20FT              # 134,400

# FOB Shantou per tin, USD. Tin + print + 35g sugar-free centre + display box.
#
# Tier 1 is the REAL QUOTE: Suntak Foods, 29 Aug 2026, USD 0.465/unit FOB
# Shantou against an inquiry of 134,400 units (1x20GP), valid 30 days.
# [SOURCE: product/quotes/suntak-quotation-2026-08-29.pdf]
#
# Tiers 2-5 are still [EST]. We have exactly one price point, so they are the
# original volume curve rescaled by the same 5.7% the quote came in above our
# estimate. Treat them as an extrapolation from a single observation, not as
# quoted prices — and ask Damita to quote the volume breaks directly.
FOB_USD_CURVE = [
    #  (annual units up to, USD FOB per tin)
    (150_000,   0.465),   # [SOURCE] quoted
    (400_000,   0.412),   # [EST]
    (800_000,   0.375),   # [EST]
    (1_500_000, 0.349),   # [EST]
    (10_000_000, 0.328),  # [EST]
]

# Sea freight, 20ft China -> Durban/Cape Town.
# [SOURCE] $2,403-$2,937 (Jul 2026). We plan at the top of the range.
FREIGHT_USD_PER_20FT = 2_900
MARINE_INSURANCE_PCT_OF_FOB = 0.005   # [EST]

# SA import duty on HS 1704 sugar confectionery = 25% of FOB customs value.
# [SOURCE] SARS tariff / JLog. No China preference applies.
IMPORT_DUTY_PCT = 0.25

# Clearing, port charges, container unpack, inland transport to our 3PL.
# [EST] ~R28,000 per 20ft all-in.
CLEARING_ZAR_PER_20FT = 28_000

# Damage / short-delivery / expiry write-off allowance on landed stock. [EST]
STOCK_WASTAGE_PCT = 0.02

# ---------------------------------------------------------------------------
# 2. Channels — price, margin and reach
# ---------------------------------------------------------------------------
# NET PRICE = what Mulligan Mints banks per tin, ex-VAT, after trade discount.
#
# Reference prices in market:
#   Fisherman's Friend 25g   R28.99  (Dis-Chem) [SOURCE]
#   Wilson's XXX 26g roll    ~R12    (PnP)      [SOURCE]
#   Mentos rolls/packs       R16-R22            [SOURCE]
# Mulligan Mints target RSP (incl VAT): R45 for a 35g branded tin.
# That is a deliberate premium: tin format, heritage build, niche channel.

TARGET_RSP_INCL_VAT = 45.00

CHANNELS = {
    "golf": {
        "label": "Golf clubs (pro shop + halfway house)",
        # Venue buys direct from us, sells at R45. Venue margin ~38% on RSP
        # ex-VAT (R39.13) => we bank ~R24.25.
        "net_price_y1": 24.25,
        "debtor_days": 30,
        # 460 affiliated clubs in SA [SOURCE: GolfRSA]. Serviceable universe
        # with a pro shop doing real traffic: ~300. [EST]
        "universe": 300,
        "outlets_end_of_year": [110, 220, 280, 295, 300],      # [EST]
        "units_per_outlet_month": [32, 38, 44, 50, 55],        # [EST]
    },
    "bars": {
        "label": "Bars, pubs and restaurants",
        "net_price_y1": 24.25,
        "debtor_days": 30,
        # Stats SA F&B sampling frame = 5,178 formal enterprises [SOURCE].
        # Premium/metro on-consumption universe we can service: ~2,500. [EST]
        "universe": 2_500,
        "outlets_end_of_year": [140, 450, 900, 1_300, 1_600],  # [EST]
        "units_per_outlet_month": [20, 22, 25, 28, 30],        # [EST]
    },
    "dtc": {
        "label": "Direct to consumer (own webshop + events)",
        # Full RSP to us, less ~R38/order shipping subsidy and payment fees.
        "net_price_y1": 35.00,
        "debtor_days": 0,
        "universe": None,
        "units_per_month_by_year": [400, 1_200, 2_200, 3_200, 4_000],   # [EST]
    },
    "retail": {
        "label": "Grocery + pharmacy retail (Checkers, Spar, Clicks, Dis-Chem)",
        # Retail RSP R42.99, retailer margin 32%, plus 13% trade spend
        # (listing fees, promo, co-op ads) => we bank ~R21.00.
        "net_price_y1": 21.00,
        "debtor_days": 65,
        "universe": 1_400,
        "start_month": 19,                                      # Y2 H2 [EST]
        "outlets_end_of_year": [0, 120, 450, 800, 1_100],       # [EST]
        "units_per_outlet_month": [0, 24, 27, 30, 32],          # [EST]
    },
    "export": {
        "label": "Export (importer/distributor, FOB South Africa)",
        # Importer buys landed-in-their-market; we bank a wholesale price
        # well below SA net but with no local selling cost attached.
        "net_price_y1": 15.50,
        "debtor_days": 45,
        "universe": None,
        "start_month": 31,                                      # Y3 H1 [EST]
        "units_by_year": [0, 0, 90_000, 320_000, 650_000],      # [EST]
    },
}

# ---------------------------------------------------------------------------
# 2b. Route to market: direct vs distributor
# ---------------------------------------------------------------------------
# You cannot service 3,000 outlets with five reps. Golf stays direct forever --
# it is a small, high-touch, brand-building universe. Bars and retail
# progressively move to third-party distributors: we give up ~R6/tin of net
# price and get reach and working capital back in exchange.
DISTRIBUTOR_NET_PRICE_BARS = 18.00        # [EST] distributor buys at this, sells at R24.25
DISTRIBUTOR_SHARE_OF_BARS_BY_YEAR = [0.00, 0.15, 0.45, 0.70, 0.80]   # [EST]
DISTRIBUTOR_DEBTOR_DAYS = 45

# Retail entry is not free. Listing/slotting fees, launch promo and shelf
# investment, charged when we go live with each national account. [EST]
RETAIL_LISTING_FEES = [
    (19, "Regional retail listing — pilot chain",     180_000),
    (26, "National listing — grocery chain #1",       450_000),
    (33, "National listing — grocery chain #2",       450_000),
    (38, "National listing — pharmacy group",         320_000),
]

# Licensing — the "brand out, not product out" route. Modelled separately as
# high-margin income, not as unit volume.
# Food & beverage brand royalties typically run 4-6% of licensee net sales.
# [SOURCE: RoyaltyRange]
LICENSING_ROYALTY_PCT = 0.06
LICENSING = {
    # year index (1-5): (signing fees ZAR, licensee net sales ZAR)
    4: {"signing_fees": 400_000, "licensee_net_sales": 0},
    5: {"signing_fees": 900_000, "licensee_net_sales": 15_000_000},
}

# ---------------------------------------------------------------------------
# 3. Operating costs
# ---------------------------------------------------------------------------
# Headcount: (start_month, role, monthly cost ZAR incl. employer costs)
HEADCOUNT = [
    (4,  "Founder / MD",                    38_000),
    (7,  "Brand & trade rep — Gauteng",     30_000),
    (14, "Brand & trade rep — Cape",        30_000),
    (18, "Operations & admin coordinator",  26_000),
    (25, "National sales manager",          58_000),
    (27, "Brand & trade rep — KZN",         32_000),
    (31, "Marketing & content lead",        48_000),
    (37, "Brand & trade rep #4",            34_000),
    (40, "Export / international manager",  62_000),
    (49, "Brand & trade rep #5",            36_000),
    (52, "Finance & supply chain manager",  60_000),
]

# Marketing. Year 1 is a fixed launch budget; thereafter a % of net revenue.
MARKETING_Y1_TOTAL = 380_000          # [EST] see gtm/go-to-market.md
# A challenger fighting Mondelez and Perfetti Van Melle does not spend less
# on brand as it scales -- and the whole licensing thesis is that brand equity
# IS the asset. We hold investment high. [EST]
MARKETING_PCT_OF_REVENUE = [None, 0.14, 0.13, 0.12, 0.11]

# Variable logistics: 3PL storage, pick-pack, outbound courier to venues.
LOGISTICS_ZAR_PER_UNIT = 1.35         # [EST]
LOGISTICS_ZAR_PER_UNIT_EXPORT = 0.45  # [EST] palletised, buyer collects

# Sales commission on direct venue channels only.
SALES_COMMISSION_PCT = 0.03

# Product development (new flavours, tin refresh, sample runs) and export
# market development (trade shows, importer visits, registration dossiers).
# Both are real and both are routinely forgotten in first-time plans. [EST]
NPD_PCT_OF_REVENUE = [0.00, 0.015, 0.020, 0.020, 0.020]
EXPORT_DEV_PCT_OF_EXPORT_REVENUE = [0.00, 0.00, 0.10, 0.07, 0.06]

# Fixed overheads, monthly ZAR, before inflation.
OVERHEADS_MONTHLY = {
    "Rent, office & storage deposit":   9_000,
    "Vehicles & travel":               16_000,
    "Insurance":                        4_500,
    "Accounting, payroll & audit":      9_500,
    "Legal & compliance":               4_000,
    "Software, POS & e-commerce":       6_500,
    "Telecoms, banking & sundry":       5_000,
}
OVERHEADS_START_MONTH = 4

# ---------------------------------------------------------------------------
# 4. One-off setup costs (pre-revenue, months 1-6)
# ---------------------------------------------------------------------------
# Ordered against the artwork gate above. Anything that has to be finished
# before the first purchase order sits in months 1-3; anything that only has to
# be ready for launch sits close to month 7.
SETUP_COSTS = [
    # (month, item, ZAR)
    (1,  "Company setup, shareholders agreement, banking",       35_000),
    (1,  "Trademark filing — SA classes 30, 25, 32",             28_000),
    # PJ Offner takes 10% equity for the brand identity, packaging and guidelines
    # instead of a fee, and carries his own costs — see
    # legal/term-sheet-pj-offner.md. There is no cash line for the brand at all.
    # Grounded in the quote, for a single launch SKU: tin sample USD 250,
    # OEM formula sample USD 200, embossing mould USD 300 per position, courier,
    # plus samples from a second supplier for comparison. One flavour instead of
    # three takes roughly R20,000 out of this line.
    (2,  "Supplier samples, freight, tooling & plate charges",   25_000),
    (2,  "Pre-press, dieline proofing & production files",       40_000),
    # Must clear before the PO — printing 30,000 tins to an unreviewed label is
    # not a risk worth taking to save a month.
    (3,  "Lab analysis, nutritional panel & R146 label review",  32_000),
    (4,  "Product photography & launch content shoot",           55_000),
    (4,  "Website, Shopify build & brand film edit",             48_000),
    (6,  "POS kit — counter units, tin displays, branded stand", 65_000),
    (7,  "Launch event at host club",                            60_000),
]

# ---------------------------------------------------------------------------
# 5. Inventory and supplier payment terms
# ---------------------------------------------------------------------------
# Suntak's MOQ is 800 kg of candy PER FLAVOUR — a batch minimum on a recipe,
# confirmed by Damita. [SOURCE: Suntak (Damita), Aug 2026] At 35 g of candy per
# tin that is 22,857 tins, or 22,944 rounded up to whole 96-tin cartons
# (239 cartons, 803 kg).
MOQ_TINS_PER_FLAVOUR = 22_944
# Launch with strong peppermint only. Each flavour is a separate 800 kg batch,
# so three flavours would tie up R681,000 of stock in three untested bets before
# a single tin has been sold — against year-one demand of ~24,500 tins and a
# 24-month shelf life. Flavours two and three get chosen on real sell-through,
# at a reorder around month 9. See docs/decisions/0006-launch-single-flavour.md.
LAUNCH_FLAVOURS = 1

MIN_ORDER_UNITS = MOQ_TINS_PER_FLAVOUR * LAUNCH_FLAVOURS

# You cannot buy 1.4 batches of candy. Reorders come in whole per-flavour
# batches, so the rounding increment is the batch, not a round number.
ORDER_ROUNDING_UNITS = MOQ_TINS_PER_FLAVOUR
TARGET_FORWARD_COVER_MONTHS = 3.5     # [EST] lead time + safety stock

# Suntak's stated terms: 50% T/T deposit in advance, balance before shipment
# from the factory. [SOURCE: quotation 2026-08-29] Worse for us than the 30/70
# we had assumed, and the balance falls due before the goods leave China rather
# than against the bill of lading.
SUPPLIER_DEPOSIT_PCT = 0.50           # paid when PO placed
PRODUCTION_LEAD_MONTHS = 2            # PO -> goods on the water
SHIPPING_TRANSIT_MONTHS = 1           # [SOURCE] 18-28 days Shanghai/Shenzhen -> Durban
CLEARING_MONTHS = 0.5                 # port health + customs release
# Balance (70%) paid against bill of lading, i.e. at shipment.

# ---------------------------------------------------------------------------
# 6. Funding
# ---------------------------------------------------------------------------
# Sized off the model's own unfunded peak deficit, plus a buffer. The model
# says base case burns to -R4.6m by month 33 with no funding, and dips below
# zero in month 24 on a R2.5m pre-seed alone -- so the pre-seed is R3.5m and
# the growth round has to land by month 20, not month 25.
FUNDING_ROUNDS = [
    # (month, label, ZAR)
    (1,  "Pre-seed — brand, first production run, SA proof of concept", 3_500_000),
    (20, "Seed — national retail rollout + export entry",              12_000_000),
]

# ---------------------------------------------------------------------------
# 7. Scenarios — volume multipliers applied to every unit-driven channel
# ---------------------------------------------------------------------------
SCENARIOS = {
    # -----------------------------------------------------------------------
    # BOOTSTRAP — a different business, not a slower version of the same one.
    #
    # No growth round, so no national retail (listing fees alone are R1.4m) and
    # no export inventory. That leaves the three channels that need no capital
    # and carry the best margin: golf clubs, bars and DTC, all sold direct.
    # No distributor either — bootstrapping needs margin, not reach.
    #
    # The route to market is Johannes himself. Get Lucky Golf Club already runs
    # 600+ golf days a year across 30+ premium courses, so the founder is
    # standing on the target customer's premises most weeks. That is the only
    # reason the outlet plan below is credible without a sales team.
    # -----------------------------------------------------------------------
    "bootstrap": {
        "label": "Bootstrap — founder-funded, licence the brand globally",
        "volume_multiplier": 1.00,
        "net_price_multiplier": 1.00,
        "fob_multiplier": 1.00,

        # No retail (R1.4m of listing fees and 65-day terms), and no export --
        # the global route is LICENSING ONLY. We ship the brand, never the tins.
        "channels_off": ["retail", "export"],

        # Warm start. Get Lucky Golf Club already has access to 30 clubs and runs
        # 600 promotions a year across them, so the golf channel does not begin
        # at zero and does not need a rep to open it. [SOURCE: founders]
        "outlets_override": {
            "golf": [60, 120, 180, 230, 270],
            "bars": [40, 120, 240, 360, 480],
        },
        # Two marketing executives running 600 sampling promotions a year should
        # drive better trial per outlet than a generic bootstrap. Set between the
        # old bootstrap (28->45) and the fully funded plan (32->55). [EST]
        "rate_override": {
            "golf": [32, 38, 43, 47, 50],
            "bars": [16, 19, 22, 24, 26],
        },
        "dtc_override": [300, 900, 1_500, 2_000, 2_500],
        "distributor_share": [0.0, 0.0, 0.0, 0.0, 0.0],
        "no_listing_fees": True,

        # Two founders, both drawing nothing in year 1. Draw rows step up rather
        # than stack (see headcount_is_cumulative_draw).
        "headcount": [
            (13, "Johannes draw (part-time)",     15_000),
            (13, "Andrew draw (part-time)",       15_000),
            (25, "Johannes draw",                 25_000),
            (25, "Andrew draw",                   25_000),
            (30, "Brand & trade rep — Gauteng",   25_000),
            (37, "Johannes draw (full)",          35_000),
            (37, "Andrew draw (full)",            35_000),
            (48, "Brand & trade rep — Cape",      28_000),
        ],
        "headcount_is_cumulative_draw": True,

        # Two marketing executives make a rand go further. That advantage is
        # modelled as HIGHER SELL-THROUGH FOR THE SAME SPEND (the rates above),
        # not as a smaller budget -- claiming both would be double-counting.
        "marketing_y1_total": 60_000,
        "marketing_pct": [None, 0.07, 0.07, 0.06, 0.06],
        "overhead_multiplier": 0.40,
        "npd_pct": [0.0, 0.0, 0.01, 0.015, 0.015],

        # THE STRATEGY. Prove it in SA, then licence the brand territory by
        # territory: a signing fee up front and a running royalty on the
        # licensee's net sales, with no inventory, no COGS and no working
        # capital on our side. Royalty rate is LICENSING_ROYALTY_PCT (6%).
        # Licensee net sales are the licensee's, not ours. [EST]
        "licensing": {
            3: {"signing_fees": 300_000, "licensee_net_sales": 0},           # 1st territory signs, launches late
            4: {"signing_fees": 600_000, "licensee_net_sales": 10_000_000},  # 3 territories live
            5: {"signing_fees": 600_000, "licensee_net_sales": 28_000_000},  # 5 territories live
        },
        # Licensing is low-cost, not no-cost. Trademark filings per territory,
        # agreements, licensee search, travel and quality audits. [EST]
        "licensing_costs": {2: 120_000, 3: 180_000, 4: 240_000, 5: 280_000},

        # Branding, website and design cost nothing in cash: PJ Offner takes
        # 10% equity for the identity and packaging, and the founders build the
        # site and shoot the content themselves. What remains below are
        # third-party fees that no amount of in-house skill removes.
        "setup_costs": [
            (1, "Company setup and banking",                     18_000),
            (1, "Trademark filing — SA classes 30 and 25",       22_000),
            (2, "Supplier samples, freight, tooling & plates",   25_000),
            (2, "GS1 barcode registration & physical proofs",     8_000),
            (3, "Lab analysis, nutrition panel & R146 review",   32_000),
            (6, "POS kit — counter units and display boxes",     20_000),
        ],

        # Trade finance against confirmed stock orders. The facility advances a
        # share of each landed-stock payment and is repaid out of sale proceeds
        # a few months later, at 17% p.a. [SOURCE: founders]
        #
        # It attacks the single biggest use of the raise -- inventory. But it
        # only arrives in year 2, once there is traction to lend against
        # [SOURCE: founders], and that timing is the whole shape of this plan:
        # the raise has to carry the launch order and the first two reorders
        # unaided, and the bank carries the stock from year two onward.
        "trade_finance": {
            "advance_pct": 0.70,      # [EST] typical import facility advance
            "repay_months": 4,        # [EST] repaid out of sale proceeds
            "rate_pa": 0.17,          # [SOURCE: founders]
            "start_month": 13,        # year 2 [SOURCE: founders]
        },

        # R1m from an outside investor on a hybrid structure: 10% of the equity
        # PLUS the R1m returned out of R2 from every tin sold, until repaid.
        # See finance/bootstrap-plan.md for what that costs.
        "funding_rounds": [
            (1, "Investor — R1m for 10% equity plus revenue share", 1_000_000),
        ],
        # R1 a tin from the first sale until the R1m is returned. That needs
        # 1,000,000 tins. This plan sells 770,505 in five years, so the capital
        # is NOT fully repaid inside the horizon — roughly R229k is still
        # outstanding at the end of year 5, clearing during year 6. That is the
        # trade: the lightest possible drag on the business, and an investor who
        # waits longer than five years to be made whole.
        "investor_repayment": {
            "per_tin": 1.00,
            "total": 1_000_000,
            "start_month": FIRST_SALE_MONTH,   # payments begin with the first sale
        },
    },

    "bear": {
        "label": "Bear — slow venue adoption, retail delayed, no export scale",
        "volume_multiplier": 0.45,
        "net_price_multiplier": 0.94,
        "fob_multiplier": 1.08,
        "licensing": False,
        # In a bear case you do not hire the base-case plan. Hires slip six
        # months, marketing is halved, overheads are held lean.
        "hire_delay_months": 6,
        "marketing_multiplier": 0.55,
        "overhead_multiplier": 0.80,
    },
    "base": {
        "label": "Base — proof of concept converts, national retail from Y2",
        "volume_multiplier": 1.00,
        "net_price_multiplier": 1.00,
        "fob_multiplier": 1.00,
        "licensing": True,
    },
    "bull": {
        "label": "Bull — creator-led breakout, export pulls forward",
        "volume_multiplier": 1.55,
        "net_price_multiplier": 1.03,
        "fob_multiplier": 0.95,
        "licensing": True,
        "hire_delay_months": 0,
        "marketing_multiplier": 1.30,
        "overhead_multiplier": 1.10,
    },
}
