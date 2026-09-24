---
name: ad-to-site-journey-handoff
description: Use when an ad, email or social campaign sends people to a website or landing page and the landing-page brief, message match, UTM and conversion-event definitions, consent and ownership must be handed to website-skills; use playbook-post-click-strategy for link-in-bio and WhatsApp flows.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Ad-to-Site Journey Handoff

Define the contract between a marketing campaign and the website that receives its traffic: what the landing page must say and do, how every click is tagged and every conversion counted, who owns each piece, and when the journey is ready to go live. This engine writes the brief and the measurement definitions; website-skills builds the page.

<!-- dual-compat-start -->
## Use When

- A paid, email or organic campaign will send traffic to a landing page or website section.
- A client asks "why do our ads get clicks but no enquiries?" and the destination is suspect.
- A new landing page, offer page or lead-magnet page must be briefed to a web team or to website-skills.
- UTM conventions, conversion events or consent handling need defining before launch.
- Ownership of copy, build, tags, QA, go-live and reporting between agency, client and developer is unclear.

## Do Not Use When

- Traffic goes to Instagram/TikTok link-in-bio, WhatsApp chat or DMs without a web page; use `playbook-post-click-strategy`.
- The deliverable is page build, code, performance engineering or design; hand off to website-skills and design-system-skills.
- The need is a full website content plan; use `12-website-content-plan`.
- The need is UTM governance across all campaigns; use `meta-utm-tracking` (this skill applies it to one journey).

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Campaign brief and ads (or copy deck) | `creative-brief-and-big-idea`, `ad-copy-and-hook-lab` | Yes | Stop; message match cannot be specified without the ads. |
| Offer facts, price, terms and proof with consent | Client commercial owner | Yes | Brief the page with placeholders marked `not assessed`; do not invent proof. |
| Conversion definition and value | `advertising-attribution-and-measurement`, client | Yes | Stop; a page without a defined conversion cannot be measured. |
| Current site, CMS, tag manager and analytics status | Client web owner, website-skills | Yes | Record as unknown; include a discovery task in the handoff. |
| Market and consent scope (EEA/UK/CH visitors? Uganda/Kenya data processing?) | Client, data-protection owner | Conditional | Block tag and form go-live until consent handling is confirmed. |
| Named owners on client, agency and developer sides | Client and agency leads | Yes | Deliver the RACI with gaps highlighted; go-live is withheld until filled. |

## Workflow

1. Confirm the journey: source ads, audience temperature, the single action, the conversion event and its value; stop if the action or event is undefined.
2. Write the landing-page brief ([landing-page brief template](references/landing-page-brief-template.md)): one page, one job; headline echoing the ad; offer; proof above the fold; objection answers; form or WhatsApp friction; mobile and speed acceptance checks.
3. Run the destination-UX heuristics ([destination UX heuristics](references/destination-ux-heuristics.md)) on the brief or the existing page; list defects and their fixes.
4. Define measurement ([measurement and ownership spec](references/measurement-and-ownership-spec.md)): UTM values per ad, conversion events, thank-you or confirmation state, offline or WhatsApp conversions, consent handling.
5. Fill the RACI for copy, design, build, tags, QA, go-live, monitoring and reporting.
6. Run the go/no-go gate: brand-slice audit, message match, tracking QA, consent, speed and accessibility checks owned by the web team. Withhold launch on any blocking failure; correct and rerun the gate.
7. Hand over the package to website-skills (resolve its location via the global engine routing table) and record acceptance; after launch, review funnel data and hand back fixes on the agreed cadence.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Landing-page brief | Website team / website-skills, designer | Every field complete; headline and offer match the ads; one primary action |
| Measurement spec | Tag owner, analyst | UTM table, event list with triggers, conversion values and consent rules defined |
| Journey RACI | Client, agency, developer | Every task has one accountable owner and a date |
| Go/no-go record | Client approver | All blocking checks pass or launch is withheld with reasons |
| Destination UX findings | Web team, strategist | Each defect has evidence, fix and owner |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Message-match table | Ad line vs page element | Every ad promise appears on the page above the fold |
| Tracking QA log | Event, test action, result, date | Each conversion fires once per real action |
| Consent check | Checklist with owner and date | Consent mechanism confirmed for in-scope jurisdictions |
| Handoff acceptance | Signed or recorded acceptance by website owner | Package accepted before build starts |

## Capability and Permission Boundaries

Read and search ads, pages and analytics exports. Writing briefs, specs and audits is drafting and read-only with respect to live systems. Editing websites, installing tags, changing consent tools, publishing pages or launching traffic requires explicit authority from the client and the website owner. Form data collection must follow the client's lawful basis and privacy notice.

## Degraded Mode

