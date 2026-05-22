---
name: playbook-content-production
description: Generates a comprehensive content production brief and shoot direction guide covering photography, video, and graphic design briefs, a batch production workflow, and a printable shoot-day checklist. Invoke this skill when briefing a photographer, videographer, or in-house team before a content shoot, or when helping a client establish a repeatable monthly content production process. This is a planning and briefing tool — it does not produce designs, edit video, or generate images.
---
# Content Production Playbook

<!-- dual-compat:start -->
## Use when
- Generates a comprehensive content production brief and shoot direction guide covering photography, video, and graphic design briefs, a batch production workflow, and a printable shoot-day checklist. Invoke this skill when briefing a photographer, videographer, or in-house team before a content shoot, or when helping a client establish a repeatable monthly content production process. This is a planning and briefing tool — it does not produce designs, edit video, or generate images.
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

## Required Input

Collect the following before generating the production guide:

- **Client name** and business type (product / service / both)
- **Shoot date** and location
- **Platforms** the content is intended for (determines formats and dimensions required)
- **Products or services** to feature in the shoot — list them specifically
- **Brand colours** — hex codes if available; describe if not
- **Brand fonts** — name the fonts used in existing materials
- **Team members** available on the shoot day — names and roles (owner, staff, model, none)
- **Campaign content** — any specific campaign, promotion, or seasonal moment to capture
- **Country/city** — defaults to Uganda/East Africa if not specified

---

## 1. Photography Brief Template

Complete this brief before the shoot and share it with the photographer or team lead.

**Client:** [Client Name]
**Shoot Date:** [Date]
**Location:** [Address and specific area within location — e.g. "storefront entrance, back kitchen, rooftop"]
**Platforms:** [List platforms — determines orientation and framing requirements]

### Scene Descriptions
Write one paragraph per scene. Each paragraph covers: where the shot is taken, who is in it, and what is happening. Example: "Owner standing behind the counter serving a customer. Warm, natural morning light from the left window. Counter is clear and products are displayed tidily. Owner is smiling and making eye contact with the customer."

### Required Shots List (8–12 per shoot)

Include all of the following that apply to this client:

1. **Hero product shot** — clean background, product centre-frame, sharp focus, no distractions
2. **Lifestyle in context** — product or service being used in a real setting (customer using the product, team delivering the service)
3. **Team or people shot** — owner or staff in a natural working moment; avoid stiff posed group photos
4. **Behind-the-scenes** — preparation, process, craftsmanship; shows authenticity
5. **Detail or close-up shot** — texture, ingredients, craftsmanship detail; creates visual variety
6. **Location or context shot** — exterior of premises, neighbourhood, establishing shot for brand place identity
7. **Testimonial setup** (if filming) — subject seated comfortably, good light on face, clean background behind them
8. **Portrait orientation version** — shoot every key scene in both landscape (16:9) and portrait (9:16 or 4:5); do not assume one orientation covers all platforms
9. **Flat lay** (for product businesses) — products arranged overhead on a clean, on-brand surface
10. **Action shot** — movement, energy; avoids the static quality of posed photography
11. **Before/after** (if relevant) — service transformation; powerful for salons, cleaning, construction, food preparation
12. **Brand detail shot** — logo on packaging, branded uniform, business card or signage; reinforces brand presence

### Lighting Guidance

Natural light is strongly preferred. For outdoor shoots in Uganda/East Africa, schedule the shoot for 07:00–09:00 (golden hour — soft, warm, directional light) or 16:30–18:00 (evening golden hour). Avoid 10:00–14:00 — harsh equatorial midday sun creates unflattering shadows and blown-out highlights.

For indoor shoots: position subjects near the largest window available. If artificial light is required, use a ring light or a softbox positioned at 45 degrees to the subject. Avoid direct flash — it flattens images and creates harsh shadows.

### Photography Do's
- Shoot in brand colours — style the scene with brand-relevant props, packaging, and colours
- Show real people — the client's actual team and real customers where possible; authentic faces outperform stock-style imagery in the EA market
- Capture genuine moments, not staged poses — direction should be "do the thing naturally and we will photograph it", not "hold that pose"
- Shoot landscape AND portrait for every key scene — different platforms require different crops and both are needed for a complete content library
- Shoot more than you think you need — aim for 3–5 versions of each scene; editing will reveal the best one

### Photography Don'ts
- No blurry, dark, or poorly exposed images — check images on a screen before the shoot team disperses
- No cluttered or distracting backgrounds — clear the scene before shooting
- No visible competitor branding in frame — check packaging, signage, clothing
- No images that contradict the brand tone — if the brand is premium, avoid images that look cheap; if the brand is warm and human, avoid cold and corporate compositions

---

## 2. Video Brief Template

Complete this brief for each video asset required.

