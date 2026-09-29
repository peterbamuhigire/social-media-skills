# Trustworthy experiments: pre-registration, SRM, power, stopping rules and holdouts

Read when a test must stand up to scrutiny: before launch (pre-registration, minimum detectable effect, power, guardrails), during the run (peeking and stopping rules), at read-out (sample-ratio-mismatch check), or when a lifecycle holdout group is designed. This file owns the experiment statistics for the engine; `ad-testing-and-scaling` and `creative-brief-and-big-idea` point here rather than repeating it.

Concept input: Kohavi, Tang and Xu (2020) *Trustworthy Online Controlled Experiments*, Cambridge University Press. The checks below apply its ideas in the engine's own words and task structure; nothing is reproduced from the book.

## 1. Pre-registration record (written and dated before launch)

A test is pre-registered when the following are written down, dated and shared with the client approver before the first impression or send. Anything decided after data arrives is labelled exploratory.

| Field | Content | Rule |
|---|---|---|
| Hypothesis | "Changing [element] from [A] to [B] will increase [metric] because [reason]" | One hypothesis per test; the reason comes from evidence, not hope. |
| Randomisation unit | Person, account, phone number, email address, session or geography | The unit that is split must be the unit that is counted; do not split people and count sessions. |
| Allocation | Planned split, e.g. 50/50 or 90/10 | Needed for the SRM check (section 3). |
| Primary metric (one) | The decision metric, with its exact definition and data source | Chosen before launch; never swapped for whichever metric "won". |
| Guardrail metrics | Metrics that must not get worse (section 4) | Each with a tolerance, e.g. "complaints not above control + 0.5 percentage points". |
| Minimum detectable effect (MDE) and sample | Smallest effect worth acting on, and the sample per arm it needs (section 2) | If the sample is out of reach, redesign before launch. |
| Horizon and stopping rule | Fixed end date or planned interim looks (section 5) | Written before launch. |
| Decision rule | What result leads to ship, iterate, kill or rerun | Numeric; includes what an inconclusive result means. |
| Exclusions | Who is excluded (staff, existing customers, suppressed contacts) and why | Applied equally to all arms. |

Store the record with the test number in the tracking sheet. A test with no pre-registration record may still be informative, but it is reported as exploratory and cannot be the sole basis for a standardisation decision.

## 2. Minimum detectable effect and power

- Decide the MDE from the business case first: the smallest lift that would change a decision or pay for itself (use the practical-significance filter in [testing method](testing-method.md)).
- Conventional design values: 5% two-sided significance and 80% power. They are conventions, not laws; state them.
- Rule of thumb for sample per arm at those values (a widely used approximation): n ≈ 16 × variance ÷ (MDE)². For a conversion rate p, variance ≈ p × (1 − p).
- Worked example: a landing page converts 3% of visitors. To detect an absolute lift of 0.6 percentage points (3.0% to 3.6%, a 20% relative lift), n ≈ 16 × 0.03 × 0.97 ÷ 0.006² ≈ 12,900 visitors per arm. A Kampala SME with 2,000 visitors a month cannot run this test in a sensible window.
- What to do when the sample is out of reach: test bigger differences (a new offer, not a new button colour); use a higher-traffic metric earlier in the funnel as a leading indicator and say so; pool three rounds of the same test type (directional, per the small-account rule in the parent skill); or do not test and decide on judgement, recorded as such.
- Never compute power after the fact to explain away a null result; an inconclusive result is reported as inconclusive.

## 3. Sample-ratio-mismatch (SRM) check

An SRM is a gap between the planned allocation and the observed counts that is too large to be chance. It usually means the split, the tracking or the delivery is broken, and it invalidates the comparison until explained.

Procedure (run before reading any outcome metric):

1. Take the observed count of randomisation units in each arm (e.g. contacts assigned, visitors bucketed).
2. Compute the expected count per arm from the planned allocation and the total.
3. Run a chi-square goodness-of-fit test: χ² = Σ (observed − expected)² ÷ expected, with (arms − 1) degrees of freedom. Any spreadsheet can do this (`CHISQ.TEST` in Google Sheets or Excel, with the observed and expected ranges).
4. House threshold: treat p < 0.001 as an SRM. The strict threshold keeps false alarms rare; it is an engine convention, not a platform rule.
5. If SRM: do not read the outcome. Look for the cause (a tag firing in one arm only, a redirect that loses visitors, bots, a broadcast list truncated by a send limit, a filter applied after assignment), fix it and rerun.

