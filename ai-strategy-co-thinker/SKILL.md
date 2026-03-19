---
name: ai-strategy-co-thinker
description: >
  Uses AI as a strategic thought partner throughout marketing strategy development — not as a drafting tool, but as a challenger, option generator, and assumption tester. Invoke when developing brand strategy, campaign strategy, or social media strategy, and when the consultant needs to explore options, pressure-test logic, or generate alternatives before making recommendations. Distinct from prompt-engineering-library, which handles co-pilot drafting tasks.
---

# AI Strategy Co-Thinker

Use this skill when the right strategic answer is not yet clear. AI is engaged as a dialogue partner — asking questions, surfacing blind spots, generating competing directions, and stress-testing assumptions. The human consultant selects, refines, and owns all final recommendations.

---

## Required Input

Before beginning, gather the following:

1. **Client business name** — exact trading name
2. **Industry** — sector, sub-sector, and primary revenue model
3. **Country/city** — default: Uganda (specify city if relevant: Kampala, Mbarara, Jinja)
4. **Current strategic challenge or question** — the specific problem the strategy must solve; one or two sentences
5. **Available context documents** — paste or reference: client brief, audit report, audience personas, competitor analysis
6. **Deadline for strategy delivery** — date the final strategy document is due to the client

---

## Co-Pilot vs Co-Thinker

The core distinction from Farri and Rosani (2025):

| Mode | When to use | What AI does |
|---|---|---|
| **Co-Pilot** | You know what you want and need it faster | Drafts, summarises, formats, rewrites |
| **Co-Thinker** | You are not yet sure of the right answer | Challenges assumptions, generates options, maps blind spots |

**This skill is exclusively for Co-Thinker mode.** The consultant does not yet have the answer; AI helps find it through structured dialogue.

For Co-Pilot drafting tasks — writing captions, formatting reports, producing first drafts — use `prompt-engineering-library` instead.

---

## Multi-Step Dialogue Sequence for Brand Strategy

Run this five-step conversation before writing any strategy document. Paste AI responses into a working document as you go; these become the evidence base for the strategy.

**Step 1 — Context brief**

> "Here is the client situation: [paste brief]. Summarise the core marketing challenge in one sentence."

Use the AI's summary to check your own framing. If the AI names a different problem than you expected, explore why before proceeding.

**Step 2 — Stakeholder mapping**

> "Identify the 5 most important stakeholders for this brand's social media success. For each, what do they want, and what do they fear?"

Include internal stakeholders (owner, sales team) and external ones (customers, community, regulators). Fear is as strategically important as desire.

**Step 3 — Pain point table**

> "Create a table of the top 5 unmet customer needs this brand could address through social media. Include: need, current solution, gap, emotional driver."

Review the output against the client brief and audience personas. Strike any row that contradicts known data; annotate rows that align.

**Step 4 — Red flags**

> "What are the 3 most dangerous assumptions in this strategy brief? What would need to be true for each assumption to hold?"

This is the most valuable step. Assumptions that seem obvious are the ones most likely to sink a strategy. Document every flag — even if you decide to proceed, you are doing so with open eyes.

**Step 5 — Strategic options**

> "Suggest 3 distinct strategic directions for [client]. For each: describe the approach, the primary audience it serves, the key risk, and the first action."

Do not skip to this step. The value of the options depends on the quality of the context built in steps 1–4.

---

## MVOSSTE Workflow with AI

Apply the MVOSSTE framework (Randazzo, 2024) at every strategy stage. Use the prompt templates below; document each prompt and its output before moving to the next stage.

| Stage | AI prompt template |
|---|---|
| **Mission** | "Draft 3 mission statement options for [client] in [industry] in Uganda that reflect [values]. Each under 20 words." |
| **Vision** | "Write a 5-year vision for [client] assuming [growth scenario]. Bold but credible." |
| **Objective** | "Generate 5 SMART social media objectives for [goal] over [timeframe]. Include metric and baseline." |
| **Situation** | "Conduct a SWOT analysis for [client] in [industry] in Uganda. Be specific — avoid generic points." |
| **Strategy** | "Suggest 3 social media strategy options for achieving [objective]. For each: approach, target audience, key channel, primary risk." |
| **Tactics** | "List 10 specific content tactics for [strategy] with a UGX [budget] monthly budget. Prioritise by expected impact." |
| **Execution** | "Create a 30-day action plan for [tactic]. Week-by-week milestones with named owner roles." |

