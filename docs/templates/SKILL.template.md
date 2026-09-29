---
name: skill-slug
description: 'Use when <client-language trigger - the deliverable and the situation>; produces <named artefact>; not for <neighbour job> (use `neighbour-skill-id`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Skill Title

Two sentences: the decision this skill makes and for whom.

<!-- dual-compat-start -->
## Use When

- 3-6 concrete triggers in the words a client or account manager would use (S08 formula; no templated phrasing).

## Do Not Use When

- `neighbour-skill-id` for <its job> (name 2-4 real neighbours by id).
- Stop condition: <what is missing or unauthorised, and what is returned instead>.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| <domain input, named precisely> | <who or what supplies it> | Yes | <domain-specific fallback: ask, narrow, or mark not assessed> |

## Workflow

1. <Domain step 1 - 5 to 9 steps in total, each a decision a senior practitioner makes.>
2. <One step names the stop condition: stop when <domain evidence or authority> is missing.>
3. <One step names the recovery: correct and rerun <the failed domain check>.>

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| <named deliverable> | <named downstream role or skill> | <observable, domain-specific check> |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| <domain evidence record> | <table, log, appendix> | <what makes it acceptable> |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority.

## Degraded Mode

Without <the domain's critical input>, return the narrowest qualified result and mark the affected checks `not assessed`. <One domain clause: what can still be delivered.>

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| <domain condition - 4 to 8 rows> | <domain action> | <domain failure> |

## Quality Standards

- 4-8 observable checks specific to the deliverable.

## Anti-Patterns

- <Domain failure 1 - 5 to 7 in total.> Fix: <domain correction>.

## References

- <Markdown link to references/<topic>.md>: read when <situation>. (one line per reference file)
- <Markdown link to the anti-AI slop gate, skills/ai-marketing/anti-ai-slop>: read when drafting client-facing copy (keep only where the skill writes copy).
<!-- dual-compat-end -->
