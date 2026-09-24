# Social Media Skill Authoring Standard

This repository uses the July 2026 portable composition contract. The standard applies to every active `skills/**/SKILL.md`; historical plans and ordinary references are not active skills.

## Entrypoint contract

- Keep `SKILL.md` at or below 500 lines and move long curricula, catalogues, schemas, and case material into directly linked `references/` files.
- Use YAML keys supported by the canonical contract: `name`, `description`, `license`, `allowed-tools`, and `metadata`. The directory-matching `name`, single-line `description`, and portable `metadata` are mandatory here.
- Begin descriptions with `Use when`, keep them at or below 350 characters, and distinguish the closest neighbouring route.
- Enclose the portable contract between `<!-- dual-compat-start -->` and `<!-- dual-compat-end -->`.

## Required contracts

Every active skill declares non-empty `Use When`, `Do Not Use When`, `Required Inputs`, `Workflow`, `Outputs`, `Evidence Produced`, capability/permission, `Degraded Mode`, `Decision Rules`, `Quality Standards`, `Anti-Patterns`, and `References` sections.

Inputs name the artefact, source/provider, requirement, and missing-input behaviour. Outputs name the artefact, consumer, and observable acceptance condition. Evidence contracts must distinguish assessed evidence from unavailable checks.

Analysis, audit, critique, review, planning, and diagnostics default to read-only. Publishing, outreach, spend, production mutation, destructive work, personal-data processing, and certification claims require explicit authority. Degraded mode returns the narrowest useful qualified result and marks unavailable checks `not assessed`.

Decision tables name the condition, action, and failure or risk avoided. Workflows include ordered decisions, stop conditions, and correction or rerun behaviour. Anti-patterns contain at least five concrete failures, each paired with `Fix:`.

## Source material and copyright

Book knowledge enters only as task-oriented skill content and `references/`; no book extractions or summaries are stored in the repository. Reference files must not be single-book digests. Synthesise across sources into the engine's own task structure (inputs, decision rules, procedures, templates, checklists, localised original examples), in your own order and wording. Do not reproduce a book's numbered lists in its sequence, an author's full catalogue of beat/step/strategy names, book case studies or near-verbatim text, or "Strategy N" / chapter numbering. Name a framework with a brief attribution (for example "value ladder (Brunson)") and apply it; cite sources briefly as Author (Year) *Title*, Publisher. Quotes stay at or under 25 words and are rare. Volatile facts come from the dated source register or are written as checks.

## Authoring and release

Start from [the local template](../templates/SKILL.template.md). Preserve the skill's domain content; do not replace it with generic compatibility prose. Run:

```powershell
python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
```

Then run the canonical quick validator for each changed skill directory and the canonical engine scanner across `skills`. A release requires empty failure counts, every routing fixture with the expected skill in the top three, clean relative links, no cache files, and `git diff --check`.
