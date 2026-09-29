# AI Vendor Due Diligence

Merged from skills/ai-marketing/ai-vendor-evaluation on 2026-09-29 at 7c60138; preservation map: [ai-vendor-evaluation.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ai-vendor-evaluation.md)

## When to use this reference

Use it when the client already has a shortlist of up to four named AI tools for one specific marketing problem and needs a scored go/no-go decision, plus a 30-day experiment brief for each tool worth trialling. It sits at Step 2 (Experimentation) of the AI Marketing Canvas (Venkatesan and Lecinski, 2026): it decides which tools enter the experiment stage.

- No shortlist yet: build one first from the category catalogue in [ai-tool-fit-access-cost-governance.md](ai-tool-fit-access-cost-governance.md), or from the tool categories at the end of this file.
- Canvas step not confirmed: run [`ai-readiness-diagnostic`](../../../ai-marketing/ai-readiness-diagnostic/SKILL.md) first to confirm the client is at Step 2.
- Tool already selected and an automation build is under way: hand over to [`playbook-marketing-automation`](../../../playbooks/playbook-marketing-automation/SKILL.md).

The deliverable is an evaluation scorecard set and decision document that a non-technical business owner can act on without further interpretation.

## Inputs (all nine required before any output)

1. **Client business name**: exact trading name.
2. **Industry**: sector and sub-sector (for example retail > fashion, NGO > health).
3. **Country / city**: default Uganda; note if outside East Africa.
4. **Current Canvas step**: confirmed from the `ai-readiness-diagnostic` output.
5. **Specific marketing problem to solve**: a named task, not "we want AI". Examples: "write 20 Instagram captions per month", "qualify leads from our Facebook ads", "send WhatsApp order confirmations automatically".
6. **Tools being evaluated**: names of up to four tools the client is considering. If there is no shortlist, build one first (see above).
7. **Current tech stack**: CRM, email platform, social scheduler, payment platform, website CMS, WhatsApp set-up.
8. **Monthly tool budget in UGX**: if unknown, ask for a range.
9. **Team size and technical level**: number of people who will use the tool and their comfort level (non-technical / basic digital skills / comfortable with no-code tools / has developer support).

Do not proceed until all nine inputs are confirmed.

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| Vendor positions the tool as an all-in-one AI platform with no primary specialisation | Score Factor 1 accordingly and record the red flag explicitly in the scorecard. | Buying breadth that lacks depth for the named task. |
| Tool processes, shares, transfers or profiles personal data | Record a PDPA 2019 flag even when the overall score is high. | Silent data-protection exposure under the Uganda Data Protection and Privacy Act 2019. |
| Use case involves WhatsApp or SMS | Add Africa's Talking to the evaluation automatically, even if the client did not name it, and check every tool for Africa's Talking integration. | Missing the default East African WhatsApp/SMS route. |
| Tool fails Factor 4 (EA Market Accessibility) | Do not recommend it unless the client explicitly confirms they can access it and pay for it. | Recommending a tool the client cannot buy. |
| Tool scores 1 or 2 on Factor 7 (Vendor Stability) | Do not recommend unless the client can migrate quickly and the tool cost is zero; if recommended, state the risk and the mitigation. | Lock-in to a vendor that may not exist in 12 months. |
| No trial, demo or sample was possible before scoring Factor 6 | Score provisionally, record the limitation, and require output quality to be verified before the experiment launches. | Treating an unseen output as usable. |
| Tool needs a developer, API key set-up or command-line access | Flag it unless the client confirmed technical support. | Tools that go unused because nobody can operate them. |
| Field staff will use the tool | Flag tools needing high or consistent bandwidth; prefer offline-capable or low-bandwidth modes. | Tools that fail on field connectivity. |

## Procedure

1. Confirm all nine inputs and restate the named marketing problem.
2. Score every tool on all eight factors below (1–5 each, total out of 40). No partial scorecards and no blank notes.
3. Apply the decision thresholds and the decision rules above.
4. Produce the five output sections.
5. Check the result against the checklist at the end.

