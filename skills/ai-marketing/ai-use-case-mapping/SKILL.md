---
name: ai-use-case-mapping
description: Use when a client asks where AI can help their marketing, wants AI tied to revenue, needs social forecasts or wants AI as a strategy thinking partner; produces a prioritised AI use-case map with a 90-day sequence, an AI growth system design and a predictive analytics plan; not for scoring AI readiness or data (use `ai-readiness-diagnostic`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Use Case Mapping

Maps a client's marketing activities onto the 2×2 AI Use Case Framework (Venkatesan and Lecinski, 2026) and turns a vague sense that "AI could help" into a scored, prioritised shortlist the marketing manager can start within 90 days.

<!-- dual-compat-start -->
## Use When
- Our team knows AI could help but not where; list our marketing tasks and rank which ones AI should take first in the next 90 days.
- Design an AI growth system that links content, lead scoring and a WhatsApp service copilot to revenue and retention, with governance and hard rules.
- Forecast which posts will perform, predict follower churn and build RFM segments from our Meta Business Suite exports.
- Use AI as a strategy co-thinker rather than a co-pilot: stakeholder and red-flag dialogue, MVOSSTE prompts, jobs-to-be-done framing and campaign risk mapping.

## Do Not Use When
- `ai-readiness-diagnostic` for a scored readiness, data foundation or AI Marketing Canvas assessment.
- `playbook-marketing-automation` for building the automations and agent workflows.
- `meta-tools-stack-evaluation` for choosing between AI tools and vendors.
- Stop before promising forecast accuracy or revenue gains, or using customer data without consent; label every estimate and assumption.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry and sub-sector, country/city and the single primary marketing goal for the next 6 months | Client or approved brief | Yes | Ask before generating; default the location to Uganda/Kampala only when it is not stated. |
| Current marketing activities (every recurring task) | Client marketing lead | Yes | Apply the standard 12-activity starter list and remove tasks the client does not perform. |
| Current AI tools in use, even informal (ChatGPT for captions, Canva Magic Write) | Client team | Yes | Record as zero and score Current AI Use 0 for every activity. |
| Team size and technical comfort (Low / Medium / High) | Client | Yes | Assume Low and keep every use case free of developer, API or data-science skills. |
| Social data exports (Meta Business Suite) and CRM volume | Client | Conditional (forecasting or segmentation) | Mark predictive use cases deferred; fewer than 3 months of data never supports a forecast. |

## Workflow

1. Confirm the goal, market and approval boundary; route to `ai-readiness-diagnostic` if the client first needs a scored maturity or data assessment.
2. Establish the activity list (client list or the 12-activity starter list) and map each activity to a quadrant, one row per quadrant opportunity, using the [mapping method](references/use-case-mapping-method.md).
3. Score each activity for Current AI Use (0–2) and Opportunity (1–5) and assign priority with the rules below.
4. Build the priority matrix and the quadrant summaries; if a quadrant is empty, add at least one standard example activity and mark it as a suggested addition.
5. Select the Top 5 High-priority use cases and 3 to defer, each deferral with a reason and a revisit trigger; stop any use case that needs customer data without consent or promises forecast accuracy or revenue.
6. Sequence the Top 5 into the 90-day plan (Q1 first, then Q2, then Q3/Q4) with a named owner and success metric per phase.
7. Where the brief asks for it, extend into a growth system, a predictive analytics plan or a co-thinking session with the linked references.
8. Check the map against the Quality Standards; correct any rating not derived from the formula or any tool without a cost indication, rerun the check, then run the `anti-ai-slop` ship gate before delivery; a blocking factual, cultural, safety or permission defect stops release.

## Priority scoring

- **Current AI Use (0–2):** 0 = no AI in use; 1 = partial (occasional ChatGPT, one automated step); 2 = full, systematic integration.
- **Opportunity Score (1–5):** the mean of Volume, Repetition, Data availability and Time cost (each 1–5; time cost 1 = under 30 minutes, 5 = over 5 hours a week), rounded.
- **Priority:** High = Opportunity 4–5 AND Current AI Use 0; Medium = Opportunity 3–4 OR Current AI Use 1; Low = Opportunity 1–2 OR Current AI Use 2.
- **Quick win threshold:** achievable within 4 weeks with free or low-cost tools under UGX 100,000/month; flag anything above it.
- **ROI on AI tool investment:** (TLV − COCA) ÷ COCA (Bodnar and Cohen, 2012).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Priority matrix (Activity, Quadrant, Current AI Use, Opportunity Score, Priority) with quadrant summaries | Client marketing manager | All four quadrants populated; every rating traces to the scoring formula. |
| Top 5 use cases and 3 deferred use cases | Client marketing manager | Each Top 5 entry has why now, what to do, named EA-accessible tool with cost, 4-week metric and effort; each deferral has a reason and revisit trigger. |
| 90-day implementation sequence | Client lead and `playbook-marketing-automation` | Each 30-day phase names an owner and a success metric. |
| Growth system design, predictive analytics plan or co-thinking record (when requested) | Strategist | Built from the linked reference, with estimates and assumptions labelled. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Scoring sheet | Table: activity, four opportunity factors, mean, current use, priority | Priorities reconcile with the formula. |
| Tool and cost register | Table: tool, tier, cost in UGX or USD, payment route, source date | Every tool has a free tier or a Visa, Mastercard or MTN Mobile Money via Payoneer route and a cost indication. |
| Assumption and deferral log | List | Every estimate, data gap and deferral trigger is labelled. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Building the automations belongs to `playbook-marketing-automation` after approval.

## Degraded Mode

Without a confirmed activity list and current AI tool inventory, return the narrowest qualified result and mark the affected checks `not assessed`. A starter-list matrix with provisional scores and the East African default opportunities can still be delivered, labelled provisional.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| An activity spans two quadrants | Create a row per quadrant opportunity; for the headline assignment use the quadrant with the highest-value AI opportunity. | Hiding a customer-facing risk inside an internal use case. |
| A Top 5 use case needs a paid tool above UGX 100,000/month | Flag it clearly and justify it, or defer it. | Quick wins the client cannot afford. |
| A use case faces customers (Q2) | Activate only after the Q1 foundations are in place, in Days 31–60. For every use case, choose the lowest viable automation level that data readiness, AI maturity and risk support, and define its human approval gate. | Customer-facing AI launched before the team can run it. |
| AI drafts responses in Luganda or Swahili | Require human review of every AI-generated local-language response before publishing. | Mistranslation and lost audience trust. |
| Local quantitative data is scarce | Synthesise qualitative signals, flag the scarcity and never present AI-synthesised insight as equal to primary research. | False market certainty. |
| Chosen use cases must work together as a growth system tied to revenue, retention or conversion | Apply the growth principle, pattern table and hard rules in [ai-growth-systems-design](references/ai-growth-systems-design.md). | AI that produces more content without moving a funnel metric. |
| The client wants forecasts (churn, content performance, campaign revenue, segments) from social data | Run the analytics-stage check, use-case match, RFM and predictive calendar in [predictive-analytics-use-cases](references/predictive-analytics-use-cases.md). | Predictions from under 3 months of data or tools beyond the client's budget. |
| The strategic answer is not yet clear before mapping or recommending | Use the Co-Thinker dialogue, MVOSSTE, JTBD and risk-mapping prompts in [ai-strategy-co-thinking-prompts](references/ai-strategy-co-thinking-prompts.md). | Delivering unreviewed AI strategy options as the consultant's recommendation. |

## Quality Standards

- All four quadrants are populated; where the client's list misses one, at least one suggested activity is added and marked as such.
- Every High, Medium and Low rating is derived from the Opportunity Score formula, not intuition or assumption.
- All Top 5 use cases are achievable within 4 weeks with free or sub-UGX 100,000/month tools; any exception is flagged and justified.
- East African context runs throughout: WhatsApp as the primary customer channel, Africa's Talking for SMS/WhatsApp API use, Mobile Money as a payment and communications touchpoint, and local data scarcity acknowledged.
- Every deferred item has a clear reason and a time- or milestone-bound revisit trigger.
- Every tool is named and EA-accessible: a free tier or payable via Visa, Mastercard or MTN Mobile Money via Payoneer, with a cost indication.
- The output is actionable by a non-technical marketing manager; no developer skills, API access or data-science knowledge is assumed unless the team profile supports it.
- The 90-day sequence names a responsible person and a success metric for every phase.

## Anti-Patterns

- Rating priority by gut feel. Fix: compute the four-factor Opportunity Score and apply the priority rules.
- Leaving a quadrant empty because the client did not list it. Fix: add a standard example activity and mark it as a suggested addition.
- Starting with a customer-facing chatbot. Fix: begin with Q1 internal quick wins and activate Q2 once they are embedded.
- Dismissing a high-opportunity use case without explanation. Fix: record the deferral reason and the milestone for revisiting it (for example when CRM data reaches 1,000+ contacts).
- Promising forecast accuracy or revenue gains. Fix: label every estimate and assumption and state the data period behind it.
- Publishing AI-drafted Luganda or Swahili replies unchecked. Fix: route each through a native-speaker review before it goes out.

## References

- [Use-case mapping method](references/use-case-mapping-method.md): read when building the activity list, assigning quadrants, scoring, writing the Top 5 and deferrals, sequencing the 90 days or applying the East African default opportunities.
- [ai-growth-systems-design](references/ai-growth-systems-design.md): read when the use-case map must become an AI growth system with patterns, data foundation, governance and a 30/60/90-day roadmap.
- [predictive-analytics-use-cases](references/predictive-analytics-use-cases.md): read when a client needs social media forecasts, RFM segmentation or a predictive content calendar.
- [ai-strategy-co-thinking-prompts](references/ai-strategy-co-thinking-prompts.md): read when AI should act as a strategy co-thinker (dialogue sequence, MVOSSTE, JTBD, campaign risk mapping, prompt footnoting).
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md): read when maturity or data readiness is unknown.
- [prompt-engineering-library](../../content-writing/prompt-engineering-library/SKILL.md): read when activating Q1 quick wins with client-specific prompts.
- [playbook-marketing-automation](../../playbooks/playbook-marketing-automation/SKILL.md): read when approved Q2 use cases need workflow automation.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
- [Anti-AI slop production gate](../anti-ai-slop/SKILL.md): read when writing use-case descriptions and the 90-day plan.
<!-- dual-compat-end -->
