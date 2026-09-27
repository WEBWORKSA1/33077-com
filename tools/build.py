#!/usr/bin/env python3
"""33077.com static site generator.
Run:  python3 tools/build.py   (from repo root). Writes every *.html page at the repo root.
Shared header, top interest bar, footer, SEO tags and JSON-LD come from this one file.
Page bodies live in tools/pages.py.
"""
import json, os, subprocess, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://33077.com"
TODAY = datetime.date.today().isoformat()
VER = TODAY.replace("-", "")

# load number data from assets/js/data.js so the JS tools and static pages share one source
_js = subprocess.run(["node", "-e", 'global.window={};require("./assets/js/data.js");process.stdout.write(JSON.stringify({D:window.DIGITS,C:window.CODES,Z:window.ZODIAC}))'],
                     cwd=ROOT, capture_output=True, text=True, check=True).stdout
DATA = json.loads(_js)

NAV = [("decoder.html", "Decoder"), ("love-codes.html", "Love Codes"), ("lucky-score.html", "Lucky Score"),
       ("zodiac.html", "Zodiac"), ("festivals.html", "Festivals"), ("economy.html", "Economy"), ("videos.html", "Videos")]
MORE = [("meanings.html", "Number Meanings 0–9"), ("concierge.html", "Lucky Number Concierge"), ("contests.html", "Contests & Prizes"),
        ("support.html", "Support 33077"), ("careers.html", "Join the Team"), ("advertise.html", "Advertise & Sponsor"),
        ("about.html", "About"), ("contact.html", "Contact"), ("legal.html", "Trademark, Copyright & Privacy")]

e = html.escape

def faq_block(items, title="Frequently asked questions"):
    body = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in items)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(__import__('re').sub('<[^>]+>', '', a))}} for q, a in items]}
    return f'<h2>{e(title)}</h2>{body}', ld

def ad(slot="content"):
    return f'<div class="ad" data-slot="{slot}" aria-label="Advertisement"></div>'

def crumbs(title):
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><a href="index.html">Home</a> › <span>{e(title)}</span></nav>'

def page_hero(eyebrow, h1, lead, extra=""):
    return f'<header class="page-hero"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div></header>'

def layout(fn, title, desc, body, lds=(), crumb=None, og_type="website"):
    url = DOMAIN + "/" + ("" if fn == "index.html" else fn)
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h == fn else ""}>{t}</a>' for h, t in NAV)
    drawer = "".join(f'<a href="{h}">{t}</a>' for h, t in [("index.html", "Home")] + NAV + MORE)
    ld_all = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}] + ([{"@type": "ListItem", "position": 2, "name": crumb, "item": url}] if crumb else [])}] + list(lds)
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld_all)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#C8102E">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="33077 — The Chinese Number Code Hub">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={VER}">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{ld_html}
</head>
<body data-base="">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="https://web.works/contact" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership</a></div>
<header class="hdr"><div class="wrap">
  <a class="logo" href="index.html" aria-label="33077 home"><span class="logo-mark">亲</span><span>33077<small>CHINESE NUMBER CODE HUB</small></span></a>
  <nav class="nav" aria-label="Main">{nav}<a class="cta" href="concierge.html">Concierge</a></nav>
  <button class="icon-btn theme-btn" type="button" aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
  <button class="icon-btn menu-btn" type="button" aria-label="Open menu" aria-expanded="false">☰</button>
