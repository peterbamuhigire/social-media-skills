---
name: meta-content-audit
description: Use when a client wants past posts reviewed to see what worked, what flopped and what to keep, update or retire, by platform and content pillar; produces the content audit with top and bottom posts, pillar coverage, tone rating and a 30-day fix list; not for auditing profiles and account set-up (use `02-platform-audit`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Content Audit

A read-only review of a client's published posts from exported platform data: performance by platform against Uganda / East Africa benchmarks, top and bottom posts, pillar coverage, tone and consistency, and five 30-day fixes. Metric findings are paired with narrative, audience-empathy and readability checks.

<!-- dual-compat-start -->
## Use When

- The client has months or years of posts and wants them rated by reach and engagement: which themes underperformed, which posts earned results and which wasted effort.
- Posts need sorting into keep, update, retire (delete) or test decisions before anything is reused or a new plan is written.
- Pillar balance, tone consistency or narrative quality looks uneven and needs rating against the brand voice.
- A read-only review of a content library is required from exported platform data, without touching live accounts.

## Do Not Use When

- `02-platform-audit` for auditing profiles, bios, links and account set-up.
- `meta-competitor-analysis` for comparing named rivals.
- `meta-content-repurposing` for turning the best posts into new formats.
- Stop when no dated platform export is supplied; request it rather than estimating performance.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Post-level data for the audit period (default last 3 months, at least 30 posts per platform) | Native analytics exports completed on the data template | Yes | Stop; hand over the template and request the export rather than estimating performance. Extend to 6 months where a platform has fewer than 30 posts. |
| Platforms to audit | Client brief | Yes | Audit only platforms with an export; mark the rest `not assessed`. |
| Client name, industry, country/city and primary goal | Client brief | Yes | Default to Uganda / Kampala; ask the goal before prioritising fixes. |
| Content pillars | `10-content-pillars` output | If established | Cluster posts into 3–5 topic groups and recommend them as draft pillars. |
| Brand voice guide | `04-brand-voice-intake` output | If available | Rate tone against observed patterns and state that no guide was supplied. |
| Representative items with renders, sources and approvals | Client content library | For the narrative audit | Mark narrative, accessibility and permission checks `not assessed`. |

## Workflow

1. Collect intake and the post-level data ([audit data and output template](references/audit-data-and-output-template.md) § Step 1); stop if no dated export exists, and route profile or set-up audits to `02-platform-audit`.
2. Sort posts by engagement rate descending and build the performance summary per platform against the Uganda / EA benchmarks; flag any platform below benchmark.
3. Analyse the top 5 posts (ties broken by absolute reach) and the bottom 3 (excluding zero-reach posts), with specific, distinct reasons and one instruction each.
4. Check pillar coverage against the 10-4-1 rule, or cluster posts into draft pillars when none exist.
5. Rate visual, tone and posting consistency on 1–10 with evidence-based justifications.
6. Apply the [narrative, audience empathy and content quality audit](references/narrative-empathy-and-content-quality.md) to representative items and publish the capped audit plus the 95/100 remediation plan.
7. Write exactly 5 priority improvements for the first 30 days, highest impact first, covering format, consistency and pillar balance.
8. Run the quality standards and anti-slop gate; correct any finding without a data basis and rerun the check. Withhold release while a metric is invented or a missing check is shown as a pass.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Performance summary per platform | Client lead | Every metric row filled from supplied data and compared with the Uganda / EA benchmark. |
| Top 5 and bottom 3 post analysis | Content team | Each post has distinct reasons and one specific replicate or avoid instruction. |
| Pillar coverage and tone/consistency ratings | Client lead; `10-content-pillars` | Pillars over 40% or under 10% flagged; each score justified with evidence. |
| Narrative quality audit (capped score) and 30-day improvement list | Client lead and next workflow owner | Audit score published as `min(raw score, 65)`; 5 improvements each traced to a finding. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Completed post-level data table | Spreadsheet or table per platform | Source export and period stated; engagement rate = engagement ÷ reach × 100. |
| Not-assessed register | Table: check, reason, recovery evidence | Missing renders, sources, permissions or native-language reviews listed, never counted as passes. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Retiring or editing a post is the client's decision after the audit; the audit never deletes or changes live content.

## Degraded Mode

Without dated post-level exports, return the narrowest qualified result and mark the affected checks `not assessed`. The data template, the benchmark table and a qualitative tone and pillar review of supplied screenshots can still be delivered, labelled as unscored.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The requested outcome belongs to `meta-competitor-analysis` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |
| A platform has fewer than 30 posts in 3 months | Extend the audit period to 6 months. | Patterns read from too small a sample. |
| A bottom-ranked post had zero reach | Exclude it and log it as a technical issue, not a content failure. | Blaming content for a delivery fault. |
| A pillar exceeds 40% of the mix or falls below 10% | Flag over-reliance or neglect against the 10-4-1 rule (Bodnar and Cohen, 2012). | An unbalanced, over-promotional feed. |
| A consistency dimension scores 1–4 | Recommend addressing it before further investment in content production. | Scaling inconsistent content. |
| Engagement is high but the offer or next step is unclear | Inspect narrative and information hierarchy before calling the content effective. | Rewarding posts that do not move the audience. |
| A post was paid-boosted | Record "Paid boost? Yes" and name paid amplification as a factor when explaining its performance. | Crediting paid amplification to content quality. |

## Quality Standards

- Uses only data provided by the consultant; no invented metrics or engagement rates without a stated basis.
- Platform summaries compare against Uganda / EA benchmarks, not just internal averages.
- Top and bottom post analysis gives specific and distinct reasons, not the same generic factors repeated.
- Pillar coverage flags imbalances clearly with reference to the 10-4-1 rule.
- Tone and consistency ratings are justified with evidence from the content, not assigned arbitrarily.
- The 30-day improvements are prioritised by impact and each traces to a specific audit finding.
- Output is direct and honest: underperformance is named, not softened.
- Metric findings are paired with audience empathy, narrative clarity, hierarchy, readability/accessibility, evidence, permissions, AI transparency and learning-value findings.

## Anti-Patterns

- Estimating performance when no export was supplied. Fix: request the dated export and hand over the data template.
- Repeating the same generic reasons ("good visuals") for every top post. Fix: name distinct factors per post from the list in the template.
- Softening the bottom-post diagnosis. Fix: state the likely cause plainly; honest diagnosis prevents repeated mistakes.
- Calling content effective because engagement is high while the audience cannot understand the offer or next step. Fix: inspect the narrative and information hierarchy.
- Treating a missing render, source, permission or native-language review as a pass. Fix: mark it `not assessed`, state the risk and name the recovery evidence.
- Judging YouTube by engagement rate alone. Fix: measure watch-time completion % and click-through rate.

## References

- [Audit data and output template](references/audit-data-and-output-template.md): read when collecting intake, sharing the post-level data template and where to find data per platform, applying the Uganda / EA benchmarks, writing the seven output sections, or citing Bodnar and Cohen (2012) and Chaffey and Ellis-Chadwick (2022) (RACE framework).
- [Narrative, audience empathy and content quality audit](references/narrative-empathy-and-content-quality.md): read when auditing audience, story, visual, accessibility and learning quality and scoring the capped audit.
- [`meta-competitor-analysis`](../meta-competitor-analysis/SKILL.md): read when named rivals must be compared.
- [`meta-content-repurposing`](../meta-content-repurposing/SKILL.md): read when the best posts are to be turned into new formats.
- [`02-platform-audit`](../../pipeline/02-platform-audit/SKILL.md): read when profiles, bios, links or account set-up need auditing.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting findings and improvements.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->
