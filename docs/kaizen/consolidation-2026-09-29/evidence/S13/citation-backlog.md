# S13 citation and edition backlog

- **Date:** 29 September 2026. Working tree on `e7d68fd` (S12) plus the S13 change set.
- **Scope:** the citation backlog carried from S03–S10 (S09 evidence, `S09/citation-verification.md`, `S10/S09-backlog-triage.md` §3 "Citations and publishers", S03–S07 "Citation backlog" bullets), plus the carried B07/B09/B11/B13/B14/B16 claims.
- **Method:** bibliographic checks against the Open Library catalogue search API (T2 library catalogue; `https://openlibrary.org/search.json`), 29 Sep 2026. The session's web-search allowance was exhausted and the Google Books API returned HTTP 429, so Open Library was the only catalogue used. An item not found there is marked verify, never guessed. Zero spend.
- **Edit scope:** `skills/**/references/*.md` only. No `SKILL.md` routing text, `ALIAS.md`, fixture or `brand-strategy-and-distinctive-assets` file was touched. `ALIAS.md` files and preservation maps keep their historical citations.
- **Rule:** citations stay as Author (Year) *Title*, Publisher. A verified fact replaces the wrong one; an unverified item gets "(verify …)" or "(publisher unverified …)" in place.

## 1. Citations

