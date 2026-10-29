# Experiment log — 29 October 2026

The pre-change baseline and synthetic tasks were frozen at `32d4262`; the
following items were kept. Dated currentness detail remains separately in
[03-currentness.md](03-currentness.md). Exact commands and captured outputs
are indexed in [04-validation-record.md](04-validation-record.md).

| Item | Hypothesis and change | Observed result / evidence |
|---|---|---|
| Currentness, `3664c85` | Scoped primary-source reviews and explicit quarantine distinguish supported claims from unavailable evidence | Thirteen scoped reviews completed; ten overdue records remain NOT_ASSESSED and freshness still exits 1. No date-only renewal or legal clearance |
| Overlay, `ecc151a` | Expose the existing social ME/AS semantics at the entry skill so the shared handoff can find them | Semantic reference retained; entrypoint/test passes. This is discoverability proof, not model compliance |
| Package, `177e2a0` | Enforce both full-checkout and package ceilings, manifest identity/path set and fail-closed traversal | Immutable 5,000-entry checks and positive/negative fixtures pass; native local installation succeeds |
| Media provenance, `5a2f371` | Require owner/source/status for media inputs instead of treating arithmetic as a supported forecast | Synthetic calculation reproduces; missing or unsupported provenance is rejected. No real campaign forecast claimed |
| Routing, `f2fd463` | Add probes for touched task routes without weakening prior fixtures | 396/396 top-three, 377 first-rank and 123/123 owned negatives; complete fixture coverage rises from 4/112 to 7/112 |
| Currentness tests, `40d6cd7` | Align tests to scoped review semantics without treating quarantine as pass | Current state remains deliberately blocked; contract tests pass |

Independent acceptance found and repaired additional failure paths: quarantine
must block even before its next review deadline (`a80bc2e`); duplicate workflow
numbering was corrected (`a4ef219`); a symlinked manifest directory is refused
before reading it (`15e73a8`); non-boolean quarantine flags fail closed
(`b42b6ea`). Final evidence refresh is `891bb43`. The complete suite passes
92 tests; source freshness remains a release blocker for the ten records.

No experiment was reverted. The original complete plan/campaign/incident
outputs remain synthetic; client facts, rendered assets, account-level forecasts,
paid behavioural runs and public marketplace approval remain NOT_ASSESSED.
The dimension scores were not increased: raw 58.5, Standard cap 58.5; initial
user cap 45. The 95 target remains unmet.
