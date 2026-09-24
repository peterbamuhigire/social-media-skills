# Conversion events and attribution models

Read when defining what counts as a result and choosing how credit is assigned. Parent: [advertising-attribution-and-measurement](../SKILL.md).

## 1. Conversion event specification

| Field | Content |
|---|---|
| Event name | e.g. `lead_whatsapp_started`, `form_submit`, `booking_confirmed`, `purchase` |
| Business meaning | What happened and why it matters |
| Trigger | Page, button, server event, CRM status change, POS code |
| Source of truth | CRM, POS, mobile-money record, booking system |
| Value | Fixed, dynamic (order value) or none |
| Deduplication | Event ID shared by browser and server events; one purchase counted once |
| Consent dependency | Fires only with consent where required (EEA/UK/CH: Consent Mode v2, register CW-10) |
| Owner | Named person for maintenance |

Hierarchy: one primary (value) event; two to four micro-conversions that predict it (e.g. WhatsApp chat started, price list requested, booking page viewed). Optimise campaigns on the deepest event with enough volume; report the value event.

## 2. Offline and WhatsApp conversions

- Unique keywords or codes per ad and medium; staff apply chat labels on first reply.
- "How did you hear about us?" field on forms and at the till.
- Mobile-money or POS reference numbers linked to the enquiry record where lawful.
- Offline conversion import to ad platforms only with consent, lawful basis and authority; check current platform documentation for the method.

## 3. Attribution models (describe the bias every time)

| Model | Credit rule | Bias |
|---|---|---|
| Last click | All credit to the final click | Over-credits search, retargeting and brand terms |
| First click | All credit to the first click | Over-credits discovery channels |
| Linear | Equal credit to every touch | Ignores which touch mattered |
| Time decay | More credit to touches nearer conversion | Under-credits awareness |
| Position-based | Most credit to first and last, remainder spread | Arbitrary weights |
| Data-driven | Credit estimated by the platform's model from observed paths | Model is proprietary; availability, defaults and thresholds change — check current platform documentation |
| Platform self-reporting | Each platform credits its own touch (click and view windows) | Platforms double-count the same sale |

Rules:
- Use one model for daily optimisation and say which.
- Never add platform-reported conversions across platforms.
- Use incrementality evidence for budget shifts between channels.

## 4. Demand harvesting vs demand generation

Search and retargeting harvest demand that already exists; social video, radio and outdoor generate it. Last-click models favour harvesters. Judge generators on reach in target, brand lift, search-demand change for the brand name, and incremental tests (Weinberg and Mares (2014) *Traction*, S-curves Publishing, on indirect response).

## 5. Consent-aware measurement

- EEA, UK and Switzerland traffic with Google tags: Consent Mode v2 with `ad_user_data` and `ad_personalization` via a consent platform; advanced mode enables modelling, basic mode blocks tags until consent (register CW-10, checked 2026-09-23). This is not a legal requirement in Uganda or Kenya but affects EU-facing campaigns.
- GA4 is Google's current analytics product; Universal Analytics data is no longer available (CW-10).
- Uganda: processing personal data needs consent (DPPA s.7); Kenya: consent plus a free, simple opt-out for direct marketing (register PL-01, PL-02). Route legal questions to counsel.
