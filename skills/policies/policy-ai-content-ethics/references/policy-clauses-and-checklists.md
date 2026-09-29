# AI policy clauses, checklists and East African considerations

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); text unchanged except that relative links drop the `references/` prefix or gain an extra `../` so they resolve from this folder. Read when adding the attribution, IP, watermarking, bias-risk, EU AI Act or additional ethical clauses, running the per-piece consultant checklist, applying East Africa considerations, or checking the full quality criteria and key citations.

## Section 2A — AI Attribution and Disclosure Standard

Source: Ching & Mothi (2025). The disclosure standard used in this policy requires specificity. "Made with AI" is insufficient. The agency standard is:

> "AI-generated [specific element], art-directed and revised by [human team]."

Professional precedent: the band YACHT documented their AI-assisted album in specific liner notes identifying exactly which elements were AI-generated and which were human-executed. This level of attribution is the standard the agency applies and recommends to clients. Where disclosure is provided, it must be specific enough that an informed reader understands what the AI contributed and what the human contributed.

---

## Section 2B — Intellectual Property and Copyright

Source: Ching & Mothi (2025, p.82). Add as a named clause in client policies for any client intending to register or commercially licence their content:

**What the policy must state:**
- AI-generated content without substantial human creative contribution may not qualify for copyright protection under UK, US, or EU law
- This agency ensures that every deliverable involving AI assistance also involves substantial human creative contribution — in the form of strategic direction, editorial revision, cultural adaptation, and brand voice application
- Before registering or licensing any AI-assisted creative work, the client must obtain legal advice from a qualified intellectual property solicitor

Include this clause in the policy when the client is a creative agency, publisher, music producer, or any business that commercialises content through licensing or registration. For general brand content, note in the production record that human contribution is documented per deliverable. Full jurisdictional detail, WGA 2023 benchmark, provenance record and referral triggers: [references/ai-ip-and-copyright-policy.md](ai-ip-and-copyright-policy.md).

---

## Section 2C — SynthID and AI Content Watermarking

For AI-generated audio and visual assets, tag original AI-generated files with persistent metadata or watermarks before any editing or compression.
- **Audio:** SynthID (Google/DeepMind) is the current standard for AI-generated audio — it embeds a watermark that survives compression and editing
- **Images and video:** Equivalent watermarking tools exist for AI-generated images and video content
- **Production record requirement:** Note in the project file which assets were AI-generated at source and confirm that watermarking was applied to the original file before editing or delivery to the client

---

## Section 2D — Training Data Bias Risk Register

Add to the policy's risk register or prohibited uses:
**Named risk: Training Data Bias.** AI-generated content depicting people, communities, or cultural practices must be reviewed for training data bias by a human reviewer with direct cultural knowledge. AI tools default to Western-centric, gender-stereotyped, and racially inaccurate representations because their training data was predominantly Western. This is not a setting that can be adjusted — it is the data the AI learned from.

**For East African clients:** This review is mandatory for all AI-generated imagery descriptions, people representations, and community references before client delivery. A reviewer without direct cultural knowledge of the community being depicted is not qualified to approve this content.

**Examples on record:** BuzzFeed's AI-generated travel images and DeepVogue's AI fashion tool both produced racially and culturally inaccurate depictions without flagging bias. These are the precedents this policy addresses. Run the audit itself with [references/cultural-bias-audit-protocol.md](cultural-bias-audit-protocol.md).

---

## Section 2E — EU AI Act Cross-Border Compliance Note

