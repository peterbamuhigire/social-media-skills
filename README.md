# social-media-skills

See [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md) for
campaign agent roles, thin commands, publication hooks, evidence, and
stop/recovery behavior.

`social-media-skills` is a professional social-media and digital-marketing consultancy engine for strategy, content, campaigns, community, analytics, training, AI-assisted marketing, and client-facing reporting.

Its default operating context is Uganda and East Africa: British English, UGX unless another currency is specified, EAT (UTC+3), mobile-first delivery, and WhatsApp-first customer journeys. When a client names another market, replace these defaults with the specified market's audience, language, channel, pricing, legal, cultural, and conversion assumptions.

## What this engine produces

The engine produces text-first, reviewable consultancy artefacts, including:

- market and social-media strategies;
- platform audits, channel architecture, audience and brand-voice work;
- content pillars, calendars, briefs, captions, articles, email, SEO/GEO content, and repurposing plans;
- campaign strategies, campaign briefs, influencer, UGC, community, social-commerce, WhatsApp, and launch playbooks;
- paid/organic/hybrid recommendations and funnel content;
- analytics frameworks, dashboards specifications, KPI reports, ROI and attribution models, testing plans, social listening, competitor analysis, and content audits;
- AI-marketing strategy, readiness assessments, vendor and data audits, prompt systems, RAG knowledge bases, chatbots, agentic workflows, and AI-content policies;
- client training, DIY content guidance, smartphone-video briefs, and team operating models;
- proposals, credentials, decks and presentation outlines. Visual design and final deck production route to `design-system-skills`.

The engine does not produce finished graphic design, video edits, websites, software, or live-account changes. It can specify, audit, brief, and govern those outputs, then route implementation to the appropriate specialist engine.

## Current capability surface

The repository currently contains 177 active `SKILL.md` files across 16 capability groups:

| Group | Coverage |
|---|---|
| `business-development` | Credentials, offers, outreach, reactivation, EAC calls and campaign-facing business development |
| `ai-marketing` | AI strategy, content workflows, vendor/data readiness, agents, personalisation, disclosure, bias, privacy, slop control and evaluation |
| `content-writing` | Captions, blogs, email, direct response, whitepapers, prompts, image/audio/video briefs and human-quality editing |
| `frameworks` | Planning and strategic models |
| `language` | East African English, language standards, French and Kiswahili copy |
| `meta-analytics-ops` | Audits, reporting, testing, ROI, attribution, listening, dashboards, metrics, privacy and measurement |
| `meta-utility` | Skill authoring, safety auditing, and the Kaizen improvement system |
| `pipeline` | Brief-to-strategy-to-calendar-to-campaign workflow |
| `platforms` | WhatsApp, Facebook, Instagram, TikTok, LinkedIn, YouTube, X, podcast and other channel plans |
| `playbooks` | Production, crisis, UGC, viral, community, post-click, chatbot, AI-content and operating playbooks |
| `policies` | AI ethics, copyright, social-media and governance policies |
| `sectors` | Sector-specific marketing guidance |
| `seo-discovery` | Search, GEO and discovery optimisation |
| `strategy` | PESO, owned media, social commerce, personal brand, communities, export, customer value, purpose, eWOM and experiential strategy |
| `training` | Client teams, DIY content, social fundamentals, smartphone video, AI foundations and prompt writing |

Use the most specific skill available. The pipeline skills provide the usual operating spine:

`client brief → platform audit → audience/voice → strategy → channel plan → content pillars → calendar → campaign brief → production → review → publication/reporting → learning`.

## Routing and engine boundaries

This repository is referenced through the canonical engine-routing table. Do not copy skills into client projects or rely on native discovery. Resolve the engine path, read the relevant router and then read only the matched `SKILL.md` files.

### Required companion engines

