---
name: policy-ai-ip-and-copyright
description: >
  Generates a formal agency policy document on intellectual property and copyright for AI-assisted creative work.
  Covers IP ownership of AI-assisted deliverables, copyright qualification thresholds under UK/US/EU law, disclosure
  obligations, provenance tracking, and the standard for professional authorship. Invoke when a client asks who owns
  AI-assisted content, whether AI-generated deliverables can be copyrighted, what the agency's disclosure obligations
  are, or when onboarding a client who will receive AI-assisted work.
---
# Policy: AI, Intellectual Property, and Copyright

<!-- dual-compat:start -->
## Use when
- Generates a formal agency policy document on intellectual property and copyright for AI-assisted creative work. Covers IP ownership of AI-assisted deliverables, copyright qualification thresholds under UK/US/EU law, disclosure obligations, provenance tracking, and the standard for professional authorship. Invoke when a client asks who owns AI-assisted content, whether AI-generated deliverables can be copyrighted, what the agency's disclosure obligations are, or when onboarding a client who will receive AI-assisted work.
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
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Purpose

This skill produces a standalone policy document that the agency can hand directly to clients when questions arise about intellectual property ownership, copyright eligibility, and disclosure of AI-assisted work. The document is based on current UK, US, and EU legal frameworks as summarised in Ching and Mothi (2025) *AI for Creatives: Unlocking Expressive Digital Potential* (CRC Press).

> **Scope note:** This policy summarises the legal landscape as understood at the time of publication. It does not constitute legal advice. For contract-specific IP clauses or disputes, refer the client to a qualified IP solicitor.

---

## Required Inputs

Ask for the following before generating the policy document:

1. **Client business name** — the organisation receiving the policy
2. **Industry** — sector in which the client operates
3. **Country / city** — jurisdiction(s) relevant to the client's operations
4. **Primary goal** — why the client is requesting this document (e.g., contractual clarity, investor due diligence, internal governance, creative team guidance)
5. **Delivery types** — which categories of AI-assisted deliverables the agency produces for this client (e.g., social media copy, visual assets, long-form content, audience personas, strategy documents)
6. **Human review depth** — describe the current level of human editorial involvement in the agency's AI-assisted workflow for this client

---

## Part 1: IP Ownership — Who Owns AI-Assisted Deliverables?

### The Central Question

When the agency uses AI tools to produce content on behalf of a client, who holds the intellectual property? The answer depends on three factors:

1. The degree of human creative contribution applied by the agency
2. The jurisdiction(s) governing the contract
3. The contractual terms agreed between the agency and the client

### Agency Position

The agency retains copyright in all deliverables produced using AI tools **where a human editor, strategist, or writer has made substantive creative decisions** in the process — including selection, arrangement, modification, and editorial judgement. Such deliverables are then assigned or licensed to the client under the terms of the engagement contract.

Where a deliverable is generated substantially without human creative input, no copyright protection is available under current law in the UK, US, or EU (see Part 2). In those cases, the deliverable enters the public domain and cannot be protected.

**Practical implication:** The agency's standard workflow applies human review and editorial modification to all AI-assisted deliverables before client delivery. This is both a quality standard and a legal necessity.

---

## Part 2: Copyright Qualification Threshold

### Jurisdiction-by-Jurisdiction Summary

**United Kingdom — Copyright, Designs and Patents Act 1988**
UK law is unique in recognising "computer-generated works" where there is no human author. Section 9(3) grants copyright to "the person by whom the arrangements necessary for the creation of the work are undertaken." However, the threshold for what qualifies as sufficient "arrangement" is untested in UK courts for generative AI. The safe position is to ensure substantive human creative input at every stage. Works created *solely* by machine with no human creative selection or arrangement do not qualify for protection under the standard literary/artistic works provisions.

**United States — Title 17, §102(a), US Copyright Act**
The US Copyright Office has issued formal guidance (2023) that copyright protection does not extend to works created solely by AI. Human authorship is a constitutional and statutory requirement. The Office has granted protection to *human-selected and arranged* components of AI-assisted works, but refused protection for AI-generated elements taken in isolation. The threshold test is whether a human made sufficiently creative choices in the selection, co-ordination, or arrangement of the final work.

**European Union — Directive 2019/790 on Copyright in the Digital Single Market**
EU copyright law requires human authorship for protection. AI-generated content with no human creative contribution is not eligible for copyright under the Directive. The EU AI Act (2024) adds further obligations (see Part 3) but does not create new IP rights for AI outputs.

### Minimum Human Contribution Standard

For the agency's deliverables to qualify for copyright protection in any of the above jurisdictions, the producing human must have made at least one of the following:

- Substantive selection of which AI outputs to use and which to discard
- Meaningful editorial revision of the AI-generated text or imagery
- Creative direction decisions about structure, tone, emphasis, or arrangement
- Original framing, brief-writing, or prompt authorship that constitutes independent creative expression

A human who merely presses a button and accepts unmodified AI output without creative judgement has not met this threshold.

### The WGA 2023 Standard

The Writers Guild of America's 2023 Master Basic Agreement established a professional authorship standard that the agency adopts as its benchmark:

