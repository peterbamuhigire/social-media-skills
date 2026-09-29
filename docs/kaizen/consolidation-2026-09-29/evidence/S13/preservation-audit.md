# S13-T02 preservation audit

- **Date:** 29 September 2026. Tree: `e7d68fd` (S12) plus the uncommitted S13 working set.
- **Auditor:** S13 executor, audit fork (read-only on skills; no content change was needed).
- **Scope:** 39 of the 83 preservation maps in [`../../preservation/`](../../preservation/): every map whose source had reads above 0 in the Aug–Sep 2026 usage scan (19), plus a sample of 20 more, stratified by phase.
- **Verdict:** **0 dropped items.** Every audited item exists in the owner skill (its `SKILL.md` or `references/`), either as mapped or where S09 later moved it. No fix was needed and no file other than this one was written.

## 1. Method

The audit ran two independent checks on each map. Neither trusts the map's own "ticked" column.

1. **Item-row check (map → owner).** For every item row, the auditor:
   - extracted its distinctive terms: quoted phrases, content words of five or more letters, figures and citation surnames;
   - searched for them in the owner skill's whole directory (`SKILL.md` plus `references/`, excluding `ALIAS.md`), because S09 (lean template) moved much `SKILL.md` text into new reference files after the maps were written.

   Rows under 60 % term coverage were read by hand. Every `references/<file>.md` named in a map was also resolved on disk.
2. **Line check (historical `ALIAS.md` → owner).** This check guards against map rows that summarise too coarsely.
   - Each retired source's verbatim historical text (`ALIAS.md`, kept per D-SK-03) was split into content lines longer than 50 characters.
   - Lines found in 5 or more skill or alias files were excluded, because they are scaffolding.
   - A line counted as carried when at least 60 % of its content words appear in the owner directory.
   - Every line below that bar was read by hand against the owner text.

`DROPPED-DUPLICATE-OF` rows were checked for the named equivalent text. The shared-scaffolding rows are the generic `Use When`, generic decision rows and anti-patterns, "read next" and `AGENTS.md` links. Their named target text was the templated dual-compat block, and S09 replaced that block under D-SK-06: the canonical Capability and Permission Boundaries and Degraded Mode sentences in `docs/standards/skill-authoring-standard.md` now carry it. The engine-wide sourcing rules in `AGENTS.md` (the attribution and "never fabricate a citation" rules) and `rules/common/core.md` also cover it. These rows are therefore not unique knowledge; see limitation 1.

This is a lexical check. It proves presence, not equal quality of paraphrase; the hand reads cover the flagged rows only.

## 2. Sample

| Selection reason | Maps |
|---|---|
| Reads > 0 (all 19) | `ai-content-humaniser` (6), `ai-influencer-strategy` (4), `ai-synthetic-personas` (3), `ai-whatsapp-chatbot-design` (2), `biz-dev-practitioner-positioning` (1), `copywriting-brochure` (3), `direct-mail-writer` (7), `meta-cohort-analysis` (3), `meta-dashboard-design` (2), `meta-social-media-roi-business-case` (2), `owned-media-strategy` (2), `platform-linkedin-company-pages` (1), `playbook-audacious-content` (1), `playbook-email-funnel` (1), `playbook-location-based-marketing` (2), `playbook-question-engine` (1), `playbook-webinars-live-events` (1), `playbook-whatsapp-business` (2), `premium-social-selling` (1) |
| Stratified, S02 (4) | `ai-agentic-marketing-workflows`, `ai-vendor-evaluation`, `policy-ai-ip-and-copyright`, `ai-data-foundation-audit` |
| Stratified, S03 (3) | `content-writing-category`, `blog-idea-generator`, `prompt-library-image-audio-video` |
| Stratified, S04 (3) | `meta-utm-tracking`, `meta-lead-scoring`, `meta-analytics-privacy` |
| Stratified, S05 (4) | `platform-instagram-growth`, `playbook-social-media-brand-style-guide`, `00-client-intake`, `playbook-ugc-strategy` |
| Stratified, S06 (3) | `framework-community-trust`, `playbook-social-media-governance`, `playbook-word-of-mouth-strategy` |
| Stratified, S07 (2) | `biz-dev-case-study`, `training-diy-content` |
| Stratified, S10 (1) | `ecommerce-brand-differentiation` (reads `NOT_ASSESSED` in its map) |

Together with the reads-above-0 maps, the audit covers every phase that merged: S02 8, S03 6, S04 6, S05 11, S06 5, S07 2 and S10 1.

## 3. Per-map results

Columns:

