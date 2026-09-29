# Brand safety and suitability

Read when writing the brand-safety floor, the suitability tiers, and the inclusion and exclusion lists for a programmatic or direct digital buy. Parent: [programmatic-and-brand-safety](../SKILL.md). Creator and influencer safety stays in [influencer marketing strategy](../../../pipeline/08-influencer-marketing-strategy/SKILL.md).

## 1. Status of GARM

The Global Alliance for Responsible Media (GARM) was discontinued by the World Federation of Advertisers on 9 August 2024 (register `WFA-GARM-DISCONTINUED-2024`). WFA named no successor body. Its Brand Safety Floor and Suitability Framework (September 2020 edition) remains a widely understood vocabulary, so this skill uses it as a **legacy reference**, never as a live standard, a certification or a body that can be "complied with".

What buyers use in practice is a combination of the client's own written policy, the verification vendor's category settings, the platform or SSP's controls, inclusion and exclusion lists, and content classification based on the IAB Tech Lab Content Taxonomy (version 3.1, December 2024; register `IAB-TECHLAB-CONTENT-TAXONOMY`). Whether any industry body now maintains a GARM-style shared floor is `NOT_ASSESSED`.

## 2. The floor (never fund)

Adapted from the GARM floor categories. No advertiser funds content that promotes or depicts, in a harmful way:

- illegal sexual content involving children, or explicit sexual acts;
- illegal arms sales or instruction to make or use them for harm;
- graphic promotion of crime, human trafficking, slavery, self-harm or animal cruelty; harassment;
- incitement to violence, murder, war crimes or genocide;
- piracy, copyright infringement and counterfeiting;
- hate speech that dehumanises people for race, ethnicity, tribe, religion, gender, sexual orientation, disability, nationality or illness;
- excessive profanity or gore intended to shock;
- sale of illegal drugs; promotion of tobacco, vaping or alcohol to minors;
- malware, phishing and spam;
- terrorist promotion;
- insensitive or inflammatory treatment of debated social issues that demeans a group.

Add the client's own absolute exclusions (for example competitor content, unlicensed betting sites for a bank) and the legal rules of each market, routed through the [legal and market release gate](../../../../docs/quality-gates/legal-market-release-gate.md).

## 3. Suitability tiers

Above the floor, content is sensitive but can carry ads with the right controls. The legacy framework grades each category in three risk tiers:

| Tier | Typical content | Default for most brands |
|---|---|---|
| High risk | Glamorised or gratuitous depiction; graphic imagery; insensitive treatment | Exclude |
| Medium risk | Dramatic depiction in entertainment; **breaking news and opinion** coverage of the topic | Include for news-tolerant brands; case-by-case for sensitive categories |
| Low risk | Educational, informative or scientific treatment; news features | Include |

Record the tier chosen per category in the suitability decision log with the owner and reason. A bank, a children's product and a political campaign need different settings.

## 4. News publishers and keyword blocking

The legacy framework places breaking news and op-ed coverage in the medium and low tiers, not the floor. Blanket keyword blocking ("attack", "death", "election", "police", "Ebola") removes large parts of legitimate news and moves spend away from the publishers that most readers trust. Practice:

- Prefer contextual suitability classification and an **inclusion list** of named news publishers over long keyword lists.
- Keep keyword lists short, reviewed monthly and tested against a sample of the publisher's pages before launch; record the share of pages each list would remove.
- For crisis periods (elections, disasters, security incidents), pause or change creative that would read badly next to the news, rather than blocking the news itself.

## 5. East Africa: local-language and local publishers

- Classification tools are trained mostly on English and major world languages. Their accuracy on Luganda, Kiswahili, Runyankore, Luo, Kinyarwanda and other local languages is `NOT_ASSESSED`; vendors may over-block (treating unknown text as unsafe) or under-block.
- For local-language news and radio-station websites, use a reviewed inclusion list and manual spot checks rather than automated keyword blocking.
- Build the inclusion list with each publisher: domain, apps, sections, ad-serving set-up (ads.txt, direct or programmatic) and a contact for placement reports. Examples to check: Daily Monitor and New Vision (Uganda), Daily Nation and The Standard (Kenya), The Citizen and Mwananchi (Tanzania), The New Times (Rwanda).
- Election periods: political content rules differ by country and platform. Suitability settings do not answer the legal question; route political and issue advertising to the legal and market release gate.

## 6. Policy template (one page)

| Item | Content |
|---|---|
| Owner | Named client marketing lead; legal reviewer |
| Floor | Section 2 list plus client exclusions |
| Tiers | Category, tier chosen, reason, owner |
| Inclusion list | Publishers, apps, channels, date reviewed |
| Exclusion list | Domains, apps, keywords (short), date reviewed |
| Vendor settings | Vendor, categories switched on, pre-bid or post-bid |
| Incident rule | Who is told, within what time, what is paused, how the make-good is agreed |
| Review | Monthly, and before any election or major national event |

## Sources

Register IDs: `WFA-GARM-DISCONTINUED-2024`, `IAB-TECHLAB-CONTENT-TAXONOMY`.
