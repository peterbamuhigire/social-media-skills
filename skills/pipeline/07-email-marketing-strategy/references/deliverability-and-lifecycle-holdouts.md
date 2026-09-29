# Deliverability and lifecycle holdouts

Read when an email programme will send marketing or subscribed mail at volume, when inbox placement or spam complaints are in question, when a new domain or IP must be warmed up, or when the client asks whether welcome, win-back or other lifecycle flows actually add revenue. Parent skill: [07-email-marketing-strategy](../SKILL.md). Added in Social Kaizen S10 (29 Sep 2026).

Evidence status. Mailbox-provider rules below were read live on 29 Sep 2026 (registers `GMAIL-SENDER-GUIDELINES`, `GMAIL-SENDER-FAQ-2026`, `YAHOO-SENDER-REQUIREMENTS`). Providers change enforcement without notice; re-check the pages before any build and date the check in the strategy's benchmark and platform-feature register. This is a planning checklist, not a DNS or legal instruction; DNS changes are live account changes and need the client's authority and its domain administrator.

## 1. Mailbox-provider sender rules (Gmail and Yahoo)

Gmail's Email sender guidelines apply to every sender; a stricter set applies to **bulk senders**, defined as those sending more than 5,000 messages a day to Gmail accounts. Gmail's FAQ states that bulk-sender status, once assigned, is permanent: dropping below 5,000 a day later does not remove it (register `GMAIL-SENDER-FAQ-2026`). Plan every client as if it will cross the line.

| Requirement | All senders (Gmail) | Bulk senders (Gmail) | Yahoo (bulk) | Register |
|---|---|---|---|---|
| Sender authentication | SPF **or** DKIM for the sending domain | SPF **and** DKIM | SPF and DKIM | `GMAIL-SENDER-GUIDELINES`, `YAHOO-SENDER-REQUIREMENTS` |
| DMARC | Not required | A DMARC record for the sending domain; the policy may be `p=none` | A valid DMARC policy of at least `p=none`, and DMARC must pass | same |
| Alignment | — | For direct mail, the From: header domain aligns with the SPF domain or the DKIM domain (organisational-domain alignment, per the FAQ) | From: domain aligns with SPF or DKIM | `GMAIL-SENDER-FAQ-2026` |
| Unsubscribe | — | Marketing and subscribed messages support one-click unsubscribe (List-Unsubscribe headers, RFC 2369 and RFC 8058) plus a clearly visible unsubscribe link in the body | One-click unsubscribe for marketing and subscribed messages; RFC 8058 POST method "highly recommended"; honour unsubscribes within 2 days | same |
| Unsubscribe processing time | — | Gmail FAQ **recommends** fulfilling requests within 48 hours | **Required**: within 2 days | same |
| Spam rate | Below 0.30 % in Postmaster Tools | Keep below 0.10 % and never reach 0.30 % | Below 0.3 % (inbox-delivered mail) | same |
| DNS | Valid forward and reverse DNS (PTR) for sending IPs | same | same | same |
| Transport and format | TLS for transmission; messages formatted to RFC 5322; do not impersonate Gmail From: headers | same | RFC 5321 and 5322 | same |

Enforcement timeline as Gmail's FAQ states it on 29 Sep 2026: requirements began in **February 2024**; spam-rate consequences (loss of mitigation support above 0.3 %) from **June 2024**; from **November 2025** Gmail is ramping up enforcement, including rejecting non-compliant traffic. Yahoo states that enforcement began in February 2024. Anything later than these dates is `NOT_ASSESSED` until re-read.

## 2. Deliverability set-up checklist for the strategy

1. Send from the client's own domain (for example `news.clientname.co.ug`), never from a free webmail address; mail "from" a Gmail or Yahoo address through a third-party platform fails DMARC alignment.
2. Ask the email platform (Mailchimp, Brevo or other) for its SPF include and DKIM keys and record who adds them to DNS; a Ugandan `.ug`, Kenyan `.ke` or Tanzanian `.tz` domain is often managed by a local registrar or web host, so name that contact as the owner.
3. Publish DMARC at `p=none` with a reporting address first; move towards `p=quarantine` only after reports show every legitimate sending service passing. The move is the client's decision.
4. Confirm the platform adds List-Unsubscribe and List-Unsubscribe-Post headers to marketing mail, and that unsubscribes sync to the suppression list within two days (Yahoo's requirement; stricter than Gmail's 48-hour recommendation, and the same in practice).
5. Register the sending domain in Google Postmaster Tools and review spam rate weekly during warm-up, monthly afterwards; set the internal alarm at 0.10 %, not 0.30 %.
6. Keep the consent record the parent skill requires (Uganda DPPA 2019 s.26 on direct marketing, register `UG-DPPA-S26-DIRECT-MARKETING-2026`; Kenya ODPC direct-marketing guidance, `KE-ODPC-DIRECT-MARKETING-2026`). Authentication does not make an unconsented list lawful.