For international clients, donor organisations, or any client producing content for European audiences, add the following cross-border compliance note:
**EU AI Act obligations relevant to AI-assisted content production** (corrected 29 Sep 2026: the transparency duties are in Article 50 of Regulation (EU) 2024/1689, applying from 2 Aug 2026, per the European Commission Article 50 FAQ, register `EU-AI-ACT-ART50-FAQ`; the draft "Article 4" and "Article 28b(4)" numbering used by the original source is withdrawn):
- **Article 50(4), deepfakes:** AI-generated or manipulated images, audio or video that resemble real people, places or events and would falsely appear authentic must be disclosed clearly at first exposure; machine-readable marking alone is not enough.
- **Article 50(4), public-interest text:** AI-generated text published to inform the public on matters of public interest must be labelled unless it has passed human review or editorial control by a person with authority over publication.
- **Human oversight:** keep the named-reviewer rule as the agency standard (ICC Code 2024 accountability, register `ICC-CODE-2024-TEXT`).
- Apply the risk-based disclosure table in [AI transparency and provenance](ai-transparency-and-provenance.md#3-risk-based-disclosure-decision-table) for everything else.

This note applies when: the client distributes content to EU audiences; the client receives EU donor funding with content compliance requirements; or the client operates a cross-border business with EU-facing channels. For legal certainty in EU-facing contexts, obtain advice from a qualified solicitor familiar with the EU AI Act.

---

## Section 2A — Additional Ethical Requirements

**Algorithmic Bias in Personalisation (Ltifi, 2024):** AI personalisation algorithms can inadvertently reinforce demographic stereotypes — showing certain product types only to certain segments, or systematically excluding groups from offers, creating discriminatory feedback loops. Require an audit of any AI personalisation tool for demographic fairness before deployment. The audit must assess whether the system treats comparable users differently based on gender, ethnicity, or age in ways that cannot be justified by legitimate business logic.

**Non-Discrimination Clause:** AI-generated advertising targeting must not use protected characteristics — gender, ethnicity, religion, or age — as primary targeting variables in ways that constitute discrimination. This applies to both inclusion targeting (showing content only to favoured groups) and exclusion targeting (hiding content from disfavoured groups). Cite GDPR Article 22 and Uganda's Data Protection and Privacy Act 2019 Section 25 when advising clients on compliant targeting practice.

**Explainability Obligation (Johnsen, 2024, Ch.28):** When AI drives a significant strategic recommendation — audience targeting decisions, content strategy pivots, or budget allocation — the agency has an obligation to explain the AI's reasoning in plain terms to the client. AI output presented without explanation is not acceptable professional practice. Document the basis for AI-informed decisions in the strategy or reporting record.

**Continuous Monitoring Obligation (Johnsen, 2024, Ch.28):** Ethical AI deployment is not a one-time review. Require quarterly bias audits and model drift reviews as standard practice for any client using AI personalisation or AI-driven targeting. AI models that performed fairly at deployment can develop bias as the distribution of their training data shifts — a model trained on historical data will reflect historical inequalities unless actively monitored and corrected.

**East African Regulatory Alignment (Johnsen, 2024, Ch.28):** For clients operating across multiple EA countries, note that national data protection frameworks vary in scope and enforcement: Uganda Data Protection and Privacy Act 2019, Kenya Data Protection Act 2019, and Tanzania's Personal Data Protection Act 2022 (in force 1 May 2023; administered by the Personal Data Protection Commission; source-register record `TZ-PDPA`, Kaizen register PL-04 — partial) have different definitions, rights, and penalties. Flag the national regulatory context explicitly before deploying any AI personalisation system for a cross-border client.

**Data Minimisation Principle (Ltifi, 2024, Ch.2):** AI personalisation systems should collect only the minimum data necessary for the task. Require clients to document their data minimisation rationale before implementing any AI personalisation or audience profiling system. Data minimisation is a legal requirement under the Uganda Data Protection and Privacy Act 2019 and Kenya Data Protection Act 2019, and a baseline ethical standard for responsible AI deployment.

---

## Section 3 — Consultant's Internal AI Ethics Checklist

Apply this checklist before publishing any AI-assisted content for a client.
Run it per piece of content, not per campaign.
- [ ] Every factual claim verified by a human against a primary or authoritative
      source
- [ ] No customer data, PII, or confidential client information entered into
      any AI prompt
- [ ] No confidential business information, trade secrets, or proprietary
      documents entered into any cloud-based AI tool
- [ ] Brand voice edit applied — the content sounds like the client, not like
      generic AI output
- [ ] No prohibited use engaged (fake review, deepfake, bot engagement,
      fabricated beneficiary story)
- [ ] Client has approved the content, or this content type is pre-approved
      per the signed content calendar
- [ ] If the client is in a regulated sector (health, finance, legal,
      political) — a qualified professional has reviewed the output
- [ ] Disclosure applied if the content is substantially AI-generated with
      minimal human editing
- [ ] If publishing under a personal name or attributed quote — confirm the
      named individual has reviewed and approved the text; apply Proof of Human
      signal for thought leadership and donor narrative content
- [ ] No attempt has been made to circumvent AI safety guidelines
      ('jailbreaking'); report any such attempt to [Name/Title] immediately
      (Venkatesan and Lecinski, 2026)

---

## Section 4 — Sector-Specific Guidance

Apply the relevant subsection (health, finance, NGO and donor-funded, political and public sector) from [references/sector-specific-ai-guidance.md](sector-specific-ai-guidance.md); include every subsection that applies when regulated sectors overlap.

---

## Section 5 — East Africa-Specific Considerations

Apply the following contextual guidance for all Uganda and East Africa clients.
**Uganda Data Protection and Privacy Act 2019 (UDPPA)**
Do not enter personal customer data into AI prompts. Names, phone numbers,
National ID numbers, locations, transaction data, and health records all
qualify as personal data under the UDPPA. Breach of this requirement exposes
the agency and the client to regulatory sanction from the Personal Data
Protection Office (PDPO). Store AI conversation logs securely and purge
sensitive sessions promptly.
**Audience trust**
East African professional and institutional audiences — government partners,
B2B buyers, international donors, and formal sector consumers — are acutely
sensitive to perceived inauthenticity. Over-reliance on generic AI output
risks damaging brand credibility in markets where relationships and personal
trust underpin commercial decisions. Apply a rigorous brand voice edit to
every piece of AI-assisted content before publication.
**Language and vernacular content**
AI tools produce more reliable output in English than in Luganda, Swahili,
Runyankore, Acholi, or other regional languages. Human-written vernacular
content is strongly preferred for community-facing and rural-audience
communications. Where AI is used to draft vernacular text, require a fluent
native-speaker review before publication — machine translation into East
African languages introduces both linguistic errors and cultural missteps that
damage trust.
**Local context accuracy**
AI tools are trained predominantly on Western and global datasets. They
frequently produce incorrect Uganda-specific facts: wrong prices, outdated
regulations, inaccurate geography, and unfamiliar local institutions. Always
verify EA-specific claims — market prices, regulatory body names, government
programme titles, local statistics — against current Ugandan or East African
primary sources before publication.

---

## Quality Criteria

Output meets the standard for this skill when:
- The policy template is complete and contains no unfilled placeholders; all
  bracketed fields are populated with client-specific information gathered
  during the Required Inputs stage.
- The five ethical principles (transparency, fairness, nonmaleficence,
  accountability, privacy) are presented as a table and cited to Ltifi (2025)
  and Johnsen (2024).
- The prohibited uses list explicitly names fake testimonials, deepfakes,
  bot engagement, fabricated beneficiary stories, filter bubble risk, and
  copyright/ownership uncertainty.
- The Proof of Human signal and virtual influencer disclosure requirement are
  present in the Disclosure clause.
- The data and privacy clause prohibits both PII entry and confidential
  business information entry into cloud AI tools, and references the Samsung
  incident (Venkatesan and Lecinski, 2026).
- The human review requirement is stated explicitly in both the policy
  document and the consultant's checklist — AI output is never published
  without human approval.
- Sector-specific guidance covers at least health and finance with specific,
  actionable instructions; all sectors relevant to the client are included.
- The Uganda Data Protection and Privacy Act 2019 is named explicitly and the
  prohibition on entering PII into AI prompts is unambiguous.
- The consultant's internal checklist is actionable as a per-piece pre-
  publication review, not a one-time setup exercise, and includes data leakage
  and jailbreak awareness items.
- The entire document is written in British English with no American spellings
  (organisation, colour, behaviour, programme, recognise, analyse, etc.).

---

## Related skills and key citations

Consult the following skills where relevant:
- `playbook-content-production` ([AI-assisted production workflow](../../../playbooks/playbook-content-production/references/ai-assisted-production-workflow.md)) — the operational workflow for
  producing AI-assisted content; read this when setting up or auditing the
  client's production process.
- `playbook-social-media-policy/SKILL.md` — the broader social media policy
  framework; the AI Content Ethics Policy sits within or alongside this
  document.
- `04-brand-voice-intake/SKILL.md` — captures the brand voice, tone, and
  communication standards that AI tools must be briefed against before
  drafting client content.
**Key citations used in this skill:**
- Ching, V. and Mothi, D. (2025) — AI attribution/disclosure standard; IP and copyright guidance; SynthID watermarking; training data bias risk; EU AI Act (source cited draft Articles 4 and 28b(4); corrected to Article 50, see [AI transparency and provenance](ai-transparency-and-provenance.md)).
- Johnsen, R. (2024) *AI Ethics in Practice*
- Ltifi, M. (2025) *Artificial Intelligence and Social Media Marketing* (verify: not found in publisher or library catalogues, 29 Sep 2026)
- Schaefer, M. (2025) *Belonging to the Brand*
- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*
