---
name: ai-slop-audit
description: Use when AI Slop Audit is needed to produce an evidence-backed audit report for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Slop Audit

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **evidence-backed audit report** and the supplied brief falls within ai slop audit.

## Do Not Use When
- Use `ai-readiness-diagnostic` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| AI marketing use-case brief, intended human control point and success measure | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Issue a qualified finding and identify the evidence needed. |

## Capability and Permission Boundaries
Default to read-only: inspect supplied material and report findings. Editing, publishing, contacting people, spending, or changing live systems requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified evidence-backed audit report; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact evidence-backed audit report, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete evidence-backed audit report; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Evidence-backed audit report | Requester, client reviewer or delivery team | The evidence-backed audit report addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Finding-to-source register and unassessed-check list | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested evidence-backed audit report, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

The detector. Given any social artefact, it decides how strongly it reads as AI slop, names exactly why, and says how to fix each finding. Production-side prevention is the companion `anti-ai-slop` skill.

## When this runs
**Cadence — run after EACH major iteration of work.** This is the default mode: whenever a meaningful unit of social work is completed — a drafted caption or post, a finished thread or carousel, a completed campaign or content calendar, a deck outline, a significant revision — run this audit on what was just produced before moving on. Log the verdict. If the verdict is **F (Blocked)**, do not progress to the next asset or iteration until the blocking findings are fixed. Treat it like a test suite that runs at every checkpoint, not a one-time final review.

Also auto-run when the user asks to **analyse, review, evaluate, audit, critique, score, or de-slop** any of: a caption, post, thread, carousel, ad copy, full campaign, content calendar, blog or article, email or email sequence, deck outline, profile/bio, an AI image, or an AI video — or asks "is this AI slop / does this look AI-generated / why does this feel off?". Also run as the final gate before publishing any engine output. The companion `anti-ai-slop` skill runs continuously *during* drafting; this audit runs *at each checkpoint* to catch what slipped through.

## What slop is (the yardstick)
Low-quality content produced in quantity by AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Three diagnostic properties (Kommers et al., *"Why Slop Matters"*, arXiv 2601.06060, verified): **superficial competence, asymmetric effort, mass producibility**. The human tell: **absence of intent**. You are measuring how strongly an artefact exhibits these.

## Audit method — layered, cheapest first
### Step 1 — Identify artefact type and load the right checklist
Map the artefact to one or more domains: written content (EN/FR), image, video. A campaign or content calendar usually spans several — audit each post and each asset, then the set as a whole (do all twelve captions share one template?).

### Step 2 — Automated gates ((auto), machine-checkable) — any hit is hard evidence
Run every applicable check; a hit on a **blocking** marker ([BLOCK]) fails the artefact outright.

**Written content (captions, posts, threads, carousels, ad copy, blog, email)**
- (auto) Focal-word density — delve/tapestry/realm/navigate/underscore/pivotal/intricate/leverage/elevate/seamless etc. >2 per 500 words (for short captions: any single banned word is a flag).
- (auto) Em-dash density >1 per paragraph; reflexive rule-of-three; "it's not X, it's Y" repetition; uniform 15–25-word sentences (low burstiness); identical-shape carousel slides.
- (auto) Transition / opener clichés ("in today's fast-paced world", "in today's digital age", "let's dive in", "in conclusion", "Unpopular opinion:", "Let that sink in").
- (auto) Mechanical formatting: Title-Case headers, excess bold, decorative-emoji flood, leftover tool markup ("oaicite", "contentReference", "As an AI language model").
- [BLOCK] (auto) Broken/fake citations or fabricated stats: dead URLs, invalid DOI/ISBN, made-up platform figures, "studies show" with no named study, utm_source params copied into the body.
- French (per `language/french-native-copy`): "plongeons dans", "il est important de noter que", "force est de constater", "dans un monde en constante évolution", filler connectors ("par ailleurs / de plus / en outre"), raw-translation artefacts.

**Image (for social)**
- (auto) Missing/contradictory C2PA provenance; SynthID absence (Google-only — absence != authentic, so do not treat absence as proof either way); ELA/JPEG-forensics anomalies; the "AI sheen" (over-smooth skin, plastic bokeh, uncanny symmetry).
- [BLOCK] (auto) Garbled text-in-image (illegible on-pack copy, invented logos, nonsense signage) on any asset meant to publish.

**Video (for social)**
- (auto) Frame-to-frame "boiling", lip-sync drift, morphing hands/objects, impossible motion; missing disclosure where the platform or `policy-ai-ip-and-copyright` requires it.

### Step 3 — Structural score ((auto)) -> 0–100 "genericness"
Combine burstiness (sentence-length variation), focal-word density, duplication across a set, and template-similarity into a single genericness score. Higher = more slop-like. Report the score and its drivers (e.g. "78 — every caption opens with a question, banned-word density 5/500, three slides restate each other").