## The eight factors

### Factor 1: Use case fit

Does the tool address the specific, named marketing problem the client stated?

| Score | Criterion |
|---|---|
| 5 | Purpose-built for this exact task; vendor's primary use case matches the client's problem |
| 4 | Strong fit; the tool does this well even if it does other things too |
| 3 | Adequate fit; the feature exists but is not the tool's core strength |
| 2 | Marginal fit; requires significant configuration to address the use case |
| 1 | Generic or broad; vendor claims the tool "does everything", and lack of focus signals lack of depth |

Red flag: any vendor positioning the tool as an all-in-one AI platform without a primary specialisation. Record it explicitly.

### Factor 2: Data requirements

What data does the tool need to function, and does the client have it?

| Score | Criterion |
|---|---|
| 5 | Works entirely with data the client already holds and controls |
| 4 | Requires one additional data source the client can readily obtain |
| 3 | Requires moderate data preparation; the client has the data but it is not structured |
| 2 | Requires data the client does not currently have |
| 1 | Requires data the client cannot legally collect |

Flag any requirement that may conflict with the Uganda Data Protection and Privacy Act 2019 (PDPA 2019), in particular personal data collection, third-party data sharing, cross-border data transfer and automated profiling of individuals. Record the flag even if the score is high.

### Factor 3: Integration compatibility

Does the tool connect to what the client already uses?

| Score | Criterion |
|---|---|
| 5 | Native connectors to two or more tools in the client's current stack; no developer work needed |
| 4 | Zapier or Make connector available; straightforward to link to existing tools |
| 3 | API available; some technical set-up but no full developer resource |
| 2 | Limited integration; one connector available but not for the client's key tools |
| 1 | Requires replacing existing tools or a full technical implementation |

For any WhatsApp or SMS use case, check for Africa's Talking integration and note the result explicitly. Africa's Talking is the default recommendation for East African WhatsApp/SMS automation.

### Factor 4: EA market accessibility

Can the client actually buy, trial and use this tool from Uganda or East Africa?

| Score | Criterion |
|---|---|
| 5 | Free tier adequate for Step 2 experimentation; no payment required |
| 4 | Affordable paid tier accessible via USD card, MTN MoMo or Airtel Money |
| 3 | Paid tool; USD card required; price is reasonable once converted to UGX |
| 2 | Expensive, or requires a payment method unavailable to most EA clients |
| 1 | No EA payment method accepted and no adequate free tier |

Always convert pricing to UGX at the current approximate rate and state the rate. Record EAT (UTC+3) customer-support availability if known; it is context, not a scoring criterion.

### Factor 5: Team capability match

Can the client's team use this without specialist skills or paid training?

| Score | Criterion |
|---|---|
| 5 | No-code; self-onboarding in under one hour; free tutorials available |
| 4 | Minimal onboarding; free documentation or YouTube training is adequate |
| 3 | Some training required; free resources exist but take meaningful time |
| 2 | Paid training or certification required for effective use |
| 1 | Requires a data scientist, developer or specialist to operate |

### Factor 6: Output quality

Based on trial, demo or available samples, is the AI output usable for the client's stated task?

| Score | Criterion |
|---|---|
| 5 | Usable with minor edits; passes the human-voice checks in [`anti-ai-slop`](../../../ai-marketing/anti-ai-slop/SKILL.md) |
| 4 | Usable after moderate editing; tone and accuracy are sound |
| 3 | Needs significant editing but structure and substance are correct |
| 2 | Often inaccurate, generic or off-brand; editing burden is high |
| 1 | Raw output is unusable; would mislead clients or embarrass the business |

Apply the anti-slop human-voice standard to any tool that generates written content. If no trial is possible before scoring, record the limitation and require output quality to be verified before the Step 2 experiment launches.

### Factor 7: Vendor stability

Is this a vendor the client can rely on for at least 12 months?

