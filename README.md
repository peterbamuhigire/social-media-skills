# Social Media Skills Engine

The Social Media Skills Engine (repository `social-media-skills`) is the Chwezi digital marketing and advertising engine: a library of 117 routed skills for consultancy work in Uganda and East Africa. It covers marketing foundations and positioning, channel selection, advertising strategy and budgeting, media planning, creative briefs, ad copy, paid search and paid social build specifications, content and copywriting in British, East African English, French and Kiswahili, campaign and community operations, measurement, attribution and reporting, AI-assisted marketing, agency business development and client training. Its produced outputs include client briefs and personas, social-media, digital-marketing and campaign strategies, media plans with reach and frequency calculations, advertising budgets and decision memos, creative briefs, ad copy sets, Google Ads and Meta/TikTok/LinkedIn campaign specifications, content calendars, publication-ready copy, audits, dashboards and monthly reports, ROI business cases, operating playbooks, organisational policies, proposals and training workbooks.

The engine works to named standards rather than house opinion. Personal-data and direct-marketing work is checked against the Uganda Data Protection and Privacy Act 2019 and its 2021 Regulations, with the Kenyan, Rwandan and Tanzanian data-protection laws held in a dated source register (`docs/source-registers/source-register.json`, 63 records under a freshness gate); advertising claims against the Uganda Communications Commission Advertising Standards 2019 and the ICC Advertising and Marketing Communications Code; influencer disclosure against the FTC Endorsement Guides and ASA/CAP guidance; platform mechanics against the Meta, WhatsApp, TikTok, LinkedIn and Google policy pages in the same register; and web accessibility against WCAG 2.2. Method draws on named practitioner texts, among them Chaffey's RACE, Bodnar and Cohen's social ROI formula, Weinberg and Mares's Bullseye and Kotler's segmentation and positioning (full list under References). Every deliverable passes an anti-slop and human-review gate. The engine is for agency owners, account leads, strategists, media planners, copywriters, paid-media specialists, in-house marketing teams and founders who need reviewable, evidence-backed marketing decisions. It plans, specifies, writes, audits and reports; spending money, changing live ad accounts, publishing and contacting people always require explicit client authority.

## Installation

Prerequisites: Claude Code for the plugin route; Node.js 18 or later for the installer scripts; Python 3.11 or later (CI uses 3.12) with `PyYAML` for the validators and tests; Git for cloning.

### Claude Code plugin

The repository ships a Claude Code marketplace (`.claude-plugin/marketplace.json`, marketplace `chwezi-social`) containing one plugin, `social`:

```text
/plugin marketplace add https://github.com/peterbamuhigire/social-media-skills
/plugin install social@chwezi-social
```

### Installer scripts

`install.sh` and `install.ps1` both delegate to `scripts/install-engine.js`, which copies `skills/` and `hooks/` into a Claude root and records what it wrote in `.chwezi/install-state.json`, so uninstall removes only its own files. `--scope user` (the default) targets `~/.claude`; `--scope project` targets `.claude` in the current directory. `--dry-run` prints the plan without writing.

```sh
git clone https://github.com/peterbamuhigire/social-media-skills
cd social-media-skills
./install.sh --scope project --dry-run   # macOS, Linux or Git Bash; drop --dry-run to install
.\install.ps1 --scope user               # Windows PowerShell
node scripts/install-engine.js doctor --scope user
node scripts/install-engine.js uninstall --engine social-media-skills --scope user
```

### Codex

Codex reads the standard layout directly: clone the repository and point Codex at [`AGENTS.md`](AGENTS.md), which routes to `skills/<category>/<skill-name>/SKILL.md`. The Codex-only model-policy check is described in [`.codex/README.md`](.codex/README.md):

```text
python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check
```

Claude skips that step.

### Manual use

Clone the repository, read [`CLAUDE.md`](CLAUDE.md) (which imports [`AGENTS.md`](AGENTS.md)) as the router, then open the matching `SKILL.md` and its `references/`. Before release, run:

```powershell
python -m pip install PyYAML
python -X utf8 scripts\validate_skill_engine.py --baseline quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py
python -X utf8 scripts\check_source_freshness.py
python -X utf8 -m unittest discover -s tests -p "test_*.py"
```

## Capabilities

117 active `SKILL.md` files across 15 category folders under `skills/` (a sixteenth, `frameworks/`, holds only inactive aliases since S06). The former category-level standards file `skills/content-writing/SKILL.md` is now an inactive alias; its standards live in `premium-commercial-writing`. Skills retired by the 2026-09-29 consolidation stay on disk as inactive `ALIAS.md` files; [docs/skill-aliases.yml](docs/skill-aliases.yml) routes each one to the active skill that now holds its content.

| Category | Skills |
|---|---:|
| `advertising` | 9 |
| `ai-marketing` | 6 |
| `business-development` | 10 |
| `content-writing` | 7 |
| `frameworks` | 0 (inactive aliases only) |
| `language` | 4 |
| `meta-analytics-ops` | 13 |
| `meta-utility` | 3 |
| `pipeline` | 13 |
| `platforms` | 8 |
| `playbooks` | 18 |
| `policies` | 1 |
| `sectors` | 2 |
| `seo-discovery` | 2 |
| `strategy` | 15 |
| `training` | 6 |
| **Total** | **117** |

