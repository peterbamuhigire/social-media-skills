# S10 evidence: gap-fill — three NEW skills, one merge, reference extensions

- **Phase:** Social Kaizen 2026-09-29, S10 (plan `04-phases/S10-gap-fill-legal-currency-and-new-skills.md`). **T01 (legal currency) is excluded**: it was done earlier under D-SK-02 and pushed as `7c60138`; see [S10-T01-legal-currency-evidence.md](S10-T01-legal-currency-evidence.md).
- **Date:** 29 September 2026. **Start commit:** `3416d0b` (S09); worktree clean at start.
- **Active skills:** 110 → **112**.
- **Change classes:** doctrine (three NEW skill contracts, reference extensions, legal/market positions as screening text); metadata (91 register rows, counts, evidence); workflow-routing (three changed "not for" clauses, 28 fixtures, alias route). D-SK-01, D-SK-05 and D-SK-06 ratified by orchestrator under Peter's delegated authority.
- **Limits:** routing figures are a lexical proxy, not live routing. Model-executed behavioural runs are `NOT_ASSESSED (zero-spend rule)`. The session's free web-search quota ran out part-way; later checks used direct page fetches, and pages that could not be fetched are `NOT_ASSESSED`, never asserted.

## Count arithmetic

| Step | Active |
|---|---|
| After S07/S08/S09 | 110 |
| + NEW `brand-strategy-and-distinctive-assets` (G01) | 111 |
| + NEW `marketing-mix-modelling` (G02) | 112 |
| + NEW `programmatic-and-brand-safety` (G03) | 113 |
| − MERGE `ecommerce-brand-differentiation` → brand skill (the plan's in-phase offset, `03-consolidation-map.md` NEW table) | **112** |

The plan offsets G02 and G03 by the S02–S07 merges already done (the consolidation map closes at 112 with them counted), and G01 by the in-phase merge. 112 is the plan's stated close target; cap 120 leaves 8 of headroom. `check_skill_aliases.py`: routes 83, active 112, cap 120, 0 findings.

## Task status

| Task | Status | Evidence |
|---|---|---|
| T01 legal currency | ALREADY DONE (`7c60138`) | T01 evidence file |
| T02 NEW `brand-strategy-and-distinctive-assets` + merge | DONE | `skills/strategy/brand-strategy-and-distinctive-assets/` (SKILL.md 125 lines; references `cep-and-mental-availability.md`, `distinctive-asset-audit.md`, `brand-tracking.md`, `long-short-balance-and-reach.md`, `ecommerce-differentiation.md`, `ecommerce-differentiation-method.md`). Merge per the runbook: [preservation map](../../preservation/ecommerce-brand-differentiation.md) (27 rows, 1 dropped as a duplicate of the canonical boundary sentence); source reference moved with plain `mv` and a provenance line; `SKILL.md` → `ALIAS.md` with the banner; route in `docs/skill-aliases.yml`; referrers re-pointed (`04-brand-voice-intake`, `marketing-foundations-stp-positioning`, `ecommerce-export-marketing-advisory`, `social-commerce-strategy` + reference, `playbook-post-click-strategy` reference, README, plugin manifest, fixtures). Historical records (`docs/plans`, `docs/engine-upgrade-july-2026`, the `ecommerce-conversion-optimisation` ALIAS) left unchanged |
| T03 NEW `marketing-mix-modelling` | DONE | `skills/advertising/marketing-mix-modelling/` (121 lines; references for data readiness and East Africa constraints, Meridian/Robyn choice, calibration and geo experiments, triangulation and decision governance). Data floors taken from the primary docs (Meridian: ≥ 2 years weekly for geo, 3 for national; Robyn: ≥ 2 years weekly). Attribution skill: "not for" now names `marketing-mix-modelling`; new reference `geo-power-and-incrementality-hierarchy.md` (IAB hierarchy read in full) |
| T04 NEW `programmatic-and-brand-safety` | DONE_WITH_LIMITATIONS | `skills/advertising/programmatic-and-brand-safety/` (132 lines; references for buying routes and supply path, viewability/IVT/attention, brand safety and suitability, CTV/DOOH/audio). GARM stated as discontinued (9 Aug 2024). Limits: IAB Tech Lab CTV release (HTTP 403, partial); successor to a shared GARM floor, DV360 access in the region, local ads.txt adoption `NOT_ASSESSED`. `media-planning` "not for" now names the new skill |
| T05 email deliverability and holdouts | DONE | `07-email-marketing-strategy/references/deliverability-and-lifecycle-holdouts.md`; `email-copywriter` pointer |
| T06 WhatsApp platform economics | DONE | `platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md` (official rate card read: UG, KE, TZ, RW in "Rest of Africa"; the 1 Oct 2026 change to service-message charging recorded); pointers in SMS/WhatsApp, chatbot, social commerce. **Currency finding:** the free entry-point window is now "up to 7 days", opened by click-to-WhatsApp ads; the benchmark's "72 hours" is stale |
| T07 creative effectiveness and test rigour | DONE | references in `creative-brief-and-big-idea`, `ad-copy-and-hook-lab`, `ad-testing-and-scaling`, `meta-testing-framework`, `meta-reporting`, `strategy-video-content` |
| T08 commerce media | DONE_WITH_LIMITATIONS | `social-commerce-strategy/references/commerce-media-and-marketplaces.md`; `paid-search-advertising/references/shopping-and-feeds.md`. Marketplace fees and the NPS Act text `NOT_ASSESSED` |
| T09 AI transparency and provenance | DONE_WITH_LIMITATIONS | `policy-ai-content-ethics/references/ai-transparency-and-provenance.md` (IAB v2 PDF read; the technical method is verified, not `NOT_ASSESSED`); `playbook-crisis-communications/references/synthetic-media-and-deepfake-protocol.md`; pointers in readiness diagnostic, prompt library, paid social, hook lab, influencer. EUR-Lex Art. 50 text and platform ad-policy pages `NOT_ASSESSED`. Draft-era "Article 4 / 28b(4)" wording corrected in two policy references |
| T10 agency commercial governance | DONE_WITH_LIMITATIONS | `playbook-agency-operations/references/commercial-governance-and-contracts.md` and `certification-and-competency-register.md` (single owner of certification facts); `biz-dev-pricing-menu/references/remuneration-models-evidence.md`; `biz-dev-proposal/references/pitch-conduct-and-ai-clauses.md`; pointers in credentials, retainer management, training. Member-only contract texts used through published summaries |
| T11 PR evaluation | DONE | `playbook-pr-publicity/references/pr-evaluation.md` (AMEC's Barcelona Principles 4.0 eBook read); the "show AVE as context" line removed |
| T12 THIN rows | DONE | spam policy, preview controls, Core Web Vitals, testing tool, Meta unoriginal content, ICC influencer articles, UCC online publishers, data excise; see the re-score |
| T13 register | DONE | 91 records added (91 → 182); every record has scope, publication and access dates, freshness class, review date and support status. `check_source_freshness.py` PASS; `--as-of 2027-06-30` still FAILs as designed |
| T14 count and fixtures | DONE | active 112; `quality-baseline.json`, `docs/skill-aliases.yml`, README, AGENTS routing lines, `.claude-plugin/plugin.json` (regenerated; the generator's shortened hooks text restored) and both marketplace counts updated; fixtures 359 → 387 |
| Benchmark re-score | DONE | [benchmark-rescore.md](benchmark-rescore.md): GAP 35 → 0, THIN 54 → 4 (each `NOT_ASSESSED`-bound), STRONG 44 → 129; East Africa 0 GAP, 0 DEFECT |

## Hand-offs closed

| From | Item | Disposition |
|---|---|---|
| S08 | Three "not for" clauses naming current owners | `advertising-attribution-and-measurement` → `marketing-mix-modelling`; `media-planning` → `programmatic-and-brand-safety`; `04-brand-voice-intake` → `brand-strategy-and-distinctive-assets`; owned negatives added for each (the old negatives stay as plain collision tests) |
| S08 | `caption-writer` Instagram hashtags 5–10 vs the five-tag cap | Primary @creators statement read (`INSTAGRAM-HASHTAG-LIMIT-PRIMARY`); every live file recommending more than five Instagram tags corrected (caption-writer ×3, meta-algorithm-guide ×2, content repurposing, platform-instagram, anti-ai-slop, brand-voice style guide). Rollout reaching every account `NOT_ASSESSED` |
| S08 | `ecommerce-brand-differentiation` merge | Done (T02) |
| S09 | "Noticed, not changed" backlog | Triaged in [S09-backlog-triage.md](S09-backlog-triage.md): currency items fixed and registered (for example Brand24/Mention pricing, YouTube Shorts length now 3 minutes, podcast download figure marked as an unsourced assumption, a PL-05 citation now `UG-DIGITAL-TAX-ADS-2026`); citation/edition and doctrine-contradiction items listed for S13 |

## Routing (lexical proxy)

| Measure | Before (S09) | After S10 |
|---|---|---|
| Fixtures | 359 | 387 |
| Top-3 | 100 % | 100 % |
| p@1 | 93.9 % (337/359) | **94.6 %** (366/387); floor 92 |
| Owned negatives | 110/110 | 120/120 |
| Fixture lint | 0 | 0 |

`marketing-mix-modelling` first pulled generic prompts (its `Use When` was full of "we", "how much", "each", "last"); its description and `Use When` were retuned to econometric vocabulary before the gate run. New skills' cross-engine similarity: none reaches the 0.5 warning band (union scan), so no S11 declaration is needed at 0.75; S11 still re-baselines.

## Gate block

[gate-block-2026-09-29.txt](gate-block-2026-09-29.txt): validator 112/112, 0 failures, median 121; routing as above; aliases 83 routes, 0 findings; pytest 68 passed; unittest OK; freshness PASS (182) and the negative run FAILs as designed; ingestion guardrail 0; scaffolding gated median 1.4 %, 0 files over 300; `git diff --check` clean. Coordination package: render check 0 findings (12 repositories); marketplace 23 ok, 0 drift; collisions PASS, 0 undeclared ≥ 0.75; routing ratchet PASS; book-extraction check 0 findings. Skill-safety audit (read-only) on each NEW skill: Safe.

## Cross-engine change (`chwezi-engine-agents`)

- `.claude-plugin/marketplace.json`: social plugin count text 110 → 112 (keeps `--check-marketplace` at 0 drift). `docs/engine-tours/social-media-skills.*` still say 110: S12 regenerates.

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`** (no blocker, no major). The reviewer read the three NEW skills and all their references, the merge against HEAD with all 27 preservation-map rows, and sampled the reference extensions; live spot-checks (Meridian data pages, Robyn analyst's guide, LinkedIn 95:5, WFA GARM notice, ISBA/PwC study PDF, Ehrenberg-Bass distinctive assets, Afrobarometer, Gmail sender rules, Core Web Vitals, IAB AI disclosure v2, EU Art. 50 FAQ, WhatsApp 7-day window) all matched the text.

| # | Finding (MINOR) | Disposition |
|---|---|---|
| 1 | `ecommerce-differentiation-method.md` §2 carries Verma's nine-intangible catalogue with the book's case examples, close to a digest (moved unchanged from the retired skill) | Carried to S13 (rewrite in the engine's words); moved text kept verbatim per the runbook |
| 2 | Same file: positive typeface claim ("sans-serif reads more clearly") | Fixed: typeface choice briefed to the design engine |
| 3 | Programmatic SKILL.md has an extra "Core terms at a glance" section | Accepted: same pattern as the exemplar's "Core formulas"; validator-compliant |
| 4 | `MRC-VIEWABILITY-2015` cites a document dated 30 Jun 2014 | Fixed: "hosted by IAB in 2015" |
| 5 | Robyn ratio misstated | Fixed: observations roughly 7–10 times the variables |
| 6 | Meridian 15 points per parameter overstated | Fixed: worked example, directional use |
| 7 | `IAB-TECHLAB-SCHAIN` marked verified on a partial read | Fixed: partial |
| 8 | `WHATSAPP-RATE-CARD-EA` lacks the country-to-market mapping | Fixed: mapping added to the note |
| 9 | Companion records (`IAB-AI-DISCLOSURE-2026`/`-V2-2026`, `ICC-CODE-2024-TEXT`/`PREMIUM-ICC-2026`, `INSTAGRAM-HASHTAG-LIMIT-PRIMARY`/`-2025`) | Carried to S11/S13: each is labelled as the primary or superseding companion; fold or mark superseded there |
| 10 | EU Art. 50 grace period stated without scope | Fixed: scope and origin added, primary text `NOT_ASSESSED` |
| 11 | "verified" for a partial Meta record | Fixed |
| 12 | Email 5–10 % holdout "default" vs "size by power" | Fixed: starting input to the power calculation |
| 13 | Process wording ("proposed in this phase", "owned by another worker"); AMEC framework status | Fixed in five references |
| 14 | `youtube-channel-playbook.md` Shorts "under 60 seconds" | Fixed |
| 15 | Inverted WhatsApp delivery formula; undated TikTok Shop claim | Fixed; dispositions table added to the triage file |
| 16 | Inactive aliases name the retired skill or its moved reference | Carried to S11 (cosmetic; aliases are historical) |

Two older fixtures (`media-planning-not-total-budget`, `advertising-attribution-and-measurement-not-roi`) now guard boundaries the descriptions no longer name; kept as collision tests by design.

## Open items

- `NOT_ASSESSED` evidence gaps carried: Gartner peer budget benchmark; IAB Tech Lab CTV portfolio text; successor to a shared GARM floor; GSMA 2025 edition; NPS Act and marketplace fees; EUR-Lex Art. 50; platform AI ad-policy pages; Meta certification validity; CIM primary framework; UCC influencer authorisation; Uganda data excise primary text.
- Routing misses for S11 (honest prompts that do not rank the owner first, because S10 did not change existing routing text): deepfake scam on WhatsApp → crisis; agency audit rights and expiring certifications → agency operations; podcast download counting → video strategy; WhatsApp split test → testing framework.
- Benchmark text corrections for S13: WhatsApp 7-day window; CIPR "ramp-up"; clean-room source.
- Three decision tables run to 9 rows (`meta-budget-planner`, `playbook-crisis-communications`, `ai-readiness-diagnostic`): over the lean template's 4–8 guide, not a validator finding.
