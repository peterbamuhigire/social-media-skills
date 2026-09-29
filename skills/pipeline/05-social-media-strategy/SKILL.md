---
name: 05-social-media-strategy
description: 'Use when intake and the audit are complete and the client needs one overarching plan for its social channels: which platforms and why, goals, pillars, posting mix, community and KPIs; produces the board-ready social strategy and implementation priorities; not for a plan spanning email, search, web and paid (use `06-digital-marketing-strategy`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Media Strategy Generator

Produces the master social media strategy document, the primary deliverable for a strategy engagement, with every section populated with client-specific content and no generic filler. Apply British English throughout and default to Uganda/East Africa context unless the client specifies otherwise.

<!-- dual-compat-start -->
## Use When

- The brief, audit, personas and voice are approved and the client wants one strategy document for its social channels.
- The board or MD wants to know which platforms to prioritise (Instagram, TikTok, Facebook, LinkedIn or X), why, and what targets and success look like in numbers for the social team.
- The plan needs posting frequency and content mix by platform, a community approach and a test-and-learn rhythm.
- The client's social presence must also hold up in AI search and answer engines, with trust and participation built into the plan.

## Do Not Use When

- `06-digital-marketing-strategy` when email, search, website, influencer and paid channels must sit in one integrated plan.
- `strategy-channel-architecture` for platform roles and audience flow between channels only.
- `09-campaign-strategy` for one launch or promotion rather than the ongoing programme.
- Stop before committing budget or promising follower or sales targets without baseline data; state the assumption and the baseline needed.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name, industry and sub-sector, country/city, primary 12-month business goal | `01-client-brief` or client | Yes | Ask; country/city defaults to Kampala, Uganda. |
| Current platform performance and competitor data | `02-platform-audit` output | Yes | Note the gap explicitly, generate the section with stated assumptions, and leave KPI baselines `not assessed`. |
| The 2–3 primary personas | `03-audience-personas` output | Yes | Note the gap and state persona assumptions; the Validated User Research tenet then fails the readiness gate. |
| Brand voice summary | `04-brand-voice-intake` output | If available | Draft the voice summary from the brief's three adjectives and label it provisional. |
| Budget band for paid social: none / low (under UGX 500K/month) / medium (UGX 500K–2M/month) / high (above UGX 2M/month) | Client | Yes | Plan organic-only and flag the budget question. |
| Website ownership and URL | Client | Yes | Omit Section 3b and record that website ownership was not confirmed. |

## Workflow

1. Collect the inputs; if any onboarding document is unavailable, note this explicitly and generate the relevant section with stated assumptions.
2. Run the strategy readiness gate below; if any tenet is missing, stop and return to the upstream stage before producing strategy.
3. Apply the Kennedy and Wiebe direct-response filter: market (who exactly is the strategy for?), message (what pain, desire or differentiated promise should the audience hear repeatedly?), media (which channels fit that audience and message?), offer (what is the next step promoted at each stage?). Do not build platform plans before those four are explicit.
4. Write all ten sections in order with markdown headings (situation analysis, strategy statement, platform selection with POEM (Paid/Owned/Earned), brand voice, content pillars, posting frequency, community management, paid social, KPI framework on RACE (Reach/Act/Convert/Engage), 90-day roadmap), plus Section 3b when the client owns a website; see [strategy-document-sections](references/strategy-document-sections.md).
5. Add an audience-affordance card for every priority platform (participation and trust lens below).
6. Test the content plan with the ARM lens (Attract, Retain, Motivate) and the 10-4-1 rule; correct any plan heavy on M without A or R, or with promotion above 10–15 %, and rerun the pillar percentages and posting table.
7. For AI-search-aware strategy, load the [AI search and social discovery rules (LinkedIn citation section)](../../ai-marketing/ai-generative-search-optimisation/references/ai-search-and-social-discovery-rules.md) and preserve its sample, denominator, date and attribution limits in the strategy's evidence register.
8. Run the anti-slop ship gate and hand the strategy on: for each proposed content unit, hand the audience job and strategic outcome to [`13-campaign-brief`](../13-campaign-brief/SKILL.md), which owns the reader-first production, evidence, rights and destination record; full campaign planning goes to `09-campaign-strategy`.

## Strategy readiness gate (four evidence areas, after Levy, 2015, UX Strategy, O'Reilly)

Canonical reference: `docs/ux-foundations.md` Section 2. Before producing the master strategy document, verify upstream artifacts contain evidence for all four tenets:

| Tenet | Where to verify | Pass criterion |
|---|---|---|
| **Business Strategy** | `01-client-brief` | Value proposition declared; revenue stream identified |
| **Value Innovation** | `02-platform-audit` | Differentiation vs competitors named with specifics |
| **Validated User Research** | `03-audience-personas` (including synthetic persona hypotheses) | Personas cite real data sources, not pure hypothesis |
| **Killer UX Design** | `04-brand-voice-intake` + content pillars | Voice and pillars actually distinct from category baseline |

Apply Four Tenets first as a gate (does this strategy belong in market at all?); apply Kennedy/Wiebe second as a structure (what is the operational shape of the next campaign?). Both run; neither replaces the other.

## Participation and trust lens

For every priority platform, add a short audience-affordance card before recommending content or effort. Record the audience motive (consume, control, connect, compete or create), the platform's useful affordance, the participation job (identity, conversation, sharing, presence, relationships, reputation or groups), the public/private boundary, the intended action, and one trust or attention guardrail. Do not infer motive from age alone; use the supplied persona, listening or pilot evidence.

