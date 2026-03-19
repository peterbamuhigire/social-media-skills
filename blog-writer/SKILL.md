---
name: blog-writer
description: Write a complete, publication-ready blog post from a content brief. Produces the full article text with SEO title, meta description, body with H2/H3 structure, and a closing CTA. Use when the user says "write a blog post", "write a blog article", "write about [topic]", or provides a content brief and wants a finished article. Output is a standalone markdown document — no web page building, no image pipelines.
---

# Blog Writer

Generate a complete, professional blog post from a brief. The output is a finished article in markdown — ready to paste into a CMS, share with a client, or hand to a web developer.

## Required Input

Ask for these before writing:

1. **Client business name and industry**
2. **Country / city** (default: Uganda/East Africa)
3. **Article topic or working title**
4. **Target reader** — who is this for? (job role, situation, problem they have)
5. **Search intent** — are they looking to learn, compare, or decide?
6. **Key questions** the article must answer (3–5)
7. **Word count target** (default: 1,200–1,800 words)
8. **Call to action** — what should the reader do at the end?
9. **Tone** — professional / conversational / authoritative (default: professional)

If any input is missing, ask before writing. Do not guess intent.

## Article Structure

Generate in this order:

### Frontmatter block
```
Title: [SEO-optimised title, under 60 characters, primary keyword included]
Meta description: [Under 155 characters, includes primary keyword and location]
Primary keyword: [The main search phrase this article targets]
Secondary keywords: [2–3 related phrases]
Estimated read time: [X min read at 200 words/min]
```

### Article body

1. **Opening hook** (1–2 paragraphs) — do not open with a definition or generic statement. Use one of: a specific scenario the reader recognises, a surprising fact, a question that surfaces a real problem, or a short story with a lesson.
2. **Nut paragraph** — if the opening uses a story or scenario, follow it immediately with a grounding paragraph that states what the article covers and why it matters.
3. **Body sections** — 4–7 H2 sections. Each section answers one of the key questions provided. Use H3 subheadings where a section has distinct sub-topics.
4. **Practical takeaways** — at least one section must give the reader something concrete to act on (a checklist, a decision framework, a step-by-step).
5. **Conclusion** — reconnect to the opening (full-circle structure). End with a natural, non-pushy CTA.

## Writing Standards

Apply the `east-african-english` skill for language and tone. Also:

- **British spelling** — organisation, programme, colour, analyse, recognise
- **Active voice** — 90%+ of sentences. Passive only when the actor is unknown.
- **Sentence variety** — mix short (8–12 words) and medium (20–28 words). No sentence over 35 words.
- **One idea per paragraph** — 2–4 sentences each.
- **Concrete and specific** — use numbers, named places, real examples. No vague abstractions.
- **No AI vocabulary** — never use: delve, tapestry, landscape (metaphorical), leverage, navigate (metaphorical), foster, realm, game-changer, revolutionary, groundbreaking.
- **No filler phrases** — cut: "in order to" → "to", "due to the fact that" → "because", "it is important to note that" → state it directly.
- **No weak modifiers** — cut: really, very, quite, basically, actually, somewhat.
- **Take positions** — at least 2 clear opinions or recommendations per article. "I recommend" not "one might consider".
- **Commit, do not hedge** — "This approach works for SMEs" not "This could potentially be a viable option".

## SEO Requirements

- Primary keyword in: title, first 100 words, at least one H2, and the conclusion.
- Secondary keywords distributed naturally through body. Never keyword-stuff.
- Internal linking suggestions: note 2–3 places where the client could link to related pages (service pages, about, contact) — mark as `[LINK: suggested anchor text → page type]`.
- External links: suggest 1–2 authoritative sources to cite where data or claims need backing.

## Platform Adaptation Notes

If the article will be shared as social content after publication, include at the end:

**Social cut-downs:**
- LinkedIn post (150 words) — professional tone, key insight as the hook
- Facebook post (80 words) — warmer, question-led
- X/Twitter thread opener (280 characters) — bold claim or surprising fact

Only include this section if the user requests it.

## Quality Criteria

Good output meets all of these:

- [ ] Opening hook captures attention without being generic or clichéd
- [ ] Every H2 section answers a real question the target reader would have
- [ ] At least one section provides a concrete, actionable takeaway
- [ ] No banned vocabulary or filler phrases
- [ ] Primary keyword placed naturally in title, opening, at least one H2, and conclusion
- [ ] British spelling throughout
- [ ] Conclusion reconnects to the opening and includes a clear CTA
- [ ] Tone matches the client's industry and the East African professional register
- [ ] Article reads as written by a human with genuine expertise, not as generated content

## References

| File | When to Read |
|---|---|
| `references/human-voice-standards.md` | If the article risks sounding generic or AI-generated — run the voice checklist |
| `references/writing-craft.md` | For sentence structure, opening hook techniques, paragraph rhythm |
| `references/editorial-standards.md` | For punctuation, capitalisation, and grammar rules |
| `east-african-english/SKILL.md` | For tone calibration, British English spelling list, courteous phrasing |
