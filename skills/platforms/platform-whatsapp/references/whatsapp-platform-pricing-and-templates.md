# WhatsApp Business Platform pricing and templates

Read when a plan uses the WhatsApp Business Platform (Cloud API or Marketing Messages API through a Business Solution Provider) and needs message costs, template categories, the customer service window, the free entry point window from click-to-WhatsApp ads, opt-in wording or marketing-message limits. This file is the engine's single source of truth for WhatsApp Platform message pricing; other skills point here. Parent skill: [platform-whatsapp](../SKILL.md). Added in Social Kaizen S10 (29 Sep 2026).

Evidence status. Read live on 29 Sep 2026 from Meta for Developers, *Pricing on the WhatsApp Business Platform* (page marked "Updated: Sep 28, 2026", register `WHATSAPP-PRICING-2025`) and the USD rate cards linked from it (register `WHATSAPP-RATE-CARD-EA`). **Meta changes pricing on 1 October 2026**, two days after this check (see §4). Re-read the page and rate card before quoting any figure to a client, and date the quote. The WhatsApp Business **app** (free, on one phone) is not billed per message; this file applies only to the Platform.

## 1. Pricing model

- Since **1 July 2025** Meta charges **per delivered template message**, replacing conversation-based pricing. Rates depend on the template category and the recipient's country calling code (register `WHATSAPP-PRICING-2025`).
- Messages a customer sends to the business are never charged.
- Utility and authentication templates qualify for lower rates through monthly **volume tiers** decided by Meta, per market and category.
- From 2026 businesses on the Marketing Messages API can set a **max-price** per marketing message; Meta then charges that price or lower.

## 2. Template categories and when each is charged (position until 30 Sep 2026)

| Category | Typical use | Charged? |
|---|---|---|
| Marketing | Offers, launches, re-engagement, anything promotional | Charged when delivered (free only inside a free entry point window) |
| Utility | Order confirmation, delivery update, appointment reminder tied to a transaction the user started | Charged outside an open customer service window; **free inside an open window** (since 1 Jul 2025) |
| Authentication | One-time passcodes | Charged when delivered; the page names no in-window exemption (free only inside a free entry point window) |
| Service (non-template, free-form replies) | Answering a customer who wrote in | Free inside the window (since 1 Nov 2024) |

Templates are the only messages that can open contact outside a customer service window. Meta assigns the category on approval, and the business accepts the charge for the category applied at the time of use, so check that a "utility" draft does not contain promotional lines that get it recategorised as marketing.

## 3. Windows

- **Customer service window (CSW).** Opens for 24 hours when a user messages the business and resets with each new user message. Inside it, free-form replies are free and (until 30 Sep 2026) utility templates are free. After it closes, only templates can be sent.
- **Free entry point (FEP) window.** Opens when a user messages the business through a **click-to-WhatsApp ad** on the Android or iOS app (desktop and web are not supported) **and** the business replies within the customer service window. The page now states the FEP window "may remain open for up to 7 days", starting from the business's reply; while it is open, every message type is free. The window belongs to the business phone number and user pair, not to one Messaging account.
- **Correction to older engine text.** Earlier guidance, and the S10 benchmark row, describe a **72-hour** free window from click-to-WhatsApp ads **and Facebook Page call-to-action buttons**. The page read on 29 Sep 2026 says **up to 7 days** and names only click-to-WhatsApp ads; Facebook Page call-to-action entry is not mentioned and is `NOT_ASSESSED`. Use "up to 7 days, click-to-WhatsApp ads only" until the page changes.

## 4. Changes effective 1 October 2026 (published on the page)

- **Service messages become chargeable** per message at the same rate as utility and authentication in each market, with a **free monthly tier of 1,000 delivered service messages per business phone number** (no roll-over; group sends use one unit per delivered recipient). Without a payment method, service messages stop after the free tier.
- **Utility templates inside an open customer service window become chargeable**; there is no change to when they can be sent.
- Nine markets leave their "Rest of" regions to become standalone (none in East Africa; Morocco leaves "Rest of Africa").
- Plans that assumed "replies are free" must be re-costed from October 2026: estimate monthly service replies per number and compare with the 1,000 free tier.
- The page also announces pricing updates for "Meta Business Agent" from 1 August 2026; their terms were not read and are `NOT_ASSESSED`.

## 5. East Africa rates

