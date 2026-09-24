---
name: creative-brief-and-big-idea
description: Use when writing or interrogating a strategic creative brief, finding the insight, generating and screening campaign ideas, or running a creative review; use ad-copy-and-hook-lab for line-level ad copy and 13-campaign-brief for the production brief.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Creative Brief and Big Idea

Turn a business problem into a single-minded strategic brief, a tested insight and a platform idea that can run across channels, then screen and review the work against agreed criteria rather than taste.

<!-- dual-compat-start -->
## Use When

- A campaign, launch or brand refresh needs a strategic creative brief before any concept or copy is written.
- A client or team has a brief that produced weak work and needs it interrogated and rewritten.
- Several concepts exist and need a structured screen (effectiveness scale, idea card, responsible-creative check) before a client sees them.
- A creative review meeting, critique session or client presentation of concepts needs a protocol and feedback language.
- The team must decide campaign structure (template-led "triplets" or varied "cousins") and copy–image construction.

## Do Not Use When

- The need is headlines, hooks, primary text or offer wording for a known concept; use `ad-copy-and-hook-lab`.
- The need is the production-ready brief (deliverables, dimensions, owners, dates); use `13-campaign-brief`.
- The need is the overall campaign plan, budget and channel mix; use `09-campaign-strategy` and `advertising-strategy-and-budget`.
- Visual design, art direction execution, typography or layout; hand off to `design-system-skills`.
- Evidence of the audience or business problem is absent and nobody can supply it; return the discovery questions instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business problem, objective and deadline | Client owner or approved brief | Yes | Stop; ask for the problem the brand faces and the result that would count as success. |
| Audience evidence (research, listening, reviews, sales notes, CRM themes) | Client, research agency or `digital-research-engine` wave | Yes for insight work | Mark the insight provisional; run the insight discovery method as a research plan, not a finding. |
| Current positioning and brand voice | `marketing-foundations-stp-positioning`, `04-brand-voice-intake` or client brand book | Conditional | Record the permitted deviation as unknown and ask before concepts go further. |
| Budget (media and production), named decision-maker, review dates | Client owner | Yes before concepts | Draft the brief only; flag the missing commercial and governance fields. |
| Mandatory legal, category or cultural constraints | Client legal, sector regulator notes, `docs/quality-gates/legal-market-release-gate.md` | Conditional | Treat regulated categories (alcohol, betting, health, finance, children, politics) as blocked until checked. |

## Workflow

1. Read the client's brief (or intake) twice and write a one-sentence directive: "The work must persuade [audience] who currently [belief/behaviour] to [action] because [reason]." Stop if the objective or audience cannot be stated.
2. Complete the strategic brief with all core fields (see [brief and insight method](references/brief-and-insight-method.md)) and run the five-question brief test. If it fails, correct the brief before any ideation.
3. Build or validate the insight: a truth about people paired with a truth about the brand. If evidence is thin, withhold the insight label and record a research action.
4. Run the five-stage ideation process with scheduled incubation; produce at least three substantially different ideas, not variations.
5. Write an idea card per concept, including the Lodestar line, press-release test and three channel sketches ([concept screen and critique](references/concept-screen-and-critique.md)).
6. Screen internally: effectiveness scale, idea-quality grid, acceptance questions and responsible-creative interrogation. Kill anything scoring 1–4; send 5 back for a sharper hook; advance 6–7.
7. Decide campaign structure and copy–image construction ([campaign structure and copy–image rules](references/campaign-structure-and-copy-image.md)); hand visual execution to `design-system-skills`.
8. Plan the test pack: message test before execution test; brand-linkage check.
9. Run the review with the critique protocol; record decisions, likely negative reactions and sign-off. If the review drifts to taste or changes the brief, stop and return to the brief; rerun the affected steps.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Strategic creative brief (one page) | Creative team, media planner, client approver | All core fields complete; passes the five-question test; names one decision-maker and review dates. |
| Insight statement with evidence note | Strategist and client | States the human truth, brand truth and the evidence source/date, or is labelled provisional. |
| Idea cards (minimum three distinct ideas) | Internal review, then client | Each has Lodestar line, benefit type, driver, brand role, press-release headline, three channel sketches and likely negative reactions. |
| Concept screen record | Creative director and account lead | Each concept scored with rationale; kill/iterate/advance decision logged. |
| Test pack and review decision log | Client approver, `ad-testing-and-scaling` | Message and execution tests defined; decisions, owners and dates recorded. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Brief test result | Five-question checklist | Every question answered yes with a line of justification, or the brief is returned. |
| Insight evidence note | Table: source, date, sample, confidence | No insight presented as fact without a traceable source. |
| Scoring sheet | Table per concept | Independent scores recorded before discussion; spread greater than 2 flagged. |
| Negative-reaction sign-off | List with approver and date | Signed before any provocative concept is released. |

