# 053053.com — Phase-wise Build Prompts

These prompts are reusable: give them to any capable coding AI one phase at a time. The site in this repo is the output of Phases 0–8.

**Global constraints. Prepend these to every phase.**
> Domain: 053053.com. Concept: "053053 — Number Intelligence & Scam Shield": decode any phone number or prefix, starting with the 053 family (Turkcell 053x 🇹🇷, Hot Mobile 053 🇮🇱, Daegu 053 🇰🇷, Hamamatsu 053 🇯🇵, Enschede 053 🇳🇱, UTC+05:30 🇮🇳🇱🇰). Static HTML/CSS/vanilla JS only, deployable on the **GitHub Pages free plan** (no server, no build step required to serve). Use relative links everywhere so it works at `/053053-com/` and at the apex domain. Mobile-first, WCAG AA, dark/light theme, Core Web Vitals green, and no layout shift from ad slots (reserve height).
> Top of every page: a bar reading "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership", linked to https://web.works/contact.
> All forms post to a single inbox via FormSubmit AJAX. The inbox address must **never** appear in HTML, JS strings, mailto links or metadata. Store it XOR-obfuscated in `config.js` and assemble it only at submit time.
> AdSense publisher `ca-pub-6620975821265271` and the matching `ads.txt` line. Never fabricate reviews, statistics or user reports. "053053" is a descriptive numeral; include the trademark/copyright disclosure.

---

## Phase 0: Research and IA
> Audit 25+ sites (tellows, shouldianswer, unknownphone, spamcalls.net, callercenter, sync.me, Hiya, Robokiller, Nomorobo, Spokeo, allareacodes, areacodes.org, countrycode.org, timeanddate, worldtimebuddy, ScamAdviser, scam-detector, BBB Scam Tracker, Scamwatch, angel-number sites, numerology.com, RingCentral, Ooma, Grasshopper, Buy Me a Coffee, GoFundMe). Output a feature matrix and a sitemap: Home, Lookup, Report, Codes hub plus 6 prefix pages, Tools hub (Formatter, IST Call Planner, Number Meaning, Scam IQ Quiz), Guides hub (6+), Get Protected (lead gen), For Business (B2B), Videos, Contests, Donate, Advertise, Careers, About, The 053053 Story, Contact, Remove My Number, Legal, Privacy, Terms, 404.

## Phase 1: Design system
> Create `assets/css/style.css`: CSS custom properties for colours (deep navy and signal teal, with an amber "warning" accent), dark/light via `prefers-color-scheme` and a `[data-theme]` toggle, fluid type scale (Space Grotesk headings, Inter body), 8px spacing grid, containers, buttons (primary/ghost/sm), cards, badges (safe/caution/danger), stat bands, steppers, form controls with visible focus, tables, accordions, toasts, modals, a sticky mobile CTA, and ad-slot boxes with reserved min-height and an "Advertisement" label. No framework.

## Phase 2: Shared layout and config
> Write a tiny Python generator (`_gen/build.py`) that wraps page bodies in one layout: partner bar, header with logo "053053", nav (Lookup, Codes, Tools, Guides, Report, Get Protected, For Business, Support), a footer with 4 columns, a newsletter form, the legal line, the lead modal and JSON-LD. Output plain `.html` files (with `.nojekyll`). Create `assets/js/config.js` as the only file an owner edits: AdSense client and slots, YouTube channel and videos, donation links and goal, GA4, the obfuscated inbox.

