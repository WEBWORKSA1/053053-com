"""Tools, community, monetisation, company and legal pages."""

def register(page, ad, faq, leadbox, searchbox):
    R = "{R}"
    # ------------------------------------------------------------------ TOOLS
    page("tools/index.html", "Free Number Tools: Lookup, IST Planner, Number Meaning, Bulk E.164, Scam Quiz · 053053",
         "Free phone-number and time tools: reverse lookup, India/Sri Lanka call planner, Chinese & numerology number meaning, bulk E.164 formatter and Scam IQ quiz.",
         f'''<section class="hero"><div class="wrap">{{CRUMBS}}<span class="eyebrow">Tools</span><h1>Free number tools</h1><p class="lead">Everything runs in your browser. Nothing you type is stored.</p>
<div class="grid g3" style="margin-top:24px">
<a class="card" href="../lookup.html"><span class="ic">🔎</span><h3>Number Lookup</h3><p>Country, type, operator, local time, red flags.</p></a>
<a class="card" href="ist-call-planner.html"><span class="ic">🕠</span><h3>IST / SLST Call Planner</h3><p>Best overlap hours with India, Sri Lanka or any 053 city.</p></a>
<a class="card" href="number-meaning.html"><span class="ic">✨</span><h3>Number Meaning</h3><p>Chinese sound-alikes, numerology and angel-number readings.</p></a>
<a class="card" href="bulk-formatter.html"><span class="ic">📋</span><h3>Bulk E.164 Formatter</h3><p>Normalise up to 500 numbers and download CSV.</p></a>
<a class="card" href="scam-quiz.html"><span class="ic">🧠</span><h3>Scam IQ Quiz</h3><p>10 real-world scenarios. Share your score.</p></a>
<a class="card" href="../report.html"><span class="ic">⚑</span><h3>Report a Number</h3><p>Warn the community.</p></a></div></div></section>{ad()}''', crumbs=[("Tools", None)])

    page("tools/ist-call-planner.html", "IST Call Planner: Best Time to Call India, Sri Lanka & 053 Cities · 053053",
         "Find the best time to call or meet India (IST, UTC+05:30), Sri Lanka, Türkiye, Israel, Korea, Japan or the Netherlands from your time zone.",
         f'''<section><div class="wrap">{{CRUMBS}}<div class="layout"><div>
<span class="eyebrow">🕠 Tool</span><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">IST Call Planner</h1><p class="lead">Pick your zone and theirs. Green blocks are their business hours, laid over your day.</p>
<form id="planner" class="form-card" onsubmit="return false"><div class="row2"><div class="f"><label for="p-tz">Your time zone</label><select id="p-tz" name="tz"></select></div>
<div class="f"><label for="p-t">Calling</label><select id="p-t" name="target"><option value="Asia/Kolkata">🇮🇳 India (IST, UTC+05:30)</option><option value="Asia/Colombo">🇱🇰 Sri Lanka (UTC+05:30)</option><option value="Europe/Istanbul">🇹🇷 Türkiye</option><option value="Asia/Jerusalem">🇮🇱 Israel</option><option value="Asia/Seoul">🇰🇷 Daegu / Korea</option><option value="Asia/Tokyo">🇯🇵 Hamamatsu / Japan</option><option value="Europe/Amsterdam">🇳🇱 Enschede / Netherlands</option><option value="America/Havana">🇨🇺 Cuba</option></select></div></div>
<div id="planner-out" aria-live="polite"></div></form>
{ad()}
<h2>053 world clocks</h2><div class="grid g4" data-clocks></div>
</div><aside class="side">{leadbox(R, "Working with India or Sri Lanka?", "Get a local +91 / +94 number or a business phone system for distributed teams.", "virtual-number")}{ad("sidebar")}</aside></div></div></section>''',
         tools=True, crumbs=[("Tools", R + "tools/index.html"), ("IST Call Planner", None)])

    page("tools/number-meaning.html", "Number Meaning Calculator: Chinese Lucky Numbers, Numerology & Angel Numbers · 053053",
         "What does your number mean? Decode any number with Chinese sound-alike meanings (520, 530, 1314, 8), numerology roots and angel-number themes. Try 053053.",
         f'''<section><div class="wrap">{{CRUMBS}}<div class="layout"><div>
<span class="eyebrow">✨ Tool</span><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">What does your number mean?</h1><p class="lead">Phone numbers, dates, prices, plates. See the cultural readings people attach to digits.</p>
<form id="meaning" class="form-card"><div class="f"><label for="m-n">Your number</label><input id="m-n" name="num" inputmode="numeric" value="053053"></div><button class="btn" type="submit">Decode meaning</button><div id="meaning-out" style="margin-top:18px" aria-live="polite"></div></form>
{ad()}
<div class="prose"><h2>053053, decoded</h2><p>Digit sum 0+5+3+0+5+3 = 16 → 1+6 = <b>7</b>, the number of analysis and insight in numerology. In Mandarin sound-alike slang, 0 ≈ 你 (you), 5 ≈ 我 (me) and 3 ≈ 生 (life) or 想 (miss), so 053 can be read playfully as “you-me-life”. It's a creative reading, not an established code like <b>520</b> (I love you) or <b>530</b> (I miss you).</p></div>
</div><aside class="side"><div class="card"><h3>Want a number that means something?</h3><p class="small">Get a memorable or lucky virtual number for your business.</p><a class="btn sm" href="../get-protected.html?need=virtual-number">Find a number</a></div>{ad("sidebar")}</aside></div></div></section>''',
         tools=True, crumbs=[("Tools", R + "tools/index.html"), ("Number Meaning", None)])

    page("tools/bulk-formatter.html", "Bulk Phone Number Formatter: Convert to E.164 & Detect Line Type · 053053",
         "Paste up to 500 phone numbers and convert them to E.164 with country, line type (mobile, landline, VoIP, premium) and region. Download CSV free.",
         f'''<section><div class="wrap">{{CRUMBS}}
<span class="eyebrow">📋 Tool</span><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">Bulk E.164 formatter</h1><p class="lead">One number per line. Processing happens in your browser.</p>
<form id="bulk" class="form-card"><div class="row2"><div class="f"><label for="bk-c">Default country for national numbers</label><select id="bk-c" name="country"><option value="auto">🌐 Auto-detect</option><option value="TR">🇹🇷 Türkiye</option><option value="IL">🇮🇱 Israel</option><option value="KR">🇰🇷 South Korea</option><option value="JP">🇯🇵 Japan</option><option value="NL">🇳🇱 Netherlands</option><option value="IN">🇮🇳 India</option><option value="LK">🇱🇰 Sri Lanka</option><option value="GB">🇬🇧 United Kingdom</option><option value="US">🇺🇸 USA / Canada</option></select></div><div class="f"><label>Need more than 500 or an API?</label><a class="btn ghost" href="../for-business.html#demo">Join the API waitlist</a></div></div>
<div class="f"><label for="bk-l">Numbers</label><textarea id="bk-l" name="list" rows="8">+90 532 123 45 67
+972 53-123-4567
0031 53 123 4567
(415) 555-0134
+44 70 1234 5678</textarea></div><button class="btn" type="submit">Format all</button><div id="bulk-out" style="margin-top:18px"></div></form>{ad()}</div></section>''',
         tools=True, crumbs=[("Tools", R + "tools/index.html"), ("Bulk Formatter", None)])

    page("tools/scam-quiz.html", "Scam IQ Quiz: Can You Spot a Phone Scam? · 053053",
         "Ten real-world phone and SMS scam scenarios. Test your Scam IQ, learn the tell-tale signs and share your score.",
         f'''<section><div class="wrap">{{CRUMBS}}<div class="layout"><div>
<span class="eyebrow">🧠 Quiz</span><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">What's your Scam IQ?</h1><p class="lead">10 scenarios based on real scam scripts. No sign-up.</p>
<div id="quiz" class="form-card"><div id="quiz-box" aria-live="polite"></div></div>{ad()}
</div><aside class="side"><div class="card"><h3>Teams &amp; schools</h3><p class="small">Run Scam IQ for your staff or students with a custom leaderboard.</p><a class="btn sm" href="../for-business.html#demo">Ask us</a></div>{ad("sidebar")}</aside></div></div></section>''',
         tools=True, crumbs=[("Tools", R + "tools/index.html"), ("Scam IQ Quiz", None)])

    # ------------------------------------------------------------------ VIDEOS
    page("videos.html", "Video Explainers: Phone Scams, Blocking & Calling Tips · 053053",
         "Watch short explainers on one-ring scams, bank impersonation, smishing, blocking spam calls, calling abroad and India's half-hour time zone.",
         f'''<section><div class="wrap">{{CRUMBS}}<span class="eyebrow">▶️ Videos</span><h1>Watch &amp; learn</h1><p class="lead">Short explainers on scams, blocking and calling across the 053 world. <a data-yt-channel target="_blank" rel="noopener" href="#">Subscribe on YouTube →</a></p>
<div class="grid g3" data-videos="12" style="margin-top:20px"></div>{ad()}
<div class="cta-band" style="margin-top:30px"><h2>Make a video with us</h2><p>Creators: explain a scam you spotted and enter the <a style="color:#7ff5df" href="contests.html">Scam Spotter Challenge</a>, or <a style="color:#7ff5df" href="careers.html">join as a contributor</a>.</p></div></div></section>''',
         crumbs=[("Videos", None)])

    # ------------------------------------------------------------------ CONTESTS
    page("contests.html", "Scam Spotter Challenge: Monthly Contest with Prizes · 053053",
         "Spot, explain and report real phone-scam patterns. Monthly Scam Spotter Challenge with cash and gear prizes, open categories for writers, creators and translators.",
         f'''<section class="hero"><div class="wrap">{{CRUMBS}}<span class="eyebrow">🏆 Monthly contest</span><h1>The Scam Spotter Challenge</h1>
<p class="lead">Help protect millions of people from phone fraud, and win. Each month we pick the clearest, most useful scam explainers from our community.</p>
<div class="grid g3" style="margin-top:20px"><div class="card"><span class="ic">🥇</span><h3>Grand prize</h3><p>$253 cash or gift card + featured creator spot</p></div><div class="card"><span class="ic">🥈</span><h3>Runner-up</h3><p>$53 + premium call-blocker subscription*</p></div><div class="card"><span class="ic">🌍</span><h3>Best translation</h3><p>$53 for the best TR / HE / KO / JA / NL adaptation</p></div></div>
<p class="small dim" style="margin-top:10px">*Subject to sponsor availability. Prize amounts are set per season and confirmed on this page before each round opens.</p></div></section>
{ad()}
<section class="sec-alt"><div class="wrap"><div class="grid g2">
<div><h2>How to enter</h2><div class="steps"><div class="card"><h3>Spot</h3><p>Find a real scam call, SMS or pattern, ideally in a 053 country.</p></div><div class="card"><h3>Explain</h3><p>Write ≤300 words or make a ≤90-second video: how it works and how to beat it.</p></div><div class="card"><h3>Submit</h3><p>Use the form. Remove all personal data.</p></div></div>
<h3 style="margin-top:24px">Leaderboard</h3><div class="card"><p class="mute">Season 1 is open. Winners will be listed here once judged. No placeholder names, ever.</p></div>
<h3 style="margin-top:24px">Rules (summary)</h3><ul class="small mute"><li>Free to enter; no purchase necessary. 18+ or with guardian consent.</li><li>Original work only; you grant 053053 a licence to publish with credit.</li><li>Judged on accuracy, clarity and usefulness. Void where prohibited.</li><li>Full rules in our <a href="terms.html">terms</a>.</li></ul></div>
<div><form class="form-card" data-form="contest-entry" data-subject="Scam Spotter entry" data-done="#ct-done"><h3>Submit your entry</h3>
<div class="row2"><div class="f"><label for="c-n">Name / handle</label><input id="c-n" name="name" required></div><div class="f"><label for="c-e">Email</label><input id="c-e" name="email" type="email" required></div></div>
<div class="row2"><div class="f"><label for="c-c">Category</label><select id="c-c" name="category" required><option value="">Choose…</option><option>Written explainer</option><option>Video explainer</option><option>Translation</option><option>Scam pattern discovery</option></select></div><div class="f"><label for="c-co">Country</label><input id="c-co" name="country" required></div></div>
<div class="f"><label for="c-l">Link to your video/post (optional)</label><input id="c-l" name="link" type="url" placeholder="https://"></div>
<div class="f"><label for="c-t">Your explainer</label><textarea id="c-t" name="entry" required placeholder="What's the scam, how does it work, how do people beat it?"></textarea></div>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> This is my original work, contains no personal data, and I accept the contest rules.</label>
<button class="btn" type="submit" style="width:100%;margin-top:8px">Submit entry</button></form>
<div id="ct-done" class="form-card" style="display:none"><h3>✓ Entry received, good luck!</h3><p>Winners are announced at the start of next month.</p></div></div>
</div></div></section>
<section id="sponsor"><div class="wrap"><div class="cta-band"><div class="grid g2" style="align-items:center"><div><h2>Sponsor a prize</h2><p>Put your security, telecom or fintech brand in front of a scam-aware audience. Logo on the contest page, winner announcements and newsletter.</p></div><div><a class="btn amb" href="advertise.html#inquiry">Become a sponsor</a> <a class="btn ghost" style="color:#fff" href="https://web.works/contact" target="_blank" rel="noopener">Partnership inquiry</a></div></div></div></div></section>''',
         crumbs=[("Contests", None)])

    # ------------------------------------------------------------------ DONATE
    page("donate.html", "Support 053053: Keep Free Scam Protection Running",
         "Donate to keep 053053's free number lookup and scam protection running: moderation, translators, marketing, hiring and Scam Spotter prizes.",
         f'''<section class="hero"><div class="wrap">{{CRUMBS}}<div class="grid g2">
<div><span class="eyebrow">💚 Support</span><h1>Keep scam protection free for everyone</h1><p class="lead">053053 has no paywall and stores no searches. Your support pays for the people and prizes that keep it useful.</p>
<div data-goal style="margin:20px 0"></div>
<h3>Where your money goes</h3><div class="tscroll"><table class="tbl"><tr><th>Use</th><th>Share</th></tr><tr><td>🛡️ Report moderation &amp; operations</td><td>35%</td></tr><tr><td>🌍 Translators (TR · HE · KO · JA · NL)</td><td>20%</td></tr><tr><td>📣 Awareness campaigns &amp; promotion</td><td>15%</td></tr><tr><td>👩‍💻 Hiring contributors &amp; developers</td><td>15%</td></tr><tr><td>🏆 Scam Spotter Challenge prizes</td><td>15%</td></tr></table></div></div>
<div class="form-card"><h3>Choose an amount</h3>
<div class="amts"><button type="button" data-amt="5">$5</button><button type="button" data-amt="15">$15</button><button type="button" data-amt="53" class="on">$53</button><button type="button" data-amt="253">$253</button></div>
<div data-donate-links style="margin:10px 0 18px"></div>
<form data-form="donation-pledge" data-subject="Donation pledge" data-done="#dn-done"><div class="row2"><div class="f"><label for="pledge-amount">Amount (USD)</label><input id="pledge-amount" name="amount" type="number" min="1" value="53" required></div>
<div class="f"><label for="d-f">Frequency</label><select id="d-f" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="row2"><div class="f"><label for="d-n">Name</label><input id="d-n" name="name" required></div><div class="f"><label for="d-e">Email</label><input id="d-e" name="email" type="email" required></div></div>
<div class="f"><label for="d-a">Direct my gift to (optional)</label><select id="d-a" name="allocation"><option>Wherever it's needed most</option><option>Moderation &amp; operations</option><option>Translations</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contest prizes</option></select></div>
<label class="chk"><input type="checkbox" name="public" value="yes"> List me as a supporter (first name only)</label>
<button class="btn amb" type="submit" style="width:100%">Pledge &amp; get a secure payment link</button></form>
<div id="dn-done" style="display:none"><h3>✓ Thank you!</h3><p>We'll email a secure payment link within 24 hours.</p></div>
<p class="small dim" style="margin-top:12px">053053 is not a registered charity; donations are not tax-deductible. Businesses: see <a href="advertise.html">sponsorship</a>.</p></div>
</div></div></section>''', noexit=True, crumbs=[("Support", None)])

    # ------------------------------------------------------------------ ADVERTISE
    page("advertise.html", "Advertise & Sponsor on 053053: Reach Scam-Aware, High-Intent Audiences",
         "Advertising and sponsorship on 053053: display placements, sponsored guides, tool sponsorships, newsletter and Scam Spotter Challenge prizes.",
         f'''<section class="hero"><div class="wrap">{{CRUMBS}}<span class="eyebrow">📣 Advertise</span><h1>Reach people at the exact moment they care about phone security</h1>
<p class="lead">Our visitors just received a suspicious call, or are choosing a number, phone system or protection plan. That intent converts.</p>
<p><a class="btn" href="#inquiry">Request the media kit</a> <a class="btn ghost" href="https://web.works/contact" target="_blank" rel="noopener">Domain / partnership inquiry</a></p></div></section>
<section class="sec-alt"><div class="wrap"><h2>Placements</h2><div class="grid g3" style="margin-top:16px">
<div class="card"><h3>Lookup result sponsor</h3><p>Exclusive box under every lookup result in one country or globally.</p><p class="small"><b>From $530 / month</b></p></div>
<div class="card"><h3>053 country page takeover</h3><p>Own a prefix page (e.g. 053 Türkiye) with native lead box and banner.</p><p class="small"><b>From $253 / month</b></p></div>
<div class="card"><h3>Sponsored guide</h3><p>Expert article, clearly labelled, permanent link and promotion.</p><p class="small"><b>From $353 one-off</b></p></div>
<div class="card"><h3>Tool sponsorship</h3><p>“Powered by” on the IST Planner, Bulk Formatter or Scam IQ.</p><p class="small"><b>From $153 / month</b></p></div>
<div class="card"><h3>Newsletter</h3><p>Scam Wave Alert: one sponsor slot per issue.</p><p class="small"><b>Ask for rates</b></p></div>
<div class="card"><h3>Contest prize sponsor</h3><p>Brand the Scam Spotter Challenge prizes and winner posts.</p><p class="small"><b>From $253 / season</b></p></div></div>
<p class="small dim" style="margin-top:12px">Launch pricing; rates scale with traffic. We don't accept ads for products that are themselves deceptive, “recovery” services, or unlicensed financial products.</p></div></section>
<section id="inquiry"><div class="wrap"><div class="grid g2"><div><h2>Advertising inquiry</h2><p class="lead">Tell us your goals. We reply with the media kit, audience data and availability.</p></div>
<form class="form-card" data-form="ad-inquiry" data-subject="Advertising inquiry" data-done="#ad-done">
<div class="row2"><div class="f"><label for="a-n">Name</label><input id="a-n" name="name" required></div><div class="f"><label for="a-e">Work email</label><input id="a-e" name="email" type="email" required></div></div>
<div class="row2"><div class="f"><label for="a-c">Company</label><input id="a-c" name="company" required></div><div class="f"><label for="a-w">Website</label><input id="a-w" name="website" type="url" placeholder="https://"></div></div>
<div class="row2"><div class="f"><label for="a-p">Interested in</label><select id="a-p" name="placement"><option>Lookup result sponsor</option><option>Country page takeover</option><option>Sponsored guide</option><option>Tool sponsorship</option><option>Newsletter</option><option>Contest prizes</option><option>Buy / partner on the domain</option></select></div><div class="f"><label for="a-b">Budget / month</label><select id="a-b" name="budget"><option>Under $500</option><option>$500–2,000</option><option>$2,000–10,000</option><option>$10,000+</option></select></div></div>
<div class="f"><label for="a-m">Message</label><textarea id="a-m" name="message"></textarea></div>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this inquiry.</label>
<button class="btn" type="submit" style="width:100%">Send inquiry</button></form>
<div id="ad-done" class="form-card" style="display:none"><h3>✓ Thanks, we'll be in touch within one business day.</h3></div></div></div></section>''',
         crumbs=[("Advertise", None)])

    # ------------------------------------------------------------------ CAREERS
    roles = [("Community moderator (remote)", "Review scam reports, remove personal data, keep quality high. Part-time, flexible."),
             ("Native translators: Turkish, Hebrew, Korean, Japanese, Dutch", "Localise prefix pages and guides. Paid per project."),
             ("Scam-awareness writer", "Research and write clear, accurate guides. Paid per article."),
             ("Video creator / editor", "60–90 second explainers for YouTube and Shorts."),
             ("Growth & partnerships lead", "Telecom, security and fintech partnerships; revenue share."),
             ("Front-end developer (contract)", "Vanilla JS, accessibility, performance, data pipelines.")]
    rcards = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in roles)
    ropts = "".join(f"<option>{t}</option>" for t, d in roles)
    page("careers.html", "Careers at 053053: Moderators, Translators, Writers, Creators, Developers",
         "Join 053053 remotely as a moderator, translator (Turkish, Hebrew, Korean, Japanese, Dutch), writer, video creator, growth lead or developer.",
         f'''<section class="hero"><div class="wrap">{{CRUMBS}}<span class="eyebrow">👩‍💻 Careers</span><h1>Help us protect people from phone fraud</h1><p class="lead">Remote, flexible roles. Paid work, real impact.</p>
<div class="grid g3" style="margin-top:20px">{rcards}</div></div></section>
<section class="sec-alt"><div class="wrap"><div class="grid g2"><div><h2>Apply</h2><p class="lead">Tell us about yourself. We reply to every applicant.</p></div>
<form class="form-card" data-form="job-application" data-subject="Job application" data-done="#jb-done">
<div class="row2"><div class="f"><label for="j-n">Name</label><input id="j-n" name="name" required></div><div class="f"><label for="j-e">Email</label><input id="j-e" name="email" type="email" required></div></div>
<div class="row2"><div class="f"><label for="j-r">Role</label><select id="j-r" name="role" required><option value="">Choose…</option>{ropts}<option>Other / open application</option></select></div><div class="f"><label for="j-l">Languages</label><input id="j-l" name="languages" placeholder="e.g. Turkish (native), English"></div></div>
<div class="f"><label for="j-p">Portfolio / LinkedIn / CV link</label><input id="j-p" name="portfolio" type="url" placeholder="https://"></div>
<div class="f"><label for="j-m">Why you?</label><textarea id="j-m" name="message" required></textarea></div>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> I agree that my application data may be stored for 12 months for recruitment.</label>
<button class="btn" type="submit" style="width:100%">Send application</button></form>
<div id="jb-done" class="form-card" style="display:none"><h3>✓ Application received. Thank you!</h3></div></div></div></section>''',
         crumbs=[("Careers", None)])

    # ------------------------------------------------------------------ ABOUT / STORY
    page("about.html", "About 053053: Number Intelligence & Scam Shield",
         "053053 is a free, privacy-first number intelligence site that helps people decode unknown numbers, avoid phone scams and get matched with vetted protection.",
         f'''<section><div class="wrap prose">{{CRUMBS}}<span class="eyebrow">About</span><h1>We decode numbers so scammers can't hide behind them</h1>
<p class="lead">Every day, millions of people get a call from a number they don't recognise. 053053 gives them a fast, private answer, and a safe next step.</p>
<h2>What we believe</h2><ul class="check"><li><b>Privacy first.</b> Lookups run in your browser; we don't store searches or sell personal data.</li><li><b>No fake numbers.</b> We never invent reviews, reports or statistics.</li><li><b>Honest money.</b> We're funded by clearly labelled ads, referrals to vetted providers, sponsorships and donations. Referrals never change a lookup result.</li><li><b>Local depth.</b> We start with the five countries that share 053, then go wider.</li></ul>
<h2>How we make money</h2><p>Advertising (Google AdSense), referral fees from vetted providers when you ask to be matched, sponsorships, and support from people like you. <a href="donate.html">Support us</a> · <a href="advertise.html">Advertise</a>.</p>
<h2>Get in touch</h2><p><a href="contact.html">Contact us</a>, or for domain, sponsorship and partnership: <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p></div></section>''',
         crumbs=[("About", None)])

    page("the-053053-story.html", "The 053053 Story: What 053 Means Across Cultures, Countries & Clocks",
         "Why 053053? The meanings of 053 across Türkiye, Israel, South Korea, Japan, the Netherlands, India's 05:30 time zone, +53 Cuba, Chinese number slang and numerology.",
         f'''<section><div class="wrap prose">{{CRUMBS}}<span class="eyebrow">The story</span><h1>Why 053053?</h1>
<p class="lead">Most six-digit numbers mean nothing. 053053 sits where five phone systems, two time zones and a handful of number superstitions overlap.</p>
<h2>📞 A prefix shared by five countries</h2><ul><li>🇹🇷 <b>Türkiye</b>: 0530–0539, Turkcell's original mobile range</li><li>🇮🇱 <b>Israel</b>: 053, Hot Mobile (since 2014)</li><li>🇰🇷 <b>South Korea</b>: 053, Daegu</li><li>🇯🇵 <b>Japan</b>: 053, Hamamatsu</li><li>🇳🇱 <b>Netherlands</b>: 053, Enschede</li></ul>
<p>The result: whenever someone in these countries, or anyone receiving calls from them, sees “053” and wonders who it is, there's a search. That everyday question is why this site exists.</p>
<h2>🕠 A clock: 05:30 · 05:30</h2><p>Read as time, 0530 is <b>UTC+05:30</b>, shared by India and Sri Lanka: roughly one in six people on Earth.</p>
<h2>🇨🇺 A cousin: +53</h2><p>Dial <b>00 53</b> and you're calling Cuba.</p>
<h2>🀄 A playful code</h2><p>In Chinese internet slang, digits stand in for words that sound alike: 5 ≈ 我 (me), 0 ≈ 你 (you), 3 ≈ 生 (life) or 想 (miss). <b>530</b> (我想你, “I miss you”) is a well-known code. “053” can be read as “you-me-life”. That's a creative reading, not an established code. Try any number in the <a href="tools/number-meaning.html">Number Meaning tool</a>.</p>
<h2>✨ Numerology</h2><p>0+5+3+0+5+3 = 16 → 7: analysis, insight, finding the truth. Fitting for a site that decodes numbers.</p>
<p class="note">Interested in this domain or a partnership? <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></p></div></section>''',
         crumbs=[("The 053053 Story", None)])

    # ------------------------------------------------------------------ CONTACT / REMOVE
    page("contact.html", "Contact 053053",
         "Contact 053053 for support, corrections, press, partnerships and advertising.",
         f'''<section><div class="wrap">{{CRUMBS}}<div class="grid g2"><div><span class="eyebrow">Contact</span><h1>Talk to us</h1><p class="lead">We reply within 1–2 business days.</p>
<ul class="check"><li><b>Domain, sponsorship, advertising, partnership:</b> <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></li><li><b>Wrongly flagged number?</b> <a href="remove-my-number.html">Request a review</a></li><li><b>Need protection or a number?</b> <a href="get-protected.html">Free match</a></li></ul></div>
<form class="form-card" data-form="contact" data-subject="Contact form" data-done="#co-done">
<div class="row2"><div class="f"><label for="ct-n">Name</label><input id="ct-n" name="name" required autocomplete="name"></div><div class="f"><label for="ct-e">Email</label><input id="ct-e" name="email" type="email" required autocomplete="email"></div></div>
<div class="f"><label for="ct-t">Topic</label><select id="ct-t" name="topic"><option>General question</option><option>Correction to a page</option><option>Press</option><option>Partnership / domain</option><option>Advertising</option><option>Privacy request</option></select></div>
<div class="f"><label for="ct-m">Message</label><textarea id="ct-m" name="message" required></textarea></div>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> I accept the <a href="privacy.html">privacy policy</a>.</label>
<button class="btn" type="submit" style="width:100%">Send message</button></form>
<div id="co-done" class="form-card" style="display:none"><h3>✓ Message sent. We'll reply soon.</h3></div></div></div></section>''',
         noexit=True, crumbs=[("Contact", None)])

    page("remove-my-number.html", "Remove or Review My Number · 053053",
         "Is your number wrongly flagged or listed on 053053? Request a review or removal. Businesses can also respond to reports.",
         f'''<section><div class="wrap">{{CRUMBS}}<div class="grid g2"><div class="prose"><span class="eyebrow">Your number, your rights</span><h1>Remove or review my number</h1>
<p class="lead">If a report about your number is wrong, or you simply want it removed, tell us. We review every request, usually within 5 business days.</p>
<ul class="check"><li>We may ask you to verify you control the number</li><li>Businesses can add an official response instead of removal</li><li>Our lookup itself never displays personal data</li></ul>
<p>Is your business flagged as “Spam Likely” by carriers? That's a separate issue. <a href="guides/spam-likely-business-caller-id.html">Read how to fix it</a>.</p></div>
<form class="form-card" data-form="removal-request" data-subject="Number removal / review" data-done="#rm-done">
<div class="f"><label for="rm-num">Phone number</label><input id="rm-num" name="number" type="tel" required></div>
<div class="row2"><div class="f"><label for="rm-n">Your name</label><input id="rm-n" name="name" required></div><div class="f"><label for="rm-e">Email</label><input id="rm-e" name="email" type="email" required></div></div>
<div class="f"><label for="rm-r">Request</label><select id="rm-r" name="request"><option>Remove a report</option><option>Add a business response</option><option>Correct information</option></select></div>
<div class="f"><label for="rm-m">Details</label><textarea id="rm-m" name="details" required></textarea></div>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> I confirm I own or am authorised to act for this number.</label>
<button class="btn" type="submit" style="width:100%">Submit request</button></form>
<div id="rm-done" class="form-card" style="display:none"><h3>✓ Request received.</h3></div></div></div></section>''',
         noexit=True, crumbs=[("Remove my number", None)])

    # ------------------------------------------------------------------ LEGAL
    page("legal.html", "Trademark & Copyright Disclosure · 053053",
         "053053 trademark and copyright disclosure: descriptive use of the numeral 053053, no affiliation with telecom operators, nominative use of names, takedown requests.",
         f'''<section><div class="wrap prose">{{CRUMBS}}<span class="eyebrow">Legal</span><h1>Trademark &amp; copyright disclosure</h1>
<h2>The name “053053”</h2><p>“053053” is used on this website as a <b>descriptive numeral</b>: the dialling prefix 053 repeated, and the time offset 05:30. We claim <b>no trademark rights</b> in the numeral “053053”, “053”, “0530” or “+53”, and do not suggest that any of these numbers is a brand of ours. We do not use any number sequence in a way intended to cause confusion with any registered mark.</p>
<h2>No affiliation</h2><p>053053 is an independent information website. We are <b>not affiliated with, endorsed by, or sponsored by</b> Turkcell, Vodafone Türkiye, Türk Telekom, Hot Mobile, Pelephone, Cellcom, Partner, Golan Telecom, any Korean, Japanese, Dutch, Indian, Sri Lankan, Cuban, British or North American operator, any regulator, government agency or police service, or any lookup, call-blocking or numbering website referenced on this site.</p>
<h2>Nominative use</h2><p>Company, operator and government names appear only to identify the public numbering allocations or services they relate to (nominative fair use). All trademarks belong to their respective owners.</p>
<h2>Copyright</h2><p>All text, code, design and graphics on 053053 are original works © 053053, unless stated otherwise. Competitor websites were studied only for general feature patterns; no third-party text, images or code were copied. Embedded YouTube videos remain the property of their creators and are shown via YouTube's embed functionality. Numbering facts are drawn from public national numbering plans.</p>
<h2>Accuracy</h2><p>Lookups are automated, informational and may be incomplete. Number portability means operator information shows the original allocation. Nothing on this site is legal, financial or security advice.</p>
<h2>Takedown and correction</h2><p>If you believe content on this site infringes your rights or is inaccurate, please use the <a href="contact.html">contact form</a> (topic: Correction / Privacy) with details. We respond promptly.</p>
<h2>Domain &amp; partnerships</h2><p>Inquiries about this website, the domain name, sponsorship, advertising or partnership: <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p></div></section>''',
         crumbs=[("Legal", None)])

    page("privacy.html", "Privacy Policy · 053053",
         "053053 privacy policy: browser-side lookups, form data, cookies, Google AdSense, analytics, data retention and your rights (GDPR, KVKK, PIPA, DPDP, CCPA).",
         f'''<section><div class="wrap prose">{{CRUMBS}}<span class="eyebrow">Privacy</span><h1>Privacy policy</h1><p class="small dim">Effective October 2026</p>
<h2>Lookups</h2><p>The number lookup and tools run <b>entirely in your browser</b>. Numbers you type are not sent to our servers or stored by us.</p>
<h2>Forms</h2><p>When you submit a form (reports, matches, contests, donations, applications, contact), the information you enter is delivered to our team's private inbox through our form processor (FormSubmit). If you ask to be matched, we share the minimum necessary details with up to three relevant providers. We never sell your data to call centres or data brokers.</p>
<h2>Cookies &amp; advertising</h2><p>We use Google AdSense. Google and its partners use cookies to serve ads based on your prior visits to this and other sites. You can opt out of personalised advertising at Google's Ads Settings (adssettings.google.com) or www.aboutads.info. In the EEA/UK, ads are served subject to your consent choices. We may use Google Analytics to understand aggregate traffic. Your theme choice is saved in your browser's local storage.</p>
<h2>Retention</h2><p>Lead and contact data is kept for up to 24 months, job applications 12 months, unless you ask us to delete it sooner.</p>
<h2>Your rights</h2><p>Depending on where you live (e.g. GDPR, UK GDPR, Türkiye's KVKK, Israel's Privacy Protection Law, Korea's PIPA, Japan's APPI, India's DPDP Act, CCPA/CPRA), you may access, correct, delete or object to processing of your data, and withdraw consent. Use the <a href="contact.html">contact form</a> (topic: Privacy request).</p>
<h2>Children</h2><p>This site is not directed to children under 13 and we do not knowingly collect their data.</p>
<h2>Changes</h2><p>We'll update this page and its date when the policy changes.</p></div></section>''',
         crumbs=[("Privacy", None)])

    page("terms.html", "Terms of Use · 053053",
         "053053 terms of use: informational lookups, community reports, contest rules, donations and limitation of liability.",
         f'''<section><div class="wrap prose">{{CRUMBS}}<span class="eyebrow">Terms</span><h1>Terms of use</h1><p class="small dim">Effective October 2026</p>
<h2>1. Information only</h2><p>053053 provides automated, informational analysis of phone numbers based on public numbering plans. It does not identify subscribers and is not a guarantee of who is calling. Do not rely on it as your only safeguard.</p>
<h2>2. Community reports</h2><p>You may submit reports only about your own genuine experiences. Do not include anyone's personal data, defamatory statements or false information. We moderate, edit or reject reports at our discretion and may publish approved content under your pseudonym.</p>
<h2>3. Matching service</h2><p>Provider matches are introductions only. Agreements you make with providers are between you and them. We may receive referral fees. We never guarantee recovery of lost funds, and you should be wary of anyone who does.</p>
<h2>4. Contests</h2><p>No purchase necessary. Entrants must be 18+ (or have guardian consent) and submit original work. Prizes, eligibility and dates are as published for each round; we may cancel or modify a round where required by law. Winners may need to verify identity. Void where prohibited.</p>
<h2>5. Donations</h2><p>Donations are voluntary, non-refundable except where required by law, and not tax-deductible. They fund operations, moderation, translations, promotion, hiring and prizes.</p>
<h2>6. Acceptable use</h2><p>No scraping at abusive rates, no use of the site to harass anyone, no attempts to misuse forms.</p>
<h2>7. Liability</h2><p>The site is provided “as is”. To the extent permitted by law, 053053 is not liable for losses arising from use of the site or reliance on its content.</p>
<h2>8. Contact</h2><p>Questions: <a href="contact.html">contact form</a>. Domain and partnerships: <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p></div></section>''',
         crumbs=[("Terms", None)])

    page("404.html", "Page not found · 053053", "This page doesn't exist. Decode a number or explore 053 codes instead.",
         f'''<section class="hero"><div class="wrap tc"><span class="eyebrow">404</span><h1>This number is not in service.</h1><p class="lead" style="margin:0 auto 20px">The page you dialled doesn't exist. Try one of these instead.</p>
<p><a class="btn" href="{R}index.html">Home</a> <a class="btn ghost" href="{R}lookup.html">Number lookup</a> <a class="btn ghost" href="{R}codes/index.html">053 codes</a></p></div></section>''', noexit=True)
