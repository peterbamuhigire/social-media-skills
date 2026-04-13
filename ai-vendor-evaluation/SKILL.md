---
name: ai-vendor-evaluation
description: >
  Structured 8-factor vendor evaluation framework for AI marketing tools,
  based on Venkatesan & Lecinski's The AI Marketing Canvas (2nd ed., Stanford
  Business Books, 2026). Scores each tool against EA market accessibility, data
  requirements, integration compatibility, team capability, and total cost in
  UGX, then produces a shortlist with 30-day experiment briefs. Invoke when a
  client has completed the ai-readiness-diagnostic and is at Canvas Step 2
  (Experimentation) and is ready to select specific AI tools for structured
  trials. Also invoke when a client wants to compare 2–4 named tools before
  purchasing or committing budget.
---
# AI Vendor Evaluation

**Framework:** Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*,
2nd ed. Stanford Business Books.

**Position in the Canvas:** Step 2 — Experimentation. Use this skill to select
which tools enter the experiment stage. Use `meta-ai-tools-audit` as the
reference catalogue when the client does not yet have a shortlist. Use
`playbook-ai-automation-workflow` once a tool has been selected and an
automation build is underway.

---

<!-- dual-compat:start -->
## Use when
- Structured 8-factor vendor evaluation framework for AI marketing tools, based on Venkatesan & Lecinski's The AI Marketing Canvas (2nd ed., Stanford Business Books, 2026). Scores each tool against EA market accessibility, data requirements, integration compatibility, team capability, and total cost in UGX, then produces a shortlist with 30-day experiment briefs. Invoke when a client has completed the ai-readiness-diagnostic and is at Canvas Step 2 (Experimentation) and is ready to select specific AI tools for structured trials. Also invoke when a client wants to compare 2–4 named tools before purchasing or committing budget.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for all of the following before generating any output:

1. **Client business name** — exact trading name
2. **Industry** — sector and sub-sector (e.g. retail > fashion, NGO > health)
3. **Country / city** — default is Uganda; note if outside EA
4. **Current Canvas step** — confirm from `ai-readiness-diagnostic` output
5. **Specific marketing problem to solve** — a named task, not "we want AI"
   (e.g. "write 20 Instagram captions per month", "qualify leads from our
   Facebook ads", "send WhatsApp order confirmations automatically")
6. **Tools being evaluated** — names of up to 4 tools the client is
   considering; if the client has no shortlist, prompt them to run
   `meta-ai-tools-audit` first
7. **Current tech stack** — list what the client already uses: CRM, email
   platform, social scheduler, payment platform, website CMS, WhatsApp setup
8. **Monthly tool budget in UGX** — if unknown, ask for a range
9. **Team size and technical level** — number of people who will use the tool
   and their comfort level (non-technical / basic digital skills / comfortable
   with no-code tools / has developer support)

Do not proceed until all nine inputs are confirmed.

---

## Evaluation Framework — 8 Factors

Apply all 8 factors to every tool. Do not produce partial scorecards.
Score each factor 1–5 using the criteria below. Sum to a total out of 40.

---

### Factor 1 — Use Case Fit

Does the tool address the specific, named marketing problem the client stated?

| Score | Criterion |
|-------|-----------|
| 5 | Purpose-built for this exact task; vendor's primary use case matches client's problem |
| 4 | Strong fit; tool does this well even if it does other things too |
| 3 | Adequate fit; the feature exists but is not the tool's core strength |
| 2 | Marginal fit; requires significant configuration to address the use case |
| 1 | Generic/broad; vendor claims the tool "does everything" — lack of focus signals lack of depth |

Red flag: any vendor positioning the tool as an all-in-one AI platform without
a primary specialisation. Record this explicitly in the scorecard.

---

### Factor 2 — Data Requirements

What data does the tool need to function, and does the client have it?

| Score | Criterion |
|-------|-----------|
| 5 | Works entirely with data the client already holds and controls |
| 4 | Requires one additional data source the client can readily obtain |
| 3 | Requires moderate data preparation; client has the data but it is not structured |
| 2 | Requires data the client does not currently have |
| 1 | Requires data the client cannot legally collect |

Flag any data requirement that may conflict with the **Uganda Data Protection
and Privacy Act 2019** (PDPA 2019). In particular: personal data collection,
third-party data sharing, cross-border data transfer, and automated profiling
of individuals. Record the flag in the scorecard even if the score is high.

---

### Factor 3 — Integration Compatibility

Does the tool connect to what the client already uses?

| Score | Criterion |
|-------|-----------|
| 5 | Native connectors to 2+ tools in the client's current stack; no developer work needed |
| 4 | Zapier or Make connector available; straightforward to link to existing tools |
| 3 | API available; requires some technical setup but no full developer resource |
| 2 | Limited integration; one connector available but not for client's key tools |
| 1 | Requires replacing existing tools or a full technical implementation |

For any use case involving WhatsApp or SMS, check for **Africa's Talking**
integration and note the result explicitly. Africa's Talking is the default
recommendation for EA WhatsApp/SMS automation.

---

### Factor 4 — EA Market Accessibility

Can the client actually buy, trial, and use this tool from Uganda or East Africa?

| Score | Criterion |
|-------|-----------|
| 5 | Free tier adequate for Step 2 experimentation; no payment required |
| 4 | Affordable paid tier accessible via USD card, MTN MoMo, or Airtel Money |
| 3 | Paid tool; USD card required; price is reasonable once converted to UGX |
| 2 | Expensive or requires payment method unavailable to most EA clients |
| 1 | No EA payment method accepted and no adequate free tier |

Always convert the pricing to UGX using the current approximate rate and state
it explicitly. Note EAT (UTC+3) customer support availability if known — not a
scoring criterion but record it as context.

---

### Factor 5 — Team Capability Match

Can the client's team use this without specialist skills or paid training?

| Score | Criterion |
|-------|-----------|
| 5 | No-code; self-onboarding in under 1 hour; free tutorials available |
| 4 | Minimal onboarding; free documentation or YouTube training adequate |
| 3 | Some training required; free resources available but take meaningful time |
| 2 | Paid training or certification required for effective use |
| 1 | Requires a data scientist, developer, or specialist to operate |

---

### Factor 6 — Output Quality

Based on trial, demo, or available samples: is the AI output usable for the
client's stated marketing task?

| Score | Criterion |
|-------|-----------|
| 5 | Output usable with minor edits; passes the `ai-content-humaniser` human voice checklist |
| 4 | Output usable after moderate editing; tone and accuracy are sound |
| 3 | Output requires significant editing but the structure and substance are correct |
| 2 | Output is often inaccurate, generic, or off-brand; editing burden is high |
| 1 | Raw output is unusable; would mislead clients or embarrass the business |

Apply the `ai-content-humaniser` standard when evaluating any tool that
generates written content. If a trial is not possible before scoring, note this
as a limitation and flag that output quality must be verified before the Step 2
experiment launches.

---

### Factor 7 — Vendor Stability

Is this a vendor the client can rely on for at least 12 months?

| Score | Criterion |
|-------|-----------|
| 5 | Established company; 2+ years of public operation; active product updates in last 6 months; public roadmap |
| 4 | 1–2 years old; funded; active updates; no public roadmap but product is clearly maintained |
| 3 | Well-known product but recent changes (acquisition, pivot, rebranding) introduce some uncertainty |
| 2 | Early-stage startup; product may change significantly; limited track record |
| 1 | No verifiable track record; tool may not exist in 12 months |

Assess honestly. Do not recommend a tool with a score of 1 or 2 on this factor
unless the client has technical capacity to migrate quickly and the tool cost is
zero.

---

### Factor 8 — Total Cost of Ownership

What is the real monthly cost once the trial period ends?

| Score | Criterion |
|-------|-----------|
| 5 | Transparent pricing under UGX 500,000/month; no per-seat or overage surprises |
| 4 | UGX 500,000–1,000,000/month; pricing is clear; no hidden fees |
| 3 | UGX 1,000,000–2,500,000/month; pricing is clear but stretches most EA budgets |
| 2 | Expensive or opaque; per-seat, per-usage, or overage fees likely to exceed stated price |
| 1 | Very expensive (above UGX 2,500,000/month) or pricing is deliberately obscured |

Always itemise: base plan cost, per-seat fees if any, usage limits and overage
rates, annual vs monthly billing difference, and the total estimated monthly
cost in UGX. Use the client's stated budget as the benchmark.

---

## Scoring and Decision Rules

Sum the 8 factor scores for a total out of 40. Apply the following decision
thresholds:

| Total Score | Decision |
|-------------|----------|
| 32–40 | **Recommended** — proceed to Step 2 experiment |
| 24–31 | **Conditional** — address named gaps before committing; note which factors to re-assess |
| Below 24 | **Deferred** — find a better-fit tool; name the reason and the alternative |

Every deferred tool must include: (a) the primary reason for deferral stated in
one sentence, and (b) a named alternative tool to evaluate in its place.

---

## Output Structure

Produce all five sections below. Do not omit any section.

---

### Section 1 — Tool Evaluation Scorecards

One scorecard per tool. Use this format for each:

```
## [Tool Name]

**Use case being evaluated:** [restate the client's named marketing problem]

| Factor | Score (/5) | Notes |
|--------|-----------|-------|
| 1. Use Case Fit | | |
| 2. Data Requirements | | |
| 3. Integration Compatibility | | |
| 4. EA Market Accessibility | | |
| 5. Team Capability Match | | |
| 6. Output Quality | | |
| 7. Vendor Stability | | |
| 8. Total Cost of Ownership | | |
| **Total** | **/40** | |

**Decision:** Recommended / Conditional / Deferred

**Key strengths:**
- [Point 1]
- [Point 2]

**Key concerns:**
- [Point 1]
- [Point 2]

**PDPA 2019 flag:** [Yes — describe the specific data concern / No]
```

---

### Section 2 — Recommended Shortlist

List all tools scoring 24 or above. For conditional tools, state explicitly
which factor(s) must be addressed and how before the experiment launches.

---

### Section 3 — Deferred Tools

List all tools scoring below 24. For each: one-sentence reason for deferral
and one named alternative tool.

---

### Section 4 — 30-Day Experiment Briefs

Produce one experiment brief for every recommended tool (score 24+). Use this
format:

```
## 30-Day Experiment Brief — [Tool Name]

**Hypothesis:** If we use [tool name] for [specific task], we expect
[measurable result] within 30 days.

**Baseline metric:** [What is the current state before the tool? Give a number
or describe how to establish one in Week 1.]

**Success metric:** [The specific, measurable target at Day 30. Apply SMART
criteria: Specific, Measurable, Achievable, Relevant, Time-bound.]

**Week 1 — Setup and baseline**
- Actions: [what to do]
- Review: [what to check]

**Week 2 — First outputs**
- Actions: [what to do]
- Review: [what to check]

**Week 3 — Iteration**
- Actions: [what to do]
- Review: [what to check]

**Week 4 — Evaluate**
- Actions: [what to do]
- Review: [what to check]

**Day 30 Go/No-Go decision criteria:**
- Go: [specific condition that justifies continuing and paying for the tool]
- No-Go: [specific condition that means the experiment failed; state what happens next]
```

---

### Section 5 — Budget Summary

Produce a single budget table covering all evaluated tools:

```
| Tool | Free Tier Adequate? | Monthly Cost (USD) | Monthly Cost (UGX) | Decision |
|------|--------------------|--------------------|---------------------|----------|
| | | | | |
```

State the USD/UGX conversion rate used.
State the client's declared budget and whether the recommended shortlist is
within budget.
If the shortlist exceeds budget, recommend which single tool to start with and
why.

---

## EA-Specific Evaluation Notes

Apply these rules throughout the evaluation:

- Prioritise tools with free tiers. EA clients at Step 2 should not pay for a
  tool until a 30-day experiment has demonstrated measurable value.
- For any WhatsApp or SMS automation use case, include **Africa's Talking** in
  the evaluation automatically, even if the client did not name it. Note it as
  a recommended addition.
- Flag any tool that requires a developer, API key setup, or command-line
  access unless the client confirmed they have technical support.
- Flag any tool that requires high or consistent bandwidth for field team usage.
  Prefer offline-capable or low-bandwidth modes where field staff are expected
  to use the tool.
- Convert all USD pricing to UGX. Use the approximate rate at time of
  evaluation and state it explicitly.
- Do not recommend any tool that fails the Factor 4 (EA Market Accessibility)
  assessment unless the client has explicitly confirmed they can access it and
  pay for it.

---

## Cross-References

| Skill | When to use it |
|-------|---------------|
| `ai-readiness-diagnostic` | Run before this skill; confirms the client is at Canvas Step 2 |
| `meta-ai-tools-audit` | Reference catalogue; use when client does not have a shortlist yet |
| `ai-content-humaniser` | Apply to evaluate output quality for any content-generation tool |
| `playbook-ai-automation-workflow` | Use after a tool is selected to build the automation workflow |

---

## Tool Categories Reference

Use this section when the client has no shortlist and needs guidance on which category of AI tool to evaluate. Cross-reference with `meta-ai-tools-audit` for the full catalogue.

---

### Category 1: RAG (Retrieval-Augmented Generation) Tools

Tools that connect LLMs to client-specific knowledge bases for accurate, on-brand output:

| Tool | Description | EA accessibility | Approx. cost |
|---|---|---|---|
| Claude Projects | Upload documents; persistent context per project | Yes — browser-based | Included in Claude Pro (~$20/month USD) |
| ChatGPT Projects | Upload documents; persistent context per project | Yes — browser-based | Included in ChatGPT Plus (~$20/month USD) |
| CustomGPT.ai | Build custom knowledge bases with API access | Yes — cloud-based | From $49/month USD |
| Notion AI | RAG within Notion workspace | Yes — cloud-based | From $10/month USD |
| Mem.ai | AI-powered knowledge management | Yes — cloud-based | Free tier available |

**Evaluation criteria:** How easily can client documents be uploaded? Does the tool maintain source attribution? Can multiple team members access the same knowledge base?

---

### Category 2: Synthetic Research and Persona Tools

Tools for generating AI-simulated audience research when primary fieldwork is unavailable or too costly:

| Tool | Description | EA accessibility | Approx. cost |
|---|---|---|---|
| Supernatural AI | Synthetic user personas for brand research | Limited — US-focused | Enterprise pricing |
| Glimpse | AI consumer research and audience analysis | Yes — cloud-based | From $99/month USD |
| Synthetic Users | Simulated user testing and focus groups | Yes — cloud-based | From $29/month USD |
| Claude/ChatGPT (prompted) | Structured persona generation via prompts | Yes | Included in existing subscription |

**EA note:** For most Ugandan SME clients, prompted persona generation via Claude or ChatGPT is the most accessible option. Supernatural AI and Glimpse are better suited to multinational clients with larger research budgets.

---

### Category 3: Agentic AI and Automation Tools

Tools for building autonomous or semi-autonomous marketing agents:

| Tool | Description | EA accessibility | Approx. cost |
|---|---|---|---|
| Persado | AI language optimisation for copy and ads | Limited — enterprise | Enterprise pricing |
| OfferFit | AI experimentation platform for retention campaigns | Limited — enterprise | Enterprise pricing |
| Braze | AI-powered customer engagement platform | Yes — cloud-based | Enterprise pricing |
| n8n | Open-source workflow automation (self-hostable) | Yes — can self-host | Free (self-hosted) |
| Zapier AI | AI-enhanced workflow automation | Yes — cloud-based | Free tier; from $19.99/month USD |
| Make.com | Visual workflow builder with AI steps | Yes — cloud-based | Free tier; from $9/month USD |
| Claude API | Build custom agents and automations | Yes — API access | Pay-per-token |

**EA recommendation:** n8n (self-hosted on a local server) combined with the Claude API is the most cost-effective agentic stack for EA-based consultancies. Zapier is the most accessible for clients with no technical resources.

---

## Quality Criteria

- All 8 factors scored for every tool with written notes — no blank cells,
  no partial scorecards.
- EA accessibility assessed explicitly: name the payment method, name the
  pricing tier, state the UGX equivalent.
- Every recommended tool (score 24+) is paired with a complete 30-day
  experiment brief including a measurable hypothesis and Day 30 Go/No-Go
  criteria.
- Every deferred tool includes a one-sentence reason and a named alternative.
- The Uganda Data Protection and Privacy Act 2019 is flagged wherever the tool
  collects, processes, or transfers personal data — even when the overall score
  is high.
- The budget summary is produced in UGX, references the client's declared
  budget, and resolves conflicts where the shortlist exceeds budget.
- Output is a decision document a non-technical business owner can act on
  without further interpretation.
- Vendor stability is assessed honestly: do not recommend a tool scoring 1 or
  2 on Factor 7 without explicitly noting the risk and the mitigation.

---

## References

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd ed. Stanford Business Books.
- Sweenor, D. and Mulkers, T. (2024) *AI-Powered Business Intelligence*. O'Reilly Media.
- Nayebi, H. (2025) *Generative AI for Product and Marketing Teams*. Packt Publishing.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.
