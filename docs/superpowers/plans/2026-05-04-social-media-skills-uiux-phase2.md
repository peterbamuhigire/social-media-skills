# Social-Media-Skills UX/UI Phase 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 1 shared UX-foundations doc + 5 inline SKILL.md appends across the Persona and Strategy clusters of the social-media-skills engine, integrating Branson persona discipline, Levy's Four Tenets / Top-10 anti-patterns, Synechron's 5 outcomes, and Deacon's 3 levels of UX scope.

**Architecture:** Documentation/skill upgrade. No code, no tests-as-pytest. Each task creates or extends a markdown file. Verification = file exists, expected line count or grep-for-section-header passes. One commit at the end (single commit appropriate since the changes are tightly coupled by the shared-doc reference).

**Tech Stack:** Markdown only. Sources in `C:\Users\BIRDC\.claude\skills\book-extractions\` (read-only inputs). Targets in `C:\wamp64\www\social-media-skills\`.

**Spec:** `C:\wamp64\www\social-media-skills\docs\superpowers\specs\2026-05-04-social-media-skills-uiux-phase2-design.md`

**Repo state:** `C:\wamp64\www\social-media-skills` is a git repo on `main`.

---

## File Map

```
social-media-skills/
├── docs/
│   └── ux-foundations.md                                 (create)
└── skills/
    ├── 03-audience-personas/SKILL.md                     (extend)
    ├── ai-synthetic-personas/SKILL.md                    (extend)
    ├── 01-client-brief/SKILL.md                          (extend)
    ├── 05-social-media-strategy/SKILL.md                 (extend)
    └── 13-campaign-brief/SKILL.md                        (extend)
```

**6 file edits total: 1 new + 5 extended.**

---

## Conventions

- The new shared doc starts with provenance:
  ```
  # UX Foundations — social-media-skills
  **Source:** Distilled from canonical extractions in `book-extractions/` (Phase 1 deliverable, 2026-05-04).
  **Used by:** 03-audience-personas, ai-synthetic-personas, 01-client-brief, 05-social-media-strategy, 13-campaign-brief.
  ```
- Each SKILL.md append must mark its addition: `## <Section Title> (added 2026-05-04 from <book>)`
- Do NOT modify existing frontmatter on any SKILL.md.
- Do NOT introduce emojis.
- Append at end-of-file with a leading blank line, unless the file already ends with one.

---

## Task 1: Create the shared UX-foundations doc

**Files:**
- Create: `C:\wamp64\www\social-media-skills\docs\ux-foundations.md`

- [ ] **Step 1: Write the file with this EXACT content:**

