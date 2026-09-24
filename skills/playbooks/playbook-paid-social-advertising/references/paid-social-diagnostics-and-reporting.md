# Paid social diagnostics and reporting

When to read: during weekly optimisation, when a campaign underperforms, or when preparing the monthly report. All thresholds are set from the client's economics and own baseline; the engine does not publish UGX CPM, CPC or CTR norms.

## 1. Setting the lines

| Line | How to set it |
|---|---|
| Break-even cost per acquisition | Gross profit per sale (or agreed share of lifetime contribution) |
| Allowable cost per qualified lead | Break-even CPA × lead-to-sale rate (from CRM) |
| Kill line | Cost per result above the allowable level for the agreed window after one creative and one audience fix |
| Scale line | Cost per result below the allowable level for the agreed window with stable lead quality |
| Fatigue watch | Frequency and hook/click rates tracked against the client's own first-month baseline |

Baselines come from the first two to four weeks of the client's own data; record them with dates.

## 2. Weekly checklist

- [ ] Cost per qualified result per ad set vs the line.
- [ ] Frequency and click-through trend vs baseline; refresh creative before fatigue sets in.
- [ ] Top and bottom ads per ad set; pause clear losers, keep a control.
- [ ] Delivery status and any learning-period notices (check current platform guidance for what they mean).
- [ ] Tracking still firing (test event).
- [ ] Lead quality from sales or WhatsApp logs; response times.
- [ ] Log every change with date and reason.

## 3. Eight-step diagnostic (one variable at a time)

Adapted from Cooper (2019) with thresholds removed:

1. Tracking: are results recorded correctly? If not, stop and fix.
2. Delivery quality diagnostics (the platform's relevance or quality rankings, where offered): a below-average quality signal points to creative.
3. Cost per click trend against the client's baseline: rising cost with acceptable quality points to audience saturation or competition.
4. Creative problem (low engagement, weak hook rate): test a new first frame or image first, then primary text, then headline.
5. Audience problem (good quality signals, high costs): widen, rotate or refresh the audience; do not change creative at the same time.
6. Destination problem (clicks without conversions): check message match, speed and form or WhatsApp friction via `ad-to-site-journey-handoff`.
7. Segment breakdown: exclude age, gender, placement or district slices with persistently high cost per result.
8. Offer problem: if all else is sound, the offer or price is the constraint; return to the offer workshop.

Kill after the planned fixes fail within the window; a third creative change without improvement usually means the audience or offer is the problem.

## 4. Decision memo (for every scale, pause or refresh)

Decision · evidence (export, date) · line used · expected effect · what would reverse the decision · approval needed (budget changes require written client approval).

## 5. Monthly report

Executive summary · spend and results vs target · audience tiers · creative learnings · downstream quality (lead-to-customer) · tests and decisions · attribution caveats (platform-reported vs CRM; modelled conversions) · next month's plan and budget split in UGX · approvals required.

Use `advertising-attribution-and-measurement` for reconciliation of platform-reported and CRM results and `meta-reporting` when the paid report is combined with organic reporting.
