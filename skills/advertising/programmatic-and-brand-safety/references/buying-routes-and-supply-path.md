# Buying routes and supply path

Read when choosing how each programmatic line is bought, auditing who takes a share of the money, or checking ads.txt, sellers.json and the SupplyChain object. Parent: [programmatic-and-brand-safety](../SKILL.md).

## 1. Who does what

| Role | Job | What to ask for |
|---|---|---|
| Advertiser | Owns the money, the brand-risk policy and the right to audit | Contract clause giving access to DSP logs and fee schedules |
| Agency or trading desk | Plans and operates the DSP seat | Whether it trades as agent (disclosed fees) or principal (resells media it bought) |
| DSP (demand-side platform) | Bids for impressions on the buyer's behalf | Platform fee, data fees, log-level export, seat ownership |
| SSP or exchange (supply-side platform) | Runs the auction for the publisher | Take rate, seller ID, sellers.json entry, schain support |
| Publisher or app developer | Owns the page, app, screen or podcast | ads.txt or app-ads.txt listing each authorised seller; direct rate card |
| Verification vendor | Measures viewability, IVT and brand safety | Accreditation scope, tag coverage, reporting cadence |

Principal media: when an agency buys inventory itself and resells it to the client, the margin is not a disclosed fee. Treat this as a disclosure question for the client's contract owner: ask in writing whether any line is principal-based and what margin applies. Legal or contract conclusions route to the client's counsel.

## 2. Buying routes

| Route | Price | Volume | Control | Use when |
|---|---|---|---|---|
| Open exchange (open auction) | Auction | Variable | Lowest: many sellers and resellers | Scale is needed and the inclusion list, IVT filtering and supply-path rules are in place |
| Private marketplace (PMP) | Auction with floor | Variable | Named publishers, deal ID | A group of trusted publishers exists but prices are not fixed |
| Preferred deal | Fixed | Not guaranteed | One publisher, first look | Premium placements where the publisher offers a fixed rate |
| Programmatic guaranteed (PG) | Fixed | Guaranteed | Closest to direct | A direct booking that the buyer wants inside the DSP for frequency and reporting |
| Direct insertion order (non-programmatic) | Negotiated | Guaranteed | Full, with publisher ad serving | The publisher does not sell programmatically, which is common in East Africa |

The 2020 UK study found PMP spend reached publishers at a higher average share (54%) than open-marketplace spend (49%) (register `ISBA-PWC-PROGRAMMATIC-2020`). Use that as a reason to test deal routes, not as an expected rate.

## 3. Supply-path optimisation (SPO) checklist

Run each check per seller and deal. Record `PASS`, `FAIL` or `NOT_ASSESSED` with date and source.

| Check | Standard | Pass condition |
|---|---|---|
| Seller authorised by the publisher | ads.txt 1.1 for web; app-ads.txt for apps and CTV apps (register `IAB-TECHLAB-ADS-TXT`) | The SSP's domain and seller account ID appear in the publisher's file, with DIRECT or RESELLER |
| Seller identity known | sellers.json (register `IAB-TECHLAB-SELLERS-JSON`) | The seller ID resolves to a named entity, not "confidential", and matches the ads.txt relationship |
| Full chain visible | OpenRTB SupplyChain object (register `IAB-TECHLAB-SCHAIN`) | The schain is complete and every node is authorised |
| Fewest hops | SPO practice | Prefer DIRECT paths; remove duplicate resellers of the same inventory |
| Fees disclosed | Contract | DSP, data, verification and SSP fees stated per line |
| Spend traceable | Log-level data | Buyer logs can be matched to seller or publisher records; the unmatched share is reported |
| Anti-fraud certification | TAG Certified Against Fraud (register `TAG-CERTIFIED-AGAINST-FRAUD`) | Each intermediary holds a current seal, or its absence is recorded |

Adoption evidence from Europe (2,054 news publishers, Aug 2025): about 73% hosted ads.txt and about 79% of valid ads.txt lines matched a sellers.json entry (register `IAB-EU-SUPPLY-CHAIN-TRANSPARENCY`). No equivalent East African study was found; adoption on East African publisher domains is `NOT_ASSESSED`, so check each domain's `/ads.txt` directly before buying.

## 4. The unknown delta and transparency reporting

The ISBA/PwC study (UK, Jan to Mar 2020) could match only 12% of 267 million impressions end to end. Among matched impressions, publishers received on average 51% of advertiser spend, and 15% of spend (the "unknown delta") could not be attributed to any disclosed cost, about one-third of supply-chain costs (register `ISBA-PWC-PROGRAMMATIC-2020`). Lessons for the brief:

- Write data access into the contract before the flight: DSP log-level data, SSP records and publisher confirmations.
- Report the matched share first; a working-media share based on a small matched sample must say so.
- Never quote 51% or 15% as the client's own figures; they describe one UK sample in 2020.

Post-flight transparency report, per line: gross spend; each disclosed fee; working media (matched); unmatched share; number of sellers and paths; viewable and IVT rates; brand-safety blocks. Any cell without data reads `NOT_ASSESSED`.

## 5. East Africa realism

- Local premium supply is thin. Check whether Nation Media Group titles (Daily Monitor in Uganda, Daily Nation in Kenya), Vision Group (New Vision), The Standard, Mwananchi Communications and The New Times sell through an SSP, a PMP, programmatic guaranteed or only by direct insertion order. The answer for each is `NOT_ASSESSED` until the publisher's ads.txt and sales team confirm it.
- Which ad server each publisher uses (for example Google Ad Manager), and whether it offers PG or PMP deals through it, is `NOT_ASSESSED`; ask the publisher. Access to Google Display & Video 360 seats in Uganda, Kenya, Tanzania or Rwanda, and through which resellers, is `NOT_ASSESSED`: confirm with the agency or Google partner before planning around it.
- Much "Kenyan" or "Ugandan" programmatic reach is global exchange inventory geotargeted to the country, often mobile apps. Treat it as the highest fraud and made-for-advertising risk (see [viewability, IVT and attention](viewability-ivt-and-attention.md)).
- Handset-maker and music-streaming inventory (for example Transsion devices or Boomplay) may be offered by resellers. Audience figures for these are UNVERIFIED; require the seller's own audited or log-based numbers and app-ads.txt before any buy.
- Prices are often quoted in US dollars; convert to UGX (or the named currency) at a dated rate and show the fee layers in the same currency.

## Sources

Register IDs: `ISBA-PWC-PROGRAMMATIC-2020`, `IAB-EU-SUPPLY-CHAIN-TRANSPARENCY`, `IAB-TECHLAB-ADS-TXT`, `IAB-TECHLAB-SELLERS-JSON`, `IAB-TECHLAB-SCHAIN`, `TAG-CERTIFIED-AGAINST-FRAUD`.