| Category | Skill | What it does |
|---|---|---|
| `advertising` | `ad-copy-and-hook-lab` | Writes and tests ad headlines, hooks, offers, proof lines and guarantees across media. |
| `advertising` | `ad-testing-and-scaling` | Designs ad tests, reads results and decides what to scale, kill or refresh. |
| `advertising` | `ad-to-site-journey-handoff` | Hands campaign traffic to a landing page with message match, UTMs, events and consent. |
| `advertising` | `advertising-attribution-and-measurement` | Defines conversion events, attribution models, incrementality tests and break-even ROAS/CPA. |
| `advertising` | `advertising-strategy-and-budget` | Sets advertising objectives, measurement levels, triangulated budgets and governance terms. |
| `advertising` | `creative-brief-and-big-idea` | Writes the strategic creative brief, finds the insight and screens campaign ideas. |
| `advertising` | `direct-response-economics` | Builds pro-forma P&L, break-even and roll-out ladders for response campaigns. |
| `advertising` | `media-planning` | Builds and reviews media plans: reach, frequency, GRPs, CPM, flighting and post-buy. |
| `advertising` | `paid-search-advertising` | Plans, specifies and audits Google Ads Search, Performance Max and Demand Gen. |
| `ai-marketing` | `ai-generative-search-optimisation` | Plans brand visibility in AI and generative search answers. |
| `ai-marketing` | `ai-readiness-diagnostic` | Produces a scored AI readiness diagnostic for a marketing team. |
| `ai-marketing` | `ai-slop-audit` | Audits content for generic AI patterns and sets remediation. |
| `ai-marketing` | `ai-use-case-mapping` | Maps and prioritises AI use cases across the marketing workflow. |
| `ai-marketing` | `anti-ai-slop` | Applies the engine's anti-slop writing rules to any deliverable. |
| `ai-marketing` | `brand-voice-ai-training` | Encodes a brand voice into AI instructions, examples and checks. |
| `business-development` | `biz-dev-beyond-agency-offer` | Designs a low-risk first engagement offer for new agency clients. |
| `business-development` | `biz-dev-case-study` | Writes evidence-backed client case studies with permissions. |
| `business-development` | `biz-dev-credentials` | Assembles an agency credentials pack from verifiable proof. |
| `business-development` | `biz-dev-lawful-prospecting-outreach` | Builds lawful B2B prospecting: lists, consent, sequences and speed-to-lead. |
| `business-development` | `biz-dev-positioning` | Defines agency niche, positioning and differentiation. |
| `business-development` | `biz-dev-practitioner-positioning` | Positions an individual practitioner with a proof architecture. |
| `business-development` | `biz-dev-pricing-menu` | Builds a priced services menu with scope and packages. |
| `business-development` | `biz-dev-proposal` | Drafts client proposals and statements of work. |
| `business-development` | `biz-dev-video-outreach` | Plans personalised video audit outreach to prospects. |
| `business-development` | `eac-call-for-applications-campaign` | Donor-compliant call-for-applications campaigns across the East African Community. |
| `content-writing` | `blog-writer` | Writes publication-ready blog posts to the engine's standards. |
| `content-writing` | `caption-writer` | Writes platform-fit social captions with calls to action. |
| `content-writing` | `content-ideas` | Produces a prioritised set of content ideas by pillar and format. |
| `content-writing` | `direct-response-funnel-copy` | Writes direct-response funnel copy: offers, pages and follow-up. |
| `content-writing` | `email-copywriter` | Writes marketing emails and sequences. |
| `content-writing` | `premium-commercial-writing` | Writes high-value commercial copy for premium offers and audiences. |
| `content-writing` | `prompt-engineering-library` | Maintains a reusable, tested marketing prompt library. |
| `language` | `east-african-english` | Sets East African English conventions for local audiences. |
| `language` | `french-native-copy` | Writes native French social copy for francophone markets. |
| `language` | `language-standards` | Sets the engine-wide British English and language rules. |
| `language` | `swahili-native-copy` | Writes native Kiswahili social copy. |
| `meta-analytics-ops` | `measurement-tracking-plan` | Writes the privacy-safe tracking plan: events, UTM convention, Consent Mode v2, Conversions API, enhanced conversions and BigQuery export. |
| `meta-analytics-ops` | `meta-algorithm-guide` | Builds a platform-ranking reference from current evidence. |
| `meta-analytics-ops` | `meta-budget-planner` | Allocates a confirmed budget across channels, production, tools and contingency. |
| `meta-analytics-ops` | `meta-competitor-analysis` | Compares named competitors to find positioning and content gaps. |
| `meta-analytics-ops` | `meta-content-audit` | Reviews content history to decide what to keep, stop, test or improve. |
| `meta-analytics-ops` | `meta-content-repurposing` | Turns a proven asset into channel-appropriate derivatives. |
| `meta-analytics-ops` | `meta-reporting` | Produces monthly written performance reports from verified data. |
| `meta-analytics-ops` | `meta-roi-framework` | Calculates campaign or channel return from attributable value and cost. |
| `meta-analytics-ops` | `meta-sales-marketing-alignment` | Defines shared lifecycle stages, ownership and handover rules. |
| `meta-analytics-ops` | `meta-social-listening` | Sets up listening queries, evidence logs, cadence and escalation. |
| `meta-analytics-ops` | `meta-social-metrics-framework` | Selects business, funnel and operational metrics with owners. |
| `meta-analytics-ops` | `meta-testing-framework` | Designs controlled marketing experiments with decision rules. |
| `meta-analytics-ops` | `meta-tools-stack-evaluation` | Evaluates the marketing technology stack for fit and total cost. |
| `meta-utility` | `kaizen-improvement-system` | Audits and improves the engine or any deliverable it produces. |
| `meta-utility` | `skill-safety-audit` | Reviews skills for unsafe instructions before adoption or release. |
| `meta-utility` | `skill-writing` | Creates or upgrades skills under the canonical skill-writing standard. |
| `pipeline` | `01-client-brief` | Turns discovery answers into the full brief and one-page client card. |
| `pipeline` | `02-platform-audit` | Audits active social profiles and named competitors. |
| `pipeline` | `03-audience-personas` | Develops research-grounded audience personas. |
| `pipeline` | `04-brand-voice-intake` | Defines verbal and visual brand direction. |
| `pipeline` | `05-social-media-strategy` | Produces the master social-media strategy. |
| `pipeline` | `06-digital-marketing-strategy` | Integrates social, email, search, web, influencer and paid into one plan. |
| `pipeline` | `07-email-marketing-strategy` | Designs a permission-based email programme and lifecycle. |
| `pipeline` | `08-influencer-marketing-strategy` | Plans creator programmes with fit, due diligence, rights and measures. |
| `pipeline` | `09-campaign-strategy` | Plans one focused launch, offer, awareness or event campaign. |
| `pipeline` | `10-content-pillars` | Defines three to five audience-linked content pillars. |
| `pipeline` | `11-content-calendar` | Schedules approved pillars and campaigns over 90 days. |
| `pipeline` | `12-website-content-plan` | Plans 90 days of website and blog content (not the build). |
| `pipeline` | `13-campaign-brief` | Turns an approved campaign strategy into an executable brief. |
| `platforms` | `platform-facebook` | Facebook channel plan: setup, content, community and measurement. |
| `platforms` | `platform-google-business-profile` | Google Business Profile plan: setup, posts, reviews and measurement. |
| `platforms` | `platform-instagram` | Instagram channel plan: setup, content, community and measurement. |
| `platforms` | `platform-linkedin` | LinkedIn channel plan for personal and professional presence. |
| `platforms` | `platform-tiktok` | TikTok channel plan: setup, content, community and measurement. |
| `platforms` | `platform-whatsapp` | WhatsApp channel plan: setup, broadcasts, community and measurement. |
| `platforms` | `platform-x-twitter` | X (Twitter) channel plan: setup, content and measurement. |
| `platforms` | `platform-youtube` | YouTube channel plan: setup, content, community and measurement. |
| `playbooks` | `playbook-agency-operations` | Agency operations playbook: roles, workflow, controls and measures. |
| `playbooks` | `playbook-chatbot-strategy` | Chatbot strategy playbook: scope, flows, handover and measures. |
| `playbooks` | `playbook-client-retainer-management` | Playbook for running and renewing client retainers. |
| `playbooks` | `playbook-community-management` | Community management playbook: moderation, response and escalation. |
| `playbooks` | `playbook-content-production` | Content production playbook from brief to approved asset. |
| `playbooks` | `playbook-crisis-communications` | Crisis communications playbook: triage, holding lines and escalation. |
| `playbooks` | `playbook-daily-operations-routine` | Daily social-media operations routine and checklists. |
| `playbooks` | `playbook-marketing-automation` | Marketing automation playbook: triggers, flows and controls. |
| `playbooks` | `playbook-networking` | Professional networking playbook for relationship-led growth. |
| `playbooks` | `playbook-paid-social-advertising` | Paid social on Meta, TikTok and LinkedIn: audiences, budgets, tracking and optimisation. |
| `playbooks` | `playbook-post-click-strategy` | Post-click playbook: landing experience, follow-up and conversion. |
| `playbooks` | `playbook-pr-publicity` | Publicity playbook: angles, pitching and coverage tracking. |
| `playbooks` | `playbook-reputation-management` | Reputation management playbook: monitoring, response and recovery. |
| `playbooks` | `playbook-sms-whatsapp-marketing` | SMS and WhatsApp marketing playbook with opt-in controls. |
| `playbooks` | `playbook-social-media-policy` | Playbook for drafting an organisational social media policy. |
| `playbooks` | `playbook-social-selling` | Social selling playbook for relationship-led sales. |
| `playbooks` | `playbook-viral-content-design` | Playbook for designing shareable content with evidence limits. |
| `playbooks` | `playbook-white-label-partnerships` | White-label partnership playbook for agencies. |
| `policies` | `policy-ai-content-ethics` | Drafts or reviews an organisational AI content ethics policy. |
| `sectors` | `healthcare` | Healthcare marketing: patient-safe content, trust and misinformation response. |
| `sectors` | `hospitality-hotel-restaurant` | Hospitality marketing for hotels, lodges, restaurants, venues and catering. |
| `seo-discovery` | `demand-forecasting` | Demand forecasts, stockout timing and reorder decisions from operational data. |
| `seo-discovery` | `seo-geo-optimisation` | Page-level SEO and generative-search citation readiness. |
| `strategy` | `ecommerce-brand-differentiation` | E-commerce positioning, naming, packaging logic and proof. |
| `strategy` | `ecommerce-export-marketing-advisory` | Export-market selection, cross-border trust and CAC-bounded campaigns. |
| `strategy` | `marketing-foundations-stp-positioning` | Segmentation, targeting, positioning, marketing mix and value proposition. |
| `strategy` | `peso-integrated-strategy` | Coordinates paid, earned, shared and owned channels. |
| `strategy` | `social-commerce-strategy` | Catalogue, WhatsApp ordering, Mobile Money and fulfilment content. |
| `strategy` | `strategy-b2b-customer-community` | Retention-first B2B account grading, contact plans and at-risk alerts. |
| `strategy` | `strategy-channel-architecture` | Platform roles, audience flows, hub-and-spoke routing and effort. |
| `strategy` | `strategy-creator-monetisation` | Creator revenue options, rate cards, partnerships and products. |
| `strategy` | `strategy-csr-purpose-communications` | CSR, community-impact and purpose communication. |
| `strategy` | `strategy-customer-value-journey` | Full-funnel content from awareness to advocacy. |
| `strategy` | `strategy-ewom-reviews` | Review generation, referrals and electronic word of mouth. |
| `strategy` | `strategy-experiential-marketing` | Live and hybrid experiences: launches, activations and pop-ups. |
| `strategy` | `strategy-personal-brand` | Individual positioning, authority, content and monetisation. |
| `strategy` | `strategy-video-content` | Cross-platform organic video formats, hooks, series and scripts. |
| `strategy` | `traction-channel-bullseye` | Chooses acquisition channels to test and fund from nineteen traction channels. |
| `training` | `training-ai-foundations` | Beginner AI literacy training for marketing teams. |
| `training` | `training-ai-prompt-writing` | Practical prompt-writing training with exercises. |
| `training` | `training-client-team` | Two-hour social-media handover workshop and workbook. |
| `training` | `training-diy-content` | Self-contained client handbook for creating and publishing content. |
| `training` | `training-smartphone-video-production` | Hands-on smartphone video shooting, sound, light and editing. |
| `training` | `training-social-media-fundamentals` | Beginner social-media concepts, safety and measurement. |

