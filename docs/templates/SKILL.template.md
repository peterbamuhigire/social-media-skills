---
name: skill-slug
description: Use when the requested deliverable needs this exact workflow; use neighbouring-skill when that route owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Skill Title

State the procedure's specific purpose in one or two sentences.

<!-- dual-compat-start -->
## Use When

- Name concrete positive triggers.

## Do Not Use When

- Name the nearest neighbouring route and unsafe stop conditions.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Decision brief | Accountable owner | yes | Ask for it or return a qualified intake gap |

## Workflow

1. Inspect the brief and evidence.
2. Apply the decision rules; stop when authority or evidence is insufficient.
3. Produce and verify the artefacts; correct failures and rerun affected checks.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Named deliverable | Named downstream role | Required fields and evidence checks pass |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision record | Table | Each recommendation cites evidence or a labelled assumption |

## Capability and Permission Boundaries

Read and search are required. Analysis is read-only. Mutation, publishing, spend, outreach, personal-data processing, destructive work, and certification claims require explicit authority.

## Degraded Mode

When a capability or source is unavailable, return the narrowest useful qualified result and mark the check `not assessed`.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence and authority are sufficient | Execute the authorised workflow | Unreviewable or unauthorised work |

## Quality Standards

- Define observable acceptance checks.
- Preserve evidence and unresolved risks for handoff.

## Anti-Patterns

- Inventing an input. Fix: verify it or label the assumption.
- Treating an unavailable check as passed. Fix: mark it `not assessed`.
- Acting beyond authority. Fix: stop at an approval-ready draft.
- Omitting a decision owner. Fix: name the accountable consumer.
- Declaring success without evidence. Fix: attach the check result.

## References

- [Repository authoring standard](../standards/skill-authoring-standard.md)
<!-- dual-compat-end -->
