---
name: ai-generative-search-optimisation
description: Optimise client content for AI-native search engines and LLM citation. Invoke when a client wants their brand and content to appear in ChatGPT, Perplexity, Google AI Overviews, and other generative search results, or when auditing existing content for AI-readiness.
---
# AI Generative Search Optimisation (GEO)

Generative Engine Optimisation (GEO) is the discipline of structuring and writing content so that large language models (LLMs) cite it when answering user queries. This skill guides an audit of existing content, a rewrite using GEO principles, and the setup of an ongoing monitoring protocol.

---

<!-- dual-compat:start -->
## Use when
- Optimise client content for AI-native search engines and LLM citation. Invoke when a client wants their brand and content to appear in ChatGPT, Perplexity, Google AI Overviews, and other generative search results, or when auditing existing content for AI-readiness.
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
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask the client for the following before generating any deliverable:

1. **Client business name** — the trading name used publicly
2. **Industry** — e.g. financial services, agriculture, retail, hospitality, professional services
3. **Country/city** — default: Uganda. Specify city if relevant (Kampala, Entebbe, Jinja, Gulu)
4. **Primary content channels** — website, blog, social media, WhatsApp, or a combination
5. **Current SEO status** — none / basic (title tags, meta descriptions) / advanced (structured data, regular publishing)
6. **Primary goal** — select one:
   - Brand visibility in AI search
   - Product or service discovery
   - Thought leadership and authority
   - Local business discovery (Google Maps, Gemini local answers)

---

## GEO vs SEO — What Changes

Traditional SEO and Generative Engine Optimisation share some foundations but differ in what they optimise for.

**Traditional SEO** optimises for keyword rankings in Google's blue-link results. Success is measured by page position, click-through rate, and organic traffic. The algorithm ranks pages; the user chooses which to click.

**Generative Search Optimisation (GEO)** optimises for citation in AI-generated answers from ChatGPT, Perplexity, Google AI Overviews, and Gemini. Success is measured by whether the brand is mentioned in the AI's response — not whether the user clicks a link. The LLM synthesises content from multiple sources and presents a single answer; if the brand is not cited, it is invisible.

**Key difference:** SEO optimises for algorithms that rank pages. GEO optimises for LLMs that synthesise and cite content.

**Why it matters:** Roth and neuroflash (2024) predict that by 2025, 30% of all discovery queries will go through AI-native interfaces. Brands not cited in AI answers lose visibility regardless of their Google ranking. A brand can rank number one on Google and still be absent from the AI answer that most users read first.

**East Africa relevance:** GEO is forward-looking for Uganda in 2026, but growing fast as urban professionals adopt ChatGPT and Gemini for research. Brands that invest now in GEO-ready content build a durable advantage as AI search adoption accelerates across East Africa. Crucially, GEO foundations — clear structure, explicit facts, author attribution — improve traditional SEO simultaneously at no additional cost.

---

## How LLMs Decide What to Cite

LLMs do not rank pages. They extract, synthesise, and attribute information from content they have been trained on or can retrieve. Prefer content that is:

1. **Factually accurate** — LLMs avoid inaccurate sources to protect the reliability of their answers. Unverifiable claims and marketing hyperbole reduce citation probability.
2. **Clearly attributed** — content with a named author, organisation, and publication date is preferred over anonymous or undated content. Attribution signals accountability.
3. **Well-structured** — headings, bullet points, numbered lists, and explicit definitions help LLMs extract and summarise information efficiently.
4. **Concise and direct** — LLMs favour content that states its point clearly in the first sentences, not content that buries the answer in padding or preamble.
5. **Authoritative** — content linked to from other credible sources signals trustworthiness. Being cited by others increases the likelihood of being cited by AI.
6. **Regularly updated** — LLMs deprioritise stale content. A visible "Updated March 2026" note signals currency and reliability.

---

## Content Structure for LLM Citation

Apply these structural principles to all new and revised content:

- **Open with a direct answer** — state the key point in the first two sentences. Do not bury the answer after lengthy context-setting.
- **Use H2 and H3 headings as question-and-answer pairs** — for example: "What is social commerce?" / "How does social commerce work in Uganda?" Headings framed as questions match the query format LLMs process.
- **Include a FAQ section** at the bottom of every article or web page. FAQs are a primary source for AI-generated answers because they are already structured as question-and-answer pairs.
- **Define key terms explicitly** — for example: "Social commerce refers to the direct purchase of products through social media platforms without leaving the app." Explicit definitions are extracted verbatim by LLMs.
- **Use numbered lists for processes** and bullet points for features or benefits. Structured lists are easier for LLMs to parse than dense paragraphs.
- **Include a one-paragraph summary at the top of long articles** — LLMs frequently extract this paragraph for their answer. Write it as if it will be read in isolation.
- **Add publication date and last-updated date** to all content. Place these in a visible, consistent location — below the title or at the top of the article body.

---

## Machine-Readable Brand Content

As consumers use AI agents to research and make purchase decisions, brands must be readable by machines as well as humans. Venkatesan and Lecinski (2026) argue that brand content must answer the questions an AI agent will ask on behalf of a consumer before a human ever sees the response.

Audit the following elements for each client:

