# Dual Compatibility Report

Date: 13 April 2026

## Objective

Upgrade `social-media-skills` so it remains fully usable in Claude Code while becoming directly understandable and operable by Codex, without relocating skills or fragmenting logic.

## What Was Wrong

### 1. Codex lacked a repository entry point

The repository had `CLAUDE.md` for authoring conventions, but no root `AGENTS.md` explaining:

- what counts as a skill
- where skills live
- how to route tasks to skills
- which skills are cross-cutting standards
- how to handle optional `references/`, `scripts/`, and `assets/`

Claude could still function from frontmatter plus existing conventions. Codex had no equivalent repo-level instruction layer.

### 2. SKILL body structure was inconsistent

A repository-wide scan of 172 top-level skills showed:

- `Use when`: 0
- `Do not use when`: 0
- `Workflow`: 0
- `Anti-Patterns`: 0
- `Outputs`: 34
- `References`: 74
- `Required Input`: 165
- `Quality Criteria` or `Quality Standards`: 166

This meant Claude could still infer usage from the `description`, but Codex did not have consistent execution scaffolding inside the skill bodies.

### 3. Future reference handling was underspecified

Some skills already used `references/` well, but many did not. There was no shared, Codex-readable rule for treating `references/` as optional now but preferred for deeper material as skills grow.

### 4. A few skills breached the 500-line convention

After standardising the missing compatibility sections, several long skills exceeded the repository's own line budget and needed trimming or consolidation.

### 5. Folded YAML descriptions were a compatibility edge case

Skills using YAML folded descriptions (`description: >`) needed correct extraction into the new `Use when` section.

## What Was Improved

### 1. Added a root `AGENTS.md`

Created a repo-level instruction file for Codex that defines:

- the repository purpose
- the top-level skill discovery rule
- default Uganda / East Africa context
- baseline cross-cutting skills
- task routing by naming convention
- execution, reference, and maintenance rules
- quality expectations

This adds Codex compatibility without disturbing Claude's existing behaviour.

### 2. Standardised all 172 top-level `SKILL.md` files

Added a consistent dual-compatible compatibility block to every top-level skill with:

- `Use when`
- `Do not use when`
- `Workflow`
- `Anti-Patterns`
- `Outputs`
- `References`

This was layered on top of existing skill logic rather than replacing the original content structure, preserving Claude-facing behaviour while giving Codex explicit execution guidance.

### 3. Added a repeatable maintenance script

Created `scripts/normalise_skills_for_dual_compat.py` to:

- scan top-level skills
- inject or refresh the shared compatibility block
- keep changes consistent across the repository
- support future maintenance without hand-editing every skill

The script now also handles folded YAML descriptions correctly.

### 4. Improved reference handling language

For skills without a current `references/` folder, the compatibility block now says:

- use the inline instructions now
- treat `references/` as the future home for deeper support material

This avoids implying that a missing `references/` folder is the final state of the skill.

### 5. Restored compliance with the 500-line rule

Trimmed or consolidated oversized skills so all top-level `SKILL.md` files are now at or below 500 lines.

Notable clean-up included:

- compressing `skill-writing` into a more execution-focused authoring guide that points to its existing reference files
- removing duplicated or low-signal sections from the longest skills

## What Was Added

- `AGENTS.md`
- `scripts/normalise_skills_for_dual_compat.py`
- this report: `docs/compatibility-report-2026-04.md`

## Why These Changes Matter

### For Claude Code

- Existing directory structure is unchanged.
- Existing skill descriptions remain the trigger mechanism.
- Existing skill logic remains in place.
- No skills were moved into a new wrapper folder.

### For Codex

- There is now a clear repo-level instruction file.
- Every top-level skill has the same execution-oriented scaffolding.
- Reference usage is explicit and progressive.
- Routing and cross-cutting baseline skills are defined.

### For maintainability

- Standardisation is now scriptable rather than manual.
- Future skills can be normalised the same way.
- Long skills are less likely to regress because the repo now has both a maintenance script and an explicit root agent guide.

## Recommendations

### Recommended next

- Continue moving deep framework material out of the longest strategy and training skills into `references/` as those skills evolve.
- Add `references/` directories to skills that are likely to keep growing, especially training, policy, AI, and platform strategy skills.
- Use `skill-safety-audit` as a required step for third-party or externally sourced skills.

### Optional improvements

- Add nested `AGENTS.md` files only in areas that develop distinct subdomain workflows, for example a future AI-heavy cluster or a dedicated policy cluster.
- Add a lightweight validation script that reports line counts, missing sections, and empty `references/` directories in CI or pre-commit workflows.
- Periodically review old skills for duplication across neighbouring strategy or playbook areas and move shared frameworks into references instead of repeating them.
