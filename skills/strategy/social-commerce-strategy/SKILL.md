---
name: social-commerce-strategy
description: 'Use when a business sells straight from social media: product catalogue, WhatsApp orders, Instagram DM selling, Mobile Money payment, delivery and shoppable posts; produces the social shop set-up with order flow, payment confirmation and DM scripts; not for diagnosing why clicks do not become orders (use `playbook-post-click-strategy`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Commerce Strategy

Makes conversation-led commerce work: a customer sees a product on social media, messages on WhatsApp, pays by Mobile Money (MTN MoMo or Airtel Money) and receives delivery, with no formal e-commerce website needed. The consultant's job is to make that path faster, more consistent and more professional from discovery to payment confirmation.

<!-- dual-compat-start -->
## Use When

- We sell through Facebook, Instagram, TikTok or WhatsApp and need a catalogue, pricing and ordering flow that works.
- Customers pay with MTN MoMo, Airtel Money or M-Pesa and we need a payment confirmation and fulfilment routine.
- Orders arrive in scattered chats; we need a simple order tracker and delivery process.
- Instagram DMs ask "how much?" and go cold: script the opener, qualifying questions, UGX offer and objection replies, then move buyers to WhatsApp to close.
- Product posts must sell: shoppable content, product videos and margin-safe pricing.

## Do Not Use When

- `playbook-post-click-strategy` for finding where visitors drop off between the click and the order.
- `playbook-social-selling` for relationship selling, employee advocacy and high-value B2B outreach.
- `ecommerce-export-marketing-advisory` for reaching buyers in other countries.
- Stop before changing a live catalogue, prices or payment settings, or messaging customers, without explicit client authority; deliver the draft for approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry, country/city and product type (physical, digital or service; perishable or not; value per transaction) | Client owner | Yes | Stop; ask the [intake questions](references/social-shop-setup-and-operations.md) before designing an order flow. |
| Current sales channels and active platforms (Facebook, Instagram, TikTok, WhatsApp Business) | Client and account review | Yes | Default to WhatsApp Business plus one discovery platform and label it provisional. |
| Payment infrastructure in place (MTN MoMo, Airtel Money, Pesapal, Paystack, Flutterwave, bank transfer, cash on delivery) | Client owner | Yes | Recommend MTN MoMo and Airtel Money as the first step; mark fee figures to confirm with each provider. |
| Fulfilment capacity (own delivery, self-pickup, delivery partner; Kampala and upcountry) | Client operations | Yes | Plan self-pickup plus one named Kampala courier; mark upcountry delivery `not assessed`. |
| Product costs, prices and order history | Client records | Conditional | Apply the 3X rule as a check only; mark margin and basket analysis `not assessed`. |
| Primary goal (order volume, less friction, upcountry reach, cash to digital) | Client owner | Yes | Ask; do not optimise for volume by default. |

## Workflow

1. Confirm the intake answers and that the sale can be completed or handed off from social channels; stop and route to `playbook-post-click-strategy` if the question is why clicks do not become orders.
2. Map the journey with RACE (Chaffey and Ellis-Chadwick, 2022): Reach, Act (WhatsApp enquiry or catalogue view), Convert (Mobile Money payment confirmed), Engage (follow-up and repeat order).
3. Set up platform commerce per platform: catalogue for discovery and price transparency, WhatsApp as checkout, TikTok videos with a WhatsApp CTA.
4. Choose payment methods and write the six-step payment confirmation workflow and the WhatsApp order template.
5. Design the order tracker and the scaling trigger, then the delivery zones, fees and partners.
6. Plan commerce content (five posts per week on the primary platform, three on the secondary, every post with a CTA) and, where sales start in Instagram DMs, the 5-stage DM sequence from [DM conversation selling](references/dm-conversation-selling.md).
7. Check pricing, product selection, buyer tiers and a point of difference with [pricing, conversion and differentiation](references/pricing-conversion-and-differentiation.md).
8. Review the set-up against the Quality Standards and the anti-slop gate; correct any failed item and rerun the check, then hand over as a draft for approval before any live catalogue, price or payment change.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Social shop set-up per platform (catalogue, links, auto-replies, Stories and TikTok CTAs) | Client owner or whoever runs the accounts | States the Uganda checkout limitation and routes every purchase to WhatsApp. |
| Order flow: WhatsApp order template and six-step payment confirmation workflow | Staff handling orders | Numbered steps a business owner can follow immediately; the order number is shared at payment confirmation. |
| Order tracker with columns and scaling trigger | Owner and dispatch staff | All ten columns defined; the move to a tool is set at 20+ orders per day. |
| Commerce content plan and DM scripts | Content lead; sales staff | At least five commerce content types, each with why it works in EA; every post carries a specific CTA. |
| Pricing, buyer-tier and differentiation notes | Client owner | 3X rule and 7 product selection criteria applied; one-time, repeat and whale tiers each have an action. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Payment provider and fee register | Table: provider, fee, date checked | Fees are shown as approximate and dated; unverified fees are marked. |
| Platform availability check | Table: feature, country, date checked | Checkout, TikTok Shop and Link sticker availability recorded with the check date. |
| Assumption register | Table in the set-up document | Order volumes, margins and delivery fees without client data are labelled. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Changing a live catalogue, prices or payment settings, or messaging customers, waits for that authority; customer photos and testimonials need the customer's permission.

## Degraded Mode