## Approval boundaries

- Research, planning, drafting, auditing and reporting run without special permission.
- Ad spend, live ad-account or platform changes, publishing, messaging and outreach to real people, and personal-data processing need explicit client authority; without it the engine returns a draft marked for approval.
- Changing legal, platform or market claims must cite a current record in `docs/source-registers/source-register.json`; a stale or unavailable source makes the check `not assessed`.
- Visual execution routes to the design engine (`design-system-skills`); website builds route to `website-skills`.

## References

Sources cited in this repository's skills, references, doctrine, continuous-improvement records, gap analyses and source registers. Citations only; no book content is stored in the repository. Where the repository gives inconsistent author initials or years, only the consistent part is shown. Sources cited solely inside client deliverables under `projects/` are excluded.

### Books

- Abrams, R. *The Successful Business Plan*
- Agius and Clancey. *Faster, Smarter, Louder*
- Albarran, A. B. *The Social Media Industries*
- Almasi, O., Fallon, M. D. et al. *Swahili Grammar for Introductory and Intermediate Levels (Sarufi ya Kiswahili)*
- Anderson, D. (2022) *AI in Digital Marketing Training Guide*, self-published
- Anderson, D. (2022) *Instagram Follower Magnet*
- Ariely, D. *Predictably Irrational*
- Baer, J. and Lemin, D. (2018) *Talk Triggers*
- Berger, J. (2013) *Contagious: Why Things Catch On*
- Bhatia, A. *Strategic Social Media Marketing*
- Bhatia, P. S. *Social Media and Mobile Marketing*
- Binet, L. and Field, P. *The Long and the Short of It*
- Bishop, W. and Starkey, D. (2006) *Keywords in Creative Writing*, Utah State University Press
- Blauer, I. and Woolley, A. (2021) *Keywords for SEO: Actionable Knowledge Bombs to Help you Rank on Google in 2021*
- Blount, J. (2015) *Fanatical Prospecting*, Wiley
- Bly, R. W. (2018) *The Digital Marketing Handbook: A Step-by-Step Guide to Creating Websites That Sell*, AWAI
- Bly, R. W. *How to Write and Sell Simple Information*
- Bodnar, K. and Cohen, J. L. (2012) *The B2B Social Media Book*, Wiley
- Boulares and Frérot. *Grammaire progressive du français — Niveau avancé*, CLE
- Boustany, S. (2024) *Generative AI for Social Media Marketing*
- Branson, S. (2020) *UX/UI Design: Introduction Guide to Intuitive Design and User-Friendly Experience*
- Brown, R. (2016) *Build Your Reputation*, Capstone/Wiley
- Brunson, R. (2013) *DotComSecrets Ignite*, SuccessEtc
- Butow, E. *Ultimate Guide to Social Media Marketing*
- Butow, E. and Walker, C. (2025) *Instagram for Business for Dummies*, 3rd edn
- Carter, C. (2026) *The New Rules of AI Search*, Wiley
- Chaffey, D. and Ellis-Chadwick, F. (2024) *Digital Marketing: Strategy, Implementation and Practice*, 8th edn, Pearson
- Chavaux, P. J. (2025) *The Big AI ChatGPT Book of 2000 Prompts*
- Ching and Mothi (2025) *AI for Creatives: Unlocking Expressive Digital Potential*, CRC Press
- Cialdini, R. *Influence*
- Cooper, M. D. (2019) *Help! My Facebook Ads Suck!*, 2nd edn
- Crawford, T. *Going Social*
- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics*, O'Reilly
- Dallas, M. (2022) *Social Media Marketing Algorithms*
- Deacon, P. B. (2020) *UX and UI Design Strategy: A Step-by-Step Guide*
- Debelak, D. (2006) *Perfect Phrases for Business Proposals and Business Plans*, McGraw-Hill
- Deiss, R. and DigitalMarketer (2023) *The Customer Value Journey*
- Dib, A. *The 1-Page Marketing Plan*
- Dietrich, G. (2020) *Spin Sucks: PR in the Digital Age*
- Dodaro, M. (2019) *LinkedIn Unlocked*, Entrepreneur Press
- Donovan, S. (2019) *5,000 Writing Prompts: A Master List of Creative Exercises*
- Duguin, S. *Cybersecurity for NGOs: Attack Prevention and Threat Response*
- Dunford, A. *Obviously Awesome*
- Edwards, P., Edwards, S. and Douglas, L. C. (1991) *Getting Business to Come to You*
- Enns, B. *The Win Without Pitching Manifesto*
- Erné (2024) *AI-Powered Marketing*
- Erné (2024) *The Artificial Intelligence Handbook for Management Consultants*
- Evelyn, L. (2025) *Making ChatGPT Work for You*, Apress
- Fabian, J. *Language and Colonial Power*
- Falls (2021) *Winfluence*
- Farri and Rosani (2025) *HBR Guide to Generative AI for Managers*, HBR Press
- Farri and Rosani (2025) *Multi-Agent Systems for Marketing*
- Farris, P. W., Bendle, N. T., Pfeifer, P. E. and Reibstein, D. J. *Marketing Metrics*
- Fekeshazi, Z. (c. 2017) *Product Managers' Guide to UX Design*, UX Studio
- Field, C. *Social Media Jobs That Pay Well*
- Fihn, F. (2025) *Beyond the Agency Box: The Phoneless Meet*
- Fitzpatrick, L. *Navigating the Digital Shift*
- Funk, T. (2011) *Social Media Playbook for Business*
- Funk, T. (2013) *Advanced Social Media Marketing*
- Garner, R. (2012) *Search and Social: The Definitive Guide to Real-Time Content Marketing*, Wiley/Sybex
- Gladwell, M. (2000) *The Tipping Point*
- Godin, S. *This Is Marketing*
- GPT Penguin (2024) *ChatGPT Prompts Library*, self-published
- Graves. *Writing for Profit*
- Gujral, R. *The AI Instinct*
- Hahn, F. E. with Davis, Killian and Magill (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn
- Handley, A. *Everybody Writes*
- Handley, A. and Chapman, C. (2012) *Content Rules*, Wiley
- Hanlon, A. and Tuten, T. L. (eds) (2022) *The SAGE Handbook of Social Media Marketing*, SAGE
- Hargis, Carey et al. *Developing Quality Technical Information*
- Harris, A. (2016) *Small Business Big Money Online*
- Hatton, A. (2007) *The Definitive Business Pitch*
- Heath, C. and Heath, D. *Made to Stick*
- Helmer, H. *7 Powers*
- Heminway, A. *Practice Makes Perfect — Complete French Grammar*, McGraw-Hill
- Hennessy, B. (2018) *Influencer*, Citadel Press
- Hietaniemi, J. (2020) *Secret Strategies for Instagram Growth*
- Hoffmann, C. R. and Bublitz, W. (eds) *Pragmatics of Social Media*
- Hofstede, G., Hofstede, G. J. and Minkov, M. *Cultures and Organisations: Software of the Mind*
- Hunter, V. L. with Tietyen, D. (1997) *Business-to-Business Marketing: Creating a Community of Customers*, NTC Business Books
- Huyen, C. *AI Engineering*
- Iny, D. et al. *Blog Post Ideas*
- Jarvis, P. *Company of One*
- Johnsen, M. (2024) *AI in Digital Marketing*, Mercury Learning and Information
- Johnsen, R. (2024) *AI Ethics in Practice*
- Johnson, J. (2023) *How to Become a Social Media Manager*
- Joseph, A. (c. 2023–24) *The Art of ChatGPT Prompt Engineering: A Guide for Digital Marketers, Series 1*, self-published
- Kahan (2022) *High-Velocity Digital Marketing*, Apress
- Kahneman, D. *Thinking, Fast and Slow*
- Kaushik, A. *Web Analytics 2.0*
- Kelley, L. D. and Sheehan, K. B. (c. 2021–22) *Advertising Management in a Digital Environment: Text and Cases*, Routledge
- Kennedy, D. *Magnetic Marketing*
- Kennedy, D. (2004) *No B.S. Sales Success*, Entrepreneur Press
- Kennedy, D. S. (2000) *The Ultimate Sales Letter*, 2nd edn, Adams Media
- Kennedy, D. S. and Marrs, J. (2011) *No B.S. Price Strategy*, Entrepreneur Press
- Kim, W. C. and Mauborgne, R. (2015) *Blue Ocean Strategy*
- Knight, S. *Social Media Strategy: A Practical Guide to Social Media Marketing and Customer Engagement*
- Kotler, P. et al. (2023) *Marketing Management*, Pearson
- Kumar, V. and Reinartz, W. *Customer Relationship Management*
- Kupsh and Graves. *High-Impact Presentations*
- Lafley, A. G. and Martin, R. L. *Playing to Win*
- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn
- Landa, R. (2022) *Strategic Creativity: A Business Field Guide to Advertising, Branding, and Design*, Routledge
- Larsson, T. (2016) *Ecommerce Evolved*
- Lecinski, J. *Winning the Zero Moment of Truth*
- LetsEnhance (2024) *How to Write AI Image Prompts — From Basic to Pro*
- Levy, J. (2015) *UX Strategy: How to Devise Innovative Digital Products that People Want*, O'Reilly
- Lima. *Fundamentals of Writing*
- Lines, C. J. *The Great Digital Commission*
- Ltifi, M. (ed.) *Advances in Digital Marketing in the Era of Artificial Intelligence*, CRC Press
- Ltifi, M. (2025) *Artificial Intelligence and Social Media Marketing*
- Luttrell, R. *Social Media: How to Engage, Share, and Connect*
- Macarthy, A. *500 Social Media Marketing Tips*
- Maister et al. *The Trusted Advisor*
- Malaquias, M. R. *Authentic East African Swahili Cuisine*
- Maltz, M. et al. (1998) *Zero-Resistance Selling*, Prentice Hall Press
- Marcos, J. et al. (c. 2025) *The High-Performing Key Account Manager*, Kogan Page
- Marten, L. and McGrath, D. L. *Colloquial Swahili*
- Maxwell. *7 Steps to Better Writing*
- McDermott, A. (2023) *Efficient Content Creation*, The Recognized Authority
- McDonald, J. *Social Media Marketing Workbook*
- Meerman Scott, D. (2022) *The New Rules of Marketing and PR*, 8th edn, Wiley
- Mendelson, N. *The Social Media Business Equation*
- Meyer, E. *The Culture Map*
- Miller, D. *Building a StoryBrand 2.0*
- Mizrahi, G. (2024) *Unlocking the Secrets of Prompt Engineering*, Packt
- Mohan, S. *Designing the AI-Driven Data Foundations*
- Mollick, E. *Co-Intelligence*
- Mugane, J. M. *The Story of Swahili*
- Nayebi (2025) *AI-First Marketing*
- Nayebi (2025) *Foundations of Agentic AI for Retail*
- Nayebi (2025) *Generative AI for Product and Marketing Teams*
- Nayebi (2025) *Human-in-the-Loop AI*
- Nelson, J. (2019) *The Seven Figure Agency Roadmap*, Seven Figure Agency LLC
- Nemo, J. (2017) *Content Marketing Made Easy*, self-published
- Nurse, D. and Spear, T. *The Swahili*
- Parsons, P. J. (2009) *Beyond Persuasion: The Healthcare Manager's Guide to Strategic Communication*
- Phillips, J. (2015) *Ecommerce Analytics*
- Pidsley (2023) *Digital Marketing in 2023: A Quickstart Guide*, self-published
- Pidsley (2023) *Social Media Marketing for Business: Scaling an Integrated Social Media Strategy Across Your Organisation*
- Pinskey, R. (1997) *101 Ways to Promote Yourself*
- Poisson-Quinton, S. *French Grammar in 44 Lessons*
- Pollard, M. *Strategy Is Your Words*
- Port, M. *Book Yourself Solid*
- Raaz, S. A. (c. 2023) *Web Analytics Blueprint*
- Rageh, A. (ed.) (2026) *Ethical Marketing and Consumer Trust in Digital and Sustainable Markets*
- Randazzo, G. W. (2024) *Winning Marketing Strategies Using Generative AI*, Business Expert Press
- Raymond, M. J. and Johnston, L. (2021) *Business Gold: Build Awareness, Authority, and Advantage with LinkedIn Company Pages*
- Reeves, R. (1961) *Reality in Advertising*
- Revella, A. *Buyer Personas*
- Ries, A. and Trout, J. (2001) *Positioning: The Battle for Your Mind*
- Roche, M. *Business English Speaking: Advanced Masterclass*, IDM Business and Law
- Roche, M. *Business English Vocabulary: Advanced Masterclass*, IDM Business and Law
- Rogers, D. L. (2011) *The Network Is Your Customer*
- Roth, H. and neuroflash Team (2024) *AI Strategy 2025 for Marketing Teams*, neuroflash
- Rubinelli, S. *Institutional Health Communication in the Information Age*
- Rumelt, R. *Good Strategy/Bad Strategy*
- Russell, J. *Swahili (Teach Yourself)*
- Sadr, A. *Designing for AI* (early release)
- Sant, T. (2012) *Persuasive Business Proposals*, 3rd edn
- Schaefer, M. *Belonging to the Brand*
- Schaefer, M. W. (2025) *Audacious: How Humans Win in an AI Marketing World*, Schaefer Marketing
- Schaffer, N. (2013) *Maximize Your Social*
- Serling, B. (ed.) (2002) *How to Write Million Dollar Ads, Sales Letters & Web Marketing Pieces*, The Internet Marketing Center
- Seymour, R. *The Twittering Machine*
- Shanks, J. (2016) *Social Selling Mastery*, Wiley
- Sharp, B. *How Brands Grow*
- Sobia Publication (2022) *Powerful Social Media Marketing for Beginners*
- Stockwell, J. and Shaw, H. M. (1994) *Direct Marketing Checklists*, NTC Business Books
- Stukus, D. R., Patrick, M. D. and Nuss, K. E. (2019) *Social Media for Medical Professionals*
- Stutts, P. (2021) *The Undefeated Marketing System*, Scribe
- Sweenor and Mulkers (2024) *AI-Powered Business Intelligence*
- Sweenor and Mulkers (2024) *Generative AI Business Applications*
- Thaler, R. and Sunstein, C. *Nudge*
- Treacy and Wiersema. *The Discipline of Market Leaders*
- Upadhyay (2024) *Generative AI for Marketing*, Packt
- Usunier, J.-C. and Lee, J. A. *Marketing Across Cultures*
- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn, Stanford Business Books
- Verma, N. (2019) *Checkout*
- Walker, J. *Launch*
- Wallas, G. (1926) *The Art of Thought*
- Walsh Phillips, K. (2023) *Ultimate Guide to Instagram for Business*, 2nd edn
- Warrillow, J. *Built to Sell*
- Weinberg, G. and Mares, J. (2014) *Traction*, S-curves Publishing
- Westergaard, N. (2016) *Get Scrappy*, AMACOM
- Wheelen, T. L. and Hunger, J. D. *Strategic Management and Business Policy*
- Wiebe, J. (2011) *Copy Hackers: 6 Persuasion Strategies*, Copy Hackers
- Wiebe, J. *Buttons*
- Wiebe, J. *Headlines, Subheads & Value Propositions*
- Wiebe, J. *Where Stellar Messages Come From*
- Wilson, P. M. *Simplified Swahili*
- Wind, J. and Mahajan, V. (2001) *Digital Marketing: Global Strategies from the World's Leading Experts*, Wiley
- Wright, A. (2025) *ChatGPT AI Business Prompts*
- Young, J. W. (1940) *A Technique for Producing Ideas*
- Zafarani, R., Abbasi, M. A. and Liu, H. *Social Media Mining: An Introduction*
- Zahay, D. et al. (2024) *Digital Marketing Management: A Handbook for the Current (or Future) CEO*, 2nd edn
- Zahay, D., Labrecque, L., Reavey, B. and Roberts, M. L. (2024) *Digital Marketing: Foundations and Strategy*, 5th edn, Cengage

Cited by title only: *The Adweek Copywriting Handbook*; *Applying the Kaizen in Africa* (2018); *The Bezos Letters*; *Buyology*; *The Chicago Manual of Style*, 17th edn; *Digital Storytelling*; *Dynamic Characters*; *LEAN: Ultimate Collection*; *Paid for Your Perspective*; *Video Game Storytelling*; *Yes!*

Language references cited by publisher: *2000 French Phrases* and *50 Most Used French Verbs* (French Hacking); *Conversational French Dialogues* (Touri Language Learning); *French–English Bilingual Visual Dictionary* (DK); *Learn French II — Parallel Text* (Polyglot Planet); *Read & Think French, Premium* (Think French); *Rough Guide Phrasebook — Swahili* (Lexus); *Swahili (Spoken World)* (Living Language); *Trilingual Story Book* (Aames).

### Repositories

- **Impeccable** — https://github.com/pbakaus/impeccable — Apache-2.0 — AS1–AS7 anti-slop overlay in `anti-ai-slop` and `ai-slop-audit` (3 September 2026). One of the ten repositories studied in the my-10-kaizen operation; recorded as an evidence source, not a dependency.
- **obra/superpowers** — https://github.com/obra/superpowers — MIT — rule SP-14 (a description must not narrate the workflow), paraphrased into the canonical `quick_validate.py` mirrored into `skills/meta-utility/skill-writing/` (29 September 2026; my-10-kaizen).
- **addyosmani/agent-skills** — https://github.com/addyosmani/agent-skills — MIT — four Tier-1 lint rules (sections, use-when, host YAML, narration) adapted from `scripts/lib/skill-lint.js` at commit `2686b62`, paraphrased into the same mirrored `quick_validate.py` (29 September 2026; my-10-kaizen).
- **ECC** — https://github.com/affaan-m/ECC — licence not stated in this repository — Tier-1 standalone installer model, the MSYS path fix in `install.sh`, symlink resolution in `install.ps1`, plugin-manifest schema notes, the brand-voice source-priority order and "what the author never does" check in `brand-voice-ai-training`, and the no-identical-crosspost rule.
- **donvito/codex-astra-luna-orchestrator** — https://github.com/donvito/codex-astra-luna-orchestrator — licence not stated in this repository — concept reference for the `.codex` model policy, inspected at commit `21f4561656a1b8f2813828520357e3cd1785d50f`; implemented independently and its installer never run.

### Standards and official sources

East African law, regulators and statistics:

- Uganda Data Protection and Privacy Act 2019, including s.26 direct-marketing opt-out — https://ulii.org/en/akn/ug/act/2019/9/eng%402019-05-03
- Uganda Data Protection and Privacy Regulations 2021 — https://ulii.org/en/akn/ug/act/si/2021/21/eng%402021-03-12
- Personal Data Protection Office Uganda, guidance for organisations — https://pdpo.go.ug/information-center/organisation
- Uganda Communications Commission, Uganda Advertising Standards 2019 — https://www.ucc.co.ug/download/the-advertising-standards/
- Uganda Copyright and Neighbouring Rights (Amendment) Act 2026 — https://ulii.org/en/akn/ug/act/2026/8/eng%402026-05-22
- Uganda consumer, competition and electronic-marketing rules relevant to influencers — https://ulii.org/
- Uganda Computer Misuse Act 2011
- Kenya Data Protection Act 2019 and ODPC guidance notes — https://www.odpc.go.ke/
- Kenya Data Protection (General) Regulations 2021 — https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf
- Kenya Consumer Protection Act 2012 s.12, Competition Act 2010, ASBK Code and Media Council Code 2025 — https://new.kenyalaw.org/
- Communications Authority of Kenya influencer licensing and BCLB gambling-advertising rules — https://www.ca.go.ke/
- Rwanda Law No. 058/2021 on the protection of personal data and privacy — https://dpo.gov.rw/dpp-law/general-provisions
- Rwanda influencer and advertising disclosure rules (RURA) — https://www.rura.rw/
- Tanzania Personal Data Protection Act — https://www.pdpc.go.tz/en/policies-legislations/acts/
- Tanzania Personal Data Protection Regulations 2023 — https://www.pdpc.go.tz/en/policies-legislations/regulations/
- Tanzania Electronic and Postal Communications (Online Content) Regulations 2020 and Fair Competition Act 2003 — https://www.tcra.go.tz/
- Uganda Communications Commission, Quarterly Market Performance Reports — https://www.ucc.co.ug/market-performance-reports/
- Uganda Bureau of Statistics, National Standard Indicator Framework 2026 — https://www.ubos.org/wp-content/uploads/publications/03_2026National_Standard_Indicator_Framework_NSI_2026.pdf

International rules, codes and data:

- ICC Advertising and Marketing Communications Code — https://iccwbo.org/business-solutions/the-icc-advertising-and-marketing-communications-code/
- US FTC Endorsement Guides and Consumer Reviews and Testimonials Rule — https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides
- UK ASA/CAP influencers' guide and CMA enforcement of the DMCC Act — https://www.asa.org.uk/resource/influencers-guide.html
- EU General Data Protection Regulation (GDPR)
- EU AI Act, Articles 4 and 28b(4)
- UK Privacy and Electronic Communications Regulations (PECR)
- US CAN-SPAM Act
- US Copyright Office (2023) *Copyright and Artificial Intelligence*
- Writers Guild of America (2023) *Minimum Basic Agreement*, AI provisions
- International Telecommunication Union, Individuals using the Internet — https://datahub.itu.int/data/?c=1&i=11624

Platform owners:

- Meta Advertising Standards — https://www.facebook.com/policies/ads/
- Meta, About campaign objectives — https://www.facebook.com/business/help/1438417719786914
- Meta, Advantage+ campaigns — https://developers.facebook.com/docs/marketing-api/advantage-campaigns
- Meta, Special ad categories — https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category
- Meta, Social issue, electoral and political ads and Ad Library — https://transparency.meta.com/policies/ad-standards/SIEP-advertising/SIEP/
- Meta Ads Guide, image and video specifications — https://www.facebook.com/business/ads-guide/update/image/facebook-feed
- Meta, Rewarding Original Creators on Facebook — https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/amp/
- Facebook Help, Share something on Facebook — https://www.facebook.com/help/170116376402147
- Facebook Help, Edit photos and add alternative text — https://www.facebook.com/help/322590311283249
- Instagram Help, Scheduled posts and Reels — https://www.facebook.com/help/instagram/439971288310029
- Instagram Help, What is considered branded content — https://www.facebook.com/help/instagram/616901995832907
- WhatsApp Business Messaging Policy — https://whatsappbusiness.com/policy/
- TikTok Branded Content Policy — https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/branded-content-policy
- TikTok, Commercial use of music on TikTok — https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/commercial-use-of-music-on-tiktok
- TikTok, Promoting a brand, product or service — https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service
- TikTok Studio — https://support.tiktok.com/en/using-tiktok/creating-videos/tiktok-studio
- TikTok Ads, Commercial Music Library — https://ads.tiktok.com/resources/help/article/how-to-use-the-commercial-music-library?lang=en-GB
- TikTok Ads, Ad testing guide — https://ads.tiktok.com/business/en/guides/ad-testing-guide
- TikTok Ads, Set up and verify Pixel — https://ads.tiktok.com/resources/help/article/get-started-pixel?lang=en
- TikTok Ads, Choose the right advertising objective — https://ads.tiktok.com/help/article/choose-right-objective
- LinkedIn Professional Community Policies — https://www.linkedin.com/legal/professional-community-policies
- LinkedIn User Agreement — https://www.linkedin.com/legal/user-agreement
- LinkedIn, Objectives and Thought Leader Ads — https://www.linkedin.com/help/lms/answer/a1399568
- LinkedIn Help, Post and share updates — https://www.linkedin.com/help/linkedin/answer/a527227
- LinkedIn Help, Add alternative text to images — https://www.linkedin.com/help/linkedin/answer/a519856
- LinkedIn Help, Accessibility features for video posts — https://www.linkedin.com/help/linkedin/answer/a1369389
- Google Ads policies — https://support.google.com/adspolicy/answer/6008942
- Google personalised advertising policy — https://support.google.com/adspolicy/answer/143465
- Google Ads Help, Responsive search ads, Performance Max and Demand Gen — https://support.google.com/google-ads/answer/7684791
- Google Analytics 4, Select attribution settings — https://support.google.com/analytics/answer/10597962
- Google Consent Mode v2 and GA4 — https://support.google.com/tagmanager/answer/13695607
- Google Search Central, Optimising for generative AI features — https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google Search Essentials — https://developers.google.com/search/docs/essentials
- Google SEO Starter Guide — https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google, Page experience — https://developers.google.com/search/docs/appearance/page-experience
- Google, Link best practices — https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- Google, General structured data guidelines — https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Google, Featured snippets — https://developers.google.com/search/docs/appearance/featured-snippets
- Bing Webmaster Blog, AI Performance in Bing Webmaster Tools — https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
- OpenAI crawlers — https://developers.openai.com/api/docs/bots
- OpenAI models — https://developers.openai.com/api/docs/models
- OpenAI image generation guide — https://developers.openai.com/api/docs/guides/image-generation
- OpenAI release notes — https://openai.com/products/release-notes/
- OpenAI Help, GPT-5.6 and GPT-6 Pro in ChatGPT — https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt
- OpenAI legacy models page — https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4
- Perplexity crawlers — https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Anthropic models overview — https://platform.claude.com/docs/en/models/overview

Technical, accessibility and provenance:

- W3C Web Content Accessibility Guidelines (WCAG) 2.2
- Coalition for Content Provenance and Authenticity (C2PA)
- Google DeepMind (2023) SynthID
- IBM Research (2018) AI Fairness 360 (AIF360)
- llms.txt proposal — https://llmstxt.org/
- Model Context Protocol — https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro

### Websites and articles

- DataReportal (Kepios), Digital 2026: Uganda and Kenya — https://datareportal.com/reports/digital-2026-uganda
- Meltwater and LinkedIn, *How LinkedIn Content Wins in AI Search* — https://learn.meltwater.com/rs/814-WJU-189/images/2026%20Meltwater%20report%20-%20How%20LinkedIn%20Content%20Wins%20AI%20Search.pdf
- LinkedIn Marketing Blog, AI search and LinkedIn: five takeaways from 9.5 million citations — https://www.linkedin.com/business/marketing/blog/ai-search/new-meltwater-research-shares-5-insights-from-9-million-citations/
- Meltwater, LinkedIn AI visibility study — https://www.meltwater.com/en/blog/linkedin-ai-visibility-study
- Pew Research Center — https://www.pewresearch.org/
- Ookla Speedtest Global Index, Kenya — https://www.speedtest.net/global-index/kenya
- StatRanker, Kenya mobile speed
- SpeedOf.Me, Uganda mobile speed
- Yazi, WhatsApp usage estimates
- EY tax alert, Uganda tax amendment acts 2025 — https://www.ey.com/en_gl/technical/tax-alerts/uganda-issues-tax-amendment-acts-for-2025
- Vivid Voice News, Uganda moves to regulate social media influencers — https://www.vividvoicenews.com/2026/05/15/uganda-moves-to-regulate-social-media-influencers-as-digital-economy-expands/
- Wiley, announcement of *Search and Social* — https://investors.wiley.com/news/news-details/2012/Wiley-Announces-Search-and-Social-The-Definitive-Guide-to-Real-Time-Content-Marketing-2012-11-12/default.aspx
- Itamar Blauer, *Keywords for SEO* author page — https://www.itamarblauer.com/keywords-for-seo/
- Utah State University Digital Commons, *Keywords in Creative Writing* — https://digitalcommons.usu.edu/usupress_pubs/158
- McKinsey, Growth, marketing and sales capabilities — https://www.mckinsey.com/capabilities/growth-marketing-and-sales/how-we-help-clients
- Reddit r/SaaS, Tally at $5M ARR with 11 people — https://www.reddit.com/r/SaaS/comments/1wime93/tally_is_doing_5m_arr_with_11_people_i_decoded/
- Chris Donnelly, "Successful posts don't just happen" (LinkedIn) — https://www.linkedin.com/posts/donnellychris_successful-posts-dont-just-happen-theyre-activity-7305572553769537537-A5jS
- Newman and Schwarz (2018), *Science Communication*, audio-quality study
- Hund (2023), on influencer-industry structure
- Sheridan, M. (2019), "They Ask, You Answer" method and River Pools case
- ManyChat — https://manychat.com
- Africa's Talking — https://africastalking.com