If the site, analytics or owners are unavailable, return the narrowest useful qualified package: the brief and measurement spec with unassessed checks marked `not assessed`, plus a discovery list. Never mark tracking or consent as working without a test record.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Ads point to the home page | Brief a dedicated landing page per message or offer | Visitors hunting for the promise and leaving |
| Page headline does not echo the ad | Rewrite the page headline to match | Mismatch that raises bounce and cost per result |
| Proof sits below the fold or on another page | Move specific, consented proof near the top | Doubt created by the promise is never answered |
| Form has fields the sales process does not use | Remove them; add one qualifying question only if sales capacity is the bottleneck | Needless friction and data over-collection |
| Tracking or consent QA fails | Withhold paid traffic | Unmeasured spend and compliance exposure |
| Owner for a task is missing | Withhold go-live until named | Launch-day gaps and blame |
| Web team rejects a brief item as infeasible | Record the trade-off and agree an alternative with the client | Silent scope changes |

## Quality Standards

- One page, one job, one primary call to action; secondary routes (call, WhatsApp) support the same job.
- The page restates the ad's promise in its first view and proves it.
- Contact routes visible where buyers expect to speak to a person (in East Africa a WhatsApp click-to-chat plus a dialable number, with a response-time promise).
- Performance and accessibility acceptance targets are stated for the web team to own: Core Web Vitals LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 at the 75th percentile of field data (CW-01); WCAG 2.2 AA as the accessibility target (CW-05); stress-test at the WebPageTest "3G" profile as a worst case (CW-04). Checked 2026-09-23.
- Measurement definitions are written before build, not after.

## Anti-Patterns

- Sending paid traffic to a page that says something different from the ad. Fix: message-match table signed off before launch.
- "We'll add tracking later." Fix: tracking QA is a go/no-go item.
- Hiding the phone or WhatsApp number to push forms. Fix: show human contact; callers are high-intent.
- Stock-photo trust. Fix: real team, real premises, consented client proof.
- Brand-slice gaps (great ads, text-wall site, unanswered phone). Fix: brand-slice audit before spend.
- Treating the landing page as the website team's problem alone. Fix: agree the RACI; this engine owns the brief and measurement definitions.
- Pre-ticked consent boxes. Fix: explicit, unticked consent with a privacy link.

## References

- [Landing-page brief template](references/landing-page-brief-template.md) — read when briefing any destination page.
- [Destination UX heuristics](references/destination-ux-heuristics.md) — read when auditing or briefing a page's usability and trust.
- [Measurement and ownership spec](references/measurement-and-ownership-spec.md) — read when defining UTMs, events, consent and the RACI.
- [UX engagement diagnostics](references/ux-engagement-diagnostics.md) — read when the destination needs UX work the client has not scoped: design paradigm, scope level, production path, maturity ladder, team roles and briefing points before handoff.
- [Post-click strategy](../../playbooks/playbook-post-click-strategy/SKILL.md); [UTM tracking](../../meta-analytics-ops/meta-utm-tracking/SKILL.md); [advertising attribution and measurement](../advertising-attribution-and-measurement/SKILL.md).
- [12-website-content-plan](../../pipeline/12-website-content-plan/SKILL.md); [legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md).
<!-- dual-compat-end -->

## Handoff package to website-skills

| Item | Owner in this engine | Receiver | Format |
|---|---|---|---|
| Landing-page brief | Strategist / copywriter | Website-skills page build | Brief template (reference) |
| Copy deck for the page | Copywriter (`ad-copy-and-hook-lab`, `premium-commercial-writing`) | Web content editor | Structured copy with headings and CTA labels |
| Proof and asset list with consent status | Account lead | Web team | Table with file names, consent record IDs |
| Measurement spec (UTMs, events, values, consent) | Analyst | Tag owner / developer | Spec table |
| Acceptance checks (speed, accessibility, mobile) | Web team owns results | Agency reviews | Test report with dates |
| Go/no-go gate | Account lead chairs | Client approver signs | Checklist |
| Post-launch learning loop | Analyst | Web team | Monthly funnel review and fix list |

Visual design, type and layout go to `design-system-skills`; code, performance and hosting stay with website-skills. This engine does not specify fonts, colours or implementation.

## Brand-slice audit (Stutts 2021)

The brand is every "slice": ad message, landing page, photos, uniforms, phone and WhatsApp scripts, packaging, reviews. Before spend, check that each of the two or three value themes in the ads is visibly present on every slice the buyer meets next, and that trust proof sits where the buyer first looks. Refuse to launch paid media when a critical slice fails (a documented pattern: many leads, few conversions, because the site contradicted the ads).

## Sources

- Levy, J. (2015) *UX Strategy*, O'Reilly — landing-page experiments and funnel matrix.
- Branson, S. (2020) *UX/UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*; Deacon, P.B. (2020) *UX and UI Design Strategy*; Fekeshazi, Z. (c. 2017) *Product Managers' Guide to UX Design*, UX Studio; Synechron (2018) *Bridge the User Experience Gap in Enterprise Applications for Financial Services & Insurance*.
- Stutts, P. (2021) *The Undefeated Marketing System*, Scribe/Lioncrest.
- Wiebe, J. (2011) *Copy Hackers: 6 Persuasion Strategies* — human-contact and pricing cues.
- Currentness register 2026-09-23: CW-01, CW-04, CW-05, CW-10, MK-04.
