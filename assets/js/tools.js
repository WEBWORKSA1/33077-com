/* 33077.com — interactive tools: decoder, love-code builder, lucky score, zodiac, festivals */
(function () {
  "use strict";
  var D = window.DIGITS, C = window.CODES || [], Z = window.ZODIAC, $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (t) { return String(t).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var base = document.body.getAttribute("data-base") || "";
  var MAP = {}; C.forEach(function (c) { MAP[c[0]] = c; });
  var CATS = { love: ["Love", "b-love"], life: ["Life", "b-good"], business: ["Prosperity", "b-good"], fun: ["Chat slang", "b-mix"], insult: ["Avoid", "b-bad"], brand: ["33077 original", "b-love"] };

  /* ---------- core analysis ---------- */
  function segment(n) {
    var L = n.length, best = new Array(L + 1).fill(null); best[L] = { s: 0, p: [] };
    for (var i = L - 1; i >= 0; i--) {
      var cand = { s: best[i + 1].s, p: [n[i]].concat(best[i + 1].p) };
      for (var k = 2; k <= Math.min(8, L - i); k++) {
        var sub = n.substr(i, k);
        if (MAP[sub] && MAP[sub][4] !== "brand" || (sub === "33077" && MAP[sub])) {
          var sc = k * k + best[i + k].s; if (sc > cand.s) cand = { s: sc, p: [sub].concat(best[i + k].p) };
        }
      }
      best[i] = cand;
    }
    return best[0].p;
  }
  function luck(n) {
    var ds = n.replace(/\D/g, ""); if (!ds) return null;
    var sum = 0, notes = [];
    for (var i = 0; i < ds.length; i++) sum += D[ds[i]].luck;
    var sc = 50 + (sum / ds.length) * 13;
    function has(x, pts, why) { if (ds.indexOf(x) > -1) { sc += pts; notes.push([pts, why]); } }
    has("168", 6, "168 一路发 “prosper all the way”"); has("518", 5, "518 我要发 “I will prosper”");
    has("888", 6, "888 triple prosperity"); has("666", 4, "666 smooth sailing"); has("999", 4, "999 everlasting");
    has("520", 4, "520 “I love you”"); has("1314", 4, "1314 “for a lifetime”"); has("3344", 5, "3344 “forever” (the good 4s)");
    has("14", -6, "14 sounds like 要死 “going to die”"); has("250", -6, "250 means “idiot”"); has("748", -10, "748 is an insult");
    if (/8$/.test(ds)) { sc += 6; notes.push([6, "Ends in 8 — the prosperity finish buyers pay for"]); }
    else if (/[69]$/.test(ds)) { sc += 3; notes.push([3, "Ends in a lucky 6 or 9"]); }
    else if (/4$/.test(ds)) { sc -= 6; notes.push([-6, "Ends in 4 — the least wanted finish"]); }
    if (/(\d)\1\1/.test(ds)) { var r = ds.match(/(\d)\1\1/)[1]; var p = D[r].luck > 0 ? 6 : D[r].luck < 0 ? -6 : 2; sc += p; notes.push([p, "Triple repeat " + r + r + r + " (memorable)"]); }
    if (/0123|1234|2345|3456|4567|5678|6789/.test(ds)) { sc += 3; notes.push([3, "Straight sequence — easy to remember"]); }
    if (ds.indexOf("4") < 0 && ds.length > 2) { sc += 3; notes.push([3, "No 4 anywhere — Chinese buyers’ first filter"]); }
    sc = Math.max(1, Math.min(99, Math.round(sc)));
    var g = sc >= 85 ? ["大吉", "Excellent", "b-good"] : sc >= 70 ? ["吉", "Good", "b-good"] : sc >= 50 ? ["平", "Average", "b-mix"] : sc >= 35 ? ["小凶", "Weak", "b-bad"] : ["凶", "Avoid", "b-bad"];
    return { score: sc, grade: g, notes: notes, digits: ds };
  }
  window.luck33 = luck;

  function digitRow(ds) {
    return '<div class="seg">' + ds.split("").map(function (d) { var x = D[d]; return '<div class="blk"><b>' + d + '</b><span class="han">' + x.sounds[0][0] + '</span><small>' + x.sounds[0][2] + '</small></div>'; }).join("") + "</div>";
  }
  function codeLine(c) {
    var cat = CATS[c[4]] || ["", "b-mix"];
    return '<div class="res-card" style="margin-bottom:12px"><div class="row" style="justify-content:space-between"><div><span class="big-num num" style="font-size:2.2rem">' + c[0] + '</span> <span class="han" style="font-size:1.6rem;margin-left:8px">' + c[1] + '</span></div><span class="badge ' + cat[1] + '">' + cat[0] + '</span></div><div class="muted">' + c[2] + '</div><p style="margin:.4em 0 0;font-weight:700;font-size:1.1rem">“' + esc(c[3]) + '”</p>' + (c[5] ? '<p class="small muted" style="margin:.4em 0 0">' + esc(c[5]) + "</p>" : "") + "</div>";
  }
  function decode(raw) {
    var n = String(raw || "").replace(/\D/g, "").slice(0, 20);
    if (!n) return '<div class="note">Type any number — a phone number, price, date, plate, or code like 520.</div>';
    var h = "", ex = MAP[n];
    if (ex) h += codeLine(ex);
    var seg = segment(n), known = seg.filter(function (p) { return p.length > 1; });
    if (!ex && known.length) {
      h += '<div class="res-card" style="margin-bottom:12px"><h3>Hidden codes inside ' + n + '</h3><div class="seg">' + seg.map(function (p) {
        if (p.length > 1) { var c = MAP[p]; return '<div class="blk" style="border:2px solid var(--red)"><b>' + p + '</b><span class="han">' + c[1] + '</span><small>' + esc(c[3]) + "</small></div>"; }
        var x = D[p]; return '<div class="blk"><b>' + p + '</b><span class="han">' + x.sounds[0][0] + '</span><small>' + x.sounds[0][2] + "</small></div>";
      }).join("") + '</div><p class="small muted" style="margin:0">Read together: <span class="han">' + seg.map(function (p) { return p.length > 1 ? MAP[p][1] : D[p].sounds[0][0]; }).join(" · ") + "</span></p></div>";
    }
    var L = luck(n);
    h += '<div class="res-card" style="margin-bottom:12px"><div class="row" style="justify-content:space-between;align-items:flex-end"><div><div class="small muted">Chinese luck score</div><span class="score-big num">' + L.score + '</span><span class="muted">/100</span></div><span class="badge ' + L.grade[2] + '" style="font-size:.95rem"><span class="han">' + L.grade[0] + "</span> · " + L.grade[1] + '</span></div><div class="meter" style="margin:12px 0"><i style="width:' + L.score + '%"></i></div>' +
      (L.notes.length ? "<ul class=small style='margin:0;padding-left:18px'>" + L.notes.map(function (x) { return "<li>" + (x[0] > 0 ? "▲ " : "▼ ") + esc(x[1]) + "</li>"; }).join("") + "</ul>" : "") + "</div>";
    h += '<div class="res-card" style="margin-bottom:12px"><h3>Digit by digit</h3><div class="tbl-wrap"><table><thead><tr><th>Digit</th><th>Chinese</th><th>Sounds like</th><th>Feel</th></tr></thead><tbody>' +
      n.split("").map(function (d) { var x = D[d]; return "<tr><td class='num'><b>" + d + "</b></td><td class='han'>" + x.han + " <span class='muted small'>" + x.py + "</span></td><td>" + x.sounds.map(function (s) { return "<span class='han'>" + s[0] + "</span> <span class='muted small'>" + s[2] + "</span>"; }).join(" · ") + "</td><td>" + (x.luck > 0 ? "<span class='badge b-good'>Lucky</span>" : x.luck < 0 ? "<span class='badge b-bad'>Unlucky</span>" : "<span class='badge b-mix'>Neutral</span>") + "</td></tr>"; }).join("") + "</tbody></table></div></div>";
    h += '<div class="row"><button class="btn sm" type="button" data-sharenum="' + n + '">Share this meaning</button><a class="btn sm ghost" href="' + base + 'lucky-score.html?n=' + n + '">Full luck report</a><a class="btn sm gold" href="' + base + 'concierge.html?goal=buy-number">Want a luckier number? Get matched →</a></div>';
    return h;
  }
  window.decode33 = decode;

  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-sharenum]"); if (!b) return;
    var n = b.getAttribute("data-sharenum"), c = MAP[n];
    window.share33((c ? n + " = " + c[1] + " “" + c[3] + "”." : "What does " + n + " mean in Chinese?") + " Decode any number:", location.origin + location.pathname.replace(/[^/]*$/, "") + "decoder.html?n=" + n);
  });

  /* decoder widgets */
  $$("form.decoder").forEach(function (f) {
    var inp = $("input", f), out = document.getElementById(f.getAttribute("data-out"));
    function run(push) { out.innerHTML = decode(inp.value); if (push && history.replaceState && f.hasAttribute("data-url")) history.replaceState(null, "", "?n=" + inp.value.replace(/\D/g, "")); }
    f.addEventListener("submit", function (e) { e.preventDefault(); run(true); out.scrollIntoView({ behavior: "smooth", block: "nearest" }); });
    $$(".chip[data-n]", f.parentNode).forEach(function (c) { c.addEventListener("click", function () { inp.value = c.getAttribute("data-n"); run(true); }); });
    var q = new URLSearchParams(location.search).get("n"); if (q && f.hasAttribute("data-url")) { inp.value = q; run(false); }
  });

  /* ---------- code dictionary ---------- */
  var dict = $("#dict");
  if (dict) {
    var fq = $("#dict-q"), fc = $("#dict-cat");
    function render() {
      var q = (fq.value || "").toLowerCase(), cat = fc.value;
      var rows = C.filter(function (c) { return (!cat || c[4] === cat) && (!q || (c.join(" ").toLowerCase().indexOf(q) > -1)); });
      dict.innerHTML = rows.length ? rows.map(function (c) { var k = CATS[c[4]]; return "<tr><td><a class='num' href='" + base + "decoder.html?n=" + c[0] + "'><b>" + c[0] + "</b></a></td><td class='han'>" + c[1] + "<div class='small muted'>" + c[2] + "</div></td><td>" + esc(c[3]) + (c[5] ? "<div class='small muted'>" + esc(c[5]) + "</div>" : "") + "</td><td><span class='badge " + k[1] + "'>" + k[0] + "</span></td></tr>"; }).join("") : "<tr><td colspan=4>No match — try the <a href='" + base + "decoder.html'>decoder</a>.</td></tr>";
      var cnt = $("#dict-count"); if (cnt) cnt.textContent = rows.length + " codes";
    }
    fq.addEventListener("input", render); fc.addEventListener("change", render); render();
  }

  /* ---------- love-code builder ---------- */
  var bank = $("#word-bank");
  if (bank) {
    var W = [["我", "5", "I"], ["你", "0", "you"], ["爱", "2", "love"], ["想", "3", "miss"], ["亲亲", "77", "kiss"], ["要", "1", "want"], ["就", "9", "only / just"], ["是", "4", "am / is"], ["一生一世", "1314", "for a lifetime"], ["生生世世", "3344", "forever"], ["久久", "99", "long-lasting"], ["长长久久", "3399", "ever and ever"], ["一路发", "168", "prosper all the way"], ["拜拜", "88", "bye-bye"]];
    var picked = [];
    bank.innerHTML = W.map(function (w, i) { return '<button type="button" class="chip" data-w="' + i + '"><span class="han">' + w[0] + '</span> ' + w[2] + ' <b class="num">' + w[1] + "</b></button>"; }).join("");
    var out = $("#builder-out");
    function draw() {
      var code = picked.map(function (i) { return W[i][1]; }).join("");
      out.innerHTML = picked.length ? '<div class="big-num num" style="font-size:clamp(2.4rem,8vw,4rem);word-break:break-all">' + code + '</div><div class="han" style="font-size:1.4rem">' + picked.map(function (i) { return W[i][0]; }).join("") + '</div><div class="muted">“' + picked.map(function (i) { return W[i][2]; }).join(" ") + '”</div><div class="row" style="margin-top:12px"><button type="button" class="btn sm" id="b-share">Share my code</button><button type="button" class="btn sm ghost" id="b-undo">Undo</button><button type="button" class="btn sm ghost" id="b-clear">Clear</button><a class="btn sm gold" href="' + base + 'contests.html#enter">Enter it in the contest</a></div>' : '<p class="muted">Tap the words below to build a secret number message.</p>';
      var s = $("#b-share"); if (s) s.onclick = function () { window.share33("My secret Chinese number code: " + code + " (" + picked.map(function (i) { return W[i][0]; }).join("") + "). Decode yours:"); };
      var u = $("#b-undo"); if (u) u.onclick = function () { picked.pop(); draw(); };
      var c = $("#b-clear"); if (c) c.onclick = function () { picked = []; draw(); };
    }
    bank.addEventListener("click", function (e) { var b = e.target.closest("[data-w]"); if (b && picked.length < 10) { picked.push(+b.getAttribute("data-w")); draw(); } });
    draw();
  }

  /* ---------- lucky score tool ---------- */
  var ls = $("#luck-form");
  if (ls) {
    var lo = $("#luck-out");
    function runL() {
      var v = $("#luck-n").value, type = $("#luck-type").value, L = luck(v);
      if (!L) { lo.innerHTML = '<div class="note">Enter a number with at least one digit.</div>'; return; }
      var tips = {
        phone: "Chinese buyers pay most for numbers ending in 8 or 88, repeats like 888/666, and no 4s. Premium numbers are sold by carriers and brokers.",
        plate: "Plates are auctioned in Hong Kong, Singapore, the UAE, the UK and more — HK’s record is HK$26M for the single letter “W” (2021).",
        address: "Many Chinese buyers avoid unit and floor numbers with 4 or 14; 8s and 6s can raise resale appeal.",
        domain: "Five-digit .com domains (“5N”) with no 4 and lots of 8/6/9 fetch the most. 2026 sales ranged from about $20 to $24,000+.",
        price: "Prices ending in 8 (¥88, ¥168, ¥888) signal prosperity; avoid 4 and 250 in gifts. 520 and 1314 work for romantic gifts.",
        date: "Weddings cluster on dates with 520, 1314 and 8s — and avoid Ghost Month (7th lunar month)."
      }[type];
      lo.innerHTML = '<div class="res-card"><div class="row" style="justify-content:space-between;align-items:flex-end"><div><div class="small muted">Luck score for <b class="num">' + esc(v) + '</b></div><span class="score-big num">' + L.score + '</span><span class="muted">/100</span></div><span class="badge ' + L.grade[2] + '" style="font-size:1rem"><span class="han">' + L.grade[0] + "</span> · " + L.grade[1] + '</span></div><div class="meter" style="margin:12px 0"><i style="width:' + L.score + '%"></i></div>' + digitRow(L.digits) +
        (L.notes.length ? "<h3>Why this score</h3><ul>" + L.notes.map(function (x) { return "<li>" + (x[0] > 0 ? "<b style='color:var(--ok)'>+" + x[0] + "</b> " : "<b style='color:var(--bad)'>" + x[0] + "</b> ") + esc(x[1]) + "</li>"; }).join("") + "</ul>" : "") +
        '<div class="note" style="margin-top:12px"><b>Market tip:</b> ' + tips + '</div><div class="row" style="margin-top:16px"><a class="btn" href="' + base + 'concierge.html?goal=' + (type === "domain" ? "domain" : type === "plate" ? "plate" : type === "date" ? "date" : "buy-number") + '">Find me a luckier ' + (type === "date" ? "date" : type) + ' →</a><a class="btn ghost" href="' + base + 'concierge.html?goal=sell">Value / sell this ' + type + '</a><button class="btn ghost" type="button" data-sharenum="' + L.digits + '">Share</button></div><p class="small muted" style="margin-top:12px">For entertainment and cultural insight — not financial advice.</p></div>';
    }
    ls.addEventListener("submit", function (e) { e.preventDefault(); runL(); });
    var q = new URLSearchParams(location.search).get("n"); if (q) { $("#luck-n").value = q; runL(); }
  }

  /* ---------- zodiac ---------- */
  function zodiacOf(dateStr) {
    var d = new Date(dateStr + "T12:00:00"); if (isNaN(d)) return null;
    var y = d.getFullYear(), cny = (window.CNY || {})[y];
    var approx = !cny; if (cny) { var c = new Date(y + "-" + cny.slice(0, 2) + "-" + cny.slice(2) + "T00:00:00"); if (d < c) y--; }
    var i = ((y - 4) % 12 + 12) % 12, e = ((y - 4) % 10 + 10) % 10;
    return { y: y, a: Z[i], el: window.ELEMENTS[e], yang: y % 2 === 0, gz: window.STEMS[e] + window.BRANCHES[i], approx: approx, idx: i };
  }
  var zf = $("#zodiac-form");
  if (zf) {
    zf.addEventListener("submit", function (e) {
      e.preventDefault(); var r = zodiacOf($("#z-date").value), o = $("#zodiac-out");
      if (!r) { o.innerHTML = '<div class="note">Pick a valid date.</div>'; return; }
      o.innerHTML = '<div class="res-card"><div class="row" style="gap:20px"><div class="han" style="font-size:4.5rem;line-height:1;color:var(--red)">' + r.a.h + '</div><div><div class="small muted">Lunar year ' + r.y + ' · <span class="han">' + r.gz + '</span></div><h2 style="margin:0">' + r.el[0] + " " + r.a.n + '</h2><div class="muted"><span class="han">' + r.el[1] + r.a.h + "</span> · " + (r.yang ? "Yang" : "Yin") + " · " + r.a.trait + '</div></div></div><div class="grid g2" style="margin-top:16px"><div><b>Lucky numbers</b><div class="seg">' + r.a.lucky.map(function (n) { return '<div class="blk"><b>' + n + "</b></div>"; }).join("") + '</div></div><div><b>Numbers to avoid</b><div class="seg">' + r.a.unlucky.map(function (n) { return '<div class="blk"><b style="color:var(--muted)">' + n + "</b></div>"; }).join("") + '</div></div></div>' + (r.approx ? '<p class="small muted">Outside our lunar table — based on calendar year.</p>' : '<p class="small muted">Born in January or February? We use the exact Lunar New Year date for ' + (r.y + 1) + '.</p>') + '<div class="row"><a class="btn sm" href="' + base + 'lucky-score.html">Score my phone number</a><a class="btn sm gold" href="' + base + 'concierge.html?goal=date">Get an auspicious date</a></div></div>';
    });
    var s1 = $("#c1"), s2 = $("#c2"), co = $("#compat-out");
    [s1, s2].forEach(function (s, k) { s.innerHTML = Z.map(function (a, i) { return '<option value="' + i + '"' + (i === (k ? 7 : 6) ? " selected" : "") + ">" + a.n + " " + a.h + "</option>"; }).join(""); });
    var tri = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]], six = [[0, 1], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]], clash = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]];
    function inPair(L, a, b) { return L.some(function (p) { return (p[0] === a && p[1] === b) || (p[0] === b && p[1] === a); }); }
    function compat() {
      var a = +s1.value, b = +s2.value, r;
      if (a === b) r = [72, "Same sign", "Mirror match — you understand each other instantly but share the same blind spots."];
      else if (inPair(six, a, b)) r = [95, "Six Harmonies 六合", "A classic secret-friend pairing — one of the best matches in Chinese astrology."];
      else if (tri.some(function (t) { return t.indexOf(a) > -1 && t.indexOf(b) > -1; })) r = [88, "Triad 三合", "Same trine: shared values and natural teamwork."];
      else if (inPair(clash, a, b)) r = [35, "Clash 六冲", "Opposite signs — sparks fly both ways. Works with patience."];
      else r = [62, "Neutral", "No classic bond or clash — the relationship is what you make it."];
      co.innerHTML = '<div class="res-card"><div class="row" style="justify-content:space-between"><div class="han" style="font-size:2.4rem">' + Z[a].h + " ❤ " + Z[b].h + '</div><span class="score-big num">' + r[0] + '%</span></div><div class="meter" style="margin:10px 0"><i style="width:' + r[0] + '%"></i></div><h3>' + r[1] + '</h3><p class="muted" style="margin:0">' + r[2] + "</p></div>";
    }
    s1.onchange = s2.onchange = compat; compat();
    var ch = $("#zodiac-chart");
    if (ch) {
      var y0 = new Date().getFullYear(), rows = "";
      Z.forEach(function (a, i) { var ys = []; for (var y = 1924; y <= 2035; y++) if (((y - 4) % 12 + 12) % 12 === i) ys.push(y === y0 ? "<b>" + y + "</b>" : y); rows += "<tr><td><span class='han' style='font-size:1.3rem;color:var(--red)'>" + a.h + "</span> " + a.n + "</td><td class='small num'>" + ys.join(", ") + "</td><td class='num'>" + a.lucky.join(", ") + "</td></tr>"; });
      ch.innerHTML = rows;
    }
  }

  /* ---------- festivals ---------- */
  var FN = {
    cny: ["Chinese New Year", "春节", "Lunar 1/1 — red envelopes with 8s, never 4s."],
    lantern: ["Lantern Festival", "元宵节", "Lunar 1/15 — riddles on lanterns; an old matchmaking night."],
    shangsi: ["Shangsi · Double Third", "上巳节 · 三月三", "Lunar 3/3 — the ancient spring love festival and Zhuang song festival. The “33” in 33077."],
    "520": ["520 Day", "520 网络情人节", "May 20 — “I love you” day; gifts, red packets of ¥520, peak wedding registrations."],
    dragon: ["Dragon Boat Festival", "端午节", "Lunar 5/5 — zongzi and boat races."],
    qixi: ["Qixi · Chinese Valentine’s Day", "七夕", "Lunar 7/7 — the Cowherd and Weaver Girl meet once a year. The “77” in 33077."],
    ghost: ["Ghost Festival", "中元节", "Lunar 7/15 — mid-point of Ghost Month; many avoid weddings and moves."],
    midautumn: ["Mid-Autumn Festival", "中秋节", "Lunar 8/15 — mooncakes and family reunions."],
    double9: ["Double Ninth", "重阳节", "Lunar 9/9 — 久久 “long-lasting”; honouring elders."],
    "1111": ["Singles’ Day 11.11", "双十一 光棍节", "Nov 11 — the world’s largest shopping festival, born as a joke about “bare sticks” 1111."]
  };
  function upcoming() {
    var now = new Date(), list = [];
    Object.keys(window.FEST || {}).forEach(function (y) {
      var f = window.FEST[y]; Object.keys(f).forEach(function (k) { list.push([k, f[k]]); });
      list.push(["520", y + "-05-20"]); list.push(["1111", y + "-11-11"]);
    });
    return list.map(function (x) { return [x[0], new Date(x[1] + "T00:00:00+08:00"), x[1]]; }).filter(function (x) { return x[1] > now - 864e5; }).sort(function (a, b) { return a[1] - b[1]; });
  }
  var fl = $("#fest-list");
  if (fl) {
    var up = upcoming().slice(0, +(fl.getAttribute("data-n") || 10));
    fl.innerHTML = up.map(function (x) {
      var f = FN[x[0]], days = Math.ceil((x[1] - Date.now()) / 864e5);
      return '<div class="card"><div class="row" style="justify-content:space-between"><span class="badge ' + (x[0] === "qixi" || x[0] === "shangsi" || x[0] === "520" ? "b-love" : "b-mix") + '">' + (days <= 0 ? "Today" : "in " + days + " days") + '</span><span class="small muted num">' + new Date(x[2] + "T12:00:00Z").toLocaleDateString(undefined, { timeZone: "UTC", weekday: "short", year: "numeric", month: "short", day: "numeric" }) + '</span></div><h3 style="margin-top:10px">' + f[0] + '</h3><div class="han" style="color:var(--red)">' + f[1] + '</div><p class="small muted" style="margin:.4em 0 0">' + f[2] + "</p></div>";
    }).join("");
  }
  $$("[data-next-fest]").forEach(function (el) {
    var k = el.getAttribute("data-next-fest"), n = upcoming().filter(function (x) { return x[0] === k; })[0];
    if (n) { el.setAttribute("data-countdown", n[2] + "T00:00:00+08:00"); var lbl = document.querySelector('[data-fest-date="' + k + '"]'); if (lbl) lbl.textContent = new Date(n[2] + "T12:00:00Z").toLocaleDateString(undefined, { timeZone: "UTC", weekday: "long", year: "numeric", month: "long", day: "numeric" }); }
  });
})();
