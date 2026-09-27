# 33077.com — Research Findings, Website Decision & Phase-Wise Build Prompt

*Prepared for Web · September 27, 2026*

---

## Part 1 — What "33 0 77" means (research summary)

| Part | Chinese reading | Status |
|---|---|---|
| **3** (sān) | Sounds like 生 shēng "life/birth" (lucky). In online love-codes 3 = 想 "miss / think of" (530 = 我想你 "I miss you") | Established |
| **33** | 生生 / 想想 · 33 roses = love "for three lifetimes" (bouquets of 33 grew by triple digits on Taobao at Qixi 2025) · Lunar 3/3 = 上巳节 Shangsi (Double Third) + Zhuang 三月三 song festival (Guangxi public holiday, national intangible heritage since 2014) | Established |
| **0** (líng) | In love-codes 0 = 你 "you" (520, 530, 770). Domain traders value 0 lower, esp. leading | Established |
| **7** (qī) | Mixed: 妻 wife, 亲 kiss/dear (770 = 亲亲你), 起 arise — but also 气 anger, 去 "gone", ghost month (7th lunar month), 头七 | Established (mixed) |
| **77** | 七夕 Qixi (7th day of 7th lunar month) = Chinese Valentine's Day · 亲亲 "kiss kiss" | Established |
| **33077 as a whole** | **想想你亲亲 "Thinking of you — kiss kiss"** (strongest, all parts from existing codes; closest existing code: 53770 我想亲亲你). Also a symbolic "from 3/3 to 7/7" — spanning China's two love festivals | **Constructed** (new, ownable) |

**Economy of lucky numbers (verified figures)**
- HK plate "W" HK$26M (2021, record); "R" HK$25.5M (2023); "18" HK$16.5M (2008).
- Sichuan Airlines paid ¥2.33M for phone number 8888-8888 (2003).
- Beijing Olympics opened 8:08pm on 8/8/08; ~9,000 Beijing couples married that day.
- Lucky stock tickers trade at an IPO premium that fades within 3 years (Hirshleifer, Jian & Zhang).
- 5N .com market H1-2026: 349 public sales, median $66 (wholesale floor), top 18000.com $24,251.
- Qixi 2025: flower pre-orders +132% YoY; Qixi menus priced ¥588–¥1,314; jewellery group-buys +255%.
- China marriage registrations 2025: 6.76M; 520 (May 20) is a peak registration date.

**Honest domain assessment:** 33077 is a mid-grade 5N. No 4 (good), but a 0 and two 7s make it less valuable to Chinese resale buyers than 8/6/9-heavy numbers. Its real edge is the **constructed love-code meaning + the 3/3→7/7 festival story** — that's a brand, not a resale flip. Build it.

---

## Part 2 — The website decision

**Winner: "33077 — The Chinese Number Code Hub"**
An interactive decoder + love-code + lucky-number platform, with a high-intent lead-gen concierge.

Why this beats the alternatives (dating site, domain-for-sale lander, generic zodiac blog):

1. **Tool traffic compounds.** Calculator/decoder pages (calculator.net, omnicalculator model) earn repeat + share traffic and long AdSense sessions.
2. **Seasonal spikes you can own:** 520 (May 20), Qixi (Aug 8 2027), Chinese New Year (Feb 6 2027, Year of the Goat), 11.11, 8/8. The domain *is* the Qixi story.
3. **Lead-gen money is in lucky-number buying:** plates, phone numbers, numeric domains, auspicious dates, China-market pricing/naming audits. Those leads sell to brokers/consultants at far higher value than ad RPM.
4. **Low cost:** 100% static, runs free on GitHub Pages.

**Revenue stack:** AdSense (tool results, in-content, sticky) · YouTube embeds + own channel · lead-gen concierge (broker referral fees) · sponsorships/house ads · donations/memberships · contests (sponsor-funded) · affiliates (language courses, travel, number/plate sellers, domain marketplaces).

---

## Part 3 — Phase-wise build prompt

Paste each phase into your AI builder in order. Phase 0 is shared context and should be pasted first every time.

