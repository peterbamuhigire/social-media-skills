---
name: brand-voice-ai-training
description: >
  Captures a client's authentic brand voice and encodes it into a reusable Brand Context Block — a standardised prompt header pasted at the start of every AI session to ensure consistent, on-brand output across all content types and platforms. Invoke at the start of every new client relationship, before any AI-assisted content is produced. Update whenever the client rebrands or when voice drift is detected in AI-assisted output.
---
# Brand Voice AI Training

<!-- dual-compat:start -->
## Use when
- Captures a client's authentic brand voice and encodes it into a reusable Brand Context Block — a standardised prompt header pasted at the start of every AI session to ensure consistent, on-brand output across all content types and platforms. Invoke at the start of every new client relationship, before any AI-assisted content is produced. Update whenever the client rebrands or when voice drift is detected in AI-assisted output.
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

## Why This Matters

AI tools default to a generic global register. The output is professional, grammatically correct, and completely bland. Left untrained, repeated AI use gradually smooths out a brand's authentic character — the local references, the signature phrases, the particular warmth or edge that makes a brand recognisable.

The **Brand Context Block** is the solution. It is a structured prompt header, pasted before every AI instruction, that gives the tool the context it needs to write in the client's voice rather than in the voice of a marketing textbook. One well-built block transforms every AI session for this client.

Without it: every session starts from scratch. Generic output. Client frustration.
With it: consistent, on-brand content from the first line, every time.

This skill works with any AI tool — Claude, ChatGPT, Gemini, or any future equivalent.

---

## Required Inputs

Before beginning, collect or confirm the following. If `04-brand-voice-intake` has already been completed for this client, pull the relevant answers from there rather than asking again.

| Input | Detail |
|---|---|
| Client business name | Trading name as used publicly |
| Industry | Sector and sub-sector |
| Country / city | Defaults to Uganda/East Africa if not specified |
| Primary goal | What this client most needs consistent AI content for |
| Sample content | 3–5 pieces of existing content that feel most "them" — posts, emails, web copy, WhatsApp messages |
| Voice adjectives | Exactly 3 adjectives describing the brand voice |
| We are / not pairs | 3 pairs: "We are [X], not [Y]" |
| Always-use vocabulary | 5–10 words or phrases the brand always uses |
| Never-use vocabulary | 5–10 words or phrases the brand avoids |
| Tone position | Where on the scale: Formal ←→ Conversational |
| Cultural references | Local language phrases, local slang, community references central to their identity |
| Emoji policy | Yes / No / Limited (and if limited, which contexts) |
| Content types produced | Which formats need few-shot examples: captions, emails, Stories/WhatsApp Status, DM replies, other |

---

## Step 1 — Capture the Voice Inputs

Ask the client for each item in the Required Inputs table above, or pull from `04-brand-voice-intake`.

**On sample content:** the 3–5 pieces must be content the client themselves considers most representative — not the highest-performing post, but the one that sounds most like them. Performance and authenticity do not always overlap.

**On cultural references (EA-specific):** ask whether the brand uses local language phrases (Luganda, Swahili, Runyankole, or others depending on region), local slang, references to local events, seasons, or community structures. These are often the most distinctive elements of an East African brand voice and the first things a generic AI strips out. Preserve them explicitly.

**On tone position:** use a simple five-point label to avoid ambiguity:

1. Formal — professional, measured, institutional
2. Mostly formal — professional with occasional warmth
3. Balanced — professional but approachable
4. Mostly conversational — warm, direct, light
5. Conversational — casual, familiar, energetic

Ask the client to pick one, then ask for a single sentence from their existing content that best represents that tone.

---

## Step 2 — Analyse the Sample Content

Do not rely solely on what the client tells you their voice is. Read the sample content and extract what it actually is. Clients often describe an aspirational voice, not their real one.

Analyse the samples for:

- **Sentence length** — are most sentences under 15 words, or longer and more considered? Count roughly.
- **Questions vs. statements** — how frequently do they open with a question? What kind of question — rhetorical, direct, invitational?
- **How they address the customer** — "you", "our community", first name, "fellow [identity]", or something else?
- **Active vs. passive voice** — count active constructions vs. passive. Most strong brand voices are predominantly active.
- **Recurring phrases** — are there phrases or sentence structures that appear more than once across the samples? These are signature patterns and must be preserved.
- **Hook style** — how do posts open? With a claim, a question, a number, a story, a challenge?
- **CTA style** — how do posts close? Soft invitation, direct instruction, question, emotional close?
- **Humour or wit** — present or absent? If present, what type — self-deprecating, dry, warm, playful?
- **Local language use** — if present, in which positions (opening hook, emphasis, sign-off) and how frequently?