```markdown
# UX Foundations — social-media-skills
**Source:** Distilled from canonical extractions in `book-extractions/` (Phase 1 deliverable, 2026-05-04).
**Used by:** 03-audience-personas, ai-synthetic-personas, 01-client-brief, 05-social-media-strategy, 13-campaign-brief.

---

## Section 1 — Branson Persona Discipline

Source: `book-extractions/branson-ux-ui-design-extraction.md` Section 4.

### Stories at the centre
Personas are people, not stick figures. "You can't recount to a very remarkable anecdote about a stick figure." Every persona must include a name, a setting, and a quotable problem statement. Strip the narrative and you get a profile, not a persona.

### Edge cases — the "edge-cased to death" rule
Cooper's principle: it can be far better to have a much smaller percentage of users be elated than the entire public half-satisfied. Use the persona to defuse feature-creep arguments:
- Stakeholder: "What if a user wants X?"
- Designer: "Sorry, but Noah won't need X."
- Stakeholder: "But somebody might."
- Designer: "Maybe, but we are designing for Noah, not 'somebody.'"

### The "designing for themselves" trap
Designers (and AI) naturally substitute themselves into the persona's seat. Personas, when **specific and richly characterized**, prevent this. The persona's name, photo, biography, and quirks make substitution impossible.

### Choosing the Essential Persona
For a sub-role with multiple candidate personas:
- The Essential Persona's design must **at least work** for the other personas.
- A design specifically for any other persona may **not** work for the Essential.
- Don't average users — averaging produces a Mr. Potato Head that works for none of them.

### Mechanics — required attributes per persona
- First and last name (fictional, to protect real users)
- Photograph (volunteer match or non-copyrighted stock)
- Demographic information: age, education, ethnicity, etc.
- Goals & motivations
- Information about the user's social, technical, and physical environment
- Pain points & stress points
- Short biographies: work role, main tasks, use stories, problems, concerns, biggest obstacles

### "Clingy" personas (memorability tactics)
Personas need visibility and stickiness in everyone's minds — not just the design team's. Tactics observed in the field:
- Posters in the office
- Trading cards distributed to the team
- T-shirts printed with persona name + photo
- Coffee cups, screen wallpapers, full-size cardboard cutouts
- Cisco-style "action figure" dolls posed in different work settings

For East African client engagements, a softer version: include the persona's full name + photo placeholder + one memorable quote on every page that references the persona, not just the persona card itself.

---

## Section 2 — Levy Four Tenets + Anti-Patterns

Source: `book-extractions/levy-ux-strategy-extraction.md` Parts I–V.

### The formula
> **UX Strategy = Business Strategy + Value Innovation + Validated User Research + Killer UX Design**

These are simultaneously-spinning plates, not phases. If any drops, the strategy fails.

### Four misinterpretations to correct at kickoff
1. **"UX strategy is a North Star."** Reality: digital products in fast markets need agile, iterative, variable processes — not a fixed star.
2. **"UX strategy is a strategic way to do UX design."** Reality: design = creating; strategy = the game plan *before* creating. Two different disciplines.
3. **"UX strategy is just product strategy."** Reality: UX strategy spans dozens of products, services, platforms — interconnected ecosystem.
4. **"UX strategy is closely tied to brand strategy."** Reality: a poor UX decreases brand value, but the brandiest brand cannot rescue a poor UX.

### Top-10 Not-UX-Strategies (anti-patterns to reject in social/strategy briefs)
If a client's stated goal matches any of these, push back before scoping.

1. A killer idea for a new product
2. A laundry list of features
3. A thoroughly researched plan with no need for customer feedback
4. Permutation of trending buzzwords ("peer-to-peer sharing economy")
5. Generic motivational statements ("Go Team Challenge Conquer")
6. An arrogant statement from an expert
7. A hypothesis with non-validated risky assumptions ("all women like pink")
8. A grandiose vision misaligned with company capabilities
9. A vague Hallmark-card affirmation
10. The North Star

---

## Section 3 — Synechron Five Outcomes (applied to social)

Source: `book-extractions/enterprise-ux-financial-insurance-extraction.md` Part I.

A premium social-media campaign must hit ALL FIVE outcomes. One No = no launch.

| # | Outcome | Campaign-specific verification |
|---|---|---|
| 1 | **Useful** | The campaign addresses the persona's stated goal (not a vanity metric) |
| 2 | **Easy** | Thumb-stop comprehension in ≤ 3 seconds; one clear CTA per asset |
| 3 | **Efficient** | Copy scannable; image conveys message before text loads |
| 4 | **Pleasing** | Visual quality matches brand premium positioning |
| 5 | **Accessible** | Alt text + captions + ≥ 4.5:1 contrast + plain-language copy |

---

## Section 4 — Cross-references

### Canonical extractions (source-of-truth)
- `book-extractions/branson-ux-ui-design-extraction.md`
- `book-extractions/levy-ux-strategy-extraction.md`
- `book-extractions/enterprise-ux-financial-insurance-extraction.md`
- `book-extractions/deacon-ux-ui-strategy-extraction.md`
- `book-extractions/fekeshazi-pm-ux-guide-extraction.md`

### Skill consumption map
- **`skills/03-audience-personas/`** — uses Section 1 (full persona discipline)
- **`skills/ai-synthetic-personas/`** — uses Section 1 (with synthetic-persona caveats)
- **`skills/01-client-brief/`** — uses Section 2 (Top-10 anti-patterns) + Deacon's Three Levels of UX Scope (skill-local rule)
- **`skills/05-social-media-strategy/`** — uses Section 2 (Four Tenets check) — complementary to existing Kennedy/Wiebe direct-response filter
- **`skills/13-campaign-brief/`** — uses Section 3 (Five Outcomes gate)

### Phase 2 spec
This document was created as part of the Phase 2 upgrade described in `docs/superpowers/specs/2026-05-04-social-media-skills-uiux-phase2-design.md`.
```

- [ ] **Step 2: Verify**

Run: `wc -l "C:/wamp64/www/social-media-skills/docs/ux-foundations.md"`
Expected: ≥ 100 lines.

Run: `grep -c "^## Section " "C:/wamp64/www/social-media-skills/docs/ux-foundations.md"`
Expected: 4.

---

## Task 2: Append to `skills/03-audience-personas/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\social-media-skills\skills\03-audience-personas\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/social-media-skills/skills/03-audience-personas/SKILL.md"`
Note the last line so the append starts on a fresh line.

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Persona discipline (added 2026-05-04 from Branson)