### PHASE 0 — Context (always include)
```
You are building 33077.com — "The Chinese Number Code Hub": a modern, fast, fully static,
mobile-first website hosted free on GitHub Pages (no server, no build step required at runtime).
Brand story: 33077 reads as 想想你亲亲 ("thinking of you — kiss kiss") and spans China's two love
festivals, lunar 3/3 (Shangsi) and 7/7 (Qixi). The site decodes any number's Chinese meaning,
generates love codes, scores lucky numbers, and explains the lucky-number economy.
Rules:
- Pure HTML/CSS/vanilla JS. All links relative (site must work under /33077-com/ subpath AND a custom domain).
- Palette: Chinese red #C8102E, gold #F2B705, warm off-white #FFF8EE, ink #141414; dark mode with gold accents.
- Fonts: Inter + Noto Sans SC / Noto Serif SC (Google Fonts). Big tabular numerals, 汉字 + pinyin lines.
- Top of EVERY page: a slim bar reading "Contact, if you are interested in this website / domain name /
  Sponsorship / Advertisement / Partnership" linking to https://web.works/contact.
- ALL forms deliver to ONE owner email: [owner inbox — stored encoded in assets/js/config.js]. This email must NEVER appear in HTML,
  text, mailto links, README, or any public file. Store it only Base64-encoded in config.js and build the
  FormSubmit (formsubmit.co/ajax/) endpoint at runtime in JS.
- No use of "33077" as a claimed trademark. Include a Trademark & Copyright disclosure page.
- Accessibility (WCAG AA), SEO (titles, meta, OG, JSON-LD, sitemap), Core Web Vitals friendly.
```

### PHASE 1 — Foundation & design system
```
Create: assets/css/style.css (tokens, light/dark, grid, cards, buttons, forms, ad slots, badges),
assets/js/config.js (site name, encoded email, AdSense client ID empty by default, donation links,
contest settings, YouTube IDs), assets/js/main.js (header/nav, mobile drawer + sticky bottom nav,
theme toggle, cookie consent, form handler, ad loader, countdowns, share buttons).
Generate pages from one Python template (tools/build.py) so header/footer/top bar stay identical.
Deliver favicon.svg, manifest.webmanifest, robots.txt, sitemap.xml, ads.txt placeholder, 404.html, .nojekyll.
```

### PHASE 2 — Core tools (traffic engines)
```
1. Number Decoder (decoder.html + hero widget): input any number → exact love-code matches
   (520, 1314, 3344, 530, 770, 53770, 88, 168, 518, 250, 748, 233…), greedy segmentation into known
   codes, per-digit homophones with 汉字/pinyin, luck verdict, share button, example chips.
2. Love Code Generator (love-codes.html): pick phrases → build a number code; full searchable dictionary
   grouped by romance / everyday / business / insult (with "kid-safe" tag).
3. Lucky Number Score (lucky-score.html): phone / plate / address / domain → 0–100 score, grade,
   digit breakdown, pattern bonuses (888, 168, ending in 8), penalties (4, 14, 250, 748). Entertainment disclaimer.
4. Zodiac Finder (zodiac.html): birth date → animal + element using a lunar new year table,
   lucky numbers/colours, compatibility checker (triads, six harmonies, clashes), 2026 Fire Horse / 2027 Fire Goat.
5. Festival Countdown (festivals.html): Shangsi 3/3, 520, Qixi 7/7, Mid-Autumn, CNY with live countdowns from a date table.
```

### PHASE 3 — Content & SEO
```
meanings.html (0–9 encyclopedia + FAQ with FAQPage schema), economy.html (plates, phones, Olympics,
floors, pricing, stock tickers, 5N domains — each fact linked to its source), videos.html (lite YouTube
facade, youtube-nocookie, lazy iframe), about.html. Every page: breadcrumb, FAQ, related tools, internal links.
```

### PHASE 4 — Lead generation (dedicated, high-conversion)
```
concierge.html — "Lucky Number Concierge": 3-step form with progress bar.
Step 1 goal cards: buy a lucky phone number · lucky licence plate · numeric/premium domain · sell or value
my number/domain · auspicious date (wedding/opening/move) · China-market brand, pricing & naming audit ·
sponsorship/partnership. Step 2: the number/asset, budget band, country, timeline. Step 3: name, email,
phone/WhatsApp/WeChat (optional), consent checkbox. Trust bar, 24-hour response promise, FAQ.
Inline mini-CTAs after every tool result pointing to the concierge. Newsletter capture in footer.
Honeypot + timing check for spam. Thank-you state with share prompt.
```