- **`design-system-skills`**: all typography, layout, visual identity, UI/UX, visual asset, presentation-design and visual anti-slop work. Social strategy and written content remain here; visual production and visual quality gates route there.
- **[Digital Research Engine](https://github.com/peterbamuhigire/digital-research-skills):** current platform, market, legal, regulatory, policy, audience, benchmark and other externally verifiable claims; evidence packs, source verification and uncertainty handling.
- **`chwezi-accounting-doctrine`**: pricing, budgets, ROI, costing, financial statements, controls and finance-system questions.
- **`skills-web-dev`**: websites, applications, APIs, automation, analytics implementation, databases and technical systems.
- **`proposal-skills`**: formal tenders, bids, EOIs, procurement responses and technical/financial proposals.
- **`business-plan-skills`**: feasibility, market sizing, business plans, investor readiness and financial projections.
- **`srs-skills`**: formal requirements, architecture, test, release, governance and standards-driven SDLC documentation.
- **`linux-skills`**: servers, Bash, deployment operations, hardening and infrastructure runbooks.

The current source register is authoritative for platform, legal, policy and market claims. A source that is stale, unavailable or not attributable makes the affected check `not assessed`; it never becomes a pass by assumption.

## Kaizen operating principle

Continuous improvement is mandatory for the engine and every product it produces. Load:

`skills/meta-utility/kaizen-improvement-system/SKILL.md`

The required cycle is:

`Observe → Baseline → Select → Experiment → Check → Standardise → Teach → Re-measure`

Apply the cycle to strategy, content systems, campaigns, calendars, AI workflows, community operations, reports, training assets, policies and client handoffs.

### Engine audit contract

Audit the engine across the applicable dimensions:

- doctrine, routing and skill taxonomy;
- skill depth, inputs, workflow, outputs and evidence;
- East African context, accessibility, readability and inclusion;
- current-source readiness and uncertainty handling;
- creative, legal, rights, privacy and AI safety gates;
- campaign and product measurement;
- handoff, permissions, reproducibility and operational hygiene;
- learning capture, standardisation and re-audit discipline.

Published audit scores are hard-capped:

`published_score = min(raw_score, 65)`

The cap is a reporting ceiling, not permission to ignore deficiencies. Every audit must produce a plan targeting 95/100 with a gap, root cause, exact change, owner, experiment, metric, guardrail, acceptance evidence, rollback/recovery path and re-audit date.

### Product audit contract

The same method applies to any social-media product: strategy, campaign, content calendar, post, article, deck outline, AI workflow, community playbook, report, dashboard specification, training guide or policy.

At minimum, inspect:

1. objective, audience, market and permission boundary;
2. evidence, source dates, assumptions and uncertainty;
3. message, narrative, offer, CTA and audience value;
4. cultural fit, language, accessibility and readability;
5. channel mechanics and conversion path;
6. AI provenance, human review, disclosure, correction and drift controls;
7. rights, privacy, safeguarding, legal/market release and escalation;
8. measurement, baseline, guardrail, decision rule and next experiment;
9. handoff, owner, approval, publication and recovery evidence.

Record whether the product should be `standardise`, `iterate`, `pause`, `reject`, or `not assessed`. Do not publish a claimed result without attributable evidence.

## Content and campaign quality system

Every significant content or campaign workflow uses the following controls:

- **Brief discipline:** define the business outcome, audience, market, message, offer, channel, budget/capacity and approval boundary before production.
- **Audience value:** apply attraction, retention, motivation, conversion, referral and community-trust tests rather than optimising reach alone.
- **Narrative:** use clear conflict, stakes, character/audience perspective, progression, choice and payoff where the format benefits from storytelling. Route visual character, composition and design decisions to `design-system-skills`.
- **Content architecture:** use content pillars, POEM/PESO, RACE, Hero/Hub/Hygiene, ARM and response-system logic; make the content mix and CTA role explicit.
- **Production:** use the content calendar, campaign brief, production playbook and brand-voice controls; maintain a source and approval record.
- **Human quality:** run `anti-ai-slop` continuously and `ai-slop-audit` whenever content is audited, critiqued, scored or de-slopped. A blocking result prevents progression until corrected.
- **Release:** run the creative review gate and, when applicable, the legal/market release gate, AI ethics gate, cultural-bias review, privacy check, accessibility/readability check and measurement-proof review.
- **Learning:** define a baseline, hypothesis, primary outcome, guardrails, test window, decision rule and next action. Record what is standardised, rejected or still uncertain.

The 10-4-1 model, PESO/POEM, RACE, Hero/Hub/Hygiene, Like-Know-Trust, customer-value-journey, direct-response and community-trust frameworks are tools, not substitutes for diagnosis or evidence.

## AI marketing and human control

AI is governed augmentation, never unsupervised authorship or publication. The engine supports AI use-case mapping, readiness, vendor evaluation, brand-voice training, prompt systems, RAG, content recycling, synthetic-persona qualification, chatbots, agentic workflows, predictive analytics, GEO and AI-content policy.

For every AI-assisted product:

- state the problem before choosing AI;
- distinguish the human, system, model, input and output layers;
- minimise data and never place PII, confidential client data or secrets into an unauthorised cloud prompt;
- record the tool, material contribution, human editor and approval owner;
- disclose material AI contribution with specific attribution where required;
- prohibit fabricated testimonials, beneficiary stories, reviews, deepfakes, impersonation, bot engagement and unreviewed regulated-sector advice;
- check cultural bias, language quality, accessibility, copyright and rights;
- provide human correction, escalation, contestability and rollback;
- monitor performance, safety and distribution drift after release;
- route legal, regulatory and current platform claims to Digital Research and qualified specialists.

East African language output, community narratives, public-sector communication, health, finance, donor, political and beneficiary content require appropriately qualified human review. The engine does not certify legal compliance.

## Uganda and East Africa defaults

Unless the brief says otherwise:

| Channel | Default role |
|---|---|
| WhatsApp | Direct customer communication, enquiries, opt-in, follow-up and community conversion |
| Facebook | Broad reach, community and customer service |
| Instagram | Urban and aspirational visual storytelling, generally 18–35 audiences where evidenced |
| TikTok | Short-form entertainment, discovery and creator-led reach |
| YouTube | Searchable tutorials, demonstrations and longer storytelling |
| LinkedIn | B2B, professional, institutional and employer audiences |
| X | Public conversation, journalists, opinion leaders and issue monitoring |
| Google Business Profile | Local discovery, reviews and location intent |

These are starting hypotheses, not guaranteed audience facts or performance benchmarks. Verify current usage, platform rules, access, language and legal requirements before making a material recommendation.

Use British English, UGX and EAT by default. Make assumptions about connectivity, mobile data, payment paths, language, trust, diaspora, urban/rural reach, creator access, moderation capacity and approval timelines visible in the deliverable.

## Book-informed capability upgrades

The current engine improvements were informed by the 16-book study recorded in the Digital Research engine. The books are treated as dated or partial references where appropriate; current platform, legal and market claims still require independent verification.

| Book-derived lesson | Implemented capability in this engine |
|---|---|
| Agile/XP and LEAN | Small experiments, validated learning, evidence-led retrospectives, guardrails, decision rules and standardisation |
| Kaizen and Applying Kaizen in Africa | Participatory, incremental, low-cost improvement; PDCA/QC Story thinking; visible baselines and operational learning |
| Digital Storytelling and Video Game Storytelling | Audience-centred narrative, emotional progression, choices, payoff, character perspective and cross-format story systems |
| Dynamic Characters and Anatomy for Artists | Stronger visual-story briefs, pose/gesture/readability prompts and explicit routing of finished visual design to the design engine; no anatomy claims are inferred from the unreadable extraction |
| Designing for AI | Problem-first AI selection, transparency, human control, correction, disclosure, contestability and drift monitoring |
| Platform Enterprise | Platform-as-product thinking for channel systems, consumer feedback, maintenance ownership, cognitive-load reduction and sustainable operations |
| Tech Lead | Role clarity, transparent communication, ownership transfer, reflection and adjustment, and non-blaming learning culture |
| Nonprofit Strategic Planning | Stakeholder mapping, mission fit, baselines, external scan, resource implications, monitoring and refresh triggers |
| Facility Move Playbook | Continuity, readiness, cutover, escalation, stabilisation and lessons-learned patterns for major campaign or channel change |
| Paid for Your Perspective | Evidence-bounded expert positioning, buyer-fit screening, compliance boundaries, preparation and knowledge-product development |
| AI for Game Developers and MSC Software Magazine | Instrumented systems thinking, model/decision traceability, assumptions, verification, test evidence and production feedback loops |

Implementation provenance and limitations are recorded in:

`docs/continuous-improvement/kaizen-adoption-2026-08.md`

## Evidence, safety and limitations

- This engine creates recommendations and text artefacts; it does not create evidence merely by writing confidently.
- Platform algorithms, prices, audience statistics, laws, regulations, AI products and policies change. Verify them before use.
- Synthetic personas, historical examples, campaign exemplars and benchmark figures must be labelled and must not be presented as client results.
- Legal and regulatory gates are screening and escalation controls, not legal advice or certification.
- Missing account access, source evidence, rights, approvals, measurement data, fluent-language review, rendering capability or qualified specialists produces `not assessed` or a qualified result.
- No campaign should be published, paid spend changed, customer data processed, account altered or external message sent without explicit authority.
- Visual asset production, final layout, typography, interface design and presentation rendering belong to `design-system-skills`.
- This repository's historical `book-extractions/` material is supporting study material, not automatically current evidence.

## Repository layout

```text
social-media-skills/
├── skills/                         # Portable skills by category
├── docs/                           # Standards, plans, source registers and evidence packs
├── scripts/                        # Read-only validation and freshness checks
├── tests/                          # Repository tests
├── book-extractions/               # Supporting book extraction material
├── AGENTS.md                       # Operating and routing instructions
├── CLAUDE.md                       # Dual-compatibility authoring guidance
├── quality-baseline.json           # Zero-debt baseline assertion
└── README.md                       # This capability and operating guide
```

Keep new skills under `skills/<category>/<skill-name>/SKILL.md`. Do not mirror this engine into a project. Keep individual skills execution-focused and move deep frameworks into `references/`.

## Validation and release checks

Run from the repository root in PowerShell:

```powershell
python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json
python -X utf8 scripts\check_source_freshness.py
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 scripts\source_ingestion_guardrail.py
python -X utf8 -m unittest discover -s tests -p "test_*.py"
git diff --check
```

The expected release state is zero contract debt, a passing routing suite, current or explicitly qualified sources, passing tests, and no whitespace errors. Review the continuous-improvement record after significant changes.

## Further reading

- `AGENTS.md` — routing, authoring, evidence, safety and release rules.
- `docs/continuous-improvement/kaizen-adoption-2026-08.md` — engine and product improvement adoption record.
- `docs/continuous-improvement/2026-08-social-books-learning-record.md` — Kaizen learning record for the nine-book social-media synthesis.
- `skills/meta-utility/kaizen-improvement-system/SKILL.md` — mandatory Kaizen workflow.
- `skills/meta-analytics-ops/meta-testing-framework/SKILL.md` — campaign experimentation and decision rules.
- `skills/meta-analytics-ops/meta-reporting/SKILL.md` — reporting and measurement structure.
- `skills/meta-analytics-ops/meta-content-audit/SKILL.md` — content quality and performance audit.
- `skills/ai-marketing/anti-ai-slop/SKILL.md` — mandatory production ship gate.
- `skills/ai-marketing/ai-slop-audit/SKILL.md` — content audit and de-slopping workflow.
- `docs/source-registers/` — dated evidence for current claims.
- `docs/evidence-packs/measurement-proof-pack.md` — metric definitions, reconciliation and proof standards.
- `docs/quality-gates/` — creative and legal/market release gates.

## Out of scope

- finished graphic design, illustration, animation or video editing;
- web, mobile, desktop or backend implementation;
- autonomous publishing, ad spend, account mutation or customer-data processing;
- legal advice, regulatory certification or financial assurance;
- unsupported claims about current platforms, markets, laws, benchmarks or client performance.
