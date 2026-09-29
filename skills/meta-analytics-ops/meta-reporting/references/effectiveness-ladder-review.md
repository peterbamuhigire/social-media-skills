# Effectiveness-ladder review, brand tracking and AI-feature search reporting

Read when a campaign ends and the client needs a post-campaign effectiveness review, when the monthly or quarterly report must show outcomes rather than activity, when brand effects need tracking over time, or when the client asks how much traffic comes from Google's AI features. This file owns the post-campaign review for the engine; `creative-brief-and-big-idea` and `playbook-pr-publicity` point here.

## 1. The outcome ladder

Report every campaign as the highest rung it can prove, and never present a lower rung as a higher one. The ladder below is the engine's own structure, informed by the effectiveness-ladder concept in *The Effectiveness Code* (Hurman and Field, 2020; register `WARC-EFFECTIVENESS-CODE-2020`). The Code's own ladder (verified in the register record) runs from Influential Idea through Behaviour Breakthrough, Sales Spike, Brand Builder and Commercial Triumph to Enduring Icon, with longer measurement horizons at the higher rungs (about three months for a sales spike, twelve for a commercial triumph, three years for an enduring icon); map each engine rung to the nearest Code level when reporting to clients who use the Code.

| Rung | What it proves | Typical evidence | Not enough on its own |
|---|---|---|---|
| 1. Delivery | The work ran and was seen | Reach, frequency, impressions, coverage, spend against plan | Says nothing about effect |
| 2. Response | People noticed and reacted | Views to 50%, engagement, recall and brand-linkage playback, comment themes | Reactions can be cheap and unlinked to the brand |
| 3. Behaviour | People did something the objective needs | Enquiries, WhatsApp chats, store visits, sign-ups, trial, qualified leads | May be pulled forward from future sales |
| 4. Brand | How people think about the brand changed | Tracked awareness, consideration, associations, distinctive-asset recognition, over repeated waves | Needs a baseline and comparable waves |
| 5. Commercial | The business moved | Sales, market share, penetration, price held, margin, customer value; incremental where measured | Needs other causes (price, distribution, season) ruled in or out |

A result sustained over a year or more at rung 4 or 5 is labelled "sustained"; a single month is not.

## 2. Post-campaign review procedure

1. Restate the brief's objective, audience, time horizon and the rung it targeted; a brief that targeted rung 5 is judged at rung 5.
2. Collect evidence per rung with source and date; mark any rung without data `not assessed`.
3. Check causality: control or holdout results, geo or time comparisons, or incrementality work from `advertising-attribution-and-measurement`; otherwise label effects "associated with", not "caused by".
4. Compare against the pre-test prediction and the concept-screen reading from `creative-brief-and-big-idea`; record whether the prediction held.
5. Record what the creative choice was (emotional, rational or both) and whether short- and long-term effects matched the expectation.
6. Write the verdict in one line: the highest rung proved, the size of effect with its uncertainty, and the next decision.
7. File the learning in the test register and the Kaizen campaign learning loop.

Report layout: the verdict line, a ladder table with one row per rung, then caveats. In the monthly report, add a short "Outcomes this month" block under the period summary showing rungs 3 to 5 only when evidence exists.

## 3. Brand tracking over time (pointer)

Rung 4 needs repeated, comparable measurement: the same questions, sample definition and timing each wave. The design (questions, distinctive-asset recognition, category entry points, affordable options for SMEs such as short phone or WhatsApp surveys and platform brand-lift studies where budgets allow) belongs to [`brand-strategy-and-distinctive-assets`](../../../strategy/brand-strategy-and-distinctive-assets/SKILL.md). In reporting: show brand measures as a trend across waves with sample size per wave; never compare waves with different questions or samples; label single waves as a baseline.

## 4. Traffic from Google AI features (AI Overviews, AI Mode)

What Google documents (register `GOOGLE-AI-FEATURES-2025`, read live 29 Sep 2026; page last updated 10 Dec 2025): sites that appear in AI features such as AI Overviews and AI Mode are included in overall search traffic in Search Console, reported in the Performance report under the "Web" search type.

Report it carefully:

- Search Console, as documented, does not give AI-feature traffic as a separate line on that page; whether any separate filter exists in the product today is `NOT_ASSESSED`. Do not present any figure as "AI Overview clicks" unless the tool shows a documented dimension for it.
- Report total Web search clicks, impressions and positions as usual, and add a note that they include AI-feature appearances.
- Where a client wants a signal, report proxies with their limits labelled: query-level shifts in impressions against clicks for question-style queries; landing-page trends; GA4 referral traffic from AI assistants (a separate source, not Google AI features). Route optimisation to `seo-geo-optimisation` and `ai-generative-search-optimisation`.

## Sources

- `WARC-EFFECTIVENESS-CODE-2020`: Hurman and Field, *The Effectiveness Code*, WARC and Cannes Lions, 2020 (concept).
- `GOOGLE-AI-FEATURES-2025`: Google Search Central, AI features and your website (page re-read 29 Sep 2026).
- `IPA-LONG-SHORT-2013`: Binet and Field, 2013 (short- and long-term effects; concept only).