Uganda (+256), Kenya (+254), Tanzania (+255) and Rwanda (+250) are all in Meta's **"Rest of Africa"** pricing region (register `WHATSAPP-RATE-CARD-EA`, read live 29 Sep 2026 from the USD rate cards linked on the pricing page).

| Rate card (USD, per delivered message) | Marketing | Utility | Authentication | Service |
|---|---|---|---|---|
| Effective 1 Jul 2026 (current on 29 Sep 2026) | 0.0225 | 0.0040 | 0.0040 | n/a (free) |
| Effective 1 Oct 2026 | 0.0225 | 0.0040 | 0.0040 | 0.0040 (after 1,000 free a month per number) |

These are Meta's list rates before volume tiers. A Business Solution Provider (for example Africa's Talking, WATI, Interakt or Twilio) usually adds its own fee or bills in another currency; ask for its written rate card and record both. Convert to UGX at the day's rate and date it; do not hard-code a UGX figure in a plan.

Worked planning example (illustrative, rate card of 1 Oct 2026): 2,000 opted-in contacts × 4 marketing templates a month = 8,000 × USD 0.0225 = USD 180 in Meta charges, before BSP fees; order updates sent as utility templates outside a window add USD 0.004 each.

## 6. Opt-in and marketing limits

- **Opt-in must name the business.** Meta's opt-in guidance, under the WhatsApp Business Messaging Policy (register `WHATSAPP-BUSINESS-POLICY`; opt-in page register `WHATSAPP-OPT-IN-2026`), requires the business to state clearly that the person is opting in to receive messages from it, to state the business's name, and to comply with applicable law. Opt-in may be collected off WhatsApp (website, SMS, IVR, paper, in person). Meta recommends separate opt-ins by message type and clear opt-out instructions. Uganda DPPA 2019 s.26 (`UG-DPPA-S26-DIRECT-MARKETING-2026`) and Kenya ODPC direct-marketing guidance (`KE-ODPC-DIRECT-MARKETING-2026`) also apply; political bulk messages in Kenya follow `KE-CA-POLITICAL-BULK-SMS-2017`.
- **Per-user marketing template limits.** WhatsApp limits how many marketing templates a user receives from businesses when engagement is low, adapting to the user's read rate and inbox volume (register `WHATSAPP-MARKETING-LIMITS-2026`). A blocked send returns error 131049; wait at least 24 hours before retrying. Messages sent inside a customer service window the user opened do not count. The limits apply in East Africa (only the EEA, UK, Japan and South Korea are excluded; +1 US numbers cannot receive marketing templates at all). No fixed number is published; treat undelivered marketing sends as a frequency signal, not a technical fault.

## 7. Planning rules

| Condition | Action |
|---|---|
| Most messages are replies to customers who wrote first | Keep them inside the 24-hour window; from 1 Oct 2026 budget for service replies above 1,000 a month per number |
| Click-to-WhatsApp ads drive the enquiries | Reply inside the window to open the free entry point window, and plan follow-ups inside its up-to-7-day span |
| Order and delivery updates | Use utility templates with no promotional lines; cost them as utility outside the window (and inside it from 1 Oct 2026) |
| Promotional broadcasts via the Platform | Cost every delivered marketing template; expect per-user limits to cut delivery to low-engagement contacts |
| A figure here is older than 91 days, or it is after a published change date | Re-read the pricing page and rate card before quoting |

## Sources

- `WHATSAPP-PRICING-2025` — Meta for Developers, Pricing on the WhatsApp Business Platform (read live 29 Sep 2026; page updated 28 Sep 2026).
- `WHATSAPP-RATE-CARD-EA` — Meta, USD rate cards effective 1 Jul 2026 and 1 Oct 2026, "Rest of Africa" row (read live 29 Sep 2026).
- `WHATSAPP-MARKETING-LIMITS-2026` — Meta for Developers, Per-user marketing template message limits (read live 29 Sep 2026).
- `WHATSAPP-OPT-IN-2026` — Meta for Developers, Get opt-in for WhatsApp (read live 29 Sep 2026).
- `WHATSAPP-BUSINESS-POLICY`, `UG-DPPA-S26-DIRECT-MARKETING-2026`, `KE-ODPC-DIRECT-MARKETING-2026`, `KE-CA-POLITICAL-BULK-SMS-2017` — existing register records.
