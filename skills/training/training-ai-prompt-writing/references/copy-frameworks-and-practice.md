Parent: [training-ai-prompt-writing](../SKILL.md)

## Module 3: Copywriting Frameworks in Prompts (45 minutes)

### Learning Objective

Teach participants to embed copywriting frameworks in the Gamma element of a prompt, producing structured, persuasive marketing copy with consistent logic.

### 3.1 Why Frameworks Matter in Prompts

Explain that copywriting frameworks give the AI a logical structure to follow. Without a framework instruction, AI copy tends to be flat and unconvincing. With a framework, output follows a proven persuasion sequence.

### 3.2 The Seven Frameworks

Explain each framework with a Uganda/East Africa brand example. Show participants how to embed the framework name in the Gamma element.

---

**1. PAS — Problem / Agitate / Solution**

*Structure:* Identify the pain point → make it emotionally vivid → present the answer.

*Prompt instruction (Gamma):* "Write using the PAS framework: first name the problem the audience faces, then agitate it (make it feel urgent or frustrating), then present the product as the solution."

*EA example:* For a Kampala fuel delivery brand — Problem: running out of petrol at the wrong time. Agitate: stuck in Ntinda traffic with an empty tank, no fuel station in sight. Solution: [Brand] delivers fuel to your location in under 30 minutes.

---

**2. AIDA — Attention / Interest / Desire / Action**

*Structure:* Grab attention → build interest → create desire → prompt action.

*Prompt instruction (Gamma):* "Write using the AIDA framework: open with a bold attention hook, develop interest with relevant detail, build desire with a benefit or outcome, close with a direct call to action."

*EA example:* For a Ugandan savings app — Attention: "Every week you delay saving costs you more than you think." Interest: [App] automatically saves UGX 5,000 from every mobile money transaction. Desire: Thousands of Ugandans have saved their first UGX 1,000,000 without thinking about it. Action: Download and start saving today.

---

**3. BAB — Before / After / Bridge**

*Structure:* Show the painful before state → paint the desirable after state → bridge with the product.

*Prompt instruction (Gamma):* "Write using the BAB framework: describe the before state (audience's current frustration), describe the after state (what life looks like with the solution), then bridge the two with the product."

*EA example:* For a Nairobi laundry service — Before: spending your Sunday washing instead of resting. After: clean, folded, delivered by Saturday evening. Bridge: [Brand] handles your laundry so your Sunday is yours again.

---

**4. FAB — Features / Advantages / Benefits**

*Structure:* State the product feature → explain its advantage → describe the real benefit to the customer.

*Prompt instruction (Gamma):* "Write using the FAB framework: name the feature, state the functional advantage it provides, then articulate the emotional or practical benefit the customer experiences."

*EA example:* For a Ugandan solar home system — Feature: 200W solar panel with 10-hour battery backup. Advantage: powers lights, phone charging, and a small TV without grid electricity. Benefit: your household stays connected and your children can study after dark.

---

**5. SSS — Star / Story / Solution**

*Structure:* Introduce a relatable character (Star) → tell their struggle (Story) → resolve it with the product (Solution).

*Prompt instruction (Gamma):* "Write using the SSS framework: introduce a relatable character facing a problem, tell a short story of their struggle, then resolve it with the product or service."

*EA example:* For a Tanzanian health insurance brand — Star: Mama Zawadi, a market vendor in Dar es Salaam. Story: when her son fell ill, she had to close her stall for three days and borrow money she couldn't afford to repay. Solution: [Brand] covered the hospital bill. She never closed her stall again.

---

**6. PPPP — Picture / Promise / Prove / Push**

*Structure:* Create a vivid mental image → make a clear promise → provide evidence → push to action.

*Prompt instruction (Gamma):* "Write using the PPPP framework: paint a vivid picture of the desired outcome, make a specific promise, provide proof or social evidence, then push the reader to act now."