### Step 4 — Human-judgement review ((human)) — the checklist no tool replaces
- (human) **Substance:** what does this assert, teach, or decide that required real work? If nothing — slop.
- (human) **Intent / authored voice:** is there a point of view, or is it relentlessly positive and viewpoint-free?
- (human) **Specificity:** real named examples, places, people, numbers, UGX prices — or generic placeholders and "African" stand-ins?
- (human) **Hard parts:** are objections, the audience that won't buy, the risk, the negative-comment / crisis path handled?
- (human) **Localisation:** UGX, Mobile Money, WhatsApp-first, real local references for the default Uganda / East Africa market (or named market) — or Western defaults (credit cards, "swipe up", US examples)?
- (human) **Visuals:** anatomy (hands/eyes/teeth), "AI sheen", garbled text-in-image, impossible geometry, video "boiling"/lip-sync.
- (human) **Domain-specific (per artefact):**
  - *Caption / post:* engagement-bait, no lived experience, clichéd hook, no real CTA tied to a real channel.
  - *Carousel:* slides that restate one another, no through-line, decorative-only final slide with no CTA.
  - *Campaign / strategy:* generic "raise awareness and engage", fabricated market stats, no authored strategic choice, "studies show" without a named study.
  - *Blog/article:* definition-opener, decontextualised statistic, no East African example, sections that restate their heading.
  - *Ad copy:* inflated superlatives, deceptive reach/AI claims, unverifiable promises, no specific offer.
  - *Image/video brief:* generic "African" placeholders, no named setting, no provenance/disclosure plan.

## Scoring & verdict
Aggregate into a grade:

| Grade | Meaning | Trigger |
|---|---|---|
| **A — Clean** | No blocking hits; genericness low; substance and intent present | ship |
| **B — Minor slop** | A few automated hits, no blockers; some genericness | fix listed items |
| **C — Slopy** | Multiple automated hits or weak substance/intent | rework before ship |
| **F — Blocked** | Any [BLOCK] blocker (fabricated stat/citation, garbled publishable image text, deceptive claim) OR no substance at all | do not ship |

## Output format (the audit report)
```
# AI Slop Audit — <artefact name> — <date>
Verdict: <A/B/C/F>   Genericness score: <0-100>
Artefact type(s): <...>

## Blocking findings (X) — must fix
- [marker] <what was found> · evidence: <quoted line / slide no. / colour / frame ref / URL> · fix: <concrete action>

## Slop findings (by severity)
- [marker] <finding> · evidence: <...> · fix: <...>

## What's good (so it isn't stripped in the fix)
- <substantive, specific, authored elements worth keeping>

## Recommended next step
- <rework / targeted fixes / ship>
```

## Discipline (anti-hallucination — applies to the audit itself)
- Every finding cites concrete evidence from the artefact (a quoted line, a slide number, a colour value, a frame reference, a URL). No finding without evidence.
- Do not invent a flaw to pad the report. "This artefact is clean" is a valid, wanted verdict.
- Mark inferences "(inference)"; never present a guess as a measured fact.

## Why slop is a real risk worth auditing (verified evidence)
The threat is documented, not rhetorical. Cite these where a client questions why the audit matters; do not embellish them or add unsourced figures:

- Spracklen et al., USENIX Security 2025 (verified): 19.7% of package references suggested by code-generating models were hallucinated — the "slopsquatting" supply-chain risk, relevant whenever AI output names a tool, plugin, or integration to install.
- Veracode (verified): 45% of AI-generated code samples introduced a known vulnerability; cross-site scripting failures in 86% of relevant cases; log-injection failures in 88%. Treat any AI-suggested embed, pixel, or script with the same suspicion.

These belong in the *evidence* column, not as decorative statistics. Use them only when on point.

## Required Input
Before auditing, confirm:

1. **Artefact** — paste or point to the caption, post, carousel, campaign, blog, email, deck, image, or video to audit.
2. **Artefact type(s)** — written EN / written FR / image / video / multi-asset campaign.
3. **Client business name and industry** — to judge whether specifics are real and on-brand.
4. **Country / city** — to judge localisation. (Default: Uganda / East Africa.)
5. **Intended channel and goal** — to judge fit and CTA.

## Quality Criteria
The audit meets the standard when:

1. **Every finding is evidenced** — each carries a quoted line, slide number, colour value, frame reference, or URL from the artefact.
2. **No fabricated flaws** — nothing is raised that is not actually present; a clean verdict is reported honestly when earned.
3. **Genericness scored with drivers** — a 0–100 score is given and its main drivers named.
4. **Blocking vs non-blocking separated** — any [BLOCK] blocker is called out distinctly and forces an F.
5. **Each finding has a concrete fix** — a specific action, not "improve this".
6. **What's good is preserved** — substantive, authored elements are named so a fix does not strip them.
7. **Localisation judged** — the report states whether the artefact fits the Uganda / East Africa (or named) market.
8. **Verified evidence only** — the Merriam-Webster, Kommers, Spracklen, and Veracode figures are used verbatim and only when on point; no new statistics are invented.

## See also
- `anti-ai-slop` — prevention companion (write, plan, and brief so slop never appears).
- `ai-content-humaniser` — broader humanisation QC; complementary checklist and banned list.
- `meta-content-audit` — performance/quality audit of a content set (different lens: engagement, not authenticity).
- `language/east-african-english`, `language/french-native-copy` — apply house style and native-language standards when judging written output.
