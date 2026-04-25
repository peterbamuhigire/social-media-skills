---
name: platform-google-business-profile
description: Generates a complete Google Business Profile (GBP) strategy and optimisation plan for a client, covering setup, verification, profile completeness scoring, photo strategy, posts, Q&A management, review generation, performance metrics, and local SEO integration. Invoke this skill when a client needs to create or improve their GBP presence, when local search visibility or Google Maps discoverability is a goal, or when GBP is identified as a priority channel for a Uganda/East Africa-based SME.
---
# Google Business Profile Strategy and Optimisation Plan

<!-- dual-compat:start -->
## Use when
- Generates a complete Google Business Profile (GBP) strategy and optimisation plan for a client, covering setup, verification, profile completeness scoring, photo strategy, posts, Q&A management, review generation, performance metrics, and local SEO integration. Invoke this skill when a client needs to create or improve their GBP presence, when local search visibility or Google Maps discoverability is a goal, or when GBP is identified as a priority channel for a Uganda/East Africa-based SME.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Before generating this plan, collect the following from the client:

- **Business name** — exact legal or trading name (used on signage and receipts)
- **Physical address** — full address including district and city, or service area (list of districts/cities served if no customer-facing premises)
- **Phone number** — WhatsApp Business number preferred for EA
- **Website URL** — include if the client has one; note if absent
- **Business category** — primary category and up to 9 secondary categories
- **Business hours** — standard weekly hours plus any irregular opening
- **Uganda public holidays affecting hours** — client to flag which holidays they close or operate reduced hours
- **10 most common customer questions** — for the Q&A section
- **5 best product/service photos** — ask the client to provide; brief them on minimum quality requirements (sharp, well-lit, representative)

---

## 1. GBP Setup and Verification Checklist

Complete every step in order. Do not skip verification before adding content.

**Step 1 — Create or claim the profile**
- Go to business.google.com and sign in with a Google account owned by the business (not a personal account)
- Search for the business name to check whether a profile already exists; if it does, select "Claim this business" rather than creating a duplicate
- If no listing exists, select "Add your business to Google"

**Step 2 — Select the primary category**
- Choose the most specific category available — the primary category is the single most important ranking signal for local search
- Common EA business type primary categories:

| Business type | Recommended primary category |
|---|---|
| Restaurant / food | Restaurant, or more specific (e.g. Pizza Restaurant, African Restaurant) |
| Retail shop | Clothing Store, Electronics Store, Grocery Store — be specific |
| Hair salon | Hair Salon (not Beauty Salon unless multi-service) |
| Consultancy | Management Consulting Service, Marketing Consultant |
| Clinic | Medical Clinic, Dental Clinic — use the specific specialism |
| School | Private School, Tutoring Service, Vocational School |
| NGO | Non-Profit Organisation |

**Step 3 — Add secondary categories**
- Add up to 9 secondary categories to capture additional search terms
- Secondary categories describe other legitimate services the business offers — do not add unrelated categories
- Example: a restaurant that also offers catering and event hire could add: Catering Food and Drink Supplier, Event Venue

**Step 4 — Enter the address or service area**
- Physical location businesses (shop, clinic, school, restaurant): enter the full street address
- Service area businesses (consultants, freelancers, delivery services): select "Service area business" and list the districts or cities served — do not enter a physical address if customers do not visit the premises; a home address appearing on Google Maps is both a privacy risk and an incorrect signal to Google's algorithm
- Hybrid businesses (e.g. a salon that also offers mobile home visits): enter the physical address and add a service area

**Step 5 — Verification**
Google offers the following verification methods — availability varies by category and location:
- **Postcard:** Google mails a postcard with a 5-digit code to the business address. In Uganda and East Africa, allow 5–7 business days minimum; delays of 2–3 weeks are common due to postal infrastructure. Do not make edits to the name, address, or category while awaiting the postcard — edits restart the process.
- **Phone:** A recorded call or SMS provides the verification code instantly. Available for some business types.
- **Email:** A code is sent to a verified business email address. Available for some categories.
- **Instant verification:** Available if the website is already verified in Google Search Console. Fastest option if the website is set up.
- **Video verification:** If the postcard is delayed beyond 3 weeks, request video verification through the GBP support chat. A Google representative reviews a live or recorded walkthrough of the premises. This has become the most reliable method for many EA businesses.