Canonical reference: `docs/ux-foundations.md` Section 1.

For research-grounded persona work specifically (this skill), the following rules apply on top of the shared discipline:

- **Choose ONE Essential Persona per audience cluster.** A 4-persona deliverable means 4 Essential Personas, not a blurred average. Document the choice and the reasoning.
- **Reject "edge-cased to death" feature requests.** When stakeholders ask "what if a user wants X?", answer: "Persona <name> doesn't need X." Use the persona's name, not "the user."
- **"Clingy" tactic for East African client engagements.** Include the persona's full name, photo placeholder, and one memorable quote on every page that references the persona — not just the persona card itself.
- **Mechanics floor.** Every persona must have name, demographics, goals, motivations, social/technical/physical environment, pain points, stress points (Synechron list).

If a stakeholder pushes back on the Essential Persona choice, walk them through `docs/ux-foundations.md` Section 1 ("Choosing the Essential Persona" subsection) — the design specifically for the right Essential Persona will at least work for the others; a design for any other won't necessarily work for the Essential.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Persona discipline (added 2026-05-04 from Branson)" "C:/wamp64/www/social-media-skills/skills/03-audience-personas/SKILL.md"`
Expected: 1.

Run: `grep -c "Essential Persona" "C:/wamp64/www/social-media-skills/skills/03-audience-personas/SKILL.md"`
Expected: ≥ 2.

---

## Task 3: Append to `skills/ai-synthetic-personas/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\social-media-skills\skills\ai-synthetic-personas\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/social-media-skills/skills/ai-synthetic-personas/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Persona discipline applied to synthetic (added 2026-05-04 from Branson)

Canonical reference: `docs/ux-foundations.md` Section 1.

Synthetic personas pass the same Branson discipline gate as research-grounded personas. The disclosure already required by this skill stays in place; this section adds discipline, not transparency.

Three caveats specific to AI-generated personas:

- **Stronger "designing for themselves" risk.** AI generation tends to mirror the operator's stated assumptions back at them. **Mitigation:** name the persona's pain points *before* generation; reject any synthetic persona whose pain points reduce to "agrees with the operator."
- **Essential Persona declaration is mandatory** even for synthetic work. Pick one persona as the canonical target; document why it was chosen over the others. Do not produce 4 synthetic personas without naming which is Essential.
- **Edge-case discipline still applies.** Synthetic personas are not licence to design for everyone. The "Sorry, but Noah won't need X" answer holds whether Noah is a real or synthetic persona.

If the synthetic persona output cannot satisfy these three caveats, the deliverable is not ready to ship. Either return to primary research (use `03-audience-personas` instead) or rerun with stronger constraints.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Persona discipline applied to synthetic" "C:/wamp64/www/social-media-skills/skills/ai-synthetic-personas/SKILL.md"`
Expected: 1.

Run: `grep -c "designing for themselves\|Essential Persona\|edge-case" "C:/wamp64/www/social-media-skills/skills/ai-synthetic-personas/SKILL.md"`
Expected: ≥ 3.

---

## Task 4: Append to `skills/01-client-brief/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\social-media-skills\skills\01-client-brief\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/social-media-skills/skills/01-client-brief/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Pre-brief filter (added 2026-05-04 from Levy + Deacon)

Three checks to apply during intake — before scoping or pricing:

### 1. Top-10 Not-UX-Strategies anti-pattern check (Levy)

See `docs/ux-foundations.md` Section 2 for the full list. During intake, score the client's stated goal against the Top-10. If the goal matches any anti-pattern, push back before scoping. Document the pushback in the brief itself under a "Brief filters applied" subsection so future audits can trace the conversation.

Most common matches in social-media intakes:
- "We need a killer Instagram strategy" → matches #1 (a killer idea) — push back, ask what problem the client is solving
- "We want viral content" → matches #5 (motivational generic) — push back, ask which persona for what action
- "We just need posts that look like [trending brand]" → matches #4 (buzzword permutation) — push back, ask what differentiated promise

### 2. Three Levels of UX Scope declaration (Deacon)

Every brief must declare which level the engagement targets:

- **Single Interaction** — one platform, one campaign, one task. Most engagements live here.
- **Journey** — multi-channel, multi-device, time-sequenced (e.g., social → email nurture → website). Opt-in upgrade.
- **Relationship** — overall brand experience across all touchpoints. Rare; treat as a separate engagement bundle.

Add the level declaration as a required field in the intake questionnaire and the at-a-glance card.

### 3. Field-of-Dreams flag (Levy)

