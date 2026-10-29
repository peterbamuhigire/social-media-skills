# Social-media engine baseline — 2026-10-29

This is a fresh read-only assessment frozen on 2026-10-29 before implementation. It uses the current checkout, freshly rerun registered checks, same-day currentness research, native install/discovery runs, and the three synthetic practitioner outputs in `00-scope-and-evidence.md`. It does not reuse the 29 September score. Scores use the Portfolio Kaizen ten-dimension frame; each deficiency names evidence and remains visible. Each dimension is equally weighted; raw total is the arithmetic mean. The Portfolio Standard publishes `min(raw, 65)`. The user's initial-cycle instruction additionally requests a separately labelled baseline cap `min(raw, 45)`; that presentation does not replace the Standard cap.

| Dimension | Score / 100 | Evidence and named deficiency |
|---|---:|---|
| Doctrine | 63 | `AGENTS.md` has market defaults, authority limits, source-currentness and anti-slop gates; the synthetic copy preserves no-proof boundaries. **Deficiency:** current-law and publish checks remain separate from operational content because this prep cannot attest real product facts or release approval. |
| Taxonomy and routing | 78 | Router maps integrated strategy, calendar, channel, media-plan, measurement and crisis tasks to dedicated skills; routing smoke logs top-3 392/392, p@1 373/392 and owned negatives 121/121 (source: `logs/routing.log`; values are lexical harness results, not live model routing). **Deficiency:** p@1 remains below the fixture's 100% top-3 result and is not behavioural proof. |
| Skill depth | 57 | Routed skill set offers specialist platform, crisis, calendar and measurement skills. **Deficiency:** no independently graded worked-example depth sample was completed in this read-only preparation; treat this dimension as limited evidence rather than assuming prior audit ratings. |
| Applied proof | 48 | Tasks include complete synthetic copy, calendar, media arithmetic and outage statements; arithmetic is reproducible in `tasks/media-plan-check.py`. **Deficiency:** no live account, audience evidence, product, actual response or campaign results; modeled reach is not an observed forecast. |
| Standards currency | 43 | Official UCC, Uganda law, FTC, Google, TikTok and LinkedIn sources reviewed; see `03-currentness.md`. **Deficiency:** freshness validator exits non-zero with 23 overdue records (`logs/freshness.log`), and Meta source could not be verified in-session. |
| Output readiness | 52 | Three substantive task outputs exist with scope, CTA, measurement definitions, incident sequence and constraints. **Deficiency:** launch copy is review-ready only; product, offer, destination, support details, permissions and account release are fictional/unverified. |
| Accessibility and inclusion | 61 | Copy uses readable language and the carousel plan calls for alt text; the fixture avoids assumptions about a specific audience cohort. **Deficiency:** no rendered assets, screen-reader review, localization check or disability-user test was available. |
| Production and handoff | 56 | Media arithmetic has a reproducible local script; incident roles and release dependencies are named. **Deficiency:** no client owner, launch gate, production asset, data instrumentation or account handoff was supplied. |
| Hygiene | 70 | Validator reports 112/112 compliant skills with zero failures; alias check reports 83 routes and zero findings (`logs/validate.log`, `logs/aliases.log`). Checkout count is 907 file entries including `.git` and 0 symlinks; after excluding `.git` and named cache/dependency folders, 868 entries remain (`logs/file-counts.json`). **Deficiency:** this count does not test future portfolio packaging behavior; preserve full-checkout count for cap compliance. |
| Safety and integrity | 57 | Copy clearly labels synthetic product/demo context; crisis text blocks unverified impact, cause and recovery claims. FTC and UCC screening sources are cited in `03-currentness.md`. **Deficiency:** Uganda-law applicability and current platform rules are not fully assessed; no real privacy incident or actual content got legal review. |
| **Raw** | **58.5** | Arithmetic: (63 + 78 + 57 + 48 + 43 + 52 + 61 + 56 + 70 + 57) ÷ 10 = 58.5. |
| **Published** | **58.5** | `min(raw, 65)` = 58.5. |
| **User-requested initial cap** | **45.0** | `min(raw, 45)` = 45.0; reported separately from the Portfolio Standard result. |

## Measured inputs and limits

| Input | Result | Source / limitation |
|---|---|---|
| Skill validator | `skills=112 compliant=112 failures=0 median_lines=121.0` | `logs/validate.log`; static contract check only. |
| Routing smoke test | 392 fixtures; top-3 1.000; p@1 373/392 (95.2%); 121/121 owned negatives; fixture lint 0 | `logs/routing.log`; lexical proxy, not behaviour. |
| Source freshness | 23 overdue source records; exit 1 | `logs/freshness.log`; currentness exceptions remain blockers. |
| Alias check | 83 routes, 0 findings, 112 active skills, cap 120 | `logs/aliases.log`. |
| Routing coverage at 3 positives + 2 owned negatives | 4/112 skills (3.6%) | Fresh rerun: `python docs/kaizen/consolidation-2026-09-29/evidence/S13/measure_routing.py <engine-root>`; only `positive` fixture types count, collision fixtures excluded. |
| Source-register size / as-of | 179 records; `as_of` 2026-09-29 | Local `docs/source-registers/source-register.json`; count is inventory metadata, not proof of current claim support. |
| Worked-example depth | NOT_ASSESSED | No independent inventory and quality sample was run in this prep. |
| Broken/machine-specific links | NOT_ASSESSED | No fresh repository-wide URL/path scan was run. |
| Dangling cross-engine references | NOT_ASSESSED | No fresh cross-engine inventory was run. |
| Tier 3 behavioural evaluation | NOT_ASSESSED | No paid model calls, live accounts or external publication. |
| Native installation and skill discovery | Claude native install exit 0; Codex native install exit 0; Codex prompt-input discovered 112/112 manifest paths, missing 0 | Offline CLI smoke tests on the frozen checkout; no network or model calls. Install logs and discovery summary are retained under `logs/`. This is not behavioural routing or output-quality evidence. |

### Blockers

- Currentness is blocked by the 23 overdue source records and the unverified Meta source, regardless of score.
- Any real use requires verified product facts, destination, budget, permissions, privacy review, current platform checks, and named release owner.
- Crisis outage language must not imply a security or privacy conclusion; a qualified incident owner and counsel review are required for a real incident involving possible personal data.