| Item | File(s) (under `skills/`) | Finding | Source checked | Action |
|---|---|---|---|---|
| Sant (2012) *Persuasive Business Proposals*, 3rd edn, AMACOM | `biz-dev-credentials/references/case-study-method.md` | AMACOM 2012 confirmed | Open Library (T2) | CORRECTED: "added at merge; verify" flag replaced with the confirmation |
| Hatton (2007) *The Definitive Business Pitch* | same | Author Angela Hatton; catalogue imprint "Financial Times Management" | Open Library (T2) | CORRECTED |
| Bodnar and Cohen (2012), Wiley | same | Confirmed in S09 (item 10) | S09 check (T1) | CORRECTED: stale verify flag removed |
| Funk (2011) *Social Media Playbook for Business*, Praeger | `strategy-ewom-reviews/references/word-of-mouth-and-referral-design.md` | Praeger 2011 confirmed | Open Library (T2) | CORRECTED (flag removed) |
| Funk (2013) *Advanced Social Media Marketing*, Apress | `meta-roi-framework`, `meta-social-listening`, `playbook-social-media-policy` references | Apress; catalogue first date 2012 (late-2012 release, 2013 imprint is plausible) | Open Library (T2) | ALREADY OK (year left as cited) |
| Gladwell (2000) *The Tipping Point*, Little, Brown | `word-of-mouth-and-referral-design.md` | Confirmed | Open Library (T2) | CORRECTED (flag removed) |
| Kotler et al. (2023) *Marketing Management* 16th edn | `word-of-mouth-and-referral-design.md` (listed, not cited in text); also `meta-testing-framework`, `08-influencer`, `playbook-community-management` (2 files), `playbook-pr-publicity`, `playbook-viral-content-design`, `strategy-customer-value-journey` references | 16th edn is Kotler, Keller and Chernev, Pearson, catalogue date 2021; no 2023 edition found | Open Library (T2) | MARKED verify in the ewom file (co-authors added, "year verify; not cited in the text above"); the other seven files NOT_ASSESSED (left, listed as a next opportunity) |
| Kelley and Sheehan (c. 2021–22) *Advertising Management in a Digital Environment* | 15 reference files across `advertising-strategy-and-budget`, `creative-brief-and-big-idea`, `marketing-foundations-stp-positioning`, `playbook-agency-operations` and others | Larry D. Kelley and Kim Bartel Sheehan, Taylor & Francis (Routledge), catalogue date 2021 | Open Library (T2) | CORRECTED: "(c. 2021–22)" → "(2021)" in every reference file |
| Stutts (2021), Scribe / Lioncrest | `ad-copy-and-hook-lab`, `ad-testing-and-scaling`, `ad-to-site-journey-handoff`, `marketing-foundations-stp-positioning` references | Phillip Stutts, Lioncrest Publishing (Scribe Media) | Open Library (T2) | CORRECTED: publisher normalised to Lioncrest |
| Nelson (2019) *The Seven Figure Agency Roadmap* | `biz-dev-positioning/references/practitioner-positioning.md`, `playbook-agency-operations/references/ai-revenue-and-seven-figure-model.md` | Josh Nelson, 2019, independently published (not "Seven Figure Agency LLC"); no 2018 citation remains live | Open Library (T2) | CORRECTED |
| Sobia Publication (2022) *Powerful Social Media Marketing for Beginners* | `practitioner-positioning.md`, `strategy-channel-architecture/references/channel-architecture-method.md` | Independently published, 2022. Listed but not cited in the channel-architecture text | Open Library (T2) | CORRECTED (publisher); left in place (the "unused" rule was not applied because the content may derive from it) |
| Stukus, Patrick and Nuss (2019) | `healthcare/references/health-sector-strategy-method.md` | Springer, 2019 | Open Library (T2) | CORRECTED (publisher added) |
| Parsons (2009) *Beyond Persuasion* | same | Health Administration Press; catalogue shows 2001 (and a 2013 University of Toronto Press book); no 2009 record | Open Library (T2) | MARKED verify (publisher added, "2009 edition verify") |
| Johnsen (2024) | `anti-ai-slop/references/humanising-rewrite-passes.md` | Maria Johnsen, *AI in Digital Marketing*, Mercury Learning, 2024 (the file gave "Johnsen, S.") | Open Library (T2) | CORRECTED; "Ltifi and Johnsen (forthcoming)" MARKED verify |
| Upadhyay (2024) *Generative AI for Marketing* | `prompt-engineering-library/references/prompt-formula-components-and-techniques.md`, `meta-tools-stack-evaluation/references/ai-tool-fit-access-cost-governance.md` | Malay Upadhyay, Business Expert Press, 2024 (engine gave "S." and "M. A.", Packt); stray full stop fixed | Open Library (T2) | CORRECTED |
| Joseph (c.2023–2024) | `prompt-formula-components-and-techniques.md` | No title or publisher identified | — | MARKED verify |
| Erné (2024), two initials and two titles | `prompt-formula-components-and-techniques.md`, `playbook-marketing-automation/references/ai-automation-recipes.md`, `ai-use-case-mapping/references/ai-strategy-co-thinking-prompts.md` | Neither *AI-Powered Marketing* nor *The Artificial Intelligence Handbook for Management Consultants* found | Open Library (T2) | MARKED verify (3 files) |
| Roth and neuroflash (2024 / 2024–25), initials J. and H. | `anti-ai-slop`, `prompt-engineering-library` (2 files), `meta-content-repurposing/references/ai-assisted-recycling-pipeline.md` | Vendor publication; initials and year inconsistent | — | MARKED verify (4 places) |
| Killian in Hahn (2003), no title | `biz-dev-credentials/references/credentials-build-method.md` | Hahn, F. E. (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn, Wiley is confirmed and is the only Hahn (2003) the engine cites | Open Library (T2) | CORRECTED (title added; contributor attribution marked verify) |
| Bly (2018), no title (social proof taxonomy) | `credentials-build-method.md` | The engine elsewhere cites Bly, R.W. (2018) *The Digital Marketing Handbook* | engine cross-reference | MARKED verify (title added as cited in the 07 references) |
| Handley (2012) vs Handley and Chapman (2012) | `meta-content-repurposing/references/content-factory-and-repurposing-chains.md` | *Content Rules* is Handley and Chapman, Wiley (first 2010; 2012 printing) | Open Library (T2) | CORRECTED (in-text cite) |
| Hanlon and Tuten (2022) handbook title | `strategy-ewom-reviews/references/ewom-programme-method.md` | *The SAGE Handbook of Social Media Marketing*, SAGE, 2022 (the file said "Digital Marketing") | Open Library (T2) | CORRECTED. `measurement-tracking-plan/references/consent-retention-and-sharing-review.md` gives a longer "Digital Mark…" title; Open Library also lists a "Digital and Social Media Marketing" record, so that line is NOT_ASSESSED |
| Westergaard (2016) and Sheridan (2019) | `12-website-content-plan/references/buyer-question-content-plan.md` | *Get Scrappy: Smarter Digital Marketing for Businesses Big and Small*, AMACOM 2016; *They Ask, You Answer*, Wiley (2019 printing) | Open Library (T2); S09 item 11 | CORRECTED (full title; flags removed) |
| Macarthy (2022 vs 2023) *500 Social Media Marketing Tips* | `playbook-community-management/references/social-customer-care.md` (l.65) | Independently published, revised repeatedly; the engine standard is 2022, 6th edn | Open Library (T2); S09 item 12 | CORRECTED (in-text l.65 aligned to 2022, 6th edn); the Sources line already records the discrepancy |
| Dietrich (2020) *Spin Sucks* | `peso-integrated-strategy/references/peso-method.md` | Only a 2013–14 Que/Pearson edition catalogued; no 2020 edition found | Open Library (T2) | MARKED verify |
| Harris (2016) *Small Business Big Money Online* | `playbook-post-click-strategy/references/ecommerce-and-whatsapp-conversion-diagnosis.md` | Not catalogued | Open Library (T2) | MARKED publisher unverified |
| Larsson (2016) *Ecommerce Evolved* | same | Tanner Larsson, CreateSpace, 2016 | Open Library (T2) | CORRECTED (publisher added) |
| Phillips (2015) | same § Sources | No live occurrence found | grep | ALREADY OK |
| Johnson (2023) *How to Become a Social Media Manager* | `02-platform-audit/references/audit-as-lead-offer.md` | Catalogue shows John Johnson, 2021, independently published | Open Library (T2) | MARKED year verify |
| Hietaniemi (2020) | `platform-instagram/references/growth-diagnosis-and-experiments.md` | Not catalogued | Open Library (T2) | MARKED publisher unverified |
| Walsh Phillips (2023), 2nd edn | same | Kim Walsh-Phillips, Entrepreneur Press, first edition 2017; second-edition year not catalogued | Open Library (T2) | CORRECTED (name, publisher) + MARKED year verify |
| Rageh (Ed.) (2026) | `03-audience-personas/references/generational-segment-lens.md` (other files already carry "IGI Global … verify") | Not catalogued (2026 title) | Open Library (T2) | MARKED verify (consistent with other files) |
| Raaz (c.2023) *Web Analytics Blueprint* | `meta-roi-framework/references/retention-cohorts-and-ltv.md` | Not catalogued | Open Library (T2) | MARKED verify; `measurement-tracking-plan` and `meta-reporting` mentions NOT_ASSESSED (left) |
| Raymond and Johnston (2021) | `platform-linkedin/references/company-pages-showcase-and-events.md` | Already labelled "title and publisher not given; confirm before citing" | — | ALREADY OK |
| Kelley and Sheehan, Hahn, Edwards, Edwards and Douglas (1991), Kennedy (2004), Levy (2015), Bodnar and Cohen, Chaffey and Ellis-Chadwick (2022) | various | Confirmed as cited (Tarcher 1991; Entrepreneur Press 2004; O'Reilly 2015) | Open Library (T2) | ALREADY OK |
| Kim and Mauborgne (2005) | `social-commerce-strategy/references/pricing-conversion-and-differentiation.md` | HBS Press 2005 confirmed; no 2015 citation live | Open Library (T2) | ALREADY OK |
| Chaffey (2024) | — | No live occurrence remains (fixed in S09) | grep | ALREADY OK |
| Ltifi 2024 vs 2025 | — | Live files use 2024 (S09 decision) | grep | ALREADY OK |
| Farri and Rosani, Nayebi in-text (`ai-automation-recipes.md` l.212, l.226) | `playbook-marketing-automation` | Both in-text names map to Sources entries already marked "(verify: not found …)" | S09 check | ALREADY OK |
| Hero/Hub/Hygiene attribution | `meta-content-repurposing` references | Already attributed to YouTube/Google | — | ALREADY OK |
| Jill Rowley via Shanks (2016); Marcos et al. (c. 2025); Wiebe (2011) *Copy Hackers* | `playbook-social-selling`, retainer and B2B references, ad-copy references | Secondary attribution stated; Marcos and Wiebe not catalogued | Open Library (T2) | NOT_ASSESSED (left as cited) |
| FSU/COLING-2025 and PubMed "delve" | `anti-ai-slop/SKILL.md` l.73 | Body text of a SKILL.md, outside this pass's edit scope | — | NOT_ASSESSED |
| "ECC brand-voice skill" as a source | `brand-voice-ai-training`, `meta-content-repurposing` references | An adaptation note for a third-party skill, not a book | — | NOT_ASSESSED (licence and commit pinning are a next opportunity) |
| Engine-name drift: `digital-research-skills` GitHub links | 4 `SKILL.md` files | `gh repo view peterbamuhigire/digital-research-skills` resolves; `digital-research-engine` does not exist on GitHub. The links are correct | GitHub CLI | ALREADY OK (no change) |

## 2. Carried B-items (verify at use)

| Item | File | Action |
|---|---|---|
| B07 $20 Rule currency error | `meta-roi-framework/references/roi-model-method.md` | CORRECTED: UGX and USD not equated; labelled house heuristic, verify at use |
| B07 "95%+ mobile" | `meta-testing-framework/references/testing-method.md` | MARKED `NOT_ASSESSED`, verify at use |
| B09 email platform plans | `07-email-marketing-strategy/references/email-funnel-build-sequence.md` | ALREADY OK (verify note above the table) |
| B11 ManyChat plan and price | `playbook-chatbot-strategy/references/chatbot-build-guide.md` | MARKED verify at use |
| B11 late-payment fee | `playbook-agency-operations/references/agency-operating-procedures.md` | MARKED house term (the white-label reference already labels its example) |
| B11 crisis UI menu paths | `playbook-crisis-communications/references/crisis-response-procedures.md` | MARKED verify at use |
| B13 Twilio pricing; Status "swipe-up link" | `playbook-sms-whatsapp-marketing/references/sms-whatsapp-campaign-method.md` | MARKED unverified, verify at use |
| B14 payment fees, VAT threshold, "85%+ mobile" | `social-commerce-strategy/references/social-shop-setup-and-operations.md`, `pricing-conversion-and-differentiation.md` | MARKED verify at use (VAT routed to the finance engine) |
| B16 WhatsApp Status 30 s | `training-client-team/references/diy-content-handbook.md` | MARKED verify at use (the TikTok and Reels ranges named in the backlog no longer appear) |
| "3.2 million Facebook users" | `meta-roi-framework/references/investment-business-case.md`, `training-social-media-fundamentals` | ALREADY OK (dated and verify/`NOT_ASSESSED`) |

## 3. Counts

CORRECTED 21 · MARKED verify 18 · ALREADY OK 14 · NOT_ASSESSED 6 (rows above, several spanning more than one file).

## 4. Not addressed: internal contradictions (next opportunities)

These doctrine contradictions from `S10/S09-backlog-triage.md` §3 were not changed. They need an owner decision, not a citation fix:

- posting frequency and EAT windows (`meta-algorithm-guide`; peak times across 03, 05 and 08);
- TLV vs CLV formulas (`meta-budget-planner`); tier totals vs ranges; RAG amber 15 % vs 10 % (`meta-reporting`);
- MQL thresholds and point tables (`meta-sales-marketing-alignment`); two NSS band sets (`meta-social-listening`); 90 % vs 95 % confidence (`meta-testing-framework`);
- tool budget tiers (`meta-tools-stack-evaluation` vs `ai-tool-fit`); USD vs UGX budget bands (06 vs 05); email cadence and two KPI tables (07);
- post-campaign report timing (09 vs 13); publication frequency vs the 12-in-90 plan (12); GBP photo minimum (8 / 9 / 10);
- WhatsApp 60 vs 90 days, broadcast caps, thumbnail and quick replies; posting frequency vs the quality rule (TikTok, Instagram);
- YouTube 5–12 vs 15 minutes; approval window 24 h vs 48 h; SLA tables; business hours; holding-statement timings; Level 1 notification timing;
- 5-point vs 4-point page structure; WhatsApp sequence timings; DM response targets; post-event NPS 48 h vs 24 h; completion-rate targets; five vs six metrics;
- misnumbered cross-references (`strategy-personal-brand`); "Launch Owned before Earned" order (peso); six vs eight intake inputs; DPPA vs DPA;
- the "Slopy" label; overlapping priority bands (`ai-use-case-mapping`); duplicate "Section 2A" and draft EU AI Act numbering (`policy-ai-content-ethics`);
- "Begin Your Journey" vs anti-slop; French and Kiswahili date formats and glosses (native review); the "leading" superlative in a biz-dev example;
- slide-format pointer to CLAUDE.md; stale "SKILL.md § …" pointers in moved references; a personal phone number in an acknowledgement; consultant-specific storytelling references; "Vidyard Goboard";
- Kotler et al. year in seven further files; Raaz in `measurement-tracking-plan` and `meta-reporting`; the Hanlon and Tuten title in `consent-retention-and-sharing-review.md`; MonkeyLearn availability (`listening-operations-playbook.md`).