- **Pricing** — is it explicitly stated on the website? "Contact us for pricing" is a citation dead end. State price ranges at minimum.
- **Product and service features** — are they listed in plain, structured language? Avoid marketing adjectives; use factual descriptions.
- **Brand values** — are they stated clearly and factually, not just as slogans? "We deliver orders within 24 hours in Kampala" is citable. "We are passionate about excellence" is not.
- **Business information** — address, opening hours, and contact details in structured format. Use Schema.org markup where technically possible; at minimum, present this information in consistent, clean HTML.
- **Customer reviews** — are they present and accessible to crawlers? Reviews are strong citation signals. Testimonials buried in images or JavaScript cannot be read by LLMs.
- **Differentiators** — is the answer to "why choose [brand] over competitors?" clearly and factually stated? Phrase this as a direct answer, not a tagline.

---

## GEO Content Audit — 10-Point Checklist

For each key page or article, score Yes (1) or No (0). Apply to the homepage, top five traffic pages, and any page central to the primary goal.

| # | Criterion | Y/N |
|---|---|---|
| 1 | Does the content open with a direct, concise answer to its primary question? | |
| 2 | Are headings structured as questions or clear topic statements? | |
| 3 | Is there a FAQ section? | |
| 4 | Are key terms defined explicitly? | |
| 5 | Is the author or organisation named? | |
| 6 | Is the publication or last-updated date visible? | |
| 7 | Are prices and key facts stated explicitly — not hidden behind forms or "contact us"? | |
| 8 | Is the content free of vague marketing language ("world-class", "best in class", "cutting-edge")? | |
| 9 | Does the page include structured data markup or at least clean HTML heading hierarchy? | |
| 10 | Is the content factually accurate and verifiable? | |

**Scoring guide:**
- **8–10:** GEO-ready. Maintain and monitor.
- **5–7:** Moderate. Prioritise revisions to criteria scored No.
- **Under 5:** High priority. Revise before investing further in content production.

---

## Content Creation Guidelines for GEO

Apply these guidelines when writing all new content for a GEO-focused client:

- **Lead with the answer** — write the key point in the first two sentences. Assume the reader — human or LLM — may read only the opening.
- **Write for the question** — identify the exact question a user would type into ChatGPT and structure the entire piece to answer it completely. One piece of content, one question.
- **Cite credible sources** — reference secondary sources, industry data, and named experts. LLMs trust content that itself cites sources; it signals the content meets an evidential standard.
- **Eliminate filler** — padding reduces citation probability. Every sentence must add a specific piece of information. Cut sentences that merely restate or introduce.
- **Use specific numbers** — "63% of marketers report improved conversion rates with AI personalisation" is more citable than "most marketers see improvement." Specificity signals research.
- **Write locally** — "In Uganda, WhatsApp is the dominant customer service channel, used by over 90% of smartphone owners" is more specific and citable than a generic global claim. Local specificity also increases relevance for regional AI queries.
- **Keep paragraphs short** — three to four sentences maximum. Long paragraphs are harder for LLMs to parse and summarise accurately.

---

## Monitoring Brand Mentions in AI Search

No dedicated tool is required. Set up a manual monitoring protocol on a recurring schedule.

**Monthly — run 5 queries per tool:**
- Select five queries a potential customer would use to find the client's category. Examples for a Kampala law firm: "best corporate lawyers in Kampala", "business registration lawyer Uganda", "how to register a company in Uganda".
- Run each query in ChatGPT, Perplexity, and Google Gemini.
- Record: date, query, tool, brand mentioned (Y/N), what was said, competitors mentioned, overall sentiment.

**Quarterly — review tracking data:**
- Is citation frequency improving across all three tools?
- Are any competitors gaining ground in AI answers?
- Are any factual errors about the brand appearing in AI responses?
- Has new content published this quarter been cited?

**Alert trigger:** if the brand is mentioned negatively or inaccurately in an AI answer, treat it as a reputation management priority. Publish a clear, factual correction on the brand's own properties — LLMs re-index frequently and will incorporate accurate content over time.

**Tracking spreadsheet columns:**
Date | Query | Tool | Brand Mentioned (Y/N) | Quote or Summary | Competitors Cited | Sentiment | Action Required

---

## EA Relevance Note

GEO is a two-to-three year horizon for most Ugandan businesses. AI search adoption is concentrated among urban professionals and is growing fastest in Kampala and among younger demographics who use ChatGPT for research tasks.

However, invest in the structural foundations now. Clear headings, explicit facts, FAQ sections, and author attribution cost nothing extra and improve traditional Google SEO simultaneously. Brands that build GEO-ready content in 2026 will hold a compounding advantage as AI search adoption grows across East Africa.

Do not overpromise to clients. Frame GEO work as: "We are building content that performs well in today's Google results and will be well-positioned when AI search becomes mainstream in this market."

---

## Quality Criteria

Good output from this skill meets all of the following standards:

- GEO content audit completed — all key pages scored on the 10-point checklist with clear Y/N decisions
- Priority pages identified for revision — all pages scoring under 5 flagged with specific improvement notes against each failed criterion
- Content creation guidelines applied — new content drafted for the client follows all seven GEO writing guidelines, verifiable sentence by sentence
- Machine-readable brand content audit completed — pricing, features, values, business information, and differentiators all explicitly stated or flagged for update
- Monthly AI search monitoring protocol set up — tracking spreadsheet template provided with five seed queries written for the client's specific category
- At least one piece of existing content revised using GEO principles, re-audited on the 10-point checklist, and score improvement documented
- EA relevance framing applied throughout — no overpromising on immediate GEO impact for Ugandan SMEs; framed as a durable foundation investment

---

## References

- Roth, H. and neuroflash (2024) *AI Strategy 2025 for Marketing Teams*. neuroflash.
- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford University Press.