The strategy must show the route from public discovery to the approved conversion hub, retention and honest advocacy. Do not optimise for outrage, humiliation, compulsive use or engagement without business context. See [`social-operating-system-and-pragmatics`](../06-digital-marketing-strategy/references/social-operating-system-and-pragmatics.md) for the reusable card and conversation controls.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Master social media strategy document (ten sections, plus 3b where a website exists) | Client board; `09-campaign-strategy`; `10-content-pillars`; `11-content-calendar` | Every section populated with client-specific content; no section omitted. |
| RACE KPI table with baselines and 90-day targets | Client lead; reporting skills | Baselines drawn from `02-platform-audit`; targets SMART; inapplicable rows removed. |
| 90-day milestone roadmap | Account team | Three months, each with a theme, 4–6 specific actions and a milestone. |
| Audience-affordance cards per priority platform | `13-campaign-brief`; content team | Motive, affordance, participation job, boundary, action and guardrail recorded from evidence. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Readiness gate record | Four-tenet table with pass or fail and source | Every tenet passes, or the strategy is withheld and the upstream stage named. |
| Strategy evidence register | Table: claim, source, date, sample and denominator | AI-search and benchmark claims keep their sample, denominator, date and attribution limits; assumptions for missing onboarding documents are stated. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Paid social guidance sets guardrails only; boosting or campaign spend needs separate client approval.

## Degraded Mode

Without the upstream brief, audit and persona outputs, return the narrowest qualified result and mark the affected checks `not assessed`. A readiness gate record naming the missing tenets, the direct-response filter answers and a provisional platform rationale can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A readiness tenet is missing | Return to the upstream stage before producing strategy; do not paper over a missing tenet with a stronger headline. | A strategy that fails downstream. |
| Choosing platforms | Apply EA defaults: Facebook for broad reach, Instagram for urban 18–35 aspirational content, TikTok for under-30 entertainment, WhatsApp for direct customer communication, LinkedIn for B2B or professional services, YouTube for long-form tutorials or brand storytelling; mark each Primary, Secondary or Exit with a POEM class. | Platform choices with no persona or goal link. |
| Setting posting times | Use EAT (UTC+3) peaks: 07:00–09:00, 12:00–13:00, 19:00–21:00; Facebook tends to peak earlier, Instagram and TikTok in evenings. | Posting when the audience is offline. |
| Budget band is none / low / medium / high | None: organic-only, noting Facebook organic reach is typically 2–5% without paid support. Low: selective boosting of 2–3 posts/month. Medium: monthly always-on boosting plus 1 structured campaign per quarter. High: always-on paid social plus multiple flights; recommend `09-campaign-strategy`. | Paid guidance detached from the client's budget. |
| A spend decision is proposed | Tie it to one system role: attract new qualified attention, convert warm traffic, retain customers, or reactivate dormant leads or past buyers. | Random visibility spend. |
| The content plan is heavy on one ARM letter | Rebalance: M without A or R shrinks the audience; A without M grows an audience that never converts (Hahn, 2003). | An unbalanced plan. |
| High-intent comments, poll replies or DMs arrive | Feed them to a follow-up path, not left in-platform. | Engagement that never becomes an identifiable opportunity. |
| Email, search, website, influencer and paid channels must sit in one integrated plan | Route to `06-digital-marketing-strategy` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- Strategy statement clearly links the social media approach to the client's primary business goal and names the primary personas (Kotler et al., 2023, on digital brand positioning where relevant).
- Platform selection rationale explicitly applies the POEM model and justifies deprioritisation decisions.
- Content pillars honour the 10-4-1 rule (Bodnar and Cohen, 2012) in aggregate percentage allocations; pillars total 100% and serve attraction, conversion, retention and referral.
- KPI table is populated with baselines drawn from 02-platform-audit and targets that are SMART.
- RACE framework (Chaffey and Ellis-Chadwick, 2022) is applied correctly across the four KPI stages.
- Community management principles include specific SLA timeframes, not vague commitments.
- British English spelling throughout; EAT timezone applied to all scheduling references.
- Paid social guidance is calibrated to the client's stated budget band.

Three further checks (client-specific situation analysis, named roadmap actions, Section 3b for website owners) are in the [strategy-document-sections](references/strategy-document-sections.md) checklist.

## Anti-Patterns

- Generic situation analysis that could apply to any brand. Fix: cite the client's audit figures, named competitors and personas.
- Building platform plans before market, message, media and offer are explicit. Fix: run the Kennedy/Wiebe filter first.
- Vague community commitments ("respond promptly"). Fix: set SLAs such as comments within 4 business hours, DMs within 24 hours, complaints within 2 hours.
- Abstract roadmap phases ("optimise"). Fix: 4–6 specific, named actions and a Day 30, 60 or 90 milestone per month.
- A website-owning client with no blog plan. Fix: include Section 3b with cadence, the four-asset recycling plan and the Monday-to-Friday distribution window.
- Planning full crisis response or a full campaign here. Fix: route crisis planning to `playbook-crisis-communications` and campaigns to `09-campaign-strategy`.

## References

- [Strategy document sections](references/strategy-document-sections.md): read when collecting inputs, writing any of the ten sections or Section 3b, applying the ARM lens, or checking the overflow quality items.
- [`social-operating-system-and-pragmatics`](../06-digital-marketing-strategy/references/social-operating-system-and-pragmatics.md): read when building the audience-affordance cards and conversation controls.
- [AI search and social discovery rules](../../ai-marketing/ai-generative-search-optimisation/references/ai-search-and-social-discovery-rules.md): read when the strategy must be AI-search-aware.
- [Reader-first content brief](../13-campaign-brief/references/reader-first-content-brief.md): read when handing content units to `13-campaign-brief`.
- [`06-digital-marketing-strategy`](../06-digital-marketing-strategy/SKILL.md): read when the plan must integrate channels beyond social.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->
