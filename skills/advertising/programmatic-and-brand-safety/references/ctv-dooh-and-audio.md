# CTV, digital out-of-home and audio

Read when a programmatic line is connected TV, a digital screen network, podcast or streaming audio. Parent: [programmatic-and-brand-safety](../SKILL.md). Classic outdoor sites, broadcast TV and FM radio are planned in [media planning](../../media-planning/SKILL.md).

## 1. Connected TV (CTV)

Key ideas for the brief:

- **Ad pods.** CTV ads run in breaks (pods) of several slots, like broadcast TV. Specify maximum pod length, slot position if bought, competitive separation (no two banks in one pod) and a household frequency cap across apps.
- **Formats.** On 11 Dec 2025 IAB Tech Lab announced a CTV Ad Portfolio of six core formats (Pause, Menu, Screensaver, In-Scene, Squeezeback, Overlay), with OpenRTB support for Pause and Menu, and an updated Guide to Programmatic CTV, both open for public comment to 31 Jan 2026 (register `IAB-TECHLAB-CTV-2025`, partial: the primary release could not be opened, and the final status is `NOT_ASSESSED`). Treat non-video formats as tests with their own reporting.
- **Transparency.** Require app-level (bundle ID) and device-type reporting, app-ads.txt authorisation, and a complete SupplyChain object. "Premium CTV" without an app list is not a buyable description.
- **Fraud.** Server-side ad insertion (SSAI) can limit what a verification tag sees about the device (practitioner understanding, not checked against a standard on 29 Sep 2026), so device and app claims need corroboration. MRC's 2024 interim update added bundle-ID spoofing and domain or inventory mismatch in CTV to the IVT requirements (register `MRC-IVT-INTERIM-2024`). Require SIVT filtration from a vendor accredited for CTV and certified partners (register `TAG-CERTIFIED-AGAINST-FRAUD`).

East Africa: CTV household penetration in Uganda, Kenya, Tanzania and Rwanda is `NOT_ASSESSED` (no dated, credible figure was read), and local streaming apps' ad inventory, if any, is unverified. Most "CTV" offered for East Africa will be global apps geotargeted by IP address, often with small audiences and high fraud exposure. Default: broadcast TV through `media-planning` for reach; CTV only as a capped test with app lists and delivery proof.

## 2. Digital out-of-home (DOOH)

The MRC Out-of-Home Measurement Standards (Phase 1 and 2 Combined Final, December 2025; register `MRC-OOH-STANDARDS`) give a ladder of metrics:

| Metric | What it needs |
|---|---|
| Location traffic | People or vehicles passing the site |
| Gross impressions | An ad play (digital) or posting (static), a working display and people present in the exposure zone |
| OTS (viewable) impressions | As above plus a viewability condition: 100% of the ad on screen for 1 second (static) or 2 continuous seconds (video) |
| LTS (likelihood to see) impressions | As above plus evidence that the display was noticed (for example visibility-adjusted contacts) |
| Audience | The fullest level, with evidence of notice |

Terms to define in the deal: **loop** (the full rotation of content), ad rotation duration, ad segment (the advertising part of the loop, like a pod), spot length and share of loop. Proof: the standard requires strong proof-of-play evidence; agree the affidavit elements (play logs per screen and hour, proof of play, dated photographs) with the seller before the campaign.

East Africa: LED screens and digital billboards in Kampala, Nairobi, Dar es Salaam and Kigali are mostly sold direct by the screen owner, some through local DOOH platforms. Whether any East African screen owner measures against the MRC standard is `NOT_ASSESSED`; most will report plays, not audiences. Minimum terms: screen list with GPS and photographs, loop length and number of advertisers in the loop, per-screen play logs, outage log (power cuts and connectivity), and dated photographs during the flight. Traffic counts from the owner are claims until audited; label them. Outdoor permits and content rules route to the [legal and market release gate](../../../../docs/quality-gates/legal-market-release-gate.md). Classic static billboards, taxi and matatu branding stay in `media-planning`.

## 3. Podcast and digital audio

The IAB Tech Lab Podcast Measurement Technical Guidelines v2.2 (May 2024; register `IAB-TECHLAB-PODCAST-2-2`) are the reference for downloaded audio:

- A download counts only if headers plus enough content to play one minute were delivered; duplicates from the same IP address and user agent in a 24-hour window are removed; pre-loading is filtered.
- An ad counts as delivered only inside a valid download; a dynamically inserted ad counts only when all its bytes were downloaded.
- Ask whether the host or ad server is IAB Tech Lab compliance-certified for v2.2. If not, label downloads and ad deliveries "(Seller-reported)".

Streaming audio (music apps, radio-station streams) is measured by the app's ad server; require impression logs, listen-through and the share of plays with the screen on or off. Boomplay and similar services may sell East African audio inventory; their user figures are UNVERIFIED and must come from the seller's own logs with app-ads.txt.

East Africa: FM radio remains the main news source in Uganda; 77% of Ugandans get news from radio at least a few times a week (Afrobarometer, published 13 Aug 2026; register `AFROBAROMETER-UG-RADIO-2026`). Radio airtime, station choice and spot logs are planned in `media-planning`; this skill covers only digital audio bought programmatically or by download. Podcast strategy and production sit with the video and content strategy skills.

## Sources

Register IDs: `IAB-TECHLAB-CTV-2025`, `MRC-IVT-INTERIM-2024`, `TAG-CERTIFIED-AGAINST-FRAUD`, `MRC-OOH-STANDARDS`, `IAB-TECHLAB-PODCAST-2-2`, `AFROBAROMETER-UG-RADIO-2026`.