## Phase 3: Core engine, Number Lookup
> In `assets/js/numbers.js`, build a client-side numbering dataset (country calling codes, plus detailed national plans for TR, IL, KR, JP, NL, IN, LK, US/CA, UK). The parser must accept any format, detect the country (by `+cc`/`00cc`, or by the user's selected country for national formats), and classify: mobile / geographic / toll-free / premium / VoIP. It returns region, original operator (with a portability caveat), the IANA time zone, local time now, "OK to call now?" (08:00–21:00 local), risk flags (premium rate, unexpected international, Wangiri-prone codes, satellite +881/+882), E.164 and every "ways of writing" variant. Render a result card with badges and actions: Report this number, How to block, Copy E.164, Share.

## Phase 4: Content and SEO pages
> Build `/codes/` with 6 deep prefix pages (053 Turkey/Turkcell, 053 Israel/Hot Mobile, 053 Daegu, 053 Hamamatsu, 053 Enschede, UTC+05:30). Each has a definition box, a format table, "ways of writing", local-time widget, how to call it from abroad, common scam patterns, an FAQ (with FAQPage schema), and a lead box. Build `/guides/` with 6+ long-form guides (Wangiri one-ring scams, block unknown callers on iPhone/Android, bank and government impersonation scripts, SMS delivery phishing, how to report scams by country, why India is UTC+5:30). Add breadcrumbs, canonical, OG tags, `sitemap.xml` and `robots.txt`.

## Phase 5: Lead generation (revenue core)
> `get-protected.html`: a 4-step form with a progress bar (1 need → 2 details → 3 contact → 4 consent). Needs: Business phone/VoIP, Local virtual number in TR/IL/KR/JP/NL/IN, Fix "Spam Likely" caller-ID flag, Identity-theft protection, I lost money to a scam (licensed help only, with a warning about recovery scams), International calling/eSIM. Capture UTM, landing page and referrer. Add `for-business.html` (B2B: caller-reputation repair, number-in-country, API waitlist, bulk lookups) with a demo-booking form. Add an exit-intent modal on desktop (once per session), a sticky mobile CTA, and inline lead boxes on every number and prefix page. Track `generate_lead` in GA4.

## Phase 6: Community and engagement
> `report.html`: a scam report form (number, country, date, call type taxonomy, 1–9 rating, claimed caller name, what they asked for, money lost Y/N plus amount, pseudonym, alert email, consent). On submit, show next-step advice for the chosen call type. Then build: `tools/scam-quiz.html` (10-question Scam IQ with score and share), `contests.html` (monthly "Scam Spotter Challenge" with prize tiers, rules, entry form, and an honest empty leaderboard until real winners exist), and `videos.html` (YouTube lite-embeds from config, falling back to search cards).

## Phase 7: Monetisation
> AdSense: auto-insert `<ins class="adsbygoogle">` into every `.ad` slot when `ADSENSE_CLIENT` is set, lazy-loaded with IntersectionObserver; house ads (advertise / sponsor) otherwise. Placements: below the lookup result, mid-article, sidebar sticky, pre-footer. `donate.html`: presets ($5/$15/$53/custom), monthly/once toggle, a "where money goes" breakdown (ops, moderation, marketing, hiring, contest prizes), a goal bar, and PayPal/Ko-fi/BMAC/Stripe/Patreon buttons from config, falling back to a pledge form. `advertise.html`: rate card, placements, sponsorship tiers and an inquiry form. `careers.html`: open roles (moderators, TR/HE/KO/JA/NL translators, writers, growth) with an application form.

## Phase 8: Legal, trust, QA, deploy
> Add `legal.html` (trademark and copyright disclosure, nominative use of operator names, no affiliation), `privacy.html` (GDPR/KVKK/PIPA/DPDP-aware, AdSense cookies, FormSubmit processor), `terms.html`, and `remove-my-number.html`. QA: every internal link resolves; the inbox string is absent from all files; Lighthouse ≥ 90; forms validate; keyboard navigation works; no horizontal scroll at 360px. Deploy: push to `main`; Settings → Pages → Deploy from branch `main` / root. Custom domain: add `CNAME` with `053053.com`, set the A records 185.199.108-111.153 and `www` CNAME → `webworksa1.github.io`, then enforce HTTPS.

## Phase 9 (growth, after launch)
> 1) Localise the 053 pages into Turkish, Hebrew, Korean, Japanese and Dutch (hreflang). 2) Generate per-number pages (`/n/90532xxxxxxx.html`) only for numbers with real moderated reports, using a GitHub Action that builds from `data/reports.json`. 3) Publish a monthly "053 Scam Wave Report" PDF as a backlink magnet. 4) Launch a public API waitlist, then a paid API. 5) Run YouTube Shorts "Is this number a scam?" that link back to the lookup.
