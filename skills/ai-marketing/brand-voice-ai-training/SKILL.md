---
name: brand-voice-ai-training
description: Use when AI tools write off-brand or generic copy for a client and need teaching the brand's voice and facts; produces a brand context block with few-shot examples and a RAG brand knowledge base of products, UGX prices, policies and personas; not for defining the brand voice itself (use `04-brand-voice-intake`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Brand Voice AI Training

Builds the Brand Context Block, a structured prompt header pasted before every AI instruction, so Claude, ChatGPT, Gemini or any later tool writes in the client's voice instead of a bland global register. Untrained, repeated AI use smooths out the local references, signature phrases and particular warmth or edge that make a brand recognisable.

<!-- dual-compat-start -->
## Use When
- ChatGPT, Claude or Gemini writes our posts in a bland global tone; make it sound like our brand.
- Build a brand context block to paste before every AI prompt, with voice adjectives, we-are-not pairs, always and never words and emoji rules.
- Create few-shot examples for captions, emails, WhatsApp Status and DM replies from the client's best existing content.
- Set up a RAG brand knowledge base in Claude or ChatGPT Projects, CustomGPT or Notion AI with the product catalogue, UGX prices, policies and personas so AI drafts stay accurate.
- The AI keeps getting prices or policies wrong; set up a maintenance routine for the knowledge base.

## Do Not Use When
- `04-brand-voice-intake` for defining the brand voice and visual direction in the first place.
- `prompt-engineering-library` for reusable task prompts for images, audio and video.
- `anti-ai-slop` for humanising a single AI draft.
- Stop before uploading customer personal data, confidential pricing or unverified facts into an AI tool without client authority.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name, industry, country/city and primary goal for consistent AI content | Client, or `04-brand-voice-intake` answers | Yes | Pull from `04-brand-voice-intake` first; default the location to Uganda/East Africa only when it is not stated. |
| 3–5 sample pieces the client considers most "them", collected in ranked source priority | Client archive: posts and threads, longer-form pieces, outbound messages that worked, then docs/site copy | Yes | Proceed with fewer than three only by stating the thin corpus in the analysis note; never substitute a generic platform exemplar, competitor post or invented example. |
| Voice fields: exactly 3 adjectives, 3 "We are X, not Y" pairs, 5–10 always-use and 5–10 never-use words, tone position 1–5 with one example sentence, emoji policy | Client or `04-brand-voice-intake` | Yes | Go back and ask; never leave a field blank or fill it with a placeholder. |
| Cultural references: local-language phrases (Luganda, Swahili, Runyankole or others), slang, local events, seasons, community structures | Client | Yes | Ask explicitly; delete the CULTURAL CONTEXT field only when the client confirms none apply. |
| Content types needing few-shot examples and 1–2 approved examples of each | Client | Yes | Skip a type only when the client does not produce it (for example no Stories or WhatsApp Status). |
| Products, UGX prices, policies, personas and local calendar | Client source documents | Conditional (knowledge base) | Build the voice block only and mark factual accuracy `not assessed`. |

## Workflow

1. Capture the voice inputs, pulling from `04-brand-voice-intake` where it exists; collect samples in ranked source priority and stop once 3–5 strong pieces are in hand, dropping a tier only when the current one is genuinely exhausted.
2. Analyse the samples for what the voice actually is (sentence length, questions, address, active voice, recurring phrases, hook, CTA, humour, local-language positions and what the author never does) and record an internal analysis note.
3. Build the Brand Context Block from the [template](references/brand-context-block-method.md) with every field filled, at least three verbatim examples, and the standard AI vocabulary ban list appended after client-specific bans.
4. Add a STYLISTIC BANS field only for highly distinctive voices; for standard SME clients keep the observation in the internal note.
5. Source few-shot examples per content type (caption, email opening, Story/WhatsApp Status script, positive-comment and neutral-enquiry replies, long-form opening) and store them in one labelled reference document.
6. Run the quality test and the two-method voice replication comparison; if the output fails any check, add verbatim examples, sharpen NEVER USE and the "We are X, not Y" pairs, then rerun until the block passes, and label the passing version v1.
7. Where the AI must also know products, prices, policies or personas, build the RAG knowledge base with the block loaded as one of its documents.
8. Store the block as `[ClientName]-brand-context-v1.txt` in the client's project folder, agree a quarterly review and hand over; stop before uploading personal data, confidential pricing or unverified facts to an AI tool without client authority.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Brand Context Block (versioned `.txt`) | Anyone prompting AI tools for the client | Every field filled from real inputs; three or more verbatim examples; standard ban list present in full; only the PLATFORM field changes per session. |
| Few-shot example document | Content team | Covers every content type the client regularly produces, labelled by type. |
| RAG brand knowledge base (when triggered) | Client content and service team | Built from the seven-category library with the block loaded as one document. |
| Review schedule and version log | Client owner | Quarterly review agreed; previous versions kept for reverting. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Sample source log and analysis note | Internal note: tier of each sample, extracted patterns, what the author never does | Tier drops and a thin corpus are stated, never padded. |
| Quality test record | Table: prompt, output, checks passed or failed, refinement, version | The passing version is recorded as v1 (or the next increment). |
| Method 1 vs Method 2 comparison | Paired outputs with a verdict | States which method replicated the voice more accurately. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Uploading customer personal data, confidential pricing or unverified facts into an AI tool or project also needs that authority.

