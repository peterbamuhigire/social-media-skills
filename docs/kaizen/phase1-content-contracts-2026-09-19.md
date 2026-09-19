# Phase 1 social content contracts

Status: implemented bounded fixture and route extension, 19 September 2026.
This slice covers B06-A01 reader-first briefs, B06-A03 claim/rights records,
B11-A01 identity/register minimisation, and B18-A05 customer-voice experiment
cards.

## Ownership and route

- `05-social-media-strategy` owns the strategic audience and content job.
- `13-campaign-brief` owns the production handoff, reader, evidence, rights and
  canonical destination fields.
- `language/french-native-copy` owns French language execution and the
  conditional identity/register fields.
- `meta-social-listening` owns the customer-voice experiment card. It records
  source scope, denominator, privacy boundary, outcome, counter-metric,
  guardrail, decision rule and knowledge link.

The social repository adapts the Digital Research source-verification contract;
the Digital Research engine remains the authority for source assessment and
currentness. No live account, customer record or external publication is
changed by these checks.

## Acceptance evidence

Run the deterministic synthetic fixture:

```powershell
python -X utf8 scripts\kaizen_phase1_contracts.py
python -X utf8 -m unittest tests.test_kaizen_phase1_contracts -v
```

The fixture covers a passing reader-first unit, unsupported claim, missing
rights, destination mismatch, minimal `display_name` + locale, missing native
review, a passing customer-voice card and a missing denominator. `BLOCKED`
means the unit cannot proceed; `NOT_ASSESSED` means evidence is unavailable or
incomplete and must remain visible.

## Currentness and model evidence

The book action cards are durable concept inputs, not current platform or legal
evidence. Current claims remain subject to the Digital Research source register
and verification route. The Codex model-policy preflight passed with Python
3.13 (`ensure_model_policy.py --runtime codex --check`); execution roles remain
pinned to `gpt-5.6-luna` by local policy. Official OpenAI model documentation
and Help Centre availability pages were checked on 19 September 2026:

- https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4 — lists
  `gpt-5.6-luna` and its current API role.
- https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt
  — describes Codex/API availability.

The local runtime/account catalogue beyond the policy preflight was not
independently queried: `NOT_ASSESSED`. No model-policy or configuration file
was changed.
