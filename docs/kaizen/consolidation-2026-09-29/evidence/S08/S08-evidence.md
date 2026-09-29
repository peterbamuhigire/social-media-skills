# S08 evidence: description and `Use When` rewrite, with owned-negative fixtures

- **Phase:** Social Kaizen 2026-09-29, S08 (plan `04-phases/S08-description-and-use-when-rewrite.md`).
- **Date:** 29 September 2026.
- **Start commit:** `b3d0ac2`; worktree clean at start.
- **Active skills:** 110 → 110.
- **Change classes:**
  - workflow-routing: descriptions, `Use When`, `Do Not Use When`, fixtures, validator findings, p@1 floor, one `ownership.yaml` row;
  - metadata: evidence, shared-asset hashes;
  - runtime-configuration: a one-number CI edit, flagged to the orchestrator (D-SK-09).
- **Limits:** routing figures are a lexical proxy, not live routing. Model-executed behavioural runs are `NOT_ASSESSED (zero-spend rule)`.

## Task status

| Task | Status | Evidence |
|---|---|---|
| S08-T01 validator findings | DONE | See "Validator findings" below |
| S08-T02..T09 rewrite in batches | DONE (applied as one change, not eight batch commits) | All 110 active skills rewritten; KEEP skills were checked and rewritten too, because 108 of 110 failed the formula. [descriptions.csv](descriptions.csv) holds the before and after text, character count and neighbour for every skill. |
| S08-T10 fixtures | DONE | 139 → 359 fixtures; 110 of 110 skills have a positive fixture; 110 owned negatives, one per "not for" clause; 131 collision fixtures |
| S08-T11 enforce and ratchet | DONE | Findings enforced; p@1 floor 91 → 92 (D-SK-09) |
| S08-T12 collision re-scan | DONE | No undeclared pair ≥ 0.75 after one IDF-shifted non-social pair was declared (see below) |
| Extra (a): "(formerly …)" `Use When` crutches | DONE, removed | Every merged job keeps its own plain-words bullet. All 82 alias fixtures still reach the top 3 (82 of 82), so no crutch was restored. The remaining "(formerly …)" strings are in bodies and references (a reference link note, and "Brevo (formerly Sendinblue)" in tool tables), not in routing sections. |
| Extra (b): alias fixtures less echo-y | DONE | All 82 alias prompts rewritten in client language. Their trigram overlap with the owner's routing text fell from a median of 0.36 (max 0.76) to a median of 0.00, and the maximum across all 359 fixtures is 0.39. The new lint keeps it below 0.4. |
| Extra (c): dormant `consolidation_until` branch | DONE | Removed from `scripts/check_skill_aliases.py` and `scripts/validate_skill_engine.py`. Both tests now prove that a re-added key does not relax the cap. The pytest assertion `assertNotIn("consolidation_until", policy)` is kept. |

## Validator findings (S08-T01, S08-T11)

`scripts/validate_skill_engine.py` gains `template_findings()`, enforced from S08. Its findings are:

| Finding | Fires when |
|---|---|
| `description_template` | Any of the four plan template phrases appears ("is needed to produce", "operating playbook with roles, ordered actions", "channel plan covering account setup", "main deliverable concerns"), or one of three generated tails ("when its narrower outcome is requested", "neighbouring contract", "neighbouring workflow") |
| `description_formula` | The description lacks "produces", or lacks a "not for … (use `<id>`)" clause |
| `use_when_template` | Any of these appears in `Use When` or `Do Not Use When`: the plan's three generated phrases; the channel, playbook and "closer route" generators; `- Use this skill for/when`; "use the closest `playbook-*` skill". It also fires when `Use When` has fewer than 3 or more than 6 bullets, or `Do Not Use When` names fewer than 2 neighbour ids. |
| `description_neighbour_unknown` | The "not for" neighbour is not an active skill |
| `do_not_use_neighbour_unknown` | A skill id in `Do Not Use When` is not active. Engine ids (`*-skills`, `*-engine`, `*-doctrine`, `*-agents`) are skipped. Added after review finding 5 so that S10 merges must re-point these ids. |

Counts, measured with the new checker:

| When | `description_template` | `description_formula` | `use_when_template` |
|---|---|---|---|
| HEAD `b3d0ac2` (110 skills) | 73 | 109 | 99 |
| After S08 | 0 | 0 | 0 |

