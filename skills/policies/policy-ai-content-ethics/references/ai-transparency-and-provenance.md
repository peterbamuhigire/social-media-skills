# AI Transparency and Provenance

Read when deciding whether a piece of AI-assisted marketing content needs a consumer-facing AI label, how to label it, what provenance metadata to keep, which platform and legal rules apply, and how the client's AI policy lines up with ISO/IEC 42001 and NIST AI 600-1.

Added in Social Kaizen S10-T09 (29 Sep 2026). Every current claim below was read live on 29 Sep 2026 unless it is marked `NOT_ASSESSED` or "as reported by IAB". This is a screening and escalation reference, not legal advice: where a law may apply, the client's counsel decides.

## 1. Which rule wins

Four layers can apply to the same asset. Check them in this order and apply the strictest.

| Layer | Examples | Status in this engine |
|---|---|---|
| Binding law where the audience is | EU AI Act Article 50 for EU-facing work; other national AI-labelling laws | Screen and escalate to counsel; never decide alone |
| Platform rules | Meta "AI info"; TikTok AI-generated content labels; political and social-issue ad rules | Mandatory for the account to stay in good standing; verify per platform on the campaign date |
| Industry self-regulation | IAB AI Transparency and Disclosure Framework v2; ICC Code 2024 | Default professional standard for this engine |
| Client policy | The client's AI Content Policy built with this skill | May be stricter than the three layers above, never looser |

The IAB framework itself says advertisers should yield to regulation wherever binding requirements are stricter, and that a disclosure never cures a deceptive claim (register `IAB-AI-DISCLOSURE-V2-2026`).

## 2. Accountability: who answers for AI output

- The ICC Advertising and Marketing Communications Code (2024) states in its responsibility section that marketers who use algorithms or other AI instruments are responsible for the communication results they produce. Its Article 5 (truthfulness) treats content altered or enhanced by AI as misleading when it misleads about a product or about a person's association with it (register `PREMIUM-ICC-2026`).
- IAB v2 places ultimate disclosure responsibility on the advertiser and says it cannot be delegated. Where an agency creates and controls content for a client, agency and client may share that responsibility. Platforms act only as secondary enforcers (register `IAB-AI-DISCLOSURE-V2-2026`).
- Engine rule: every AI-assisted asset has a named human reviewer who records the disclosure decision before publication. "The tool did it" is never an answer to a client, a platform or a regulator.

## 3. Risk-based disclosure decision table

The test, following IAB v1 (15 Jan 2026) and v2 (18 Aug 2026): does the AI involvement create a material risk that a reasonable consumer is misled about authenticity, identity or representation? The trigger is consumer impact, not how many AI tools touched the asset (registers `IAB-AI-DISCLOSURE-2026`, `IAB-AI-DISCLOSURE-V2-2026`).

| Situation | IAB v2 position | Engine default | Extra checks |
|---|---|---|---|
| Photorealistic image or video generated from a prompt (text-to-image, image-to-video), even if later edited | Disclose | Label "AI-generated" | EU-facing: Article 50 deepfake duty if it resembles real people, places or events |
| Routine retouching, colour correction, background clean-up, upscaling, noise removal | No disclosure | No label; keep the provenance log | Label if the edit changes how the product looks or performs |
| Real product photographed, AI-generated background that does not change the product | No disclosure | No label | Health, food and cosmetics claims: check the sector rules first |
| Obviously stylised, animated or fantastical imagery | No disclosure | No label | None |
| Photorealistic synthetic human in a primary role, synthetic avatar or virtual influencer | Disclose on first frame and throughout | Label in every appearance and every post | Influencer disclosure rules also apply (see `08-influencer-marketing-strategy`) |
| Voice or likeness of a deceased person | Disclose, even with estate consent | Label; hold estate consent in writing | Refer to counsel before production |
| Living person's authorised digital twin or voice clone in a scripted endorsement | No disclosure (IAB treats paid endorsement framing as removing the risk) | **Label anyway** for EU-facing work, and wherever the audience may not read it as a paid ad | IAB v2 notes EU Article 50(4), South Korea, Vietnam and India do not share this exemption |
| Living person shown in events that never happened (voice or likeness) | Disclose, even with consent | Label; get consent for the specific scenario | Refer to counsel; high defamation and electoral risk |
| Conversational agent or chatbot in an ad that simulates a human | Disclose ("AI-powered") throughout | Label; the bot must say it is automated when asked | EU Article 50(1) places a separate duty on providers |
| Ad copy, headlines, captions and emails drafted with AI | Generally no disclosure | No label; a human checks every claim | EU-facing text on matters of public interest without human editorial control: Article 50(4) label |
| AI translation or light localisation of human-made content | Usually below the threshold | No label | Native-speaker review for Luganda, Swahili and other languages |
| Dynamic creative or serve-time AI personalisation | Disclose where any component triggers; set rules at system level | Record the rule set per campaign | Keep the component log for audit |
| Crowds and background figures that are not the focus | No disclosure | No label | Label if a figure could be read as a real, identifiable person |
| Social-issue, electoral or political ad with realistic altered or synthetic people, events or audio | Meta requires an AI disclosure whatever tool made it | Label and complete the platform declaration | Meta authorisation and "Paid for by" rules (register `META-SIEP-AD-LIBRARY-2026`); election periods in Uganda and Kenya go to counsel |