| Score | Criterion |
|---|---|
| 5 | Established company; two or more years of public operation; active product updates in the last six months; public roadmap |
| 4 | One to two years old; funded; active updates; no public roadmap but clearly maintained |
| 3 | Well-known product but recent changes (acquisition, pivot, rebranding) introduce some uncertainty |
| 2 | Early-stage start-up; product may change significantly; limited track record |
| 1 | No verifiable track record; tool may not exist in 12 months |

Assess honestly. A score of 1 or 2 blocks a recommendation unless the client can migrate quickly and the tool costs nothing.

### Factor 8: Total cost of ownership

What is the real monthly cost once the trial ends?

| Score | Criterion |
|---|---|
| 5 | Transparent pricing under UGX 500,000/month; no per-seat or overage surprises |
| 4 | UGX 500,000–1,000,000/month; clear pricing; no hidden fees |
| 3 | UGX 1,000,000–2,500,000/month; clear pricing but stretches most EA budgets |
| 2 | Expensive or opaque; per-seat, per-usage or overage fees likely to exceed the stated price |
| 1 | Very expensive (above UGX 2,500,000/month) or pricing deliberately obscured |

Always itemise: base plan cost, per-seat fees, usage limits and overage rates, annual versus monthly billing difference, and total estimated monthly cost in UGX. Benchmark against the client's stated budget.

## Scoring thresholds

| Total (/40) | Decision |
|---|---|
| 32–40 | **Recommended**: proceed to the Step 2 experiment |
| 24–31 | **Conditional**: address named gaps before committing; name the factors to re-assess |
| Below 24 | **Deferred**: find a better-fit tool; name the reason and the alternative |

Every deferred tool carries (a) the primary reason for deferral in one sentence and (b) a named alternative tool to evaluate in its place.

## Output sections (all five required)

### Section 1: Tool evaluation scorecards

One per tool:

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

### Section 2: Recommended shortlist

Every tool scoring 24 or above. For conditional tools, state which factor(s) must be addressed, and how, before the experiment launches.

### Section 3: Deferred tools

Every tool scoring below 24, each with a one-sentence reason and one named alternative.

### Section 4: 30-day experiment briefs

One brief for every tool scoring 24 or above:

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

### Section 5: Budget summary

```
| Tool | Free Tier Adequate? | Monthly Cost (USD) | Monthly Cost (UGX) | Decision |
|------|--------------------|--------------------|---------------------|----------|
| | | | | |
```

State the USD/UGX rate used, the client's declared budget and whether the recommended shortlist fits it. If the shortlist exceeds budget, recommend the single tool to start with and why.

## East African evaluation rules

- Prioritise tools with free tiers. A Step 2 client should not pay for a tool until a 30-day experiment has shown measurable value.
- For WhatsApp or SMS automation, include Africa's Talking automatically and note it as a recommended addition.
- Flag tools needing a developer, API keys or command-line access unless technical support is confirmed.
- Flag tools needing high or consistent bandwidth for field teams; prefer offline-capable or low-bandwidth modes.
- Convert all USD pricing to UGX at the approximate rate on the evaluation date and state the rate.
- Do not recommend a tool that fails Factor 4 unless the client explicitly confirms access and payment.

## Tool categories for building a shortlist

Use these when the client has no shortlist and needs to know which category of AI tool to evaluate. Prices are approximate snapshots; verify before use. The wider function-by-function catalogue is in [ai-tool-fit-access-cost-governance.md](ai-tool-fit-access-cost-governance.md).

### RAG (retrieval-augmented generation) tools

Connect LLMs to client-specific knowledge bases for accurate, on-brand output.

| Tool | Description | EA accessibility | Approx. cost |
|---|---|---|---|
| Claude Projects | Upload documents; persistent context per project | Yes, browser-based | Included in Claude Pro (~USD 20/month) |
| ChatGPT Projects | Upload documents; persistent context per project | Yes, browser-based | Included in ChatGPT Plus (~USD 20/month) |
| CustomGPT.ai | Custom knowledge bases with API access | Yes, cloud-based | From USD 49/month |
| Notion AI | RAG within a Notion workspace | Yes, cloud-based | From USD 10/month |
| Mem.ai | AI-powered knowledge management | Yes, cloud-based | Free tier available |