If the brief contains no validated user research and no plan to acquire it, mark the brief as "speculative" rather than "execution-ready." This affects pricing — speculative work cannot be priced as a delivery engagement; it must be priced as a discovery engagement first.

If the client refuses discovery and demands execution-priced delivery on a speculative brief, decline the work or document the risk acceptance in writing.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Pre-brief filter (added 2026-05-04" "C:/wamp64/www/social-media-skills/skills/01-client-brief/SKILL.md"`
Expected: 1.

Run: `grep -c "Single Interaction\|Field-of-Dreams\|Top-10" "C:/wamp64/www/social-media-skills/skills/01-client-brief/SKILL.md"`
Expected: ≥ 3.

---

## Task 5: Append to `skills/05-social-media-strategy/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\social-media-skills\skills\05-social-media-strategy\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/social-media-skills/skills/05-social-media-strategy/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Four Tenets check before strategy (added 2026-05-04 from Levy)

Canonical reference: `docs/ux-foundations.md` Section 2.

Before producing the master strategy document, verify upstream artifacts contain evidence for all four tenets:

| Tenet | Where to verify | Pass criterion |
|---|---|---|
| **Business Strategy** | `01-client-brief` | Value proposition declared; revenue stream identified |
| **Value Innovation** | `02-platform-audit` | Differentiation vs competitors named with specifics |
| **Validated User Research** | `03-audience-personas` (or `ai-synthetic-personas`) | Personas cite real data sources, not pure hypothesis |
| **Killer UX Design** | `04-brand-voice-intake` + content pillars | Voice and pillars actually distinct from category baseline |

If any tenet is missing, return to the upstream stage before producing strategy. Do not paper over a missing tenet with a stronger headline; the strategy will fail downstream.

### Complementarity with existing direct-response filter

The Kennedy/Wiebe direct-response filter (market / message / media / offer) already specified in this skill operates **within** the Four Tenets framework, not in place of it. Both run; they don't replace each other:

- Four Tenets → does this strategy belong in market at all?
- Market/Message/Media/Offer → if so, what is the operational shape of the next campaign?

Apply Four Tenets first as a gate; apply Kennedy/Wiebe second as a structure.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Four Tenets check before strategy" "C:/wamp64/www/social-media-skills/skills/05-social-media-strategy/SKILL.md"`
Expected: 1.

Run: `grep -c "Business Strategy\|Value Innovation\|Validated User Research\|Killer UX Design" "C:/wamp64/www/social-media-skills/skills/05-social-media-strategy/SKILL.md"`
Expected: ≥ 4.

---

## Task 6: Append to `skills/13-campaign-brief/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\social-media-skills\skills\13-campaign-brief\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/social-media-skills/skills/13-campaign-brief/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Five Outcomes gate before sign-off (added 2026-05-04 from Synechron Enterprise UX)

Canonical reference: `docs/ux-foundations.md` Section 3.

Every campaign brief must declare expected pass per the five outcomes table below. **One No = no campaign launch.** No exceptions for premium-priced campaigns.

| # | Outcome | Campaign-specific verification |
|---|---|---|
| 1 | **Useful** | The campaign addresses the persona's stated goal (not a vanity metric like "more followers") |
| 2 | **Easy** | Thumb-stop comprehension in ≤ 3 seconds; one clear CTA per asset |
| 3 | **Efficient** | Copy scannable; image conveys message before text loads on slow connections |
| 4 | **Pleasing** | Visual quality matches brand premium positioning; not "good enough" |
| 5 | **Accessible** | Alt text + captions + ≥ 4.5:1 contrast + plain-language copy |

### How to apply at sign-off

Add a "Five Outcomes" subsection to the campaign brief with a one-paragraph Yes/No declaration per outcome and the evidence behind each Yes:

- Useful — Yes, because [persona X's goal Y is addressed by asset Z]
- Easy — Yes, because [the 3-second user-test result was X]
- Efficient — Yes, because [text-load fallback shows complete message]
- Pleasing — Yes, because [visual reference comparison passed]
- Accessible — Yes, because [alt text written, captions ready, contrast measured at X.X:1]

If any outcome cannot be declared Yes with evidence, the campaign cannot ship. The brief returns to the strategy or content stage to close the gap.

### Why "Accessible" is non-optional

Most social-campaign briefs in the wild treat accessibility as cleanup. The Synechron rule treats it as a launch gate. For premium-priced engagements ($20k+) the cost of an accessibility-rejection at launch (legal exposure on regulated industries; brand damage on inclusive-marketing claims) far exceeds the cost of building accessibility in.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Five Outcomes gate before sign-off" "C:/wamp64/www/social-media-skills/skills/13-campaign-brief/SKILL.md"`
Expected: 1.

Run: `grep -c "Useful\|Easy\|Efficient\|Pleasing\|Accessible" "C:/wamp64/www/social-media-skills/skills/13-campaign-brief/SKILL.md"`
Expected: ≥ 5.

---

## Task 7: Commit

- [ ] **Step 1: Stage and commit all 6 file edits in one commit**

```bash
cd "C:/wamp64/www/social-media-skills"
git add docs/ux-foundations.md \
  skills/03-audience-personas/SKILL.md \
  skills/ai-synthetic-personas/SKILL.md \
  skills/01-client-brief/SKILL.md \
  skills/05-social-media-strategy/SKILL.md \
  skills/13-campaign-brief/SKILL.md
git status  # confirm 6 files staged
git commit -m "$(cat <<'EOF'
social-media-skills: integrate UX foundations into Persona + Strategy clusters

Phase 2 UX upgrade per spec 2026-05-04-social-media-skills-uiux-phase2-design.md.
- New shared doc docs/ux-foundations.md (4 sections: Branson personas, Levy tenets + Top-10, Synechron 5 outcomes, cross-references)
- 03-audience-personas: Branson persona discipline section appended
- ai-synthetic-personas: discipline applied to synthetic with 3 caveats
- 01-client-brief: pre-brief filter (Top-10 anti-patterns, 3 levels of scope, Field-of-Dreams flag)
- 05-social-media-strategy: Four Tenets check, complementary to existing Kennedy/Wiebe filter
- 13-campaign-brief: Five Outcomes gate (one No = no launch)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
git log -1 --stat
```

Expected: 6 files changed (1 new + 5 modify).

- [ ] **Step 2: Verify commit**

Run: `git log -1 --name-only`
Expected output includes all 6 file paths.

---

## Task 8: End-to-end verification

- [ ] **Step 1: All 6 file edits exist and contain expected markers**

Run:

```bash
cd "C:/wamp64/www/social-media-skills"

# New file exists
test -f docs/ux-foundations.md && echo "OK: docs/ux-foundations.md"

# All 5 SKILL.md files contain the 2026-05-04 marker
grep -l "added 2026-05-04" \
  skills/03-audience-personas/SKILL.md \
  skills/ai-synthetic-personas/SKILL.md \
  skills/01-client-brief/SKILL.md \
  skills/05-social-media-strategy/SKILL.md \
  skills/13-campaign-brief/SKILL.md
```

Expected: 1 "OK:" line + 5 file paths.

- [ ] **Step 2: Each SKILL.md references either the shared doc or a Levy/Branson/Synechron concept**

Run:

```bash
cd "C:/wamp64/www/social-media-skills"
for f in \
  skills/03-audience-personas/SKILL.md \
  skills/ai-synthetic-personas/SKILL.md \
  skills/01-client-brief/SKILL.md \
  skills/05-social-media-strategy/SKILL.md \
  skills/13-campaign-brief/SKILL.md \
; do n=$(grep -c "ux-foundations\|Branson\|Levy\|Synechron\|Four Tenets\|Five Outcomes\|Essential Persona\|Top-10" "$f"); echo "$f: $n matches"; done
```

Expected: 5 lines, each with count ≥ 1.

- [ ] **Step 3: Final report**

Print a one-paragraph summary:
- Number of new files created (expect 1)
- Number of files extended (expect 5)
- Commit SHA from `git log -1 --format=%H`
- Any verification step that did not match expectation (should be none)

If any verification fails, do not declare the plan complete; create a follow-up task to fix and re-verify.

---

## Self-Review (executed by writing-plans skill)

**1. Spec coverage:**
- Shared doc with 4 sections → Task 1 ✓
- 03-audience-personas append → Task 2 ✓
- ai-synthetic-personas append → Task 3 ✓
- 01-client-brief append (Top-10 + 3 levels + Field-of-Dreams) → Task 4 ✓
- 05-social-media-strategy append (Four Tenets + complementarity) → Task 5 ✓
- 13-campaign-brief append (5 outcomes gate) → Task 6 ✓
- Commit → Task 7 ✓
- Verification → Task 8 ✓

**2. Placeholder scan:** No "TBD"/"TODO"/"implement later"/"add validation"/"handle edge cases" present. Each new section has full content provided in the task.

**3. Type consistency:** All file paths consistent. Section names match between the shared doc and the citations in each SKILL.md ("Section 1", "Section 2", "Section 3"). The phrase "Essential Persona" used uniformly. "Five Outcomes" capitalized consistently.

No issues to fix.