**Client:** [Client Name]
**Video Title / Working Name:** [e.g. "Product demo — [Product Name]"]
**Platform(s):** [Determines duration and format]
**Shoot Date:** [Date]

### Duration Targets by Platform

| Platform | Target Duration |
|---|---|
| TikTok / Instagram Reels | 15–45 seconds |
| Instagram Stories | Up to 15 seconds per card |
| Facebook feed video | 30–90 seconds |
| WhatsApp Status / Broadcast | Under 60 seconds |
| LinkedIn | 30–90 seconds |
| YouTube (educational / tutorial) | 5–12 minutes |
| YouTube Shorts | Under 60 seconds |

### Scene and Setting Description
[Where is the video filmed? What is happening? Who is speaking or appearing?]

### Dialogue or Voiceover Plan
[Option A: Scripted — write the full script here.]
[Option B: Talking points — "Subject speaks naturally to camera covering these points: [list 3–5 points]. Do not script word-for-word; natural delivery preferred."]
[Option C: No dialogue — describe what the visuals show and what music/audio will accompany.]

### B-Roll List (Supporting Footage)
Shoot the following alongside the main footage to give the editor cutting options:

- [ ] Product detail shots (hands holding, pouring, opening, applying)
- [ ] Process shots (preparation, packaging, service delivery)
- [ ] Reaction shots (customer receiving the product/service; genuine response)
- [ ] Team interaction shots (natural working moments)
- [ ] Location B-roll (exterior, signage, street context)
- [ ] Close-up texture or ingredient shots

### Captions
Captions are required on all videos. Specify to the editor: add captions using CapCut auto-caption, YouTube auto-caption (check and correct), or manual SRT file. Captions are not optional — the majority of social video is watched without sound in the EA market.

### Call to Action
What does the video say or show at the end? [e.g. "Visit our website", "WhatsApp us on [number]", "Follow for more", "Order now — link in bio"]. The CTA must be stated verbally AND shown on screen.

### Branding
- Logo placement: [Intro card / watermark bottom-right / outro card — choose one or combine]
- Intro: [Does the video open with a branded title card? Duration: 2–3 seconds maximum]
- Outro: [Branded end card with CTA and logo? Duration: 3–5 seconds]
- Watermark: [Subtle bottom-corner watermark throughout, or clean without watermark?]

---

## 3. Graphic Design Brief Template

Complete this brief for each designed asset and share it with the graphic designer.

**Client:** [Client Name]
**Asset Name:** [e.g. "March promotion — Instagram feed post"]
**Platform and Placement:** [Determines dimensions]

### Standard Dimensions by Platform

| Platform / Placement | Dimensions |
|---|---|
| Facebook feed (landscape) | 1200 × 630 px |
| Facebook / Instagram feed (square) | 1080 × 1080 px |
| Instagram feed (portrait) | 1080 × 1350 px |
| Instagram Stories / Reels cover | 1080 × 1920 px |
| LinkedIn feed | 1200 × 627 px |
| WhatsApp broadcast image | 800 × 800 px (square performs best) |
| TikTok thumbnail | 1080 × 1920 px |
| YouTube thumbnail | 1280 × 720 px |
| Facebook / LinkedIn cover photo | 1640 × 924 px |

### Key Message
**Headline (maximum 6 words on the graphic):** [Write the headline here]
**Supporting text (optional — maximum 15 words):** [Write here or mark as not required]
**CTA text:** [e.g. "Order now", "WhatsApp us", "Learn more"]

### Brand Elements
- **Primary colour:** [Hex code]
- **Secondary colour:** [Hex code]
- **Accent colour:** [Hex code if applicable]
- **Primary font:** [Name and weight — e.g. Montserrat Bold for headlines]
- **Secondary font:** [Name and weight — e.g. Open Sans Regular for body text]

### Image Guidance
[Describe the photo or illustration to use: "Use the hero product shot from the [date] shoot — clean background version." Or: "Use a lifestyle photo of a customer using the product in a real setting."]

### Text Hierarchy
1. Headline — largest text, high contrast, immediately readable at thumbnail size
2. Supporting text — smaller, secondary importance
3. CTA — distinct button or text block; visually separated from the headline
4. Logo — present but not dominant; bottom corner or bottom centre

### Design Do's and Don'ts
- Do maintain enough contrast between text and background for readability on a mobile screen
- Do leave adequate white space — overcrowded graphics perform poorly
- Do use brand fonts consistently — do not substitute with default system fonts
- Do not use more than two font families in a single graphic
- Do not use colours outside the brand palette without prior approval
- Do not place important text or the logo in the outer 10% of the frame (safe area — will be cropped on some platforms)

---

## 4. Batch Production Workflow

Batch production reduces content creation cost by 60–80% compared to ad hoc shoots. One well-planned shoot day can produce 4–6 weeks of content. Follow this workflow.