Without the client's payment and fulfilment set-up, return the narrowest qualified result and mark the affected checks `not assessed`. A WhatsApp order template, a payment confirmation workflow built on MTN MoMo and Airtel Money, an order tracker and a content plan can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The sale can be completed or handed off from social channels | Design the order-to-payment workflow before scaling content | Demand generation overwhelms an informal order process |
| Sales start in Instagram DMs for a service or consultant offer | Script the 5-stage DM sequence and WhatsApp move per [DM conversation selling](references/dm-conversation-selling.md) | Unscripted, pushy or automated DMs that lose warm prospects |
| The client wants Facebook Shop or Instagram Shopping checkout, or TikTok Shop, in Uganda | Present Shop and Shopping as a catalogue and price list, route purchases to WhatsApp, and do not set up TikTok Shop (not available in Uganda as of 2026) | Promising a checkout that does not exist |
| Click-to-WhatsApp ads feed the WhatsApp order flow on the Business Platform (API) | Reply inside the 24-hour window so the free entry point window opens (up to 7 days, all messages free; ad-originated chats on the Android or iOS app only), and close the order within it (register `WHATSAPP-PRICING-2025`) | Paying for follow-ups the ad entry made free, or losing the lead after the window |
| A first-time or unknown customer asks for cash on delivery | Decline; reserve cash on delivery for trusted repeat customers or orders below UGX 50,000 | Non-collection losses |
| Orders exceed 20 per day | Move from the Google Sheet to an order management tool | Missed deliveries and payment disputes |
| Annual turnover approaches UGX 150 million | Flag VAT registration with the Uganda Revenue Authority and recommend receipt-generating payment links | Tax non-compliance |
| A product fails the 3X rule or the UGX 90,000 minimum retail price | Re-price, bundle or drop it from the range | Selling at a loss after delivery costs |
| A post says "DM for price" or claims false scarcity | State the price; use accurate stock counts only | Lost trust in a relationship-led market |

## Quality Standards

- EA payment infrastructure is covered with provider names, approximate fees and a clear recommendation, with MTN MoMo and Airtel Money as the primary methods and the reason stated.
- The WhatsApp order workflow is a numbered, step-by-step process a business owner can follow immediately.
- The Facebook Shop and Instagram Shopping checkout limitation in Uganda is noted with the WhatsApp alternative.
- The order system has specific column headings and the 20+ orders per day scaling trigger.
- At least five commerce content types are listed with why each works in EA.
- EA delivery partners (SafeBoda, Glovo, DHL Uganda, Posta Uganda) are named and upcountry fulfilment is addressed; the UGX 150 million VAT threshold and trust signals are flagged.
- Product decisions apply the 3X rule and the 7 selection criteria; buyers are segmented into one-time, repeat and whale tiers with an action each.
- The brand intangible type is identified and a Soleness statement produced; the full checklist is in [pricing, conversion and differentiation](references/pricing-conversion-and-differentiation.md).

## Anti-Patterns

- Treating the lack of in-app checkout as a barrier. Fix: make WhatsApp the checkout with a standard order process, consistent response times and reliable payment confirmation.
- Processing an order before payment is confirmed. Fix: ask for the Mobile Money screenshot and confirm receipt first.
- Hiding prices behind "DM for price". Fix: state the price in the caption or on-screen text.
- Deceptive scarcity ("Only 5 left" when stock is plentiful). Fix: post accurate stock counts only.
- Spreading content and paid spend evenly across the range. Fix: concentrate on the top 20% of products that earn 80% of revenue.
- Ignoring scam fears among Ugandan buyers. Fix: build trust signals: a verified Page, a Google Business Profile, visible testimonials and a consistent posting history.
- Competing on price alone. Fix: choose a brand intangible and write a Soleness statement; route the full work to `brand-strategy-and-distinctive-assets`.

## References

- [Social shop set-up and operations](references/social-shop-setup-and-operations.md): read when running the intake, setting up platform commerce, choosing payment methods, writing the order and payment workflow, planning commerce content, building the order tracker or applying EA delivery, VAT and trust rules.
- [Pricing, conversion and differentiation](references/pricing-conversion-and-differentiation.md): read when setting prices, choosing products, matching traffic temperature and buyer modality, reducing friction, segmenting buyers or choosing a point of difference.
- [DM conversation selling](references/dm-conversation-selling.md): read when prospects arrive through Instagram DMs and must be qualified and moved to WhatsApp to close.
- [Commerce media and marketplaces](references/commerce-media-and-marketplaces.md): read when selling or advertising on Jumia, Jiji or a retail media network, checking vendor-reported sales against IAB/MRC retail-media guidelines and incrementality, sizing mobile-money checkout, or screening a payments-licence question.
- [`platform-whatsapp`](../../platforms/platform-whatsapp/SKILL.md): read when configuring the WhatsApp Business catalogue, broadcasts and auto-replies; its [Platform pricing and templates](../../platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md) reference: read when costing API messages or the click-to-WhatsApp free entry point window.
- [`playbook-post-click-strategy`](../../playbooks/playbook-post-click-strategy/SKILL.md): read when visitors drop off between the click and the order.
- [`brand-strategy-and-distinctive-assets`](../brand-strategy-and-distinctive-assets/SKILL.md): read when the shop needs full positioning, naming, packaging and community work (e-commerce content in its [e-commerce differentiation](../brand-strategy-and-distinctive-assets/references/ecommerce-differentiation.md) reference).
- [`east-african-english`](../../language/east-african-english/SKILL.md): read when writing catalogue descriptions, WhatsApp templates and CTA copy.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting posts, scripts and catalogue copy.
<!-- dual-compat-end -->