## Capability and Permission Boundaries

Read and search supplied briefs, research and brand material. Brief writing, ideation, screening and review planning are drafting work. Commissioning production, contacting research participants, publishing or spending media requires explicit client authority. Personal data from listening or interviews must be handled under the client's lawful basis; use themes, not identities.

## Degraded Mode

If audience evidence, brand documents or the decision-maker are unavailable, return the narrowest useful qualified result: a draft brief with gaps, a provisional insight labelled `not assessed`, and a research plan. Never present a hypothesis as a validated insight or an unscored concept as approved.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Brief fails any of the five questions | Rewrite the brief before ideation | Weeks of work against a vague or contradictory brief |
| Only variations of one idea exist | Generate at least two substantially different ideas | Client rejects the core idea and nothing remains |
| Concept scores 1 (harmful) on the effectiveness scale | Kill it regardless of other merits | Reputational or legal damage |
| Idea works in only one channel | Treat it as an execution, not a platform; keep searching | A campaign that cannot scale across the media plan |
| Feedback is taste-based or changes the objective mid-stream | Return to the brief; formal brief revision if the objective really changed | Diluted work and scope creep |
| Liked but not linked (high likeability, weak message playback or brand linkage) | Fix branding and single message, not media weight | Spend on advertising nobody attributes to the brand |
| Regulated category or cultural risk unresolved | Withhold release; route to legal/market gate | Breach of advertising codes or community harm |

## Quality Standards

- One page, plain language, one message; the problem is framed, not the ad ("an ad that solves X", not "make an ad").
- Insight states tension and truth, not a demographic description.
- At least three distinct ideas per round; incubation of at least 48 hours between rounds where the timeline allows (practitioner norm, not a law).
- Every critique line ties to the brief, the business requirement or the audience, with a reason.
- Landa's mnemonics (C.H.O.I.C.E., S.U.I.T.E.S., A.L.T.E.R., L.A.S.T.) are internal checklists only; do not present them to clients as industry standards.
- Apply `anti-ai-slop` to every brief line and idea card.

## Anti-Patterns

- "Target audience: everyone in Uganda." Fix: name one primary segment with mindset and a behaviour, e.g. salaried Kampala women 25–40 managing household budgets on mobile money.
- Presenting three colourways of one layout as "options". Fix: present three different ideas so the client chooses a direction.
- Deciding in the presentation room by consensus. Fix: percolate-then-discuss protocol with one named decision-maker.
- "Make the logo bigger" with no reason. Fix: state the problem (weak brand linkage) and let the specialists solve it.
- Purpose claims with no funded action. Fix: require a multi-year committed action and backlash sign-off, or drop the claim.
- Testing to decide the most novel idea. Fix: test to validate and mitigate; familiar work usually wins tests.
- Casting the brand as the saviour of a community. Fix: the community is the hero; the brand is the guide or helper.

## References

