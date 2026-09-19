# Customer-voice experiment card

Use this card to turn a bounded listening observation into a reversible
content or service experiment. Listening is a source of hypotheses; sentiment
or activity alone does not establish demand, impact or causality.

```yaml
experiment_id: voice-001
source_scope: "Channels, market, period and question covered"
source_ids: [listening-001]
observation: "Observed question, complaint or praise"
hypothesis: "If [change], [audience] will [outcome] because [reason]."
sample:
  unit: "eligible posts|enquiries|sessions|customers"
  denominator: 120
  inclusion: "Who counts"
  exclusion: "Who does not count"
privacy_boundary: "Public aggregate only; no unnecessary personal data"
action: "One reversible content, service or research action"
primary_outcome: "Outcome tied to the audience job"
counter_metric: "Metric that could worsen"
guardrail: "Trust, safety, rights, quality or complaint threshold"
test_window: "Start/end dates or event boundary"
decision_rule: "Support, mixed, weakens or inconclusive threshold"
owner: "Named accountable owner"
review_date: "YYYY-MM-DD"
result: support|mixed|weakens|inconclusive|not-assessed
knowledge_record:
  lesson: "What can be reused, if supported"
  source_ids: [listening-001]
  standardise: true|false
  retirement_trigger: "When to stop using the lesson"
```

Missing `source_scope`, denominator, privacy boundary, decision rule or
knowledge link is `NOT_ASSESSED`. Keep the original evidence immutable and
record the experiment result separately. A weak or mixed result is useful
learning; do not rewrite it as a win.
