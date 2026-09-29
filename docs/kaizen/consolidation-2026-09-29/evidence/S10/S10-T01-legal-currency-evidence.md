# S10-T01 evidence: East Africa legal currency (gap G05)

- **Date:** 29 September 2026. Run ahead of S02–S09 under deviation D-SK-02 (ratified by orchestrator under Peter's delegated authority); committed separately from S01 so it can be reverted on its own.
- **Class:** doctrine + metadata. Reviewer verdict for this commit, if accepted: `ACCEPT WITH DOCUMENTED DEVIATION` (D-SK-02).
- **Method:** Digital Research currentness gate (`digital-research-engine/docs/continuous-improvement/kaizen-currentness-gate.md`; source evaluation and verification). Every claim was re-read live on 29 Sep 2026 with free web search and fetch. Factual reporting for screening and escalation, not legal advice.
- **Active skills:** 191 → 191.

## Claims verified

| # | Claim | Sources read (29 Sep 2026) | Disposition | Register ID |
|---|---|---|---|---|
| a1 | The Constitutional Court (five justices, unanimous, 17 Mar 2026; Consolidated Petitions 34, 37 and 42 of 2022) declared the **whole Computer Misuse (Amendment) Act 2022 void** because Parliament passed it without ascertaining quorum (Rule 24(3); Articles 88–89) | CPJ 19 Mar 2026; CIPESA 18 Mar 2026; search snippets from Monitor, The Independent, Hivos | Secondary, consistent across sources. Judgment on ULII: `NOT_ASSESSED` (Cloudflare challenge, HTTP 403, for both fetch and curl) | `UG-CMA-2022-VOID-2026` (partial) |
| a2 | Provisions of the **principal** Act struck: ss.11, 23, 26, 27, 28, 29 (2023 revised edition numbering); criminal libel (Penal Code ss.162–163) struck | The Independent; Monitor ("10 provisions", not listed); CPJ (Penal Code) | Section numbers per secondary reports; judgment `NOT_ASSESSED`; wording in skills says "per secondary reports" and "verify against the judgment on ULII" | `UG-CMA-SECTIONS-STRUCK-2026` (partial) |
| a3 | s.25 (offensive communication) was struck earlier, on 11 Jan 2023 | Monitor | Secondary | `UG-CMA-S25-2023` (partial) |
| a4 | The Attorney General (communication of 18 Mar 2026) halted arrests and prosecutions under the nullified provisions, advised against an appeal and recommended re-enactment by Parliament | Monitor 26 Mar 2026; Observer 27 Mar 2026 | Secondary. Any later appeal or re-enactment bill: `NOT_ASSESSED` (searches found none) | `UG-CMA-AG-DIRECTIVE-2026` (partial) |
| a5 | The remainder of the principal Computer Misuse Act 2011 (core cybercrime offences) remains in force | CIPESA, CPJ, AG reports (enforcement halt limited to named provisions) | Supported by the scope of the rulings; principal-Act text on ULII not read | as a1 |
| b | Facebook in Uganda: access reported restored on 13 Jun 2026 after the January 2021 block | Pulse Uganda 13 Jun 2026 (states that no UCC statement confirmed the change); a minister's post quoted there; no UCC, wire-service or Monitor/Observer confirmation found | **Official status `NOT_ASSESSED`.** Guidance written so that it asserts neither state: "status unstable; verify access at the campaign date" | `UG-FACEBOOK-ACCESS-2026` (partial) |
| c | Uganda suspended mobile internet on 13 Jan 2026 around the general election; UCC directed restoration of public internet on 18 Jan; social media restored about 26 Jan | UCC public update of 18 Jan 2026 (primary); Pulse Uganda 18 and 26 Jan 2026 | Restoration verified at UCC; start date and social-media end date secondary | `UG-INTERNET-SHUTDOWN-2026` (verified), `UG-SOCIAL-RESTORATION-2026` (partial) |
| d1 | Kenya ASBK Code of Advertising Practice and Direct Marketing is the April 2003 edition (substantiation 10.1, testimonials 13.0, children 21.0, recognition of an advertisement 24.0) | ASBK PDF (text extracted locally) | Edition verified; whether a later edition applies `NOT_ASSESSED` | `KE-ASBK-CODE-2003` (partial) |
| d2 | BCLB directive of 29 May 2025: no celebrities, influencers or content creators in gambling adverts; BCLB approval and KFCB classification | The Star, 30 May 2025 | Secondary; directive text `NOT_ASSESSED` | `KE-BCLB-GAMBLING-ADS-2025` (partial) |
| d3 | CA bulk-SMS guideline scope | CA/NCIC PDF (text extracted locally) | **Correction to plan E28:** it is the July 2017 guideline on *political* bulk and premium-rate messages and political social-media content, not a general commercial bulk-SMS rule (cl.10.1 express opt-in and opt-out; cl.9.2 08:00–17:00; cl.8.2 sender named). Commercial bulk SMS stays under the Data Protection Act rules (`KE-DP-GENERAL-2021`); KICA consumer-protection regulations `NOT_ASSESSED` | `KE-CA-POLITICAL-BULK-SMS-2017` (verified, scope-bound) |
| e1 | Tanzania PDPA 2022: no collection or processing without PDPC registration; certificate 5 years | Victory Attorneys legal alert (28 Mar 2024) and search results quoting s.14 | Secondary; PDPC PDF failed (certificate mismatch, then 404) and TanzLII returned 403: statute text `NOT_ASSESSED` | `TZ-PDPA-REGISTRATION-2026` (partial) |
| e2 | Rwanda Law 058/2021 art. 29: controllers and processors must register with the NCSA Data Protection and Privacy Office | NCSA DPO registration guide PDF (text extracted locally); DPO "who we are" page | Verified (regulator guide) | `RW-DPP-REGISTRATION-2026` (verified) |
| e3 | Tanzania TCRA online-content licensing | TCRA page for the Online Content (Amendment) Regulations 2021 (published 23 Aug 2021, updated 28 Jul 2026) | Page verified; amendment content `NOT_ASSESSED`; existing `TZ-ONLINE-CONTENT-2020` (verified 25 Sep 2026) reused for the licence duty, not re-verified | `TZ-TCRA-ONLINE-CONTENT-AMEND-2021` (not_assessed) |

Existing records reused, not duplicated: `TZ-ONLINE-CONTENT-2020`, `KE-DP-GENERAL-2021`, `KE-INFLUENCER-LAW-2026`, `DATAREPORTAL-UG-KE-2026` (MK-02; its note now points to the Facebook record, `verified_on` unchanged). New records carry scope, publication date, access date, verification date, freshness class, review date, support status and uncertainty.

## Changes

| File | Change |
|---|---|
| `skills/pipeline/08-influencer-marketing-strategy/references/influencer-term-sheet-and-disclosure.md` | Uganda row: s.26B no longer cited as law; the ruling stated with the precision above; check added to verify the section list on ULII. Kenya row: BCLB directive and ASBK edition. Tanzania row: 2021 amendment `NOT_ASSESSED`, PDPC registration. Rwanda row: art. 29 registration. Blockers paragraph updated |
| `skills/playbooks/playbook-social-media-policy/SKILL.md` (L12) | "Computer Misuse Act (2011, amended 2022)" replaced by the post-ruling position |
| `skills/playbooks/playbook-social-media-governance/SKILL.md` (L173) | Training row: "Computer Misuse Act (Uganda, 2011/2022)" replaced by the post-ruling position; defamation row notes that criminal libel was struck while civil liability and other speech offences remain |
| `skills/platforms/platform-facebook/SKILL.md` | Decision row for Uganda: status unstable, verify at the campaign date, keep a fallback channel |
| `AGENTS.md` | Platform-defaults Facebook row re-worded (status unstable; verify at campaign date; MK-02 kept as a floor) |
| `skills/playbooks/playbook-crisis-communications/SKILL.md` + NEW `references/internet-shutdown-contingency.md` | Shutdown and platform-block contingency (pre-flight, during, reporting); decision row and reference link |
| `skills/advertising/media-planning/SKILL.md` + `references/east-african-media-mix.md` | Decision row for elections and unstable platforms; MK-02 Facebook sentence re-worded; shutdown bullet with link to the crisis reference |
| `docs/quality-gates/legal-market-release-gate.md` | Six rows: Uganda cyber law, platform access, Kenya gambling with creators, Kenya bulk SMS, Kenya advertising code, Tanzania and Rwanda registration |
| `docs/source-registers/source-register.json` | 13 new records; `as_of` 2026-09-29; MK-02 note extended |
| `tests/test_engine_quality.py` | The register window test's as-of date moves from 2026-09-25 to 2026-09-29, because new records are verified on 29 Sep 2026 (the overdue-rejection test at 2026-10-20 still fails as designed) |

## Acceptance

- `git grep -n "Computer Misuse (Amendment) Act 2022\|Amendment) Act 2022 s.26B"`: every remaining hit presents the Amendment Act as void (influencer reference, policy playbook, legal-market gate, register titles and notes). No text presents it as live law. `2011, amended 2022` and `2011/2022`: 0 hits.
- `check_source_freshness.py`: PASS, 76 records as of 2026-09-29; `--as-of 2026-10-20` still fails on overdue records (negative test intact).
- Legal-market gate updated.
- Standard gate block: green (see the S01 evidence gate table; same run).

## Other engines citing the Computer Misuse Act (reported, not edited: outside this executor's scope)

| File | Line | Issue |
|---|---|---|
| `business-plan-skills/skills/pipeline/14-ai-integration/references/uganda-ict-ip-guidelines.md` | 37, 212–213 | "Computer Misuse Act 2011 (amended ...)" and a list of objectives (minors, hate speech, false information, ten-year bar on public office) that came from the void 2022 Amendment Act; needs the post-ruling note |
| `digital-research-engine/docs/plans/2026-04-26-upf-cris-design.md` | 197 | States "Currently in force: Computer Misuse Act amendment 2022"; now wrong |
| `business-plan-skills/skills/pipeline/10-financial-projections/references/uganda-ip-framework.md` | 310, 419 | Generic "Computer Misuse Act" mentions; fine if read as the principal Act; optional note |
| `srs-skills/domains/uganda/references/regulations.md` | 14 | "Computer Misuse Act 2011": unauthorised access and data interference; s.11 (2023 edition numbering) is reported struck, so the row should carry "as amended by the 2026 ruling; verify sections" |

## Reviewer verdict

Independent reviewer (read-only code-review agent, 29 Sep 2026): **ACCEPT_WITH_DOCUMENTED_LIMITATIONS**. The precision requirement was met: the text never says the Computer Misuse Act was voided, and Facebook is never asserted as blocked or open. All four minor findings were fixed:

1. The 15 Jan 2026 vote date is now held in `UG-SOCIAL-RESTORATION-2026`.
2. "Confirmed by a minister's post" now reads "welcomed in a minister's post".
3. The gate row now separates the 2023-edition numbering from pre-revision s.25.
4. "(2011; core cybercrime offences)" is shortened to "(2011)", and the governance training row now reads "defamation risk (criminal libel struck in Uganda; civil liability and other speech offences remain)".

## Open items

- Read the judgment on ULII when automated access allows, then upgrade `UG-CMA-*` records to verified or correct the section list.
- Facebook status: re-check by the record's review date (2026-10-29) for a UCC or other official statement.
- Kenya BCLB directive text, ASBK current edition, KICA consumer-protection regulations, Tanzania PDPA statute text and 2021 amendments, Uganda UCC Advertising Standards text: `NOT_ASSESSED`.
- The rest of S10 (T02–T14) runs after S09 as planned.