- **Items**: item rows in the map.
- **Rows flagged**: rows under 60 % term coverage in the owner directory, read by hand.
- **Lines**: historical content lines checked.
- **Lines flagged**: lines under 60 %, read by hand.
- **Result**: after the hand read.

| Map | Owner | Items | Rows flagged | Lines | Lines flagged | Result |
|---|---|---|---|---|---|---|
| `ai-content-humaniser` | `skills/ai-marketing/anti-ai-slop` | 49 | 0 | 242 | 0 | All carried; the 24 banned words, 10 phrases, transitions and hedges (rows 15–16, dropped as duplicates) are all present in the owner |
| `ai-influencer-strategy` | `skills/pipeline/08-influencer-marketing-strategy` | 27 | 1 | 78 | 1 | All carried; flags were a routing-link row and a generic workflow line |
| `ai-synthetic-personas` | `skills/pipeline/03-audience-personas` | 23 | 2 | 100 | 1 | All carried; the flagged row is the "Quality Criteria (8 items)" label, whose content terms are present |
| `ai-whatsapp-chatbot-design` | `skills/playbooks/playbook-chatbot-strategy` | 36 | 3 | 56 | 4 | All carried; flags were generic scaffolding (decision rows 3–4, anti-patterns 5–9); the stop rule and the permission rule are now in the owner's Required Inputs, Workflow and the canonical sentences |
| `biz-dev-practitioner-positioning` | `skills/business-development/biz-dev-positioning` | 35 | 1 | 133 | 5 | All carried; niche-statement output, viability test and the "specific to East African professional services" check are in `practitioner-positioning.md` §§ viability, checklist |
| `copywriting-brochure` | `skills/content-writing/premium-commercial-writing` | 16 | 0 | 68 | 0 | All carried |
| `direct-mail-writer` | `skills/content-writing/direct-response-funnel-copy` | 20 | 0 | 73 | 3 | All carried; flags were scaffolding lines |
| `meta-cohort-analysis` | `skills/meta-analytics-ops/meta-roi-framework` | 18 | 0 | 62 | 1 | All carried (flag: routing line) |
| `meta-dashboard-design` | `skills/meta-analytics-ops/meta-reporting` | 16 | 0 | 66 | 1 | All carried (flag: routing line) |
| `meta-social-media-roi-business-case` | `skills/meta-analytics-ops/meta-roi-framework` | 19 | 0 | 121 | 1 | All carried (flag: routing line) |
| `owned-media-strategy` | `skills/strategy/peso-integrated-strategy` | 36 | 0 | 84 | 0 | All carried |
| `platform-linkedin-company-pages` | `skills/platforms/platform-linkedin` | 43 | 1 | 148 | 2 | All carried; the "below 1,000 followers, no Showcase Pages" and "bespoke services, no Product Pages" rules are in `company-pages-showcase-and-events.md` decision rows |
| `playbook-audacious-content` | `skills/playbooks/playbook-viral-content-design` | 26 | 2 | 111 | 0 | All carried (flags: label rows) |
| `playbook-email-funnel` | `skills/pipeline/07-email-marketing-strategy` | 18 | 0 | 65 | 1 | All carried; "single column only" is in `email-funnel-build-sequence.md` |
| `playbook-location-based-marketing` | `skills/platforms/platform-google-business-profile` | 34 | 1 | 81 | 0 | All carried (flag: label row) |
| `playbook-question-engine` | `skills/pipeline/12-website-content-plan` | 30 | 1 | 104 | 0 | All carried (flag: label row) |
| `playbook-webinars-live-events` | `skills/strategy/strategy-experiential-marketing` | 30 | 0 | 100 | 0 | All carried |
| `playbook-whatsapp-business` | `skills/platforms/platform-whatsapp` | 25 | 0 | 66 | 0 | All carried |
| `premium-social-selling` | `skills/playbooks/playbook-social-selling` | 14 | 3 | 22 | 0 | All carried (flags: "Quality Bar", "Citations" and `AGENTS.md` label rows) |
| `ai-agentic-marketing-workflows` | `skills/playbooks/playbook-marketing-automation` | 36 | 1 | 143 | 1 | All carried; flags were generic anti-patterns |
| `ai-vendor-evaluation` | `skills/meta-analytics-ops/meta-tools-stack-evaluation` | 36 | 0 | 174 | 3 | All carried; the humaniser standard for content tools is now the anti-slop human-voice standard in `ai-vendor-due-diligence.md` |
| `policy-ai-ip-and-copyright` | `skills/policies/policy-ai-content-ethics` | 32 | 0 | 71 | 0 | All carried |
| `ai-data-foundation-audit` | `skills/ai-marketing/ai-readiness-diagnostic` | 20 | 0 | 129 | 1 | All carried (flag: scaffolding) |
| `content-writing-category` | `skills/content-writing/premium-commercial-writing` | 41 | 0 | 182 | 0 | All carried |
| `blog-idea-generator` | `skills/content-writing/content-ideas` | 32 | 1 | 107 | 3 | All carried. The missing `headline-mastery.md` pointer is replaced by `headline-and-hook-families.md`, as the map records |
| `prompt-library-image-audio-video` | `skills/content-writing/prompt-engineering-library` | 25 | 1 | 92 | 0 | All carried |
| `meta-utm-tracking` | `skills/meta-analytics-ops/measurement-tracking-plan` | 23 | 1 | 101 | 3 | All carried; the "real East African contexts, no `mywebsite.com`" check is in `utm-convention-and-campaign-register.md` |
| `meta-analytics-privacy` | `skills/meta-analytics-ops/measurement-tracking-plan` | 30 | 1 | 72 | 5 | All carried. The Usercentrics option and the GA4 configuration steps are in `consent-retention-and-sharing-review.md`. The source's IP-masking step was deliberately corrected there, because GA4 does not store IP addresses (register `GA4-IP-2026`). That is a currency correction, not a drop |
| `platform-instagram-growth` | `skills/platforms/platform-instagram` | 50 | 1 | 202 | 4 | All carried; the no-slow-intro hook, the loop and the collaboration tactics are in `growth-diagnosis-and-experiments.md` |
| `playbook-social-media-brand-style-guide` | `skills/pipeline/04-brand-voice-intake` | 43 | 0 | 173 | 0 | All carried |
| `00-client-intake` | `skills/pipeline/01-client-brief` | 19 | 0 | 69 | 0 | All carried |
| `playbook-ugc-strategy` | `skills/pipeline/08-influencer-marketing-strategy` | 24 | 0 | 62 | 0 | All carried |
| `framework-community-trust` | `skills/playbooks/playbook-community-management` | 22 | 1 | 104 | 4 | All carried (flags: scaffolding and routing lines) |
| `playbook-social-media-governance` | `skills/playbooks/playbook-social-media-policy` | 33 | 0 | 158 | 0 | All carried |
| `playbook-word-of-mouth-strategy` | `skills/strategy/strategy-ewom-reviews` | 38 | 1 | 168 | 2 | All carried; "viral content vs WOM seeding" is in `word-of-mouth-and-referral-design.md` § 6 (comparison table and East Africa line) |
| `biz-dev-case-study` | `skills/business-development/biz-dev-credentials` | 25 | 0 | 57 | 3 | All carried (flags: scaffolding) |
| `training-diy-content` | `skills/training/training-client-team` | 13 | 1 | 18 | 0 | All carried (flag: "Citations" label row) |
| `ecommerce-brand-differentiation` | `skills/strategy/brand-strategy-and-distinctive-assets` | 27 | 1 | 68 | 0 | All carried (flag: the canonical boundary sentence, which is the standard sentence). The Verma catalogue in `ecommerce-differentiation-method.md` is present; its S13 rewrite is out of this audit's scope |