The HEAD figures are lower than the plan's baseline of 105 templated descriptions and 117 templated `Use When` sections because those were measured across 191 skills; S02–S07 retired 81 of them.

Tests are in `tests/test_routing_text_contract.py`:
- each finding fires on a synthetic template;
- formula-compliant text is clean;
- the fixture lint flags a slug and a copy;
- both neighbour findings fire on a synthetic repository;
- live coverage: at least 150 fixtures, at least 40 collision fixtures, every skill has a positive fixture, and every "not for" clause has its owned negative.

## Description formula and method

- **Formula:** `Use when <client-language trigger>; produces <named artefact>; not for <neighbour job> (use `<neighbour-id>`).`
- **Lengths:** 279–348 characters (median 330; limit 350).
- **Wording rules:** British spelling. No slop vocabulary; a spelling and slop scan found only false positives ("size", "prize", "kaizen").
- **Drafting:** six parallel drafting agents worked from `before.json`, the plan and the benchmark. Each wrote the two fixture prompts for a skill before drafting its description (the anti-overfitting order in plan §9).
- **Integration:** the executor integrated the drafts and tuned 25 skills where an honest prompt missed.
- **Tuning rule:** add the words a client actually uses to the owning skill's routing text; never edit the prompt to match. Examples of words added:
  - "sounds too American";
  - "like a bot wrote it";
  - the seven Ps spelled out;
  - "never comes up when people ask ChatGPT";
  - "Swahili" beside "Kiswahili";
  - "cost per lead keeps climbing".

**Neighbour departures from §6.1:** the three NEW ids do not exist yet, so each clause names the current owner:
- `advertising-attribution-and-measurement` → `meta-roi-framework`;
- `media-planning` → `advertising-strategy-and-budget`;
- `04-brand-voice-intake` → `ecommerce-brand-differentiation`.

S10 re-points these clauses to the NEW ids and adds collision fixtures for them.

The drafters chose neighbours for the KEEP skills that §6.1 does not list. Each is recorded in [descriptions.csv](descriptions.csv).

## Routing results (lexical proxy)

| Measure | HEAD `b3d0ac2` | Drafted text, before tuning | After S08 |
|---|---|---|---|
| Fixtures | 139 | 359 | 359 |
| Top-3 | 139/139 (100 %) | 337/359 (93.9 %) | **359/359 (100 %)** |
| p@1 | 135/139 (97.1 %) | 311/359 (86.6 %) | **337/359 (93.9 %)** |
| Owned negatives (expected ranks above the `negative_for` skill) | 0 | 103/110 | **110/110** |
| Fixture lint (slug, copy ≥ 0.4, ids, aliases, `negative_for`) | 24 findings under the new lint | 5 | **0** |
| Independent 60-prompt holdout, p@1 | 22/60 (36.7 %) | — | **48/60 (80.0 %)** |
| Independent 60-prompt holdout, top-3 | 33/60 (55.0 %) | — | **54/60 (90.0 %)** |

- **Fixtures file:** `tests/routing-fixtures.json` now holds 218 positive, 131 collision, 6 failure-path and 4 limited-capability fixtures. Of these, 82 are alias fixtures and 110 are owned negatives.
- **HEAD p@1 was inflated:** the 97.1 % came from alias prompts that echoed the "(formerly …)" bullets (see S06/S07 limitations).
- **Holdout independence:**
  - A separate agent wrote the holdout ([holdout-prompts.json](holdout-prompts.json)) from skill titles, `Outputs` tables and the benchmark only. It never saw descriptions, `Use When` or fixtures.
  - It is not in the fixture set and was not tuned on. It stands in for the plan's reviewer sample of 20 unseen prompts; the independent reviewer also sampled prompts of their own (see the review section).
  - The process never tuned on the holdout, but tuning words can overlap with it lexically (review finding 3). For example, "sounds too American", added to `east-african-english` from a fixture, shares the term `american` with one holdout prompt, and "like a bot wrote it" shares `wrote` with another. Read the holdout figure as strong evidence, not proof, of generalisation.
  - One tuning edit cost one holdout prompt: `h11` fell from rank 1 to 2 after the `07-email-marketing-strategy` "never sends anything" wording. That edit is recorded here, and the prompt is still in the top 3.
