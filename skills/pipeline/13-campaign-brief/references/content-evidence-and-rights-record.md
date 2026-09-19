# Content evidence and rights record

Attach this record to a content unit before approval. It is the social-engine
adaptation of the Digital Research source-verification contract; the research
engine remains authoritative for source assessment and currentness.

## Claim row

```yaml
claim_id: claim-001
text: "Exact claim or quotation used in the asset"
source_scope: "Market, period and decision covered"
source_ids: [source-001]
publication_date: "YYYY-MM-DD or unknown"
accessed_on: "YYYY-MM-DD"
support_review:
  state: supported|unsupported|synthesis|inference|no-source
  reviewer: "Named reviewer"
  basis: "Locator, method or limitation"
  reviewed_on: "YYYY-MM-DD"
```

`source_ids` is a list. Use `[]` only with `no-source`; unsupported,
inference and no-source claims are quarantined or explicitly qualified and do
not pass a release gate. `source_scope`, dates and limitations keep historical
or partial evidence from silently becoming a current platform, market, legal
or performance claim.

## Rights row

```yaml
asset_id: asset-001
asset_type: image|video|audio|quote|logo|likeness|customer-story|other
rights_status: cleared|owned|licensed|permission-pending|denied|not-applicable
rights_owner: "Named rights or approval owner"
licence_or_consent_ref: "Record ID, licence or consent reference"
territory: "Where use is allowed"
channels: [Instagram]
expires_on: "YYYY-MM-DD or none"
attribution: "Required credit or none"
reviewed_on: "YYYY-MM-DD"
```

Missing, pending or denied rights block publication. Do not infer permission
from public availability, a repost, a tag or an AI-generated label.

## Acceptance oracle

An independent reviewer can trace every material claim and reused asset to a
record, identify the source scope and dates, see the rights owner and decide
whether the destination and review state are release-ready. If that evidence
is missing, return `NOT_ASSESSED` or `BLOCKED` with the exact recovery owner.
