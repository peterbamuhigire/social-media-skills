# S02 evidence: AI marketing, AI governance and automation merges

- **Date:** 29 September 2026.
- **Executor:** Claude (Opus 5.5) under the Social Kaizen executor brief; the orchestrator commits. Content work for each target cluster was done by one merge worker per cluster (steps 1–5 of the [merge runbook](../../merge-runbook.md)); the coordinator did steps 6–9 and 11 (retirement, registry, referrers, fixtures, counts, manifest, evidence).
- **Start commit:** `7c60138` (S10-T01). Rollback point for the phase: the S01 acceptance commit `008896a`, or revert the S02 commit.
- **Active skills:** 191 → **176** (15 MERGE-INTO).
- **Authority:** decisions ratified by orchestrator under Peter's delegated authority, 29 Sep 2026 (D-SK-03 alias mechanism, D-SK-04 merge evidence rule; see [decisions.md](../../decisions.md)).
- **Git:** no commit, stage or `git mv`. Retirements are plain renames (`SKILL.md` → `ALIAS.md`) and moved references are plain moves; `git add -A` records them as renames (similarity 77–99 %).

## Tasks

| Task | Target | Sources → reference | Status |
|---|---|---|---|
| S02-T01 | `ai-readiness-diagnostic` | `ai-data-foundation-audit` → `data-foundation-audit.md`; `ai-data-foundation-plan` → `data-foundation-plan.md` (+ moved `data-product-and-ai-foundation-principles.md`); `ai-marketing-canvas-assessment` → `ai-marketing-canvas-scoring.md` | DONE |
| S02-T02 | `ai-use-case-mapping` | `ai-growth-systems-design` → `ai-growth-systems-design.md`; `ai-predictive-analytics-social` → `predictive-analytics-use-cases.md`; `ai-strategy-co-thinker` → `ai-strategy-co-thinking-prompts.md` | DONE |
| S02-T03 | `anti-ai-slop` | `ai-content-humaniser` → `humanising-rewrite-passes.md` | DONE |
| S02-T04 | `brand-voice-ai-training` | `ai-rag-brand-knowledge-base` → `brand-knowledge-base-rag.md` | DONE |
| S02-T05 | `meta-tools-stack-evaluation` | `ai-vendor-evaluation` → `ai-vendor-due-diligence.md`; `meta-ai-tools-audit` → `ai-tool-fit-access-cost-governance.md` | DONE |
| S02-T06 | `playbook-chatbot-strategy` | `ai-whatsapp-chatbot-design` → `whatsapp-chatbot-design.md` | DONE |
| S02-T07 | `playbook-marketing-automation` | `ai-agentic-marketing-workflows` → `agentic-workflows-and-human-checkpoints.md` (+ moved `agentic-marketing-operating-model.md`, `ai-campaign-trust-control-correction-drift.md`); `playbook-ai-automation-workflow` → `ai-automation-recipes.md` | DONE |
| S02-T08 | `policy-ai-content-ethics` | `ai-cultural-bias-audit` → `cultural-bias-audit-protocol.md`; `policy-ai-ip-and-copyright` → `ai-ip-and-copyright-policy.md` | DONE (target was 500 lines; its old §4 sector guidance moved nearly verbatim to `references/sector-specific-ai-guidance.md` to make room; now 473 lines) |
| S02-T09 | fixtures | 15 alias-routing fixtures (`alias_of`), one per source | DONE: all 15 rank 1 |
| S02-T10 | count and registry | `quality-baseline.json` and `docs/skill-aliases.yml` = 176 | DONE |

## Merges

