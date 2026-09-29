# AI slop audit method

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); text unchanged except that the yardstick, the grade table and the verified-evidence section stay verbatim in `SKILL.md`, as noted under their headings. Read when running the layered audit checks, the ME1-ME7 and AS1-AS7 overlays, scoring genericness or writing the audit report.

## Machine-error audit extension

Report ME1-ME7 at post, slide, caption, and campaign-sequence level. Cite the repeated or inflated
unit and state the missing audience value. Do not treat a repeated safety warning, accessibility
label, or approved campaign message as slop; record it as a functional exception.

### Impeccable-derived overlay audit

For social visuals, campaign decks, landing-page handoffs, and rendered posts, report AS1-AS7 with
evidence mode and concrete location. Purple gradients, glassmorphism, neon glow, AI-beige defaults,
decorative editorial scaffolding, and decorative motion are blocking visual findings unless a
functional state, accessibility need, data encoding, or approved brand reason is recorded. Mark
non-visual checks `not_applicable` and unavailable render evidence `NOT_ASSESSED`.

The detector. Given any social artefact, it decides how strongly it reads as AI slop, names exactly why, and says how to fix each finding. Production-side prevention is the companion `anti-ai-slop` skill.

## When this runs
**Cadence — run after EACH major iteration of work.** This is the default mode: whenever a meaningful unit of social work is completed — a drafted caption or post, a finished thread or carousel, a completed campaign or content calendar, a deck outline, a significant revision — run this audit on what was just produced before moving on. Log the verdict. If the verdict is **F (Blocked)**, do not progress to the next asset or iteration until the blocking findings are fixed. Treat it like a test suite that runs at every checkpoint, not a one-time final review.

Also auto-run when the user asks to **analyse, review, evaluate, audit, critique, score, or de-slop** any of: a caption, post, thread, carousel, ad copy, full campaign, content calendar, blog or article, email or email sequence, deck outline, profile/bio, an AI image, or an AI video — or asks "is this AI slop / does this look AI-generated / why does this feel off?". Also run as the final gate before publishing any engine output. The companion `anti-ai-slop` skill runs continuously *during* drafting; this audit runs *at each checkpoint* to catch what slipped through.

## What slop is (the yardstick)

Kept verbatim in the parent [`SKILL.md`](../SKILL.md) (Yardstick and verified evidence; Grades) so there is one copy; read it there.

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
- (auto) Frame-to-frame "boiling", lip-sync drift, morphing hands/objects, impossible motion; missing disclosure where the platform or `policy-ai-content-ethics` (AI IP and copyright policy) requires it.

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

Kept verbatim in the parent [`SKILL.md`](../SKILL.md) (Yardstick and verified evidence; Grades) so there is one copy; read it there.

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

Kept verbatim in the parent [`SKILL.md`](../SKILL.md) (Yardstick and verified evidence; Grades) so there is one copy; read it there.

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
- `anti-ai-slop` (humanising rewrite passes) — broader humanisation QC; complementary checklist and banned list.
- `meta-content-audit` — performance/quality audit of a content set (different lens: engagement, not authenticity).
- `language/east-african-english`, `language/french-native-copy` — apply house style and native-language standards when judging written output.

## Responsibility audit

Do not call a post AI-written because it has emojis, repeated openers, three-part phrasing, or a
familiar cadence. Cite the exact unit and audience-value loss for style findings. Verify claims,
dates, links, testimonials, platform limits, and performance numbers; distinguish internal links
from evidence citations. Separate stylistic concerns from deception, cultural harm, provenance,
and garbled visual text. Unavailable review evidence is `NOT_ASSESSED`.

- Shared standard: [`AI-slop responsible publishing`](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/references/ai-slop-responsible-publishing-standard-2026-09-11.md)
