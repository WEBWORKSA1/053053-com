#!/usr/bin/env python3
"""053053.com static generator: wraps page bodies in the shared layout and writes plain .html files.
Run: python3 _gen/build.py   (from repo root). Output is committed; GitHub Pages serves it as-is."""
import json, os, re, sys, html
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://webworksa1.github.io/053053-com/"
BASE_PATH = "/053053-com/"   # change to "/" with the custom domain   # change to https://053053.com/ when the custom domain is live
TODAY = date.today().isoformat()
PAGES = []

def page(path, title, desc, body, *, tools=False, lookup=False, noexit=False, ld=None, crumbs=None, ogtype="website"):
    PAGES.append(dict(path=path, title=title, desc=desc, body=body, tools=tools, lookup=lookup, noexit=noexit, ld=ld or [], crumbs=crumbs, ogtype=ogtype))

def ad(slot="inContent"):
    return f'<div class="ad" aria-label="Advertisement"><div class="box" data-slot="{slot}"></div></div>'

def faq(items):
    h = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub("<[^>]+>", "", q), "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in items]}
    return h, ld

def leadbox(r, title="Need a number in this country, or help after a scam call?", text="Get matched with vetted providers in 60 seconds: virtual local numbers, business phone systems, call-blocking, identity protection and licensed fraud help.", need=""):
    q = f"?need={need}" if need else ""
    return f'''<div class="leadbox"><div class="grid g2" style="align-items:center"><div><span class="eyebrow">Free · no obligation</span><h3>{title}</h3><p class="mute" style="margin:0">{text}</p></div>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="{r}get-protected.html{q}">Get matched free</a><a class="btn ghost" href="{r}for-business.html">For business</a></div></div></div>'''

COUNTRY_OPTS = '''<option value="auto">🌐 Auto-detect</option><option value="TR">🇹🇷 Türkiye</option><option value="IL">🇮🇱 Israel</option><option value="KR">🇰🇷 South Korea</option><option value="JP">🇯🇵 Japan</option><option value="NL">🇳🇱 Netherlands</option><option value="IN">🇮🇳 India</option><option value="LK">🇱🇰 Sri Lanka</option><option value="GB">🇬🇧 United Kingdom</option><option value="US">🇺🇸 USA / Canada</option>'''

def searchbox(r, autofocus=False, action=None):
    act = f' action="{action}"' if action else ""
    af = " autofocus" if autofocus else ""
    return f'''<form class="search" id="lookup" role="search"{act}><label class="hp" for="lk-c">Country</label><select id="lk-c" name="country" aria-label="Country">{COUNTRY_OPTS}</select>
<label class="hp" for="lk-q">Phone number or prefix</label><input id="lk-q" name="q" inputmode="tel" autocomplete="off" placeholder="Enter any number · e.g. +90 532… or 053"{af} required><button class="btn" type="submit">Decode number</button></form>'''

def header(r):
    return f'''<div class="pbar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership → <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{r}index.html" aria-label="053053 home"><span class="mk">053</span><span>053053<small>Number intelligence</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">☰ Menu</button>
<nav class="nav" id="nav" aria-label="Main"><a href="{r}lookup.html">Lookup</a><a href="{r}codes/index.html">053 Codes</a><a href="{r}tools/index.html">Tools</a><a href="{r}guides/index.html">Guides</a><a href="{r}report.html">Report</a><a href="{r}for-business.html">Business</a><a href="{r}donate.html">Support</a><button class="theme-btn" type="button" aria-label="Toggle dark or light theme">◐</button><a class="btn sm" href="{r}get-protected.html">Get Protected</a></nav>
</div></header>'''