| Source | Target | Reference | Preservation map (rows; dropped as duplicate) | Gates | Commit |
|---|---|---|---|---|---|
| `ai-data-foundation-audit` | `ai-readiness-diagnostic` | `data-foundation-audit.md` | [20; 2](../../preservation/ai-data-foundation-audit.md) | green | set by the orchestrator |
| `ai-data-foundation-plan` | `ai-readiness-diagnostic` | `data-foundation-plan.md` | [16; 2](../../preservation/ai-data-foundation-plan.md) | green | set by the orchestrator |
| `ai-marketing-canvas-assessment` | `ai-readiness-diagnostic` | `ai-marketing-canvas-scoring.md` | [18; 2](../../preservation/ai-marketing-canvas-assessment.md) | green | set by the orchestrator |
| `ai-growth-systems-design` | `ai-use-case-mapping` | `ai-growth-systems-design.md` | [30; 2](../../preservation/ai-growth-systems-design.md) | green | set by the orchestrator |
| `ai-predictive-analytics-social` | `ai-use-case-mapping` | `predictive-analytics-use-cases.md` | [32; 2](../../preservation/ai-predictive-analytics-social.md) | green | set by the orchestrator |
| `ai-strategy-co-thinker` | `ai-use-case-mapping` | `ai-strategy-co-thinking-prompts.md` | [29; 2](../../preservation/ai-strategy-co-thinker.md) | green | set by the orchestrator |
| `ai-content-humaniser` | `anti-ai-slop` | `humanising-rewrite-passes.md` | [49; 8](../../preservation/ai-content-humaniser.md) | green | set by the orchestrator |
| `ai-rag-brand-knowledge-base` | `brand-voice-ai-training` | `brand-knowledge-base-rag.md` | [24; 5](../../preservation/ai-rag-brand-knowledge-base.md) | green | set by the orchestrator |
| `ai-vendor-evaluation` | `meta-tools-stack-evaluation` | `ai-vendor-due-diligence.md` | [36; 4](../../preservation/ai-vendor-evaluation.md) | green | set by the orchestrator |
| `meta-ai-tools-audit` | `meta-tools-stack-evaluation` | `ai-tool-fit-access-cost-governance.md` | [29; 4](../../preservation/meta-ai-tools-audit.md) | green | set by the orchestrator |
| `ai-whatsapp-chatbot-design` | `playbook-chatbot-strategy` | `whatsapp-chatbot-design.md` | [36; 10](../../preservation/ai-whatsapp-chatbot-design.md) | green | set by the orchestrator |
| `ai-agentic-marketing-workflows` | `playbook-marketing-automation` | `agentic-workflows-and-human-checkpoints.md` | [36; 9](../../preservation/ai-agentic-marketing-workflows.md) | green | set by the orchestrator |
| `playbook-ai-automation-workflow` | `playbook-marketing-automation` | `ai-automation-recipes.md` | [25; 4](../../preservation/playbook-ai-automation-workflow.md) | green | set by the orchestrator |
| `ai-cultural-bias-audit` | `policy-ai-content-ethics` | `cultural-bias-audit-protocol.md` | [28; 2](../../preservation/ai-cultural-bias-audit.md) | green | set by the orchestrator |
| `policy-ai-ip-and-copyright` | `policy-ai-content-ethics` | `ai-ip-and-copyright-policy.md` | [32; 3](../../preservation/policy-ai-ip-and-copyright.md) | green | set by the orchestrator |

"Dropped" counts are the grep count of rows containing `DROPPED`; every dropped row names the equivalent target text (mostly the shared contract scaffolding, the templated decision rows and the five generic anti-patterns, which are identical across the catalogue). Source-register IDs carried: `WHATSAPP-USAGE-EA-2026` (WA-01, review 2026-12-25, current). The other 14 sources cite no register ID (freshness `NOT_ASSESSED`).

## Referrers re-pointed (live files)

`AGENTS.md` (anti-slop gate paragraph), `README.md` (counts, category table, 15 rows removed, alias sentence), `.claude-plugin/plugin.json` (regenerated, 176), `.claude-plugin/marketplace.json` (count text), and these skills: `advertising/creative-brief-and-big-idea`, `ai-marketing/ai-slop-audit`, `ai-marketing/ai-use-case-mapping` (+ `references/predictive-analytics-use-cases.md`), `ai-marketing/anti-ai-slop` (+ `references/humanising-rewrite-passes.md`), `content-writing/SKILL.md`, `blog-writer`, `caption-writer`, `content-ideas`, `content-whitepaper-ebook`, `direct-response-funnel-copy`, `email-copywriter`, `meta-evergreen-content-strategy`, `playbook-ai-content-workflow`, `playbook-audacious-content`, `playbook-daily-operations-routine`, `playbook-white-label-partnerships`, `training-ai-foundations` (+ `references/tools-and-human-review.md`), `training-ai-prompt-writing` (+ `references/copy-frameworks-and-practice.md`); plus `playbook-chatbot-strategy/references/whatsapp-chatbot-design.md` (RAG link to the new reference).

