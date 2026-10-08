"""Core revenue pages: home, lookup, report, get-protected (lead gen), for-business (B2B)."""

def register(page, ad, faq, leadbox, searchbox):
    R = "{R}"

    # ------------------------------------------------------------------ HOME
    fh, fld = faq([
        ("Who is calling me from a 053 number?", "It depends on the country. 053 is Turkcell mobile in Türkiye (0530–0539), Hot Mobile in Israel, the Daegu area code in South Korea, Hamamatsu in Japan and Enschede in the Netherlands. Paste the full number into the lookup and we'll tell you which one."),
        ("Is the lookup free? Do you store my searches?", "Yes, it's free. The analysis runs entirely in your browser from public numbering plans. We do not store the numbers you search."),
        ("Can you tell me the name of the person calling?", "No. We don't sell personal data. We tell you the country, number type, original operator, local time and structural red flags, plus what other people have reported once reports are moderated."),
        ("How do I report a scam call?", "Use our <a href='report.html'>report form</a>, and also report to your country's official body. We list them on the <a href='guides/report-scams-by-country.html'>reporting-by-country guide</a>."),
        ("Why is the site called 053053?", "053 is one of the most-searched “who called me?” prefixes in the world, shared by five countries. Read <a href='the-053053-story.html'>the 053053 story</a>."),
    ])
    page("index.html", "053053: Who Called Me? Decode Any Number · 053 Prefix & Scam Shield",
         "Free number intelligence: decode any phone number or prefix (053 Türkiye, Israel, Daegu, Hamamatsu, Enschede), check scam red flags, report spam calls and get protected.",
         f'''<section class="hero"><div class="wrap">
<span class="eyebrow">Free · private · runs in your browser</span>
<h1>Who called you from <span>053</span>?<br>Decode any number in seconds.</h1>
<p class="lead">Paste a phone number or prefix. Get the country, number type, original operator, local time, red-flag check and the safest next step. Then report it so the next person is warned.</p>
{searchbox(R, autofocus=False)}
<div class="chips" aria-label="Examples"><button class="chip" data-try="053" type="button">053 (all countries)</button><button class="chip" data-try="+90 532 000 00 00" type="button">🇹🇷 +90 532…</button><button class="chip" data-try="+972 53 000 0000" type="button">🇮🇱 +972 53…</button><button class="chip" data-try="+82 53 000 0000" type="button">🇰🇷 +82 53…</button><button class="chip" data-try="+1 876 000 0000" type="button">⚠ +1 876…</button><button class="chip" data-try="+44 70 0000 0000" type="button">⚠ UK 070…</button></div>
<div id="result" class="result" aria-live="polite"></div>
<div class="stats"><div class="stat"><b>5</b><span>countries share the 053 prefix</span></div><div class="stat"><b>110+</b><span>calling codes decoded</span></div><div class="stat"><b>1.5B</b><span>people live on UTC+05:30</span></div><div class="stat"><b>0</b><span>searches stored. Ever.</span></div></div>
</div></section>
{ad("result")}
<section class="sec-alt"><div class="wrap">
<span class="eyebrow">The 053 family</span><h2>One prefix. Five countries. Millions of “who's this?” moments.</h2>
<p class="lead">053 means something different depending on where the call comes from. Pick yours.</p>
<div class="grid g3" style="margin-top:24px">
<a class="card" href="codes/053-turkey-turkcell.html"><span class="flag">🇹🇷</span><div class="pfx">0530–0539</div><h3>Türkiye · Turkcell mobile</h3><p>The country's largest mobile operator's original range. +90 53x xxx xx xx.</p></a>
<a class="card" href="codes/053-israel-hot-mobile.html"><span class="flag">🇮🇱</span><div class="pfx">053</div><h3>Israel · Hot Mobile</h3><p>Mobile prefix since 2014 (formerly 057). +972 53 xxx xxxx.</p></a>
<a class="card" href="codes/053-daegu-korea.html"><span class="flag">🇰🇷</span><div class="pfx">053</div><h3>South Korea · Daegu</h3><p>Area code for Korea's 4th-largest city. +82 53.</p></a>
<a class="card" href="codes/053-hamamatsu-japan.html"><span class="flag">🇯🇵</span><div class="pfx">053</div><h3>Japan · Hamamatsu</h3><p>Western Shizuoka's industrial and music-instrument hub. +81 53.</p></a>
<a class="card" href="codes/053-enschede-netherlands.html"><span class="flag">🇳🇱</span><div class="pfx">053</div><h3>Netherlands · Enschede</h3><p>Twente region and university city. +31 53.</p></a>
<a class="card" href="codes/utc-0530-india-sri-lanka.html"><span class="flag">🇮🇳🇱🇰</span><div class="pfx">05:30</div><h3>UTC+05:30 · India &amp; Sri Lanka</h3><p>The half-hour time zone of 1.5 billion people.</p></a>
</div>
<h3 style="margin-top:40px">Right now across the 053 world</h3>
<div class="grid g4" data-clocks style="margin-top:14px"></div>
</div></section>
<section><div class="wrap">
<div class="grid g2" style="align-items:center">
<div><span class="eyebrow">Get protected</span><h2>Stop scam calls and get help fast</h2>
<p class="lead">Tell us what happened or what you need. We match you with vetted providers, from call-blocking and identity protection to licensed fraud help and virtual local numbers.</p>
<ul class="check"><li>Free, 60-second form, no obligation</li><li>Up to 3 vetted options, never sold to robocallers</li><li>Business? Fix “Spam Likely” and get answered again</li></ul>
<a class="btn" href="get-protected.html">Start my free match</a> <a class="btn ghost" href="for-business.html">I'm a business</a></div>
<div class="steps"><div class="card"><h3>Decode</h3><p>Look up the number: country, type, operator, local time, red flags.</p></div><div class="card"><h3>Report</h3><p>Flag scams. Moderated reports warn the next person.</p></div><div class="card"><h3>Protect</h3><p>Get matched with blocking, identity and business-phone providers.</p></div></div>
</div></div></section>
{ad()}
<section class="sec-alt"><div class="wrap">
<span class="eyebrow">Free tools</span><h2>Number tools people bookmark</h2>
<div class="grid g4" style="margin-top:20px">
<a class="card" href="lookup.html"><span class="ic">🔎</span><h3>Number Lookup</h3><p>Decode any number worldwide.</p></a>
<a class="card" href="tools/ist-call-planner.html"><span class="ic">🕠</span><h3>IST Call Planner</h3><p>Find the best time to call India or Sri Lanka.</p></a>
<a class="card" href="tools/number-meaning.html"><span class="ic">✨</span><h3>Number Meaning</h3><p>Chinese sound-alikes, numerology, angel numbers.</p></a>
<a class="card" href="tools/scam-quiz.html"><span class="ic">🧠</span><h3>Scam IQ Quiz</h3><p>10 questions. Can you spot every trick?</p></a>
<a class="card" href="tools/bulk-formatter.html"><span class="ic">📋</span><h3>Bulk E.164 Formatter</h3><p>Clean up to 500 numbers into CSV.</p></a>
<a class="card" href="report.html"><span class="ic">⚑</span><h3>Report a Number</h3><p>Warn others about scam callers.</p></a>
<a class="card" href="guides/wangiri-one-ring-scam.html"><span class="ic">📵</span><h3>One-Ring Scam Guide</h3><p>Why you must never call back.</p></a>
<a class="card" href="videos.html"><span class="ic">▶️</span><h3>Video Explainers</h3><p>Scams, blocking and calling tips.</p></a>
</div></div></section>
<section><div class="wrap">
<div class="cta-band"><div class="grid g2" style="align-items:center"><div><span class="eyebrow" style="color:#7ff5df">Monthly contest</span><h2>Scam Spotter Challenge 🏆</h2><p>Spot and report real scam patterns, explain them clearly and win prizes. Sponsors welcome.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn amb" href="contests.html">Enter this month</a><a class="btn ghost" style="color:#fff" href="contests.html#sponsor">Sponsor a prize</a></div></div></div>
</div></section>
<section class="sec-alt"><div class="wrap"><div class="layout"><div>
<span class="eyebrow">FAQ</span><h2>Common questions</h2>{fh}</div>
<aside class="side"><div class="card"><h3>Keep 053053 free</h3><p>Lookups are free and private. Support pays for moderators, translators and prizes.</p><div data-goal style="margin:14px 0"></div><a class="btn sm" href="donate.html">Support us</a></div>{ad("sidebar")}</aside>
</div></div></section>''', lookup=True, tools=True, ld=[fld])

    # ------------------------------------------------------------------ LOOKUP
    page("lookup.html", "Reverse Phone Number Lookup: Country, Operator, Local Time & Scam Flags · 053053",
         "Free reverse number lookup that runs in your browser. Decode country code, mobile or landline, original operator, local time and scam red flags for any phone number.",
         f'''<section class="hero" style="padding-bottom:30px"><div class="wrap">{{CRUMBS}}
<span class="eyebrow">Number lookup</span><h1>Decode any phone number</h1>
<p class="lead">Works with any format: <code>+90 532 123 45 67</code>, <code>0090…</code>, <code>(053) 123-4567</code>, <code>011 44…</code>. Choose the country if you type a national number that starts with 0.</p>
{searchbox(R, autofocus=True)}
<div class="chips"><button class="chip" data-try="053" type="button">053</button><button class="chip" data-try="05321234567" data-c="TR" type="button">🇹🇷 0532…</button><button class="chip" data-try="053-123-4567" data-c="IL" type="button">🇮🇱 053-…</button><button class="chip" data-try="+31 900 123 4567" type="button">🇳🇱 0900 premium</button><button class="chip" data-try="+91 140 123 4567" type="button">🇮🇳 140 telemarketer</button></div>
<div id="result" class="result" aria-live="polite"></div></div></section>
{ad("result")}
<section class="sec-alt"><div class="wrap"><div class="layout"><div class="prose">
<h2>What this lookup tells you, and what it doesn't</h2>
<ul class="check"><li><b>Country and calling code</b> for 110+ codes, including satellite and international networks</li><li><b>Number type</b>: mobile, landline, toll-free, premium-rate, VoIP, telemarketing, personal</li><li><b>Region or original operator</b> for detailed plans: Türkiye, Israel, South Korea, Japan, Netherlands, India, Sri Lanka, UK, USA/Canada</li><li><b>Local time now</b>, and whether it's a sensible hour to call back</li><li><b>Red flags</b>: Wangiri-prone codes, Caribbean +1 tricks, premium and personal numbers, odd lengths</li><li><b>Every way of writing the number</b>, so you can search it properly</li></ul>
<p>We do <b>not</b> reveal subscriber names or addresses. Because of number portability, a mobile's operator may have changed since the range was allocated. Caller ID can be spoofed, so treat any “urgent” request for money, codes or remote access as a scam until you've verified it through an official channel you dialled yourself.</p>
<h2>Next steps after a suspicious call</h2>
<div class="steps"><div class="card"><h3>Don't call back</h3><p>Especially after one ring from abroad.</p></div><div class="card"><h3>Report it</h3><p><a href="report.html">Report here</a> and to your <a href="guides/report-scams-by-country.html">national body</a>.</p></div><div class="card"><h3>Block it</h3><p><a href="guides/block-unknown-callers.html">iPhone &amp; Android steps</a>.</p></div><div class="card"><h3>Shared details?</h3><p>Call your bank via the number on your card, then <a href="get-protected.html?need=scam-help">get help</a>.</p></div></div>
</div><aside class="side">{leadbox(R, "Stop spam calls for good", "Compare call-blocking and identity-protection options matched to your country.", "call-blocking")}{ad("sidebar")}</aside></div></div></section>''', lookup=True, tools=False, crumbs=[("Lookup", None)])

    # ------------------------------------------------------------------ REPORT
    page("report.html", "Report a Scam or Spam Phone Number · 053053",
         "Report a scam, spam or robocall number. Moderated community reports warn others about one-ring, bank impersonation, delivery and investment scams.",
         f'''<section><div class="wrap">{{CRUMBS}}<div class="layout"><div>
<span class="eyebrow">Community shield</span><h1>Report a scam number</h1>
<p class="lead">Your report is reviewed by a moderator before it's published. We never publish your email or personal details.</p>
<form class="form-card" data-form="scam-report" data-subject="Scam report" data-done="#rep-done" data-steps>
<div class="small mute" data-step-lbl></div><div class="progress"><i></i></div>
<div class="fstep"><h3>1 · The number</h3>
<div class="row2"><div class="f"><label for="r-n">Phone number (any format)</label><input id="r-n" name="number" type="tel" required placeholder="+90 532 …"></div>
<div class="f"><label for="r-cc">Country it appeared to come from</label><select id="r-cc" name="country"><option>Not sure</option><option>Türkiye</option><option>Israel</option><option>South Korea</option><option>Japan</option><option>Netherlands</option><option>India</option><option>Sri Lanka</option><option>United Kingdom</option><option>USA / Canada</option><option>Other</option></select></div></div>
<div class="row2"><div class="f"><label for="r-d">When did it happen?</label><input id="r-d" name="date" type="date" required></div>
<div class="f"><label for="r-ch">Channel</label><select id="r-ch" name="channel"><option>Phone call</option><option>Missed call / one ring</option><option>SMS / text</option><option>WhatsApp / Telegram / messenger</option><option>Voicemail</option></select></div></div>
<button class="btn" type="button" data-next>Next →</button></div>
<div class="fstep"><h3>2 · What kind of call?</h3>
<div class="opts">
<label class="opt"><input type="radio" name="call_type" value="One-ring / Wangiri" required><span>📵 One ring / Wangiri<small>Missed call to make you call back</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Bank / payment impersonation"><span>🏦 Bank impersonation<small>Asks for OTP, PIN, card</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Government / police / tax impersonation"><span>🏛️ Gov / police / tax<small>Threats, fines, arrest</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Delivery / parcel"><span>📦 Delivery / parcel<small>Fee or link to “release” package</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Investment / crypto"><span>📈 Investment / crypto<small>Guaranteed returns, mentors</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Tech support"><span>💻 Tech support<small>Wants remote access</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Telemarketing / robocall"><span>🤖 Telemarketing / robocall<small>Annoying, not necessarily fraud</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Harassment"><span>🚫 Harassment<small>Repeated, abusive</small></span></label>
<label class="opt"><input type="radio" name="call_type" value="Legit / safe"><span>✅ It was legit<small>Help clear the number</small></span></label>
</div>
<div class="f"><label for="r-s">Danger rating: <b id="r-sv">7</b>/9</label><input id="r-s" name="rating" type="range" min="1" max="9" value="7" oninput="document.getElementById('r-sv').textContent=this.value"></div>
<div class="nav-btns"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn" type="button" data-next>Next →</button></div></div>
<div class="fstep"><h3>3 · Details</h3>
<div class="row2"><div class="f"><label for="r-cn">Name / company they claimed</label><input id="r-cn" name="claimed_name" placeholder="e.g. “Bank security team”"></div>
<div class="f"><label for="r-l">Did you lose money?</label><select id="r-l" name="lost_money"><option>No</option><option>Yes</option><option>Shared details but no loss yet</option></select></div></div>
<div class="f"><label for="r-c">What happened? (no personal data, please)</label><textarea id="r-c" name="comment" required placeholder="What they said, what they asked for, any links or names used…"></textarea></div>
<div class="nav-btns"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn" type="button" data-next>Next →</button></div></div>
<div class="fstep"><h3>4 · Publish &amp; alerts</h3>
<div class="row2"><div class="f"><label for="r-p">Display name (pseudonym)</label><input id="r-p" name="pseudonym" placeholder="e.g. Ayşe from Bursa"></div>
<div class="f"><label for="r-e">Email for alerts on this number (private)</label><input id="r-e" name="email" type="email" placeholder="optional"></div></div>
<label class="chk"><input type="checkbox" name="help_requested" value="yes"> I'd like free help from vetted providers (identity protection, call-blocking, licensed fraud help).</label>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> My report is truthful and contains no one's private data. I accept the <a href="terms.html">terms</a> and <a href="privacy.html">privacy policy</a>.</label>
<div class="nav-btns"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn" type="submit">Submit report</button></div></div>
</form>
<div id="rep-done" class="form-card" style="display:none"><h2>✓ Report received, thank you</h2><p class="lead">A moderator will review it. Meanwhile:</p><ul class="check"><li>Don't call the number back. <a href="guides/block-unknown-callers.html">Block it</a>.</li><li>Shared a code or card? Call your bank now on the number printed on your card.</li><li>Also report to your <a href="guides/report-scams-by-country.html">national authority</a>.</li></ul><a class="btn amb" href="get-protected.html?need=scam-help">Get free help now</a> <a class="btn ghost" href="contests.html">Enter the Scam Spotter Challenge</a></div>
</div><aside class="side"><div class="card"><h3>How moderation works</h3><ul class="check small"><li>Every report is checked by a person before it's published</li><li>Personal data is removed</li><li>Businesses can respond or request review</li><li><a href="remove-my-number.html">Request removal</a> of a wrongly flagged number</li></ul></div>{ad("sidebar")}</aside></div></div></section>
<script>(function(){{var n=new URLSearchParams(location.search).get("number");if(n){{var i=document.getElementById("r-n");if(i)i.value=n;}}var d=document.getElementById("r-d");if(d&&!d.value)d.value=new Date().toISOString().slice(0,10);}})();</script>''', noexit=True, crumbs=[("Report", None)])

    # ------------------------------------------------------------------ GET PROTECTED (LEAD GEN)
    page("get-protected.html", "Get Protected: Free Match for Call Blocking, Identity Protection, Fraud Help & Virtual Numbers · 053053",
         "60-second free match: stop spam calls, protect your identity, get licensed help after a scam, or get a local virtual number in Türkiye, Israel, Korea, Japan, Netherlands or India.",
         f'''<section class="hero" style="padding-top:44px"><div class="wrap">{{CRUMBS}}<div class="layout"><div>
<span class="eyebrow">Free match · 60 seconds</span><h1 style="font-size:clamp(1.9rem,4.4vw,3rem)">Get protected, or get connected.</h1>
<p class="lead">Tell us what you need. We match you with up to 3 vetted providers. No spam, no robocalls, and your details are never sold to call centres.</p>
<form class="form-card" data-form="lead-main" data-subject="Lead — Get Protected" data-done="#lead-done" data-steps style="margin-top:20px">
<div class="small mute" data-step-lbl></div><div class="progress"><i></i></div>
<div class="fstep"><h3>What do you need help with?</h3>
<div class="opts">
<label class="opt"><input type="radio" name="need" value="call-blocking" required><span>📵 Stop spam &amp; scam calls<small>Call-blocking apps &amp; carrier tools</small></span></label>
<label class="opt"><input type="radio" name="need" value="identity-protection"><span>🛡️ Identity-theft protection<small>Monitoring, alerts, insurance</small></span></label>
<label class="opt"><input type="radio" name="need" value="scam-help"><span>🆘 I lost money / shared details<small>Licensed lawyers &amp; ID restoration</small></span></label>
<label class="opt"><input type="radio" name="need" value="virtual-number"><span>🌍 Virtual local number<small>TR · IL · KR · JP · NL · IN · LK</small></span></label>
<label class="opt"><input type="radio" name="need" value="business-phone"><span>☎️ Business phone / VoIP<small>Cloud PBX, call centre, porting</small></span></label>
<label class="opt"><input type="radio" name="need" value="spam-likely-fix"><span>🏷️ Fix “Spam Likely” on my calls<small>Caller-ID reputation repair</small></span></label>
<label class="opt"><input type="radio" name="need" value="esim-travel"><span>✈️ Travel eSIM / intl calling<small>Turkey, Israel, Korea, Japan, NL</small></span></label>
<label class="opt"><input type="radio" name="need" value="other"><span>💬 Something else<small>Tell us in the next step</small></span></label>
</div><button class="btn" type="button" data-next>Continue →</button></div>
<div class="fstep"><h3>A few details</h3>
<div class="row2"><div class="f"><label for="g-c">Your country</label><input id="g-c" name="country" required autocomplete="country-name"></div>
<div class="f"><label for="g-who">This is for</label><select id="g-who" name="for"><option>Me / my family</option><option>My business (1–9 people)</option><option>My business (10–49)</option><option>My business (50–249)</option><option>My business (250+)</option></select></div></div>
<div class="row2"><div class="f"><label for="g-u">Urgency</label><select id="g-u" name="urgency"><option>Right now: it's happening</option><option>This week</option><option>This month</option><option>Just researching</option></select></div>
<div class="f"><label for="g-b">Monthly budget</label><select id="g-b" name="budget"><option>Free options only</option><option>Under $10</option><option>$10–50</option><option>$50–250</option><option>$250+</option></select></div></div>
<div class="f"><label for="g-m">Anything we should know?</label><textarea id="g-m" name="message" placeholder="e.g. need a 053 Turkcell-area number forwarding to Canada; or bank called, I gave an OTP…"></textarea></div>
<div class="nav-btns"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn" type="button" data-next>Continue →</button></div></div>
<div class="fstep"><h3>Where should we send your matches?</h3>
<div class="row2"><div class="f"><label for="g-n">Full name</label><input id="g-n" name="name" required autocomplete="name"></div>
<div class="f"><label for="g-e">Email</label><input id="g-e" name="email" type="email" required autocomplete="email"></div></div>
<div class="row2"><div class="f"><label for="g-p">Phone / WhatsApp</label><input id="g-p" name="phone" type="tel" autocomplete="tel"></div>
<div class="f"><label for="g-co">Company (if business)</label><input id="g-co" name="company" autocomplete="organization"></div></div>
<div class="f"><label for="g-t">Best time to reach you</label><select id="g-t" name="contact_time"><option>Email only</option><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div>
<div class="nav-btns"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn" type="button" data-next>Continue →</button></div></div>
<div class="fstep"><h3>Last step</h3>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> I agree that 053053 and up to 3 matched providers may contact me about this request by email, phone or WhatsApp. Consent isn't a condition of any purchase. I accept the <a href="privacy.html">privacy policy</a>.</label>
<label class="chk"><input type="checkbox" name="newsletter" value="yes"> Also send me the weekly Scam Wave Alert.</label>
<p class="note small">⚠ <b>Beware of “recovery scams”.</b> Nobody can guarantee getting your money back, and legitimate help never asks for crypto or gift-card fees. We only refer to licensed professionals and official channels.</p>
<div class="nav-btns"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn amb" type="submit">Get my free matches</button></div></div>
</form>
<div id="lead-done" class="form-card" style="display:none"><h2>✓ You're matched. Check your inbox.</h2><p class="lead">We'll email your options within one business day (usually much faster).</p><ul class="check"><li>If money is at risk right now: call your bank on the number on your card</li><li>Report to your <a href="guides/report-scams-by-country.html">national authority</a></li><li>Warn others: <a href="report.html">report the number</a></li></ul></div>
</div>
<aside class="side"><div class="card"><h3>Why people use us</h3><ul class="check small"><li>Free for you. Providers pay us a referral fee</li><li>Max 3 matches, no auctions to call centres</li><li>Licensed / registered providers only</li><li>Your data is deleted on request</li></ul></div>
<div class="card"><h3>Popular right now</h3><p class="small"><a href="?need=virtual-number">🌍 Local 053 numbers in Türkiye / Israel</a><br><a href="?need=spam-likely-fix">🏷️ “Spam Likely” repair for sales teams</a><br><a href="?need=identity-protection">🛡️ Family identity protection</a></p></div>{ad("sidebar")}</aside></div></div></section>''', noexit=True, crumbs=[("Get Protected", None)])

    # ------------------------------------------------------------------ FOR BUSINESS
    page("for-business.html", "For Business: Caller-ID Reputation Repair, Local Numbers in 053 Markets, Bulk Lookups · 053053",
         "Is your company flagged as Spam Likely? Get caller-ID reputation repair, virtual local numbers in Türkiye, Israel, Korea, Japan, Netherlands & India, bulk number validation and API access.",
         f'''<section class="hero"><div class="wrap">{{CRUMBS}}
<span class="eyebrow">053053 for business</span><h1>Get your calls <span>answered</span> again.</h1>
<p class="lead">Outbound teams lose a large share of connects when carriers label their numbers “Spam Likely” or “Scam Risk”. We help fix it, and give you local presence in the markets where 053 lives.</p>
<a class="btn" href="#demo">Book a free caller-ID audit</a> <a class="btn ghost" href="tools/bulk-formatter.html">Try bulk validation</a>
</div></section>
<section class="sec-alt"><div class="wrap"><div class="grid g3">
<div class="card"><span class="ic">🏷️</span><h3>Caller-ID reputation repair</h3><p>Audit how your numbers display across major carriers and apps, register them with analytics providers, fix mislabels, and set up branded caller ID where it's available.</p></div>
<div class="card"><span class="ic">🌍</span><h3>Local numbers in 053 markets</h3><p>Türkiye, Israel, South Korea, Japan, Netherlands, India and Sri Lanka: local, mobile-style or toll-free numbers that forward to your team anywhere.</p></div>
<div class="card"><span class="ic">📋</span><h3>Bulk validation &amp; E.164</h3><p>Clean CRM lists: country, line type, premium and VoIP detection. Free browser tool now; <b>API waitlist</b> open.</p></div>
<div class="card"><span class="ic">☎️</span><h3>Cloud phone systems</h3><p>Compare VoIP / UCaaS providers for teams of 1 to 1,000+, with number porting and call-centre features.</p></div>
<div class="card"><span class="ic">🛡️</span><h3>Fraud-awareness training</h3><p>Scam-call simulations and short modules for front-line and finance teams. Includes our Scam IQ.</p></div>
<div class="card"><span class="ic">📣</span><h3>Reach scam-aware audiences</h3><p>Sponsor guides, tools and the monthly Scam Spotter Challenge. <a href="advertise.html">See the rate card</a>.</p></div>
</div></div></section>
{ad()}
<section id="demo"><div class="wrap"><div class="grid g2">
<div><span class="eyebrow">Free audit</span><h2>Book a caller-ID audit or get quotes</h2><p class="lead">A specialist replies within one business day with a plan and transparent pricing.</p>
<ul class="check"><li>Check how up to 25 of your numbers are labelled</li><li>Local number options per country</li><li>Provider shortlist with no-obligation quotes</li></ul></div>
<form class="form-card" data-form="b2b-demo" data-subject="B2B demo / quote" data-done="#b2b-done">
<div class="row2"><div class="f"><label for="b-n">Full name</label><input id="b-n" name="name" required autocomplete="name"></div><div class="f"><label for="b-e">Work email</label><input id="b-e" name="email" type="email" required autocomplete="email"></div></div>
<div class="row2"><div class="f"><label for="b-c">Company</label><input id="b-c" name="company" required autocomplete="organization"></div><div class="f"><label for="b-p">Phone</label><input id="b-p" name="phone" type="tel" autocomplete="tel"></div></div>
<div class="row2"><div class="f"><label for="b-s">Team size</label><select id="b-s" name="employees" required><option value="">Choose…</option><option>1–9</option><option>10–49</option><option>50–249</option><option>250–999</option><option>1,000+</option></select></div>
<div class="f"><label for="b-i">Main interest</label><select id="b-i" name="interest" required><option value="">Choose…</option><option>Fix Spam Likely / caller-ID reputation</option><option>Local numbers in TR/IL/KR/JP/NL/IN/LK</option><option>Business phone system / VoIP</option><option>Bulk validation / API access</option><option>Fraud-awareness training</option><option>Advertising / sponsorship</option></select></div></div>
<div class="row2"><div class="f"><label for="b-m">Markets</label><input id="b-m" name="markets" placeholder="e.g. Türkiye, Israel"></div><div class="f"><label for="b-v">Monthly outbound calls</label><select id="b-v" name="volume"><option>Under 1,000</option><option>1,000–10,000</option><option>10,000–100,000</option><option>100,000+</option></select></div></div>
<div class="f"><label for="b-t">Preferred meeting slot</label><select id="b-t" name="slot"><option>Any time</option><option>Morning (my time)</option><option>Afternoon (my time)</option><option>Evening (my time)</option></select></div>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this request and accept the <a href="privacy.html">privacy policy</a>.</label>
<button class="btn" type="submit" style="width:100%;margin-top:10px">Book my free audit</button></form>
<div id="b2b-done" class="form-card" style="display:none"><h2>✓ Request received</h2><p>We'll reply within one business day with next steps.</p></div>
</div></div></section>''', crumbs=[("For Business", None)])