---

## 2. Profile Optimisation Checklist — 10-Point Completeness Score

Score the profile against each element. A score of 10/10 is required before any content or promotion activity begins. An incomplete profile ranks lower and converts fewer visitors.

**1. Business name**
- Enter the exact legal or trading name as it appears on signage, receipts, and the website
- Do not keyword-stuff: "Kampala Best Pizza Restaurant Delivery Fast" violates Google's guidelines and risks suspension. The name field is not a tagline — it is an identifier.
- What good looks like: "Kawa Coffee Roasters" — not "Kawa Coffee Roasters Kampala Best Coffee Uganda"

**2. Primary and secondary categories**
- Primary: the most specific category matching the core business activity (see Section 1)
- Secondary: all legitimate supplementary services, up to 9
- What to avoid: adding aspirational or loosely related categories to capture traffic (e.g. a salon adding "Medical Spa" without medical services)

**3. Address and/or service area**
- Address must match exactly what appears on the website contact page, Facebook Page, and any other directory listing — letter for letter, abbreviation for abbreviation
- What good looks like: "Plot 12, Acacia Avenue, Kololo, Kampala" — consistently rendered everywhere
- What to avoid: "Plot 12 Acacia Ave" on GBP and "12 Acacia Avenue, Kololo" on the website; inconsistency damages local rankings

**4. Phone number**
- Use the primary WhatsApp Business number — this is the single most used customer contact channel in Uganda and East Africa
- The number must be active; Google may call to verify
- What good looks like: +256 7XX XXX XXX — include the country code

**5. Website URL**
- Enter the full URL with a UTM parameter to track GBP traffic in Google Analytics:
  `https://www.yourdomain.com/?utm_source=google&utm_medium=gbp&utm_campaign=organic`
- If the client has no website, leave blank rather than entering a Facebook page URL — this sends a weak authority signal
- What to avoid: a broken URL or a link to a page under construction

**6. Business hours**
- Enter accurate standard hours for each day; mark days closed explicitly rather than leaving blank
- Add special hours for Uganda public holidays: New Year's Day (1 Jan), Liberation Day (26 Jan), International Women's Day (8 Mar), Good Friday, Easter Monday, Labour Day (1 May), Martyrs' Day (3 Jun), Heroes' Day (9 Jun), Independence Day (9 Oct), Christmas Day (25 Dec), Boxing Day (26 Dec)
- What good looks like: all 7 days explicitly set; special hours added for every public holiday 2 weeks in advance
- What to avoid: leaving hours blank — Google may auto-generate hours from user suggestions, which are often incorrect

**7. Business description**
- Maximum 750 characters; lead with the value proposition, include the location and 2–3 relevant keywords naturally
- Structure: sentence 1 — what the business does and for whom; sentence 2–3 — differentiators; sentence 4 — location and contact invitation
- What good looks like: "Kawa Coffee Roasters is a speciality coffee roastery and café in Kololo, Kampala, sourcing single-origin beans from Ugandan farms and roasting in-house daily. We serve espresso-based drinks, cold brew, and light meals in a relaxed setting. Visit us on Acacia Avenue or order freshly roasted beans for delivery across Kampala."
- What to avoid: keyword lists, superlatives ("best", "number one"), phone numbers, and URLs in the description — these violate policy

**8. Products and services**
- Add a minimum of 3 products or services with names, descriptions, and prices where applicable
- Each product/service listing increases the profile's keyword coverage and gives visitors a reason to stay longer
- What good looks like: each listing has a title (max 58 characters), description (max 1,000 characters), category, and price or price range

**9. Photos uploaded**
- Minimum: 8 photos (see Section 3 for the full photo strategy)
- What good looks like: cover photo set, logo uploaded, minimum 3 exterior/interior photos, minimum 3 product/service photos
- What to avoid: stock photography, heavily filtered images, watermarked images, images with text overlaid (use Posts for promotional messaging)