Record findings in a short analysis note before building the block. This is internal reference — not delivered to the client.

---

## Step 3 — Build the Brand Context Block

The Brand Context Block is the deliverable. Produce it using the template below, populated with everything gathered in Steps 1 and 2.

```
BRAND CONTEXT — [Client Name]
You are writing for [Business Name], a [one-sentence description] based in [location].

VOICE: [Adjective 1], [Adjective 2], [Adjective 3].
We are [X], not [Y].
We are [X], not [Y].
We are [X], not [Y].

TONE: [Tone level 1–5 with label]. Example of our tone: "[paste one sentence from their content]"

ALWAYS USE:
- [Signature phrase or word]
- [Signature phrase or word]
- [Signature phrase or word]
- [Signature phrase or word]
- [Signature phrase or word]
[Add up to 10 total]

NEVER USE:
- [Client-specific banned word or phrase]
- [Client-specific banned word or phrase]
- [Client-specific banned word or phrase]
[Add client specifics, then append the standard ban list below]
- delve
- tapestry
- landscape (when used metaphorically)
- leverage
- navigate (when used metaphorically)
- foster
- realm
- game-changer
- revolutionary
- groundbreaking
- comprehensive
- robust
- seamlessly
- "in today's digital age"
- "in the ever-evolving world of"
- "it is worth noting"
- "it is important to note"
- furthermore
- moreover

AUDIENCE: [Who they are writing for — demographic, what they care about, what they already know, what language they use]

PLATFORM: [Platform this session is for — Facebook / Instagram / LinkedIn / WhatsApp / X / email / other]

CULTURAL CONTEXT: [Local language phrases in use, regional references, community identity markers — delete this field if none apply]

EMOJI POLICY: [Yes — use freely / No — do not use / Limited — use only in [specified contexts]]

EXAMPLES OF OUR VOICE:
"[2–3 sentences from their best existing content — paste verbatim, do not edit]"

TASK: [The specific content request follows here]
```

**Critical notes on the template:**

- Every field is mandatory. If a client has not supplied a value, go back and ask rather than leaving it blank or inventing a placeholder.
- The EXAMPLES OF OUR VOICE field is the most important field in the block. Paste real, verbatim content. This single section does more work than all the adjectives combined.
- **Minimum three examples standard** (Source: Evelyn, 2025, p.71; Mizrahi, 2024): Provide a minimum of three separate examples in the EXAMPLES OF OUR VOICE field. Two examples produce inconsistent voice replication. Three or more enable the AI to reverse-engineer voice characteristics reliably — including sentence rhythm, structural habits, and register — that cannot be described in words alone. Fewer than three examples is the most common reason a Brand Context Block underperforms on live client work.
- The PLATFORM field changes with every session. Keep the rest of the block fixed and update only this field when switching platforms.
- The standard AI vocabulary ban list is included in every block for every client, without exception. Add client-specific banned terms on top of it.

---

### Character-Voice Differentiation (Highly Distinctive Brands)

Source: Donovan, S. (2019) *5,000 Writing Prompts: A Master List of Creative Exercises*. For clients with highly distinctive, idiosyncratic voices — founders who write in a recognisable personal style, brands with a cult following, or professional voices with known stylistic signatures — add an optional STYLISTIC BANS field to the Brand Context Block. This goes beyond vocabulary to structural habits the brand avoids:

```
STYLISTIC BANS:
- Never opens with a statistic
- Never uses a list of three where a paragraph would be stronger
- Never starts a post with a question
- Never closes with a sentence beginning "Remember:"
- Never uses em dashes for dramatic pauses
```

The principle: specify what the voice does NOT do as precisely as what it does. The most distinctive voices are as defined by what they refuse as by what they embrace. Vocabulary bans catch words; stylistic bans catch habits of structure and rhythm that are invisible to the vocabulary scanner but obvious to a careful reader.

Add this field only for clients where voice distinctiveness is material to brand value. For standard SME clients, vocabulary and example-based training is sufficient.

---

## Step 4 — Few-Shot Examples by Content Type

For each content type the client regularly produces, source 1–2 approved examples in their voice. These are stored alongside the Brand Context Block and pasted into the prompt when working on that content type.