def footer(r):
    return f'''<footer class="ftr"><div class="wrap"><div class="cols">
<div><a class="logo" href="{r}index.html"><span class="mk">053</span><span>053053<small>Number intelligence</small></span></a>
<p class="mute small" style="margin-top:14px">Decode any phone number, spot scam patterns, and get matched with vetted protection and business-phone providers. Lookups run in your browser.</p>
<form data-form="newsletter" data-subject="Scam Wave Alert signup" class="news" aria-label="Newsletter"><input type="email" name="email" placeholder="Your email" required aria-label="Email"><button class="btn sm" type="submit">Get alerts</button></form>
<p class="small dim" style="margin-top:8px">“Scam Wave Alert”: new phone-scam patterns, weekly. Unsubscribe anytime.</p></div>
<div><h4>Decode</h4><ul><li><a href="{r}lookup.html">Number lookup</a></li><li><a href="{r}codes/index.html">The 053 family</a></li><li><a href="{r}codes/053-turkey-turkcell.html">053 Türkiye (Turkcell)</a></li><li><a href="{r}codes/053-israel-hot-mobile.html">053 Israel</a></li><li><a href="{r}codes/utc-0530-india-sri-lanka.html">UTC+05:30</a></li><li><a href="{r}tools/index.html">All tools</a></li></ul></div>
<div><h4>Protect</h4><ul><li><a href="{r}get-protected.html">Get protected (free)</a></li><li><a href="{r}report.html">Report a scam number</a></li><li><a href="{r}guides/index.html">Scam guides</a></li><li><a href="{r}guides/report-scams-by-country.html">Official reporting by country</a></li><li><a href="{r}tools/scam-quiz.html">Scam IQ quiz</a></li><li><a href="{r}remove-my-number.html">Remove my number</a></li></ul></div>
<div><h4>053053</h4><ul><li><a href="{r}about.html">About</a></li><li><a href="{r}the-053053-story.html">The 053053 story</a></li><li><a href="{r}for-business.html">For business</a></li><li><a href="{r}contests.html">Scam Spotter Challenge</a></li><li><a href="{r}videos.html">Videos</a></li><li><a href="{r}advertise.html">Advertise</a></li><li><a href="{r}careers.html">Careers</a></li><li><a href="{r}donate.html">Support us</a></li><li><a href="{r}contact.html">Contact</a></li></ul></div>
</div>
<div class="legal">© <span data-year></span> 053053. “053053” is used as a descriptive numeral (the 053 dialling prefix, repeated). No trademark is claimed in it, and this site has no affiliation with Turkcell, Hot Mobile, any telecom operator, regulator or the sites referenced. Operator names identify public numbering allocations only. Lookups are informational. <a href="{r}legal.html">Trademark &amp; copyright</a> · <a href="{r}privacy.html">Privacy</a> · <a href="{r}terms.html">Terms</a> · <a href="https://web.works/contact" target="_blank" rel="noopener">Buy / sponsor this domain</a></div>
</div></footer>
<div class="mcta"><a class="btn" href="{r}get-protected.html">🛡️ Get protected / get a number: free match</a></div>
'''

def render(p):
    depth = p["path"].count("/")
    r = "../" * depth
    if p["path"] == "404.html": r = BASE_PATH
    canon = BASE + (p["path"] if p["path"] != "index.html" else "")
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "053053", "url": BASE,
           "potentialAction": {"@type": "SearchAction", "target": BASE + "lookup.html?n={number}", "query-input": "required name=number"}},
          {"@context": "https://schema.org", "@type": "Organization", "name": "053053", "url": BASE, "logo": BASE + "assets/img/icon.svg"}] + p["ld"]
    crumbs = ""
    if p["crumbs"]:
        items = [("Home", r + "index.html")] + p["crumbs"]
        crumbs = '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(f'<a href="{u}">{n}</a>' if u else n for n, u in items) + "</nav>"
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n} for i, (n, u) in enumerate(items)]})
    body = p["body"].replace("{CRUMBS}", crumbs).replace("{R}", r)
    scripts = f'<script src="{r}assets/js/config.js"></script><script src="{r}assets/js/app.js" defer></script>'
    if p["lookup"] or p["tools"]: scripts += f'<script src="{r}assets/js/numbers.js" defer></script>'
    if p["tools"]: scripts += f'<script src="{r}assets/js/tools.js" defer></script>'
    t = html.escape(p["title"]); d = html.escape(p["desc"])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#070d1a">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{p['ogtype']}"><meta property="og:site_name" content="053053">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE}assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{r}assets/img/icon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
<script>try{{var t=localStorage.getItem("053_theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body data-root="{r}"{' data-no-exit' if p['noexit'] else ''}>
<a class="skip" href="#main">Skip to content</a>
{header(r)}
<main id="main">
{body}
</main>
{footer(r)}
{scripts}
</body>
</html>
'''

def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import pages_core, pages_codes, pages_guides, pages_more  # noqa: registers pages
    for m in (pages_core, pages_codes, pages_guides, pages_more): m.register(page, ad, faq, leadbox, searchbox)
    urls = []
    for p in PAGES:
        out = os.path.join(ROOT, p["path"]); os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(render(p))
        if p["path"] != "404.html": urls.append(p["path"])
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        pr = "1.0" if u == "index.html" else "0.9" if u.startswith(("codes/", "lookup", "get-protected")) else "0.7"
        sm.append(f"<url><loc>{BASE}{'' if u == 'index.html' else u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    print(f"built {len(PAGES)} pages")

if __name__ == "__main__":
    main()
