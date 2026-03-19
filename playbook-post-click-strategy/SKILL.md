---
name: playbook-post-click-strategy
description: >
  Generates a post-click conversion strategy and planning guide for social media consultancy clients. Covers the full journey from social post or ad through to a completed action — WhatsApp enquiry, sale, email opt-in, or form submission. Invoke this skill when a client has an active social presence but is not converting followers into leads or customers, or when conducting a social-to-sale audit.
---

# Post-Click Conversion Strategy Playbook

## Required Input

Before generating any deliverable, ask for:

1. **Client business name** — trading name as used on social media
2. **Industry and product/service type** — what they sell and at what price point
3. **Country/city** — default is Uganda; specify region if relevant (Nairobi, Dar es Salaam, etc.)
4. **Primary goal** — enquiries via WhatsApp, form submissions, direct sales, email opt-ins, or calls
5. **Current conversion path** — what happens when someone clicks the link today (bio link, no link, direct message, etc.)
6. **Website status** — full website, simple WordPress, landing page only, or no website at all
7. **WhatsApp Business** — are they using WhatsApp Business or personal WhatsApp?
8. **Primary platforms** — Instagram, Facebook, TikTok, YouTube, WhatsApp Status, or a combination

---

## 1. The Post-Click Gap

### Why EA SMEs Lose Customers After the Click

Most social media consultancy work focuses on reach and engagement — growing followers, increasing likes, improving posting frequency. The post-click gap is the space between a follower seeing a post and taking a commercial action. In East Africa, this gap is wider than in markets with high website penetration.

**Common broken conversion paths:**

- Bio link points to a homepage with no clear next step
- Bio link has not been updated in months and leads to an expired promotion
- Post says "DM us" with no further instruction — enquirer sends one message and hears nothing
- Facebook page has a phone number but no click-to-call; user must copy and dial manually
- Landing page takes 12 seconds to load on 3G — user abandons
- WhatsApp number is personal; messages arrive at 2 am with no automated response

**What friction means in a mobile-first, low-bandwidth context:**

Friction is any step that increases the effort required to complete an action. In Uganda and East Africa, friction is amplified by:

- Predominantly mobile browsing on mid-range Android devices
- 3G connections in peri-urban and rural areas; 4G available but inconsistent even in Kampala
- Data costs making slow pages expensive to load, not just slow
- Low tolerance for forms with more than three fields
- High trust in WhatsApp as a communication channel versus email or web forms

Apply the principle: every additional step between the social post and the conversion action reduces conversion rate. Design for the fewest possible steps.

---

## 2. Link-in-Bio Strategy (Instagram and TikTok)

### The One-Link Problem

Instagram and TikTok allow one clickable link in the bio. This creates a forced choice: send traffic to a website, a WhatsApp chat, a landing page, or a multi-option menu.

**Solutions:**

- **Linktree** (free tier available) — multi-link page hosted at `linktr.ee/[handle]`; easy to update; sufficient for most EA clients
- **Beacons.ai** — similar to Linktree with additional customisation; free tier adequate for SMEs
- **Instagram native link sticker** — available in Stories only; use for campaign-specific CTAs without changing the bio link
- **Single WhatsApp CTA** — for clients with one clear conversion goal, a direct `wa.me` link in the bio outperforms a multi-option menu; fewer choices mean fewer decisions

**What to put in the bio link:**

| Client situation | Recommended bio link |
|---|---|
| One product or service, WhatsApp primary | Direct `wa.me` click-to-chat link with pre-filled message |
| Multiple services, no website | Linktree with 3–4 options maximum |
| Has a landing page | Landing page URL with UTM parameter |
| Running a campaign | Linktree top button updated to campaign CTA; other links remain |

**Updating links for campaigns:**

- Use Linktree so the bio URL never changes; only update the destination inside Linktree
- Announce link updates in Stories: "New link in bio — [what it goes to]"
- Do not change the bio link URL itself — followers who saved it will land correctly

**The "link in bio" caption formula:**

```
[Hook or problem statement]
[Value or outcome]
[Single instruction]: Link in bio → [specific action]
```

