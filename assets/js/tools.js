/* 053053 — interactive tools: world-053 clocks, IST call planner, number meaning, bulk formatter, Scam IQ quiz */
(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var esc = window.esc053 || function (s) { return String(s); };
  function fmt(tz, d, opt) { try { return new Intl.DateTimeFormat("en-GB", Object.assign({ timeZone: tz, hour: "2-digit", minute: "2-digit", hour12: false }, opt || {})).format(d || new Date()); } catch (e) { return "—"; } }
  function hourIn(tz, d) { return parseInt(fmt(tz, d, { minute: undefined }), 10) % 24; }
  var userTZ = (Intl.DateTimeFormat().resolvedOptions().timeZone) || "UTC";

  /* ---------- World of 053 clock board ---------- */
  var CL = [["🇹🇷","İstanbul · Turkcell 053x","Europe/Istanbul"],["🇮🇱","Tel Aviv · Hot Mobile 053","Asia/Jerusalem"],["🇰🇷","Daegu · 053","Asia/Seoul"],["🇯🇵","Hamamatsu · 053","Asia/Tokyo"],["🇳🇱","Enschede · 053","Europe/Amsterdam"],["🇮🇳","India · UTC+05:30","Asia/Kolkata"],["🇱🇰","Sri Lanka · UTC+05:30","Asia/Colombo"],["🇨🇺","Havana · +53","America/Havana"]];
  $$("[data-clocks]").forEach(function (box) {
    function draw() {
      box.innerHTML = CL.map(function (c) {
        var h = hourIn(c[2]), st = h >= 9 && h < 18 ? ['Business hours', "b-safe"] : h >= 8 && h < 21 ? ["OK to call", "b-info"] : ["Night: don't call", "b-warn"];
        return '<div class="card" style="padding:18px"><div class="small mute">' + c[0] + " " + c[1] + '</div><div class="clock">' + fmt(c[2]) + '</div><span class="badge ' + st[1] + '">' + st[0] + "</span></div>";
      }).join("");
    }
    draw(); setInterval(draw, 30000);
  });

  /* ---------- IST / SLST call planner ---------- */
  var pl = $("#planner");
  if (pl) {
    var sel = $("[name=tz]", pl), tgtSel = $("[name=target]", pl), outp = $("#planner-out");
    var zones = []; try { zones = Intl.supportedValuesOf("timeZone"); } catch (e) { zones = ["UTC","Europe/London","Europe/Istanbul","Asia/Jerusalem","Asia/Seoul","Asia/Tokyo","Europe/Amsterdam","America/New_York","America/Toronto","America/Los_Angeles","Asia/Dubai","Asia/Singapore","Australia/Sydney","Asia/Kolkata","Asia/Colombo"]; }
    if (zones.indexOf(userTZ) === -1) zones.unshift(userTZ);
    sel.innerHTML = zones.map(function (z) { return '<option' + (z === userTZ ? " selected" : "") + ">" + z + "</option>"; }).join("");
    function offsetMin(tz, d) {
      var p = new Intl.DateTimeFormat("en-US", { timeZone: tz, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" }).formatToParts(d), o = {};
      p.forEach(function (x) { o[x.type] = x.value; });
      return (Date.UTC(+o.year, +o.month - 1, +o.day, +o.hour % 24, +o.minute) - Math.floor(d.getTime() / 60000) * 60000) / 60000;
    }
    function drawP() {
      var tz = sel.value, tg = tgtSel.value, now = new Date();
      var diff = offsetMin(tg, now) - offsetMin(tz, now), sign = diff >= 0 ? "ahead of" : "behind";
      var ad = Math.abs(diff), hh = Math.floor(ad / 60), mm = ad % 60;
      var cells = "", best = [];
      for (var h = 0; h < 24; h++) {
        var t = new Date(now); t.setUTCMinutes(0, 0, 0);
        var base = new Date(now.getTime() - (hourIn(tz, now) - h) * 3600000);
        var th = hourIn(tg, base), cls = th >= 9 && th < 18 ? "w" : th >= 8 && th < 21 ? "e" : "n";
        if (cls === "w") best.push(h);
        cells += '<i class="' + cls + (h === hourIn(tz, now) ? " now" : "") + '" title="' + String(h).padStart(2, "0") + ":00 your time → " + fmt(tg, base) + ' there"></i>';
      }
      var range = best.length ? String(best[0]).padStart(2, "0") + ":00 – " + String(best[best.length - 1] + 1).padStart(2, "0") + ":00" : "none";
      outp.innerHTML = '<div class="kv"><div><small>Your time (' + esc(tz) + ')</small><b>' + fmt(tz, now) + '</b></div><div><small>' + esc(tg) + '</small><b>' + fmt(tg, now, { weekday: "short" }) + '</b></div><div><small>Difference</small><b>' + (diff === 0 ? "Same time" : hh + "h " + (mm ? mm + "m " : "") + sign + " you") + '</b></div><div><small>Best window (your time)</small><b>' + range + '</b></div></div><div class="small mute">Your 24 hours, coloured by the other side’s clock: <span class="badge b-safe">9–18 business</span> <span class="badge b-warn">8–9 / 18–21 OK</span> <span class="badge b-info">night</span></div><div class="tl" aria-hidden="true">' + cells + '</div><div class="small dim" style="display:flex;justify-content:space-between"><span>00:00</span><span>12:00</span><span>23:00</span></div>';
    }
    sel.addEventListener("change", drawP); tgtSel.addEventListener("change", drawP); drawP(); setInterval(drawP, 60000);
  }

  /* ---------- Number meaning (cultural readings, for fun) ---------- */
  var mf = $("#meaning");
  if (mf) {
    var ZH = { "0": ["líng", "你 nǐ (you) / 零 zero"], "1": ["yī", "要 yào (want) / 一 one"], "2": ["èr", "爱 ài (love)"], "3": ["sān", "生 shēng (life) / 想 xiǎng (miss)"], "4": ["sì", "死 sǐ (death): considered unlucky"], "5": ["wǔ", "我 wǒ (I, me)"], "6": ["liù", "溜 liū (smooth, going well)"], "7": ["qī", "起 qǐ (rise) / 妻 qī (wife)"], "8": ["bā", "发 fā (prosper): luckiest"], "9": ["jiǔ", "久 jiǔ (long-lasting)"] };
    var CODES = { "520": "我爱你: I love you", "521": "我爱你: I love you (variant)", "530": "我想你: I miss you", "1314": "一生一世: forever", "5201314": "I love you forever", "88": "拜拜: bye-bye", "886": "拜拜啦: bye-bye", "666": "溜溜溜: awesome / skilful", "918": "就要发: about to prosper", "168": "一路发: prosperity all the way", "518": "我要发: I will prosper", "9420": "就是爱你: it's you I love", "1314520": "forever I love you", "748": "去死吧: rude, avoid", "250": "二百五: fool (insult)" };
    var ANG = { "0": "potential, a fresh cycle", "1": "new beginnings, initiative", "2": "balance, partnership", "3": "creativity, expression", "4": "foundations, hard work", "5": "change, freedom, movement", "6": "home, care, responsibility", "7": "insight, analysis, inner wisdom", "8": "abundance, power, money", "9": "completion, service" };
    function reduce(n) { var steps = [n]; while (n > 9 && n !== 11 && n !== 22 && n !== 33) { n = String(n).split("").reduce(function (a, b) { return a + +b; }, 0); steps.push(n); } return steps; }
    function run() {
      var d = ($("[name=num]", mf).value || "").replace(/\D/g, "").slice(0, 24), o = $("#meaning-out");
      if (!d) { o.innerHTML = '<p class="mute">Type a number, e.g. 053053, a phone number, a date or a price.</p>'; return; }
      var sum = d.split("").reduce(function (a, b) { return a + +b; }, 0), r = reduce(sum);
      var pats = [];
      if (/^(\d+)\1+$/.test(d)) pats.push("Repeating block “" + d.match(/^(\d+?)\1+$/)[1] + "”: amplified energy in angel-number folklore.");
      if (d === d.split("").reverse().join("")) pats.push("Palindrome: reads the same both ways.");
      if (/(\d)\1\1/.test(d)) pats.push("Triple digit " + d.match(/(\d)\1\1/)[0] + ": a strong ‘sign’ in angel-number culture.");
      if (/0123|1234|2345|3456|4567|5678|6789/.test(d)) pats.push("Ascending run: progress, momentum.");
      var codes = Object.keys(CODES).filter(function (k) { return d.indexOf(k) > -1; }).sort(function (a, b) { return b.length - a.length; });
      var c4 = (d.match(/4/g) || []).length, c8 = (d.match(/8/g) || []).length;
      o.innerHTML = '<div class="kv"><div><small>Digit sum</small><b>' + d.split("").join("+") + " = " + sum + '</b></div><div><small>Numerology root</small><b>' + r.join(" → ") + '</b></div><div><small>Root meaning</small><b>' + (ANG[String(r[r.length - 1]).slice(-1)] || "master number") + '</b></div><div><small>Chinese luck score</small><b>' + (c8 * 2 - c4 * 2 + (d.match(/[69]/g) || []).length) + ' <span class="small mute">(8s up, 4s down)</span></b></div></div>' +
        (pats.length ? '<h4>Patterns</h4><ul class="check">' + pats.map(function (p) { return "<li>" + esc(p) + "</li>"; }).join("") + "</ul>" : "") +
        (codes.length ? '<h4>Chinese number-slang codes inside</h4><ul class="check">' + codes.map(function (k) { return "<li><b>" + k + "</b>: " + CODES[k] + "</li>"; }).join("") + "</ul>" : "") +
        '<h4>Digit by digit (Mandarin sound-alikes)</h4><div class="tscroll"><table class="tbl"><tr><th>Digit</th><th>Mandarin</th><th>Sounds like</th><th>Angel-number theme</th></tr>' + d.split("").slice(0, 12).map(function (x) { return "<tr><td><b>" + x + "</b></td><td>" + ZH[x][0] + "</td><td>" + ZH[x][1] + "</td><td>" + ANG[x] + "</td></tr>"; }).join("") + "</table></div>" +
        '<p class="small dim" style="margin-top:10px">Cultural folklore for entertainment. Numerology has no scientific basis.</p>';
    }
    mf.addEventListener("submit", function (e) { e.preventDefault(); run(); }); $("[name=num]", mf).addEventListener("input", run); run();
  }

  /* ---------- Bulk E.164 formatter ---------- */
  var bf = $("#bulk");
  if (bf && window.N053) {
    bf.addEventListener("submit", function (e) {
      e.preventDefault();
      var lines = $("[name=list]", bf).value.split(/\n+/).map(function (s) { return s.trim(); }).filter(Boolean).slice(0, 500), c = $("[name=country]", bf).value, rows = [], csv = ["input,e164,country,type,region"];
      lines.forEach(function (l) {
        var r = window.N053.analyze(l, c);
        if (r.cc) { rows.push([l, r.e164, r.cc.name, (window.N053.TYPE[r.info.type] || [r.info.type])[0], r.info.region]); }
        else rows.push([l, "—", r.family ? "053 family: choose a country" : r.needCountry ? "choose a country" : (r.error || "?"), "", ""]);
      });
      rows.forEach(function (r) { csv.push(r.map(function (x) { return '"' + String(x).replace(/"/g, '""') + '"'; }).join(",")); });
      $("#bulk-out").innerHTML = '<p><b>' + rows.length + '</b> numbers processed. <button class="btn sm" type="button" id="dl-csv">Download CSV</button> <button class="btn sm ghost" type="button" data-copy="' + esc(rows.map(function (r) { return r[1]; }).join("\n")) + '">Copy E.164 list</button></p><div class="tscroll"><table class="tbl"><tr><th>Input</th><th>E.164</th><th>Country</th><th>Type</th><th>Region</th></tr>' + rows.map(function (r) { return "<tr>" + r.map(function (x) { return "<td>" + esc(x) + "</td>"; }).join("") + "</tr>"; }).join("") + "</table></div>";
      $("#dl-csv").addEventListener("click", function () { var b = new Blob([csv.join("\n")], { type: "text/csv" }), a = document.createElement("a"); a.href = URL.createObjectURL(b); a.download = "053053-e164.csv"; a.click(); });
    });
  }

  /* ---------- Scam IQ quiz ---------- */
  var qz = $("#quiz");
  if (qz) {
    var Q = [
      ["You get one ring from +222 (Mauritania) and it stops. Best move?", ["Call back to see who it was", "Ignore it, don't call back", "Text them asking who they are"], 1, "One-ring (Wangiri) scams want you to call back a premium international line."],
      ["Your “bank” calls and asks for the one-time code they just sent you. You should…", ["Read it out, since they're the bank", "Hang up and call the number on your card", "Give only half the code"], 1, "Banks never ask for OTPs. Hang up and call the official number yourself."],
      ["A text says a parcel is held for a €1.99 fee with a link. It's most likely…", ["A real customs charge", "Delivery phishing (smishing)", "A loyalty reward"], 1, "Tiny ‘fees’ are bait to steal full card details."],
      ["Caller ID shows your own bank's real number. That proves…", ["It's definitely the bank", "Nothing: caller ID can be spoofed", "It's a recorded message"], 1, "Spoofing lets scammers display any number."],
      ["“This is the tax office: pay now in gift cards or you'll be arrested.”", ["Pay to be safe", "Scam: agencies never take gift cards", "Ask for a discount"], 1, "Gift cards, crypto or wire = scam, every time."],
      ["A +1 876 number leaves a voicemail saying you won a prize. +1 876 is…", ["A US toll-free number", "Jamaica: international charges apply", "Canada"], 1, "Several Caribbean codes use +1 and look domestic."],
      ["An investment ‘mentor’ on WhatsApp shows huge crypto gains and wants you to deposit. Red flag?", ["No, screenshots prove it", "Yes, it's classic ‘pig-butchering’", "Only if they're foreign"], 1, "Fake dashboards are part of the script."],
      ["After a scam, someone offers to ‘recover your funds’ for an upfront fee. This is…", ["A lucky break", "Often a second ‘recovery scam’", "Required by law"], 1, "Use police, your bank and licensed lawyers only."],
      ["The safest way to verify an unexpected caller is to…", ["Ask them to prove it", "Hang up and call back via an official number", "Ask for their employee ID"], 1, "Control the channel: you dial, from a source you trust."],
      ["A tech-support caller says your PC is infected and asks to install remote software. You…", ["Install it quickly", "Hang up: unsolicited tech support is a scam", "Let them in for 5 minutes"], 1, "Remote access hands over your bank sessions."]
    ];
    var i = 0, score = 0, box = $("#quiz-box");
    function draw() {
      if (i >= Q.length) {
        var lvl = score >= 9 ? "Scam Shield Master 🛡️" : score >= 7 ? "Sharp Spotter" : score >= 5 ? "Getting there" : "At risk: read our guides";
        box.innerHTML = '<h3>You scored ' + score + "/" + Q.length + '</h3><p class="lead">' + lvl + '</p><div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn" type="button" data-share="I scored ' + score + '/10 on the 053053 Scam IQ test. Can you beat me?">Share your score</button><a class="btn ghost" href="../contests.html">Enter the Scam Spotter Challenge</a><button class="btn ghost" type="button" id="qz-again">Try again</button></div>';
        $("#qz-again").addEventListener("click", function () { i = 0; score = 0; draw(); });
        if (window.track053) window.track053("quiz_done", { score: score });
        return;
      }
      var q = Q[i];
      box.innerHTML = '<div class="small mute">Question ' + (i + 1) + " of " + Q.length + ' · Score ' + score + '</div><div class="progress"><i style="width:' + ((i) / Q.length * 100) + '%"></i></div><h3>' + q[0] + "</h3>" + q[1].map(function (o, j) { return '<button class="q-opt" type="button" data-j="' + j + '">' + o + "</button>"; }).join("") + '<p id="qz-exp" class="mute" aria-live="polite"></p>';
      $$(".q-opt", box).forEach(function (b) {
        b.addEventListener("click", function () {
          var j = +b.getAttribute("data-j");
          $$(".q-opt", box).forEach(function (x) { x.disabled = true; if (+x.getAttribute("data-j") === q[2]) x.classList.add("right"); });
          if (j === q[2]) score++; else b.classList.add("wrong");
          $("#qz-exp").innerHTML = (j === q[2] ? "✓ Correct. " : "✗ Not quite. ") + q[3] + ' <br><button class="btn sm" type="button" id="qz-next" style="margin-top:10px">Next →</button>';
          $("#qz-next").addEventListener("click", function () { i++; draw(); }); $("#qz-next").focus();
        });
      });
    }
    draw();
  }
})();
