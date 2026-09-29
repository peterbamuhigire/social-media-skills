# S09 preservation log — B10-platforms

Worker: S09 B10 worker (Claude Opus 5.5), 29 Sep 2026. Start commit `0e0af8a`. Method: lean template (roadmap §7); moves per S09-T03..T10. Every body section below the contract markers was moved text-unchanged into a new reference in the same skill (only relative links re-levelled where noted), so platform spec tables, character limits, algorithm notes, figures, dates, register IDs and "verify" labels are preserved verbatim. Frontmatter, `## Use When` and `## Do Not Use When` are byte-identical to HEAD (routecheck 0 changed).

Generic contract scaffolding replaced in every skill (counted once here, row 1 of each table): the three generic Required Inputs rows, the generic Capability paragraph, the generic Degraded Mode paragraph, generic workflow steps 1–5, the two generic Outputs rows, the two generic Evidence rows, the one-paragraph generic Quality Standards, the six generic anti-patterns, and the "Use the directly cited sources…" References line. The three generic decision rows ("Account is absent…", "Evidence shows an established account…", "A rule, limit or feature is time-sensitive…") were kept as domain-worded equivalents (same condition, action and failure, platform named).

## platform-facebook — 142 → 114 lines (gated shared ratio 30.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "A peer-to-peer community is the primary need" | KEPT | SKILL.md § Decision Rules row 1 |
| 3 | Decision row "The plan targets Uganda" (UG-FACEBOOK-ACCESS-2026; restored 13 Jun 2026 after the January 2021 block; no UCC statement; WhatsApp/Instagram/SMS fallback) | KEPT (verbatim) | SKILL.md § Decision Rules row 5; also § Required Inputs row 5, § Workflow step 5, § Quality Standards, § Anti-Patterns |
| 4 | Workflow step 3 link to the channel creative and service lab | KEPT | SKILL.md § Workflow step 3 and § References |
| 5 | "## Page, community and conversion plan" | MOVED (text unchanged) | references/facebook-page-community-and-enquiry-method.md; also § Required Inputs, § Workflow step 2 |
| 6 | "## Creative and community choices" | MOVED (text unchanged) | same reference; group rules → § Quality Standards; criticism/prospect-list rules → § Anti-Patterns |
| 7 | "## Enquiry and service handoff" (response decision tree) | MOVED (text unchanged) | same reference; also § Workflow step 4, § Decision Rules row 7 |
| 8 | "## Pilot, paid readiness and reporting" | MOVED (text unchanged) | same reference; also § Workflow steps 6–7, § Decision Rules row 8, § Evidence Produced |
| 9 | "## Worked example and acceptance" (retail post, stock/delivery) | MOVED (text unchanged) | same reference; rule → § Decision Rules row 6 |
| 10 | "## Operational reference" (lab link) | MERGED-INTO-CONTRACT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding (generic degraded line, generic workflow step 3 wording, generic Outputs row), 0 paraphrased, 0 lost; validator clean.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: none.

## platform-google-business-profile — 430 → 119 lines (gated shared ratio 8.3 % → 0.0 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows "no customer-facing premises" and "goal is footfall… location reference" | KEPT | SKILL.md § Decision Rules rows 1 and 4 |
| 3 | "## Required Input" (9 intake items) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | references/gbp-setup-optimisation-and-review-method.md § Required Input; SKILL.md § Required Inputs rows 1–4 |
| 4 | "## 1. GBP Setup and Verification Checklist" (Steps 1–5, category table, verification methods, postcard 5–7 business days / 2–3 weeks / video after 3 weeks) | MOVED (text unchanged) | same reference § 1; also § Workflow step 2, § Decision Rules rows 6–7 |
| 5 | "## 2. Profile Optimisation Checklist — 10-Point Completeness Score" (750 characters, 58/1,000 characters, minimum 8 photos, holiday list, UTM string) | MOVED (text unchanged) | same reference § 2; also § Workflow step 3, § Anti-Patterns |
| 6 | "## 3. Photo Strategy" (1024×575px, 250×250px, 35%, 9-photo minimum viable set, 2 new photos per month) | MOVED (text unchanged) | same reference § 3 |
| 7 | "## 4. GBP Posts Strategy" (post-type table, 7-day expiry, 3-step formula, 150–300 words, UGX examples, UTM) | MOVED (text unchanged) | same reference § 4 |
| 8 | "## 5. Q&A Management" (10 universal starters, 48 hours) | MOVED (text unchanged) | same reference § 5; also § Required Inputs row 4 |
| 9 | "## 6. Review Management Strategy" (templates, 30 minutes, 24/48 hours, no incentives) | MOVED (text unchanged) | same reference § 6; also § Anti-Patterns 2 and 5, § Quality Standards 2 |
| 10 | "## 7. GBP Performance Metrics" (metric table, 4.2 rating, +2 reviews/month under 50, monthly checklist) | MOVED (text unchanged) | same reference § 7; also § Decision Rules row 8, § Evidence Produced row 3 |
| 11 | "## 8. Local SEO Integration" (relevance/distance/prominence, NAP rule, citations) | MOVED (text unchanged) | same reference § 8; also § Evidence Produced row 2, § Quality Standards 7 |
| 12 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8 criteria kept; NAP bullet added, response-template and WhatsApp-template bullets combined) |
| 13 | References line for location-based-and-proximity-marketing | KEPT | SKILL.md § References |
| 14 | Existing reference `location-based-and-proximity-marketing.md` cites "SKILL.md §1–§8" | Appended section "Where the SKILL.md sections now live" (pointer only; original text unchanged) | references/location-based-and-proximity-marketing.md |

