---
name: training-social-media-fundamentals
description: 'Use when beginners (owners, new staff, SACCO or youth groups) must learn how social media marketing works: what each platform is for, algorithms, followers versus engagement, safety and what to track; produces the beginners'' training guide; not for handing an agreed strategy to client staff (use `training-client-team`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Media Fundamentals Training Guide

Produces a warm, plain-English, standalone beginners' guide (cover page and nine sections) grounded in Uganda and East Africa, for owners and staff with no marketing background to read alone or with a facilitator.

<!-- dual-compat-start -->
## Use When

- Business owners or new staff have never used social media for business.
- People confuse followers with results and need the basics of algorithms, the 80/20 content rule and engagement.
- A platform primer is needed: what Facebook, Instagram, TikTok, WhatsApp, LinkedIn and X are each for in Uganda.
- Beginners must stay safe online: scams, account security and what not to post.
- Trainees need the few numbers worth tracking and the most common beginner mistakes.

## Do Not Use When

- `training-client-team` for handing an approved strategy and daily operations to the client's staff.
- `training-smartphone-video-production` for phone filming and editing skills.
- `05-social-media-strategy` when the group needs an actual strategy rather than training.
- Stop before creating or logging into trainees' accounts on their behalf; teach them to do it themselves.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry and country/city | Client lead | Yes | Default to Uganda/East Africa and use mixed-sector examples (restaurant, school, NGO, retail). |
| Primary goal for social media | Client lead | Yes | Frame the guide around weekly enquiries from social media and ask for the goal before release. |
| Platforms currently used (even if used poorly) | Client lead or a look at the client's pages | Yes | Start from Facebook and WhatsApp under the 2-platform focus rule. |
| Team size and prior experience (posting already, or starting from scratch) | Client lead | Yes | Assume starting from scratch and keep every section at beginner level. |
| Current platform user figures for Uganda | Dated platform or market source; register WA-01 for WhatsApp | For Section 2 | Keep the stated figures qualified; state no WhatsApp percentage and point to the client's own audience data. |

## Workflow

1. Run the intake in [fundamentals-guide-sections.md](references/fundamentals-guide-sections.md); route strategy requests to `05-social-media-strategy` and operational handovers to `training-client-team`.
2. Write the cover page and Section 1 (what social media marketing is and is not, organic vs paid, why posting alone is not a strategy, three misconceptions).
3. Write Sections 2–3: why social media matters in Uganda (numbers, trust journey, cost advantage) and the platform primer with the 2-platform focus rule; stop and qualify any platform figure that has no dated source.
4. Write Sections 4–6: algorithms (what they reward and penalise), the 80/20 rule with the last-10-posts self-audit and an industry-specific example table, and followers vs engagement with the engagement-rate formula.
5. Write Sections 7–9: content basics (hook, value, one CTA; photo basics; posting frequency), the four metrics and weekly enquiry count, and the seven common mistakes.
6. End each section with one actionable takeaway, then check the guide against the Quality Standards and `anti-ai-slop`, blocking release on an F from `ai-slop-audit`; correct any failing section and rerun the check.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Beginners' training guide: cover page and nine sections | Business owner, new staff, SACCO or youth group | Self-contained, all nine sections in full, client name and industry throughout. |
| Last-10-posts self-audit and weekly enquiry count | Trainees | Each trainee can classify their last 10 posts and record weekly enquiries from social media. |
| Industry-specific 80/20 example table | Trainees | Value and promotional examples drawn from the client's own industry. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Platform figure register | Table: figure, source, date or register ID | Every Uganda platform figure is dated, registered or qualified. |
| Section takeaway check | List of nine takeaways | Each section ends with one actionable takeaway. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Trainees create and log into their own accounts; never do it on their behalf.

## Degraded Mode

Without current dated Uganda platform figures, return the narrowest qualified result and mark the affected checks `not assessed`. Sections 1 and 4–9 can still be delivered in full, as they teach principles rather than market statistics.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Learners need conceptual foundations before operational handover | Teach the decision model first, then route to role-specific practice | Tool clicks are taught without explaining why a channel or metric matters |
| A new starter wants to be on every platform | Apply the 2-platform focus rule; for most Ugandan businesses start with Facebook and WhatsApp | Five half-managed accounts and no results |
| More than 2 of the last 10 posts are promotional | Rebalance to 80% value, 20% promotion | An audience that tunes out |
| Engagement rate is below 1% | Treat content as not connecting; fix relevance before frequency or follower growth | Chasing followers while engagement collapses |
| A trainee proposes buying followers or follow-unfollow | Reject it and explain that fake growth reduces reach | A low-quality account signal to the algorithm |
| A Uganda platform figure has no dated source | Keep it qualified in Section 2 and point trainees to their own audience data | Beginners quoting stale statistics as fact |
| Trainees ask the trainer to set up or log into their accounts | Talk them through it on their own devices; never hold their passwords | Account ownership and security lost at the start |

## Quality Standards

- The guide reads as a complete, self-contained training document, not a list of instructions to the consultant.
- All bracketed placeholders are replaced with the client's specific business name, industry, city, and context.
- Ugandan examples, platform figures, and local context are present throughout; no generic Western examples remain.
- The 80/20 content rule table in Section 5 includes examples drawn from the client's specific industry.
- Tone is warm, clear, and jargon-free throughout, appropriate for a business owner or NGO staff member with no marketing background.
- British English spelling is used consistently (organisation, colour, programme, analyse, behaviour).
- Every section ends with at least one clear, actionable takeaway the reader can apply immediately.
- The guide covers all nine sections in full; no sections are skipped or condensed to bullet points only.

## Anti-Patterns

- Posting only promotional content. Fix: apply the 80/20 rule and run the last-10-posts self-audit.
- Ignoring comments and messages. Fix: reply within a few hours during business hours, always.
- Copying other accounts' photos or videos. Fix: create original content; imperfect originals outperform polished stolen content.
- Going silent for weeks, then posting a burst. Fix: pick a sustainable schedule (for example Facebook 3–4 times per week) and keep it.
- Using the same caption across all platforms. Fix: adapt the message to each platform's language and audience.
- Celebrating follower count while enquiries stay flat. Fix: track weekly enquiries from social media as the first number.
- Waiting for perfection before posting. Fix: start posting, learn from what works and improve.

## References

- [fundamentals-guide-sections.md](references/fundamentals-guide-sections.md): read when running intake or writing the cover page and Sections 1–9, including the Uganda platform numbers, platform primer table, engagement-rate formula, posting frequencies and metrics table.
- [`training-client-team`](../training-client-team/SKILL.md): read when the group moves on to running an approved strategy.
- [`training-smartphone-video-production`](../training-smartphone-video-production/SKILL.md): read when trainees need phone filming beyond Section 7's photo basics.
- [`05-social-media-strategy`](../../pipeline/05-social-media-strategy/SKILL.md): read when the group needs an actual strategy.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting guide copy and hooks.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read when scoring the finished beginners' guide before release.
- [AGENTS.md](../../../AGENTS.md): read when checking repository-wide doctrine.
<!-- dual-compat-end -->
