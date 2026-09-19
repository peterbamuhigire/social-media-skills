# Reader-first content brief

Use this record for each content unit handed from strategy to production. The
campaign brief remains the owner; the record makes the reader's job, proof,
rights, destination and review state explicit before drafting.

## Required record

```yaml
brief_id: unit-001
reader:
  audience: "Named audience and context"
  reader_job: "What the reader needs to understand or decide"
  utility: "Practical help the unit provides"
  inspiration: "Why the reader may care or feel encouraged"
  empathy: "Constraint, concern or lived context to respect"
objective: "One business or audience outcome"
channel: "One named channel and placement"
destination:
  kind: website|whatsapp|form|profile|none
  url: "Exact approved destination, or null when no click is intended"
  promise: "What the CTA says the reader will find"
  status: verified|unverified|not-applicable
claims: []
rights: []
review:
  owner: "Role accountable for correction"
  reviewer: "Named human reviewer"
  reviewed_on: "YYYY-MM-DD"
  language_review: completed|not-assessed
```

The reader job must be recoverable in one sentence. Keep utility,
inspiration and empathy distinct: a warm tone is not evidence of usefulness.
Record the source scope and source IDs on each material claim. Record one
rights row for every reused image, quote, music track, logo, likeness or
customer story. Use `not-assessed` when a source, destination, language review
or reviewer is unavailable; it is never a release pass.

## Destination and review gate

The CTA, destination kind, URL and destination promise must agree. A post that
promises a booking form but links to a general homepage is a destination
mismatch and is blocked until the destination owner repairs it. A `none`
destination is valid only when the CTA asks for an on-platform action.

The independent acceptance check is the content-unit validator fixture at
[`tests/fixtures/kaizen-phase1-contracts.json`](../../../../tests/fixtures/kaizen-phase1-contracts.json).
It is synthetic test data and does not establish client evidence or campaign
performance.

## Handoff

`05-social-media-strategy` may define the strategic audience and job, but
`13-campaign-brief` owns the production handoff. Carry this record into the
calendar, creative review and approval packet. Route unresolved claims or
rights to the owner and quarantine them from release.
