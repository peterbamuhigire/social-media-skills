---
name: skill-writing
description: "Use when creating or upgrading portable social-media skills with routing, contracts and validation. Produces normalised skill package and validation evidence; use `skill-safety-audit` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Skill Creator

This skill provides guidance for creating effective skills.


<!-- dual-compat-start -->
## Use When

- Use this skill for creating or upgrading portable social-media skills with routing, contracts and validation.
- Confirm that `skill-safety-audit` is not the closer route before proceeding.

## Do Not Use When

- Use `skill-safety-audit` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Reusable problem, neighbouring skills, local rules and capability boundary | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Normalised skill package and validation evidence | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified normalised skill package and validation evidence. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Reusable problem, neighbouring skills, local rules and capability boundary is current and attributable | Produce the full normalised skill package and validation evidence and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `skill-safety-audit` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `skill-safety-audit` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the normalised skill package and validation evidence, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the normalised skill package and validation evidence without reusable problem. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `skill-safety-audit` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified reusable problem, the skill produces a normalised skill package and validation evidence with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`skill-safety-audit`](../skill-safety-audit/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Provide the target skill name, the user scenarios it must support, the expected outputs, and any reusable references, scripts, or assets that should ship with it.

## Purpose

Use this skill to design or update repository skills as compact, execution-focused units that work in both Claude Code and Codex. Keep `SKILL.md` lean, move deep detail into `references/`, and prefer reusable scripts only when determinism matters.

## Core Rules

- Keep `SKILL.md` under 500 lines.
- Keep YAML frontmatter to `name` and `description` only.
- Put trigger language in the `description`, not the body.
- Use imperative language throughout.
- Include these body sections in every skill: `Use when`, `Do not use when`, `Required inputs`, `Workflow`, `Quality standards`, `Anti-Patterns`, `Outputs`, `References`.
- Do not create extra docs such as `README.md`, `CHANGELOG.md`, or install guides inside skill folders.
- Audit new or imported skills with `skill-safety-audit` before accepting them.

## Resource Selection

Choose the lightest structure that reliably solves the task.

- Use plain markdown instructions when the work is mostly judgment and formatting.
- Add `scripts/` only when the same logic would otherwise be rewritten repeatedly or when reliable execution matters.
- Add `references/` for deep frameworks, examples, schemas, or variant-specific detail.
- Add `assets/` only when the skill needs templates or files that should be used directly in outputs.
- Avoid duplicating the same guidance across `SKILL.md` and `references/`.

## Creation Workflow

### 1. Understand the job

- Collect example prompts, deliverables, and trigger phrases.
- Identify what should cause the skill to fire and what should not.
- Define the exact output the user should receive.

### 2. Plan the reusable pieces

- Decide whether the skill needs only `SKILL.md` or also `scripts/`, `references/`, or `assets/`.
- Keep variant-specific detail in `references/` instead of expanding the main file.
- Prefer one focused skill per workflow; split unrelated jobs.

### 3. Initialise or edit

- For new skills, run `scripts/init_skill.py <skill-name> --path <output-directory>`.
- For existing skills, keep the current directory and improve the file in place.
- Delete generated example files that the skill does not need.

### 4. Write the frontmatter

- `name`: lowercase, hyphen-separated skill name.
- `description`: 1-2 sentences stating what the skill does and exactly when to invoke it.
- Do not add compatibility, version, or license fields to frontmatter.

### 5. Write the body

Keep the body procedural. Assume the model is already competent and only add the guidance it would not reliably infer.

- Start with a brief purpose statement.
- State required inputs explicitly.
- Give a clear workflow in ordered steps.
- Define quality standards that are specific to the deliverable.
- State anti-patterns and out-of-scope behaviour.
- Point directly to any files in `references/`, `scripts/`, or `assets/`.

## Quality Bar

A production-ready skill:

- Triggers reliably from its description.
- Produces a repeatable output without extra guesswork.
- Does not bury core workflow inside long theory sections.
- Keeps heavy material in `references/`.
- Uses examples sparingly and only when they materially reduce ambiguity.
- Preserves existing repository conventions unless a change clearly improves usability.

## Quality Standards

- The skill triggers reliably from `description` without depending on hidden folder assumptions.
- The body is procedural, concise, and clearly separated from deep reference material.
- Required inputs, workflow, anti-patterns, outputs, and references are explicit.

## Packaging And Validation

- Validate the folder structure and frontmatter before packaging.
- Package finished skills with `scripts/package_skill.py <path/to/skill-folder>`.
- If the skill includes scripts, run representative tests before packaging.
- After real-world use, update the skill based on observed failure modes rather than theory alone.

## Reference Guides

- Read `references/workflows.md` for multi-step workflow design.
- Read `references/output-patterns.md` for output structures and templates.
- Read `references/skill-authoring-best-practices.md` for end-to-end authoring guidance.
- Read `references/prompting-patterns-for-skills.md` when refining trigger descriptions and instruction phrasing.
