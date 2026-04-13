---
name: playbook-webinars-live-events
description: >
  Produces a complete planning and execution playbook for digital or hybrid live events —
  webinars, Facebook Lives, Instagram Lives, YouTube Live sessions, or hybrid in-person +
  broadcast events. Calibrated for Uganda/East Africa where bandwidth is variable and mobile
  is the primary viewing device. Invoke this skill when a client wants to run an online or
  hybrid event and needs a platform recommendation, pre-event timeline, promotion calendar,
  run sheet, technical checklist, and post-event action plan.
---
# Playbook — Webinars and Live Events

<!-- dual-compat:start -->
## Use when
- Produces a complete planning and execution playbook for digital or hybrid live events — webinars, Facebook Lives, Instagram Lives, YouTube Live sessions, or hybrid in-person + broadcast events. Calibrated for Uganda/East Africa where bandwidth is variable and mobile is the primary viewing device. Invoke this skill when a client wants to run an online or hybrid event and needs a platform recommendation, pre-event timeline, promotion calendar, run sheet, technical checklist, and post-event action plan.
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

Collect all of the following before generating any deliverable:

1. **Client business name and industry**
2. **Country/city** (default: Uganda / East Africa)
3. **Event type** — choose one or more: Facebook Live, Instagram Live, YouTube Live, Zoom Webinar, Google Meet, Hybrid (in-person + broadcast)
4. **Topic and key session objectives** — what must attendees know or be able to do after the event?
5. **Target audience and estimated size** — consumer, B2B, youth, professionals; expected headcount
6. **Date, time, and duration** — confirm time zone as EAT (UTC+3)
7. **Panellists or speakers** — full names and job titles
8. **Budget** — free tools only, or is a paid platform available?
9. **Monetisation intent** — free event, paid tickets (UGX), or lead generation?
10. **Primary goal** — brand awareness, lead generation, sales, community building, or thought leadership?

---

## Section 1 — Event Type Selection

Use the table below to recommend the best platform for the client's context. Default to the EA bandwidth recommendation unless the client specifies otherwise.

| Format | Platform | Best For | EA Bandwidth Requirement | Cost |
|---|---|---|---|---|
| Facebook Live | Facebook | Broad consumer audience; existing Page followers | Low — viewers can watch on 2G/3G | Free |
| Instagram Live | Instagram | Urban, younger audience; 18–35 demographic | Medium | Free |
| YouTube Live | YouTube | Structured, longer content; searchable after broadcast | Medium–high | Free |
| Zoom Webinar | Zoom | Professional B2B, interactive, structured Q&A | High — poor on mobile data | Free (40 min) / ~UGX 56,000/month |
| Google Meet | Google | Internal training, small groups up to 100 | Medium | Free |
| Hybrid (in-person + Facebook Live) | Facebook | Maximise reach from a physical venue | Low for remote viewers | Venue/studio cost only |