Example: "Struggling to fill your school's intake? We've helped 14 schools in Kampala double enquiries in 90 days. Book a free 20-minute strategy call — link in bio."

---

## 3. WhatsApp as the Primary Conversion Channel

### Click-to-Chat Links

A WhatsApp Click-to-Chat link opens a chat with a pre-filled message. No need to save the number.

**Format:** `https://wa.me/256XXXXXXXXX?text=Your%20pre-filled%20message`

- Replace `256XXXXXXXXX` with the full international number (Uganda: 256 prefix, drop leading 0)
- Encode spaces as `%20`; use a URL encoder for longer messages
- Use `https://wa.me/` not `http://wa.me/` — the `https` version is more reliable on mobile browsers

**Where to place the link:**

- Instagram and TikTok bio (as the single link or top Linktree button)
- Facebook page "Send Message" button — set to Messenger OR use the website URL field for the `wa.me` link
- Email signature, Google Business Profile, Linktree
- Landing page CTA button

### Pre-Filled Opening Messages

The pre-filled message qualifies the enquirer before the conversation begins.

**Formula:** `Hi [Business Name], I'm interested in [service]. I found you on [platform].`

Example for a Kampala bakery: `Hi Sweet Layers, I'm interested in ordering a cake. I found you on Instagram.`

This tells the business owner: who enquired, what they want, and which platform drove the lead.

### The 3-Message Qualification Sequence

Once the enquiry arrives, use this sequence in WhatsApp Business:

1. **Welcome** — acknowledge the enquiry within 5 minutes or use an automated greeting: "Hello! Thanks for reaching out to [Business Name]. We'll respond shortly. What would you like to order or enquire about?"
2. **Qualify** — ask the one question that determines whether this is a genuine lead: budget, timeline, location, quantity, or service type
3. **Invite to proceed** — based on the answer, send a catalogue link, price list, booking link, or next step: "Great — here's our menu with prices. Which option suits you?"

### WhatsApp Business Setup for Conversion

- **Automated greeting message** — set in WhatsApp Business Settings → Business Tools → Greeting Message; fires on first contact or after 14 days of inactivity
- **Away message** — set for out-of-hours; include expected response time and a self-service option ("Browse our catalogue while you wait: [link]")
- **Quick replies** — save frequent responses as shortcuts (e.g., `/price` sends the price list; `/location` sends the address with Google Maps link)
- **Catalogue** — upload products or services with photos, descriptions, and prices; share the catalogue link in the bio and in opening conversations

---

## 4. Lead Magnet Delivery via Social

### What a Lead Magnet Is

A lead magnet is a free item of value exchanged for a contact or conversation. In the EA context, the most effective formats are:

- A free PDF guide (e.g., "5 Things to Check Before Hiring a Contractor in Uganda")
- A free consultation or audit (15–30 minutes)
- An exclusive offer for followers ("Show this post for 10% off your first order")
- A free sample, trial, or demo

### Delivery Methods

| Method | Best for | How it works |
|---|---|---|
| WhatsApp DM | High-touch services; immediate relationship | Caption says "Comment GUIDE below or DM us GUIDE to receive it" — staff reply with PDF or voice note |
| Google Form opt-in | Email list building; clients with CRM ambitions | Form collects name, email, phone; confirmation message delivers the link |
| Direct DM reply (Instagram/Facebook) | Follower base is active; team can respond quickly | Story or post: "DM us the word GUIDE" — reply with the PDF or Linktree link |
| WhatsApp Broadcast | Existing WhatsApp contacts | Send the lead magnet to broadcast list; include a forward-to-a-friend instruction |

### Promoting a Lead Magnet by Platform

**Instagram Stories:**
- Slide 1: Problem or pain point
- Slide 2: Solution teaser
- Slide 3: "DM us [keyword] to get the free guide" with a link sticker pointing to WhatsApp

**Facebook post:**
- Post the first three points of the guide as a preview
- End with: "Comment GUIDE below and we'll send you the full version"
- Pin the post to the top of the page during the campaign