**Caption example**
One caption that performed well and that the client considers representative. Include the platform it was written for.

**Email opening example**
The first 3–4 sentences of an email the client considers on-brand. Subject line included if available.

**Story / WhatsApp Status script example**
One short script (3–5 frames or lines) for ephemeral content. If the client does not use Stories or WhatsApp Status, skip this.

**Response to a comment or DM example**
One example of how the brand replies to a positive comment and one for a neutral enquiry. Tone in replies often differs from broadcast content — capture both.

**Blog or long-form opening example** (if applicable)
First paragraph only. Enough to establish rhythm and hook style.

Store all few-shot examples in a single reference document in the client's project folder, labelled clearly by content type.

---

## Step 5 — Quality Test the Block

Before the block is used in live client work, run a quality test.

**Test prompt:** Using only the Brand Context Block (no few-shot example), ask the AI to write one piece of content the client produces regularly — a Facebook caption, an email opening, a WhatsApp message.

**Compare the output against 2–3 pieces of the client's existing approved content. Ask:**

- Does this feel like this brand, or does it feel generic?
- Is the vocabulary matching — are the signature phrases appearing naturally?
- Is the tone right for the platform and for this client's position on the scale?
- Are the banned words absent?
- Would the client recognise this output as theirs without being told the AI wrote it?
- Does local language appear where appropriate, or has the AI defaulted to Standard English only?

**If the output fails any of these checks:**

- Add more verbatim examples to the EXAMPLES OF OUR VOICE field — this is almost always the fix.
- Make the NEVER USE list more specific — add the exact generic phrases that appeared in the failing output.
- Tighten the "We are X, not Y" pairs to address the specific failure mode observed.
- Re-run the test after each refinement. Iterate until the block passes.

Document which version passed the quality test. Label it v1.

### Voice Replication Comparison Test

Source: Mizrahi (2024). When testing the Brand Context Block, run two versions of the same prompt:

**Method 1 — Adjectives and "We are X, not Y" only** (no EXAMPLES OF OUR VOICE field): Generate one piece of content using only the VOICE, TONE, ALWAYS USE, NEVER USE, and AUDIENCE fields.

**Method 2 — Full block including examples**: Generate the same piece using the complete Brand Context Block with the EXAMPLES OF OUR VOICE field populated with three or more verbatim examples.

Compare the two outputs. Document which produces more accurate voice replication. If Method 1 significantly underperforms, the block needs more examples before it is deployed on live client work. This test is the single most reliable diagnostic for a Block that is technically complete but still producing generic output.

---

## Step 6 — Maintain and Update the Block

The Brand Context Block is a living document, not a one-time deliverable.

**Storage:** save the block as a plain text file in the client's project folder. Name it `[ClientName]-brand-context-v1.txt`. Keep all versions.

**Scheduled review:** review the block quarterly, or immediately after any of the following:
- The client rebrands (name, positioning, visual identity, or audience shift)
- The client launches a new product line or service that requires a distinct tone
- Voice drift is detected (see below)

**Detecting voice drift:** if recent AI-assisted content is drifting toward generic — if it sounds more like a marketing textbook than like the client — the block needs updating. Signs of drift include: banned words reappearing, overly formal constructions, loss of local references, CTAs that feel transactional rather than relational.

**Updating the block:**
- Add new signature phrases as they emerge in the client's organic content.
- Add new banned terms as generic AI patterns appear.
- Replace EXAMPLES OF OUR VOICE with more recent content if the brand has evolved.
- Increment the version number (v1 → v2). Keep the previous version on file in case the update makes output worse.

**Do not delete old versions.** Reverting is sometimes necessary.

---

## Quality Criteria

Output from this skill meets the standard when:

- The Brand Context Block is complete — no field is blank or contains a placeholder; every item in the Required Inputs table is represented.
- The EXAMPLES OF OUR VOICE field contains verbatim, unedited client content — not paraphrased or improved versions.
- The standard AI vocabulary ban list is present in full, with client-specific terms added above it.
- A quality test has been run and documented, and the block has been refined until AI output is indistinguishable in voice from the client's approved content.
- Few-shot examples cover every content type the client regularly produces, stored and labelled separately.
- Local language, cultural references, and EA-specific identity markers are preserved explicitly in the block, not left to the AI to infer.
- The block is versioned, stored in the client's project folder, and a review schedule is agreed (quarterly minimum).
- The block is platform-agnostic in its fixed fields, with only the PLATFORM field updated per session.
