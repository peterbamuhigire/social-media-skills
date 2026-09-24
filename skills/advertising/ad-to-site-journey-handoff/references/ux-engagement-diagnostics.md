# UX Engagement Diagnostics for Advertising Destinations

**When to read:** when an advertising plan depends on a website, app or portal whose user experience the client has not yet funded or scoped, and you must brief the client (and the receiving website-skills or design-system-skills team) on what kind of UX work, team and evidence the destination needs. This file is diagnostic and briefing material. It does not design screens; finished UX and UI work routes to `website-skills` and `design-system-skills` through the [journey handoff](../SKILL.md).

Sources (ideas synthesised; order, grouping and examples are the engine's own): Branson, S. (2020) *UX/UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*; Deacon, P. B. (2020) *UX and UI Design Strategy*; Fekeshazi, Z. (c. 2017) *Product Managers' Guide to UX Design*, UX Studio; Synechron (2018) *Bridge the User Experience Gap in Enterprise Applications for Financial Services & Insurance*; Levy, J. (2015) *UX Strategy*, O'Reilly. Statistics quoted in these sources (for example UX return-on-investment multiples) are not used; any business case must rest on the client's own baseline.

## 1. Name the design paradigm before arguing about "good design"

Stakeholders who disagree about a destination are often judging it by different standards. Ask which one dominates this project, then apply the others as checks.

| Paradigm | Judges success by | Dominant when | Check it adds to an ad destination |
|---|---|---|---|
| Engineering / building | Task completion, error reduction, productivity | Complex, well-understood workflows (quote forms, claims, applications) | Can the visitor complete the conversion task without error? |
| Human information processing | Fit to perception and memory limits | Dense choices, forms, comparison tables | Are choices chunked; is working memory respected? |
| Design thinking / experiential | Meaning, emotion, social context, minorities of use | Brand, lifestyle and community destinations | Does the page feel right for this audience and context, including users outside the average? |

Rule: the three are complementary. A brand-led landing page still needs task-level ergonomics; a form-heavy page still needs someone to ask how it feels.

## 2. Memory model for page and form decisions

- Sensory memory holds raw input for a moment; it rarely drives decisions.
- Working memory holds a few chunks for seconds and fades faster when interrupted. Group information into chunks, keep steps short, and give the visitor frequent closure (a confirmed step) rather than one long stacked task.
- Long-term memory is large but retrieval is unreliable. Prefer recognition (choose from visible options) to recall (type from memory), especially for first-time and occasional visitors; offer shortcuts only for repeat users.

## 3. Scope the UX engagement

1. **Declare the level of scope**: single interaction (one page or task), journey (several channels over time, such as ad → WhatsApp → site → email), or relationship (the whole customer experience with the organisation). Mismatched levels between client and supplier cause most scope disputes.
2. **Choose a production path by value and risk:**

| Value and risk | Path |
|---|---|
| High business value, new or complex flow | Wireframe → interactive prototype → user test → visual design → build |
| Medium | Sketch → wireframe → high-definition wireframe → visual → build |
| Lean | Sketch → wireframe → visual → build |
| Back-office, low visual weight | Sketch → build |

3. **Wireframe production steps:** research related products and the design principle; turn the research into a one-page reference (objectives, personas, contexts, competitor cues, customer quotes); map the user flow including which ad or channel sends traffic and where it should end; sketch rather than draw; add detail and test; turn wireframes into clickable prototypes.
4. **Default UX process for a product destination:** personas and analytics → user journeys (think in processes, not screens) → wireframes and prototypes → user testing and iteration before build → look-and-feel drafts → detailed designs → A/B testing of key copy (value proposition, call to action). Short weekly design sprints with research built in suit ongoing work.

## 4. What to agree with a client who commissions UX

Agree these expectations in writing before work starts:

| Expectation | What it means for the plan |
|---|---|
| Design covers how it works, not only how it looks | Budget research and flow work, not just visuals |
| The first visit decides adoption | The interface must explain itself; do not rely on tutorials |
| Quality comes from iteration | Plan several rounds and prototypes |
| The client's decision-maker takes part | Weekly feedback from the person who knows the business, with fast replies |
| It is tested and never finished | Budget for testing (quick user tests, first-impression tests, A/B tests, interviews) and for continuing improvement after launch |

Briefing points to reuse: put the key action on the screen where users need it, not in a menu; watch how experienced users work around the current system, because their workarounds show what to build; test how shapes and colours are read (for example, whether a red outline around a delivery zone on a map reads as "danger" or simply as "boundary") before launch.

## 5. Team roles and working rhythm

- Three roles, not necessarily three people: UI design (screens), UX design (flows, wireframes, prototypes, workshops), UX research (tests, interviews, analytics, personas). A single junior "doing everything" usually drops research first.
- Kick-off workshops include everyone with a stake (product, marketing, sales, development). Weekly design meetings stay small and short, with one representative per function.
- Clickable wireframes communicate better than long specification documents. When opinions conflict, let user research arbitrate.

## 6. UX maturity diagnostic

Place the client's destination owner on this ladder before promising conversion gains; the next investment is the next rung, not the top.

| Level | Signs | Next investment |
|---|---|---|
| 0 — No design | Screens assembled by developers and stakeholders | Problem definition, success criteria, basic usability review |
| 1 — Cosmetic styling | Design means colours and buttons | User research and information architecture |
| 2 — Problem-solving design | Business goals and user needs shape flows | Journey maps, task flows, prototypes tested with users |
| 3 — UX design | Flow drives the intended behaviour | Usability testing programme, experience maps |
| 4 — Experience design | Asks how the product changes the user's life | Innovation work, service design |

Activities by level (use as an audit checklist): problem definition and business objective; stakeholder interviews; agreed success criteria; qualitative and quantitative user research; competitor review; user interviews (process, device, preferences, context); personas; experience maps; user journeys; information architecture and navigation pattern (persistent, sequential, hierarchical drill-down); task flows; wireframes; clickable prototypes; visual mock-ups; mood boards; templates and design guides; heuristic review; usability testing (moderated in person, moderated remote, unmoderated remote); test scenarios; accessibility (target WCAG 2.2 AA — register CW-05, checked 2026-09-23).

Common failures of enterprise and portal destinations: feature overload, design without user research, inconsistency, technology-led look, and clutter without content strategy. The fix is the process above, not decoration.

## 7. Design thinking loop (for new destinations)

Research users and stakeholders → define needs → ideate → prototype → test with end users → deliver a proof of concept or minimum viable product; loop back from test to ideate until validation passes.

## 8. Dashboards and data visualisation shown to clients

When a destination or client report includes charts: choose the chart for the data and the decision, not decoration; avoid 3D widgets, heavy shadows and gradients; use colour to highlight meaning; give context for every number; use pre-attentive attributes (size, colour difference, orientation, proximity, similarity, connection) deliberately. Route visual production to `design-system-skills`; route dashboard content to [meta-dashboard-design](../../../meta-analytics-ops/meta-dashboard-design/SKILL.md).

## 9. Internal portals and intranets

If the ad programme targets staff or partners through a portal: design for the user's goal and context of use, keep it clean and simple, prioritise information architecture and the highest-frequency scenarios, keep content current by role, and make the look welcoming and on-brand.