*EA example:* For a Ugandan real estate brand — Picture: imagine driving through your gate, not your landlord's. Promise: we help first-time buyers own a home in Wakiso from UGX 120M. Prove: over 400 families have moved in since 2021. Push: book your site visit this weekend — plots are releasing fast.

---

**7. AFOREST — Alliteration / Facts / Opinions / Repetition / Examples / Rhetorical questions / Statistics / Three-part lists**

*Structure:* A toolkit of persuasive writing devices — use selectively rather than all at once.

*Prompt instruction (Gamma):* "Write using AFOREST persuasive devices. Include at least: one factual statement, one rhetorical question, one statistic, and a three-part list."

*EA example instruction to AI:* "You are a copywriter for a Kenyan mobile data brand. Write a Facebook post using AFOREST devices: include a rhetorical question, a statistic about mobile data usage in Kenya, and a three-part list of what customers can do with the data bundle."

---

### 3.3 Embedding Frameworks in the Gamma Element

Show participants the exact pattern for embedding any framework in a prompt:

*"Write [quantity] [content type] using the [FRAMEWORK NAME] framework ([brief description of the framework sequence]). [Add length, CTA, and hashtag requirements here.]"*

### 3.4 Hands-On Activity (20 minutes)

Participants complete two exercises:

**Exercise A:** Write one Instagram caption using the PAS framework for their own brand. Run it through the AI, review the output, and refine once.

**Exercise B:** Write one email subject line using the AIDA framework for their own brand. Run it through the AI, compare 3 variations.

Share and discuss outputs with the group.

---

## Module 4: Practical Prompt Library and Iterative Refinement (30 minutes)

### Learning Objective

Equip participants with a reusable set of prompt templates and the habit of iterative refinement — so they leave training with tools they can use the next day.

### 4.1 The Prompt Library

Walk through 7 ready-made prompt templates from the `prompt-engineering-library` skill. Cover one template from each common content type:

1. Instagram / Facebook caption
2. WhatsApp broadcast message
3. Email subject line
4. Email body (short-form)
5. LinkedIn post (thought leadership)
6. Blog post introduction
7. SMS / short copy

For each template, show participants where to substitute their own brand details. Demonstrate live on the AI tool.

*Reference:* For the full library of templates, see the `prompt-engineering-library` skill.

### 4.2 Iterative Refinement

Explain the five prompting approaches (Upadhyay, 2024) and when to use each:

| Approach | Description | Best for |
|---|---|---|
| **Zero-shot** | Single instruction, no examples | Simple tasks: date, format, quick edits |
| **One-shot** | One example provided before the request | Tone matching when you have one good example |
| **Few-shot** | 2–5 examples provided before the request | Brand voice matching; consistent series of posts |
| **Chain-of-thought** | Ask AI to reason step by step before outputting | Strategy tasks: campaign planning, audience analysis |
| **Iterative refinement** | Start broad, narrow with follow-up prompts | Any high-stakes content requiring multiple drafts |

**Demonstrate iterative refinement live** using a three-prompt sequence:

- **Prompt 1 (broad):** Run the initial Alpha-Beta-Gamma-Delta-Epsilon prompt. Review output.
- **Prompt 2 (narrow):** "Good. Now shorten the first caption to under 100 characters and make the CTA more direct. Keep everything else the same."
- **Prompt 3 (refine):** "Replace the third hashtag with a more location-specific Ugandan tag. Do not change the rest."

Show that iterative refinement produces better results than trying to write the perfect prompt first time.

### 4.3 The AI Content Quality Checklist

Before any AI-generated content is published, apply the checklist from the `ai-content-humaniser` skill. Key checks include:

- Does this sound like a human wrote it, or an AI?
- Does it match the brand voice guide?
- Are all facts, statistics, and figures verified?
- Are there any AI clichés ("game-changing", "seamless", "dive into", "in today's fast-paced world")?
- Has a human editor reviewed and approved it?

*Reference:* For the full humanisation checklist and editing protocol, see the `ai-content-humaniser` skill.

### 4.4 East African Context Notes

Apply these additional considerations when prompting for EA-market content:

