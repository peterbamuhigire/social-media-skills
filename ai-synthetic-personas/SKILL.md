---
name: ai-synthetic-personas
description: Generate research-grade audience personas using AI when primary fieldwork is unavailable or too costly. Invoke when a client needs audience personas for strategy development but cannot commission primary research, or when quick validation of messaging concepts is needed.
---

# AI Synthetic Personas

Generate structured audience personas using AI-assisted synthesis when primary research is unavailable. Personas produced by this skill are informed hypotheses grounded in secondary data and East African market knowledge — not primary research findings. Every deliverable produced using this skill must carry the disclosure specified in the Citation Standard section below.

Apply the `east-african-english` skill for tone throughout. For clients who can commission primary research, use `03-audience-personas` instead and return to this skill only for supplementary rapid-validation work.

---

## Required Input

Ask for the following before generating any personas:

- **Client business name** — the trading name as used publicly
- **Industry** — be specific (e.g. "private healthcare clinic", "SME accounting software", "mid-range restaurant chain")
- **Country / city** — defaults to Kampala, Uganda if not specified; adjust EA norms for Kenya or Tanzania if relevant
- **Target audience description** — age range, income band, location (urban/peri-urban/rural), and any known sub-segments
- **Primary goal** — choose one: strategy development / messaging validation / content planning / campaign targeting
- **Available secondary data** — note any existing research, sales data, customer feedback, or Meta Audience Insights the client can share; state "none available" if there is nothing

---

## When to Use Synthetic vs Primary Research

### Use synthetic personas when:

- Budget for primary research is unavailable
- The project timeline is under two weeks
- Preliminary hypotheses need rapid validation before commissioning fieldwork
- The client has existing secondary data (sales records, CRM data, website analytics) that can anchor the AI output

### Commission primary research instead when:

- Launching a new product in an unfamiliar market where AI training data is likely thin
- The decision at stake is high-value — above UGX 50 million in campaign or product investment
- There is reason to believe AI training data underrepresents the target audience (e.g. rural low-income segments, elderly populations, niche occupational groups)
- The client has had prior strategy failures that suggest existing assumptions are wrong

### Always:

- Disclose the synthetic origin of personas in all deliverables (see Citation Standard)
- Flag every assumption that could not be cross-referenced against secondary data
- Treat synthetic personas as a starting point, not a conclusion

---

## Uganda / East Africa Calibration

Apply this demographic and behavioural context when constructing prompts. Adjust for the specific country and city provided by the client.

**Income bands (UGX per month):**

| Band | Monthly Income |
|---|---|
| Low income | Under UGX 500,000 |
| Lower-middle income | UGX 500,000 – 1,500,000 |
| Middle income | UGX 1,500,000 – 5,000,000 |
| Upper-middle income | Above UGX 5,000,000 |

**Platform norms:**

- **WhatsApp** — primary communication channel across all income levels; business enquiries, referrals, and purchase decisions frequently happen via WhatsApp groups and DMs
- **Facebook** — broadest reach; urban and peri-urban, 18–55+, all income levels
- **TikTok** — fast-growing, urban youth 16–30, entertainment-first
- **LinkedIn** — formal sector professionals, NGO workers, senior management, B2B audiences
- **YouTube** — research, tutorials, long-form; consumed when users have Wi-Fi access

**Trust landscape:**

- Word-of-mouth and community recommendations carry high weight; formal advertising is viewed with scepticism by many segments
- Social proof from peers and WhatsApp group endorsements consistently outperforms broadcast advertising
- Localisation — local language, local place names, local events — drives significantly higher engagement than generic international content

**Language:**

- Most urban Ugandans code-switch between English and Luganda; formal communications default to English
- Luganda phrases in captions or CTAs can increase relatability for Kampala-based mass-market audiences
- Kiswahili is the appropriate local language calibration for Kenya and Tanzania

---

## Structured Prompt Template

Use this prompt to generate one persona. Replace all bracketed placeholders with the client's specific details before running. Run the prompt once per persona.

```
You are a market researcher specialising in Uganda/East Africa consumer behaviour.

Generate a detailed audience persona for a [industry] business targeting
[audience description] in [location].

Include:
- Name and age
- Occupation and income range (in UGX)
- Education level
- Primary social media platforms used and how (passive/active, time of day)
- WhatsApp usage (personal/business, groups joined, typical message patterns)
- Daily routine (morning to evening — brief)
- Top 3 pain points related to [product/service category]
- Top 3 goals or aspirations related to [product/service category]
- Barriers to purchase or engagement
- Preferred content format (video, text, image, audio)
- Language and register preferences (formal English, casual English, Luganda, Kiswahili)
- Trusted information sources (family, WhatsApp groups, Facebook, radio, newspaper)
- A direct quote that captures their attitude toward [brand/product category]
```

Add the Uganda/EA Calibration data above to the prompt when working on Ugandan clients to anchor the AI output in realistic local context.