### PHASE 5 — Monetization
```
AdSense: loader activates only when config.adsenseClient is set; slots below hero, after result, in-content,
sidebar, mobile sticky; never between input and result. When not set, show house ads linking to advertise.html.
advertise.html: sponsorship packages (Festival Sponsor, Tool "Presented by", Newsletter, Contest title sponsor),
media-kit request form. YouTube hub + channel CTA. Affiliate disclosure.
```

### PHASE 6 — Community: donations, contests, hiring
```
support.html: lucky-amount presets ($3.30, $7.70, $8.88, $33.07, custom), purpose selector (operations,
promotions, marketing, hiring talent, contest prizes), goal progress bar, supporter wall, membership tiers,
pledge form; external payment buttons (PayPal/Ko-fi/Buy Me a Coffee/Stripe links) rendered only if set in config.
contests.html: "Love Code Challenge" — countdown to Qixi, prizes, entry form, bonus-entry share links,
official rules (no purchase necessary, eligibility, judging, privacy), past winners wall.
careers.html: talent roles (writers, Mandarin translators, video creators, designers, campus ambassadors,
sales partners) with application form.
```

### PHASE 7 — Legal, performance, deploy
```
legal.html: Trademark disclosure (33077 used descriptively as a number; no trademark claim; no affiliation with
any company, postal code, product or ticker using it; third-party marks belong to owners), Copyright notice,
Privacy (forms, cookies, AdSense, YouTube), Terms, Affiliate & donation disclosures, entertainment disclaimer.
Performance: no frameworks, deferred JS, lazy images/iframes, preconnect fonts.
Deploy: push to GitHub repo WEBWORKSA1/33077-com (public), publish via GitHub Pages (branch deploy),
then point 33077.com DNS (A records 185.199.108-111.153 + CNAME file) when ready.
```

### PHASE 8 — Growth roadmap (post-launch)
```
Programmatic pages /n/520.html for top 300 codes · 简/繁 language versions · shareable OG result images ·
daily "number of the day" email · Qixi/520/CNY campaigns · sponsor-funded contests · paid PDF reports.
```

---

## Sources
- [Wikipedia — Chinese numerology](https://en.wikipedia.org/wiki/Chinese_numerology)
- [ShawnLiv — Chinese love numbers](https://shawnliv.com/chinese-love-numbers-and-the-meaning/)
- [LingoAce — Chinese number slang](https://www.lingoace.com/blog/chinese-number-slang/)
- [Wikipedia — Double Third Festival](https://en.wikipedia.org/wiki/Double_Third_Festival)
- [Wikipedia — Qixi Festival](https://en.wikipedia.org/wiki/Qixi_Festival)
- [Global Times — Qixi 2025 consumption](https://www.globaltimes.cn/page/202508/1342066.shtml)
- [SCMP — HK plate auctions](https://www.scmp.com/news/hong-kong/society/article/3209965/lucky-car-number-plate-letter-r-sells-hk25-million-auction-hong-kong)
- [China Daily — 8888-8888 phone number](https://www.chinadaily.com.cn/en/doc/2003-08/19/content_256178.htm)
- [CBC — China's craze for 08-08-08](https://www.cbc.ca/news/world/china-s-craze-for-08-08-08-1.706200)
- [GGRG — 5N .com sales data](https://report.ggrg.com/period-data/5n-a/)
- [MediaOptions — Numeric domain value in Chinese culture](https://mediaoptions.com/blog/understanding-numeric-domain-value-in-chinese-culture/)
- [UCI — Superstition and financial decision making](https://sites.uci.edu/dhirshle/abstracts/superstition-and-financial-decision-making/)
- [Xinhua — marriage registrations 2026](https://english.news.cn/20260521/dffae732c7da4f22ab7056169923ef1d/c.html)
- 40 competitor sites audited (yourchineseastrology, chinasage, mdbg, yellowbridge, numerology.com, cafeastrology, fengshuinexus, regtransfers, nationalnumbers, numberbarn, afternic, calculator.net, omnicalculator, buymeacoffee, ko-fi, gleam, kickstarter, patreon, gofundme, and others).
