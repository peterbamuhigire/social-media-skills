---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
license: Complete terms in LICENSE.txt
---
# Skill Creator

This skill provides guidance for creating effective skills.

<!-- dual-compat:start -->
## Use when
- Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- Use it when maintaining, reviewing, or extending the skill repository itself.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.
- Do not invoke this skill for client deliverables; it is for repository maintenance and governance.

## Workflow
1. Inspect the target skill, file set, or repository area in full before making recommendations.
2. Apply the repository rules and any checks defined in this skill step by step.
3. Return a clear verdict, concrete findings, and the next actions required.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not approve unclear or risky repository changes without stating the exact issue and the action required.

## Outputs
- A repository maintenance output such as a review, audit, packaging step, or skill-authoring recommendation.

## References
- Read `references/output-patterns.md` when you need the deeper framework, examples, or supporting material it contains.
- Read `references/prompting-patterns-for-skills.md` when you need the deeper framework, examples, or supporting material it contains.
- Read `references/skill-authoring-best-practices.md` when you need the deeper framework, examples, or supporting material it contains.
- Read `references/workflows.md` when you need the deeper framework, examples, or supporting material it contains.

<!-- dual-compat:end -->

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
