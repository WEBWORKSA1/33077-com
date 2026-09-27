/* 33077.com — site behaviour (no dependencies) */
(function () {
  "use strict";
  var S = window.SITE || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (t) { return String(t).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var LOAD_T = Date.now();

  function toast(msg) {
    var t = $(".toast"); if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
    t.textContent = msg; t.classList.add("on"); clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("on"); }, 2200);
  }
  window.toast33 = toast;

  /* ---------- theme ---------- */
  var root = document.documentElement;
  var saved = store.get("theme"); if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  $$(".theme-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = root.getAttribute("data-theme");
      var dark = cur ? cur === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
      var next = dark ? "light" : "dark"; root.setAttribute("data-theme", next); store.set("theme", next);
    });
  });

  /* ---------- mobile drawer ---------- */
  var drawer = $(".drawer");
  $$(".menu-btn").forEach(function (b) { b.addEventListener("click", function () { drawer.classList.add("open"); b.setAttribute("aria-expanded", "true"); }); });
  if (drawer) drawer.addEventListener("click", function (e) { if (e.target === drawer || e.target.closest(".close-drawer")) { drawer.classList.remove("open"); } });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer) drawer.classList.remove("open"); });

  /* ---------- cookie consent ---------- */
  var ck = $(".cookie");
  if (ck && !store.get("consent")) ck.classList.add("on");
  $$(".cookie [data-consent]").forEach(function (b) { b.addEventListener("click", function () { store.set("consent", b.getAttribute("data-consent")); ck.classList.remove("on"); }); });

  /* ---------- share ---------- */
  function share(text, url) {
    url = url || location.href;
    if (navigator.share) { navigator.share({ title: document.title, text: text, url: url }).catch(function () {}); return; }
    var s = (text ? text + " " : "") + url;
    if (navigator.clipboard) navigator.clipboard.writeText(s).then(function () { toast("Copied — paste it anywhere"); });
    else toast(s);
  }
  window.share33 = share;
  $$("[data-share]").forEach(function (b) { b.addEventListener("click", function () { share(b.getAttribute("data-share")); }); });

  /* ---------- forms → owner inbox (never exposed) ---------- */
  function endpoint() {
    var v = (S.inbox || []).join("");
    var id = S.inboxIsAlias ? v : atob(v.split("").reverse().join(""));
    return "https://formsubmit.co/ajax/" + encodeURIComponent(id);
  }
  function sendForm(form) {
    var msg = $(".form-msg", form);
    var btn = $("button[type=submit]", form);
    if ((form.querySelector("[name=_gotcha]") || {}).value) return; // bot
    if (Date.now() - LOAD_T < 2500) { show("err", "Please take a moment and try again."); return; }
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var data = {};
    new FormData(form).forEach(function (v, k) { if (k === "_gotcha") return; data[k] = data[k] ? data[k] + ", " + v : v; });
    data._subject = "[33077.com] " + (form.getAttribute("data-subject") || "Website form") + (data.name ? " — " + data.name : "");
    data._template = "table"; data._captcha = "false"; data.page = location.href; data.submitted = new Date().toISOString();
    if (data.email) data._replyto = data.email;
    if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
    fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false" || j.success === false) throw new Error(j.message || "fail"); }); })
      .then(function () {
        show("ok", form.getAttribute("data-ok") || "Thank you! Your message is in — we reply within 24–48 hours.");
        form.reset(); form.dispatchEvent(new CustomEvent("sent33"));
      })
      .catch(function () { show("err", "Could not send right now. Please try again in a minute, or use the Contact link at the top of the page."); })
      .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn._t; } });
    function show(k, t) { if (!msg) { toast(t); return; } msg.className = "form-msg " + k; msg.textContent = t; }
  }
  $$("form.js-form").forEach(function (f) {
    if (!f.querySelector("[name=_gotcha]")) { var hp = document.createElement("input"); hp.type = "text"; hp.name = "_gotcha"; hp.tabIndex = -1; hp.autocomplete = "off"; hp.className = "hp"; hp.setAttribute("aria-hidden", "true"); f.appendChild(hp); }
    if (!f.querySelector(".form-msg")) { var m = document.createElement("div"); m.className = "form-msg"; m.setAttribute("role", "status"); f.appendChild(m); }
    f.addEventListener("submit", function (e) { e.preventDefault(); sendForm(f); });
  });

  /* ---------- multi-step forms ---------- */
  $$(".steps").forEach(function (form) {
    var steps = $$(".step", form), bars = $$(".progress i", form), i = 0;
    function go(n) {
      if (n > i) { var inv = $$("input,select,textarea", steps[i]).filter(function (x) { return !x.checkValidity(); }); if (inv.length) { inv[0].reportValidity(); return; } }
      i = Math.max(0, Math.min(steps.length - 1, n));
      steps.forEach(function (s, k) { s.classList.toggle("on", k === i); });
      bars.forEach(function (b, k) { b.classList.toggle("on", k <= i); });
      var y = form.getBoundingClientRect().top + scrollY - 90; if (Math.abs(scrollY - y) > 200) scrollTo({ top: y, behavior: "smooth" });
    }
    $$("[data-next]", form).forEach(function (b) { b.addEventListener("click", function () { go(i + 1); }); });
    $$("[data-prev]", form).forEach(function (b) { b.addEventListener("click", function () { go(i - 1); }); });
    form.addEventListener("sent33", function () { go(0); });
    var q = new URLSearchParams(location.search).get("goal");
    if (q) { var r = form.querySelector('input[name=goal][value="' + q + '"]'); if (r) r.checked = true; }
    go(0);
  });

  /* ---------- ads (AdSense when configured, otherwise house ads) ---------- */
  var slots = $$(".ad[data-slot]");
  if (S.adsenseClient) {
    var sc = document.createElement("script"); sc.async = true; sc.crossOrigin = "anonymous";
    sc.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(S.adsenseClient);
    document.head.appendChild(sc);
    slots.forEach(function (el) {
      var slot = (S.adSlots || {})[el.getAttribute("data-slot")] || "";
      el.innerHTML = '<div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' + esc(S.adsenseClient) + '"' + (slot ? ' data-ad-slot="' + esc(slot) + '"' : "") + ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
    var st = $(".ad-sticky"); if (st) st.classList.add("on");
  } else {
    var base = document.body.getAttribute("data-base") || "";
    var houses = [
      ["Your brand here — reach lucky-number & China-culture fans", "Sponsor a tool, a festival or the newsletter.", "advertise.html", "See packages"],
      ["Want a lucky phone number, plate or numeric domain?", "Tell the 33077 Concierge what you need — free matching.", "concierge.html", "Start now"],
      ["Help keep 33077 free", "Support operations, contests and new tools.", "support.html", "Support us"]
    ];
    slots.forEach(function (el, k) {
      var h = houses[k % houses.length];
      el.innerHTML = '<div class="ad-label">Sponsored</div><div class="house-ad"><div><b>' + h[0] + '</b><div class="small muted">' + h[1] + '</div></div><a class="btn sm gold" href="' + base + h[2] + '">' + h[3] + '</a></div>';
    });
  }

  /* ---------- lite YouTube ---------- */
  function ytCard(el) {
    var id = el.getAttribute("data-id"), t = el.getAttribute("data-title") || "Video";
    el.innerHTML = '<img loading="lazy" alt="' + esc(t) + '" src="https://i.ytimg.com/vi/' + esc(id) + '/hqdefault.jpg"><span class="play" aria-hidden="true"></span>';
    el.setAttribute("role", "button"); el.setAttribute("tabindex", "0"); el.setAttribute("aria-label", "Play: " + t);
    function play() { el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + esc(id) + '?autoplay=1&rel=0" title="' + esc(t) + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }
    el.addEventListener("click", play, { once: true });
    el.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); } });
  }
  $$("[data-videos]").forEach(function (box) {
    var n = parseInt(box.getAttribute("data-videos"), 10) || 99;
    box.innerHTML = (S.videos || []).slice(0, n).map(function (v) {
      return '<div><div class="yt" data-id="' + esc(v.id) + '" data-title="' + esc(v.title) + '"></div><h3 style="margin-top:10px;font-size:1rem">' + esc(v.title) + '</h3><div class="small muted">' + esc(v.channel) + ' · via YouTube</div></div>';
    }).join("");
  });
  $$(".yt[data-id]").forEach(ytCard);
  $$("[data-channel]").forEach(function (a) { if (S.youtubeChannel) { a.href = S.youtubeChannel; a.hidden = false; } });

  /* ---------- countdowns ---------- */
  $$("[data-contest-cd]").forEach(function (el) { if (S.contest) el.setAttribute("data-countdown", S.contest.closes); });
  function tick() {
    $$("[data-countdown]").forEach(function (el) {
      var d = new Date(el.getAttribute("data-countdown")) - Date.now();
      if (d <= 0) { el.innerHTML = "<strong>It’s today — or it just happened!</strong>"; return; }
      var dd = Math.floor(d / 864e5), hh = Math.floor(d / 36e5) % 24, mm = Math.floor(d / 6e4) % 60, ss = Math.floor(d / 1e3) % 60;
      el.innerHTML = [[dd, "days"], [hh, "hrs"], [mm, "min"], [ss, "sec"]].map(function (x) { return "<div><b class=num>" + x[0] + "</b><small>" + x[1] + "</small></div>"; }).join("");
    });
  }
  if ($("[data-countdown]")) { tick(); setInterval(tick, 1000); }

  /* ---------- config-driven bits ---------- */
  var g = S.fundingGoal;
  $$("[data-goal]").forEach(function (el) {
    if (!g) return; var pct = Math.min(100, Math.round((g.raised / g.goal) * 100));
    el.innerHTML = '<div class="row" style="justify-content:space-between"><b>' + esc(g.label) + '</b><span class="num">$' + g.raised.toLocaleString() + ' of $' + g.goal.toLocaleString() + '</span></div><div class="meter" style="margin:10px 0"><i style="width:' + Math.max(pct, 2) + '%"></i></div><div class="small muted">' + pct + '% funded · ' + g.supporters + ' supporters · every dollar is published in our quarterly report</div>';
  });
  var pays = { paypal: "PayPal", kofi: "Ko-fi", buymeacoffee: "Buy Me a Coffee", stripe: "Card / Apple Pay / Google Pay" };
  $$("[data-paylinks]").forEach(function (el) {
    var h = Object.keys(pays).filter(function (k) { return S.donate && S.donate[k]; }).map(function (k) { return '<a class="btn ' + (k === "stripe" ? "" : "ghost") + '" target="_blank" rel="noopener" href="' + esc(S.donate[k]) + '">' + pays[k] + '</a>'; }).join("");
    el.innerHTML = h || '<p class="small muted">Instant online payment buttons are being connected. Use the pledge form below — we’ll send you a secure payment link within 24 hours.</p>';
  });
  $$("[data-prizes]").forEach(function (el) {
    var c = S.contest; if (!c) return;
    el.innerHTML = c.prizes.map(function (p, k) { return '<div class="card"><div class="ico">' + ["🥇", "🥈", "🏅"][k] + '</div><h3>' + esc(p.place) + '</h3><p class="muted" style="margin:0">' + esc(p.prize) + '</p></div>'; }).join("");
  });
  $$(".year-now").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* amount pickers */
  $$(".amounts").forEach(function (box) {
    var target = document.getElementById(box.getAttribute("data-target"));
    $$("button", box).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", box).forEach(function (x) { x.classList.remove("on"); }); b.classList.add("on");
        if (target) { target.value = b.getAttribute("data-v"); target.dispatchEvent(new Event("input")); }
      });
    });
  });
})();
