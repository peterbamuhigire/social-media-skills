# Contributing

Create and revise skills under `skills/<category>/<skill-name>/`. Read [the authoring standard](docs/standards/skill-authoring-standard.md) and copy [the skill template](docs/templates/SKILL.template.md); do not create an active skill directly under `skills/`.

Preserve the skill's domain knowledge. Frontmatter and marker repairs may be mechanical, but inputs, decisions, examples, evidence, degraded behaviour, safety boundaries, and acceptance conditions require domain judgement. Keep `SKILL.md` at or below 500 lines and link extracted references back to the parent entrypoint.

Before opening or merging a change, run:

```powershell
python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 -m unittest discover -s tests -p "test_*.py"
```

Run the canonical `quick_validate.py` with each changed skill directory, then run the canonical engine scanner over `skills`. Finish with `git diff --check`. Update routing fixtures when a trigger or neighbour boundary changes. The expected skill must remain in the top three for every fixture, with a 100% release threshold.

Do not add findings to `quality-baseline.json`; its empty `failure_counts` object is the release invariant. A new finding must be fixed before merge.
