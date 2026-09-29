---
name: skill-writing
description: 'Use when a social or digital-marketing skill in this engine must be created, split, merged or upgraded: frontmatter, routing description, Use When, contracts, references and routing fixtures under the canonical standard; produces the skill directory and passing fixtures; not for a read-only safety review (use `skill-safety-audit`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Skill Writing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Pointer stub. The canonical standard is `chwezi-dev-engine/skills/sdlc-meta/skill-writing` ([canonical on GitHub](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/skills/sdlc-meta/skill-writing/SKILL.md); local path `C:\wamp64\www\chwezi-dev-engine\skills\sdlc-meta\skill-writing\SKILL.md`). Load it first; this file keeps a portable minimum and this engine's delta.
<!-- dual-compat-start -->
## Use When
- A new social, advertising or content job needs its own skill: a SKILL.md with frontmatter, a routed description, trigger sections and test prompts (fixtures).
- An existing skill's description, Use When or Do Not Use When no longer routes correctly and must be rewritten.
- Two skills overlap and one must absorb the other, with references moved and aliases kept.
- Validators or routing fixtures fail after an edit and the skill must be brought back to standard.

## Do Not Use When
- `skill-safety-audit` for a read-only safety review before adoption or release.
- `kaizen-improvement-system` for a wider audit of the engine's quality.
- Stop before committing or releasing the skill until validators pass and the maintainer approves.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Reusable problem, trigger prompts and neighbour descriptions | Requester and live catalogue | Yes | Stop; search the catalogue before drafting. |
| Canonical skill-writing standard | chwezi-dev-engine checkout or GitHub | Yes | Apply the portable minimum and mark canonical-only checks `NOT ASSESSED`. |
## Workflow
1. Read the canonical standard, then this engine's delta; inspect the closest neighbours.
2. Write the input, output, evidence, capability, degraded-mode and decision contracts before the procedure.
3. Run `python -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json` and `python -X utf8 scripts/routing_smoke_test.py`, then `python -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py <skill-dir>`.
4. Stop on any finding or routing collision; recover by fixing the named contract and rerun, never by weakening the gate.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Skill directory and routing fixtures | Maintainer and router | Validators pass and the expected skill ranks in the top three. |
## Evidence Produced
| Evidence | Artefact and format | Consumer | Acceptance condition |
|---|---|---|---|
| Validation and routing record | Command output | Release owner | Zero findings; unrun checks marked `NOT ASSESSED`. |
<!-- dual-compat-end -->
## Quality Standards
- Portable minimum, applied even when the canonical is unreachable: frontmatter uses only approved keys and `name` matches the folder.
- The description starts `Use when`, stays within 350 characters and names a neighbour, with no workflow steps.
- `SKILL.md` stays within 300 lines in this engine (validator `line_budget`; aim for 120-220) and follows the lean template; deep detail sits in references one level deep, linked directly with a "read when" note.
- Every new or changed skill gets positive, negative and collision routing fixtures.
- Bundled scripts run through their interpreter, for example `python -X utf8 scripts/<name>.py`.
- No book extractions or copied third-party text; paraphrase and attribute.
- British English, the imperative mood, and `NOT ASSESSED` for any check not run.
## Engine-Local Delta
- Write for the stated client market and currency; never publish, spend, change a live account or certify compliance while authoring.
- Use the [lean skill template](../../../docs/templates/SKILL.template.md) (D-SK-06): domain-specific contract rows, the two canonical sentences for capability and degraded mode, and no repeated scaffolding (`scripts/measure_skill_scaffolding.py --max-median 12`).
- Apply [anti-AI slop](../../ai-marketing/anti-ai-slop/SKILL.md) while writing and [the slop audit](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint; follow the [local authoring standard](../../../docs/standards/skill-authoring-standard.md).
## Capability Contract
Read and search are required. Editing files and running validators need explicit permission for the authoring task; publishing, deletion and release changes need separate authorisation.
## Degraded Mode
If the canonical standard is unavailable, apply the portable minimum, return the narrowest qualified result, and mark each canonical-only check `NOT ASSESSED`; never report it as passed.
## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| An existing skill owns the trigger and output | Normalise it in place; put branch-only detail in a linked reference | Duplicate routes and oversized entrypoints |
## Anti-Patterns
- Copying the canonical body into this engine. Fix: link the canonical and keep only the delta here.
- Writing only positive triggers. Fix: name the neighbour and add a collision fixture.
- Treating an unrun validator as a pass. Fix: record `NOT ASSESSED` with the reason.
- Granting edit rights to a review procedure. Fix: default review and audit to read-only.
- Weakening a baseline to clear a finding. Fix: repair the named contract instead.
## Worked Example
Given a request for a LinkedIn carousel skill, inspect the closest content and platform skills, name the neighbour that wins on a pure copy request, then add positive and collision fixtures before activation.
## References
- [Canonical skill-writing standard](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/skills/sdlc-meta/skill-writing/SKILL.md)
- [Local authoring standard](../../../docs/standards/skill-authoring-standard.md)
- [Skill authoring practices (canonical mirror)](references/skill-authoring-best-practices.md)
- [Skill safety audit](../skill-safety-audit/SKILL.md)
