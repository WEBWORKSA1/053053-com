# 053053.com: Number Intelligence & Scam Shield

Decode any phone number or prefix, starting with the **053 family**: Turkcell 0530–0539 🇹🇷, Hot Mobile 053 🇮🇱, Daegu 053 🇰🇷, Hamamatsu 053 🇯🇵, Enschede 053 🇳🇱, plus UTC+05:30 🇮🇳🇱🇰 and +53 🇨🇺. Also includes scam red flags, community reports, a lead-generation funnel, a B2B offer, contests, donations and AdSense. Pure static HTML/CSS/JS on the **GitHub Pages free plan**.

Live: https://webworksa1.github.io/053053-com/

## Structure
```
index.html          home: hero lookup, 053 family, live clocks, tools, contest, FAQ
lookup.html         reverse number lookup (browser-side engine)
get-protected.html  4-step lead-gen funnel (8 verticals) ★ revenue core
for-business.html   B2B: Spam-Likely repair, local numbers, bulk/API, demo form
report.html         4-step moderated scam report
codes/              053 hub + 5 prefix pages + UTC+05:30 + +53 Cuba (FAQ schema)
tools/              IST call planner · number meaning · bulk E.164 · Scam IQ quiz
guides/             7 long-form guides
videos · contests · donate · advertise · careers · about · the-053053-story
contact · remove-my-number · legal (trademark/copyright) · privacy · terms · 404
assets/js/config.js ← the only file you edit (AdSense slots, YouTube, donations, GA4)
assets/js/app.js    UI, theme, forms, ads, video, donations, lead modal
assets/js/numbers.js number-intelligence engine + lookup UI
assets/js/tools.js  clocks, planner, meaning, bulk formatter, quiz
_gen/               python3 _gen/build.py regenerates every page from one layout
project-docs/       RESEARCH.md · BUILD-PROMPTS.md (phase-wise prompts)
```

## Go-live checklist
1. **Pages:** Settings → Pages → Build and deployment → *Deploy from a branch* → `main` / `(root)` → Save.
2. **Forms:** the first submission triggers a one-time FormSubmit activation email to the site inbox. Click *Activate*. The inbox address never appears on the site: it is assembled at submit time from an obfuscated array in `config.js`.
3. **AdSense:** publisher `ca-pub-6620975821265271` is set (Auto Ads + `ads.txt`). Add the site in AdSense → Sites. Optionally paste ad-unit slot ids into `AD_SLOTS`; until then reserved slots show house ads.
4. **YouTube / donations / GA4:** fill the matching keys in `config.js`.
5. **Custom domain 053053.com:** add a `CNAME` file containing `053053.com`. In `_gen/build.py` set `BASE = "https://053053.com/"` and `BASE_PATH = "/"`, then run `python3 _gen/build.py`. DNS: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, and `www` CNAME → `webworksa1.github.io`. Then tick *Enforce HTTPS* and update the `robots.txt` sitemap URL.
6. Submit `sitemap.xml` in Google Search Console.

## Partnerships
Interested in this website / domain / sponsorship / advertising / partnership → https://web.works/contact

## Trademark & copyright
“053053” is used as a descriptive numeral (the 053 dialling prefix repeated). No trademark is claimed in it, and the site is not affiliated with any telecom operator, regulator or referenced website. Operator names identify public numbering allocations only (nominative use). All content and code are original. See `legal.html`.
