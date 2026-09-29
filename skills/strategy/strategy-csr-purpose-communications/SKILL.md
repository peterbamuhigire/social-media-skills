---
name: strategy-csr-purpose-communications
description: Use when a company wants to talk about its community work, sustainability or purpose without greenwashing, or needs a trust audit of price openness, reviews and data consent; produces the CSR communication plan with messaging and a digital transparency report; not for winning press coverage (use `playbook-pr-publicity`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Strategy CSR Purpose Communications

Plans honest communication of a company's purpose, CSR and community work for East African audiences, with every claim evidenced and every beneficiary image consented, and audits digital transparency when trust is the issue.

<!-- dual-compat-start -->
## Use When

- We fund schools, health camps or tree planting and want social content that tells the story honestly.
- We worry our sustainability or impact claims look like greenwashing or charity selfies.
- Beneficiary stories need consent and dignity rules before anything is posted.
- Customers doubt us (hidden prices, only five-star reviews shown, unclear data consent) and we need a digital transparency audit and trust report.
- A purpose statement and messaging framework must link the cause to what the business actually does.

## Do Not Use When

- `playbook-pr-publicity` for press releases, story angles and journalist pitching.
- `playbook-reputation-management` when criticism of the company's conduct is already live.
- `strategy-ewom-reviews` for collecting more reviews and testimonials.
- Stop before publishing impact figures or beneficiary images without verified evidence and recorded consent.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry and country/city | Client | Yes | Default to Uganda/East Africa and ask for the sector before framing purpose. |
| Every current CSR, community, environmental or employee-welfare programme, however small | Client | Yes | Return the CSR audit table blank for the client to complete; draft no content. |
| Evidence per activity (receipts, photos, beneficiary numbers, NEMA certification, HR or supplier data) and consent records | Client files | Yes | Record the activity as a future communications opportunity, not a current claim. |
| Target audiences and the commercial objective (brand preference, employee pride, investor or donor reporting, regulatory goodwill, differentiation) | Client lead | Yes | Plan for customers and community only and mark investor, donor and regulator outputs `not assessed`. |
| Past CSR communications, reception and any greenwashing accusations | Client; public record | If any | Treat the audience as sceptical and apply the journalist test to every claim. |
| Budget and production capacity (video, photographer, one person or a team) | Client | Yes | Plan photo-and-caption formats only. |

## Workflow

1. Confirm whether the trust gap is a CSR or purpose story or a digital customer-experience problem (pricing, curated reviews, consent); route the latter to the [digital transparency framework](references/digital-transparency-framework.md) and live criticism to `playbook-reputation-management`.
2. Agree the purpose vs CSR vs greenwashing distinction with the client; if no credible purpose is grounded in how the business operates, stop and help them name their operational values rather than inventing one.
3. Complete the CSR audit table; stop any activity without evidence or consent from reaching content and log it as a future opportunity.
4. Plan the four content types (impact stories as Hero, progress reports and behind-the-scenes as Hub, employee voice as Hygiene) with platforms chosen per audience.
5. Draft copy and review it against the five messaging principles, adding Luganda or other local-language captions for community audiences.
6. Apply the journalist test and the children's consent rule to every claim and image; correct or cut any claim that fails and rerun the test before approval.
7. Run the anti-slop gate and hand the plan, messaging framework and consent log to the client approver; nothing is published without their sign-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Purpose statement and messaging framework linking the cause to what the business does | Client leadership; communications team | Purpose is grounded in operations; no content claims purpose where evidence supports only CSR. |
| Completed CSR audit table | Client lead | Every activity has an evidence column; unevidenced ones are flagged as future opportunities. |
| CSR content plan across the four content types, by audience and platform | Content team; `05-social-media-strategy` | All four types present with Uganda/East Africa examples and cadence. |
| Digital Transparency Report (when the gap is digital) | Client lead | Built with the transparency framework's audit, scores and release checklist. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Claim-to-evidence register | Table | Every CSR assertion links to a photo, data point, document or named, consenting person. |
| Consent log for beneficiaries, employees and children | Table | Documented parental or guardian consent for every child under 18 shown or named; otherwise not published. |
| Journalist-test record | Checklist per claim | Each published claim records the evidence the client could produce tomorrow. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Collecting beneficiary names, images or stories is personal-data processing and needs recorded consent.

## Degraded Mode

Without evidence and consent records for each CSR activity, return the narrowest qualified result and mark the affected checks `not assessed`. The purpose/CSR/greenwashing framing, a blank CSR audit table and an evidence-gathering plan can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Impact evidence is incomplete or disputed | Publish only substantiated scope and commission evidence review. | Greenwashing or overstated community benefit. |
| A claim fails the journalist test ("could the client produce evidence tomorrow?") | Do not publish; advise the client to create the evidence first. | Challenge from the Monitor, the Observer, NBS Television or NGO networks. |
| Content features a child under 18 without documented parental or guardian consent | Do not photograph, film, name or publish, in any format. | Legal liability under the Children Act (Cap. 59) and reputational damage. |
| The CSR activity has no logical link to the business's operations | Reframe towards the harms or dependencies the business actually has, or present it plainly as CSR, not purpose. | Performative CSR that audiences see through. |
| Targets were missed | Report the shortfall and the reason alongside the next commitment. | A progress report that reads as spin. |
| The trust gap is in the digital customer experience (unclear pricing, curated reviews, consent) rather than a CSR programme | Audit clarity, openness and objectivity with [digital-transparency-framework](references/digital-transparency-framework.md) before recommending. | Assumed transparency and unlawful data collection. |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source. | Confident advice built on an unresolved premise. |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist. | Unauthorised publication, spend, outreach, or data use. |

## Quality Standards

- The distinction between purpose, CSR, and greenwashing is stated clearly and applied consistently — no content claims purpose when the evidence supports only CSR.
- The CSR audit table is completed before any content strategy is produced — unevidenced activities are flagged as future opportunities, not current claims.
- The evidence requirement is stated explicitly for every claim: every CSR assertion is linked to a specific piece of evidence (photo, data, document, name).
- All four content types (impact stories, progress reports, behind the scenes, employee voice) are represented in the content plan, with Uganda/East Africa-specific examples.
- The children's photography consent rule is stated and applied — no content featuring minors is approved without documented parental or guardian consent.
- Greenwashing risk is acknowledged and mitigated — the journalist test is applied to all claims before publication.
- The messaging framework (specificity, show don't claim, acknowledge complexity, community voice, regulatory context) is applied to all draft content before approval.
- Uganda/East Africa, British English, EAT, UGX and WhatsApp-first assumptions are explicit; `ai-marketing/anti-ai-slop` is applied during drafting and release is blocked on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Posting "We are committed to a greener Uganda" with no supporting evidence. Fix: state a specific, evidenced figure, or invest first and communicate second.
- Making the CEO or marketing manager the hero of the story. Fix: feature beneficiaries, employees and local leaders; leadership appears as supporters and enablers.
- Scripted or coached "happy employee" content. Fix: use only genuinely voluntary, unscripted staff voices.
- Manufacturing links with churches, mosques or community institutions for content. Fix: feature only genuine relationships, with the institution's consent.
- Publishing only in English for community audiences. Fix: add Luganda, Runyankole/Rukiga, Acholi/Luo or Lusoga captions, translations or voiceovers where relevant.
- Communicating CSR only during a crisis. Fix: frame it as a long-term relationship with the community and publish steadily.
- Treating a missing consent record or evidence file as a pass. Fix: mark it `not assessed` and hold the content.

## References

- [CSR communication method](references/csr-communication-method.md): read when running the intake, separating purpose from CSR and greenwashing, completing the CSR audit, planning the four content types, reviewing copy against the messaging framework or applying East African defaults and platform selection.
- [Digital transparency framework](references/digital-transparency-framework.md): read when auditing digital transparency, calibrating trust by generation or producing a Digital Transparency Report.
- [`05-social-media-strategy`](../../pipeline/05-social-media-strategy/SKILL.md): read when fitting CSR communications into the broader social media strategy, channel plan and content calendar.
- [`playbook-reputation-management`](../../playbooks/playbook-reputation-management/SKILL.md): read when CSR communications is being used to respond to or mitigate a reputational crisis about social or environmental conduct.
- [`biz-dev-credentials`](../../business-development/biz-dev-credentials/SKILL.md): read when impact reports, case studies or beneficiary stories go into pitch or agency credentials.
- [`east-african-english`](../../language/east-african-english/SKILL.md): read when setting language, tone and register for English-language CSR content before publication.
- [AGENTS.md](../../../AGENTS.md): read when routing to a neighbour skill or engine.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting impact stories, captions and reports.
<!-- dual-compat-end -->