Each stage builds on the previous. Do not generate tactics before the strategy stage is agreed. Do not write execution plans before tactics are prioritised.

---

## Job-to-be-Done Framing

Shifts the brief from "what should we post?" to "what job is our audience hiring this content to do?" (Randazzo, 2024).

**Prompt:**

> "Using the Jobs-to-be-Done framework, what job is [client's target audience] in Uganda hiring social media content to do for them? List 3 functional jobs, 3 emotional jobs, and 3 social jobs."

Once the AI returns a list, audit the existing content strategy against it:

- Which jobs does the current content serve?
- Which jobs are unserved or underserved?
- Is there a mismatch between the content the brand is producing and the job the audience needs done?

Use this audit to justify content pivots or new content pillars in the strategy document.

---

## Campaign Risk Mapping

Use AI to identify and stress-test assumptions before any campaign launches (Farri and Rosani, 2025). Run in three steps:

**Step 1 — Assumption inventory**

> "List all the assumptions embedded in this campaign plan. Be exhaustive."

Do not filter at this stage. Include obvious assumptions alongside hidden ones.

**Step 2 — Criticality ranking**

> "Rank these assumptions from most to least critical. Which, if wrong, would cause the campaign to fail?"

Focus on the top three. A campaign can tolerate minor assumption failures; it cannot survive critical ones.

**Step 3 — Validation method**

> "For the top 3 critical assumptions, suggest the cheapest way to validate or invalidate each before the campaign launches."

Validation methods might include: a soft-launch post to test audience response, a WhatsApp poll to a sample of existing customers, a one-week pilot with a reduced budget. Include the validation plan in the campaign brief so the client knows the strategy has been tested before full deployment.

---

## Prompt Footnoting Practice

Professional standard for AI-assisted strategy work (Randazzo, 2024). Every AI-generated output used in a client document must be cited.

**Format:**

> *Generated using Claude, prompt: "[exact prompt text]", [date].*

Add this footnote directly below any table, list, or paragraph drawn from an AI output. This practice:

- Enables clients to audit, reproduce, or modify outputs independently
- Protects the consultant if outputs are later questioned or found to be inaccurate
- Creates a record of the strategy's development process — useful for retrospectives and case studies
- Demonstrates professional rigour to sophisticated clients

Never omit the footnote to make a deliverable look cleaner. If a client asks where an insight came from, the answer must always be available.

---

## Quality Gate

AI generates options; the human consultant selects, refines, and takes responsibility. The following rules are non-negotiable:

- **No direct delivery** — never present AI-generated strategic options directly to a client without human editorial review. Every AI output must pass through the consultant's judgement before it reaches a client.
- **Add market knowledge** — layer in local market knowledge, client relationship context, and professional experience that AI does not have access to. A strategy that could have been written without knowing the client is not a strategy; it is a template.
- **Flag unverifiables** — if an AI output makes a claim that cannot be verified against a source, a known data point, or direct client knowledge, flag it before including it in a deliverable. Do not include unverifiable claims in client documents.
- **Own the recommendation** — the strategy document is signed by the consultant, not by the AI. The consultant is responsible for every recommendation, regardless of which tool was used to generate it.

---

## Quality Criteria

- Multi-step dialogue sequence (all 5 steps) completed before any strategic recommendation is drafted
- MVOSSTE workflow applied with AI at each stage — all prompts documented with outputs
- Job-to-be-Done framing applied to at least one strategic question in the brief
- Campaign risk mapping completed — top 3 critical assumptions identified and a validation method assigned to each
- All AI-generated outputs reviewed and edited by the human consultant before any content reaches the client
- Prompt footnoting applied throughout the strategy document — every AI output cited with exact prompt and date
- Final strategy document reflects the consultant's professional judgement, not a compiled set of AI outputs

---

## References

- Erné, J. (2024) *The Artificial Intelligence Handbook for Management Consultants*.
- Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*. Harvard Business Review Press.
- Randazzo, G.W. (2024) *Winning Marketing Strategies Using Generative AI*. Business Expert Press.