**10. Posts published in the last 30 days**
- At least 1 post within the last 30 days signals an active, managed profile; Google rewards active profiles with better local visibility
- What good looks like: 1–3 posts per week (see Section 4)
- What to avoid: no posts for 60+ days — GBP treats dormant profiles as less relevant

---

## 3. Photo Strategy

Photos are the highest-engagement element of a GBP profile. Profiles with recent, high-quality photos receive 35% more click-throughs than those without. All photos must be sharp, well-lit, and genuinely representative of the business.

**Cover photo**
- Dimensions: 1024×575px (minimum); displayed as the primary image in the Knowledge Panel
- Use the most compelling single image: a professional exterior shot, a signature dish, or a hero product
- Avoid logos, heavy text overlays, or composite graphics — this is the face of the business on Google Maps

**Logo**
- Dimensions: 250×250px (minimum square); displays in the profile as a small circular or square icon
- Use a clean version on a white or solid brand-colour background
- Ensure it is legible at thumbnail size

**Exterior photos (2–5 images)**
- Show the building exterior, entrance, signage, and parking area if available
- Help customers recognise the location before they arrive — critical for businesses on busy streets or inside complexes
- Include at least one photo that shows the business sign clearly

**Interior photos (3–5 images)**
- For restaurants, offices, clinics, and shops: show the seating area, layout, or workspace
- These photos manage customer expectations and reduce "I didn't know what to expect" complaints
- Ensure the space is clean, well-lit, and styled before photographing

**Team photos (2–3 images)**
- Human faces build trust and make the business feel approachable
- Include the owner/founder and 1–2 key staff members in professional but warm settings
- Avoid overly staged corporate photography — natural, in-context shots perform better

**Product and service photos (5–10 images)**
- For food businesses: these are the most clicked photos on the profile — invest in quality
- Show the product or service in context: plated food, styled retail products, a consultation in progress
- Include at least one photo per major product category or service line

**Minimum viable photo set**
1 cover photo + 1 logo + 2 exterior + 2 interior + 3 product/service = 9 photos

**Ongoing: add at least 2 new photos per month.** Google's algorithm treats recently added photos as a freshness signal. Profiles with photos added in the last 30 days outperform those with only older photos.

---

## 4. GBP Posts Strategy

GBP posts appear in the Knowledge Panel (the business information box in search results) and on Google Maps. They are visible to anyone searching for the business by name or category. Use posts to drive enquiries, promote offers, and signal an active, trusted business.

**Post types**

| Post type | Use for | Duration |
|---|---|---|
| What's New | General updates, news, new products, new services | Expires after 7 days — post at least weekly |
| Offer | Promotions with a specific start/end date and optional redemption code | Displays a badge in search results; use for all sales and discounts |
| Event | Workshops, product launches, open days, seasonal events | Displays until the event end date |
| Product | Showcasing specific products with a photo, description, and price | Does not expire; appears in the Products section |

**Posting frequency**
- Minimum: 1 What's New post per week (to prevent the profile appearing inactive)
- Recommended: 2–3 posts per week combining post types

**Post structure (3-step formula)**
1. **Hook sentence** — open with the customer benefit, the offer, or a direct statement of relevance ("Save UGX 20,000 on your next haircut this weekend only.")
2. **Key information** — 2–4 sentences covering the essential details: what, when, where, how much, any conditions
3. **Clear CTA** — one action only, matched to the post type:
   - Call Now — for enquiry-driven businesses
   - Learn More — for blog posts, news, or information-led posts (use UTM-tagged URL)
   - Book — for appointment-based businesses
   - Order Online — for e-commerce or delivery businesses
   - Get Directions — for foot-traffic-driven events or new location announcements

**Optimal post length:** 150–300 words. Posts over 300 words are truncated in the display.