- **Ranker calibration trial:** adopting the union ranker's stop words was trialled and rejected. It was neutral on HEAD, but on the S08 set p@1 fell from 311 to 303 while top-3 rose from 337 to 343. The local ranker is unchanged (ledger RC-016).

**Floor ratchet (S08-T11):** measured 93.9 % minus 2, rounded down, is 91. The plan says "never below 92 if the measurement allows", and 92 needs 331 of 359 hits against 337 measured. The floor therefore moves from 91 to 92:
- `p1_floor` 0.92 in `tests/routing-fixtures.json`;
- CI `--min-rank1 92`;
- merge-runbook gate line;
- decision row D-SK-09.

The portfolio ledger rows are RC-015 to RC-017 in `chwezi-engine-agents/evals/routing/rejected-changes.md`. Social has no entry in `baseline.json` until S11, so `baseline.json` is unchanged.

## Collision re-scan (S08-T12)

Command: `validate-runtime-skill-budget.py --collisions --ownership evals/routing/ownership.yaml` (union lexical proxy).

**Portfolio totals:**
- cross-engine pairs ≥ 0.75 fell from 19 to 15;
- within-engine pairs ≥ 0.75 stayed at 16 (none involves social; the social `biz-dev-positioning` / `biz-dev-proposal` pair at 0.77 dropped out of the report).

**Mirrored-pack pairs.** The rule is that each stays below its `score_at_decision` + 0.05. All moved down:

| Pair | Before | After |
|---|---|---|
| Social ↔ proposal hospitality | 0.84 | 0.74 |
| Social ↔ business-plan hospitality | 0.81 | 0.65 |
| Social ↔ dev hospitality | 0.78 | 0.66 |
| Social ↔ design hospitality | 0.75 | 0.73 |
| Social ↔ proposal east-african-english | 0.77 | 0.64 |
| Social ↔ website east-african-english | 0.75 | 0.58 |

**Other social pairs:**
- `skill-writing` pairs fell (the website copy 0.66 → 0.54);
- blog-writer and demand-forecasting against business-plan fell (0.71 → 0.53 and 0.71 → 0.51).

**One new undeclared pair:** business-plan ↔ proposal `east-african-english`, 0.741 → 0.761. Neither copy was edited; the union IDF shift from the social rewrite lifted it. It is the same mirrored language pack, so `business-plan-skills/east-african-english` joins the existing EAE `mirrored_domain_pack` row in `ownership.yaml`, with an S08 note. The scan is now PASS with 0 undeclared pairs.

The `blog-idea-generator` row's follow-up note now records that the social description is no longer templated.

## Shared assets

`chwezi-engine-agents/catalog/shared-assets.yaml` re-registers two social variants with S08 reasons:
- `routing-smoke-test`: the owned-negative and lint additions;
- `skill-writing-skill`: the engine-local routing delta changed; the body is unchanged.

`render_host_files.py --check`: 0 findings across 12 repositories.

## Other changed files

- `docs/templates/SKILL.template.md`: the description, `Use When` and `Do Not Use When` placeholders follow the S08 formula. The old template sentence would have failed the new findings.
- `docs/standards/skill-authoring-standard.md`: one rule line naming the formula and the four findings.
- `skills/language/language-standards/SKILL.md`: its stop line keeps the publish-and-spend guard (review finding 6). The file sat at exactly 500 lines, so the new routing sections forced a small body trim to stay at the 500-line limit:
  - four legacy website-engine bullets (i18n, page-builder, seo, sector-strategies, none of which exist in this engine) became one line pointing to website-skills;
  - one paragraph break was merged.

  No guidance was dropped.
- `scripts/routing_smoke_test.py` gains:
  - the `negative_for` owned-negative evaluation and report line;
  - slug-in-prompt and routing-text-copy lint (limit 0.4; the portfolio uses 0.6);
  - `negative_for` id lint.

## Independent review

The reviewer was a separate agent. It re-ran every gate, sampled 22 skills against HEAD, scripted the formula checks across all 110 skills, and wrote 20 new prompts of its own.

**Reviewer's 20 prompts** (none in the fixtures or the holdout):
- p@1 17/20 after S08, against 4/20 on HEAD text;
- top-3 17/20 after S08, against 7/20 on HEAD text.

