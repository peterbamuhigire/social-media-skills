# Social-Media-Skills UX/UI Phase 2 Upgrade — Design Spec
**Date:** 2026-05-04
**Author:** Claude (with peter.bamuhigire@gmail.com)
**Status:** Approved
**Phase:** 2 of 3 (Phase 1 = book extractions, Phase 3 = implementation per writing-plans output)

## Context

Phase 1 produced 5 UX/UI book extractions (Levy, Enterprise UX, Branson, Deacon, Fekeshazi). Canonical extractions are at `C:\Users\BIRDC\.claude\skills\book-extractions\`; engine copies at `C:\wamp64\www\social-media-skills\book-extractions\`.

This spec defines the social-media-skills changes that translate those extractions into skill upgrades for **two clusters only**: Persona + Strategy. Other clusters (Content/copy, Visual/dashboard) are deferred to optional later specs.

## Scope

5 target skills + 1 new shared doc:

**Target skills (in `C:\wamp64\www\social-media-skills\skills\`):**
1. `03-audience-personas/SKILL.md`
2. `ai-synthetic-personas/SKILL.md`
3. `01-client-brief/SKILL.md`
4. `05-social-media-strategy/SKILL.md`
5. `13-campaign-brief/SKILL.md`

**New shared doc:**
6. `C:\wamp64\www\social-media-skills\docs\ux-foundations.md`

## Approach

Hybrid (per user choice "C"): one shared doc holds cross-cutting UX foundations referenced by multiple skills; each skill gets a focused inline append for its skill-specific application of those foundations.

**Pattern observation:** social-media skills are single-file (no `references/` folder). Inline appends and a sibling `docs/ux-foundations.md` match this pattern; introducing per-skill `references/` folders would break convention.

## New Shared Doc — `docs/ux-foundations.md`

The doc has four sections:

### Section 1 — Branson Persona Discipline
- **Stories at the centre** — personas are people, not stick figures. "You can't recount to a very remarkable anecdote about a stick figure."
- **Edge cases / "edge-cased to death" rule** — design for the Essential Persona, not for "somebody." Cooper: "Sorry, but Noah won't need to include X."
- **Designing-for-themselves trap** — designers naturally substitute themselves; rich, specific personas prevent this.
- **Choosing the Essential Persona** — pick one of the candidate personas as the absolute best target. The design specifically for the right Essential Persona will at least work for the others; a design for any other won't necessarily work for the Essential.
- **Don't average users** — averaging produces a Mr. Potato Head that works for none of them.
- **Mechanics** — first/last name, photo (volunteer or stock), short biography (work role, goals, main tasks, use stories, problems, concerns, biggest obstacles).
- **"Clingy" personas** — visibility tactics: posters, trading cards, T-shirts, coffee cups, screen wallpapers, full-size cardboard cutouts. Goal: persona stays in everyone's mind, not just the design team's.

### Section 2 — Levy Four Tenets + Anti-Patterns
- **Formula:** UX Strategy = Business Strategy + Value Innovation + Validated User Research + Killer UX Design — simultaneously-spinning plates, not phases.
- **Four misinterpretations to correct at kickoff:** North Star, "strategic way to UX design," "just product strategy," "tied to brand strategy."
- **Top-10 Not-UX-Strategies** (anti-patterns to reject in social/strategy briefs):
  1. A killer idea
  2. A laundry list of features
  3. A fully-researched plan with no need for customer feedback
  4. Permutation of trending buzzwords
  5. Generic motivational statements
  6. Arrogant statement from an expert
  7. Hypothesis with non-validated risky assumptions
  8. Grandiose vision misaligned with capabilities
  9. Vague Hallmark-card affirmation
  10. The North Star

### Section 3 — Synechron Five Outcomes (applied to social)
A premium social-media campaign must hit ALL FIVE:
1. **Useful** — addresses the persona's actual goal (not a vanity metric)
2. **Easy** — thumb-stop comprehension in ≤ 3 seconds; one clear CTA per asset
3. **Efficient** — minimal cognitive load; copy is scannable; image conveys the message even before text loads
4. **Pleasing** — visual quality matches the brand's premium positioning
5. **Accessible** — alt text on images, captions on video, readable contrast, plain-language copy

### Section 4 — Cross-references
- Canonical extractions: `book-extractions/branson-ux-ui-design-extraction.md`, `book-extractions/levy-ux-strategy-extraction.md`, `book-extractions/enterprise-ux-financial-insurance-extraction.md`, `book-extractions/deacon-ux-ui-strategy-extraction.md`, `book-extractions/fekeshazi-pm-ux-guide-extraction.md`
- Pointer to which skills consume which sections

## Per-skill Inline Edits

### 1. `skills/03-audience-personas/SKILL.md`

**Append section: "Persona discipline (Branson)"**

- Cite `docs/ux-foundations.md` Section 1 as the canonical persona-discipline reference.
- Mandatory rules specific to research-grounded persona work:
  - **Choose ONE Essential Persona per audience cluster.** A 4-persona deliverable means 4 Essential Personas, not a blurred average.
  - **Reject "edge-cased to death" feature requests.** When stakeholders say "what if a user wants X?", answer: "Persona <name> doesn't need X."
  - **"Clingy" tactic for East African client engagements:** include the persona's full name, photo placeholder, and one memorable quote on every page that references the persona — not just the persona card itself.
  - **Mechanics floor:** every persona must have name, demographics, goals, motivations, environment, pain points, stress points (Synechron list).

### 2. `skills/ai-synthetic-personas/SKILL.md`

**Append section: "Persona discipline (Branson, applied to synthetic)"**

- Cite `docs/ux-foundations.md` Section 1.
- Synthetic-persona caveats:
  - **Stronger "designing for themselves" risk.** AI generation tends to mirror the operator's assumptions. Mitigation: name the persona's pain points *before* generation; reject any persona whose pain points reduce to "agrees with the operator."
  - **Essential Persona declaration is mandatory** even for synthetic work. Pick one persona as the canonical target; document why.
  - **Edge-case discipline still applies.** Synthetic personas are not licence to design for everyone.
- Rule: synthetic personas pass the same Branson discipline gate as research-grounded personas. The disclosure already required by this skill stays in place; this section adds discipline, not transparency.

### 3. `skills/01-client-brief/SKILL.md`

**Append section: "Pre-brief filter (Levy + Deacon)"** — skill-specific only (no shared-doc citation needed for this section since the rules apply uniquely at intake)

- **Top-10 Not-UX-Strategies anti-pattern check.** During intake, score the client's stated goal against Levy's Top-10 (see `docs/ux-foundations.md` Section 2). If the goal matches any anti-pattern, push back before scoping. Document the pushback in the brief itself.
- **Three Levels of UX Scope declaration** (Deacon). Every brief must declare which level the engagement targets:
  - Single Interaction — one product, one task (most engagements)
  - Journey — multi-channel, multi-device, time-sequenced (opt-in)
  - Relationship — overall brand experience (rare, separate engagement bundle)
- **Field-of-Dreams flag** (Levy). If the brief contains no validated user research and no plan to acquire it, mark the brief as "speculative" rather than "execution-ready." This affects pricing.

### 4. `skills/05-social-media-strategy/SKILL.md`

**Append section: "Four Tenets check before strategy"**

- Cite `docs/ux-foundations.md` Section 2.
- Before producing the master strategy document, verify upstream artifacts contain evidence for all four tenets:
  - **Business Strategy** — value proposition declared in `01-client-brief`?
  - **Value Innovation** — differentiation vs competitors named in `02-platform-audit`?
  - **Validated User Research** — personas in `03-audience-personas` cite real data sources (not pure hypothesis)?
  - **Killer UX Design** — `04-brand-voice-intake` and content pillars actually distinct from category baseline?
- If any tenet is missing, return to the upstream stage before producing strategy.
- **Complementarity note (preserved):** the existing Kennedy/Wiebe direct-response filter (market / message / media / offer) operates *within* the Four Tenets framework. Both run; they don't replace each other.

### 5. `skills/13-campaign-brief/SKILL.md`

**Append section: "Five Outcomes gate before sign-off"**

- Cite `docs/ux-foundations.md` Section 3.
- For every campaign brief, declare expected pass per the five outcomes table:

| Outcome | Campaign-specific verification |
|---|---|
| Useful | The campaign addresses the persona's stated goal (not a vanity metric) |
| Easy | Thumb-stop comprehension ≤ 3 seconds; one clear CTA per asset |
| Efficient | Copy scannable; image conveys message before text loads |
| Pleasing | Visual quality matches brand premium positioning |
| Accessible | Alt text + captions + ≥ 4.5:1 contrast + plain-language copy |

- **One No = no campaign launch.** No exceptions for premium-priced campaigns.

## Out of Scope

- Cluster C (Content & copy) — `caption-writer`, `content-writing`, `direct-response-funnel-copy` etc. Separate spec if desired.
- Cluster D (Visual & dashboard) — `meta-dashboard-design` etc. Separate spec if desired.
- Modifying existing 30+ social-media book extractions
- AI-prefixed skills beyond `ai-synthetic-personas`
- Creating new skills
- Modifying `website-skills` or `srs-skills`

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Append-bloat on 250–300-line SKILL.md files | Each append capped ~30–50 lines; substantive content lives in shared doc |
| Conflict with existing Kennedy/Wiebe filter in `05-social-media-strategy` | Spec explicitly notes complementarity, not replacement |
| Synthetic-persona caveats become preachy | Keep to 3 short bullet rules, not a sermon |
| `docs/ux-foundations.md` location not yet conventional in this engine | Place at `docs/` root; reference by relative path from each SKILL.md |

## Success Criteria

- Shared doc (`docs/ux-foundations.md`) created with 4 sections (Branson personas, Levy tenets + Top-10, Synechron 5 outcomes, cross-references)
- 5 SKILL.md files each contain a new "added 2026-05-04" section with the appropriate citation
- Each SKILL.md keeps its existing structure; the append is non-destructive
- Spot-test: opening any of the 5 skills surfaces the new section within the first scroll without breaking existing flow

## Approval

Approved by user 2026-05-04 ("yes" after design presentation).

## Next Step

Invoke `superpowers:writing-plans` to create the implementation plan for the 6 file edits.
