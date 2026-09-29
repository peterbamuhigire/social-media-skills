# S12 evidence: README, router, manifest, plugin and host-file regeneration

- **Phase:** Social Kaizen 2026-09-29, S12 (plan `04-phases/S12-readme-router-manifest-and-plugin-regeneration.md`).
- **Date:** 29 September 2026. **Start state:** the S11 change set (index snapshot tree `8c945d32a4e5`, uncommitted at the time; the orchestrator commits S11 and S12 separately).
- **Active skills:** 112 → 112.
- **Change classes:** metadata (README, counts, manifests, tours, graph, evidence); workflow-routing (AGENTS.md router text); external-release (marketplace text: prepared locally, ships only at push checkpoint 4 with Peter's approval).
- **Limits:** routing figures are a lexical proxy. The engine tours record the HEAD commit at generation (`973e1af` for social, because S11 and S12 were not yet committed); `generate_engine_tour.py --check` will report the social tour as stale after the commits until it is regenerated.

## Task status

| Task | Status | Evidence |
|---|---|---|
| T01 README capability table and retired routes | DONE | Category table (15 active folders + `frameworks/` aliases only; total 112) and the 112-row skill table regenerated from the filesystem; new "Retired skill routes" section lists all 83 routes from `docs/skill-aliases.yml` (retired skill → owner). Portfolio README structure kept: two-paragraph executive summary (register count 182 → 179), Installation, Capabilities, Approval boundaries, References last. References: new "Source-register sources" subsection lists the 122 register records whose URL was not yet cited (benchmark sources for brand building, MMM, programmatic and brand safety, tracking, email and WhatsApp, commerce media, AI transparency, agency governance and East African legal currency), each with its register ID. Two stale reference lines corrected: the EU AI Act line now cites Article 50 and says older material citing Article 4 (the AI-literacy duty) or draft Article 28b(4) for disclosure is incorrect and the Computer Misuse Act line notes that the 2022 Amendment Act was declared void on 17 March 2026 |
| T02 AGENTS.md | DONE | Category list notes `frameworks/` is aliases only; baseline skills point to `premium-commercial-writing/references/content-writing-standards.md` instead of the `content-writing/` category file; prefix list `00-` → `01-`, retired `framework-` and `owned-media-` prefixes removed, brand-strategy prefix and route added; Skill Categories rows corrected (content-writing contents, pipeline `01-`–`13-`, language adds French and Kiswahili, meta-utility adds `kaizen-improvement-system`, sectors lists `hospitality-hotel-restaurant`, strategy names `ecommerce-export-marketing-advisory`); "Existing Skills" table adds the four NEW skills; "absorbed `<alias>`" parentheticals removed. Check: no alias name appears anywhere in AGENTS.md, and in README only inside the Retired skill routes table. `render_host_files.py --check`: 0 findings. The advertising routing rule already named `marketing-mix-modelling`, `programmatic-and-brand-safety` and `brand-strategy-and-distinctive-assets` (S10) |
| T03 marketplace and plugin | DONE | `node scripts/generate-plugin-manifest.js --engine . --check`: `plugin.json` current, 112 skills. Engine marketplace already "112 skills …" (S10). Suite marketplace (`chwezi-engine-agents/.claude-plugin/marketplace.json`) social description hand-written (no generator writes description text) from "social media strategy, content planning, campaigns, platform playbooks" to the engine's actual scope. `--check-marketplace` (verifies the leading count only): 23 ok, 0 drift. Plugin version left at 1.1.0 (a version bump is an external-release decision) |
| T04 engine manifest and portfolio catalogue | DONE | `.skills-engine/engine-manifest.yaml`: `discovery_glob` confirmed; `source_of_truth.aliases: docs/skill-aliases.yml`; validation entries added for the routing gate (`--lint-fixtures`), the alias gate (`check_skill_aliases.py`) and source freshness. `chwezi-engine-agents/catalog/engines.yaml`: social validator list adds `check_skill_aliases.py` and uses the `--lint-fixtures` form of the routing test (so the tour lists it once). `validate-catalog.ps1`: PASS; render check 0 findings. `readiness/run_tier1.py` exists only as M10-14 evidence, so it was not used (`NOT_ASSESSED`) |
| T05 shared-assets register | NOT APPLICABLE | `catalog/shared-assets.yaml` tracks byte, block and registered-variant copies; each engine's `docs/skill-aliases.yml` is engine-specific data, not a shared copy, so there is nothing to register. Render check 0 findings |
| T06 NEXT_FEATURES | DONE | `docs/plans/NEXT_FEATURES.md`: "September 2026 — Consolidation 191 → 112" entry |
| T07 count-surface test | DONE | `tests/test_engine_quality.py`: `count_surface_findings()` plus `test_current_active_count_matches_filesystem_and_documented_surfaces` (executive-summary count, capability sentence, category rows and total, the (category, skill) pairs of the skill table, the (retired skill, owner) pairs of the retired-route table against `docs/skill-aliases.yml`, marketplace leading count, `plugin.json` skill list); a scratch mutation run confirmed that a wrong owner, a skill filed under the wrong category and a wrong summary count each produce a finding and `test_count_surface_check_fails_on_a_mutated_count` (a copy with the README total or the marketplace count off by one fails). Both pass |
| Extra: engine tours | DONE | `generate_engine_tour.py --all` regenerated all 12 tours (every other engine repository was clean, so each tour reflects its HEAD); social tour now says 112 skills and lists the three new gate commands. `--all --check`: PASS, 0 dangling paths, 0 missing gate commands |
| Extra: skill graph | DONE | `docs/skill-graph/skill-graph.json` regenerated with `skill_graph.py` (report kept out of the repository); 112 social skill nodes. Like the tours, it was built from the uncommitted working tree but records the HEAD commit (`973e1af`) |

## Files changed

- `social-media-skills`: `README.md`, `AGENTS.md`, `.skills-engine/engine-manifest.yaml`, `docs/plans/NEXT_FEATURES.md`, `tests/test_engine_quality.py`, `docs/kaizen/consolidation-2026-09-29/execution-log.md`, this evidence folder, and `evidence/S11/gate-block-2026-09-29.txt` (host paths in the log text replaced with `<workspace>`, portable-links rule).
- `chwezi-engine-agents`: `.claude-plugin/marketplace.json`, `catalog/engines.yaml`, `docs/engine-tours/*.md` and `*.json` (24 files), `docs/skill-graph/skill-graph.json`.

## Gate block

[gate-block-2026-09-29.txt](gate-block-2026-09-29.txt): validator 112/112, 0 failures; routing 392/392 top-3, p@1 94.9 % (floor 92), owned negatives 121/121, lint 0; aliases 83 routes, 0 findings; pytest 70 passed; unittest OK; freshness PASS (179); ingestion guardrail 0; scaffolding gated median 1.4 %, 0 over 300; `plugin.json` current; `git diff --check` clean. Coordination package: render check 0 findings (social and all 12 repositories); marketplace 23 ok, 0 drift; collisions PASS, 0 undeclared; routing ratchet PASS; book-extraction check 0 findings; engine tours PASS; catalogue schema PASS; pytest 162 passed.

## Open items

- Regenerate the social engine tour after the S11 and S12 commits if an exact commit hash in the tour is wanted.
- Marketplace text and all of S11–S12 reach public `main` only at push checkpoint 4 (Peter).

## Reviewer verdict

Independent review (general-purpose agent, 29 Sep 2026): **ACCEPT_WITH_DOCUMENTED_LIMITATIONS**, no blocking finding, four minor findings. It rechecked the README against the filesystem with its own script (112 skills, 15 folders plus `frameworks/`, 83 routes matching the registry, 122 register sources all resolving), AGENTS.md against HEAD and the filesystem, and every gate.

| # | Finding | Disposition |
|---|---|---|
| 1 | EU AI Act line called Article 4 a withdrawn draft number (it is the AI-literacy duty) | Fixed in README and here |
| 2 | Count-surface test compared names and row counts only | Fixed: compares (category, skill) and (retired, owner) pairs and the summary count; mutation run recorded above |
| 3 | Social tour listed the routing test twice | Fixed: catalogue command uses `--lint-fixtures`; tour regenerated (4 checks) |
| 4 | T03 overstated how the suite marketplace text was made; graph commit caveat | Fixed: wording above |