**WhatsApp Status:**
- Post the offer as a Status image with a direct reply prompt: "Reply to this Status with YES and we'll send it to you"
- Replies go directly into individual chats — respond with the PDF or link

---

## 5. Landing Page Principles for the EA Context

### Design for the Constraint, Not the Ideal

Most EA clients will not have a professionally built website. The principles below apply whether the page is WordPress, Wix, Google Sites, or a Linktree page.

**Non-negotiable requirements:**

- **Mobile-first layout** — design and test on a mid-range Android screen first; desktop is secondary
- **Load time under 3 seconds on 3G** — compress all images; avoid video autoplay; use minimal scripts
- **Single CTA per page** — one button, one action; do not offer multiple options on the same page
- **Social proof above the fold** — the first screen the user sees must include a real photo, a testimonial, a WhatsApp screenshot of a happy client, or a client logo

**Page structure:**

1. **Headline** — one sentence stating who this is for and what they get
2. **Three key benefits** — short bullets, no more than eight words each
3. **Social proof** — photo, testimonial, or before/after result
4. **Single CTA button** — "Chat with us on WhatsApp" or "Call Now"; large enough to tap on mobile; high-contrast colour

**Page builder options appropriate for EA:**

| Tool | Cost | Best for |
|---|---|---|
| WordPress + Elementor | Low (hosting ~UGX 50,000/mo) | Clients who want a long-term website |
| Wix | Free tier available | Quick setup; no developer needed |
| Google Sites | Free | Non-profits, schools, very small businesses |
| Linktree Pro | ~USD 5/mo | Clients with no website; multi-link menu |
| Carrd.co | Free–USD 19/yr | Single-page sites; very fast load times |

---

## 6. Post-Click Measurement

### UTM Parameters for Social Traffic

UTM parameters tag the URL so analytics tools (Google Analytics, Bitly stats) can identify which social post drove a visit.

**Standard UTM structure:**
```
?utm_source=instagram&utm_medium=social&utm_campaign=[campaign-name]
```

Cross-reference the `meta-utm-tracking` skill for full parameter conventions and a UTM builder template.

### WhatsApp Link Tracking

WhatsApp itself does not provide click analytics. Work around this:

