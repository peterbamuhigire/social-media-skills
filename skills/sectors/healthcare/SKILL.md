---
name: healthcare
description: Use when the main deliverable concerns healthcare trust, patient-safe content, misinformation response, and East African health-sector communication; use policy-ai-content-ethics when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Healthcare Sector Social Media

<!-- dual-compat-start -->
## Use When

- Use this skill for healthcare trust, patient-safe content, misinformation response, and East African health-sector communication.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `policy-ai-content-ethics` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to healthcare trust, patient-safe content, misinformation response, and East African health-sector communication | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `policy-ai-content-ethics`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Healthcare trust, patient-safe content, misinformation response, and east african health-sector communication deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
| Decision and risk record | Reviewer or implementer | Links each recommendation to supplied evidence or labels it as an assumption |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed |
| Release check | Completed quality checklist | All blocking findings are fixed or the deliverable is explicitly withheld |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Analysis and planning remain read-only. Edit only files placed in scope; publishing, outreach, spend, personal-data processing, production changes, and certification claims require explicit authority and evidence of success.

## Degraded Mode

If files, tools, network, current evidence, rendering, or authorised access are unavailable, return the narrowest useful qualified deliverable. Mark each unavailable check `not assessed`; never convert it into a pass or invent market facts.

## Decision Rules

| Choice condition | Action | Failure or risk avoided |
|---|---|---|
| Clinical or reputational risk is present | Require qualified clinical, legal, or data-protection review before release | Unsafe health claims or unlawful patient-data use |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source | Confident advice built on an unresolved premise |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist | Unauthorised publication, spend, outreach, or data use |

## Quality Standards

- Keep Uganda/East Africa, British English, EAT, UGX, and WhatsApp-first assumptions explicit where they apply.
- Tie recommendations to observed evidence, a named assumption, or a verification action.
- Give the next operator enough detail to execute without guessing ownership, sequence, or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Inventing a client metric, audience fact, price, partner, or platform rule. Fix: verify it or label the decision provisional.
- Treating a missing tool, source, render, or approval as a passed check. Fix: mark it `not assessed` and narrow the output.
- Producing channel tactics before defining the decision and consumer. Fix: state the required outcome and handoff first.
- Copying a global template without adapting Uganda/East Africa access, language, payment, or trust conditions. Fix: record which local assumptions apply.
- Recommending publication, outreach, spend, data collection, or a regulated claim without authority. Fix: stop at an approval-ready draft.
- Reporting activity as success without an acceptance condition. Fix: name the observable result and evidence source.

## References

- [AGENTS.md](../../../AGENTS.md)
<!-- dual-compat-end -->

## Required Input

Ask the client for the following before generating any deliverable:

1. **Client type** — healthcare organisation (hospital, clinic, NGO, pharmaceutical, public health department) or individual medical professional?
2. **Organisation/professional name and specialty** — e.g., "Mulago National Referral Hospital, maternal health" or "Dr Nakato, paediatric allergist"
3. **Country/city** — default Uganda if not specified
4. **Primary goal** — patient education, reputation building, public health advocacy, crisis response, staff communications, professional brand, or clinical knowledge-sharing?
5. **Current social media presence** — which platforms are active, and approximate follower counts
6. **Target audiences** — patients, carers, medical peers, donors, general public, policymakers, or a combination?
7. **Key compliance concern** — patient privacy, professional conduct, organisational policy, or none yet identified?
8. **Existing social media policy** — does one exist? If yes, what are its key provisions?

---

## Section 1 — Why Healthcare Social Media Demands a Different Approach

The stakes of healthcare communication are uniquely high: misinformation about medications, vaccines, and treatments can cause direct patient harm. In East Africa, smartphone penetration is growing rapidly, and 80% of internet users search online for health information (Stukus et al., 2019). Most will encounter social media before they reach a clinic.

Three structural forces make healthcare social media different from every other sector:

**The Illusory Truth Effect** — Repeated exposure to false information increases perceived credibility regardless of accuracy (Stukus et al., 2019). Vaccine misinformation shared frequently will be believed even after clinical correction. Proactive, credible, regular content is the only effective counter-measure.

**The Health Literacy Gap** — Only 12% of US adults are health-literate; the figure is substantially lower across EA. Communication that assumes medical knowledge will fail. Every post must pass a plain-language test: "Can a standard Form 4 student understand this?"

**The Absent Voice Problem** — Patients are already building health communities online whether healthcare professionals participate or not (Stukus et al., 2019; Rogers, 2011). Absence does not mean privacy — it means the professional's voice is replaced by unverified sources.

Apply Parsons' (2009) **4-Level Complexity Model** before planning:
- **Level 1** — Simple information dissemination (clinic hours, seasonal health tips)
- **Level 2** — Policy or procedural change requiring patient explanation
- **Level 3** — Complex issue involving multiple audiences with conflicting interests
- **Level 4** — Crisis or institutional threat to reputation

