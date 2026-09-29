# Text prompt templates by task

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); text unchanged. Citations corrected afterwards per D-SK-10c (Chaffey and Ellis-Chadwick 2022; Ltifi 2024; see evidence/S09/citation-verification.md). Read when building caption, blog brief, email subject line, persona, platform selection, community response, report narrative or funnel-stage prompts, or when showing a client the before/after quality gap.

## Prompt Library — Templates by Task
Replace all content in square brackets with client-specific detail before use. The Brand Context Block is abbreviated as `[BCB]` below; always paste the full block.

### 1. Caption Writing
```
[BCB]

Consider the situation: [describe what the business is promoting and why it matters
to the audience right now — include the campaign phase or seasonal trigger].
Acting as a social media copywriter for [Brand] writing for [audience description:
age, location, aspiration, current pain point].
Write a [platform] caption using the [PAS / AIDA / BAB — choose one] framework.
In a single caption with a line break after the hook, body text, and a CTA on a
new line.
Using: British English; maximum 150 words; no banned vocabulary; end with a
WhatsApp CTA [wa.me/256XXXXXXXXX]; include [number] hashtags drawn from
[hashtag guidance or list]; never begin with "Are you".
```

### 2. Blog Post Brief
```
[BCB]

Consider the situation: [describe the target reader's search intent or problem —
what are they typing into Google or asking on WhatsApp right now].
Acting as a content strategist briefing a writer for [Brand].
Create a complete blog post brief including: SEO title (under 60 characters),
meta description (under 155 characters), primary keyword, 5 H2 headings,
one practical takeaway section, and a closing CTA.
In a structured markdown document.
Using: British English; 1,200–1,800 word target; first H2 must include the primary
keyword; all examples must be drawn from Uganda or East Africa; no Western-market
assumptions; link suggestion for one internal and one external source.
```

### 3. Email Subject Line and Preview Text
```
[BCB]

Consider the situation: [state the email campaign goal, the audience segment,
and the stage in the customer journey — e.g. re-engagement, post-purchase, onboarding].
Acting as an email marketer writing for [audience description].
Generate 5 subject line options and 5 matching preview texts.
In a table format with columns: Subject Line | Preview Text | Technique Used.
Using: subject line under 50 characters; preview text under 90 characters;
no clickbait or false urgency; techniques may include curiosity, benefit,
urgency, social proof, or personalisation; include at least one option with
a localised East African reference; British English throughout.
```

### 4. Audience Persona
```
Consider the situation: [business name, industry, and Uganda/East Africa market —
include any known data about current customers or target segment].
Acting as a market researcher building a detailed audience persona for [Brand].
Create a complete audience persona for [client's target segment name or description].
In a structured document with the following fields: Name (fictional), Age, Location
(specific EA city or town), Occupation, Monthly income (UGX), Education level,
Social platforms used, WhatsApp behaviour (how they use it for commerce and comms),
content formats they engage with, their primary problem, what they want to achieve,
objections to buying, and one direct quote that captures their mindset.
Using: only realistic Uganda/East Africa demographics and income ranges; cite
Facebook penetration data where relevant; no Western market assumptions; reference
Chaffey and Ellis-Chadwick (2022) for audience segmentation methodology if applicable.
```

### 5. Social Media Strategy — Platform Selection Section
```
[BCB]

Consider the situation: [client's current social media presence, primary business
goal, competitive context in Uganda/EA, and budget constraints if known].
Acting as a social media strategist applying the RACE framework
(Reach/Act/Convert/Engage — Chaffey and Ellis-Chadwick, 2022) for [Brand].
Produce the platform selection and channel roles section of a social media strategy.
In structured markdown: one summary table (Platform | Primary Role | Content Type |
Posting Frequency) followed by a rationale paragraph per recommended platform.
Using: Uganda/EA platform penetration data; WhatsApp as the primary owned channel
for customer communications; Facebook as the primary reach channel; recommend no
more than 3 platforms for a starter client; cite the POEM model
(Paid/Owned/Earned) when classifying channels.
```