- **Bit.ly short link** — wrap the `wa.me` link in a Bit.ly link; Bit.ly tracks clicks by date, source, and geography; free tier is sufficient for most clients
- **Separate numbers per campaign** — clients with multiple SIM cards can use a dedicated number per campaign to attribute WhatsApp leads
- **WhatsApp Business API** — for larger clients (50+ enquiries per day); enables webhook-based tracking and CRM integration; requires a third-party provider (e.g., Twilio, Bird, Africa's Talking)

### Conversion Events to Track

Define these events at the start of every engagement:

| Event | How to track |
|---|---|
| WhatsApp message received | Bit.ly click count on the `wa.me` link as a proxy; manual count in WhatsApp Business |
| Form submission | Google Form response count; Google Analytics goal (if form is on website) |
| Call made | Google Business Profile call clicks; manual log |
| Landing page visit | Google Analytics sessions with UTM source = social platform |
| Lead magnet download | Bit.ly clicks on the PDF link; Google Drive view count |

### What to Report to the Client

Include in the monthly report:

- Total WhatsApp enquiries received (by week)
- Top platform driving WhatsApp clicks (from Bit.ly data)
- Landing page visits from social (UTM breakdown)
- Form submissions
- Conversion rate: enquiries ÷ link clicks (where trackable)
- One recommended optimisation based on the data

---

## 7. Platform-Specific Conversion Paths

### Instagram

Path: Post or Story → Bio link (Linktree or direct `wa.me`) → WhatsApp conversation or landing page

- Use the link sticker in Stories for campaign-specific CTAs without touching the bio link
- Reels: add "Link in bio" in the caption; include a verbal CTA in the video audio if possible
- Carousel posts: final slide is the CTA slide with the bio link instruction

### Facebook

Path: Post or Page → CTA button (Messenger, Call, or website URL) → WhatsApp or landing page

- Set the Page CTA button to "Send Message" for Messenger, or use the website field for the `wa.me` link
- For posts: use the "Learn More" or "Shop Now" button when boosting to drive to a landing page
- Facebook Groups: pin a post with the WhatsApp link at the top of the group

### TikTok

Path: Video → Bio link (Linktree or landing page) → WhatsApp

- TikTok does not allow clickable links in captions; the bio link is the only organic exit point
- Verbal and text-overlay CTAs in the video are essential: "Link in bio to order"
- For accounts under 1,000 followers, the bio link may not be available; use "DM us" as the fallback

### WhatsApp Status

Path: Status view → Direct reply to Status → Individual chat conversation

- Viewers who reply to a Status are already in your contacts — a warm audience
- Use Status for flash offers, reminders, and lead magnet delivery
- Broadcast lists amplify reach to opted-in contacts; keep broadcasts to 2–3 per week maximum

### YouTube

Path: Video → Description link or end screen → Landing page or `wa.me` link

- Place the WhatsApp or landing page link as the first line of the video description
- Use end screens in the final 20 seconds to drive to a landing page or to subscribe
- Pinned comment with the link increases visibility on mobile where descriptions are collapsed

---

## 8. Conversion Path Audit

### How to Review a Client's Current Social-to-Sale Journey

Conduct the audit from a cold-start perspective: behave as a new potential customer who has just discovered the client on social media.

**Audit steps:**

1. Open the client's Instagram or Facebook profile on a mobile device (not desktop)
2. Tap the bio link — record what loads and how long it takes
3. Follow every CTA in the top 10 posts — record where each leads
4. Send a DM enquiry — record response time and quality
5. If a WhatsApp number is visible, initiate a chat — record the greeting and follow-up sequence
6. If a landing page exists, assess it against the five-point page structure above
7. Record every point where you would have abandoned as a real customer

**Friction point checklist:**

- [ ] Bio link is present and working
- [ ] Bio link destination matches the current offer or campaign
- [ ] Page load time is under 3 seconds on a mobile connection
- [ ] Single clear CTA visible above the fold
- [ ] WhatsApp link uses `wa.me` format with a pre-filled message
- [ ] WhatsApp Business greeting message is active
- [ ] Post captions include an explicit CTA with instructions
- [ ] DM enquiries receive a response within 1 business hour
- [ ] Google Business Profile (if applicable) has a current phone number and WhatsApp link
- [ ] UTM parameters are in use on at least the primary conversion link

**Priority fixes (in order of impact):**

1. Replace a broken or outdated bio link immediately
2. Add a `wa.me` click-to-chat link as the primary or sole CTA
3. Activate WhatsApp Business greeting and away messages
4. Compress landing page images; test load time on 3G
5. Add social proof (testimonials, photos) above the fold on the landing page
6. Set up Bit.ly tracking on the WhatsApp link
7. Introduce a lead magnet with a simple delivery mechanism

---

## Quality Criteria

Output for this skill meets the standard when it:

1. **Addresses the client's actual conversion gap** — the strategy is built around the specific broken path identified in the required input, not a generic template
2. **Recommends the fewest steps to conversion** — every recommended path has three steps or fewer between the social post and the completed action
3. **Prioritises WhatsApp as the default conversion channel** — all paths default to WhatsApp unless the client has a specific reason to use another channel; WhatsApp links use the correct `wa.me` format with pre-filled messages
4. **Is realistic for the client's technical capacity** — tool and platform recommendations match the client's website status and team size; free or low-cost options are offered for SME clients
5. **Includes a measurable outcome for each recommendation** — every tactic includes at least one trackable signal (Bit.ly clicks, form submissions, WhatsApp message count)
6. **Passes the mobile-first test** — all landing page and link-in-bio recommendations are assessed against 3G load time and mid-range Android usability
7. **Delivers a clear audit checklist** — the conversion path audit section produces a prioritised list of fixes specific to the client, not a generic review
8. **Uses British English and EA market context throughout** — pricing references use UGX or KES as appropriate; platform defaults reflect EA penetration data; examples use locally recognisable business types and scenarios