- [Brief and insight method](references/brief-and-insight-method.md) — read when writing or repairing a brief and building the insight.
- [Concept screen and critique](references/concept-screen-and-critique.md) — read before internal screening, client presentation or feedback sessions.
- [Campaign structure and copy–image rules](references/campaign-structure-and-copy-image.md) — read when deciding campaign templates and headline/visual relationships.
- [Ad copy and hook lab](../ad-copy-and-hook-lab/SKILL.md) for line-level copy; [13-campaign-brief](../../pipeline/13-campaign-brief/SKILL.md) for production briefs.
- [Creative review gate](../../../docs/quality-gates/creative-review-gate.md) and [legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md).
- [Direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md).
- [AI cultural bias audit](../../ai-marketing/ai-cultural-bias-audit/SKILL.md) for the responsible-creative check.
<!-- dual-compat-end -->

## Core method in brief

### The brief (Kelley & Sheehan)

Core fields: project scope and problem; business and communication goals; target audience (demographics and mindset, ideally a named archetype); current perceptions; value proposition or positioning; core message (one sentence); timeline. Optional: KPIs, competitors, past learnings. Add from Landa's practitioner interviews: what must be accomplished (not what must be designed), audience misconceptions, pitfalls to avoid, permitted deviation from current positioning, evaluation criteria with weights, named final decision-maker, feedback deadlines, disclosed budget including a separate production-asset line.

Five-question brief test: single-minded? logical (the story flows from it)? contains a compelling insight or brand truth? specific to this brand? commits to a point of view?

Three-sentence strategy story: "The consumer wants [X]. The obstacle is [Y]. This brand can deliver [X] because [reason to believe]."

### The idea

- Insight = truth about people + truth about the brand; fixed insights anchor a brand for years, dynamic insights flex with the audience's situation.
- Lodestar (platform) idea: one sentence of what people should think or feel plus the mechanism; prove flexibility with sketches in three channels; write the press release culture would publish (for East Africa also the one-image-plus-two-lines WhatsApp forward).
- Every unit offers the audience a benefit: social good, utility, information, temptation, entertainment or shareworthiness. Reject "the brand talks about itself".
- Story spine: human driver (safety, status, belonging, convenience…), brand role matching the audience's self-image (guide, guardian, helper, coach…), plot archetype.

### The screen

Seven-point creative effectiveness scale (paraphrased from Landa 2022): 1 destructive; 2 pedestrian; 3 off-brand; 4 not an idea; 5 on-brand but not attention-getting; 6 attention-getting short term; 7 strategically creative (builds the brand, moves behaviour, earns media). Advance only 6–7.

### East Africa adaptation

- Listening sources include WhatsApp groups (consent and ethics), Facebook community groups, radio call-in shows, Ugandan X and Kenyans on X, and offline observation (taxi parks, markets, chama and SACCO meetings, school-fees season).
- Image-driven or emblematic constructions travel across languages and literacy levels; for radio the "image" is sound design.
- Transcreate rather than translate; use in-community reviewers for Luganda, Kiswahili, Runyankore, Luo and other language executions.
- Avoid poverty imagery, tribal humour, colourism and party symbolism in election periods; see the responsible-creative checklist.

### Worked scenario (labelled, not client evidence)

A honey-based energy drink wants women 35+ in Kampala and Nairobi. Directive: persuade busy women who see energy drinks as "chemicals, not for someone like me" to try a natural lift. Insight: they want a sweet lift in the working day but distrust the category. Lodestar: "Nature's energy, made for your afternoon." Channel sketches: breakfast-radio sound piece, WhatsApp Status series, market-stall sampling. Press-release test: "Beekeepers' co-op honey drink wins over office workers who never drank energy drinks." Test pack: two benefit statements to 40 target women by WhatsApp poll (directional, not normed), then execution test on a small paid split.

## Sources

- Landa, R. (2022) *Strategic Creativity: A Business Field Guide to Advertising, Branding, and Design*. Routledge.
- Kelley, L.D. and Sheehan, K.B. (c. 2021–22) *Advertising Management in a Digital Environment: Text and Cases*. Routledge.
- Wallas, G. (1926) *The Art of Thought*; Young, J.W. (1940) *A Technique for Producing Ideas* (via Landa).