Worked example: 10,000 WhatsApp contacts split 50/50; arm A received 5,210, arm B 4,790. Expected 5,000 each: χ² = (210² + 210²) ÷ 5,000 = 17.6, p ≈ 0.00003. SRM: find out why 420 more contacts landed in A before reading any result.

Where SRM applies. It applies whenever the team controls or can see the assignment counts: landing-page split tests, email and SMS splits, WhatsApp broadcast splits, lifecycle holdouts, and geo tests with planned market lists. In platform-run ad A/B tests (for example Meta Experiments) the platform assigns people and reports reach, not assignment counts; unequal reach can reflect auction delivery rather than broken randomisation. There, record SRM as `not assessed`, keep budgets and schedules identical across arms, and rely on the platform's own split method as stated on its live help page.

## 4. Guardrail metrics

Guardrails protect the business and the audience while a primary metric is optimised. Pick two to four per test and set a tolerance before launch.

| Guardrail family | Examples |
|---|---|
| Trust and harm | Complaints, unsubscribes or opt-outs, "report" or "hide" actions, WhatsApp blocks, negative comment rate |
| Quality | Lead-to-customer rate, refund or no-show rate, average order value |
| Experience | Page load time on a mid-range Android phone, form errors, accessibility checks |
| Data integrity | SRM result, tracking coverage, share of conversions with unknown source |

A variant that breaches a guardrail tolerance is rejected or rolled back whatever its primary-metric lift (this extends the parent skill's guardrail decision row).

## 5. Peeking and stopping rules

- Repeatedly checking a fixed-horizon test and stopping at the first "significant" reading inflates false positives well above the stated significance level. The parent skill's rule stands: run to the planned end.
- Allowed exceptions, written before launch: a guardrail breach (stop for harm, not for success); a pre-planned interim look using a method designed for it (a sequential or group-sequential design, or a platform feature that states it corrects for continuous monitoring); a data-integrity failure such as SRM.
- Platform "winner" badges shown mid-test are not a stopping rule.
- Record every interim look in the Notes column with date and reason.

## 6. Lifecycle holdout groups (testing side)

A holdout measures what a lifecycle programme (welcome series, cart reminder, WhatsApp re-engagement, SMS reminders) adds over doing nothing. The email and lifecycle build belongs to [07-email-marketing-strategy](../../../pipeline/07-email-marketing-strategy/SKILL.md); this section owns the experiment design.

1. Randomly assign a fixed share of eligible contacts to a holdout that receives no message from the programme being measured. The share is a trade-off between measurement precision and forgone revenue; size it with section 2, not by habit.
2. Assign at the person level (one phone number or email address), once, and keep the holdout stable for the whole measurement window.
3. Never hold out legally required, transactional or safety messages (receipts, delivery notices, account security, consent confirmations); holdouts apply to marketing messages only.
4. Measure the outcome for both groups from a source the programme does not control (sales records, mobile-money receipts, CRM orders), not from message clicks.
5. Run the SRM check on the group sizes at the start and at read-out; contacts who opt out mid-window stay in their assigned group for analysis.
6. Report incremental effect = outcome rate in the messaged group − outcome rate in the holdout, with its uncertainty, and the absolute number of extra outcomes per 1,000 contacts.
7. Personal data: the holdout uses the same lawful basis as the programme; route consent and direct-marketing questions to the legal and market release gate.

For paid-media incrementality (geo tests, conversion lift) use `advertising-attribution-and-measurement`; this section covers owned-channel holdouts only.

## Sources

- Kohavi, R., Tang, D. and Xu, Y. (2020) *Trustworthy Online Controlled Experiments*, Cambridge University Press (concept input for pre-registration, SRM, guardrails, peeking and power; not reproduced).
- Register IDs: none; the statistical methods are standard and the thresholds marked as house conventions are engine rules, not external claims.
