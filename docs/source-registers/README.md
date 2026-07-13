# Current-source registers

Last full verification: 13 July 2026.

`source-register.json` is the release-controlled register for changing legal, platform and market sources. Tier 1 means a statute, regulator, platform owner or intergovernmental data owner. It does not mean that an interpretation is legal advice or that a platform page will remain unchanged.

## Operating rules

1. Start with the record matching the market, channel and decision. Open the source; never cite this register as though it were the source itself.
2. Record the source ID, access date, relevant section/table, claim and any contradictory evidence in the client evidence log.
3. For market figures, retain the indicator definition, geography, period, population and denominator. Subscribers, accounts, devices, reach estimates and individual users are different measures.
4. For platform policy, verify again on the release date. A passing monthly freshness check does not replace campaign-level review.
5. For legal questions, identify the jurisdiction and processing/advertising act. Escalate material ambiguity, regulated sectors, minors, political/public communications, cross-border data, complaints, or disputed rights to qualified counsel or the responsible regulator.
6. If a source is unavailable, stale or contradictory, mark the check `not assessed` and withhold the affected claim, targeting, collection, publication or approval.

## Registers by use

- Legal and privacy: `UG-*`, `KE-*`, `RW-*`, and `TZ-*` records. See [legal and market release gate](../quality-gates/legal-market-release-gate.md).
- Platform and creator policy: `META-*`, `WHATSAPP-*`, `TIKTOK-*`, and `GOOGLE-*` records.
- Market context: `UCC-*`, `ITU-*`, and `UBOS-*` records. Prefer a current national source for national decisions and ITU for definition-aligned comparisons.

Run the freshness gate:

```powershell
python -X utf8 scripts\check_source_freshness.py
```

Adding a record requires a stable unique ID, current URL, publisher, tier, jurisdiction, verification date, review interval, next-review date, intended uses and a verification note. The checker rejects duplicate IDs, missing fields, invalid dates, inconsistent review dates and overdue records.