Prohibited whatever the label: fabricated testimonials, false claims, and any use of a real person's likeness or voice without authorisation (IAB v2; ICC Article 5).

## 4. How to label

- **Text label or icon.** IAB v2 accepts either a text label ("AI-generated"; "AI-generated voice" for audio; "AI-powered" for chat) or the Unicode sparkle (U+2728) as the indicator. Text is the clearer option for comprehension (register `IAB-AI-DISCLOSURE-V2-2026`).
- **Placement.** Image: near the image. Video, avatar or digital twin: on the first frame and visible throughout. Audio (radio, podcast): spoken at normal pace before or straight after the AI segment, repeated at least once if the ad runs over 60 seconds.
- **Language.** In the language of the primary audience. Whether a Luganda, Swahili or Sheng rendering of "AI-generated" is understood is `NOT_ASSESSED`; test the wording with five to ten target users before a large campaign, and fall back to English plus the sparkle if unclear.
- **Accessibility.** Alt text for visual labels, captions that include the disclosure, and a visual equivalent when an audio disclosure sits in a video.
- **Every appearance.** A synthetic persona or recurring avatar is labelled in every post and on every platform, not once in a bio.
- **Platform labels.** A platform-applied label can satisfy the disclosure if it is visible enough. IAB v2 cautions that platforms mostly render labels for content made with their own AI tools, not for third-party creative uploaded with metadata. Unless a platform is confirmed to render the label for this asset, put the label in the creative itself.

## 5. Provenance: the machine layer

