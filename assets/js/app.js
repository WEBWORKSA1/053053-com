/* 053053 — UI, theme, forms, ads, video, donations, lead modal */
(function () {
  "use strict";
  var S = window.SITE || {};
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} },
    lget: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    lset: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var root = document.body.getAttribute("data-root") || "";

  /* ---------- lead modal markup (injected once, keeps pages light) ---------- */
  if (!document.getElementById("lead-modal")) {
    var md = document.createElement("div");
    md.innerHTML = '<div class="modal" id="lead-modal" role="dialog" aria-modal="true" aria-labelledby="lm-h"><div class="form-card"><button class="x" aria-label="Close">×</button><span class="eyebrow">Free · 60 seconds</span><h2 id="lm-h" style="font-size:1.5rem">Before you go: want to stop spam calls for good, or get a local number abroad?</h2><form data-form="lead-quick" data-subject="Quick lead (modal)"><div class="row2"><div class="f"><label for="lm-n">Name</label><input id="lm-n" name="name" required autocomplete="name"></div><div class="f"><label for="lm-e">Email</label><input id="lm-e" type="email" name="email" required autocomplete="email"></div></div><div class="row2"><div class="f"><label for="lm-p">Phone / WhatsApp (optional)</label><input id="lm-p" name="phone" type="tel" autocomplete="tel"></div><div class="f"><label for="lm-c">Country</label><input id="lm-c" name="country" required autocomplete="country-name"></div></div><div class="f"><label for="lm-o">What do you need?</label><select id="lm-o" name="need" required><option value="">Choose…</option><option>Block spam / scam calls</option><option>Identity-theft protection</option><option>I lost money to a scam</option><option>Business phone system / VoIP</option><option>Virtual local number (TR/IL/KR/JP/NL/IN)</option><option>Fix “Spam Likely” on my business calls</option><option>Other</option></select></div><label class="chk"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the <a href="' + root + 'privacy.html">privacy policy</a>.</label><button class="btn" type="submit" style="width:100%;margin-top:14px">Get my free match</button></form></div></div>';
    document.body.appendChild(md.firstChild);
  }

  /* ---------- theme ---------- */
  var th = store.lget("053_theme"); if (th) document.documentElement.setAttribute("data-theme", th);
  $$(".theme-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
      var nx = cur === "light" ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", nx); store.lset("053_theme", nx);
    });
  });

  /* ---------- nav ---------- */
  var mb = $(".menu-btn"), nav = $(".nav");
  if (mb && nav) {
    mb.addEventListener("click", function () {
      var o = nav.classList.toggle("open");
      mb.setAttribute("aria-expanded", o); mb.textContent = o ? "✕ Close" : "☰ Menu";
    });
  }
  var here = location.href.split(/[?#]/)[0].replace(/\/$/, "/index.html");
  $$(".nav a:not(.btn)").forEach(function (a) { if (a.href.split(/[?#]/)[0] === here) a.setAttribute("aria-current", "page"); });
  $$("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });

  /* ---------- toast ---------- */
  function toast(msg) {
    var t = $(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
    t.textContent = msg; t.classList.add("on");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("on"); }, 3800);
  }
  window.toast053 = toast;

  /* ---------- analytics ---------- */
  if (S.GA4) {
    var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + S.GA4; document.head.appendChild(g);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date()); gtag("config", S.GA4);
  }
  function track(ev, p) { if (window.gtag) gtag("event", ev, p || {}); }
  window.track053 = track;

  /* ---------- ads ---------- */
  var HOUSE = [
    ["Advertise on 053053", "Reach people checking unknown numbers in TR · IL · KR · JP · NL · IN.", "advertise.html", "See rate card"],
    ["Is your business flagged as “Spam Likely”?", "Fix caller-ID reputation and get answered again.", "for-business.html", "Fix my caller ID"],
    ["Get a local 053 number", "Virtual numbers in Turkey, Israel, Korea, Japan & the Netherlands.", "get-protected.html?need=virtual-number", "Get quotes"],
    ["Keep 053053 free", "Fund moderators, translators and Scam Spotter prizes.", "donate.html", "Support us"]
  ];
  if (S.ADSENSE_CLIENT) {
    var a = document.createElement("script"); a.async = true; a.crossOrigin = "anonymous";
    a.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + S.ADSENSE_CLIENT;
    document.head.appendChild(a);
  }
  $$(".ad .box").forEach(function (b, i) {
    var slot = S.AD_SLOTS && S.AD_SLOTS[b.getAttribute("data-slot") || "inContent"];
    if (S.ADSENSE_CLIENT && slot) {
      b.innerHTML = '<span class="k">Advertisement</span><ins class="adsbygoogle" style="display:block;width:100%" data-ad-client="' + S.ADSENSE_CLIENT + '" data-ad-slot="' + slot + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    } else {
      var h = HOUSE[i % HOUSE.length];
      b.innerHTML = '<span class="k">Sponsored · house ad</span><strong>' + h[0] + '</strong><span class="mute small">' + h[1] + '</span><a class="btn sm ghost" href="' + root + h[2] + '">' + h[3] + "</a>";
    }
  });

  /* ---------- video ---------- */
  var CURATED = [
    ["Scams", "wangiri one ring scam explained"], ["Scams", "bank impersonation phone scam how it works"],
    ["Protection", "how to block unknown callers iphone"], ["Protection", "how to block spam calls android"],
    ["Scams", "SMS delivery phishing scam explained"], ["Scams", "tech support scam call explained"],
    ["Travel", "how to call turkey from abroad"], ["Travel", "how to call south korea from abroad"],
    ["Time", "why india time zone is half an hour"], ["Business", "why business calls show spam likely"],
    ["Protection", "how to spot a phishing text"], ["Scams", "crypto investment scam phone call"]
  ];
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  window.esc053 = esc;
  function lite(el, id, title) {
    el.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    el.setAttribute("aria-label", "Play: " + title);
    el.addEventListener("click", function () {
      el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + esc(title) + '" allow="accelerometer;autoplay;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>';
      track("video_play", { id: id });
    }, { once: true });
  }
  $$("[data-videos]").forEach(function (box) {
    var n = parseInt(box.getAttribute("data-videos"), 10) || 6, filt = box.getAttribute("data-topic");
    var vids = (S.VIDEOS || []).filter(function (v) { return !filt || v.topic === filt; });
    var html = "";
    if (vids.length) {
      vids.slice(0, n).forEach(function (v) {
        html += '<div class="vcard"><button class="vthumb" data-yt="' + esc(v.id) + '" data-t="' + esc(v.title || "") + '"></button><div class="b"><span class="tag">' + esc(v.topic || "Video") + "</span><h3>" + esc(v.title) + "</h3></div></div>";
      });
    } else {
      CURATED.filter(function (c) { return !filt || c[0] === filt; }).slice(0, n).forEach(function (c) {
        html += '<a class="vcard" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=' + encodeURIComponent(c[1]) + '"><div class="vph">' + c[0] + '</div><div class="b"><span class="tag">' + c[0] + "</span><h3>" + c[1].charAt(0).toUpperCase() + c[1].slice(1) + '</h3><p class="small mute">Curated YouTube search · opens in a new tab</p></div></a>';
      });
    }
    box.innerHTML = html;
    $$("[data-yt]", box).forEach(function (b) { lite(b, b.getAttribute("data-yt"), b.getAttribute("data-t")); });
  });
  $$("[data-yt-channel]").forEach(function (x) { x.href = S.YOUTUBE_CHANNEL || "https://www.youtube.com/results?search_query=phone+scam+explained"; });

  /* ---------- donations ---------- */
  var D = S.DONATE || {}, dl = $("[data-donate-links]");
  if (dl) {
    var names = { paypal: "PayPal", kofi: "Ko-fi", bmac: "Buy Me a Coffee", stripe: "Card (Stripe)", patreon: "Patreon (monthly)" }, out = "";
    Object.keys(names).forEach(function (k) { if (D[k]) out += '<a class="btn" target="_blank" rel="noopener" href="' + D[k] + '">' + names[k] + "</a> "; });
    dl.innerHTML = out || '<p class="mute">Card and PayPal buttons are being connected. Use the pledge form: we reply with a secure payment link within 24 hours.</p>';
  }
  var G = S.DONATION_GOAL;
  $$("[data-goal]").forEach(function (m) {
    if (!G) return;
    var p = Math.min(100, Math.round((G.raised / G.goal) * 100));
    m.innerHTML = '<div class="small mute" style="display:flex;justify-content:space-between;gap:10px;margin-bottom:6px"><span>' + G.label + "</span><span>$" + G.raised.toLocaleString() + " / $" + G.goal.toLocaleString() + '</span></div><div class="meter"><i style="width:' + Math.max(p, 2) + '%"></i></div>';
  });
  $$("[data-amt]").forEach(function (b) {
    b.addEventListener("click", function () {
      $$("[data-amt]").forEach(function (x) { x.classList.remove("on"); }); b.classList.add("on");
      var i = $("#pledge-amount"); if (i) { i.value = b.getAttribute("data-amt"); }
    });
  });

  /* ---------- forms ---------- */
  function addr() {
    var r = window.__r || [], k = window.__k || "", s = "";
    for (var i = 0; i < r.length; i++) s += String.fromCharCode(r[i] ^ k.charCodeAt(i % k.length));
    return s;
  }
  function params() {
    var q = new URLSearchParams(location.search), o = {};
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid"].forEach(function (k) { if (q.get(k)) o[k] = q.get(k); });
    return o;
  }
  var landing = store.get("053_landing") || location.href; store.set("053_landing", landing);
  var ref = store.get("053_ref") || document.referrer || "direct"; store.set("053_ref", ref);

  function validate(scope) {
    var ok = true, first = null;
    $$("input,select,textarea", scope).forEach(function (f) {
      if (f.closest(".hp")) return;
      f.classList.remove("err");
      var bad = false;
      if (f.required) {
        if (f.type === "checkbox") bad = !f.checked;
        else if (f.type === "radio") bad = !$$('input[name="' + f.name + '"]', scope).some(function (x) { return x.checked; });
        else bad = !f.value.trim();
      }
      if (!bad && f.type === "email" && f.value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.value)) bad = true;
      if (!bad && f.type === "tel" && f.value && !/^[+()\d\s.-]{6,}$/.test(f.value)) bad = true;
      if (!bad && f.type === "url" && f.value && !/^https?:\/\/.+\..+/.test(f.value)) bad = true;
      if (bad) { ok = false; f.classList.add("err"); if (f.type === "radio") { var o = f.closest(".opt"); if (o) o.querySelector("span").classList.add("err"); } if (!first) first = f; }
    });
    if (first) { try { first.focus(); } catch (e) {} toast("Please complete the highlighted fields."); }
    return ok;
  }

  function send(form) {
    var msg = $(".form-msg", form);
    if (!msg) { msg = document.createElement("div"); msg.className = "form-msg"; msg.setAttribute("aria-live", "polite"); form.appendChild(msg); }
    if (!validate(form)) return;
    var hp = $('input[name="_honey"]', form);
    if (hp && hp.value) return;
    var fd = new FormData(form), data = {};
    fd.forEach(function (v, k) { if (k === "_honey") return; data[k] = data[k] ? data[k] + ", " + v : v; });
    var kind = form.getAttribute("data-form") || "general";
    data._subject = "[053053] " + (form.getAttribute("data-subject") || kind) + (data.name ? " — " + data.name : "");
    data._template = "table"; data._captcha = "false";
    data.form_type = kind; data.page = location.href; data.landing = landing; data.referrer = ref;
    data.submitted = new Date().toISOString();
    var u = params(); Object.keys(u).forEach(function (k) { data[k] = u[k]; });
    var btn = $('button[type="submit"]', form); if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
    msg.className = "form-msg"; msg.textContent = "";
    fetch("https://formsubmit.co/ajax/" + addr(), {
      method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data)
    }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (!res.ok || res.j.success === "false" || res.j.success === false) throw new Error("fail");
        track("generate_lead", { form: kind });
        var done = form.getAttribute("data-done");
        if (done && $(done)) { form.style.display = "none"; $(done).style.display = "block"; $(done).scrollIntoView({ behavior: "smooth", block: "center" }); }
        else { msg.className = "form-msg ok"; msg.textContent = "✓ Received! We'll be in touch shortly."; form.reset(); }
        toast("Thanks, your submission was received.");
        document.dispatchEvent(new CustomEvent("form053:sent", { detail: { kind: kind, data: data } }));
      })
      .catch(function () { msg.className = "form-msg bad"; msg.textContent = "Couldn't send right now. Please check your connection and try again in a minute."; })
      .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn._t; } });
  }
  $$("form[data-form]").forEach(function (f) {
    if (!$('input[name="_honey"]', f)) { var h = document.createElement("div"); h.className = "hp"; h.innerHTML = '<label>Leave empty<input name="_honey" tabindex="-1" autocomplete="off"></label>'; f.prepend(h); }
    f.setAttribute("novalidate", "");
    f.addEventListener("submit", function (e) { e.preventDefault(); send(f); });
  });

  /* ---------- multi-step ---------- */
  $$("form[data-steps]").forEach(function (f) {
    var steps = $$(".fstep", f), bar = $(".progress i", f), lbl = $("[data-step-lbl]", f), cur = 0;
    function show(i) {
      steps.forEach(function (s, j) { s.classList.toggle("on", j === i); });
      cur = i; if (bar) bar.style.width = ((i + 1) / steps.length * 100) + "%";
      if (lbl) lbl.textContent = "Step " + (i + 1) + " of " + steps.length;
      track("lead_step", { step: i + 1 });
    }
    $$("[data-next]", f).forEach(function (b) { b.addEventListener("click", function () { if (validate(steps[cur])) { show(Math.min(cur + 1, steps.length - 1)); f.scrollIntoView({ behavior: "smooth", block: "start" }); } }); });
    $$("[data-prev]", f).forEach(function (b) { b.addEventListener("click", function () { show(Math.max(cur - 1, 0)); }); });
    $$(".opt input", f).forEach(function (r) { r.addEventListener("change", function () { $$(".opt span.err", f).forEach(function (s) { s.classList.remove("err"); }); }); });
    var q = new URLSearchParams(location.search);
    q.forEach(function (v, k) {
      $$('[name="' + k + '"]', f).forEach(function (el) {
        if (el.type === "radio" || el.type === "checkbox") { if (el.value.toLowerCase() === v.toLowerCase()) el.checked = true; }
        else if (el.type !== "hidden") el.value = v;
      });
    });
    show(0);
  });

  /* ---------- lead modal ---------- */
  var modal = $("#lead-modal");
  function openM() { if (!modal) return; modal.classList.add("on"); var i = $("input:not([type=hidden]):not([name=_honey])", modal); if (i) setTimeout(function () { i.focus(); }, 40); }
  function closeM() { if (modal) modal.classList.remove("on"); }
  $$("[data-open-lead]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); openM(); }); });
  if (modal) {
    $$(".x", modal).forEach(function (x) { x.addEventListener("click", closeM); });
    modal.addEventListener("click", function (e) { if (e.target === modal) closeM(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeM(); });
    if (!document.body.hasAttribute("data-no-exit")) {
      var armed = false; setTimeout(function () { armed = true; }, 15000);
      document.addEventListener("mouseout", function (e) {
        if (!armed || e.relatedTarget || e.clientY > 8 || store.get("053_exit")) return;
        store.set("053_exit", "1"); openM(); track("exit_intent");
      });
    }
  }

  /* ---------- share / copy ---------- */
  document.addEventListener("click", function (e) {
    var c = e.target.closest("[data-copy]");
    if (c) { var t = c.getAttribute("data-copy"); (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { toast("Copied " + t); }, function () { toast(t); }); }
    var s = e.target.closest("[data-share]");
    if (s) {
      var d = { title: document.title, text: s.getAttribute("data-share") || document.title, url: location.href };
      if (navigator.share) navigator.share(d).catch(function () {}); else if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(function () { toast("Link copied"); });
    }
  });
})();
