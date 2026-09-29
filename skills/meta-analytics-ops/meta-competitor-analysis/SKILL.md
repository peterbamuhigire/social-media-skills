---
name: meta-competitor-analysis
description: 'Use when a client asks how named rivals compare on social: what they post, how often, their ads, tone and positioning, and where the openings are; produces the competitor comparison table, gap analysis and opportunity register; not for auditing the client''s own profiles (use `02-platform-audit`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Competitor Analysis

Compares the client with three to five named rivals on platforms, followers, posting frequency, content style, engagement and visible paid activity, then turns the gaps into five recommendations. Defaults to the Uganda / East Africa context unless another market is specified.

<!-- dual-compat-start -->
## Use When

- The client names three to five rivals (competing banks, telcos, retailers or schools) and wants to know what they post, their themes, formats and messages, posting frequency and audience response.
- The team needs to see which competitors run paid ads now, from the Meta Ad Library and other public sources.
- Find the angles, positioning or content gaps none of the competitors are using yet, before the strategy is written.
- A competitive matrix is needed for a pitch or a quarterly review.

## Do Not Use When

- `02-platform-audit` for auditing the client's own profiles, bios and quick fixes.
- `meta-social-listening` for ongoing share of voice and sentiment from conversation data.
- `marketing-foundations-stp-positioning` for choosing the client's own positioning.
- Stop before stating a competitor figure without a dated public source; mark it not assessed.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Competitor list (3–5): business names, handles per platform, and whether each is direct, aspirational or indirect | Client and sales team | Yes | Build the list from where buyers look ([competitive matrix](references/competitive-matrix-and-analysis.md) § 2) and confirm it with the client before analysis. |
| Client's own stats: platforms, followers, engagement rate, posting frequency, paid ads running | Client or client-authorised insights | Yes | Fill the client row from public profiles and label every figure an estimate. |
| Client name, industry and sub-sector, country/city, primary goal | Client brief | Yes | Default to Uganda / Kampala; ask the goal question before writing recommendations. |
| The decision the comparison must inform | Client brief | Yes | Stop; a matrix without a decision becomes a directory. |
| Dated public evidence (profiles, last 10 posts, ad libraries) | Public platform pages and ad libraries | Yes | Mark the cell `not assessed`; never state a competitor figure without a dated source. |

## Workflow

1. Collect the intake ([five-section analysis template](references/five-section-analysis-template.md) § Intake questions) and confirm the decision the analysis serves; stop if no competitors or decision can be named, and route own-profile audits to `02-platform-audit`.
2. Fill the comparison table with the client row labelled **[CLIENT — FOR COMPARISON]** at the top, recording the source and access date for every cell.
3. Write the content style breakdown for each competitor and the client, including what each does not talk about.
4. Check paid activity in the Meta Ad Library, TikTok Creative Center, LinkedIn Ad Library and Google Images; record Active / Not active / Unknown with the caveat that presence confirms activity only.
5. Categorise activity with the POEM model (Paid / Owned / Earned) and cluster rivals that play the same game ([competitive matrix](references/competitive-matrix-and-analysis.md) § 4).
6. Identify 3–5 actionable gaps (platform, content, tone, community, speed) and write exactly 5 recommendations, each tied to a named gap or competitor insight.
7. Run the quality standards and the anti-slop gate; correct any undated figure or generic gap and rerun the check. Withhold any comparative claim meant for publication until it has evidence and legal review.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Competitor comparison table | Client lead; strategy owner | Client row first; every competitor covered with no placeholder rows; engagement labelled as an estimate. |
| Content style analysis and paid ad activity note | Client lead | Each profile names genuine absences; ad status per platform with the tool used. |
| Gap analysis and five strategic recommendations (opportunity register) | Client lead; `marketing-foundations-stp-positioning` or strategy writer | 3–5 client-specific gaps; 5 recommendations across at least 3 platforms, each with action, why, platform and 90-day benefit. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Source and access-date log | Table: competitor, cell, source, date | Every figure has a source and date or is marked `not assessed`; third-party traffic figures labelled estimates. |
| Ad library screenshots or notes | Dated captures per competitor | Ad status backed by a dated capture; spend never inferred. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Use only public or legitimately obtained information: no pretexting and no approaching rivals' staff.

## Degraded Mode

Without dated public evidence for a competitor, return the narrowest qualified result and mark the affected checks `not assessed`. The comparison table for the rivals that can be evidenced, the content style profiles and provisional gaps can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The requested outcome belongs to `02-platform-audit` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |
| Engagement rate must be estimated from public data | Use visible likes and comments on the last 10 posts ÷ follower count × 100 and label it an estimate, not platform-reported data. | Presenting guesses as platform metrics. |
| Ad library shows ads for a rival | Record the ads as active and note formats and calls to action; say nothing about budget, targeting or performance. | Inventing ad spend from presence data. |
| All competitors crowd one platform and neglect another | Treat the neglected platform as a platform gap the client can own. | Following the field into the crowded channel. |
| Two rivals already own the client's intended claim | Choose another claim or prove superiority with evidence. | A me-too position. |
| Every rival shares a weakness customers complain about | Treat that weakness as the opening. | Missing the clearest gap. |
| A gap exists only in the analyst's opinion | Test it with customers before building a campaign on it. | Campaigns built on untested assumptions. |

## Quality Standards

- A client row sits at the top of the comparison table for direct benchmarking.
- Every competitor provided is covered, with no placeholder or skipped rows.
- Content style analysis identifies genuine absences (what competitors do *not* cover), not just what they do.
- The paid ad section directs the consultant to free tools with specific navigation instructions, not generic advice.
- Gaps are actionable for this client, not observations that could apply to any business.
- Each recommendation ties to a specific gap or competitor insight; recommendations span multiple platforms with a realistic timeframe for the expected benefit.
- Output defaults to Uganda / East Africa context unless otherwise specified.
- Earned media evidence (shares, press, organic viral) is noted in the profiles where observed.

## Anti-Patterns

- Stating a competitor's follower count or engagement without a date. Fix: record source and access date or mark it `not assessed`.
- Reading ad-library presence as spend or performance. Fix: report activity only; spend is not disclosed.
- Listing what rivals do and ignoring what they omit. Fix: complete the "What they do not talk about" line for every profile.
- Generic gaps ("post more video"). Fix: name the competitor, the gap type and why the client can exploit it.
- Recommendations with no link to the analysis. Fix: cite the gap or competitor finding behind each of the five.
- Using a personal social login or copying rivals' creative. Fix: use a shared test account and public evidence only.

## References

- [Five-section analysis template](references/five-section-analysis-template.md): read when collecting intake, filling the comparison table columns, writing style breakdowns, checking ad libraries, framing gap categories (including local-language content in Luganda and Swahili), writing recommendations, or citing Bodnar and Cohen (2012) and Chaffey and Ellis-Chadwick (2022).
- [Competitive matrix and analysis procedure](references/competitive-matrix-and-analysis.md): read when building the competitor list, the matrix columns and the findings brief.
- [`02-platform-audit`](../../pipeline/02-platform-audit/SKILL.md): read when the client's own profiles need auditing.
- [`meta-social-listening`](../meta-social-listening/SKILL.md): read when ongoing share of voice and sentiment are needed.
- [Legal, privacy and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when a comparative claim will be published.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting findings and recommendations.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->
