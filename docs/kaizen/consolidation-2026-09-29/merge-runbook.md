# Merge runbook (every MERGE-INTO row)

Copied into the engine from the Social Kaizen 2026-09-29 roadmap §6 (S01-T11) and adjusted to the tooling that S01 added. Decisions D-SK-03 (alias mechanism) and D-SK-04 (merge evidence rule) govern it: see [decisions.md](decisions.md). A merge proceeds only when the row in the consolidation map passes D-SK-04: job overlap plus one supporting signal. A raw similarity score alone is never enough.

Placeholders: `<cat>` = category folder, `<source>` = retired skill, `<target>` = active owner, `<ref>` = the reference that receives the content, `S0n` = the phase.

1. **Read** the source `SKILL.md` and every file in its `references/` in full.
2. **Preservation map.** Copy [preservation-map-template.md](preservation-map-template.md) to `docs/kaizen/consolidation-2026-09-29/preservation/<source>.md` and list:
   - every non-contract heading (the phase file's §5.2 seeds these);
   - every decision row and anti-pattern not already in the target;
   - every citation and source-register ID;
   - every reference file.

   Give each item its destination (file and section) before any content moves.
3. **Write the target reference** `skills/<cat>/<target>/references/<ref>.md`:
   - Start with the provenance line: `Merged from skills/<cat>/<source> on <date> at <commit>; preservation map: <relative link>`.
   - Re-express the unique content in the target's task structure (inputs, decision rules, procedure, checklist).
   - Drop the source's copy of the shared contract scaffolding.
   - Keep citations as Author (Year) *Title*, Publisher. Quotes stay at or under 25 words.
   - No single-book digest and no book numbering. British English.
4. **Move** the source `references/*` with `git mv` into the target `references/`. Prefix the source name if a filename collides, and add the provenance line to each moved file.
5. **Point the target `SKILL.md` at it.** Add one Workflow branch or Decision row and one References link with a "read when" note. Widen the description only as much as routing needs (S08 finalises it). Stay at or under 300 lines (`line_budget`, from S09).
6. **Retire the source.**
   - `git mv skills/<cat>/<source>/SKILL.md skills/<cat>/<source>/ALIAS.md`
   - Insert this banner as the first line below the frontmatter (the checker requires it to start with `> Inactive alias.` and to name the target path):

     `> Inactive alias. Route to skills/<cat>/<target> through docs/skill-aliases.yml; content preserved in <target>/references/<ref>.md. Retained for historical content.`
   - Add the route under `inactive_skill_aliases:` in `docs/skill-aliases.yml`, for example `skills/<cat>/<source>: skills/<cat>/<target>`.
   - Lower `active_skill_policy.current_active_skill_count` and `quality-baseline.json` `active_skill_count` by one.
   - Do not edit the historical text of `ALIAS.md`, even where its old `references/` links no longer resolve: the repository link test skips `ALIAS.md` files (D-SK-03).
7. **Re-point referrers.** Every file listed in the phase's §5.1 now points to the target (path, plus an anchor to the reference). Include `AGENTS.md`, `README.md`, `docs/` (live guidance such as `docs/quality-gates/`, `docs/standards/`, `docs/templates/`), `rules/`, `prompts/` and other skills. Then run the grep over live files only; it must return nothing:

   `git grep -n "<source>/SKILL.md" -- skills AGENTS.md README.md CLAUDE.md rules prompts .claude-plugin docs/quality-gates docs/standards docs/templates docs/evidence-packs docs/world-class-exemplars docs/source-registers`

   Historical records (`docs/engine-upgrade-*`, `docs/audits/`, `docs/kaizen/`, dated plans and gap analyses, and the preservation map itself) keep the old path as history. The validator's `alias_link` finding fails any active skill that still links to an `ALIAS.md` or into a retired folder.
8. **Fixtures.** Add one alias-routing fixture per source to `tests/routing-fixtures.json`: a prompt in the old job's words, `"expected": "<target>"` and `"alias_of": "<source>"`. Re-point any fixture whose `expected` was the source (`--lint-fixtures` rejects an alias as `expected`).
9. **Manifest and counts.** Regenerate the plugin manifest so it stops listing the retired folder: from `chwezi-engine-agents`, run `node scripts/generate-plugin-manifest.js --engine ..\social-media-skills`, then the same command with `--check`. Update the active count where it is stated: `README.md` (summary, category table and total) and the "N skills" text in the marketplace entry (external-release text: the orchestrator applies it; S12 regenerates it in full).
10. **Gates.** Run the standard gate block below. Then commit one cluster per commit, with the message `refactor(consolidation): merge <sources> into <target> (S0n)` and the attribution line. Executors leave changes unstaged when the orchestrator commits.
11. **Evidence.** Add a row to `docs/kaizen/consolidation-2026-09-29/evidence/S0n/merges.md` recording: source, target, reference, preservation-map status, gate results and commit hash.

## Standard gate block

Run it after each commit that changes skills, and in full at the end of every phase. A red result stops the phase.

```powershell
# Engine root
python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json      # failures=0; count = baseline; no catalogue_cap_exceeded
python -X utf8 scripts\routing_smoke_test.py --min-rank1 92 --lint-fixtures            # top-3 = 1.000; p@1 >= floor (92 from S08); lint 0; owned negatives pass
python -X utf8 scripts\check_skill_aliases.py                                         # routes <-> ALIAS.md lockstep; targets active; count and cap
python -X utf8 -B -m pytest -q tests                                                  # all pass
python -X utf8 -m unittest discover -s tests -p "test_*.py"                           # the CI form
python -X utf8 scripts\check_source_freshness.py                                      # no overdue record used by a changed skill
python -X utf8 scripts\source_ingestion_guardrail.py                                  # no book extraction
git diff --check

# Coordination package (chwezi-engine-agents, sibling checkout)
python -X utf8 scripts\render_host_files.py --check --workspace-root .. --engine ..\social-media-skills
node scripts\generate-plugin-manifest.js --check-marketplace --workspace-root ..
python -X utf8 scripts\validate-runtime-skill-budget.py --collisions --ownership evals\routing\ownership.yaml
python -X utf8 scripts\validate-routing-baseline.py
python -X utf8 scripts\validate-no-book-extractions.py
```

Raise `--min-rank1` only when the measured p@1 rises; never lower it without a recorded decision. Routing figures are a lexical proxy, not live routing.

## Rollback

`git revert` the merge commit. Because the source stays on disk as `ALIAS.md` with its historical text, a revert restores the active skill, its route and its count in one step.