</div></header>
<div class="drawer" aria-label="Menu"><div class="panel"><div class="row" style="justify-content:space-between;margin-bottom:8px"><b>Menu</b><button class="icon-btn close-drawer" type="button" aria-label="Close menu">✕</button></div>{drawer}</div></div>
{crumbs(crumb) if crumb else ""}
<main id="main">
{body}
</main>
<footer class="ftr"><div class="wrap">
  <div class="grid">
    <div><a class="logo" href="index.html" style="color:#fff"><span class="logo-mark">亲</span><span>33077<small style="color:#a99">想想你亲亲 · thinking of you</small></span></a>
      <p class="small" style="margin-top:12px">Decode any number’s meaning in Chinese culture, build secret love codes, score lucky numbers and explore the economy of luck — from lunar 3/3 to 7/7.</p>
      <form class="js-form" data-subject="Newsletter signup" data-ok="You’re in! Watch for the number of the week.">
        <label for="nl-email" style="color:#fff">Number of the week — free email</label>
        <div class="row" style="flex-wrap:nowrap"><input id="nl-email" type="email" name="email" required placeholder="you@email.com" autocomplete="email"><input type="hidden" name="form" value="newsletter"><button class="btn gold" type="submit">Join</button></div>
      </form>
    </div>
    <div><h4>Tools</h4><ul><li><a href="decoder.html">Number Decoder</a></li><li><a href="love-codes.html">Love Code Builder</a></li><li><a href="lucky-score.html">Lucky Number Score</a></li><li><a href="zodiac.html">Zodiac & Compatibility</a></li><li><a href="festivals.html">Festival Countdown</a></li></ul></div>
    <div><h4>Explore</h4><ul><li><a href="meanings.html">Meanings 0–9</a></li><li><a href="economy.html">Economy of Luck</a></li><li><a href="videos.html">Videos</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    <div><h4>Get involved</h4><ul><li><a href="concierge.html">Lucky Number Concierge</a></li><li><a href="contests.html">Contests & Prizes</a></li><li><a href="support.html">Support / Donate</a></li><li><a href="careers.html">Careers & Talent</a></li><li><a href="advertise.html">Advertise & Sponsor</a></li><li><a href="https://web.works/contact" target="_blank" rel="noopener">Buy / partner on this domain</a></li></ul></div>
  </div>
  <div class="legal-line">© <span class="year-now">2026</span> 33077.com. Original content © its authors; all rights reserved. “33077” is used on this site descriptively as a number and is not claimed as a trademark; this site is not affiliated with any company, product, postal code or ticker that uses the same digits. Third-party names and trademarks belong to their owners. Tools are for entertainment and cultural education — not financial, legal or religious advice. <a href="legal.html">Trademark, Copyright & Privacy</a> · <a href="legal.html#terms">Terms</a> · <a href="legal.html#privacy">Privacy</a></div>
</div></footer>
<nav class="bottom-nav" aria-label="Quick"><a href="decoder.html"><span>解</span>Decode</a><a href="love-codes.html"><span>爱</span>Love</a><a href="lucky-score.html"><span>吉</span>Luck</a><a href="zodiac.html"><span>龙</span>Zodiac</a><a href="concierge.html"><span>找</span>Concierge</a></nav>
<div class="ad-sticky" data-slot="sticky"></div>
<div class="cookie" role="dialog" aria-label="Cookie notice"><p class="small" style="margin:0 0 10px">We use cookies for preferences, analytics and ads (Google AdSense), and YouTube videos load only when you press play. See our <a href="legal.html#privacy">privacy policy</a>.</p><div class="row"><button class="btn sm" data-consent="all">Accept</button><button class="btn sm ghost" data-consent="essential">Essential only</button></div></div>
<script src="assets/js/config.js?v={VER}"></script>
<script src="assets/js/data.js?v={VER}"></script>
<script src="assets/js/dates.js?v={VER}"></script>
<script src="assets/js/tools.js?v={VER}"></script>
<script src="assets/js/main.js?v={VER}"></script>
</body>
</html>
'''

def write(fn, *a, **k):
    with open(os.path.join(ROOT, fn), "w", encoding="utf-8") as f:
        f.write(layout(fn, *a, **k))

if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import pages
    pages.build(sys.modules[__name__])
    # sitemap
    files = ["index.html"] + [h for h, _ in NAV] + [h for h, _ in MORE]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f'  <url><loc>{DOMAIN}/{"" if f == "index.html" else f}</loc><lastmod>{TODAY}</lastmod><priority>{"1.0" if f == "index.html" else "0.8"}</priority></url>\n' for f in files) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    print("built", len(files), "pages + 404")