Checks: factcheck 0 missing; linecheck 5 flagged → 5 scaffolding (generic Required Inputs row, degraded line, workflow step 3, Outputs row, "Output meets the standard when it:" lead-in), 0 lost; validator clean.
Paraphrased lines: none beyond the merged Quality Criteria (covered).
Noticed, not changed: GBP photo minimum — HEAD 10-point score says "Minimum: 8 photos" and the minimum viable set totals 9 (both now in references/gbp-setup-optimisation-and-review-method.md §2 and §3); references/location-based-and-proximity-marketing.md sets 10 photos as the Essential floor (its own note already flags the difference). All three figures kept as they are.

## platform-instagram — 154 → 113 lines (gated shared ratio 27.1 % → 1.8 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision rows "discovery and proof", "growth stalled → growth diagnosis", "grid or visual standards brief → chwezi-design-engine" | KEPT | SKILL.md § Decision Rules rows 1, 5, 6 |
| 3 | References lines for growth-diagnosis and grid-and-visual-system | KEPT | SKILL.md § References |
| 4 | "## Profile and visual proof" | MOVED (text unchanged; grid link re-levelled) | references/instagram-format-discovery-and-sales-method.md; also § Workflow step 2, § Anti-Patterns 1–2 |
| 5 | "## Format and series decisions" | MOVED (text unchanged) | same reference; also § Workflow step 3, § Quality Standards 2–3, 5, § Anti-Patterns 3–4 |
| 6 | "## Discovery and creator partnerships" | MOVED (text unchanged) | same reference; also § Required Inputs row 5, § Quality Standards 4 and 6, § Anti-Patterns 5 |
| 7 | "## Instagram to sales" | MOVED (text unchanged) | same reference; also § Capability, § Decision Rules row 8, § Anti-Patterns 6 |
| 8 | "## Pilot and review" | MOVED (text unchanged) | same reference; also § Evidence Produced row 3, § Quality Standards 7 |
| 9 | "## Worked example and acceptance" | MOVED (text unchanged) | same reference; also § Decision Rules row 7, § Quality Standards 1 |
| 10 | "## Operational reference" (lab link) | MERGED-INTO-CONTRACT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 3 flagged → 3 scaffolding, 0 lost; validator clean.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: none.

## platform-linkedin — 185 → 118 lines (gated shared ratio 23.5 % → 3.3 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Acknowledgement line (Peter Bamuhigire, techguypeter.com, +256 784 464178) | KEPT (verbatim) | SKILL.md intro |
| 3 | AI-search pointer paragraph (LinkedIn citation section; sample-bound hypotheses) | MERGED-INTO-CONTRACT | SKILL.md § References (with its caveat) |
| 4 | "## Evidence boundary" | MOVED (text unchanged) + MERGED | references/linkedin-practitioner-content-and-pilot-method.md § Evidence boundary; SKILL.md § Quality Standards 7 |
| 5 | Decision rows "named practitioner" and "Company Page, sub-pages or events" | KEPT | SKILL.md § Decision Rules rows 1 and 5 |
| 6 | Workflow step 3 (consulting authority; profile, content, website, CRM handoff) | CONDENSED-IN-PLACE | SKILL.md § Workflow step 5 |
| 7 | "## Practitioner and company decisions" (collect list) | MOVED (text unchanged) | same reference; also § Required Inputs, § Workflow step 2, § Anti-Patterns 1 |
| 8 | "## Profile review" | MOVED (text unchanged) | same reference; also § Workflow step 3, § Anti-Patterns 2 |
| 9 | "## Content choices" | MOVED (text unchanged; link re-levelled) | same reference; also § Workflow step 4, § Anti-Patterns 3–4 |
| 10 | "## Thirty-day pilot" | MOVED (text unchanged) | same reference; also § Workflow step 6, § Outputs row 3, § Anti-Patterns 7 |
| 11 | "## Conversations and employee participation" | MOVED (text unchanged; link re-levelled) | same reference; also § Capability, § Anti-Patterns 5–6 |
| 12 | "## Measurement and review" | MOVED (text unchanged) | same reference; also § Evidence Produced row 3, § Decision Rules row 8 |
| 13 | "## Other professional identities" | MOVED (text unchanged) | same reference; also § Decision Rules row 7 |
| 14 | "## Worked example" | MOVED (text unchanged) | same reference; also § Decision Rules row 6 |
| 15 | "## Release criteria" (6 bullets) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | same reference; SKILL.md § Quality Standards 1–6 (verbatim) |
| 16 | "## Operational reference" and existing References lines | MERGED-INTO-CONTRACT | SKILL.md § References (all four references linked) |