Strategy depth and resource allocation increase with complexity level.

---

## Section 2 — Stakeholder Architecture

Healthcare organisations face more distinct audience groups than most sectors. Apply Parsons' (2009) 11-stakeholder taxonomy before building any strategy:

| Stakeholder | Primary Concern | Primary Channel | Tone |
|---|---|---|---|
| Patients | Accurate information, reassurance | WhatsApp, Facebook | Plain language, warm |
| Patient families/carers | Practical guidance, updates | WhatsApp, Facebook | Empathetic, direct |
| General community | Public health awareness, trust | Facebook, YouTube, TikTok | Educational, accessible |
| Clinical staff | Policy updates, professional development | WhatsApp groups | Professional, collegial |
| Non-clinical employees | Conduct expectations, organisational news | WhatsApp groups | Informational |
| Board/governing body | Performance, reputation, risk | Confidential briefings | TTR standard |
| Media | Expert comment, news, public statements | X/Twitter, direct contact | Evidence-based, measured |
| Government/regulators | Compliance, public health partnership | Formal channels, LinkedIn | Formal, documented |
| Donors/funders | Impact, accountability | Facebook, email, LinkedIn | Narrative, quantified |
| Medical peers | Knowledge-sharing, referrals | LinkedIn, X/Twitter | Peer-level, evidence-cited |
| Suppliers/partners | Operational coordination | WhatsApp, email | Functional |

**TTR Standard for Senior Stakeholder Communication** (Parsons, 2009): Board and regulatory communications must be **Timely** (before information reaches media), **Transparent** (complete, not selective), and **Relevant** (tied to organisational objectives). Apply this standard to all public health emergency communications.

---

## Section 3 — Patient Network Strategy

Apply Rogers' (2011) five customer network strategies — **Access, Engage, Customise, Connect, Collaborate** — adapted for the healthcare context:

**ACCESS — Make Health Information Findable**
- Ensure facility information (location, hours, services, WhatsApp contact) appears correctly on Google Business Profile, Facebook Page, and WhatsApp Business profile
- Provide a dedicated WhatsApp Business number for patient enquiries — dominant messaging channel across EA
- Answer the top 10 patient questions for the specialty publicly, on the platform where patients search

**ENGAGE — Build Trust through Education**
- Think like a public health educator, not an advertiser: content must inform, not sell
- Use digital storytelling: map clinical information to reporter questions (Who? What? When? Why? How?) to explain conditions, treatments, and prevention in narrative form (Stukus et al., 2019)
- Apply the **5-second rule**: a post must communicate its value to a new reader within 5 seconds
- Healthcare video content receives 1,200% more shares than text and image combined (Stukus et al., 2019) — prioritise short explainer videos (60–90 seconds) on WhatsApp Status and YouTube

**CUSTOMISE — Serve Different Patient Needs**
- Segment content by condition, demographic, and language (English + Luganda or Swahili for broad public health content)
- Provide different formats for different literacy levels: infographic for low-literacy audiences; long-form article for caregivers and peers
- On WhatsApp, use separate broadcast lists for: general health tips (broad public), chronic condition education, appointment reminders

**CONNECT — Build the Patient Community**
- Monitor brand mentions using Google Alerts (free, adequate for most EA healthcare clients)
- Respond to every patient query within 24 hours — "customer service is the new public relations" (Rogers, 2011)
- Apply the **90-9-1 Rule**: for every 100 people who see content, approximately 1 will create content, 9 will comment, and 90 will read silently — design primarily for the 90

**COLLABORATE — Involve the Community in Health**
- Invite patients with similar conditions to share experiences in a moderated Facebook Group or WhatsApp Group — this reduces isolation and generates authentic health narratives (cf. PatientsLikeMe model; Rogers, 2011)
- For NGOs and public health departments: use a dedicated WhatsApp number for community health workers to flag emerging issues and share local data
- For medical professionals: contribute to public health knowledge by sharing conference insights, clinical observations (de-identified), and evidence summaries on X/Twitter and LinkedIn

---

## Section 4 — Platform Strategy for EA Healthcare

**WhatsApp — Priority 1 for all EA healthcare clients**
- Set up a WhatsApp Business account with professional profile, automated greeting, and away message
- Use Broadcast Lists (not groups) for one-to-many health education — patients receive messages directly without group privacy exposure
- Never provide specific diagnosis or treatment via WhatsApp; always direct to appointment: "For personalised advice, please book a consultation at [number/location]"
- During public health emergencies, WhatsApp is the fastest and most trusted channel for official updates