**EA recommendation:** Facebook Live is the most accessible format for Uganda — viewers can watch on slow 3G/4G without buffering. For professional or B2B audiences, broadcast the Zoom Webinar simultaneously to Facebook Live (use Zoom's stream key feature) to combine structured interactivity with maximum reach.

Apply the RACE framework (Chaffey, 2024) to position the event:

- **Reach** — promotional posts and paid boosting to attract new audiences
- **Act** — registration or RSVP as the first conversion step
- **Convert** — the event itself drives the primary CTA (purchase, enquiry, sign-up)
- **Engage** — post-event replay, FAQ content, and follow-up nurture

---

## Section 2 — Pre-Event Planning (4-Week Timeline)

### Week 4 (28 days out)

- Lock the topic, date, and time. Default windows: **12:00–13:00 EAT** (lunchtime) or **18:00–19:00 EAT** (after work). Avoid before 10:00 EAT and after 20:00 EAT.
- Confirm all speakers; send a calendar invite with a one-page briefing document covering topic scope, session length, and technical requirements.
- Choose the platform; create the event page — Facebook Event, Eventbrite (free tier available), or a simple landing page.
- Write the event description: 150 words maximum. Include who it is for, what attendees will learn, and exactly how to join (link, app, or dial-in).
- Set a SMART objective (Chaffey, 2024) — e.g., "Register 200 attendees by D-1 and retain 60% for at least 30 minutes of the live session."

### Week 3 (21 days out)

- Brief the designer to produce promotional graphics: landscape (1200×628 px) for Facebook/YouTube, square (1080×1080 px) for Instagram feed, portrait (1080×1920 px) for Stories and Reels. This skill does not produce graphic files — brief a designer.
- Launch the promotional campaign: 3 social posts, 1 email to the mailing list, 1 WhatsApp broadcast message.
- Open registrations and begin tracking RSVPs.
- Publish the first speaker spotlight post on Facebook and Instagram.

### Week 2 (14 days out)

- Second promotional push: countdown Stories, "what you will learn" posts listing 3 key takeaways.
- Confirm panellist talking points; share a slide template if speakers are presenting.
- Run a full technical rehearsal: test internet connection speed (minimum 5 Mbps upload for live streaming), audio quality, camera framing, and screen share.
- Send speakers a technical guide covering camera, audio, lighting, and backup connection requirements.

### Week 1 (7 days out)

- Final reminder campaign: post 3 days before, 1 day before, and on the morning of the event.
- Prepare and circulate the run sheet (see Section 4) to all speakers and co-hosts.
- Conduct a live-stream test from the actual broadcast location — not just a home office test.
- Confirm the WhatsApp broadcast list is populated and the day-of message is drafted and ready to send.

---

## Section 3 — Promotion Calendar

Generate a day-by-day content schedule using this template. Fill in client-specific copy for each entry.

| Day | Channel | Content Type | Message Focus |
|---|---|---|---|
| D-28 | All social + email | Announcement post | Event announced; registration/RSVP link prominent |
| D-21 | Facebook + Instagram | Speaker spotlight | Introduce Speaker 1 with photo, title, and one-sentence expertise statement |
| D-21 | WhatsApp broadcast | Text message | Short message: topic, date, time EAT, join link |
| D-14 | All social + email | "What you will learn" | 3 bullet-point takeaways; registration link |
| D-14 | Facebook + Instagram | Speaker spotlight | Introduce Speaker 2 (if applicable) |
| D-7 | Email + social | Urgency post | "One week away — have you registered?" + registration link |
| D-3 | Facebook + Instagram | Countdown post | Behind-the-scenes preparation; build anticipation |
| D-1 | All channels | Final reminder | "Tomorrow at [time] EAT — join us here: [link]" |
| D-0 (08:00 EAT) | WhatsApp + email | Day-of reminder | Link to join + instructions for accessing on mobile |
| D-0 (at go-live) | Facebook | Go-live post | "We are LIVE now — join here: [link]" |
| D+1 | All channels | Recording share | Replay link + 3 key highlights + next CTA |

Apply the POEM model (Chaffey, 2024) to classify each channel: Facebook Page posts and WhatsApp broadcasts are **Owned**; organic shares and word-of-mouth are **Earned**; boosted posts are **Paid**. Recommend a small paid boost (UGX 30,000–50,000 per post) on the D-7 and D-1 posts if the client has budget.

---

## Section 4 — Run Sheet Template

Populate with the client's actual speaker names and topic titles. The host manages time; a co-host monitors comments and questions throughout.

| Time (EAT) | Segment | Owner | Notes |
|---|---|---|---|
| −15 min | Speakers join; tech check | Host | Verify audio, camera, slides, and internet for all participants |
| 00:00 | Welcome and introduction | Host | 3 minutes maximum; introduce topic, format, and speakers |
| 00:03 | Speaker 1 presentation | [Name, Title] | 12 minutes; Key Topic 1 |
| 00:15 | Q&A — Speaker 1 | Host + Co-host | 5 minutes; co-host reads questions from comments |
| 00:20 | Speaker 2 presentation | [Name, Title] | 12 minutes; Key Topic 2 |
| 00:32 | Q&A — Speaker 2 | Host + Co-host | 5 minutes |
| 00:37 | Panel discussion | All speakers | 10 minutes; 2 pre-agreed questions + live audience questions |
| 00:47 | Wrap-up and call to action | Host | What to do next; where to find the recording; next event teaser |
| 00:50 | End broadcast | Host | Thank attendees; close stream |

For single-speaker events, replace the panel block with an extended Q&A or a live demonstration. Keep total duration at or under 60 minutes — EA audiences on mobile data are sensitive to session length.

---

## Section 5 — EA Technical Checklist

Complete this checklist at the broadcast location at least 30 minutes before going live.

**Internet and connectivity**
- [ ] Use a wired ethernet connection where possible — do not rely on Wi-Fi alone
- [ ] If using mobile data, confirm full 4G signal at the exact broadcast spot — signal varies by room and floor
- [ ] Have a second mobile data hotspot (different network — e.g., MTN as primary, Airtel as backup) ready to switch within 60 seconds
- [ ] Test upload speed: minimum 5 Mbps for Facebook Live or YouTube Live; minimum 10 Mbps for Zoom Webinar with video

**Power**
- [ ] Charge all devices (laptop, phone, ring light) to 100% before the event
- [ ] Plug into mains power during broadcast — do not run on battery
- [ ] Have a UPS (uninterruptible power supply) or generator on standby for events longer than 30 minutes; Uganda load-shedding is unpredictable
- [ ] Confirm the venue has a reliable power supply; for hybrid events, brief the venue on UPS requirements

**Audio**
- [ ] Use a wired lapel microphone or a USB headset — built-in laptop microphones pick up background noise and echo
- [ ] Test audio with a colleague on the same platform before the live broadcast
- [ ] Reduce background noise: close windows, silence phones, post a "Recording in Progress" notice outside the room

**Video and lighting**
- [ ] Face a window or use a ring light — never sit with a window or bright light source behind you
- [ ] Frame the camera at eye level; avoid looking down into the lens
- [ ] Use a clean, professional background; a branded backdrop is recommended for client events
- [ ] Set camera resolution to 720p minimum; 1080p where bandwidth allows

**Pre-broadcast test**
- [ ] Go live in a private or unlisted test stream 30 minutes before the real broadcast
- [ ] Have a co-host: one person presents, one monitors comments, questions, and technical issues — do not attempt both roles simultaneously
- [ ] Prepare a contingency message to post on social media if the stream drops: "We are experiencing a technical issue — we will be back in 5 minutes. Watch here: [backup link]"

---

## Section 6 — Post-Event Actions (Within 24 Hours)

Complete all of the following within 24 hours of the event ending.

**Recording and distribution**
- Download the recording: Facebook video manager, YouTube Studio, or Zoom recording dashboard.
- If the event was not on YouTube, upload the recording there immediately. Optimise the title (include the topic keyword), description (250 words minimum with timestamps), and tags.
- Trim the intro and outro if there is dead air at the start or end — brief a video editor; this skill does not produce edited video files.

**Follow-up communications**
- Send a follow-up email to all registrants within 6 hours: thank-you message + replay link + 3 bullet-point key takeaways + one clear next CTA (book a call, download a resource, register for the next event).
- Send a WhatsApp broadcast to the broadcast list with the replay link and a one-line summary.
- Post the replay on Facebook, Instagram, LinkedIn (if B2B), and YouTube with a highlight caption of 100–150 words.

**Content repurposing**
- Identify the top 5 questions asked during the event. Turn each question into a standalone social media post, a FAQ blog post, or a short video clip — refer to `meta-content-repurposing/SKILL.md` for the full repurposing workflow.
- Extract 2–3 strong quote or statistic moments from the recording. Use these as pull-quote graphics for Instagram and LinkedIn (brief a designer for the graphic; provide the text).
- Add the event recording to the client's YouTube playlist and embed it in a blog post — refer to `blog-writer/SKILL.md` for the post structure.

**Reporting**
- Record the following metrics within 48 hours and add to the monthly report: peak concurrent viewers, total replay views (at 7 days), registrations vs. attendees (show-up rate), top questions, and CTA click-through rate.
- Update the Media Contacts Log if journalists, influencers, or public figures attended or shared the event.
- Refer to `meta-reporting/SKILL.md` for the standard reporting template.

---

## Quality Criteria

Output from this skill meets the standard when it:

1. **Platform selection is justified** with explicit reference to EA bandwidth conditions and the client's target audience — not a generic recommendation.
2. **Pre-event timeline is complete** across all four weeks with specific, dated tasks assigned to named owners (host, co-host, designer, speakers).
3. **Promotion calendar is day-by-day** with channel, content type, and message focus specified for every entry from D-28 to D+1.
4. **Run sheet includes exact timings in EAT** with each segment, speaker name, duration, and host/co-host responsibilities clearly defined.
5. **EA technical checklist is location-specific** and includes power backup (UPS/generator), dual-network internet redundancy, and audio hardware — not generic advice.
6. **Post-event actions are time-bound** (within 24 hours, within 48 hours) and include recording upload, follow-up email, WhatsApp broadcast, and replay posts.
7. **Content repurposing plan is included** converting the recording into at least 5 derivative content assets (social posts, FAQ blog, quote graphics).

---

## References

| Skill | When to use |
|---|---|
| `11-content-calendar/SKILL.md` | To build the full promotional content calendar into the client's monthly schedule |
| `07-email-marketing-strategy/SKILL.md` | To draft the registration confirmation email, reminder sequence, and post-event follow-up |
| `playbook-sms-whatsapp-marketing/SKILL.md` | To structure the WhatsApp broadcast strategy for event promotion and day-of reminders |
| `meta-content-repurposing/SKILL.md` | To build the full post-event content repurposing workflow from the recording |

**Cited works:**
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Pearson.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley.
