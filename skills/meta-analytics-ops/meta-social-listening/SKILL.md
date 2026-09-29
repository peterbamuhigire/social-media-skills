---
name: meta-social-listening
description: 'Use when a brand wants to know what people say about it and its rivals online: listening queries, sentiment and net sentiment score, share of voice, alert thresholds and escalation; produces the listening plan, sentiment dashboard and monthly insight report; not for answering a live complaint wave (use `playbook-reputation-management`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Listening Programme

Monitors what customers, critics and rivals say about the brand across social, reviews and news, and turns it into logged, scored and routed intelligence for Ugandan and East African clients.

<!-- dual-compat-start -->
## Use When

- The client wants to hear what customers, critics and rivals say about the brand across social, reviews and news.
- Comments, mentions and Google or Facebook reviews need scoring for sentiment (positive, negative, neutral and net sentiment score), share of voice against rivals in the conversation, and ranked themes, in a monthly report.
- A weekly listening routine is needed: tools by budget, crisis-trigger keywords, Mobile Money complaint terms, alert thresholds and a Monday/Wednesday/Friday check.
- Findings must feed content, product or service decisions through an intelligence log.

## Do Not Use When

- `playbook-reputation-management` for responding to complaints and repairing reviews.
- `meta-competitor-analysis` for full competitor benchmarking beyond conversation share.
- `playbook-crisis-communications` for running the response once a crisis is declared.
- Stop before collecting personal data beyond public posts or monitoring in breach of platform terms.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Brand name with all known misspellings and abbreviations, founder or spokesperson name if public-facing, brand hashtag | Client at onboarding | Yes | Stop the taxonomy; the brand terms cannot be guessed. |
| 3–5 competitor names with social handles | Client or `meta-competitor-analysis` | Yes | Monitor brand and industry terms only; mark competitor intelligence and share of voice `not assessed`. |
| Product or service category keywords in customer language, and local language variants (Luganda, Swahili, Sheng) | Client and customer-facing staff | Yes | Use English terms, flag that Luganda and Swahili mentions will be missed, and ask a speaker to supply the top 5 names. |
| Platforms to monitor and current monitoring set-up | Client | Yes | Default to Facebook, Instagram, TikTok, X/Twitter and Google Business Profile, starting from nothing. |
| Tool budget and conversation data or exports for scoring | Client; dated platform exports | If sentiment scoring is wanted | Use the free tool set and manual scoring; mark automated scores `not assessed`. |
| Client name, industry, country/city and primary goal | Client brief | Yes | Default to Uganda / Kampala; ask the goal (catch complaints early, track competitors, surface content ideas). |

The intake list is in [listening programme method](references/listening-programme-method.md) § Required Input.

## Workflow

1. Confirm the goal and the intake; stop and route to `playbook-reputation-management` or `playbook-crisis-communications` when the request is to answer a live complaint wave or run a declared crisis.
2. Build the five-category keyword taxonomy with the client (20–30 minutes): brand, competitor, industry, sentiment triggers and EA location terms, including Luganda or Swahili variants.
3. Set up the four tools: Google Alerts, native platform search, Brand24 or Mention, and Google Business Profile review notifications; add crisis-trigger and Mobile Money keywords from [listening-operations-playbook](references/listening-operations-playbook.md) when the client needs weekly operations.
4. Fix the cadence (daily 5 minutes, weekly 20 minutes, monthly 45 minutes) with a named owner for each task.
5. Log every material mention in the listening log and answer the five weekly listening questions in writing.
6. Score the month: sentiment, NSS, share of voice and ranked themes with [sentiment-and-share-of-voice-method](references/sentiment-and-share-of-voice-method.md), naming the NSS band set used.
7. Route findings to content, campaign, community, crisis and operations owners; turn a listening observation that may change content or service into an experiment card.
8. Check the log and report against the quality standards; correct misclassified or unsourced entries and rerun the NSS and share-of-voice figures before release.

Taxonomy tables, tool set-up steps, cadence tasks, the log template and EA considerations are in [listening programme method](references/listening-programme-method.md).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Listening plan: completed keyword taxonomy, tool set-up and cadence | Consultant and client lead | All five taxonomy categories hold the client's actual terms; every tool has numbered set-up steps; each cadence task has a time estimate. |
| Listening log (Google Sheet, one tab per month) | Social media manager and client | Every row has date, platform, mention type, sentiment, summary, action taken and priority. |
| Weekly debrief and monthly listening summary | Client lead | The five questions are answered; the monthly summary names themes and at least one action with owner and deadline. |
| Monthly sentiment report and dashboard specification | Client; `meta-reporting` | NSS as a number with trend and volume, share of voice against named competitors, ranked themes. |
| Routed findings | `11-content-calendar`, `10-content-pillars`, `09-campaign-strategy`, `playbook-community-management`, `playbook-crisis-communications`, client operations | Each finding names the receiving skill or owner. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Listening entry fields | Log columns: `context`, `audience`, `public/private`, `interaction type`, `confidence`, `action owner`, `decision changed`, `guardrail or escalation` | Every material entry carries them; an inaccessible source is recorded `not assessed`, not filled with a conclusion. |
| Scoring record | Sheet of classified mentions with counts behind NSS and share of voice | A reviewer can recompute NSS and share of voice; Luganda and Swahili items show manual review. |
| Customer-voice experiment card | YAML card per tested observation | Source scope, denominator, privacy boundary, counter-metric, guardrail, decision rule, owner and knowledge link are filled, or the card is `NOT_ASSESSED`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Monitor public posts only, within platform terms; joining Facebook Groups or reading WhatsApp groups needs the client's agreement on which account is used.