## 3. List hygiene and warm-up

- **Hygiene.** Remove hard bounces at once; suppress addresses with no open or click in the reactivation window set by [win-back-and-reactivation](win-back-and-reactivation.md) rather than deleting them; never buy, rent or scrape lists; use double opt-in for new sign-ups ([lead-magnets-and-list-building](lead-magnets-and-list-building.md)). Treat opens as directional because of Apple Mail Privacy Protection.
- **Complaint prevention.** Name the business and the reason for the email in the first line; keep the promised cadence; make unsubscribe easier to find than the spam button.
- **Warm-up of a new domain or dedicated IP.** Start with the most engaged, most recently consented segment, grow volume in steps only while complaint and bounce rates stay low, and hold or step back when they rise. No fixed step size is stated by Gmail or Yahoo; take the platform's own warm-up guidance and record it as vendor guidance. Shared-IP plans on Mailchimp or Brevo carry the platform's reputation, so warm-up there is mainly domain reputation.

## 4. East Africa notes

- Many Ugandan and Kenyan subscribers use Gmail addresses, so Gmail's rules decide most inbox placement; the share of Gmail in any client list is `NOT_ASSESSED` until the client's own export is counted by domain (count it, do not assume it).
- Local ISP or corporate mail domains (for example government, university or telecom addresses) behave differently and often filter harder; report their bounce and complaint rates separately.
- Clients who send from a web host's shared mail server in Kampala or Nairobi often lack DKIM and a correct PTR record; route bulk sends through an email service provider that signs mail, or have the host fix DNS before the first campaign.
- Where email reach is weak, the lifecycle map should name WhatsApp or SMS as the consented fallback ([`playbook-sms-whatsapp-marketing`](../../../playbooks/playbook-sms-whatsapp-marketing/SKILL.md)), not a bigger email send.

## 5. Lifecycle holdout groups

A lifecycle flow (welcome, post-purchase, win-back, abandoned basket) always looks profitable in platform reports because it mails people who were likely to buy anyway. A holdout answers the only useful question: what extra revenue does the flow cause?

Method (experiment design as in Kohavi, Tang and Xu (2020) *Trustworthy Online Controlled Experiments*, Cambridge University Press; the incrementality method hierarchy in the IAB and IAB Europe commerce-media guidelines ranks randomised tests and holdouts as the strongest causal evidence, register `IAB-INCREMENTAL-COMMERCE-MEDIA-2025`):

1. **Define the estimand first.** For example: incremental revenue per eligible subscriber over 90 days from the win-back flow.
2. **Randomise at subscriber level before entry.** Assign each newly eligible subscriber at random (hash of subscriber ID) to receive the flow or to a holdout that receives nothing from that flow; keep all other mail identical for both groups.
3. **Make the holdout persistent.** The same people stay held out for the whole test so the comparison is not contaminated; re-draw the holdout only between test periods.
4. **Size and duration.** Choose the holdout share from a power calculation with [`meta-testing-framework`](../../../meta-analytics-ops/meta-testing-framework/SKILL.md), given list size, baseline conversion and the smallest lift worth acting on. Size by power, not habit: 5–10 % of eligible subscribers is only the engine's starting input to that calculation (not an industry figure), held out held out for at least one full purchase cycle and never less than 8 weeks. If the power calculation shows the list cannot detect the smallest lift worth acting on, say so and run the flow without an incrementality claim.
5. **Measure on business data.** Compare orders and revenue per eligible subscriber in each group from the client's sales records or order tracker (mobile-money and WhatsApp orders included), not platform-attributed revenue.
6. **Report.** Incremental revenue, confidence interval, holdout share, dates and any contamination (for example holdout members reached by the same offer on WhatsApp). A non-significant result is reported as "no detectable lift at this size", not as zero effect.
7. **Ethics and consent.** Holding someone out of a marketing flow is usually low-risk (screen it with the legal and market release gate; this is not legal advice); never hold people out of transactional or service messages (order confirmations, receipts, password resets).

## Sources

- `GMAIL-SENDER-GUIDELINES` — Gmail Help, Email sender guidelines (read live 29 Sep 2026).
- `GMAIL-SENDER-FAQ-2026` — Gmail Help, Email sender guidelines FAQ (read live 29 Sep 2026).
- `YAHOO-SENDER-REQUIREMENTS` — Yahoo Sender Hub, Sender best practices (read live 29 Sep 2026).
- `IAB-INCREMENTAL-COMMERCE-MEDIA-2025` — IAB and IAB Europe, Guidelines for Incremental Measurement in Commerce Media (Nov 2025).
- `UG-DPPA-S26-DIRECT-MARKETING-2026`, `KE-ODPC-DIRECT-MARKETING-2026` — consent for direct marketing.
- Concept input: Kohavi, R., Tang, D. and Xu, Y. (2020) *Trustworthy Online Controlled Experiments*, Cambridge University Press.
