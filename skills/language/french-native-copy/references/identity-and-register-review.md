# Identity and register review

Use this record when French copy names a person, organisation, product or
community identity. It keeps the field set proportional to the stated purpose
and market.

## Minimum record

```yaml
display_name: "Name shown to the audience"
locale: fr-CD
purpose: "Why this identity/register decision is needed"
native_review:
  status: completed|not-assessed
  reviewer: "Named fluent French reviewer"
  reviewed_on: "YYYY-MM-DD"
```

`display_name` and `locale` are sufficient identity fields when the purpose
does not require legal identity, pronunciation, script or relationship data.
Do not collect or infer those fields by default. Add `legal_name`,
`preferred_name`, `pronunciation`, `script` or `relationship` only when the
task, jurisdiction, audience and explicit consent require them; record the
purpose and retention/deletion boundary for each addition.

Missing native-language review is `NOT_ASSESSED`, even when the fields look
complete. A French register decision must also name the market and the
`vous`/`tu` choice where the copy needs it; this record does not certify legal
identity or native-quality copy.

## Acceptance examples

Pass: `{display_name, locale, purpose, native_review}` with no legal or
pronunciation need. Fail or omit: unnecessary legal name or pronunciation
fields when those needs are false. `NOT_ASSESSED`: no fluent reviewer or no
review date.
