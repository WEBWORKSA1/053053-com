/* 053053 — client-side number intelligence engine (no data leaves the browser) */
(function () {
  "use strict";
  /* [calling code, country, flag, IANA tz, ISO] */
  var CC = [
    ["1","USA / Canada / Caribbean (NANP)","🇺🇸","America/New_York","US"],["7","Russia / Kazakhstan","🇷🇺","Europe/Moscow","RU"],["20","Egypt","🇪🇬","Africa/Cairo","EG"],["27","South Africa","🇿🇦","Africa/Johannesburg","ZA"],
    ["30","Greece","🇬🇷","Europe/Athens","GR"],["31","Netherlands","🇳🇱","Europe/Amsterdam","NL"],["32","Belgium","🇧🇪","Europe/Brussels","BE"],["33","France","🇫🇷","Europe/Paris","FR"],["34","Spain","🇪🇸","Europe/Madrid","ES"],
    ["36","Hungary","🇭🇺","Europe/Budapest","HU"],["39","Italy","🇮🇹","Europe/Rome","IT"],["40","Romania","🇷🇴","Europe/Bucharest","RO"],["41","Switzerland","🇨🇭","Europe/Zurich","CH"],["43","Austria","🇦🇹","Europe/Vienna","AT"],
    ["44","United Kingdom","🇬🇧","Europe/London","GB"],["45","Denmark","🇩🇰","Europe/Copenhagen","DK"],["46","Sweden","🇸🇪","Europe/Stockholm","SE"],["47","Norway","🇳🇴","Europe/Oslo","NO"],["48","Poland","🇵🇱","Europe/Warsaw","PL"],
    ["49","Germany","🇩🇪","Europe/Berlin","DE"],["51","Peru","🇵🇪","America/Lima","PE"],["52","Mexico","🇲🇽","America/Mexico_City","MX"],["53","Cuba","🇨🇺","America/Havana","CU"],["54","Argentina","🇦🇷","America/Argentina/Buenos_Aires","AR"],
    ["55","Brazil","🇧🇷","America/Sao_Paulo","BR"],["56","Chile","🇨🇱","America/Santiago","CL"],["57","Colombia","🇨🇴","America/Bogota","CO"],["58","Venezuela","🇻🇪","America/Caracas","VE"],["60","Malaysia","🇲🇾","Asia/Kuala_Lumpur","MY"],
    ["61","Australia","🇦🇺","Australia/Sydney","AU"],["62","Indonesia","🇮🇩","Asia/Jakarta","ID"],["63","Philippines","🇵🇭","Asia/Manila","PH"],["64","New Zealand","🇳🇿","Pacific/Auckland","NZ"],["65","Singapore","🇸🇬","Asia/Singapore","SG"],
    ["66","Thailand","🇹🇭","Asia/Bangkok","TH"],["81","Japan","🇯🇵","Asia/Tokyo","JP"],["82","South Korea","🇰🇷","Asia/Seoul","KR"],["84","Vietnam","🇻🇳","Asia/Ho_Chi_Minh","VN"],["86","China","🇨🇳","Asia/Shanghai","CN"],
    ["90","Türkiye","🇹🇷","Europe/Istanbul","TR"],["91","India","🇮🇳","Asia/Kolkata","IN"],["92","Pakistan","🇵🇰","Asia/Karachi","PK"],["93","Afghanistan","🇦🇫","Asia/Kabul","AF"],["94","Sri Lanka","🇱🇰","Asia/Colombo","LK"],
    ["95","Myanmar","🇲🇲","Asia/Yangon","MM"],["98","Iran","🇮🇷","Asia/Tehran","IR"],["212","Morocco","🇲🇦","Africa/Casablanca","MA"],["213","Algeria","🇩🇿","Africa/Algiers","DZ"],["216","Tunisia","🇹🇳","Africa/Tunis","TN"],
    ["218","Libya","🇱🇾","Africa/Tripoli","LY"],["220","Gambia","🇬🇲","Africa/Banjul","GM"],["221","Senegal","🇸🇳","Africa/Dakar","SN"],["222","Mauritania","🇲🇷","Africa/Nouakchott","MR"],["225","Côte d’Ivoire","🇨🇮","Africa/Abidjan","CI"],
    ["233","Ghana","🇬🇭","Africa/Accra","GH"],["234","Nigeria","🇳🇬","Africa/Lagos","NG"],["243","DR Congo","🇨🇩","Africa/Kinshasa","CD"],["251","Ethiopia","🇪🇹","Africa/Addis_Ababa","ET"],["252","Somalia","🇸🇴","Africa/Mogadishu","SO"],
    ["254","Kenya","🇰🇪","Africa/Nairobi","KE"],["255","Tanzania","🇹🇿","Africa/Dar_es_Salaam","TZ"],["256","Uganda","🇺🇬","Africa/Kampala","UG"],["263","Zimbabwe","🇿🇼","Africa/Harare","ZW"],["351","Portugal","🇵🇹","Europe/Lisbon","PT"],
    ["352","Luxembourg","🇱🇺","Europe/Luxembourg","LU"],["353","Ireland","🇮🇪","Europe/Dublin","IE"],["354","Iceland","🇮🇸","Atlantic/Reykjavik","IS"],["355","Albania","🇦🇱","Europe/Tirane","AL"],["357","Cyprus","🇨🇾","Asia/Nicosia","CY"],
    ["358","Finland","🇫🇮","Europe/Helsinki","FI"],["359","Bulgaria","🇧🇬","Europe/Sofia","BG"],["370","Lithuania","🇱🇹","Europe/Vilnius","LT"],["371","Latvia","🇱🇻","Europe/Riga","LV"],["372","Estonia","🇪🇪","Europe/Tallinn","EE"],
    ["373","Moldova","🇲🇩","Europe/Chisinau","MD"],["374","Armenia","🇦🇲","Asia/Yerevan","AM"],["375","Belarus","🇧🇾","Europe/Minsk","BY"],["380","Ukraine","🇺🇦","Europe/Kyiv","UA"],["381","Serbia","🇷🇸","Europe/Belgrade","RS"],
    ["385","Croatia","🇭🇷","Europe/Zagreb","HR"],["420","Czechia","🇨🇿","Europe/Prague","CZ"],["421","Slovakia","🇸🇰","Europe/Bratislava","SK"],["852","Hong Kong","🇭🇰","Asia/Hong_Kong","HK"],["853","Macau","🇲🇴","Asia/Macau","MO"],
    ["855","Cambodia","🇰🇭","Asia/Phnom_Penh","KH"],["856","Laos","🇱🇦","Asia/Vientiane","LA"],["870","Inmarsat (satellite)","🛰️","UTC","XS"],["881","Global satellite services","🛰️","UTC","XS"],["882","International Networks","🌐","UTC","XN"],
    ["883","International Networks","🌐","UTC","XN"],["880","Bangladesh","🇧🇩","Asia/Dhaka","BD"],["886","Taiwan","🇹🇼","Asia/Taipei","TW"],["960","Maldives","🇲🇻","Indian/Maldives","MV"],["961","Lebanon","🇱🇧","Asia/Beirut","LB"],
    ["962","Jordan","🇯🇴","Asia/Amman","JO"],["963","Syria","🇸🇾","Asia/Damascus","SY"],["964","Iraq","🇮🇶","Asia/Baghdad","IQ"],["965","Kuwait","🇰🇼","Asia/Kuwait","KW"],["966","Saudi Arabia","🇸🇦","Asia/Riyadh","SA"],
    ["967","Yemen","🇾🇪","Asia/Aden","YE"],["968","Oman","🇴🇲","Asia/Muscat","OM"],["970","Palestine","🇵🇸","Asia/Hebron","PS"],["971","United Arab Emirates","🇦🇪","Asia/Dubai","AE"],["972","Israel","🇮🇱","Asia/Jerusalem","IL"],
    ["973","Bahrain","🇧🇭","Asia/Bahrain","BH"],["974","Qatar","🇶🇦","Asia/Qatar","QA"],["975","Bhutan","🇧🇹","Asia/Thimphu","BT"],["977","Nepal","🇳🇵","Asia/Kathmandu","NP"],["994","Azerbaijan","🇦🇿","Asia/Baku","AZ"],
    ["995","Georgia","🇬🇪","Asia/Tbilisi","GE"],["998","Uzbekistan","🇺🇿","Asia/Tashkent","UZ"]
  ];
  var byCC = {}; CC.forEach(function (c) { byCC[c[0]] = { cc: c[0], name: c[1], flag: c[2], tz: c[3], iso: c[4] }; });

  /* Codes frequently reported in one-ring (Wangiri) / premium call-back campaigns */
  var WANGIRI = ["216","222","225","234","243","252","370","371","373","375","381","882","883","881","870","960","220","221"];
  var NANP_RISK = { "268":"Antigua & Barbuda","284":"British Virgin Islands","473":"Grenada","649":"Turks & Caicos","664":"Montserrat","767":"Dominica","809":"Dominican Republic","829":"Dominican Republic","849":"Dominican Republic","876":"Jamaica","658":"Jamaica","869":"St Kitts & Nevis","758":"St Lucia","784":"St Vincent","441":"Bermuda","246":"Barbados","242":"Bahamas" };
  var NANP_CITY = { "212":"New York City, NY","646":"New York City, NY","718":"New York City, NY","213":"Los Angeles, CA","310":"Los Angeles, CA","312":"Chicago, IL","415":"San Francisco, CA","202":"Washington, DC","305":"Miami, FL","713":"Houston, TX","214":"Dallas, TX","617":"Boston, MA","206":"Seattle, WA","404":"Atlanta, GA","702":"Las Vegas, NV","514":"Montréal, QC","438":"Montréal, QC","416":"Toronto, ON","647":"Toronto, ON","604":"Vancouver, BC","403":"Calgary, AB","613":"Ottawa, ON" };

  /* National plans: [prefix (NSN, no trunk 0), type, region/operator, extra note] — longest prefix wins */
  var PLAN = {
    TR: { trunk: "0", len: [10, 7], rules: [
      ["50","mobile","Türk Telekom (original allocation)"],["53","mobile","Turkcell (original allocation, 0530–0539)","053x"],["54","mobile","Vodafone Türkiye (original allocation)"],["55","mobile","Türk Telekom (original allocation)"],["56","mobile","Mobile range"],
      ["212","geographic","İstanbul (European side)"],["216","geographic","İstanbul (Asian side)"],["312","geographic","Ankara"],["232","geographic","İzmir"],["242","geographic","Antalya"],["224","geographic","Bursa"],["322","geographic","Adana"],["2","geographic","Western Türkiye landline"],["3","geographic","Central Türkiye landline"],["4","geographic","Eastern Türkiye landline"],
      ["444","business","Nationwide business number (444)"],["800","tollfree","Toll-free (0800)"],["850","business","Non-geographic / corporate (0850)"],["900","premium","Premium-rate (0900)"]] },
    IL: { trunk: "0", len: [9, 8], rules: [
      ["50","mobile","Pelephone"],["51","mobile","wecom"],["52","mobile","Cellcom"],["53","mobile","Hot Mobile (053, previously 057)","053"],["54","mobile","Partner"],["55","mobile","Various MVNOs"],["58","mobile","Golan Telecom"],["56","mobile","Ooredoo Palestine"],["59","mobile","Jawwal (Palestine)"],
      ["2","geographic","Jerusalem District"],["3","geographic","Tel Aviv & Central District"],["4","geographic","Haifa & Northern District"],["8","geographic","Lowland & Southern District"],["9","geographic","Sharon area"],
      ["72","voip","VoIP / non-geographic"],["73","voip","VoIP / non-geographic"],["74","voip","VoIP / non-geographic"],["76","voip","VoIP / non-geographic"],["77","voip","VoIP / non-geographic"],["78","voip","VoIP / non-geographic"],["79","voip","VoIP / non-geographic"],["1800","tollfree","Toll-free (1-800)"],["1700","business","Shared-cost (1-700)"]] },
    KR: { trunk: "0", len: [9, 10, 8], rules: [
      ["10","mobile","Mobile (010)"],["2","geographic","Seoul"],["31","geographic","Gyeonggi-do"],["32","geographic","Incheon"],["33","geographic","Gangwon"],["41","geographic","Chungcheongnam-do"],["42","geographic","Daejeon"],["43","geographic","Chungcheongbuk-do"],["44","geographic","Sejong"],
      ["51","geographic","Busan"],["52","geographic","Ulsan"],["53","geographic","Daegu Metropolitan City","053"],["54","geographic","Gyeongsangbuk-do"],["55","geographic","Gyeongsangnam-do"],["61","geographic","Jeollanam-do"],["62","geographic","Gwangju"],["63","geographic","Jeollabuk-do"],["64","geographic","Jeju"],
      ["70","voip","Internet phone (070)"],["80","tollfree","Toll-free (080)"],["15","business","Nationwide representative number (15xx)"],["16","business","Nationwide representative number (16xx)"]] },
    JP: { trunk: "0", len: [9, 10], rules: [
      ["90","mobile","Mobile (090)"],["80","mobile","Mobile (080)"],["70","mobile","Mobile / PHS (070)"],["50","voip","IP phone (050)"],["120","tollfree","Toll-free Freedial (0120)"],["800","tollfree","Toll-free (0800)"],["570","business","Navi Dial shared-cost (0570)"],
      ["3","geographic","Tokyo (23 wards)"],["6","geographic","Osaka"],["52","geographic","Nagoya"],["53","geographic","Hamamatsu & western Shizuoka","053"],["54","geographic","Shizuoka"],["45","geographic","Yokohama"],["75","geographic","Kyoto"],["78","geographic","Kobe"],["92","geographic","Fukuoka"],["11","geographic","Sapporo"],["22","geographic","Sendai"],["82","geographic","Hiroshima"]] },
    NL: { trunk: "0", len: [9], rules: [
      ["6","mobile","Mobile (06)"],["20","geographic","Amsterdam"],["10","geographic","Rotterdam"],["70","geographic","The Hague"],["30","geographic","Utrecht"],["40","geographic","Eindhoven"],["50","geographic","Groningen"],["53","geographic","Enschede & Twente","053"],["74","geographic","Hengelo"],
      ["85","voip","Non-geographic / VoIP (085)"],["88","business","Company number (088)"],["800","tollfree","Toll-free (0800)"],["900","premium","Premium-rate (0900)"],["906","premium","Premium-rate (0906)"],["909","premium","Premium-rate (0909)"]] },
    IN: { trunk: "0", len: [10], rules: [
      ["6","mobile","Mobile"],["7","mobile","Mobile"],["8","mobile","Mobile"],["9","mobile","Mobile"],["11","geographic","Delhi"],["22","geographic","Mumbai"],["33","geographic","Kolkata"],["44","geographic","Chennai"],["80","geographic","Bengaluru"],["40","geographic","Hyderabad"],["20","geographic","Pune"],["79","geographic","Ahmedabad"],
      ["140","telemarketing","Registered telemarketing series (140)"],["1800","tollfree","Toll-free (1800)"]] },
    LK: { trunk: "0", len: [9], rules: [
      ["70","mobile","Mobile"],["71","mobile","Mobile"],["72","mobile","Mobile"],["74","mobile","Mobile"],["75","mobile","Mobile"],["76","mobile","Mobile"],["77","mobile","Mobile"],["78","mobile","Mobile"],
      ["11","geographic","Colombo"],["31","geographic","Negombo / Gampaha"],["81","geographic","Kandy"],["91","geographic","Galle"],["1","geographic","Western Province"]] },
    GB: { trunk: "0", len: [10, 9], rules: [
      ["7","mobile","Mobile (07)"],["70","personal","Personal number (070): often abused, can be costly"],["20","geographic","London"],["121","geographic","Birmingham"],["161","geographic","Manchester"],["131","geographic","Edinburgh"],["141","geographic","Glasgow"],["113","geographic","Leeds"],["151","geographic","Liverpool"],
      ["1","geographic","UK landline"],["2","geographic","UK landline"],["3","business","Non-geographic (03), charged like landline"],["800","tollfree","Freephone (0800)"],["808","tollfree","Freephone (0808)"],["84","business","Service number (084)"],["87","business","Service number (087)"],["9","premium","Premium-rate (09)"]] }
  };
  var ISO2CC = { TR: "90", IL: "972", KR: "82", JP: "81", NL: "31", IN: "91", LK: "94", GB: "44", US: "1" };
  var TYPE = { mobile: ["Mobile", "b-info"], geographic: ["Landline (geographic)", "b-info"], tollfree: ["Toll-free", "b-safe"], premium: ["Premium-rate", "b-bad"], voip: ["VoIP / internet number", "b-warn"], business: ["Business / non-geographic", "b-info"], telemarketing: ["Telemarketing", "b-warn"], personal: ["Personal number", "b-bad"], unknown: ["Unclassified", "b-warn"] };

  /* The 053 family, shown when a bare national "053…" number is entered without a country */
  var F053 = [
    { iso: "TR", t: "Turkcell mobile (0530–0539)", page: "codes/053-turkey-turkcell.html" },
    { iso: "IL", t: "Hot Mobile (053)", page: "codes/053-israel-hot-mobile.html" },
    { iso: "KR", t: "Daegu landline (053)", page: "codes/053-daegu-korea.html" },
    { iso: "JP", t: "Hamamatsu landline (053)", page: "codes/053-hamamatsu-japan.html" },
    { iso: "NL", t: "Enschede landline (053)", page: "codes/053-enschede-netherlands.html" }
  ];

  function clean(s) {
    s = String(s || "").trim();
    var plus = /^\s*\+/.test(s);
    var d = s.replace(/\D/g, "");
    if (!plus && d.indexOf("00") === 0) { d = d.slice(2); plus = true; }
    if (!plus && d.indexOf("011") === 0 && d.length > 10) { d = d.slice(3); plus = true; }
    return { intl: plus, d: d };
  }
  function matchCC(d) { for (var l = 3; l >= 1; l--) { var p = d.slice(0, l); if (byCC[p]) return byCC[p]; } return null; }
  function classify(iso, nsn) {
    var pl = PLAN[iso]; if (!pl) return null;
    var best = null;
    pl.rules.forEach(function (r) { if (nsn.indexOf(r[0]) === 0 && (!best || r[0].length > best[0].length)) best = r; });
    return best ? { prefix: r0(best), type: best[1], region: best[2], f053: best[3] || "" } : { prefix: "", type: "unknown", region: "Not in our dataset yet", f053: "" };
    function r0(b) { return b[0]; }
  }
  function nanp(nsn) {
    var npa = nsn.slice(0, 3), o = { prefix: npa, type: "geographic", region: "North American area code " + npa, f053: "" };
    if (/^8(00|33|44|55|66|77|88)$/.test(npa)) { o.type = "tollfree"; o.region = "Toll-free (" + npa + ")"; }
    else if (npa === "900") { o.type = "premium"; o.region = "Premium-rate (900)"; }
    else if (NANP_RISK[npa]) { o.region = NANP_RISK[npa] + " (international, uses +1)"; o.caribbean = true; }
    else if (NANP_CITY[npa]) o.region = NANP_CITY[npa] + " (area code " + npa + ")";
    return o;
  }
  function localTime(tz) {
    try {
      var now = new Date();
      var t = new Intl.DateTimeFormat("en-GB", { timeZone: tz, hour: "2-digit", minute: "2-digit", weekday: "short", hour12: false }).format(now);
      var h = parseInt(new Intl.DateTimeFormat("en-GB", { timeZone: tz, hour: "2-digit", hour12: false }).format(now), 10) % 24;
      return { txt: t, h: h };
    } catch (e) { return { txt: "—", h: 12 }; }
  }
  function group(s) { return s.replace(/(\d{3})(?=\d{4,})/g, "$1 ").trim(); }
  function ways(cc, nsn, trunk) {
    var w = ["+" + cc + nsn, "+" + cc + " " + group(nsn), "00" + cc + nsn, "00" + cc + " " + group(nsn)];
    if (trunk) w.push(trunk + nsn, trunk + group(nsn), "(" + trunk + nsn.slice(0, 3) + ") " + group(nsn.slice(3)));
    if (cc === "1") w.push("(" + nsn.slice(0, 3) + ") " + nsn.slice(3, 6) + "-" + nsn.slice(6), "1-" + nsn.slice(0, 3) + "-" + nsn.slice(3, 6) + "-" + nsn.slice(6), "011 " + cc + " " + nsn);
    w.push(cc + nsn);
    return w.filter(function (x, i, a) { return a.indexOf(x) === i; });
  }

  function analyze(input, country) {
    var c = clean(input);
    if (c.d.length < 3) return { error: "Enter at least 3 digits, e.g. +90 532 123 45 67, 053-123-4567 or 053." };
    var cc = null, nsn = "";
    if (c.intl) { cc = matchCC(c.d); if (!cc) return { error: "Unknown country calling code. Check the digits after “+”." }; nsn = c.d.slice(cc.cc.length); }
    else if (country && country !== "auto") { cc = byCC[ISO2CC[country]]; nsn = c.d.replace(/^0/, ""); if (country === "US" && nsn.length === 11 && nsn[0] === "1") nsn = nsn.slice(1); }
    else {
      if (/^053/.test(c.d) || c.d === "53" || /^0?53$/.test(c.d)) return { family: true, d: c.d };
      if (/^0/.test(c.d)) return { needCountry: true };
      if (c.d.length === 10 && /^[2-9]/.test(c.d)) { cc = byCC["1"]; nsn = c.d; }
      else if (c.d.length === 11 && c.d[0] === "1") { cc = byCC["1"]; nsn = c.d.slice(1); }
      else { cc = matchCC(c.d); if (!cc) return { needCountry: true }; nsn = c.d.slice(cc.cc.length); }
    }
    var pl = PLAN[cc.iso], info = cc.cc === "1" ? nanp(nsn) : classify(cc.iso, nsn) || { prefix: "", type: "unknown", region: cc.name + " (prefix detail coming soon)", f053: "" };
    var tz = cc.tz; if (info.region.indexOf("Vancouver") > -1) tz = "America/Vancouver"; else if (/CA\)|NV\)|WA\)/.test(info.region)) tz = "America/Los_Angeles"; else if (/IL\)|TX\)/.test(info.region)) tz = "America/Chicago"; else if (/Calgary/.test(info.region)) tz = "America/Edmonton";
    var lt = localTime(tz);
    var flags = [];
    var expect = pl ? pl.len : (cc.cc === "1" ? [10] : null);
    if (expect && expect.indexOf(nsn.length) === -1) flags.push(["warn", "Length looks unusual for " + cc.name + " (" + nsn.length + " digits after the country code; typical: " + expect.join(" or ") + "). Spoofed or mistyped?"]);
    if (info.type === "premium") flags.push(["warn", "Premium-rate number: calling back can cost a lot per minute."]);
    if (info.type === "personal") flags.push(["warn", "UK 070 “personal numbers” look like mobiles but can be expensive. They are a classic call-back trap."]);
    if (info.caribbean) flags.push(["warn", "Looks domestic (+1) but is an international Caribbean code, a well-known one-ring (Wangiri) trick. Don't call back."]);
    if (WANGIRI.indexOf(cc.cc) > -1) flags.push(["warn", "+" + cc.cc + " is frequently reported in one-ring (Wangiri) call-back campaigns. Don't call back unknown numbers from this code."]);
    if (cc.iso === "XS" || cc.iso === "XN") flags.push(["warn", "Satellite / international-network numbers are very expensive to call."]);
    if (info.type === "voip") flags.push(["warn", "VoIP numbers are cheap to obtain and easy to spoof. Verify the caller another way."]);
    if (info.type === "mobile" && pl) flags.push(["info", "Mobile number portability: the operator shown is the original allocation; the subscriber may have switched."]);
    if (info.type === "tollfree") flags.push(["ok", "Toll-free numbers are free for the caller in-country and usually belong to registered businesses (still verify)."]);
    if (lt.h < 8 || lt.h >= 21) flags.push(["info", "It is " + lt.txt + " there now, outside normal calling hours (08:00–21:00)."]);
    if (!flags.some(function (f) { return f[0] === "warn"; })) flags.push(["ok", "No structural red flags. Risk depends on what the caller asks for: never share OTPs, PINs or card details."]);
    return { cc: cc, nsn: nsn, info: info, tz: tz, lt: lt, flags: flags, e164: "+" + cc.cc + nsn, ways: ways(cc.cc, nsn, pl ? pl.trunk : (cc.cc === "1" ? "" : "0")) };
  }
  window.N053 = { analyze: analyze, byCC: byCC, PLAN: PLAN, F053: F053, ISO2CC: ISO2CC, TYPE: TYPE, localTime: localTime, list: CC };

  /* ---------- Lookup UI ---------- */
  var form = document.getElementById("lookup"), out = document.getElementById("result");
  if (!form || !out) return;
  var root = document.body.getAttribute("data-root") || "", esc = window.esc053 || function (s) { return s; };
  function render(r, raw) {
    if (r.error) { out.innerHTML = '<div class="card"><p>' + esc(r.error) + "</p></div>"; return; }
    if (r.needCountry) { out.innerHTML = '<div class="card"><h3>Which country is this number from?</h3><p>National numbers starting with 0 are ambiguous. Pick a country in the selector, or type the full international format (+cc…).</p></div>'; var sel = form.querySelector("select"); if (sel) sel.focus(); return; }
    if (r.family) {
      var h = '<div class="card"><span class="eyebrow">The 053 family</span><h3>“053” is used in five countries. Which one called you?</h3><p class="mute">Without a country code, 053 could be any of these. Check the full number on your call log: it usually shows +90, +972, +82, +81 or +31.</p><div class="grid g3" style="margin-top:14px">';
      F053.forEach(function (f) {
        var c = N053.byCC[ISO2CC[f.iso]];
        h += '<a class="card" href="' + root + f.page + '"><span class="flag">' + c.flag + '</span><h3 style="margin:6px 0">' + c.name + ' · +' + c.cc + ' 53</h3><p>' + f.t + '</p><p class="small" style="margin-top:6px">Local time: <b>' + localTime(c.tz).txt + "</b></p></a>";
      });
      h += '<a class="card" href="' + root + 'codes/utc-0530-india-sri-lanka.html"><span class="flag">🕠</span><h3 style="margin:6px 0">Not a phone number? 05:30</h3><p>UTC+05:30: India &amp; Sri Lanka time.</p></a><a class="card" href="' + root + 'codes/plus-53-cuba.html"><span class="flag">🇨🇺</span><h3 style="margin:6px 0">+53 · Cuba</h3><p>Dialled as “0053…” from most of the world.</p></a>';
      h += "</div></div>";
      out.innerHTML = h; return;
    }
    var T = TYPE[r.info.type] || TYPE.unknown, warn = r.flags.filter(function (f) { return f[0] === "warn"; }).length;
    var verdict = warn >= 2 ? ['High caution', "b-bad"] : warn === 1 ? ["Caution", "b-warn"] : ["No structural red flags", "b-safe"];
    var h2 = '<div class="card"><div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;justify-content:space-between"><div><span class="eyebrow">Number intelligence</span><h3 style="font-size:1.6rem;margin:0">' + r.cc.flag + " " + esc(r.e164) + '</h3></div><div style="display:flex;gap:8px;flex-wrap:wrap"><span class="badge ' + T[1] + '">' + T[0] + '</span><span class="badge ' + verdict[1] + '">' + verdict[0] + "</span></div></div>";
    h2 += '<div class="kv"><div><small>Country</small><b>' + esc(r.cc.name) + " (+" + r.cc.cc + ')</b></div><div><small>Region / operator</small><b>' + esc(r.info.region) + '</b></div><div><small>Local time now</small><b>' + esc(r.lt.txt) + '</b></div><div><small>Time zone</small><b>' + esc(r.tz) + "</b></div></div>";
    h2 += '<h4 style="margin:6px 0">Risk checklist</h4><ul class="flags">' + r.flags.map(function (f) { return '<li class="' + (f[0] === "warn" ? "" : "ok") + '">' + esc(f[1]) + "</li>"; }).join("") + "</ul>";
    h2 += '<h4 style="margin:14px 0 8px">Ways of writing this number</h4><div class="ways">' + r.ways.map(function (w) { return "<code>" + esc(w) + "</code>"; }).join("") + "</div>";
    if (r.info.f053) {
      var f = F053.filter(function (x) { return x.iso === r.cc.iso; })[0];
      if (f) h2 += '<p class="note" style="margin-top:16px">This is part of the <b>053 family</b>. <a href="' + root + f.page + '">Read the full ' + esc(f.t) + " guide →</a></p>";
    }
    h2 += '<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn" href="' + root + "report.html?number=" + encodeURIComponent(r.e164) + '">⚑ Report this number</a><a class="btn ghost" href="' + root + 'guides/block-unknown-callers.html">How to block it</a><button class="btn ghost" type="button" data-copy="' + esc(r.e164) + '">Copy E.164</button><a class="btn ghost" target="_blank" rel="noopener" href="https://www.google.com/search?q=%22' + encodeURIComponent(r.e164) + '%22+OR+%22' + encodeURIComponent(r.ways[r.ways.length - 1]) + '%22">Search the web</a></div>';
    h2 += '<p class="small dim" style="margin-top:14px">Analysis runs in your browser from public numbering plans. We never store what you search. Results are informational, not a guarantee of who is calling.</p></div>';
    h2 += '<div class="leadbox" style="margin-top:18px"><div class="grid g2" style="align-items:center"><div><span class="eyebrow">Stop the next one</span><h3>Lost money or shared details with this caller?</h3><p class="mute" style="margin:0">Get matched with vetted identity-protection, call-blocking and licensed fraud-help providers. Free, takes 60 seconds.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn amb" href="' + root + 'get-protected.html?need=scam-help">Get help now</a><a class="btn ghost" href="' + root + 'get-protected.html?need=call-blocking">Block spam calls</a></div></div></div>';
    out.innerHTML = h2;
  }
  function run(push) {
    var q = form.querySelector("[name=q]").value, ctry = (form.querySelector("[name=country]") || {}).value || "auto";
    var r = analyze(q, ctry); render(r, q);
    if (window.track053) window.track053("lookup", { country: ctry });
    if (push && history.replaceState) { var u = new URL(location.href); u.searchParams.set("n", q); if (ctry !== "auto") u.searchParams.set("c", ctry); else u.searchParams.delete("c"); history.replaceState(null, "", u); }
    out.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
  form.addEventListener("submit", function (e) { e.preventDefault(); run(true); });
  document.querySelectorAll("[data-try]").forEach(function (b) { b.addEventListener("click", function () { form.querySelector("[name=q]").value = b.getAttribute("data-try"); var s = form.querySelector("[name=country]"); if (s) s.value = b.getAttribute("data-c") || "auto"; run(true); }); });
  var p = new URLSearchParams(location.search);
  if (p.get("n")) { form.querySelector("[name=q]").value = p.get("n"); if (p.get("c") && form.querySelector("[name=country]")) form.querySelector("[name=country]").value = p.get("c"); run(false); }
})();
