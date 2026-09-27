# 33077.com — The Chinese Number Code Hub

**想想你亲亲 — “thinking of you, kiss kiss.”** A fast, fully static website that decodes any number’s meaning in Chinese culture, builds love codes, scores lucky numbers, and turns that traffic into revenue through AdSense, YouTube, a lead-gen concierge, sponsorships, donations and contests.

Hosted free on **GitHub Pages**. No framework, no build step at runtime.

## Pages
| Page | Purpose |
|---|---|
| `index.html` | Hero decoder, tools, 3/3→7/7 story, love codes, videos, festivals, FAQ |
| `decoder.html` | Number Decoder (exact codes, hidden codes, homophones, luck score) |
| `love-codes.html` | Love Code Builder + searchable dictionary |
| `lucky-score.html` | Phone / plate / address / domain / price / date luck score |
| `zodiac.html` | Zodiac finder (exact Lunar New Year dates 1924–2035) + compatibility |
| `festivals.html` | Live countdowns: Shangsi, 520, Qixi, Mid-Autumn, Lunar New Year… |
| `meanings.html`, `economy.html`, `videos.html`, `about.html` | Content & SEO |
| `concierge.html` | **Lead generation** — 3-step Lucky Number Concierge |
| `support.html` | Donations, memberships, funding goal |
| `contests.html` | Love Code Challenge, prizes, official rules |
| `careers.html` | Talent hiring |
| `advertise.html` | Sponsorship packages & media-kit form |
| `contact.html`, `legal.html`, `404.html` | Contact, trademark/copyright/privacy/terms |

## Configure (one file: `assets/js/config.js`)
- **AdSense:** set `adsenseClient` (`ca-pub-…`) and optional `adSlots`; update `ads.txt`. Until then, slots show house ads for sponsorship/concierge/support.
- **Donations:** paste PayPal / Ko-fi / Buy Me a Coffee / Stripe links in `donate`. The pledge form always works.
- **Funding goal, contest dates & prizes, YouTube channel and videos** are all in the same file.
- **Forms:** every form posts via FormSubmit to the owner inbox, which is stored encoded and never appears in the page. The **first** submission triggers a one-time FormSubmit activation email to the owner — click it once to activate.

## Edit pages
Page bodies live in `tools/pages.py`; the shared header, top interest bar, footer and SEO tags are in `tools/build.py`.
```bash
python3 tools/build.py   # regenerates all *.html and sitemap.xml (needs Python 3 + Node)
```

## Custom domain
In **Settings → Pages**, set the custom domain to `33077.com` (this adds a `CNAME` file), then point DNS:
`A` records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, and `www` CNAME → `webworksa1.github.io`. Enable “Enforce HTTPS”.

## Legal
“33077” is used descriptively as a number; no trademark is claimed in it and the site is not affiliated with any other user of the digits. See `legal.html`.
Interested in this website, domain, sponsorship, advertising or partnership? → https://web.works/contact
