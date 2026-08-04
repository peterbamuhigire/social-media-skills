# AI campaign trust, control, correction, and drift

[Owning skill](../SKILL.md)

Use this reference for AI-assisted or agentic campaign systems that draft, classify, recommend, target, schedule, respond, or learn from social activity.

## Source basis and limits

The admitted evidence from *Designing for AI* (Arash Sadr) is limited to the available early-release Chapters 1-3: problem-first AI selection, system-centred design, human/AI/system layers, model-versus-system distinction, input/output awareness, data/inference transparency, and user understanding. Chapters on trust, rollout, drift, governance, culture, and legal detail were unavailable and are not treated as read. Verify current legal, platform, model, and safety requirements through Digital Research.

## Required workflow fields

| Field | Minimum requirement |
|---|---|
| Problem fit | State the audience problem, non-AI alternative, reason AI is needed, and expected value. |
| System map | Separate model, prompt/rules, data, inferred data, platform, automation, human reviewer, output, and action. |
| Disclosure | Describe the specific AI contribution: generated, transformed, inferred, ranked, or automated. Avoid vague “AI-powered” wording. |
| Human control | Define approval boundary, edit/reject/undo path, escalation trigger, permission scope, and accountable owner. No autonomous public response for complaints, crises, sensitive claims, or high-value decisions. |
| Correction | Provide a way to correct an output and record whether correction affects only the current item, the prompt/rules, the source data, or future model behaviour. |
| Drift | Name monitored signal, baseline, threshold, review cadence, owner, fallback, and rollback for changes in audience, data, model, platform, or policy. |
| Campaign quality | Run anti-slop, factual, cultural, readability, accessibility, privacy, and permissions checks before release. |

## Stop conditions

Stop and route to human review when the system cannot show its input/source, the audience cannot understand or correct its output, the result changes a sensitive decision, the model/platform behaviour is materially different from baseline, or required legal/market evidence is current but unverified.