- **WhatsApp broadcast prompts** require different constraints than email or Instagram. Specify: conversational tone, short paragraphs, no HTML, no markdown formatting, clear opt-out line.
- **Luganda / Swahili phrases** can be embedded. Instruct the AI: "Include one Luganda phrase in the caption and provide an English translation in brackets."
- **Low-data context** means shorter, punchier copy performs better. Default to under 150 characters for captions; under 160 characters for SMS.
- **Local cultural context** is powerful. Instruct the AI to reference locally recognisable elements: boda-boda, rolex (the Ugandan street food), market day, supper culture, Kampala traffic, KCCA, etc.
- **UGX pricing** should always appear in prompts where price is relevant. Do not let the AI invent pricing — always provide it in the Beta element.

### 4.5 Prompt Type Taxonomy and Examples-First Methodology

**Eight prompt types** — use as a decision tool:

| Type | When to Use |
|---|---|
| **Zero-shot** | Simple tasks, quick edits |
| **Few-shot** | Brand voice matching — correct default for any voice task |
| **Instructional** | Complex multi-part deliverables |
| **Conversational** | Refinement, ideation, brainstorming |
| **Contextual** | Strategy documents, personas, reports |
| **Creative** | Storytelling, campaign concepts |
| **Chain-of-Thought** | Strategy, audience analysis, decision-making |
| **Systematic** | Repeatable tasks: caption series, email sequences |

**Few-shot is the correct default for brand voice work.** Supply 2–3 examples of actual human writing before issuing a content task. Master structure:

```
Here is an example of [content type] in the voice and style I want:
###
[Example 1]
###
[Example 2]
###
Now write a new [content type] on [topic] in the same voice and style.
```

Adjectives are imprecise; examples are exact. Three or more examples enable reliable voice matching; fewer produce inconsistency. Training activity: participants paste three real brand posts, generate a new post, compare against tone-adjective-only output.

## Worked Prompt Examples

### Example 1: Instagram Caption — PAS Framework (Telecoms Brand)

```
Alpha: You are a senior social media copywriter specialising in Ugandan telecoms brands.

Beta: The brand is [X], targeting urban professionals aged 25–35 in Kampala. Brand voice: confident, friendly, slightly witty. Product: 5G data bundle, UGX 15,000 for 5GB/7 days.

Gamma: Write 3 Instagram captions using the PAS framework (Problem → Agitate → Solution). Each caption must be under 150 characters, end with a clear CTA, and include 2–3 relevant hashtags.

Delta: Do not mention competitor brands. Do not use the words "affordable" or "seamless". Avoid exclamation marks.

Epsilon: Present as a numbered list with the PAS label for each element.
```

### Example 2: Email Subject Lines — AIDA Framework (Microfinance Institution)

```
Alpha: You are an email copywriter for an East African microfinance institution.

Beta: We are sending a re-engagement email to customers who have not transacted in 90 days. Brand tone: warm, encouraging, professional.

Gamma: Write 5 subject line options using the AIDA framework (Attention → Interest → Desire → Action), each under 50 characters.

Delta: Do not mention overdue balances. Do not use the word "urgent".

Epsilon: Numbered list, subject line only, no explanation.
```

### Example 3: WhatsApp Broadcast — BAB Framework (Delivery Service)

```
Alpha: You are a WhatsApp copywriter for a Kampala-based same-day delivery service.

Beta: Brand: [X]. Audience: small business owners and traders aged 28–45 in Kampala. Tone: direct, reliable, no-nonsense. Promotion: free delivery on orders above UGX 50,000 this Friday only.

Gamma: Write one WhatsApp broadcast message using the BAB framework (Before → After → Bridge). Maximum 3 short paragraphs. End with a WhatsApp reply CTA ("Reply YES to book your first delivery").

Delta: No emojis. No markdown. No bullet points — plain text only. Do not use the phrase "limited time".

Epsilon: Single plain-text message, no formatting, ready to paste into WhatsApp Business.
```

---