## Degraded Mode

Without confirmed brand terms and access to the monitored sources, return the narrowest qualified result and mark the affected checks `not assessed`. A draft taxonomy for the client to confirm, the free tool set-up steps and the cadence can still be delivered; NSS and share of voice wait for data.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The same complaint theme appears three or more times across separate posts | Escalate to the client's operations team, not only the social media manager. | Treating a service or product fault as a social media problem. |
| Negative brand mentions rise sharply, particularly one topic across several platforms in the same 48-hour window | Treat it as a Level 1 crisis trigger and escalate at once using `playbook-crisis-communications`. | A reputational threat found after it has spread. |
| Supplied conversation data must be scored for sentiment, NSS, share of voice or themes | Apply [sentiment-and-share-of-voice-method](references/sentiment-and-share-of-voice-method.md) and end with a named action, owner and deadline. | Unscored mentions, word-only sentiment and data that changes nothing. |
| An NSS figure is reported | Use the EA service-business bands in the sentiment method for monthly and client reports, and the Johnsen (2024) weekly operating bands in the operations playbook for the weekly operating check; name the band set in every report; pair it with mention volume and the driving theme. | Two readings of one score in the same report. |
| The client needs listening run weekly with AI sentiment, dashboard and crisis alerts | Apply [listening-operations-playbook](references/listening-operations-playbook.md) with named owners per day. | Unscheduled monitoring and missed crisis signals. |
| A client story appears on Sqoop, Nile Post or Chimp Reports | Put their feeds in the daily digest; treat coverage as a Level 2 crisis minimum per the operations playbook. | Local amplification outrunning the brand's own reach. |
| The client or staff assume WhatsApp can be monitored | State that it is end-to-end encrypted and cannot be; use a monthly staff feedback form on the top 3 WhatsApp complaints or questions. | False assurance about the largest feedback channel. |
| A listening observation may change content or service | Use the [customer-voice experiment card](references/customer-voice-experiment-card.md); sentiment or activity alone does not prove demand or impact. | Acting on a signal as if it were proof. |

## Quality Standards

- The keyword taxonomy is completed with the client's actual terms across all five categories, not left as a blank template for the client.
- All four tools have numbered, step-by-step set-up instructions, not only tool names and descriptions.
- The cadence lists daily, weekly and monthly tasks separately, each with a time estimate and individually actionable.
- The five listening questions are specific enough that a consultant with public social media data can answer each within 15 minutes.
- The listening log template has column guidance and example rows and is described as a Google Sheet the client can use at once.
- EA considerations cover multilingual monitoring with concrete Luganda examples, the WhatsApp limitation with a named practical workaround, and Facebook Groups with a named monitoring method.
- The strategy integration explicitly connects findings to at least five other skills in the suite by slug name.
- British English throughout, with no American spellings anywhere in the deliverable.

## Anti-Patterns

- Conflating listening with reporting. Fix: read what people say, not only how many said it; reach and engagement numbers belong in `meta-reporting`.
- Treating public mentions as the whole conversation in East Africa. Fix: read them as a proxy for the private WhatsApp majority and add staff-reported WhatsApp themes.
- Monitoring only English keywords. Fix: add the top 5 product and service names as customers say them in Luganda, Swahili or Sheng.
- Sorting TikTok results by "Top". Fix: sort by "Latest" so historical viral content does not hide new mentions.
- Letting findings sit in the log. Fix: route each finding to the named content, campaign, community, crisis or operations owner.
- Reporting sentiment as a word or without volume and driving theme. Fix: follow the NSS rules in the sentiment references.
- Monitoring only mainstream media. Fix: add informal online outlets through RSS in Google Alerts or Feedly.

## References

- [Listening programme method](references/listening-programme-method.md): read when building the taxonomy, setting up tools, fixing the cadence, keeping the log, routing findings or handling EA-specific channels.
- [sentiment-and-share-of-voice-method](references/sentiment-and-share-of-voice-method.md): read when scoring supplied conversation data for sentiment, NSS, share of voice or themes, or producing the monthly sentiment report.
- [listening-operations-playbook](references/listening-operations-playbook.md): read when setting up tools by budget, crisis-trigger keywords, the sentiment dashboard, weekly decision table or the Monday/Wednesday/Friday routine.
- [customer-voice experiment card](references/customer-voice-experiment-card.md): read when a listening observation may change content or service.
- [`meta-competitor-analysis`](../meta-competitor-analysis/SKILL.md): read when full competitor benchmarking is needed beyond conversation share.
- [`playbook-crisis-communications`](../../playbooks/playbook-crisis-communications/SKILL.md): read when a crisis trigger fires.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when writing the debrief and monthly summary.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->
