# Social Media Skill Authoring Standard

This repository uses the July 2026 portable composition contract. The standard applies to every active `skills/**/SKILL.md`; historical plans and ordinary references are not active skills.

## Entrypoint contract

- Keep `SKILL.md` at or below 300 lines (the `line_budget` validator finding, Social Kaizen S09, D-SK-06) and aim for 120-220 lines; the catalogue median must stay at or below 200. Move procedures longer than about 25 lines, catalogues, schemas, examples, platform tables and case material into directly linked `references/` files, each linked with a "read when" note. Decision rows, quality checks and anti-patterns stay in `SKILL.md`.
- Use YAML keys supported by the canonical contract: `name`, `description`, `license`, `allowed-tools`, and `metadata`. The directory-matching `name`, single-line `description`, and portable `metadata` are mandatory here.
- Begin descriptions with `Use when`, keep them at or below 350 characters, and distinguish the closest neighbouring route.
- Follow the routing-text formula (Social Kaizen S08): `Use when <client-language trigger>; produces <named artefact>; not for <neighbour job> (use `<neighbour-id>`).` `Use When` holds 3-6 triggers in the client's words; `Do Not Use When` names 2-4 neighbours by id plus one stop condition. The validator enforces this as `description_template`, `description_formula`, `use_when_template`, `description_neighbour_unknown` and `do_not_use_neighbour_unknown`; each "not for" neighbour needs an owned-negative fixture (`negative_for`) in `tests/routing-fixtures.json`.
- Enclose the portable contract between `<!-- dual-compat-start -->` and `<!-- dual-compat-end -->`.

## Required contracts

Every active skill declares non-empty `Use When`, `Do Not Use When`, `Required Inputs`, `Workflow`, `Outputs`, `Evidence Produced`, capability/permission, `Degraded Mode`, `Decision Rules`, `Quality Standards`, `Anti-Patterns`, and `References` sections.

Inputs name the artefact, source/provider, requirement, and missing-input behaviour. Outputs name the artefact, consumer, and observable acceptance condition. Evidence contracts must distinguish assessed evidence from unavailable checks.

Analysis, audit, critique, review, planning, and diagnostics default to read-only. Publishing, outreach, spend, production mutation, destructive work, personal-data processing, and certification claims require explicit authority. Degraded mode returns the narrowest useful qualified result and marks unavailable checks `not assessed`.

Decision tables name the condition, action, and failure or risk avoided. Workflows include ordered decisions, stop conditions, and correction or rerun behaviour. Anti-patterns contain at least five concrete failures, each paired with `Fix:`.

## Lean template and budgets (D-SK-06)

Every active skill follows [the lean template](../templates/SKILL.template.md): the twelve contract sections above, written as domain decisions, with depth one link away in `references/`. Generic contract prose repeated from skill to skill is not allowed; only the canonical sentences below may repeat verbatim.

| Measure | Budget |
|---|---|
| `SKILL.md` length | 120-220 lines; catalogue median at or below 200; hard ceiling 300 (`line_budget`) |
| Required Inputs / Outputs / Evidence Produced rows | at most 6 / 5 / 4 |
| Workflow | 5-9 domain steps; one names the stop condition, one the correction and rerun |
| Decision Rules | 4-8 domain rows |
| Quality Standards | 4-8 observable checks |
| Anti-Patterns | 5-7 domain failures, each with `Fix:` |
| Shared-line ratio | gated median at or below 12 % (`scripts/measure_skill_scaffolding.py --max-median 12`) |

**Canonical sentences (the allow-list).** These are allowed verbatim in every skill and are excluded from the shared-line ratio:

- Capability and Permission Boundaries: "Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority." A skill may add one domain sentence after it.
- Degraded Mode: "Without <the domain's critical input>, return the narrowest qualified result and mark the affected checks `not assessed`." followed by one domain clause.

The meter also excludes the structural lines the validator requires: frontmatter keys, the dual-compat markers, headings, table separator rows and the four contract table header rows (`| Artefact | Source/provider | Required? | If absent |`, `| Artefact | Consumer | Acceptance condition |`, `| Evidence | Format | Acceptance condition |`, `| Condition | Action | Failure or risk avoided |`). Its `raw` figure, which counts every line, is reported alongside for comparison with the plan-time baseline.

**Moving content to `references/`.** A move keeps every decision rule, figure, citation and register ID. The reference starts with a provenance line ("Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026)"), and each moved block is recorded in the phase's preservation log. Nothing is deleted except generic contract prose that the canonical sentences or the domain-specific contract sections replace.

## Source material and copyright

Book knowledge enters only as task-oriented skill content and `references/`; no book extractions or summaries are stored in the repository. Reference files must not be single-book digests. Synthesise across sources into the engine's own task structure (inputs, decision rules, procedures, templates, checklists, localised original examples), in your own order and wording. Do not reproduce a book's numbered lists in its sequence, an author's full catalogue of beat/step/strategy names, book case studies or near-verbatim text, or "Strategy N" / chapter numbering. Name a framework with a brief attribution (for example "value ladder (Brunson)") and apply it; cite sources briefly as Author (Year) *Title*, Publisher. Quotes stay at or under 25 words and are rare. Volatile facts come from the dated source register or are written as checks.

## Authoring and release

Start from [the local template](../templates/SKILL.template.md). Preserve the skill's domain content; do not replace it with generic compatibility prose. Run:

```powershell
python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
```

Then run the canonical quick validator for each changed skill directory and the canonical engine scanner across `skills`. A release requires empty failure counts, every routing fixture with the expected skill in the top three, clean relative links, no cache files, and `git diff --check`.