Historical records (`docs/engine-upgrade-july-2026/`, `docs/plans/`, `docs/gap-analysis-*`, `docs/march-20-review.md`, `docs/kaizen/`) keep the old names as history, per the runbook step 7.

Phase check (runbook step 7, live paths `skills AGENTS.md README.md CLAUDE.md rules prompts .claude-plugin docs/quality-gates docs/standards docs/templates docs/evidence-packs docs/world-class-exemplars docs/source-registers`): `grep "<source>/SKILL.md"` and `grep "<source>/references"` return nothing for all 15 sources (excluding `ALIAS.md` and provenance lines).

## Routing widening (minimal, S08 finalises)

Each target gained one `Use When` bullet per source in the old job's words, ending "(formerly `<source>`)", and a few description words. Without the bullets 7 of 15 alias fixtures missed the top 3, because the lexical harness scores only name, description and `Use When`.

## Alias fixtures (`tests/routing-fixtures.json`)

| Fixture id | Expected | Rank |
|---|---|---|
| `alias-ai-data-foundation-audit` | `ai-readiness-diagnostic` | 1 |
| `alias-ai-data-foundation-plan` | `ai-readiness-diagnostic` | 1 |
| `alias-ai-marketing-canvas-assessment` | `ai-readiness-diagnostic` | 1 |
| `alias-ai-growth-systems-design` | `ai-use-case-mapping` | 1 |
| `alias-ai-predictive-analytics-social` | `ai-use-case-mapping` | 1 |
| `alias-ai-strategy-co-thinker` | `ai-use-case-mapping` | 1 |
| `alias-ai-content-humaniser` | `anti-ai-slop` | 1 |
| `alias-ai-rag-brand-knowledge-base` | `brand-voice-ai-training` | 1 |
| `alias-ai-vendor-evaluation` | `meta-tools-stack-evaluation` | 1 |
| `alias-meta-ai-tools-audit` | `meta-tools-stack-evaluation` | 1 |
| `alias-ai-whatsapp-chatbot-design` | `playbook-chatbot-strategy` | 1 |
| `alias-ai-agentic-marketing-workflows` | `playbook-marketing-automation` | 1 |
| `alias-playbook-ai-automation-workflow` | `playbook-marketing-automation` | 1 |
| `alias-ai-cultural-bias-audit` | `policy-ai-content-ethics` | 1 |
| `alias-policy-ai-ip-and-copyright` | `policy-ai-content-ethics` | 1 |

No existing fixture had a source as `expected`.

## Gate block (merge runbook, `--min-rank1 91`)

Full output: [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt).

| Check | Before (HEAD `7c60138`) | After S02 |
|---|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | 191 compliant, 0 failures | **176 compliant, 0 failures** |
| `routing_smoke_test.py --min-rank1 91 --lint-fixtures` | 56/56 top-3; p@1 51/56 (91.1 %) | **71/71 top-3 = 1.000; p@1 66/71 (93.0 %)**; lint 0 |
| `check_skill_aliases.py` | routes 0, findings 0 | **routes 15, findings 0, active 176** |
| `pytest -q tests` / `unittest discover` | 49 passed / OK | 49 passed / OK |
| `check_source_freshness.py` | PASS (76) | PASS (76) |
| `source_ingestion_guardrail.py` | 0 findings | 0 findings |
| `git diff --check` | clean | clean |
| `render_host_files.py --check` (engine and workspace) | findings 0 | findings 0 (after the marketplace count text was set to 176) |
| `generate-plugin-manifest.js --check-marketplace` | 23 ok, 0 drift | 23 ok, 0 drift |
| `validate-runtime-skill-budget.py --collisions` | PASS, 0 undeclared ≥ 0.75 | PASS, 0 undeclared ≥ 0.75 (skills 1154) |
| `validate-routing-baseline.py` | PASS | PASS |
| `validate-no-book-extractions.py` | roots 12, findings 0 | roots 12, findings 0 |
| `lexical_routing.py --collisions` | exit 0 | exit 0 |