Checks: factcheck 0 missing; linecheck 3 flagged → 2 scaffolding, 1 paraphrased, 0 lost; validator clean.
Paraphrased lines: workflow step 3 "Apply consulting authority to pipeline… Connect the profile, evidence-bearing content, website destination and CRM handoff" → SKILL.md § Workflow step 5.
Noticed, not changed: none.

## platform-tiktok — 146 → 111 lines (gated shared ratio 29.1 % → 1.8 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "A trend conflicts with the brand…" | KEPT | SKILL.md § Decision Rules row 1 |
| 3 | "## Audience, offer and account decision" (NOT_ASSESSED rule) | MOVED (text unchanged) | references/tiktok-native-video-rights-and-testing-method.md; also § Required Inputs rows 1 and 4, § Workflow step 2 |
| 4 | "## Develop native video with evidence" | MOVED (text unchanged) | same reference; also § Workflow steps 3–4, § Quality Standards 2–3, § Anti-Patterns 1, 4, 5 |
| 5 | "## Rights and participation" | MOVED (text unchanged) | same reference; also § Required Inputs row 5, § Workflow step 5, § Decision Rules row 5 |
| 6 | "## Production and paid testing" | MOVED (text unchanged) | same reference; also § Workflow steps 6–7, § Decision Rules row 7, § Anti-Patterns 2–3 |
| 7 | "## Measurement and acceptance" (synthetic case) | MOVED (text unchanged) | same reference; also § Evidence Produced row 3, § Decision Rules row 6, § Quality Standards 7 |
| 8 | "## Operational reference" (lab link) | MERGED-INTO-CONTRACT | SKILL.md § References |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding, 0 lost; validator clean.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: none.