## Degraded Mode

Without real client sample content, return the narrowest qualified result and mark the affected checks `not assessed`. A block with the voice fields, the standard ban list and a flagged empty EXAMPLES OF OUR VOICE field can still be delivered, marked not ready for live client work.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client describes a voice that the samples do not show | Build the block from what the samples actually show and record the gap in the analysis note. | An aspirational voice the AI cannot reproduce. |
| Fewer than three genuine samples exist | Say so, proceed with the reduced set and flag the block for revisiting once more real content exists. | A padded, contaminated corpus. |
| The best-performing post is not the most representative | Choose the piece that sounds most like the client; performance and authenticity do not always overlap. | Training on an outlier. |
| The voice is highly distinctive (founder style, cult following, known stylistic signatures) | Add the STYLISTIC BANS field built from the "what the author never does" observations. | Structural habits the vocabulary scanner cannot catch. |
| The quality test output feels generic | Add more verbatim examples first; this is almost always the fix. | Refining adjectives while the real gap stays. |
| The client rebrands, launches a distinct product line or voice drift appears | Update the block, increment the version (v1 → v2) and keep the previous version. | A stale block producing textbook copy. |
| The AI must also know the client's products, UGX prices, policies, audience or local calendar, or the brief asks for a RAG brand knowledge base | Build the seven-category document library and query workflow in [brand-knowledge-base-rag](references/brand-knowledge-base-rag.md); load the Brand Context Block as one of its documents. | Generic or factually wrong AI output that no voice block can fix. |

## Quality Standards

- The Brand Context Block is complete: no field is blank or holds a placeholder, and every required input is represented.
- EXAMPLES OF OUR VOICE holds at least three verbatim, unedited client pieces; no generic platform exemplar, competitor post or invented example appears.
- The standard AI vocabulary ban list is present in full, with client-specific terms added above it.
- A quality test has been run and documented, and the block refined until AI output is indistinguishable in voice from the client's approved content.
- Few-shot examples cover every content type the client regularly produces, stored and labelled separately.
- Local language, cultural references and EA-specific identity markers are preserved explicitly in the block, not left to the AI to infer.
- The block is versioned, stored in the client's project folder, platform-agnostic in its fixed fields, with a review schedule agreed (quarterly minimum).
- The analysis note records what the author never does and states any drop in sample tier or a thin corpus; the full 11-item checklist is in the [method reference](references/brand-context-block-method.md).

## Anti-Patterns

- Writing the block from the client's self-description alone. Fix: analyse the samples and build from what they actually show.
- Paraphrasing or "improving" the voice examples. Fix: paste real content verbatim.
- Two voice examples in the block. Fix: provide at least three; two produce inconsistent voice replication (Evelyn, 2025, p.71; Mizrahi, 2024).
- Padding a thin archive with a stock "high-performing Instagram caption". Fix: state the thin corpus and revisit later.
- Dropping local-language phrases because the AI prefers Standard English. Fix: list them in CULTURAL CONTEXT and check the test output for them.
- Overwriting the block on each update. Fix: increment the version and keep old versions; reverting is sometimes necessary.

## References

- [Brand Context Block build method](references/brand-context-block-method.md): read when collecting and analysing samples, filling the template, adding STYLISTIC BANS or few-shot examples, running the quality and comparison tests, or maintaining versions.
- [brand-knowledge-base-rag](references/brand-knowledge-base-rag.md): read when the client needs an AI knowledge base (Claude/ChatGPT Projects, CustomGPT, Notion AI) grounded in brand, product, policy and East African market documents.
- [`04-brand-voice-intake`](../../pipeline/04-brand-voice-intake/SKILL.md): read when the brand voice itself is not yet defined.
- [Anti-AI slop production gate](../anti-ai-slop/SKILL.md): read when testing block output and when a single AI draft needs humanising.
- [`ai-readiness-diagnostic`](../ai-readiness-diagnostic/SKILL.md): read when the client's wider AI or data readiness is in doubt before tools are trained.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->
