# Data-protection and platform checks for outreach

Read before any contact list is used, matched or messaged. Parent skill: [biz-dev-lawful-prospecting-outreach](../SKILL.md). This is a screening checklist, not legal advice. Facts below are taken from the Kaizen currentness register checked on 2026-09-23 (claim IDs in brackets) and the engine source register (`docs/source-registers/source-register.json`: UG-DPPA-2019, UG-DPPR-2021, UG-PDPO-ORG, KE-DP-GENERAL-2021, RW-DPP-2021, TZ-PDPA, TZ-PDPR-2023, WHATSAPP-BUSINESS-POLICY). Re-verify before client release; anything not listed is a check to run.

## Uganda (register PL-01, checked 2026-09-23)

- Every data collector, processor and controller must register with the Personal Data Protection Office unless exempted by gazette notice; registration is valid for 12 months (Data Protection and Privacy Regulations 2021). Confirm current fees with the PDPO.
- Processing personal data without prior consent (s.7) is an offence; collecting a list therefore needs consent or another basis the Act permits.
- **Direct marketing (s.26) is an objection right:** a person may, by written notice, require the controller to stop processing for direct marketing; the controller must respond within 14 days.
- **Do not state that the Act "requires opt-in for all marketing".** It has no ePrivacy-style opt-in rule, but the s.7 consent requirement applies to collecting the data.
- The Act now appears as Cap. 97 in the 2023 revised laws.

## Kenya (register PL-02, checked 2026-09-23)

- Data Protection (General) Regulations 2021, regulations 14–18: using non-sensitive data for direct marketing needs the data collected from the person, the purpose notified, consent, and a **simplified, free opt-out**. Read the conditions cumulatively.
- The right to object to direct marketing is **absolute**.
- Direct-marketing email must not conceal the sender's identity and must give a valid opt-out address.
- Registration Regulations 2021: small entities (turnover under KES 5M **and** fewer than 10 employees) are exempt **unless** listed in the Third Schedule, which includes businesses wholly or mainly in direct marketing; certificates last 24 months.

## Rwanda and Tanzania (register PL-03, PL-04 — partial)

- Rwanda: controllers and processors must register with the National Cyber Security Authority. Direct-marketing provisions are **not assessed**.
- Tanzania: the Personal Data Protection Act 2022 is administered by the Personal Data Protection Commission and requires registration. Direct-marketing provisions and the reported enforcement date are **not assessed**.

## Other markets

UK/EU prospects: GDPR and PECR apply; US prospects: CAN-SPAM. These are not in the Kaizen register; check current regulator guidance before use.

## Platform checks

- **WhatsApp Business:** business-initiated messages generally require prior opt-in and approved templates. Confirm the current WhatsApp Business Messaging Policy (source register WHATSAPP-BUSINESS-POLICY) before any first-contact use.
- **LinkedIn and Meta messaging:** automation, mass friend requests and scraping breach platform terms; check the current user agreement before any tool is used.
- **Email bulk-sender rules:** check current mailbox-provider sender requirements before sending at volume.

## Per-list checklist

| Check | Pass condition |
|---|---|
| Source recorded | Where, when and how each record was obtained |
| Lawful basis | Consent or another documented basis for each market |
| Registration | Client (and agency as processor) registered where required |
| Privacy notice | States purpose, identity and opt-out route |
| Opt-out in every message | Free, simple, honoured within the legal window |
| Suppression list | Checked before every send; objections never re-contacted |
| Purpose limitation | Data used only for the notified purpose |
| No list rental or resale | No renting, selling or sharing without a lawful basis |
| Retention | Records deleted when no longer needed |

Any failed check stops sending for that list. Missing evidence is `not assessed`, never a pass.
