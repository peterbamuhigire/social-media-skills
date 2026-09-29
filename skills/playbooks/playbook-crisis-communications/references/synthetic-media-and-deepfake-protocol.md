# Synthetic media and deepfake protocol

Read when a fake video, cloned voice note, AI-generated image or impersonating account about the client, its leaders or its products is circulating, or when the client's own AI-made content is accused of being fake.

Added 29 Sep 2026 (Social Kaizen S10-T09, benchmark row SL20-C4). This is a crisis-response procedure, not legal advice. It sits inside the severity levels of the main plan; a deepfake that names a person, alleges a crime or touches an election is Level 3 from the start.

## 1. Detect

- Add the brand name, leaders' names and product names to social listening, including WhatsApp status and group screenshots forwarded by staff and customers (WhatsApp content is invisible to listening tools).
- Brief front-line staff and community managers: any voice note, video or screenshot "from the CEO" asking for money, announcing a promotion or making a statement is escalated, not answered.
- Open an incident log entry at first sight: where seen, time, link or file, who reported it. Save the original file, not a screenshot of it, where possible.

## 2. Verify provenance before saying anything

| Check | How | Result recorded |
|---|---|---|
| Did we publish it? | Search the client's content calendar, provenance log and platform publishing history | Ours / not ours / unknown |
| Content Credentials | Inspect the file for C2PA credentials with a public verification tool; read the IPTC digital source type if present (register `C2PA-SPECIFICATION`, `IPTC-DIGITAL-SOURCE-TYPE`) | Credentials present, absent or stripped. Absence proves nothing: forwarding and screenshots strip metadata |
| The person shown | Ask the named person directly where they were and what they said | Confirmed genuine / confirmed fake / cannot confirm |
| Platform label | Note any "AI info" or AI-generated label the platform shows (registers `META-AI-INFO-LABELS`, `TIKTOK-AIGC-LABELS`) | Label present or absent |
| Detection tools | Use a detector only as a weak signal; record the tool and its output | Never the sole basis for a public "this is fake" statement |

If the item is genuine, it is not a deepfake case: return to the main severity levels.

## 3. Respond

1. **Holding statement within the level's timeline.** State what the organisation knows, that the item is being checked, and where official information is published. Do not repeat the false claim in the headline, and do not share the fake file.
2. **Once verified as fake.** Publish a short correction on every owned channel the audience uses (for Uganda and Kenya this usually includes WhatsApp broadcast lists, Facebook and radio), naming the official channels and, where useful, one or two tell-tale signs. The CIPR guide recommends pre-bunking and early-warning monitoring as the standing defence against disinformation (register `CIPR-CRISIS-SOCIAL-2024`).
3. **Scam variant** (fake promotion, fake payment request, fake job offer). Tell customers the only official payment numbers and that the organisation never asks for mobile money PINs; inform the mobile-money provider's fraud desk.
4. **If the client's own AI content is challenged.** Show the provenance log and the disclosure decision; if the label was missing, add it, say so plainly and correct the process (see [AI transparency and provenance](../../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md)).

## 4. Platform reporting

- Report the item through each platform's in-app reporting for impersonation, manipulated media or scams, and through the intellectual-property or privacy forms where the client's trademarks or a person's likeness are used. The exact form names and routes are `NOT_ASSESSED` in this wave: check each platform's help centre at the time.
- TikTok's Community Guidelines do not allow AI-generated content that misleads on matters of public importance or harms individuals, even when labelled (register `TIKTOK-AIGC-LABELS`); cite the relevant rule in the report.
- Record each report: platform, time, reference number, outcome. Re-report if the item re-appears under a new account.

## 5. Legal escalation (screening only)

Escalate to the client's counsel, without delay, when any of these apply:

- the fake shows an identifiable person saying or doing something they did not (defamation, personality and personal-data questions; Uganda Data Protection and Privacy Act 2019, register `UG-DPPA-2019`);
- it alleges a crime, involves a minor, is sexual, or runs during an election period;
- it is used to take money from the public (fraud; the police cybercrime unit may need a report);
- the client wants a takedown demand, a police complaint or a court order.

Uganda: the Computer Misuse (Amendment) Act 2022 was declared void on 17 Mar 2026; do not cite it (register `UG-CMA-2022-VOID-2026`). Which provisions of the 2011 Act and other laws apply is a question for counsel. Kenya, Tanzania and Rwanda: refer to local counsel; the applicable offences are `NOT_ASSESSED` here.

## 6. Recover

Add to the post-crisis review: how the fake was first seen, time to verification, time to correction, reach of the fake versus the correction, which platform acted and how fast, and what monitoring or pre-bunking would have caught it earlier. Update the listening terms and the holding statement bank.

## Sources

- `CIPR-CRISIS-SOCIAL-2024` — CIPR Crisis Communications Network, *Crisis Communication and Social Media*, 2024.
- `C2PA-SPECIFICATION`, `IPTC-DIGITAL-SOURCE-TYPE`, `META-AI-INFO-LABELS`, `TIKTOK-AIGC-LABELS` — provenance and platform label records (S10 proposals).
- `UG-DPPA-2019`, `UG-CMA-2022-VOID-2026` — existing register records.