- **C2PA Content Credentials.** An open technical standard that binds a signed, tamper-evident manifest (a claim plus assertions about how the asset was made and edited) to the file. Current published version: 2.4, April 2026 (register `C2PA-SPECIFICATION`).
- **IAB assertions.** IAB v2 recommends recording the disclosure decision in C2PA before distribution, using two custom assertions it is defining: `com.iab.threshold` (met or not met) and `com.iab.disclosure` (label applied: yes or no), plus the AI-involvement type and tool. The classification is a human judgement even when other fields are captured automatically.
- **IPTC digital source type.** The IPTC controlled vocabulary distinguishes, among others, `trainedAlgorithmicMedia` (created by a generative model), `compositeWithTrainedAlgorithmicMedia` (generative inpainting or outpainting), `algorithmicallyEnhanced` (non-generative correction such as sharpening) and `digitalCapture` (register `IPTC-DIGITAL-SOURCE-TYPE`). Meta reads both C2PA and IPTC signals when it applies labels (register `META-AI-INFO-LABELS`).
- **Watermarks.** IAB v2 treats invisible watermarks (for example Google's SynthID) as a complement to C2PA, because metadata is lost when files are re-saved, compressed or screenshotted.
- **East Africa reality.** Much distribution runs through WhatsApp forwards, screenshots and re-uploads, so assume the metadata will not survive. The visible label and the agency's own provenance log are the controls that last; C2PA is the audit trail, not the consumer notice.
- **Provenance log per asset.** Tool and version, prompt or brief, human reviewer, substantive changes, disclosure decision (threshold met or not, label applied or not, reason), date signed off, and whether C2PA credentials and a watermark were attached. Keep for three years (the retention period in [AI IP and copyright policy](ai-ip-and-copyright-policy.md#agency-provenance-protocol--production-record-template)).

## 6. Platform rules (verify on the campaign date)

| Platform | What was read on 29 Sep 2026 | Status |
|---|---|---|
| Meta (Facebook, Instagram, Threads) | The "AI info" label replaced "Made with AI" on 1 Jul 2024. Labels are applied from industry-standard signals (C2PA, IPTC), from self-disclosure and from Meta's own detection. Since 12 Sep 2024 content only edited with AI shows the label in the post menu. Meta may add a more prominent label where content carries a particularly high risk of materially deceiving the public. | Organic policy read on Meta's newsroom (register `META-AI-INFO-LABELS`, partial). Ad-specific rules (auto-label for ads made with Meta's generative tools; label beside "Sponsored" for photorealistic humans) are as reported by IAB v2; Meta's ads help page `NOT_ASSESSED` |
| TikTok | Community Guidelines (2026 H2 update) require creators to label AI-generated or significantly edited content showing realistic-looking scenes or people. Unlabelled content may be removed, restricted or labelled by TikTok. Misleading AI content on matters of public importance is not allowed even with a label. | Organic verified (register `TIKTOK-AIGC-LABELS`). Ads policy (AIGC label or clear disclaimer; auto-label for Symphony Creative Studio output; consent for a real person's likeness; rejection if undisclosed) is as reported by IAB v2; TikTok's ads policy page was unreachable, `NOT_ASSESSED` |
| Google and YouTube | IAB v2 reports SynthID watermarking, C2PA credentials in several generative tools, election-ad synthetic content disclosure since 2023, and a 2026 "How this ad was made" panel. | As reported by IAB v2; Google primary pages `NOT_ASSESSED` in this wave |
| Meta political and social-issue ads | Disclosure of realistic altered or synthetic people or events is required whatever tool was used. | Register `META-SIEP-AD-LIBRARY-2026` (partial) |

## 7. EU AI Act Article 50 (EU-facing work only)

Applies when the client distributes to EU audiences, runs EU-facing channels or has EU donor content rules. Source: the European Commission's Article 50 FAQ, updated 24 Jul 2026 (register `EU-AI-ACT-ART50-FAQ`). The Regulation's text on EUR-Lex could not be read (automated access blocked): `NOT_ASSESSED`.

- **From 2 Aug 2026**, with a limited grace period for the machine-readable marking duty to 2 Dec 2026 for systems already placed on the market before 2 Aug 2026 (scope and origin in the AI Omnibus as reported by IAB v2; primary text `NOT_ASSESSED`).
- **Providers** of AI systems: tell people when they are interacting with an AI system unless that is obvious (50(1)); mark synthetic audio, image, video and text in a machine-readable, detectable form (50(2)).
- **Deployers** (this is where a brand or agency using AI tools sits): disclose deepfakes clearly and distinguishably at first exposure; machine-readable marking alone is not enough. Label AI-generated or manipulated text published to inform the public on matters of public interest, unless it has had human review or editorial control by someone with the authority to approve it (spelling and grammar checks do not count) (50(4)).
- **Creative and satirical work:** an evidently artistic, satirical or fictional deepfake needs only an appropriate disclosure that does not spoil the work.
- **Code of Practice and Guidelines:** a voluntary Code of Practice on Transparency of AI-Generated Content and Commission Guidelines support compliance. IAB v2 reports the Code as finalised in June 2026 with official EU icons, the Guidelines adopted on 20 Jul 2026, and fines of up to EUR 15 million or 3% of worldwide turnover; these details are as reported by IAB, primary text `NOT_ASSESSED`.
- **Correction to older text in this skill.** Earlier references cited "Article 4 (labelling)" and "Article 28b(4) (human oversight)" from a draft numbering. The transparency duties are in Article 50. Do not cite the draft numbers to a client.

## 8. Other jurisdictions (as reported by IAB v2, 18 Aug 2026)

Not verified against primary law in this wave; use only as a prompt to ask counsel: New York's synthetic-performer disclosure law (effective 9 Jun 2026); the California AI Transparency Act (effective 2 Aug 2026, duties on large generative-AI providers rather than advertisers); China's labelling measures (1 Sep 2025); South Korea's AI Basic Act (22 Jan 2026); India's 2026 amendment to the IT Rules and draft ASCI guidance; Vietnam's AI law; Thailand's consumer-protection notification; and Taiwan's fraud-prevention rule for platforms.

**Uganda, Kenya, Tanzania and Rwanda.** No AI-specific advertising labelling law was verified for any of the four: `NOT_ASSESSED`. General rules still bite: truthfulness and substantiation under the ICC Code (register `PREMIUM-ICC-2026`) and Kenya's advertising code (register `KE-ASBK-CODE-2003`), personal-data rules when a real person's image or voice is processed (register `UG-DPPA-2019` and the Kenya and Tanzania records), and election-period rules. Apply the Section 3 table as the floor and label every realistic depiction of a real person or event.

## 9. Management-system alignment

**ISO/IEC 42001:2023 (AI management system).** The standard sets requirements to establish, implement, maintain and continually improve an AI management system, and organisations can be certified against it. The ISO page could not be read (blocked); this summary is from an accredited certification body (register `ISO-IEC-42001-2023`, partial). Clause-level mapping is `NOT_ASSESSED` because the standard text was not read. Map the client's artefacts to the management-system cycle instead:

| Management-system element | Artefact from this skill |
|---|---|
| AI policy and scope | Client AI Content Policy (purpose, tools, prohibited uses) |
| Roles and accountability | Named reviewer per asset; AI Disclosure Lead (IAB v2 recommends naming one within 60 days) |
| Risk and impact assessment | Section 3 disclosure table; cultural bias audit; sector subsections |
| Operational control | Per-piece checklist; provenance log; C2PA and label decision before publication |
| Supplier control | AI tool register with data-handling terms (see agency AI contract clauses in `biz-dev-proposal`) |
| Monitoring and improvement | Quarterly policy review; incident log from `playbook-crisis-communications` |

A client that wants certification needs an accredited certification body and its own counsel; this engine drafts the marketing-side artefacts only.

**NIST AI 600-1 (Generative AI Profile, July 2024).** A voluntary companion to the NIST AI RMF 1.0 (Govern, Map, Measure, Manage). It names 12 risks that generative AI creates or worsens and focuses its actions on governance, content provenance, pre-deployment testing and incident disclosure. NIST states the AI RMF 1.0 is being revised (register `NIST-AI-600-1`). The risks most relevant to marketing, with the control in this skill:

| NIST AI 600-1 risk | Marketing form | Control |
|---|---|---|
| Confabulation | Invented statistics, prices, quotes or product facts | Human verification of every claim |
| Information integrity | Deepfakes, fabricated events, political content | Section 3 table; crisis deepfake protocol |
| Harmful bias or homogenisation | Western-default images of East Africans; stereotyped personas | Cultural bias audit |
| Data privacy | Customer data pasted into public AI tools | No PII in prompts; UG DPPA 2019 |
| Intellectual property | Output that copies protected work or a real person's likeness | AI IP and copyright policy; consent records |
| Obscene, degrading or abusive content | Unsafe image or voice generations | Reviewer rejection; platform policy checks |
| Human-AI configuration | Over-trust in AI output; automation bias | Named human reviewer; no auto-publishing |
| Value chain and component integration | Unknown third-party models inside tools | AI tool register; contract clauses |

## 10. Minimum viable implementation

For a small Ugandan or Kenyan client, do these five things now, even before a full policy exists (adapted from the IAB v2 minimum practices):

1. Name one AI Disclosure Lead.
2. Add the Section 3 question to the pre-publication checklist: does the AI use risk misleading someone about what is real?
3. Label every triggering asset in the creative itself.
4. Keep the provenance log; attach C2PA credentials where the tool supports them.
5. Put AI disclosure into the existing legal or approval review rather than creating a new approval layer.

## Sources

- `IAB-AI-DISCLOSURE-2026` — IAB, AI Transparency and Disclosure Framework, 15 Jan 2026 (landing page; full PDF behind login).
- `IAB-AI-DISCLOSURE-V2-2026` — IAB, AI Transparency and Disclosure Framework V2, 18 Aug 2026 (42-page PDF read in full for the sections used).
- `EU-AI-ACT-ART50-FAQ` — European Commission, transparency obligations under Article 50 AI Act, FAQ.
- `META-AI-INFO-LABELS` — Meta newsroom, approach to labelling AI-generated content and manipulated media.
- `TIKTOK-AIGC-LABELS` — TikTok Community Guidelines, integrity and authenticity (2026 H2).
- `C2PA-SPECIFICATION` — C2PA technical specification 2.4.
- `IPTC-DIGITAL-SOURCE-TYPE` — IPTC NewsCodes digital source type vocabulary.
- `ISO-IEC-42001-2023` — ISO/IEC 42001:2023 (partial).
- `NIST-AI-600-1` — NIST AI 600-1 Generative AI Profile.
- `PREMIUM-ICC-2026`, `META-SIEP-AD-LIBRARY-2026`, `KE-ASBK-CODE-2003`, `UG-DPPA-2019` — existing register records.
