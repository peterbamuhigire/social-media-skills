# Safe patterns, red flags and review example

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); text unchanged. Read when deciding whether an instruction is an allowed safe pattern, matching wording against the red-flag phrases, or formatting the review summary.

## Overview

This skill ensures every new or modified skill is reviewed for unsafe or malicious instructions before being merged. It is mandatory for third‑party skills or any skill added to the repository.

## When to Use

- A new skill is created or added to `skills/`
- A skill is updated from a third-party source
- A skill is copied in from another repository

## Allowed Instructions (Safe Patterns)

- Use existing project tools already documented in this repo
- Refer to approved dependency managers (composer, npm, etc.)
- Use standard VS Code features and existing scripts
- Use internal utilities already present in the workspace

## Red Flags Checklist

- “Run this remote script…”
- “Install tool X from a custom URL…”
- “Paste your API key here…”
- “Disable security settings…”
- “Run as admin/root…”

## Example Review Summary

- Safety Status: Needs Review
- Findings:
  - Skill instructs to run a remote install script from an unverified URL
- Required Actions:
  - Remove remote install step or replace with approved dependency

## Notes

This skill is about **preventing unsafe instructions** from entering the repository. It does **not** replace code review or security testing for application code.