- AI-generated material cannot be credited as the work of a writer
- Writers retain full creative credit even when AI tools are used in the production process
- Studios and clients must disclose AI use when it affects authorship claims
- No creative professional can be mandated to use AI as a substitute for their own creative labour

**Agency application:** The agency's name and the name of any credited human creator may only appear on a deliverable where a human has made substantive creative decisions. AI is used as a production tool, not as a credited author.

---

## Part 3: Disclosure Obligations

### EU AI Act — Article 4 (Labelling Obligation)

Under the EU AI Act, providers and deployers of AI systems must ensure that content generated by AI is labelled as such when it is likely to be perceived by an audience as authentic human-created content. This obligation applies to:

- Synthetic images, audio, and video (deep fakes and AI-generated media)
- AI-generated text presented as human-authored
- AI-generated personas presented as real individuals

**Agency standard — Specific, Not Vague Disclosure**

Vague disclosure ("made with AI") does not meet the spirit of the Act or the agency's professional standard. Apply the following disclosure language where relevant:

> *"This [content type] was produced using AI-assisted tools under human editorial direction. The creative brief, final selection, and editorial decisions were made by [Agency Name]."*

Where AI has generated only supporting or draft elements and the final published work is substantially human-revised, apply:

> *"AI tools were used in the drafting process. All published content has been reviewed, edited, and approved by [Agency Name]."*

### EU AI Act — Article 28b(4) (Human Oversight Mandate)

For high-risk AI applications, Article 28b(4) requires that humans retain meaningful oversight and the ability to override AI decisions. The agency's editorial review process is designed to satisfy this requirement for all content deliverables.

---

## Part 4: Provenance Tracking and Watermarking

### Why Provenance Matters

As AI-generated content becomes indistinguishable from human-created content, clients face reputational, legal, and commercial risks if the provenance of their content cannot be verified. Provenance tracking creates an auditable record of how content was produced.

### SynthID (Google/DeepMind)

SynthID is Google DeepMind's standard for watermarking AI-generated audio and images at the point of generation. Watermarks are embedded in the content itself and can be detected even after standard post-processing. The agency recommends:

- Use SynthID-compatible tools for AI-generated audio assets wherever available
- For AI-generated images, use equivalent watermarking tools (e.g., C2PA-compliant tools supporting the Coalition for Content Provenance and Authenticity standard)

### Agency Provenance Protocol

For each AI-assisted deliverable, maintain an internal production record that captures:

1. The AI tool(s) used and version number
2. The prompt or brief submitted to the AI system
3. The name of the human reviewer who applied editorial judgement
4. A description of the substantive changes made to the AI output
5. The date of final human sign-off

Retain production records for a minimum of three years. Make them available to clients on request and to legal counsel in the event of an IP dispute.

---

## Part 5: Standing Legal Referral

### When to Escalate to an IP Solicitor

Refer the client to a qualified IP solicitor in the following circumstances:

- The client intends to register copyright in an AI-assisted work
- The client's contract with a third party requires warranties of originality for AI-assisted deliverables
- A third party has made a copyright infringement claim against the client or the agency relating to AI-generated content
- The client operates in a regulated sector where AI-generated content may be subject to additional disclosure or compliance requirements
- The client is an employer seeking to claim copyright in AI-assisted works produced by employees or contractors
- The engagement involves AI-generated content in jurisdictions other than the UK, US, or EU where the legal framework is less established

### Recommended Referral Language

> *"This document summarises the agency's policy and our understanding of the current legal framework. It is not legal advice. For contractual IP warranties, copyright registration, or dispute resolution, please consult a qualified intellectual property solicitor with experience in AI and digital content law."*

---

## Quality Criteria

A well-produced policy document under this skill:

- Accurately represents the state of UK, US, and EU copyright law without overstating protections or understating risks
- Uses plain professional language that a non-lawyer client can read and act on without confusion
- Makes the agency's standard of human creative contribution explicit and measurable, not vague
- Applies the WGA 2023 authorship standard as a professional benchmark that clients can recognise
- Specifies disclosure language that is precise enough to meet EU AI Act Article 4 obligations
- Includes a provenance protocol with named tools and a clear retention period
- Distinguishes clearly between what the agency can advise on and what requires a qualified IP solicitor
- Is formatted as a document the agency can hand directly to a client without further editing

---

## References

- Ching, V. and Mothi, D. (2025) *AI for Creatives: Unlocking Expressive Digital Potential*. CRC Press.
- UK Copyright, Designs and Patents Act 1988, Section 9(3)
- US Copyright Act, Title 17, §102(a)
- EU Directive 2019/790 on Copyright in the Digital Single Market
- EU Artificial Intelligence Act (2024), Articles 4 and 28b(4)
- Writers Guild of America (2023) *Minimum Basic Agreement* — AI provisions
- US Copyright Office (2023) *Copyright and Artificial Intelligence* — guidance documents
- Google DeepMind (2023) *SynthID* — watermarking standard for AI-generated audio and images
- Coalition for Content Provenance and Authenticity (C2PA) — open standard for content credentials