## 4. Totals

| Measure | Value |
|---|---|
| Maps audited | 39 of 83 (19 reads-above-0 + 20 stratified) |
| Item rows checked | 1,102 (MOVED 888, MERGED-WITH-EXISTING 80, DROPPED-DUPLICATE-OF 93, n/a or STAYS 41) |
| Item rows flagged and read by hand | 25 |
| Historical content lines checked | 3,989 |
| Lines flagged and read by hand | 49 (about 40 are scaffolding or routing lines; the rest were found in the owner under different wording) |
| Named reference files resolved | 64 names; 62 on disk under the named name. The other 2 are historical names recorded in their maps: `differentiation-method.md` is now `ecommerce-differentiation-method.md`, and `headline-mastery.md` never existed in this engine and is replaced as the map records |
| Dropped unique items | **0** |
| Fixes applied | none needed |

## 5. Limitations

1. The `DROPPED-DUPLICATE-OF` scaffolding rows no longer point at verbatim target text, because S09 replaced the templated dual-compat blocks with the lean template. They are accepted here because the text was generic by construction: it was identical across the catalogue. Its obligations survive in the canonical sentences (`docs/standards/skill-authoring-standard.md`) and the engine rules in `AGENTS.md`.
2. The check is lexical. It shows that the terms are present in the owner directory, not that each paraphrase is equally good. The 44 maps outside the sample were accepted in their own phases' independent reviews and were not re-read here.
3. Reads are an Aug–Sep 2026 local usage scan, used as evidence only. The `ecommerce-brand-differentiation` reads are `NOT_ASSESSED` in its map.