## platform-whatsapp — 386 → 117 lines (gated shared ratio 10.5 % → 1.6 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "Important" blockquote (direct channel, permission-based, spam destroys trust) | CONDENSED-IN-PLACE + MOVED (verbatim) | SKILL.md intro; references/whatsapp-channel-playbook.md (top) |
| 3 | Decision rows "privacy and one-way updates → broadcast" and "day-to-day operations → app operations" | KEPT | SKILL.md § Decision Rules rows 1 and 5 |
| 4 | References (source register, legal gate, app operations) | KEPT | SKILL.md § References; campaign-and-broadcast-sequences reference added |
| 5 | "## Required Input" (10 items) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | references/whatsapp-channel-playbook.md § Required Input; SKILL.md § Required Inputs |
| 6 | "## 1. WhatsApp Business App Setup Checklist" (256 characters, 640×640px, 50×50px, 3–5 catalogue items, "contact for pricing", quick replies, labels 30/60 days) | MOVED (text unchanged) | same reference § 1; also § Workflow step 2 |
| 7 | "## 2. Broadcast List Strategy and Segmentation" (60-day segments) | MOVED (text unchanged) | same reference § 2; also § Workflow step 3 |
| 8 | "## 3. Broadcast Content Guidelines" (max 3/week, 2 safer, 4/week for 2 weeks in campaigns, under 150 words, STOP) | MOVED (text unchanged) | same reference § 3; also § Workflow step 4, § Decision Rules row 6, § Anti-Patterns 2–4 |
| 9 | "## 4. WhatsApp Status Content Plan" (1–3/day, 24 hours, EAT windows) | MOVED (text unchanged) | same reference § 4 |
| 10 | "## 5. WhatsApp Groups Strategy" (comparison table, rules template, 3–5 posts/week, 24 hours) | MOVED (text unchanged) | same reference § 5; also § Workflow step 5, § Anti-Patterns 5 |
| 11 | "## 6. Opt-in Capture Methods and Opt-out Etiquette" | MOVED (text unchanged) | same reference § 6; also § Evidence Produced row 1, § Anti-Patterns 1 |
| 12 | "## 7. 30-Day Broadcast Message Calendar" incl. "### Week-by-Week Plan" and "### 12 Full Message Templates" | MOVED (text unchanged) | same reference § 7; also § Outputs row 3 |
| 13 | "## 8. WhatsApp-specific KPIs" (85–98%, 10–20%, 20–40%, 5–10%, 2 hours, 2%, 5–15%, 14 days) | MOVED (text unchanged) | same reference § 8; also § Evidence Produced row 3, § Anti-Patterns 6 |
| 14 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |
| 15 | Existing reference `whatsapp-business-app-operations.md` compares "the parent skill" figures | Appended section "Where the parent skill's figures now live" (pointer only; original text unchanged) | references/whatsapp-business-app-operations.md |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding, 0 lost; validator clean.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed (all kept exactly as they were; the new playbook's provenance line lists them and SKILL.md § Decision Rules row 7 tells the planner to pick one per client):
- Active/lapsed line: 60 days in references/whatsapp-channel-playbook.md §1–§2 (from HEAD SKILL.md) vs 90 days in references/whatsapp-business-app-operations.md §3.
- Promotional broadcasts: "Maximum 3… 2 per week is safer" in references/whatsapp-channel-playbook.md §3 vs "at most 2 promotional broadcasts a week" in references/whatsapp-business-app-operations.md §3.
- Pricing: "contact for pricing" allowed in references/whatsapp-channel-playbook.md §1 vs "never blank" in references/whatsapp-business-app-operations.md §4 (its release checklist allows the recorded "contact for pricing" choice).
- Chat-list thumbnail: 50×50px in references/whatsapp-channel-playbook.md §1 vs about 48×48px in references/whatsapp-business-app-operations.md §1.
- Quick replies 5–8 (playbook) vs at least 10 (operations reference) — the operations reference already frames this as an extension.

## platform-x-twitter — 392 → 114 lines (gated shared ratio 10.5 % → 1.7 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | "Before generating this plan" blockquote (fit check; audience list; B2B vs FMCG) | CONDENSED-IN-PLACE + MOVED (verbatim) | SKILL.md intro, § Required Inputs row 2, § Workflow step 1, § Decision Rules rows 5–6; references/x-channel-playbook.md (top) |
| 3 | Decision row "live topic… facts unverified" | KEPT | SKILL.md § Decision Rules row 1 |
| 4 | "## Required Input" (8 items) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | references/x-channel-playbook.md § Required Input; SKILL.md § Required Inputs |
| 5 | "## EA Market Context" (hashtag communities) | MOVED (text unchanged) | same reference; also § Decision Rules rows 5–6 |
| 6 | "## 1. Profile Optimisation" (160 characters, 1500×500px) | MOVED (text unchanged) | same reference § 1; also § Anti-Patterns 4–5 |
| 7 | "## 2. Content Types and Rationale" (280 characters, Spaces 48 hours) | MOVED (text unchanged) | same reference § 2; also § Anti-Patterns 6 |
| 8 | "## 3. Posting Frequency Guide" (5–7 and 3–5 per day, 5–10 replies, EAT windows) | MOVED (text unchanged) | same reference § 3; also § Decision Rules row 8 |
| 9 | "## 4. Thread Strategy" (10-post structure; five topic ideas) | MOVED (text unchanged) | same reference § 4 |
| 10 | "## 5. Community Building Tactics" | MOVED (text unchanged) | same reference § 5; also § Anti-Patterns 1–3 |
| 11 | "## 6. X's Role in the EA Media Ecosystem" (within the hour for regulated industries) | MOVED (text unchanged) | same reference § 6; also § Decision Rules row 7, § Anti-Patterns 7 |
| 12 | "## 7. 30-Day Content Plan" incl. "### Weekly Content Rhythm", "### 4 Full Thread Outlines", "### 20 Single Post Ideas", "### 8 Poll Ideas" | MOVED (text unchanged) | same reference § 7; also § Outputs row 3 |
| 13 | "## 8. X-specific KPIs" (20%, 1–3%, analytics.twitter.com) | MOVED (text unchanged) | same reference § 8 |
| 14 | "## Quality Criteria" (8 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (all 8) |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding, 0 lost; validator clean.
Paraphrased lines: none beyond scaffolding (Quality Criteria lines kept close to verbatim).
Noticed, not changed: frequency guidance of "5–7 posts per day" (growth) sits alongside the Quality Criteria rule that a client who can post twice per day gets a twice-per-day plan; both kept. The playbook provenance line adds a pointer to the skill's existing "verify time-sensitive platform figures" decision rule; no figure changed.

## platform-youtube — 362 → 114 lines (gated shared ratio 12.1 % → 1.7 %)

| # | HEAD block (heading or item) | Action | Destination |
|---|---|---|---|
| 1 | Generated contract prose (see header) | REPLACED-BY-CANONICAL / domain rows | SKILL.md contract sections |
| 2 | Decision row "durable explanation → long-form, Shorts after" | KEPT | SKILL.md § Decision Rules row 1 |
| 3 | "## Required Input" (9 items) | MOVED (text unchanged) + MERGED-INTO-CONTRACT | references/youtube-channel-playbook.md § Required Input; SKILL.md § Required Inputs |
| 4 | "## EA Market Context" (5–12 minutes, Shorts under 60 seconds, Hero/Hub/Hygiene, bilingual titles) | MOVED (text unchanged) | same reference; also § Workflow step 2, § Decision Rules row 5, § Anti-Patterns 6 |
| 5 | "## 1. Channel Setup and Optimisation" (2560×1440px, 1546×423px, 800×800px, 1,000 characters, 60–90 seconds, 20 seconds) | MOVED (text unchanged) | same reference § 1 |
| 6 | "## 2. Video Type Taxonomy" (Chaffey, 2024 RACE) | MOVED (text unchanged) | same reference § 2 |
| 7 | "## 3. YouTube SEO Content Guidance" (60 characters, 150 characters, 5–10 tags, 20–30%) | MOVED (text unchanged) | same reference § 3; title format also § Quality Standards 2 |
| 8 | "## 4. Video Cadence" (1/week, 6 months, 2/week, Tue/Thu 6–8pm EAT, 24–48 hour window, private-first) | MOVED (text unchanged) | same reference § 4; also § Anti-Patterns 2–3 |
| 9 | "## 5. YouTube Shorts Strategy" (1080×1920px, 30–45 seconds, 3–5 per week) | MOVED (text unchanged) | same reference § 5 |
| 10 | "## 6. Community Tab" (500 subscribers, 2–3 posts per week) | MOVED (text unchanged) | same reference § 6 |
| 11 | "## 7. 30-Day Content Plan" (4 long-form + 8 Shorts table) | MOVED (text unchanged) | same reference § 7; also § Outputs row 3 |
| 12 | "## 8. YouTube-specific KPIs" (20%, 40%+, 3–7%) | MOVED (text unchanged) | same reference § 8 |
| 13 | "## 9. Algorithm Intelligence" (~70% / <20%, watch-time hierarchy, 3-minute CTA, YPP caution) | MOVED (text unchanged) | same reference § 9; also § Decision Rules rows 6–8, § Anti-Patterns 1, 4, 5 |
| 14 | "## 10. Blog Post Angles" (10 titles) | MOVED (text unchanged) | same reference § 10 |
| 15 | "## Quality Criteria" (10 bullets) | MERGED-INTO-CONTRACT | SKILL.md § Quality Standards (8 kept); 2 (Section 9 algorithm, Section 10 blog angles) → references/youtube-channel-playbook.md § Release checklist (overflow from Quality Standards), verbatim |

Checks: factcheck 0 missing; linecheck 4 flagged → 4 scaffolding, 0 lost; validator clean.
Paraphrased lines: none beyond scaffolding.
Noticed, not changed: the EA context says shorter videos (5–12 minutes) perform better for most topics, while §9 says a 15-minute video at 50% completion delivers more algorithm value than a 5-minute one at 80%; both kept. Shorts are described as "under 60 seconds" (a volatile limit); kept as written, with the skill's verify-before-stating decision row applying.

## Batch checks

- `validate_skill_engine.py --json`: no findings for any B10 skill.
- `routecheck.py`: 0 routing sections changed.
- `factcheck.py` (8 skills): 0 missing fact tokens.
- `linecheck.py` THR=0.6: 30 flagged → 29 scaffolding, 1 paraphrased (LinkedIn workflow step 3), 0 lost.
- `measure_skill_scaffolding.py`: gated ratios 0.0–3.3 % (all ≤ 5).
- `pytest -k markdown_links`: passed. `git diff --check` on B10 paths: clean (CRLF notices only).
