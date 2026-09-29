# Test rigour for paid creative tests: pre-registered card, guardrails and SRM applicability

Read when a paid creative or message test must be decision-grade: before launch (to lock the card), when a platform shows an early "winner", or when results look odd. The statistics (sample size, power, the SRM calculation, stopping rules, holdouts) live in [trustworthy experiments](../../../meta-analytics-ops/meta-testing-framework/references/trustworthy-experiments-srm-power-holdouts.md); this file applies them to ad accounts.

## 1. Pre-registered creative test card

Extend the test card in [test design and reading](test-design-and-reading.md) with these fields, dated and approved before launch:

| Field | Paid-creative example |
|---|---|
| Hypothesis and reason | "Opening on the product in hand in the first two seconds, instead of the presenter, will lower cost per qualified WhatsApp lead because recall checks show weak brand linkage." |
| What the concept screen predicted | The pre-test or concept-screen reading from `creative-brief-and-big-idea`, so the test also checks the prediction |
| Split method | Platform A/B test feature, separate ad sets with identical audiences and budgets, or geo split; state which |
| Primary metric | One, defined from the export column it comes from |
| Guardrails and tolerances | e.g. frequency not above control + 0.5; negative feedback not above control; lead-to-sale rate not below the line; brand-linkage playback not below control |
| MDE and the result count needed | From the power rule of thumb; if the budget cannot buy it, test a bigger difference |
| Horizon | Fixed dates covering at least one weekly cycle |
| Stop-for-harm rule | Which guardrail breach stops the test early |
| Decision rule | Scale, iterate, kill or rerun, with the numeric line |

Record the hypothesis in the client's words too; a test the client cannot restate is not ready.

## 2. SRM and delivery balance in ad platforms

- Where the team controls assignment (landing-page splits behind one ad, click-to-WhatsApp keyword splits, SMS or email follow-up splits, geo lists), run the SRM check before reading results.
- In platform-run A/B tests the platform assigns people and reports reach, impressions and spend. Unequal reach between arms may be auction delivery, not broken randomisation. Record SRM as `not assessed`, confirm spend and schedule were equal, and note any delivery gap larger than the budget split as a caveat.
- Separate ad sets without the platform's split feature can share audience members; label such tests "unrandomised comparison" and read them as directional.
- Check the platform's current A/B test method and minimums on its live help page, with the date, before stating them to the client.

## 3. Reading order at the end of the window

1. Integrity: tracking coverage, SRM result or `not assessed` reason, spend parity.
2. Guardrails: any breach means reject or roll back, whatever the primary lift.
3. Primary metric against the pre-registered line and MDE.
4. Downstream quality and segments (per the existing reading steps).
5. Prediction check: did the pre-test or concept-screen favourite win? Log the answer; over time it shows whether the pre-test method earns its cost.

## Sources

- Kohavi, R., Tang, D. and Xu, Y. (2020) *Trustworthy Online Controlled Experiments*, Cambridge University Press (concept input, applied through the meta-testing-framework reference).
- Register IDs: none; platform split behaviour is to be checked live per test and is not asserted here.