---

## 3-Persona Output Format

Generate three distinct personas per engagement. Do not generate all three using the same demographic profile — vary income, age, or use case meaningfully.

**Primary persona** — the highest-value or most common customer segment; the person the strategy is primarily built around.

**Secondary persona** — the second priority segment; often a different demographic or a distinct use case (e.g. a gifter rather than an end user, or a B2B decision-maker alongside a B2C buyer).

**Edge persona** — a segment the client may be overlooking; often a future growth opportunity, an underserved demographic, or a non-obvious use case. Flag explicitly that this persona represents a growth hypothesis.

### Output structure for each persona:

| Field | Detail |
|---|---|
| **Name** | Realistic EA name (e.g. Harriet, Brian, Fatuma, Ronald, Aisha) |
| **Archetype label** | A specific label for this client's context (e.g. "The Growth-Minded SME Owner") |
| **Day in the Life** | Three sentences: morning, workday, evening — grounded in this persona's specific circumstances |
| **Content preferences** | Two to three specific formats with examples relevant to the client's category |
| **Messaging triggers** | Three specific reasons this persona would engage with or buy from the client |
| **Primary platforms** | The one or two platforms where this persona is most reachable and most likely to act |
| **Key barriers** | Two to three specific obstacles to purchase or engagement |

After the three persona cards, produce a **side-by-side summary table** using the fields above for quick team reference.

---

## Synthetic Focus Group Technique

Simulate audience reactions to campaign concepts before investing in creative production. Use this technique for messaging validation and campaign brief development.

**Run this prompt for each of the three personas:**

```
You are [Persona Name], a [description — occupation, age, income, location].

The brand [Client Name] is about to launch [campaign concept — one sentence].

Answer the following:
1. What is your first reaction to this campaign?
2. What would make you engage with it (like, comment, share, visit, buy)?
3. What would put you off or make you scroll past?
4. What would you tell a friend about this brand after seeing this campaign?
```

**Analyse the three responses to identify:**

- Universal appeal — elements that resonate across all three personas
- Segment-specific messaging — elements that work for one persona but not others
- Red flags — anything that alienates more than one persona
- Gaps — something the campaign does not address that multiple personas care about

Document the synthetic focus group findings as a table: Persona | Reaction | Engage trigger | Turn-off | Verdict. Include this table in the strategy or campaign brief alongside the disclosure footnote.

---

## Validation Checklist

Complete this checklist before using synthetic personas in any client-facing strategy document. Record the outcome of each check as: Validated / Partially validated / Unvalidated — assumption retained.

- [ ] Cross-reference age and income assumptions against Uganda Bureau of Statistics household survey data or equivalent national statistics authority for the relevant country
- [ ] Check platform usage assumptions against GSMA Mobile Economy Sub-Saharan Africa report (most recent edition)
- [ ] If the client has a Facebook Page, run Meta Audience Insights for Uganda to check age, gender, and location breakdowns against persona assumptions
- [ ] Run at least one real interview or WhatsApp conversation with a person who matches each persona profile — even one conversation per persona adds significant validation
- [ ] Note any assumptions that could not be validated and flag these explicitly as risks in the strategy document

For each unvalidated assumption, add a bracketed risk note in the strategy: *[Assumption: [description]. Validate before campaign launch.]*

---

## Citation Standard

**In every client-facing deliverable that uses synthetic personas, include the following footnote verbatim:**

> Audience personas were generated using AI (Claude/ChatGPT) based on secondary data and market knowledge. They represent informed hypotheses, not primary research findings. Assumptions that could not be cross-referenced against secondary data are flagged within the document.

**Additional rules:**

- Never present synthetic personas as "research findings" in a proposal or strategy without the disclosure footnote
- In presentation decks, add the disclosure to the slide footer or speaker notes of every slide that references a persona
- If the client requests that the disclosure be removed, explain the professional and reputational risk and decline; if they insist, note the removal in the project file

---

## Quality Criteria

- Three distinct personas generated — primary, secondary, and edge — with meaningfully different demographics or use cases
- Each persona uses the full structured output format with all fields completed; no field left blank without explanation
- Uganda/EA calibration applied — income expressed in UGX, platform norms accurate for the target city, language preferences noted
- Synthetic focus group run for at least one campaign concept with a completed four-column analysis table
- Validation checklist completed with an explicit outcome recorded for each item
- All unvalidated assumptions flagged with bracketed risk notes in the deliverable
- Citation standard applied — synthetic origin disclosure included verbatim in every client-facing document
- At least one secondary data source (UBOS, GSMA, Meta Audience Insights) cross-referenced and cited

---

## References

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford University Press.
- Farri, E. and Rosani, G. (2025) *HBR Guide to Generative AI for Managers*. Harvard Business Review Press.
- Randazzo, G.W. (2024) *Winning Marketing Strategies Using Generative AI*. Business Expert Press.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.