### Step 1 — Prepare (Day Before the Shoot)
- Open the content calendar and confirm which content types are needed for the next 4–6 weeks
- Print the shot list and video brief; share with everyone attending the shoot
- Gather and prepare all props, products, packaging, and branded items
- Confirm outfits for all team members — they should align with brand colours
- Charge all equipment: phone, camera, ring light, stabiliser, lapel microphone
- Scout the location if not already familiar — confirm backgrounds are clean and on-brand
- Confirm with all team members: time, location, what to wear, what to bring

### Step 2 — Morning Session (Approximately 2 Hours)
Shoot all photography content during this session. Morning light (07:00–09:00) is optimal. Work through the shot list systematically — do not skip scenes. Check images on a screen, not just the camera display, before moving on.

### Step 3 — Midday Session (Approximately 1 Hour)
Shoot all video content: talking-head videos, product demonstrations, testimonials. Use indoor light or shade at this time to avoid harsh midday sun. Work from the video brief and B-roll list.

### Step 4 — Afternoon Session (Approximately 1 Hour)
Shoot behind-the-scenes content, candid team moments, and informal footage. This session is lower pressure — use it for experimentation. Golden hour (16:30–18:00) is available at the end of this session for any remaining outdoor photography.

### Step 5 — Post-Shoot Review (30 Minutes)
Review all images and video on a laptop or large screen before the team disperses. Identify any re-shoots needed while the team, props, and location are still available. Confirm you have covered the full shot list.

### Step 6 — Editing and Scheduling (2–3 Days After the Shoot)
Edit photos (basic colour correction and crop); edit videos (captions, logo, CTA, B-roll cuts). Write captions. Load content into Buffer or Hootsuite and schedule across the full content calendar period. Notify the client that content is loaded and ready for review before publishing begins.

---

## 5. Content Shoot Checklist

Print this checklist and bring it to the shoot.

**Pre-Shoot (Confirm All the Night Before)**
- [ ] Shot list printed and confirmed with all team members
- [ ] All products, props, and packaging gathered and clean
- [ ] Location scouted — backgrounds are clear and on-brand
- [ ] All equipment charged: phone/camera, ring light, stabiliser, lapel microphone
- [ ] Memory cards cleared or new storage available
- [ ] Outfits and uniforms confirmed — align with brand colours
- [ ] Content calendar open — confirmed what is needed for the next 4–6 weeks
- [ ] Branded elements ready: logo props, branded packaging, brand-coloured surfaces
- [ ] Natural light window or outdoor timing confirmed (07:00–09:00 or 16:30–18:00 EAT)
- [ ] Written permission obtained from any person appearing in the shoot who is not a team member

**On the Day**
- [ ] Arrive early enough to set up before the best light window
- [ ] Work through the shot list in order — tick off each scene as completed
- [ ] Check images on a screen (not just the camera display) before moving on
- [ ] Shoot portrait AND landscape orientation for every key scene
- [ ] Review all footage before the team leaves

---

---

## 6. Content Quality Standard

Before approving any piece of content for publication, apply these two filters:

**The "Share or Solve" Test (Handley, 2012):**
Does this content either (a) solve a real problem the audience has, or (b) create something the audience wants to share? If the answer is neither, do not publish it. Content that exists only to show the brand exists is wasted effort.

**The Six Story Characteristics (Handley, 2012):**
Strong content — whether video, photography caption, or graphic — is:
1. **True** — based on real experience, real results, or verified facts
2. **Relevant** — speaks to a specific problem or aspiration the audience recognises
3. **Human** — has a real person or real story at its centre
4. **Passionate** — the creator visibly cares about the topic
5. **Original** — a fresh angle, not a rephrase of what competitors already posted
6. **Surprising** — contains at least one unexpected element

**The "Think Like a Publisher" principle (Meerman Scott, 2022):**
Approach the shoot day editorial plan the way a magazine editor approaches an issue. Each piece of content has a purpose in the reader's/viewer's journey. Before briefing the photographer or videographer, ask: what is this content trying to make the audience think, feel, or do? Brief for that outcome — not just for a visual deliverable.

---

## Quality Criteria

Output meets production standard when it satisfies all of the following:

- The photography brief includes a specific, scene-by-scene shot list of 8–12 shots tailored to the client's product or service — not a generic list
- The video brief includes a complete B-roll list and states captions as mandatory, not optional
- The graphic design brief includes the correct platform dimensions table and a clear text hierarchy instruction
- Batch production workflow steps are assigned realistic time blocks that add up to a full working day
- All platform dimensions in the design brief are current and accurate
- Lighting guidance is specific to the East African context (equatorial sun timing, golden hour windows in EAT)
- The shoot checklist is formatted for printing and use on the day — not as a reference section in a longer document
- All content uses British English; no American spellings appear in any section