**Facebook — Priority 1 for organisations**
- Maintain a Facebook Page posting at minimum 3 times per week
- Set up community guidelines on the Page covering: comment deletion policy (hate speech, profanity, patient privacy violations), moderation frequency, and disclaimer that nothing posted constitutes medical advice
- Respond to all comments and messages within 24 hours

**YouTube — Priority 2**
- Short health explainer videos (2–3 minutes) on common conditions, prevention, and facility information generate the highest engagement in EA
- Build a content series organised around condition categories; cross-post all videos to Facebook and WhatsApp

**X/Twitter — Individual medical professionals and public health advocacy**
- Ideal for building professional credibility, engaging with medical peers, and advocating on health policy
- Use conference hashtags to extend reach — hashtags double engagement on X/Twitter (Stukus et al., 2019)
- Time management: maximum 60 minutes per day split across 3–4 sessions
- Always assume any post is "on the record" — equivalent to speaking to a journalist

**TikTok — Youth health education**
- Fastest-growing platform among 16–30 demographic in EA — critical for sexual health, vaccine education, and mental health content
- High risk of health misinformation; credible healthcare creators provide essential counterbalance
- Use myth-busting format: state the myth (as the hook), disprove with evidence, provide correct information

---

## Section 5 — Content Strategy: The Trust Triangle

| Category | Purpose | Ratio | Examples |
|---|---|---|---|
| **Education** | Build knowledge and trust | 60% | Health tips, explainer videos, myth-busting, condition guides |
| **Community** | Build connection and loyalty | 30% | Patient milestones (with consent), staff introductions, events |
| **Institutional** | Drive appointments and enquiries | 10% | Service announcements, new facilities, health day promotions |

Healthcare social media that is primarily promotional will fail — it violates the trust relationship patients require.

**Content Curation Standards** (Stukus et al., 2019)
Only share third-party health content that meets all 5 criteria:
1. Published by a recognised medical institution, government health body, or peer-reviewed journal
2. Cites specific evidence (study name, sample size, publication) — not "studies show"
3. Written by a named author with verifiable credentials
4. Dated within the past 3 years, or confirmed still current
5. Free of undisclosed commercial interest

**7 Red Flags — Do Not Share If:**
- No author or institution credited
- Headline makes an extreme claim without citation
- No specific evidence cited, or vague citation ("scientists say")
- Contradicts established clinical guidelines without peer-reviewed counter-evidence
- Promotes a specific product, supplement, or service
- Uses fear or emotional manipulation rather than evidence
- Cannot be verified in 30 seconds via PubMed, WHO, or MOH Uganda website

**Content Calendar**: Planning 2+ weeks in advance and aligning with national health days (World Health Day, World Malaria Day, World AIDS Day, World Mental Health Day) increases content effectiveness by 60% compared with ad hoc posting (Stukus et al., 2019).

---

## Section 6 — Compliance and Privacy Standards

Healthcare social media in Uganda is governed by the **Uganda Data Protection and Privacy Act 2019** (DPPA) and the **Uganda Medical and Dental Practitioners Act** professional conduct standards. For international best practice, apply HIPAA (USA) de-identification principles.

**4 Principles of Patient De-identification** (Stukus et al., 2019)
Before sharing any clinical case, patient story, or health data, apply all four tests:
1. **Replicability** — Could another person reach the same privacy decision using this information?
2. **Data Source Availability** — Is the source data publicly accessible in a way that could re-identify this person?
3. **Distinguishability** — Does this person stand out from the general population in a way that makes identification possible?
4. **Risk Assessment** — What is the probability a reasonable person could identify this individual?

The combination of apparent details (approximate age + gender + location + condition) is sufficient to identify an individual even without a name. If uncertain: do not share. Obtain explicit written consent before sharing any patient photograph, video, testimonial, or case study.

**4-Component Social Media Policy** (Parsons, 2009)
Every healthcare organisation must document:
1. **Purpose** — Why the organisation uses social media and what it aims to achieve
2. **Approved Platforms and Accounts** — Which platforms are officially maintained; who is authorised to post
3. **Staff Personal Use** — Expectations for employees posting in a personal capacity, including required disclosure ("I work at X but views are my own")
4. **Crisis Protocol** — What staff must not post during a crisis; who is the designated spokesperson; escalation process

**Professional Boundary Rules** (Stukus et al., 2019)
Individual medical professionals must:
- Never befriend, follow, or accept follow requests from patients or their families on personal social media accounts
- Never provide specific diagnosis, treatment recommendation, or prescription via social media — always direct to appointment
- Disclose organisational affiliation in bio when posting in professional capacity
- Never endorse commercial products or brands without clear disclosure of any commercial relationship

---

## Section 7 — Managing Complaints, Trolls, and Negative Feedback