Routing figures are a lexical proxy, not live routing. Model-executed behavioural runs: `NOT_ASSESSED (zero-spend rule)`.

## Open items and limitations

- **Citation conflicts carried, not resolved** (flagged in the references for checking before external use): Farri and Rosani (2025) and Nayebi (2025) appear with two different initials and titles across the two automation sources; Ching and Mothi (2025) initials differ between `policy-ai-content-ethics` and its merged sources; Venkatesan and Lecinski (2026) publisher given as Stanford University Press and Stanford Business Books; WGA "Master" versus "Minimum" Basic Agreement.
- **EU AI Act numbering:** the IP reference carries a verification note that the final Regulation (EU) 2024/1689 uses Article 50 for transparency; the target's §2E uses draft numbering. Correction is S10 gap-fill work (benchmark gap 10), not S02.
- **Additions beyond the sources:** verify-before-quoting notes on tool prices, a consent caveat on data monetisation, a counsel note on Uganda DPA 2019 wording, and one new policy note (Uganda, Kenya and Tanzania treated as less established jurisdictions for the IP-solicitor referral). Each is marked in the reference.
- `docs/engine-tours/social-media-skills.{json,md}` in `chwezi-engine-agents` still state 191; no gate checks them; S12 regenerates them.
- **Unplanned but necessary move:** `policy-ai-content-ethics` was exactly 500 lines, so its old §4 (sector-specific AI guidance) moved nearly verbatim, with a provenance line, to `references/sector-specific-ai-guidance.md`; §4 in SKILL.md is now a pointer. Accepted by the coordinator under phase §8 ("detail stays in `references/`"); no text was dropped.
- **Ching and Mothi (2025):** the target's initials were aligned to the merged sources' form (V. and D.); external verification of the author initials is `NOT_ASSESSED`.

## Independent review

Reviewer: independent review agent (Claude Opus 5.5, read-only), 29 Sep 2026. **Phase verdict: `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`.** No blocking finding and no substantive loss; the reviewer sampled at least five specific facts per source (checklists, thresholds, UGX figures, citations, East Africa details) and found each in its destination. Per source: 12 `ACCEPT`; `playbook-ai-automation-workflow`, `ai-cultural-bias-audit` and `policy-ai-ip-and-copyright` `ACCEPT_WITH_DOCUMENTED_LIMITATIONS` (the citation, EU AI Act numbering and §4-move items above). All 15 preservation maps are ticked and signed.

Minor findings fixed after review (29 Sep 2026):

| Finding | Fix |
|---|---|
| Invented rule in `ai-use-case-mapping/references/ai-growth-systems-design.md` ("stays in the map as Low priority or is deferred") | Deleted |
| Prices called "snapshots at 7c60138" in `ai-tool-fit-access-cost-governance.md` although the source figures are undated | Reworded to "undated figures carried from the source skill; reconfirm" |
| Checklist in `whatsapp-chatbot-design.md` asked for 4 KPIs "with targets" when the source gives numeric targets for 2 | Reworded to "each with a target agreed with the client" |
| "Native-language review" (agentic source anti-pattern) had no real equivalent in the target | Added to the `playbook-marketing-automation` anti-pattern; map row 13 updated |
| Ching/Mothi initials differed between target and sources | Target aligned to the sources' form |
| EU AI Act §2E stated draft article numbers as fact | §2E now carries a verification pointer to the numbering note (Article 50 in Regulation (EU) 2024/1689) |
| Dropped "harder to detect" claim not recorded | Recorded in humaniser map row 37 |
