---
name: ai-slop-audit
description: Use when a finished caption, post, carousel, ad, campaign, calendar, email, deck, AI image or video needs checking for AI-generated tells before it moves on or ships; produces a graded audit report with a genericness score, blocking findings and a fix list; not for guardrails applied while drafting (use `anti-ai-slop`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Slop Audit

The detector. Given any social artefact, it decides how strongly it reads as AI slop, names exactly why, and says how to fix each finding; production-side prevention is the companion `anti-ai-slop` skill.

<!-- dual-compat-start -->
## Use When
- Does this caption, carousel, email or ad copy look like a bot or ChatGPT wrote it? Tell us why it feels off and what gives it away.
- A campaign, content calendar, blog, email sequence or deck outline is finished; check it before we move to the next piece.
- Review an AI-generated image or video for the tells that make it look fake or generic.
- Grade it A to F with a genericness score, cite each finding, say whether it can ship, and keep the good parts.
- Run the final gate before anything from the engine is published or sent to the client.

## Do Not Use When
- `anti-ai-slop` for guardrails applied while drafting and for humanising a draft.
- `policy-ai-content-ethics` for cultural bias, AI disclosure and copyright policy.
- `premium-commercial-writing` for general editorial standards and brochure copy.
- Stop the next asset or iteration when the verdict is F (blocked) until the blocking findings are fixed; never invent evidence for a finding.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| The artefact itself: caption, post, thread, carousel, ad copy, campaign, calendar, blog, email, deck, profile/bio, image or video | Requester (pasted text, file, rendered post or URL) | Yes | Stop; no audit without the artefact, and never infer findings from a description. |
| Artefact type(s): written EN, written FR, image, video or multi-asset campaign | Requester, or read from the artefact | Yes | Classify from the artefact and state the classification in the report. |
| Client business name and industry | Brief or requester | Yes | Judge specificity only against what the artefact claims and mark on-brand fit `not assessed`. |
| Country/city of the audience | Brief | Yes | Default to Uganda / East Africa and state the default. |
| Intended channel and goal | Brief | Yes | Judge the CTA generically and mark channel fit `not assessed`. |
| Render, provenance or source evidence (C2PA data, rendered frames, links behind claims) | Requester or file metadata | Conditional (visuals, cited claims) | Mark the affected check `NOT_ASSESSED`; mark non-visual checks `not_applicable`. |

## Workflow

1. Confirm the artefact and inputs, then identify the artefact type(s) and load the matching checklists from the [audit method](references/audit-method.md); for a campaign or calendar, plan to audit each post and asset, then the set as a whole.
2. Run the automated gates (focal-word density, em-dash and rule-of-three patterns, opener clichés, mechanical formatting, citations and statistics, image and video checks); any [BLOCK] hit fails the artefact outright.
3. Compute the 0–100 genericness score from burstiness, focal-word density, duplication across the set and template similarity, and name its drivers.
4. Run the human-judgement review: substance, intent, specificity, hard parts, localisation, visuals and the artefact-specific checks.
5. Apply the ME1-ME7 machine-error checks at post, slide, caption and campaign-sequence level, and AS1-AS7 with evidence mode (`cli`, `browser`, `llm_only`, `human_review`) for visuals and rendered posts.
6. Grade A, B, C or F and write the report: blocking findings, slop findings by severity, what's good, recommended next step, each finding with quoted evidence and a concrete fix.
7. If the verdict is F, stop: the next asset or iteration does not start until the blocking findings are fixed.
8. After fixes, rerun the audit on the corrected artefact and log the new verdict; run it again at each checkpoint and as the final gate before publishing.

## Yardstick and verified evidence

Low-quality content produced in quantity by AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Three diagnostic properties (Kommers et al., *"Why Slop Matters"*, arXiv 2601.06060, verified): **superficial competence, asymmetric effort, mass producibility**. The human tell: **absence of intent**. You are measuring how strongly an artefact exhibits these.

The threat is documented, not rhetorical. Cite these where a client questions why the audit matters; do not embellish them or add unsourced figures:

- Spracklen et al., USENIX Security 2025 (verified): 19.7% of package references suggested by code-generating models were hallucinated — the "slopsquatting" supply-chain risk, relevant whenever AI output names a tool, plugin, or integration to install.
- Veracode (verified): 45% of AI-generated code samples introduced a known vulnerability; cross-site scripting failures in 86% of relevant cases; log-injection failures in 88%. Treat any AI-suggested embed, pixel, or script with the same suspicion.

These belong in the *evidence* column, not as decorative statistics. Use them only when on point.

## Grades

Aggregate into a grade:

| Grade | Meaning | Trigger |
|---|---|---|
| **A — Clean** | No blocking hits; genericness low; substance and intent present | ship |
| **B — Minor slop** | A few automated hits, no blockers; some genericness | fix listed items |
| **C — Slopy** | Multiple automated hits or weak substance/intent | rework before ship |
| **F — Blocked** | Any [BLOCK] blocker (fabricated stat/citation, garbled publishable image text, deceptive claim) OR no substance at all | do not ship |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| AI slop audit report (verdict, genericness score, blocking findings, slop findings, what's good, next step) | Content owner and client reviewer | Every finding cites evidence from the artefact and carries a concrete fix; any [BLOCK] forces an F. |
| Verdict log entry for the checkpoint | Delivery lead and the next workflow | Records artefact, date, grade and whether progression is blocked. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Finding evidence | Quoted line, slide number, colour value, frame reference or URL per finding | No finding without evidence; inferences marked "(inference)". |
| Genericness score with drivers | Score 0–100 and named drivers in the report header | Drivers are measurable (for example banned-word density per 500 words). |
| Overlay record | ME1-ME7 and AS1-AS7 rows with evidence mode | Unavailable render evidence is `NOT_ASSESSED`; non-visual checks are `not_applicable`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. The audit reports findings and fixes; it does not rewrite or publish the artefact.

## Degraded Mode

Without the artefact or its render and source evidence, return the narrowest qualified result and mark the affected checks `not assessed`. The written-content gates can still be run on supplied text, with image, video and citation checks recorded as `NOT_ASSESSED` and no grade above the evidence seen.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Any [BLOCK] hit (fabricated statistic or citation, garbled publishable image text, deceptive claim) or no substance at all | Grade F and block progression to the next asset or submission. | Shipping fabricated or deceptive content. |
| The only signals are emojis, repeated openers, three-part phrasing or a familiar cadence | Do not call the post AI-written; cite the exact unit and the audience-value loss as a style finding. | False authorship accusations. |
| A repeated safety warning, accessibility label or approved campaign message recurs | Record it as a functional exception, not slop. | Stripping required repetition. |
| A visual uses purple gradients, glassmorphism, neon glow, AI-beige defaults, decorative editorial scaffolding or decorative motion | Report a blocking visual finding unless a functional state, accessibility need, data encoding or approved brand reason is recorded. | Generator-default visuals shipping. |
| SynthID is absent from an image | Do not treat absence as proof either way (Google-only). | Misreading provenance. |
| The artefact is a campaign or calendar | Audit each post and asset, then the set (do all twelve captions share one template?). | Missing set-level uniformity. |
| The artefact is clean | Report "This artefact is clean" honestly. | Invented flaws that erode trust in the audit. |
| A claim, date, link, testimonial, platform limit or performance number appears | Verify it and distinguish internal links from evidence citations; unverifiable items are `NOT_ASSESSED` or a [BLOCK] if fabricated. | Treating a plausible figure as verified. |

## Quality Standards

- Every finding is evidenced with a quoted line, slide number, colour value, frame reference or URL from the artefact.
- No fabricated flaws: nothing is raised that is not actually present, and a clean verdict is reported honestly when earned.
- A 0–100 genericness score is given and its main drivers named.
- Blocking and non-blocking findings are separated; any [BLOCK] blocker is called out distinctly and forces an F.
- Each finding has a concrete fix, a specific action, not "improve this".
- What's good is preserved: substantive, authored elements are named so a fix does not strip them.
- Localisation is judged: the report states whether the artefact fits the Uganda / East Africa (or named) market.
- Verified evidence only: the Merriam-Webster, Kommers, Spracklen, and Veracode figures are used verbatim and only when on point; no new statistics are invented.

## Anti-Patterns

- Running the audit once at the end. Fix: run it after each major iteration and log the verdict each time, like a test suite at every checkpoint.
- Presenting a guess as a measured fact. Fix: mark inferences "(inference)".
- Padding the report with invented flaws. Fix: raise only what is present; "This artefact is clean" is a valid, wanted verdict.
- Stripping the strong parts while fixing slop. Fix: list what's good so the rewrite keeps it.
- Grading one caption from a set in isolation. Fix: audit each asset and the set as a whole for shared templates.
- Letting a C or F artefact move on because the deadline is close. Fix: an F blocks progression; a C needs rework before ship.
- Using the Spracklen or Veracode figures as decoration. Fix: cite them only where a client questions why the audit matters.

## References

- [Audit method](references/audit-method.md): read when running the cadence, the layered checks by artefact type, the ME1-ME7 and AS1-AS7 overlays, the report template, the responsibility audit or the see-also routes.
- [`anti-ai-slop`](../anti-ai-slop/SKILL.md): read when fixing findings or humanising the draft (prevention companion and banned list).
- [`policy-ai-content-ethics`](../../policies/policy-ai-content-ethics/SKILL.md): read when a finding involves disclosure, copyright or cultural bias.
- [AI-slop responsible publishing standard](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/references/ai-slop-responsible-publishing-standard-2026-09-11.md): read when separating style findings from deception, cultural harm or provenance.
- [Creative review gate](../../../docs/quality-gates/creative-review-gate.md): read when the audited asset is finished creative going to release.
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md): read when the question is AI maturity rather than an artefact.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide cadence rule and anti-slop gates.
<!-- dual-compat-end -->
