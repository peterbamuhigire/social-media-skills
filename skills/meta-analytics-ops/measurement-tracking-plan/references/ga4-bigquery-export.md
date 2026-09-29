# GA4 BigQuery Export

New reference for `measurement-tracking-plan` (Social Kaizen S04-T01, benchmark row SL15-C1; 29 September 2026). Platform facts were read live on 29 September 2026 (register GA4-BIGQUERY-EXPORT-2026, GA4-DATA-RETENTION-2026).

## When to use this reference

Use it when the client or analyst needs raw GA4 events: history longer than GA4 retention, joins with CRM or WhatsApp order data, custom attribution or cohort work, or a dashboard that GA4's interface cannot produce. Use it before promising any of these, because export type, limits and cost decide what is possible.

## Facts to work from

| Fact | Register |
|---|---|
| BigQuery export is available to standard and 360 properties. | GA4-BIGQUERY-EXPORT-2026 |
| Daily export: standard properties up to 1M events per day, with filtering options to stay under the limit; 360 properties up to 20B events per day. | GA4-BIGQUERY-EXPORT-2026 |
| Streaming export: available to both; near real time; no completeness SLO and may contain gaps; excludes new-user and new-session traffic-source data; costs USD 0.05 per GB (about 600,000 events per GB, varying by event size). | GA4-BIGQUERY-EXPORT-2026 |
| Fresh daily export (faster, more complete intraday data, typically by 5 a.m.) is for 360 properties. | GA4-BIGQUERY-EXPORT-2026 |
| GA4 interface retention on standard properties is 2 or 14 months for user-level and key-event data and applies to explorations and funnel reports; exported BigQuery tables are kept under the client's own BigQuery settings. | GA4-DATA-RETENTION-2026 |

BigQuery storage and query pricing, sandbox limits and table-expiry defaults were not read on 29 September 2026: verify on Google Cloud's pricing pages before quoting a cost.

## Decision rules

| Condition | Action | Risk avoided |
|---|---|---|
| Standard property under 1M events a day, with headroom | Daily export | Paying for streaming without need |
| Standard property near or over 1M events a day | Filter the export (exclude low-value events) or add streaming; state the choice and cost | Exports that stop or drop data |
| Intraday reporting needed (flash sales, live campaigns) | Streaming export, labelled "may contain gaps"; reconcile with the daily table next day | Treating incomplete intraday data as final |
| New-user acquisition analysis | Use the daily tables (streaming excludes new-user and new-session traffic source) | Wrong acquisition splits |
| Client has no Google Cloud billing owner | Stop; name an owner and a monthly budget alert before linking | Unowned cloud bills |
| Personal data would sit in BigQuery | Confirm lawful basis, access list, dataset location and cross-border record | Unlogged transfer and over-wide access |

## Procedure

1. **Estimate volume**: current daily events from GA4 (Admin or a 7-day report); project campaign peaks.
2. **Choose export type** with the decision rules; write the reason in the plan.
3. **Name owners**: Google Cloud project and billing owner, dataset access list, budget alert amount.
4. **Record data-protection details**: dataset location, who can query, retention (table expiry) and the cross-border entry in the minimisation register.
5. **Specify the first uses**: the two or three questions the export must answer (for example CRM-joined revenue by campaign, 13-month trend, WhatsApp-click to order match rate), so the export is not an empty warehouse.
6. **QA**: after 48 hours compare BigQuery event counts with GA4 for the same day and key events; differences beyond an agreed tolerance are investigated before any dashboard is built on the data.
7. **Review monthly**: volume against the limit, cost against the budget alert, access list.

## Working notes for analysts (verify against the current schema at use)

- Daily tables are date-sharded (`events_YYYYMMDD`); streaming writes to intraday tables. Event parameters are nested and need `UNNEST(event_params)` to read.
- Always filter on the table suffix (date range) to control query cost.
- Join to CRM data on a lawful, non-personal key where possible (order or lead ID carried as an event parameter), not on raw email or phone.

## Output (template)

| Decision | Choice | Reason | Cost estimate and source | Owner |
|---|---|---|---|---|
| Export type | daily / daily + streaming / filtered daily | | | |
| Dataset location and access | | | | |
| Retention (table expiry) | | | | |
| First questions answered | | | | |
| QA tolerance and date | | | | |