**Verdict:** `ACCEPT_WITH_DOCUMENTED_LIMITATIONS`, conditional on finding 1.

| # | Severity | Finding | Resolution |
|---|---|---|---|
| 1 | BLOCKING | The link to the gate-block file was broken, so the link test failed | Fixed: the gate-block file is written, and pytest and unittest were re-run |
| 2 | MINOR | Many owned negatives pass without a real contest | Recorded; handed to S11 |
| 3 | MINOR | Tuning words overlap lexically with the holdout | Recorded in the holdout note |
| 4 | MINOR | The single-character "X" token is dropped | `platform-x-twitter` wording added; ranker limit recorded |
| 5 | MINOR | `Do Not Use When` ids were not checked | Fixed: new `do_not_use_neighbour_unknown` finding, with a test |
| 6 | MINOR | `language-standards` lost its publish and spend guard | Fixed |

## Gate block (end of phase)

The full output is in [gate-block-2026-09-29.txt](gate-block-2026-09-29.txt).

**Social engine:**

| Check | Result |
|---|---|
| Validator (`--baseline`) | 110 compliant, failures 0, `failure_counts {}` |
| Routing (`--min-rank1 92 --lint-fixtures`) | 359/359 top-3; p@1 93.9 %; owned negatives 110/110; lint 0 |
| Alias check | routes 82, findings 0, active 110, cap 120 |
| pytest | 61 passed, 18 subtests |
| unittest (CI form) | 61 OK |
| Source freshness | PASS |
| Ingestion guardrail | findings 0 |
| `git diff --check` | clean |

**chwezi-engine-agents:**

| Check | Result |
|---|---|
| Render check (social engine only) | 0 findings |
| Render check (workspace) | 0 findings |
| Marketplace | 23 ok, 0 drift |
| Collisions | PASS, 0 undeclared |
| Routing ratchet | PASS |
| No book extractions | roots 12, findings 0 |
| pytest (coordination package) | 162 passed |

## Open items and limitations

- **Tier 3:** live-model routing and behaviour are `NOT_ASSESSED (zero-spend rule)`. All figures are a lexical proxy.
- **Holdout misses:** 6 of 60 holdout prompts miss the top 3. They are listed in the holdout run and left as honest misses:
  - `caption-writer` rank 5;
  - `strategy-personal-brand` rank 6;
  - `platform-tiktok` rank 7;
  - `blog-writer` rank 20;
  - `08-influencer-marketing-strategy` rank 31;
  - `03-audience-personas` rank 32.

  S11 may add them to the fixture set as it re-baselines.
- **Weak owned negatives (review finding 2):** every owned negative passes, but in only 26 of the 110 is the `negative_for` skill a real contender (in the top 3). It sits at ranks 4–10 in 29 and below rank 10 in 55; for example, `paid-search-advertising-not-social` puts the competitor at 72. **Hand-off to S11:** sharpen the weakest 10–15 owned negatives so that the competitor genuinely competes.
- **Single-character tokens (review finding 4):** the ranker drops them, so a client who writes "X" alone loses that signal. `platform-x-twitter` now also says "tweets" and "X (Twitter)"; otherwise this is a known limit of the lexical proxy.
- **Weak prescribed pairing:** the `healthcare` neighbour is `hospitality-hotel-restaurant`, as prescribed by §6.1, but it is a weak competitor. Its collision fixture uses a spa and wellness resort so that the clause is really tested. `playbook-crisis-communications` is named in `Do Not Use When`.
- **Handed to S10:**
  - the three NEW-skill neighbour clauses and their collision fixtures;
  - the `caption-writer` hashtag reference still recommends 5–10 Instagram tags (S05 follow-up);
  - `ecommerce-brand-differentiation` is rewritten now but merges in S10.
- **Legacy generator:** `scripts/normalise_skills_for_dual_compat.py` still emits the old "Use this skill when…" line. The new `use_when_template` finding would reject its output, so it cannot reintroduce templating silently. It is left unchanged because it is out of S08 scope.
- **Single change, not eight batch commits:** the brief asks for one S08 commit, so the rewrite was applied as one change rather than one commit per batch. The per-batch drafts are summarised in [descriptions.csv](descriptions.csv).