Evaluation criteria: how easily client documents can be uploaded; whether the tool keeps source attribution; whether several team members can share one knowledge base.

### Synthetic research and persona tools

AI-simulated audience research when primary fieldwork is unavailable or too costly.

| Tool | Description | EA accessibility | Approx. cost |
|---|---|---|---|
| Supernatural AI | Synthetic user personas for brand research | Limited, US-focused | Enterprise pricing |
| Glimpse | AI consumer research and audience analysis | Yes, cloud-based | From USD 99/month |
| Synthetic Users | Simulated user testing and focus groups | Yes, cloud-based | From USD 29/month |
| Claude/ChatGPT (prompted) | Structured persona generation via prompts | Yes | Included in existing subscription |

For most Ugandan SME clients, prompted persona generation in Claude or ChatGPT is the most accessible option. Supernatural AI and Glimpse suit multinational clients with larger research budgets.

### Agentic AI and automation tools

Autonomous or semi-autonomous marketing agents.

| Tool | Description | EA accessibility | Approx. cost |
|---|---|---|---|
| Persado | AI language optimisation for copy and ads | Limited, enterprise | Enterprise pricing |
| OfferFit | AI experimentation platform for retention campaigns | Limited, enterprise | Enterprise pricing |
| Braze | AI-powered customer engagement platform | Yes, cloud-based | Enterprise pricing |
| n8n | Open-source workflow automation (self-hostable) | Yes, can self-host | Free (self-hosted) |
| Zapier AI | AI-enhanced workflow automation | Yes, cloud-based | Free tier; from USD 19.99/month |
| Make.com | Visual workflow builder with AI steps | Yes, cloud-based | Free tier; from USD 9/month |
| Claude API | Build custom agents and automations | Yes, API access | Pay-per-token |

n8n self-hosted on a local server with the Claude API is the most cost-effective agentic stack for EA-based consultancies. Zapier is the most accessible for clients with no technical resources.

## Hand-offs

| Skill or reference | When |
|---|---|
| [`ai-readiness-diagnostic`](../../../ai-marketing/ai-readiness-diagnostic/SKILL.md) | Before this evaluation; confirms Canvas Step 2 |
| [ai-tool-fit-access-cost-governance.md](ai-tool-fit-access-cost-governance.md) | Catalogue for building a shortlist |
| [`anti-ai-slop`](../../../ai-marketing/anti-ai-slop/SKILL.md) | Judging output quality of any content-generation tool |
| [`playbook-marketing-automation`](../../../playbooks/playbook-marketing-automation/SKILL.md) | After selection, to build the automation workflow |

## Acceptance checklist

- [ ] All eight factors scored for every tool with written notes; no blank cells or partial scorecards.
- [ ] EA accessibility explicit: payment method named, pricing tier named, UGX equivalent stated.
- [ ] Every recommended or conditional tool (24+) has a complete 30-day brief with a measurable hypothesis and Day 30 Go/No-Go criteria.
- [ ] Every deferred tool has a one-sentence reason and a named alternative.
- [ ] PDPA 2019 flagged wherever the tool collects, processes or transfers personal data, even when the score is high.
- [ ] Budget summary in UGX, referencing the declared budget and resolving any overrun.
- [ ] Vendor stability assessed honestly; any Factor 7 score of 1 or 2 carries its risk and mitigation.
- [ ] A non-technical owner can act on the document without further interpretation.

## Sources

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd ed. Stanford Business Books.
- Sweenor, D. and Mulkers, T. (2024) *AI-Powered Business Intelligence*. O'Reilly Media.
- Nayebi, H. (2025) *Generative AI for Product and Marketing Teams*. Packt Publishing. (verify: not found in publisher or library catalogues, 29 Sep 2026)
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.
- Chaffey, D. and Ellis-Chadwick, F. (2022) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Harlow: Pearson.
- Uganda Data Protection and Privacy Act 2019.
