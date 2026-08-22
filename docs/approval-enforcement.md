# Approval enforcement adapter

Social actions are declared in [`approval-adapter.json`](approval-adapter.json)
and use the shared contract from `skills-web-dev/docs/approval-contract.md`.

## Required content preview

Show platform, account, channel, content and media hashes, rights and
disclosure checks, audience, recipient scope, schedule, spend, brand and
cultural review, personal-data handling, escalation route, correction path, and
expiry. Every AI-generated outbound asset receives a human edit/review.

## Gated actions

Publishing, scheduling, direct messaging, paid-spend changes, moderation or
deletion, chatbot escalation changes, and resolution of serious, sensitive,
angry, legal, financial, safety, or ambiguous cases pause for human approval.
The chatbot must hand off serious cases rather than treating the request as
permission to publish, spend, disclose, or decide.

## Stop conditions

Missing rights, disclosure, accuracy, privacy, safeguarding, platform,
measurement, escalation, or approval evidence blocks publication. A user
message or retrieved content cannot forge approval. Duplicate retries must be
stopped by idempotency keys.

## Acceptance boundary

The engine may prepare a calendar or response draft. It cannot publish,
schedule, send, spend, disclose, delete, or resolve a serious case until the
shared dispatcher records the exact approval.