### 6. Community Management Response
```
[BCB]

Consider the situation: [paste or describe the comment, DM, or WhatsApp message
verbatim — include the sentiment, platform, and whether it is public or private].
Acting as a community manager for [Brand] responding to a
[complaint / question / compliment / crisis comment].
Write a response that [acknowledges the issue and offers resolution /
answers the question directly / expresses genuine gratitude].
In a [public comment reply / private DM / WhatsApp message] of under 60 words.
Using: warm, respectful East African professional tone; move the conversation
to WhatsApp if resolution requires further discussion
[wa.me/256XXXXXXXXX]; never be defensive or dismissive; never delete a
complaint without resolution; British English throughout.
```

### 7. Monthly Performance Report Narrative
```
Consider the situation: [paste the month's key metrics — reach, impressions,
engagement rate, follower growth, link clicks, WhatsApp enquiries generated,
and any notable campaign results. Include the previous month's figures for
comparison where available].
Acting as a social media analyst writing an executive summary for
[client's management team — state their level of digital literacy].
Produce a 3-paragraph performance narrative covering: (1) overall summary
and standout metric; (2) what drove the best-performing content and what
underperformed; (3) one recommended action for next month.
In plain, jargon-free English formatted as three labelled paragraphs.
Using: British English; cite specific numbers in every paragraph;
no hollow phrases such as "robust performance" or "going forward";
conclude with a forward-looking recommendation framed as a SMART objective;
reference the RACE framework (Chaffey and Ellis-Chadwick, 2022) if applicable.
```

## Sales Funnel Stage-Specific Prompts
Source: GPT Penguin (2024). Calibrate content prompts by buyer journey stage:

**Top-of-Funnel (Attract)** — first-time visitors; no prior relationship with the brand.
```
[BCB]
Consider the situation: {{prospect description}} has just discovered {{brand name}} for the first time. They do not know the brand. Acting as a social media copywriter for {{brand name}} writing for {{audience values description}}. Write a {{platform}} post that introduces the brand's core value proposition without selling — educate and intrigue first. In a single post of under 120 words. Using: British English; no promotional language; no price mentions; end with a curiosity question or an invitation to learn more.
```

**Middle-of-Funnel (Nurture)** — leads who have shown interest (followed, engaged, clicked).
```
[BCB]
Consider the situation: {{prospect description}} has interacted with {{brand name}} content before. They know who the brand is. Acting as a social media copywriter for {{brand name}} writing for an audience that is considering but not yet committed. Write a {{platform}} post that provides proof of value — a case study, testimonial, or behind-the-scenes detail. In a narrative post of 100–150 words. Using: British English; specific and credible detail (no vague claims); include one social proof element; end with a soft CTA: "Find out how we helped [type of client]."
```

**Bottom-of-Funnel (Decision)** — decision-stage prospects ready to act.
```
[BCB]
Consider the situation: {{prospect description}} is actively deciding whether to work with {{brand name}}. They have seen the brand before. Acting as a social media copywriter for {{brand name}} writing for a warm, ready-to-act audience. Write a {{platform}} post that makes a direct, specific offer with a clear CTA. In a concise post of under 100 words. Using: British English; one specific offer or guarantee; one frictionless CTA ("Message us on WhatsApp: {{WhatsApp link}}"); no watered-down language; genuine urgency only where a real deadline exists.
```

## Before/After Prompt Comparison — Social Caption
Source: Chavaux (2025). The most effective technique for making the quality gap between weak and strong prompts tangible.

**BEFORE — Weak Prompt:**
```
Write a caption for a Ugandan coffee brand.
```
*Typical output:* Generic, Western coffee-culture language. No local context. No CTA. No emotional pull.

**AFTER — Strong Prompt:**
```
[BCB for {{brand name}}, a specialty Ugandan coffee brand targeting urban Kampala professionals aged 28–42 who value locally-produced quality]

Consider the situation: It is Monday morning. Our audience is starting their working week and already thinking about productivity. Acting as a social media copywriter for {{brand name}} writing for ambitious Kampala professionals who take pride in supporting Ugandan-grown products. Write a Facebook caption using the AIDA framework (Attention → Interest → Desire → Action) that positions our coffee as the professional's daily ritual. In a single caption with a line break after the hook, body text, and CTA on a new line. Using: British English; maximum 120 words; evoke morning energy and local pride; end with a WhatsApp CTA {{WhatsApp link}}; include 3 relevant hashtags; never begin with "Are you".
```
*Typical output:* Locally grounded, emotionally resonant, framework-structured, with a clear CTA.