**Best-performing content for EA businesses**
- Offers with specific savings stated in UGX ("Save UGX 15,000 when you buy two")
- Event countdowns ("3 days to go — our anniversary sale starts Friday")
- New product or service arrivals ("Now available: our new range of locally sourced honey products")
- Behind-the-scenes and team updates — humanise the brand

**Links in posts:** include a UTM-tagged link in every post that contains a link:
`?utm_source=google&utm_medium=gbp_post&utm_campaign=[campaign_name]`

---

## 5. Q&A Management

The Google Q&A section allows anyone — including competitors, trolls, or well-meaning but incorrect members of the public — to ask and answer questions on the business profile. Left unmanaged, it becomes a liability. Managed proactively, it becomes a trust-building asset.

**Pre-populate with the 10 most common customer questions**
Do not wait for customers to ask — add the questions and answers yourself using a Google account. Use a secondary Google account (not the GBP owner account) to post each question, then answer from the GBP owner account immediately.

**10 universal Q&A starters for EA businesses**
Adapt the answers to the specific business:

1. What are your payment methods? (Mobile money, cash, card, bank transfer — specify which)
2. Do you offer delivery, and what areas do you cover?
3. What is the price range for your products/services?
4. Are you open on public holidays?
5. Is parking available at your location?
6. Do you require bookings or appointments, or do you accept walk-ins?
7. What is your WhatsApp number for enquiries?
8. Do you offer group or bulk discounts?
9. Where exactly are you located? (Give landmarks, not just the address)
10. How long does a standard service/order take?

**Ongoing Q&A management**
- Set up a Google Alert for the business name (google.com/alerts) to receive notifications when new content — including Q&A — appears
- Check the Q&A section weekly
- Answer new questions within 48 hours
- Flag inaccurate answers posted by third parties for removal using the "Report" option on the answer
- Upvote correct answers (including your own) — higher-upvoted answers appear first

---

## 6. Review Management Strategy

Reviews are the single most important ranking signal in Google's local search algorithm — they influence both ranking position and click-through rate. A business with 4.5 stars and 80 reviews consistently outperforms a business with 5 stars and 3 reviews.

**Generating reviews**

Ask directly after a positive customer experience. The highest-converting moments:
- In person at point of sale or service completion
- Via WhatsApp immediately after delivery or service
- On the printed receipt, packaging, or table tent card (QR code)
- In the email signature as a persistent link

**WhatsApp message template — review request**
Send within 30 minutes of service completion:

> "Hi [Name], thank you for visiting us today — we really hope you enjoyed [specific product/service]. If you have a moment, we would be very grateful if you could share your experience on Google. It genuinely helps other customers find us. Here is the direct link: [GBP review shortlink]
> Thank you so much — we look forward to seeing you again."

To generate a direct review link: in the GBP dashboard, go to Home → Get more reviews → Copy the short URL.

**Important:** never offer discounts, gifts, or any incentive in exchange for a review. This violates Google's review policy and risks profile suspension. The request itself is legitimate; the incentive is not.

**Additional review generation tactics**
- QR code on receipts, menus, packaging, and at the point of sale — link directly to the review page
- Add a "Leave us a review on Google" link to the email footer and WhatsApp Business auto-reply
- Brief customer-facing staff to ask verbally: "If you were happy with your experience, a Google review really helps us — here is the QR code."

**Responding to reviews**
Respond to every review — positive and negative. Unanswered reviews signal a business that does not care about its customers.

- **Response time target:** within 24 hours on weekdays; within 48 hours at weekends
- **Tone:** warm, professional, East African business register — reference the east-african-english skill for language standards

**Positive response template**
Personalise each response — do not use an identical template for every review:
> "Thank you so much, [Name] — we are delighted to hear you enjoyed [specific detail from their review]. It means a great deal to the whole team. We look forward to welcoming you back soon!"

**Negative response template**
Never argue, never deflect, never copy-paste the same generic apology:
> "Hello [Name], thank you for sharing your experience with us. We are genuinely sorry that your visit did not meet the standard we hold ourselves to — this is not the experience we want for any customer. Please contact us directly on [WhatsApp number / email] so we can understand what happened and make it right. We appreciate your feedback."