**4-Step Complaint Protocol** (Stukus et al., 2019; Parsons, 2009)
1. **Acknowledge** — Reply publicly within 24 hours: "Thank you for reaching out. We want to address your concern."
2. **Take Offline** — "Please contact us at [email/phone] so we can assist you directly." Never resolve a complaint in a public comment thread.
3. **Escalate** — Pass to patient relations, clinical governance, or management. Do not respond further publicly while the matter is under review.
4. **No Apologies on Social Media** — A public apology implies admitted fault and may be used in litigation. Express care and willingness to resolve, not admission of error.

**6 Troll Types and Recommended Response** (Stukus et al., 2019)

| Type | Behaviour | Response |
|---|---|---|
| Grammar/Spelling | Corrects errors, sometimes with insults | Thank briefly; correct where possible; ignore persistence |
| Political | Attacks healthcare policy positions | Ignore — political debate is unwinnable and damages credibility |
| Insult | Cyberbully with no clinical substance | Block and report; do not engage |
| Bad Experience | Genuine patient complaint via trolling | Apply 4-step complaint protocol |
| Topic (Persistent Debate) | Anti-vaccine or anti-medicine communities | Post one evidence-based response; do not continue the debate |
| Extremist | Threats, false claims to employer | Report to platform and law enforcement; notify management |

**Key principle**: If compelled to respond to any troll, wait 12–24 hours before composing the reply. Responding from anger is always a mistake (Stukus et al., 2019).

---

## Section 8 — Crisis Communication Protocol

**The 3–6 Hour Window** (Parsons, 2009): Healthcare organisations must issue an initial public statement within 3–6 hours of a crisis becoming known. Silence communicates guilt or incompetence. The first statement does not require all answers — it must demonstrate awareness, active response, and care.

**Three Prerequisites — Must Exist Before a Crisis** (Parsons, 2009)
1. **Written Crisis Communication Plan** — Approved holding statements, escalation contact tree, and media policy
2. **Designated Communication Team** — Communications lead, clinical spokesperson, legal adviser, and executive — each with a defined role
3. **Single Designated Spokesperson** — All public statements, interviews, and official social media posts during a crisis go through one approved voice

**Crisis Holding Statement Template** (Stukus et al., 2019):
> *"We are currently aware of [situation]. Our teams are actively responding. Updates will be posted on [platform/website] as information becomes available. Families with immediate concerns may contact us at [number/email]."*

**What Not to Do During a Crisis**
- Do not share photographs from the scene — never during a mass casualty event
- Do not repost third-party social media content about the crisis — accuracy cannot be verified
- Do not allow clinical staff to speak to media or post publicly without authorisation
- Do not delete negative comments — this inflames public anger and is widely noted

**The Virginia Tech Principle** (Parsons, 2009): Since 2007, social media has permanently changed healthcare crisis communication. Bystanders, staff, and witnesses post in real time. The organisation's choice is not whether information will circulate — it is whether the organisation's voice will be part of it.

---

## Quality Criteria

Output from this skill meets the standard if it:

- Identifies the client's complexity level (1–4) and adjusts strategy depth accordingly
- Maps all relevant stakeholder groups from the 11-stakeholder taxonomy, with channel and tone specified for each
- Applies all five Rogers network strategies (Access, Engage, Customise, Connect, Collaborate) with at least one specific EA-contextualised tactic per strategy
- Recommends platform priorities explicitly ranked for the client type (organisation vs individual medical professional)
- Produces a content mix recommendation with 60/30/10 Education/Community/Institutional rationale
- Addresses patient de-identification using all four principles before recommending any patient content
- Includes a social media policy framework covering all 4 components
- Specifies a 4-step complaint protocol and names the appropriate troll type responses for the client's most likely risks
- Provides a crisis communication structure including holding statement template, 3-prerequisite checklist, and Virginia Tech Principle rationale

---

## References

- Parsons, P.J. (2009) *Beyond Persuasion: The Healthcare Manager's Guide to Strategic Communication*. Stakeholder taxonomy, 4-level complexity model, TTR standard, 4-component social media policy, crisis communication structure
- Stukus, D.R., Patrick, M.D. and Nuss, K.E. (2019) *Social Media for Medical Professionals*. Platform guidance, HIPAA de-identification principles, content curation standards, troll taxonomy, complaint protocol, crisis template, professional boundary rules
- Rogers, D.L. (2011) *The Network Is Your Customer*. A-E-C-C-C framework, patient network strategy, 90-9-1 Rule, PatientsLikeMe model, customer-network-focused organisation
- Uganda Data Protection and Privacy Act 2019 — patient data and privacy obligations
- `platform-facebook/SKILL.md` — Facebook platform operational detail
- `platform-linkedin/SKILL.md` — LinkedIn for medical professionals and healthcare organisations
- `playbook-crisis-communications/SKILL.md` — Full crisis communication playbook