Take the conversation offline immediately. Do not ask for the review to be removed — this request is visible and looks defensive.

---

## 7. GBP Performance Metrics

Track the following metrics monthly using GBP Insights (accessible from the GBP dashboard under "Performance"). These metrics are available without any third-party tool.

| Metric | What it measures | Monthly health target (EA SME) |
|---|---|---|
| Search impressions | Times the profile appeared in Google Search results | Growing month-on-month |
| Maps impressions | Times the profile appeared in Google Maps | Growing month-on-month |
| Direction requests | Times a user tapped "Get Directions" | Strong intent signal — track trend |
| Phone calls | Calls initiated directly from GBP | Track volume; target: growing monthly |
| Website clicks | Clicks through to the website | Track with UTM confirmation in GA4 |
| Photo views | Total views of profile photos | Benchmark: growing with photo additions |
| Review count | Total reviews accumulated | +2 new reviews/month minimum (under 50 reviews) |
| Average rating | Current star rating | Maintain at 4.2 or above |

**Monthly management checklist**
- Minimum 4 posts published
- Minimum 2 new photos added
- All reviews responded to within 48 hours
- Q&A section checked and any new questions answered
- Special hours updated for any upcoming public holidays
- Average rating at 4.2 or above; if below, prioritise the review generation strategy in Section 6

Present monthly GBP findings alongside social media metrics using the meta-reporting skill.

---

## 8. Local SEO Integration

A GBP profile does not operate in isolation — its ranking is influenced by the consistency and authority of the business's entire online presence. Google's local ranking algorithm weighs three factors:

- **Relevance** — does the profile match what the user is searching for? (Controlled by: category selection, keywords in description, products/services listed)
- **Distance** — how close is the business to the user or the location in the search query? (Not controllable — set the correct address)
- **Prominence** — how well-known and credible is the business online? (Controlled by: review volume and quality, posting activity, inbound links to the website, NAP consistency across the web)

**NAP consistency rule**
NAP stands for Name, Address, Phone number. These three data points must be identical — character for character — on every online platform: the GBP profile, the business website contact page, the Facebook Page About section, any directory listings (Yellow Pages Uganda, Cylex, Hotfrog), and any press mentions. A discrepancy as minor as "Plot 12" vs. "12" causes Google to lower its confidence in the listing and reduces local ranking.

Audit NAP consistency at setup and again every six months.

**Website and GBP cross-linking**
- Add a "Find us on Google Maps" link on the website contact page, linking directly to the GBP profile URL
- This creates a reciprocal authority signal: the website vouches for GBP; GBP drives traffic to the website
- Add the GBP review shortlink to the website's contact page ("Leave us a Google review")

**Embedding the Google Map**
- Embed the Google Map (using the embed code from Google Maps) on the website contact page
- This confirms to Google that the website and the GBP profile refer to the same physical location

**Citation building**
Beyond the website and Facebook, list the business on:
- Yellow Pages Uganda (yellowpages.co.ug)
- Uganda Yellow Pages (ugandayellowpages.com)
- Cylex Uganda
- TripAdvisor (for hospitality and tourism businesses)
- LinkedIn Company Page (for B2B and professional services)

Ensure NAP is consistent across every listing. Each consistent citation strengthens the Prominence signal.

---

## Quality Criteria

Output meets the standard when it:

- The setup checklist is complete enough for a client to create a profile from scratch without consulting any other resource
- All response templates (review request WhatsApp message, positive review response, negative review response) are ready to use with minimal editing — not described in abstract terms
- Photo guidance states specific pixel dimensions and minimum quantities for each photo type
- The post structure section gives a clear 3-step formula (hook → key information → CTA) usable without additional guidance
- EA context is embedded throughout: UGX pricing in post examples, WhatsApp as the primary review request channel, Uganda public holidays in the hours guidance, Kampala/EA location references in all examples
- The review generation section includes the full WhatsApp message template, not just a description of what it should say
- The performance metrics section specifies numerical targets for each metric — not just what to measure but what to aim for
- British English is used throughout with no American spelling variants
