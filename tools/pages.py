"""Page bodies for 33077.com. Called by build.py."""
import html
e = html.escape


def build(B):
    D, C, Z = B.DATA["D"], B.DATA["C"], B.DATA["Z"]
    CODEMAP = {c[0]: c for c in C}

    def code_card(n):
        c = CODEMAP[n]
        return (f'<a class="card" href="decoder.html?n={n}"><div class="row" style="justify-content:space-between">'
                f'<span class="big-num num" style="font-size:2.4rem">{n}</span><span class="han" style="font-size:1.3rem">{c[1]}</span></div>'
                f'<div class="small muted">{c[2]}</div><p style="margin:.3em 0 0;font-weight:700">“{e(c[3])}”</p></a>')

    decoder_form = lambda fid, url=False, big=True: f'''
<form class="decoder" data-out="{fid}" {"data-url" if url else ""} role="search" aria-label="Number decoder">
  <div class="search-xl"><label for="{fid}-in" class="skip">Number to decode</label>
    <input id="{fid}-in" inputmode="numeric" pattern="[0-9 +\\-]*" maxlength="24" placeholder="Enter any number… e.g. 520" autocomplete="off">
    <button class="btn" type="submit">Decode</button></div>
  <div class="chips">{"".join(f'<button type="button" class="chip" data-n="{n}">{n}</button>' for n in ["33077","520","1314","168","888","3344","530","250","7758","5201314"])}</div>
</form>'''

    lead_band = lambda h="Want a luckier number — or to sell yours?", p="The 33077 Concierge matches you with vetted brokers for lucky phone numbers, licence plates, numeric domains and auspicious dates. Free to ask, no obligation.": f'''
<section><div class="wrap"><div class="cta-band"><div><span class="eyebrow" style="color:var(--gold)">Lucky Number Concierge</span><h2>{h}</h2><p style="margin:0">{p}</p></div>
<div class="row"><a class="btn gold" href="concierge.html">Get matched free →</a><a class="btn ghost" style="color:#fff;border-color:#ffffff66" href="concierge.html?goal=sell">Value my number</a></div></div></div></section>'''

    # ------------------------------------------------------------------ HOME
    faq, ld = B.faq_block([
        ("What does 33077 mean in Chinese?", "Read as number slang, 3 = 想 (miss), 0 = 你 (you) and 77 = 亲亲 (kiss kiss), so 33077 becomes <b>想想你亲亲 — “thinking of you, kiss kiss.”</b> It also joins China’s two love festivals: lunar 3/3 (Shangsi) and 7/7 (Qixi). The phrase is a new code built from established parts."),
        ("Why do Chinese people care so much about numbers?", "Chinese has many words that sound alike, so digits pick up the meaning of words they sound like: 8 (bā) sounds like 发 “prosper”, 4 (sì) like 死 “death”. It affects prices, phone numbers, plates, addresses and wedding dates."),
        ("What is the luckiest number in Chinese culture?", "8 is the most sought after, followed by 6 (smooth) and 9 (long-lasting). The Beijing Olympics opened at 8:08 pm on 8/8/2008."),
        ("Is the lucky score scientific?", "No — it measures cultural perception, which is what buyers pay for. Use it for fun, naming and pricing ideas, not as financial advice."),
        ("Can I buy a lucky number through 33077?", "Yes. Our <a href='concierge.html'>Concierge</a> takes your request for a phone number, plate, numeric domain or auspicious date and connects you with vetted sellers and brokers.")])
    home = f'''
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">解码数字 · Decode the numbers</span>
    <h1>What does your number <span class="hl">really</span> say in Chinese?</h1>
    <p class="lead">Type any phone number, price, date or plate. We decode its hidden Chinese meaning, spot love codes like <b>520</b> and score its luck — in one second.</p>
    {decoder_form("home-out")}
    <div id="home-out" class="result" aria-live="polite"></div>
  </div>
  <div class="seal">
    <div class="small muted" style="letter-spacing:.14em">THE CODE BEHIND THE NAME</div>
    <div class="big-num num">33<span class="g">0</span>77</div>
    <div class="han" style="margin-top:6px">想想你 · 亲亲</div>
    <p class="muted" style="margin:.3em 0 1em">“Thinking of you — kiss kiss”</p>
    <div class="grid g3" style="gap:10px;text-align:center">
      <div class="card" style="padding:12px"><b class="num" style="font-size:1.5rem;color:var(--red)">33</b><div class="han">想想 · 三月三</div><div class="small muted">miss you · Shangsi 3/3</div></div>
      <div class="card" style="padding:12px"><b class="num" style="font-size:1.5rem;color:var(--gold-2)">0</b><div class="han">你</div><div class="small muted">you</div></div>
      <div class="card" style="padding:12px"><b class="num" style="font-size:1.5rem;color:var(--red)">77</b><div class="han">亲亲 · 七夕</div><div class="small muted">kiss kiss · Qixi 7/7</div></div>
    </div>
    <a class="btn block" style="margin-top:16px" href="love-codes.html">Build your own love code</a>
  </div>
</div></section>
{B.ad("top")}
<section><div class="wrap">
  <span class="eyebrow">Free tools</span><h2>Six ways to read the numbers</h2>
  <div class="grid g3" style="margin-top:20px">
    <a class="card" href="decoder.html"><div class="ico">解</div><h3>Number Decoder</h3><p class="muted" style="margin:0">Any number → hidden codes, homophones, luck verdict.</p></a>
    <a class="card" href="love-codes.html"><div class="ico">爱</div><h3>Love Code Builder</h3><p class="muted" style="margin:0">Turn “I miss you” into 530. 50 codes, one tap to share.</p></a>
    <a class="card" href="lucky-score.html"><div class="ico">吉</div><h3>Lucky Number Score</h3><p class="muted" style="margin:0">Rate a phone, plate, address, domain or price 0–100.</p></a>
    <a class="card" href="zodiac.html"><div class="ico">马</div><h3>Zodiac & Compatibility</h3><p class="muted" style="margin:0">Your animal, element, lucky digits and love match.</p></a>
    <a class="card" href="festivals.html"><div class="ico">夕</div><h3>Festival Countdown</h3><p class="muted" style="margin:0">Shangsi, 520, Qixi, Mid-Autumn and Lunar New Year.</p></a>
    <a class="card" href="meanings.html"><div class="ico">〇</div><h3>Meanings 0–9</h3><p class="muted" style="margin:0">Every digit’s sound, symbolism and do’s and don’ts.</p></a>
  </div>
</div></section>
<section class="sec-alt"><div class="wrap hero-grid">
  <div><span class="eyebrow">From 3/3 to 7/7</span><h2>Two love festivals, one number</h2>
  <p class="lead">Lunar <b>3/3</b> is 上巳节 Shangsi, the ancient spring festival of courtship — still celebrated as the Zhuang people’s 三月三 song festival. Lunar <b>7/7</b> is 七夕 Qixi, when the Cowherd and the Weaver Girl meet across the Milky Way. 33077 sits between them.</p>
  <p><b>Next Qixi:</b> <span data-fest-date="qixi">—</span></p><div class="cd" data-next-fest="qixi" aria-live="off"></div>
  <p style="margin-top:16px"><a href="festivals.html">See every festival date →</a></p></div>
  <div class="grid g2">
    <div class="card stat"><b>HK$26M</b>Paid for Hong Kong plate “W” at auction, 2021 — a record.</div>
    <div class="card stat"><b>¥2.33M</b>Paid by Sichuan Airlines for phone number 8888-8888 in 2003.</div>
    <div class="card stat"><b>~9,000</b>Beijing couples married on 08-08-2008, more than double the old record.</div>
    <div class="card stat"><b>+132%</b>Growth in Qixi 2025 flower pre-orders on Taobao Flash Sale.</div>
  </div>
</div></section>
<section><div class="wrap">
  <div class="row" style="justify-content:space-between"><div><span class="eyebrow">Most searched</span><h2>Chinese love codes everyone should know</h2></div><a class="btn ghost sm" href="love-codes.html">All 50 codes →</a></div>
  <div class="grid g4" style="margin-top:20px">{"".join(code_card(n) for n in ["520","1314","5201314","3344","530","770","9420","33077"])}</div>
</div></section>
{lead_band()}
<section class="sec-alt"><div class="wrap">
  <div class="row" style="justify-content:space-between"><div><span class="eyebrow">Watch</span><h2>Numbers, explained on video</h2></div><a class="btn ghost sm" href="videos.html">Video hub →</a></div>
  <div class="grid g3" style="margin-top:20px" data-videos="3"></div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">Coming up</span><h2>Festival calendar</h2>
  <div id="fest-list" data-n="4" class="grid g4" style="margin-top:20px"></div>
</div></section>
{B.ad("content")}
<section class="sec-alt"><div class="wrap">
  <span class="eyebrow">Be part of 33077</span><h2>Win, support, work, sponsor</h2>
  <div class="grid g4" style="margin-top:20px">
    <a class="card" href="contests.html"><div class="ico">奖</div><h3>Love Code Challenge</h3><p class="muted" style="margin:0">Create the best number code — win cash prizes at Qixi.</p></a>
    <a class="card" href="support.html"><div class="ico">助</div><h3>Support us</h3><p class="muted" style="margin:0">Fund new tools, contests and translators. From $3.30.</p></a>
    <a class="card" href="careers.html"><div class="ico">才</div><h3>Join the team</h3><p class="muted" style="margin:0">Writers, translators, video creators, ambassadors.</p></a>
    <a class="card" href="advertise.html"><div class="ico">商</div><h3>Advertise</h3><p class="muted" style="margin:0">Sponsor a tool, festival or the newsletter.</p></a>
  </div>
</div></section>
<section><div class="wrap prose" style="margin:0 auto">{faq}</div></section>'''
    B.write("index.html", "33077 — What Does Your Number Mean in Chinese? Decoder, Love Codes & Lucky Numbers",
            "Decode any number’s Chinese meaning, discover love codes like 520 and 1314, score lucky phone numbers and plates, and find your zodiac — free tools from 33077.com.",
            home, lds=[{"@context": "https://schema.org", "@type": "WebSite", "name": "33077", "alternateName": "The Chinese Number Code Hub", "url": B.DOMAIN + "/",
                        "potentialAction": {"@type": "SearchAction", "target": B.DOMAIN + "/decoder.html?n={number}", "query-input": "required name=number"}}, ld])

    # ------------------------------------------------------------------ DECODER
    faq, ld = B.faq_block([
        ("How does the number decoder work?", "It checks your number against our dictionary of established Chinese number codes (520, 1314, 3344…), finds codes hidden inside longer numbers, then reads each remaining digit by its most common homophone and gives a cultural luck score."),
        ("Can I decode a phone number?", "Yes — spaces, dashes and + are ignored. Up to 20 digits."),
        ("Why does 4 score so low?", "四 (sì) sounds like 死 (sǐ, death). Many Chinese buildings skip 4th and 14th floors, and plates or phone numbers with 4 sell for less."),
        ("Is 7 lucky or unlucky?", "Both. It reads as 亲 (kiss) or 妻 (wife) in love codes and marks Qixi on 7/7 — but the 7th lunar month is Ghost Month and 748 is an insult. We rate it neutral."),
        ("Where do these meanings come from?", "Chinese homophones and widely used internet slang. See our <a href='meanings.html'>meanings guide</a> and <a href='about.html#standards'>editorial standards</a>.")])
    body = B.page_hero("解码器 · Decoder", "Chinese Number Decoder", "Type any number — we reveal its hidden Chinese meaning, love codes and luck score.") + f'''
<section><div class="wrap layout"><div>
  {decoder_form("dec-out", url=True)}
  <div id="dec-out" class="result" aria-live="polite"><div class="note">Try <b>33077</b>, your phone number, or the price on your last receipt.</div></div>
  {B.ad("content")}
  <div class="prose"><h2>How Chinese number meanings work</h2>
  <p>Mandarin has only about 400 distinct syllables, so many words sound alike. Digits borrow the meaning of the words they sound like: <b>8 (bā)</b> ≈ 发 fā “prosper”, <b>4 (sì)</b> ≈ 死 sǐ “death”, <b>9 (jiǔ)</b> ≈ 久 jiǔ “long-lasting”. Online, young people string digits into whole sentences — <b>520</b> = 我爱你 “I love you”.</p>
  <p>The decoder reads your number three ways: <b>exact codes</b>, <b>hidden codes</b> inside longer numbers, and <b>digit-by-digit homophones</b>, then weighs lucky and unlucky patterns into a 0–100 score.</p>
  {faq}</div>
</div><aside class="sidebar"><div class="sticky">
  <div class="card"><h3>Related tools</h3><p><a href="love-codes.html">Love Code Builder →</a></p><p><a href="lucky-score.html">Lucky Number Score →</a></p><p style="margin:0"><a href="zodiac.html">Zodiac finder →</a></p></div>
  {B.ad("sidebar")}
  <div class="card"><h3>Need a lucky number?</h3><p class="small muted">Phones, plates, domains, dates — tell us what you want.</p><a class="btn block" href="concierge.html">Get matched</a></div>
</div></aside></div></section>'''
    B.write("decoder.html", "Chinese Number Decoder — What Does My Number Mean in Chinese? | 33077",
            "Free Chinese number meaning decoder: find love codes (520, 1314), hidden homophones and a luck score for any phone number, price or date.", body,
            lds=[ld, {"@context": "https://schema.org", "@type": "WebApplication", "name": "Chinese Number Decoder", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}], crumb="Decoder")

    # ------------------------------------------------------------------ LOVE CODES
    faq, ld = B.faq_block([
        ("What does 520 mean?", "520 (wǔ èr líng) sounds like 我爱你 wǒ ài nǐ, “I love you”. May 20 has become an unofficial Valentine’s Day in China."),
        ("What does 1314 mean?", "一生一世 “for a whole lifetime”. 5201314 means “I love you for a lifetime”."),
        ("What does 3344 mean?", "生生世世 “life after life, forever” — a rare case where 4 is positive."),
        ("What does 77 mean?", "亲亲 “kiss kiss”, and 七夕 Qixi — the 7th day of the 7th lunar month, Chinese Valentine’s Day."),
        ("Which number codes should I avoid?", "250 (idiot), 748 (go die), 7456 (I’m furious) and anything with 14 (要死). Our dictionary tags these “Avoid”.")])
    body = B.page_hero("爱的密码 · Love codes", "Chinese Love Codes & Number Slang", "Build a secret number message, then browse the full dictionary of Chinese number codes — romantic, lucky, funny and the ones to avoid.") + f'''
<section><div class="wrap layout"><div>
  <div class="card"><h2>Love Code Builder</h2><div id="builder-out" aria-live="polite" style="min-height:120px"></div><div id="word-bank" class="chips" style="margin-top:16px"></div></div>
  {B.ad("content")}
  <div class="row" style="justify-content:space-between;margin-top:32px"><h2 style="margin:0">Number code dictionary</h2><span id="dict-count" class="muted small"></span></div>
  <div class="row" style="margin:14px 0"><input id="dict-q" style="flex:1 1 220px;width:auto;min-width:0" type="search" placeholder="Search number, 汉字 or meaning…" aria-label="Search codes"><select id="dict-cat" aria-label="Category" style="flex:0 1 190px;width:auto"><option value="">All types</option><option value="love">Love</option><option value="business">Prosperity</option><option value="life">Life</option><option value="fun">Chat slang</option><option value="insult">Avoid</option></select></div>
  <div class="tbl-wrap"><table><thead><tr><th>Code</th><th>Chinese</th><th>Meaning</th><th>Type</th></tr></thead><tbody id="dict"></tbody></table></div>
  <div class="prose" style="margin-top:32px">{faq}</div>
</div><aside class="sidebar"><div class="sticky">
  <div class="card"><h3>Enter the contest</h3><p class="small muted">Invent the best new love code before Qixi and win cash prizes.</p><a class="btn block" href="contests.html">Love Code Challenge</a></div>
  {B.ad("sidebar")}
  <div class="card"><h3>Getting married?</h3><p class="small muted">Find an auspicious date with 520, 1314 or 8s.</p><a class="btn block ghost" href="concierge.html?goal=date">Pick my date</a></div>
</div></aside></div></section>'''
    B.write("love-codes.html", "Chinese Love Codes: 520, 1314, 3344 & 50 Number Slang Meanings | 33077",
            "Every Chinese love number code explained — 520, 1314, 5201314, 3344, 530, 770 — plus a builder to create your own secret number message.", body, lds=[ld], crumb="Love Codes")

    # ------------------------------------------------------------------ LUCKY SCORE
    faq, ld = B.faq_block([
        ("How is the lucky score calculated?", "Each digit carries a traditional weight (8 = +3, 6 and 9 = +2, 4 = −3…). We add bonuses for lucky patterns (168, 888, ending in 8, no 4s) and subtract for unlucky ones (14, 250, 748, ending in 4), then scale to 0–100."),
        ("Do lucky numbers really sell for more?", "Yes. Hong Kong’s plate “W” sold for HK$26M in 2021, and Chinese phone and numeric-domain markets price 8s and 6s at a premium. See the <a href='economy.html'>Economy of Luck</a>."),
        ("Can letters be scored?", "Letters in plates or domains are ignored; only digits are scored."),
        ("Can you find me a better number?", "Yes — the <a href='concierge.html'>Concierge</a> connects you with vetted sellers of premium phone numbers, plates and domains.")])
    body = B.page_hero("吉数 · Lucky score", "Lucky Number Score", "How lucky is your phone number, plate, address, domain or price in Chinese culture? Get a 0–100 score with reasons.") + f'''
<section><div class="wrap layout"><div>
  <form id="luck-form" class="card">
    <div class="grid g2" style="gap:14px"><div class="field" style="margin:0"><label for="luck-type">What are you scoring?</label><select id="luck-type"><option value="phone">Phone number</option><option value="plate">Licence plate</option><option value="address">Address / floor / unit</option><option value="domain">Numeric domain</option><option value="price">Price</option><option value="date">Date (e.g. 20270808)</option></select></div>
    <div class="field" style="margin:0"><label for="luck-n">Number</label><input id="luck-n" required maxlength="24" placeholder="e.g. 138 8888 1688" inputmode="text"></div></div>
    <button class="btn" type="submit" style="margin-top:14px">Score it</button>
  </form>
  <div id="luck-out" class="result" aria-live="polite"></div>
  {B.ad("content")}
  <div class="prose"><h2>What the score looks at</h2>
  <div class="tbl-wrap"><table><thead><tr><th>Signal</th><th>Effect</th><th>Why</th></tr></thead><tbody>
  <tr><td>8 · 6 · 9</td><td>▲ strong</td><td>发 prosper · 溜 smooth · 久 lasting</td></tr>
  <tr><td>1 · 2 · 3</td><td>▲ mild</td><td>要 want · pairs · 生 life</td></tr>
  <tr><td>0 · 5 · 7</td><td>neutral</td><td>mixed readings</td></tr>
  <tr><td>4</td><td>▼ strong</td><td>死 death</td></tr>
  <tr><td>168 · 518 · 888 · 1314 · 520</td><td>▲ bonus</td><td>famous lucky or love codes</td></tr>
  <tr><td>14 · 250 · 748</td><td>▼ penalty</td><td>“going to die”, “idiot”, insult</td></tr>
  <tr><td>Ends in 8 / No 4 at all</td><td>▲ bonus</td><td>what buyers filter for first</td></tr></tbody></table></div>
  {faq}</div>
</div><aside class="sidebar"><div class="sticky">
  <div class="card"><h3>Sell or value your number</h3><p class="small muted">Own a lucky number, plate or 5-digit domain? Get a free valuation.</p><a class="btn block" href="concierge.html?goal=sell">Free valuation</a></div>
  {B.ad("sidebar")}
</div></aside></div></section>'''
    B.write("lucky-score.html", "Lucky Number Calculator — Is My Phone Number Lucky in Chinese? | 33077",
            "Score any phone number, licence plate, address, numeric domain or price for Chinese luck (0–100) with reasons — 8s, 6s, 9s, 4s, 168, 888 and more.", body,
            lds=[ld, {"@context": "https://schema.org", "@type": "WebApplication", "name": "Lucky Number Score", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}], crumb="Lucky Score")

    # ------------------------------------------------------------------ ZODIAC
    faq, ld = B.faq_block([
        ("What is the Chinese zodiac animal for 2026?", "2026 is the Year of the Fire Horse (丙午), from 17 February 2026 to 5 February 2027."),
        ("What is the Chinese zodiac for 2027?", "2027 is the Year of the Fire Goat (丁未), starting on 6 February 2027."),
        ("Why does my birthday in January give a different animal?", "The zodiac year starts on Lunar New Year (late January to mid-February), not 1 January. Our finder uses the exact date for 1924–2035."),
        ("Which signs are most compatible?", "The Six Harmonies (Rat–Ox, Tiger–Pig, Rabbit–Dog, Dragon–Rooster, Snake–Monkey, Horse–Goat) and the four Triads are considered best; the six Clashes (e.g. Rat–Horse) are hardest."),
        ("Are the lucky numbers per sign fixed?", "They are traditional associations; lists differ slightly between sources. Treat them as culture, not prediction.")])
    body = B.page_hero("生肖 · Zodiac", "Chinese Zodiac Finder & Compatibility", "Find your animal, element and lucky numbers from your exact birth date — then test your love match.") + f'''
<section><div class="wrap layout"><div>
  <div class="grid g2">
    <form id="zodiac-form" class="card"><h2 style="font-size:1.4rem">Find my sign</h2><div class="field"><label for="z-date">Date of birth</label><input id="z-date" type="date" required min="1924-01-01" max="2035-12-31"></div><button class="btn" type="submit">Reveal</button></form>
    <div class="card"><h2 style="font-size:1.4rem">Love compatibility</h2><div class="grid g2" style="gap:10px"><div><label for="c1">You</label><select id="c1"></select></div><div><label for="c2">Partner</label><select id="c2"></select></div></div><div id="compat-out" style="margin-top:14px" aria-live="polite"></div></div>
  </div>
  <div id="zodiac-out" class="result" aria-live="polite"></div>
  {B.ad("content")}
  <div class="grid g2" style="margin-top:24px">
    <div class="card"><div class="han" style="font-size:3rem;color:var(--red)">丙午 马</div><h3>2026 · Year of the Fire Horse</h3><p class="muted" style="margin:0">17 Feb 2026 – 5 Feb 2027. Speed, independence and bold moves. Horse’s traditional lucky numbers: 2, 3, 7.</p></div>
    <div class="card"><div class="han" style="font-size:3rem;color:var(--red)">丁未 羊</div><h3>2027 · Year of the Fire Goat</h3><p class="muted" style="margin:0">From 6 Feb 2027. Creativity, calm and community. Goat’s traditional lucky numbers: 3, 4, 9.</p></div>
  </div>
  <h2 style="margin-top:32px">Zodiac year chart 1924–2035</h2>
  <div class="tbl-wrap"><table><thead><tr><th>Animal</th><th>Years</th><th>Lucky numbers</th></tr></thead><tbody id="zodiac-chart"></tbody></table></div>
  <p class="small muted">Born in January or February? Use the finder above — the year changes at Lunar New Year.</p>
  <div class="prose">{faq}</div>
</div><aside class="sidebar"><div class="sticky">
  <div class="card"><h3>Planning a wedding or launch?</h3><p class="small muted">Get an auspicious date matched to both zodiac signs.</p><a class="btn block" href="concierge.html?goal=date">Find my date</a></div>
  {B.ad("sidebar")}
</div></aside></div></section>'''
    B.write("zodiac.html", "Chinese Zodiac Finder 2026–2027, Lucky Numbers & Compatibility | 33077",
            "Find your Chinese zodiac animal and element from your exact birth date, your lucky numbers, and your love compatibility. 2026 Fire Horse, 2027 Fire Goat.", body, lds=[ld], crumb="Zodiac")

    # ------------------------------------------------------------------ FESTIVALS
    faq, ld = B.faq_block([
        ("When is Qixi (Chinese Valentine’s Day) 2027?", "Sunday, 8 August 2027 (lunar 7/7). In 2026 it fell on 19 August."),
        ("What is the Shangsi (Double Third) Festival?", "上巳节 falls on lunar 3/3 — an ancient spring festival of bathing, outings and courtship. In Guangxi it lives on as the Zhuang 三月三 song festival, a regional public holiday listed as national intangible heritage. In 2027 it falls on 9 April."),
        ("What is 520 Day?", "20 May — “5-2-0” sounds like “I love you”. It is one of China’s busiest days for gifting and marriage registration."),
        ("Why avoid weddings in Ghost Month?", "The 7th lunar month is traditionally when spirits roam; many families avoid weddings, moves and big purchases then — even though Qixi falls in the same month.")])
    body = B.page_hero("节日 · Festivals", "Chinese Love & Luck Festival Calendar", "Live countdowns to Shangsi (3/3), 520 Day, Qixi (7/7), Mid-Autumn and Lunar New Year — with the stories behind each date.") + f'''
<section><div class="wrap">
  <div class="grid g2">
    <div class="card"><span class="badge b-love">The “77” in 33077</span><h2 style="margin-top:8px">Qixi 七夕</h2><p class="muted">Next: <b data-fest-date="qixi">—</b></p><div class="cd" data-next-fest="qixi"></div>
      <p style="margin-top:14px">A weaver-goddess and a mortal cowherd are separated by the Milky Way and allowed to meet once a year, when magpies form a bridge. Today Qixi is China’s Valentine’s Day: in 2025 Taobao Flash Sale flower pre-orders rose 132%, and bouquets of 11, 33 and 52 roses each grew by triple digits.</p></div>
    <div class="card"><span class="badge b-love">The “33” in 33077</span><h2 style="margin-top:8px">Shangsi 上巳 · 三月三</h2><p class="muted">Next: <b data-fest-date="shangsi">—</b></p><div class="cd" data-next-fest="shangsi"></div>
      <p style="margin-top:14px">On lunar 3/3, people in ancient China bathed in rivers to wash away bad luck, picnicked by the water and courted. The tradition survives as the Zhuang song festival in Guangxi, where young people once sang to find partners.</p></div>
  </div>
  {B.ad("content")}
  <h2>Upcoming dates</h2><div id="fest-list" data-n="12" class="grid g3" style="margin-top:16px"></div>
  <p class="small muted" style="margin-top:12px">Dates are for China (UTC+8), computed from the Chinese lunisolar calendar.</p>
</div></section>
{lead_band("Picking a wedding or opening date?", "Get an auspicious date shortlist — avoiding Ghost Month and matched to both zodiac signs.")}
<section><div class="wrap prose" style="margin:0 auto">{faq}</div></section>'''
    B.write("festivals.html", "Qixi 2027, 520 Day & Chinese Festival Countdown | 33077",
            "Countdowns and stories for Qixi (Chinese Valentine’s Day, 8 Aug 2027), Shangsi 3/3, 520 Day, Mid-Autumn and Lunar New Year 2027.", body, lds=[ld], crumb="Festivals")

    # ------------------------------------------------------------------ MEANINGS
    badge = lambda l: '<span class="badge b-good">Lucky</span>' if l > 0 else '<span class="badge b-bad">Unlucky</span>' if l < 0 else '<span class="badge b-mix">Neutral</span>'
    cards = "".join(
        f'<div class="card digit" id="d{d}"><div class="d num">{d}</div><div class="han">{x["han"]} <span class="small muted">{x["py"]}</span></div>'
        f'<div style="margin:6px 0">{badge(x["luck"])}</div>'
        f'<p class="small" style="text-align:left">Sounds like: {" · ".join(f"<span class=han>{s[0]}</span> {e(s[2])}" for s in x["sounds"])}</p><p class="small muted" style="text-align:left;margin:0">{e(x["note"])}</p></div>'
        for d, x in sorted(D.items()))
    faq, ld = B.faq_block([
        ("What are the lucky numbers in Chinese culture?", "8 (prosper), 6 (smooth), 9 (long-lasting) are the classic three; 2 (pairs) and 3 (life) are mildly lucky."),
        ("What are the unlucky numbers?", "4 (death) above all, plus combinations like 14, 250 and 748."),
        ("What does 0 mean in Chinese?", "零 líng. It’s neutral; in love codes it stands for 你 “you”."),
        ("What does 7 mean in Chinese?", "Mixed: 亲 kiss / 妻 wife / 起 rise in positive readings, but 气 anger and 去 gone in negative ones, and the 7th lunar month is Ghost Month.")])
    body = B.page_hero("数字含义 · Meanings", "Chinese Number Meanings 0–9", "The sound, symbolism and real-world weight of every digit — the building blocks of every code on 33077.") + f'''
<section><div class="wrap"><div class="grid g4">{cards}</div>
{B.ad("content")}
<div class="prose" style="margin:0 auto">
<h2>Combinations that matter</h2><div class="tbl-wrap"><table><thead><tr><th>Number</th><th>Chinese</th><th>Meaning</th></tr></thead><tbody>
{"".join(f"<tr><td class=num><a href='decoder.html?n={n}'><b>{n}</b></a></td><td class=han>{CODEMAP[n][1]}</td><td>{e(CODEMAP[n][3])}</td></tr>" for n in ["168","518","888","666","99","520","1314","3344","14","250","748"])}
</tbody></table></div>{faq}</div></div></section>'''
    B.write("meanings.html", "Chinese Number Meanings 0–9: Lucky & Unlucky Numbers Explained | 33077",
            "What every number from 0 to 9 means in Chinese — homophones, lucky and unlucky digits, and famous combinations like 168, 888, 520 and 250.", body, lds=[ld], crumb="Meanings")

    # ------------------------------------------------------------------ ECONOMY
    body = B.page_hero("经济 · Economy of luck", "The Economy of Lucky Numbers", "Superstition with a price tag: how 8s and 4s move money in plates, phones, property, IPOs, domains and festivals.") + f'''
<section><div class="wrap layout"><div class="prose">
<div class="grid g2" style="margin-bottom:24px"><div class="card stat"><b>HK$26M</b>Plate “W”, Hong Kong, 2021 — about 5,200× its opening bid.</div><div class="card stat"><b>¥2.33M</b>Phone number 8888-8888, Chengdu, 2003.</div></div>
<h2>Licence plates</h2><p>Hong Kong auctions vanity and lucky plates for charity. The single letter “W” set the record at HK$26 million in March 2021; “R” sold for HK$25.5 million in 2023 after opening at HK$5,000, and “18” fetched HK$16.5 million back in 2008. <a href="https://www.scmp.com/news/hong-kong/society/article/3209965/lucky-car-number-plate-letter-r-sells-hk25-million-auction-hong-kong" rel="noopener" target="_blank">SCMP</a></p>
<h2>Phone numbers</h2><p>In 2003 Sichuan Airlines paid 2.33 million yuan for 8888-8888 in Chengdu. <a href="https://www.chinadaily.com.cn/en/doc/2003-08/19/content_256178.htm" target="_blank" rel="noopener">China Daily</a> Around the 2008 Olympics, numbers ending in 6888 or 1888 went for over US$3,000. <a href="https://www.cbc.ca/news/world/china-s-craze-for-08-08-08-1.706200" target="_blank" rel="noopener">CBC</a></p>
<h2>The 08-08-08 Olympics</h2><p>Beijing opened the Games at 8:08 pm on 8 August 2008. About 9,000 couples married in Beijing that day — more than double the city’s previous single-day record. <a href="https://www.cbc.ca/news/world/china-s-craze-for-08-08-08-1.706200" target="_blank" rel="noopener">CBC</a></p>
{B.ad("content")}
<h2>Property & pricing</h2><p>Many buildings in Chinese communities skip 4th, 14th and 24th floors (Hong Kong towers sometimes skip 13 too), and retail prices tend to end in 8 rather than 9 — ¥88, ¥168, ¥888. <a href="https://en.wikipedia.org/wiki/Chinese_numerology" target="_blank" rel="noopener">Wikipedia</a></p>
<h2>Stock tickers</h2><p>Research by Hirshleifer, Jian and Zhang found Chinese firms choose lucky listing codes more often than chance. Those stocks trade at a premium after IPO — but the premium fades within three years and they underperform. <a href="https://sites.uci.edu/dhirshle/abstracts/superstition-and-financial-decision-making/" target="_blank" rel="noopener">UC Irvine</a></p>
<h2>Numeric domains</h2><p>Five-digit .com domains (“5N”) trade actively with Chinese investors. In the first half of 2026 there were 349 public 5N sales with a median of just $66 — wholesale-grade names — while the best (18000.com) sold for $24,251. Names without 4 and heavy in 8/6/9 lead the market; a leading 0 lowers value. <a href="https://report.ggrg.com/period-data/5n-a/" target="_blank" rel="noopener">GGRG</a> · <a href="https://mediaoptions.com/blog/understanding-numeric-domain-value-in-chinese-culture/" target="_blank" rel="noopener">MediaOptions</a></p>
<h2>Love festivals</h2><p>At Qixi 2025, Taobao Flash Sale flower pre-orders rose 132% year on year, restaurant set menus were priced from ¥588 to ¥1,314, and jewellery group-buys rose 255%. <a href="https://www.globaltimes.cn/page/202508/1342066.shtml" target="_blank" rel="noopener">Global Times</a> China recorded 6.76 million marriage registrations in 2025, with 520 among the peak days. <a href="https://english.news.cn/20260521/dffae732c7da4f22ab7056169923ef1d/c.html" target="_blank" rel="noopener">Xinhua</a></p>
<div class="note">For businesses: localising prices, SKUs, phone numbers and launch dates for Chinese customers is cheap and measurable. Ask the <a href="concierge.html?goal=audit">Concierge for a China-market number audit</a>.</div>
</div><aside class="sidebar"><div class="sticky">
  <div class="card"><h3>Business number audit</h3><p class="small muted">Prices, hotlines, addresses and launch dates reviewed for Chinese customers.</p><a class="btn block" href="concierge.html?goal=audit">Request an audit</a></div>
  {B.ad("sidebar")}
  <div class="card"><h3>Score a number</h3><a class="btn block ghost" href="lucky-score.html">Lucky Score tool</a></div>
</div></aside></div></section>
{lead_band()}'''
    B.write("economy.html", "The Economy of Lucky Numbers in China — Plates, Phones, Property & Domains | 33077",
            "How lucky numbers move money in China: HK$26M licence plates, ¥2.33M phone numbers, the 08-08-08 Olympics, skipped 4th floors, IPO tickers and numeric domains.", body,
            lds=[{"@context": "https://schema.org", "@type": "Article", "headline": "The Economy of Lucky Numbers in China", "datePublished": "2026-09-27", "author": {"@type": "Organization", "name": "33077.com"}}], crumb="Economy", og_type="article")

    # ------------------------------------------------------------------ VIDEOS
    body = B.page_hero("视频 · Videos", "Chinese Numbers, Explained on Video", "Hand-picked explainers on lucky numbers, number slang and Qixi. Videos load only when you press play.") + f'''
<section><div class="wrap"><div class="grid g3" data-videos="99"></div>
<div class="row" style="margin-top:24px"><a class="btn" data-channel hidden target="_blank" rel="noopener">Subscribe on YouTube</a></div>
{B.ad("content")}
<div class="grid g2"><div class="card"><h2 style="font-size:1.4rem">Creators: get featured</h2><p class="muted">Make videos about Chinese language, numbers or culture? Submit one for the hub, or pitch a paid collaboration.</p>
<form class="js-form" data-subject="Video submission / creator collab">
<div class="field"><label for="v-name">Name / channel</label><input id="v-name" name="name" required></div>
<div class="field"><label for="v-email">Email</label><input id="v-email" type="email" name="email" required autocomplete="email"></div>
<div class="field"><label for="v-url">Video or channel URL</label><input id="v-url" type="url" name="video_url" required placeholder="https://youtube.com/…"></div>
<div class="field"><label for="v-msg">Pitch (optional)</label><textarea id="v-msg" name="message"></textarea></div>
<button class="btn" type="submit">Submit</button></form></div>
<div class="card"><h2 style="font-size:1.4rem">Sponsor a video series</h2><p class="muted">Brands can sponsor short explainers for 520, Qixi and Lunar New Year campaigns, with pre-roll mentions and on-page placement.</p><a class="btn gold" href="advertise.html">Sponsorship packages</a></div></div>
</div></section>'''
    B.write("videos.html", "Chinese Lucky Numbers & Qixi Videos | 33077", "Watch the best explainers on Chinese lucky numbers, number slang like 520, and the Qixi love festival.", body, crumb="Videos")

    # ------------------------------------------------------------------ CONCIERGE (lead gen)
    goals = [("buy-number", "Buy a lucky phone number", "Mobile or business line with 8s, 6s, 9s"), ("plate", "Buy a lucky licence plate", "Vanity or auction plates"),
             ("domain", "Buy a numeric / premium domain", "5N, 4N, Chinese-friendly .com"), ("sell", "Sell or value my number / domain", "Free estimate from brokers"),
             ("date", "Auspicious date", "Wedding, opening, move, signing"), ("audit", "China-market number audit", "Prices, SKUs, hotlines, launch dates for Chinese customers"),
             ("naming", "Brand or baby name with lucky numbers", "Names, handles, product codes"), ("partner", "Sponsorship / partnership", "Brands, brokers, media")]
    opts = "".join(f'<label class="opt"><input type="radio" name="goal" value="{v}" required {"checked" if i == 0 else ""}><span>{t}<small>{s}</small></span></label>' for i, (v, t, s) in enumerate(goals))
    faq, ld = B.faq_block([
        ("Is the Concierge free?", "Yes. Asking is free and there is no obligation. If you go ahead, the seller, broker or consultant quotes you directly."),
        ("How fast will I hear back?", "Usually within 24 hours, and never more than 48 on business days."),
        ("Who are the partners?", "Established number brokers, plate dealers, domain brokers, feng shui and date-selection consultants, and China-market localisation specialists. We only introduce partners relevant to your request."),
        ("Is my information shared?", "Only with the partner(s) needed to answer your request, and only after we confirm with you. See our <a href='legal.html#privacy'>privacy policy</a>."),
        ("Can I list my number or domain for sale?", "Yes — choose “Sell or value my number / domain”.")])
    body = B.page_hero("找号 · Concierge", "Lucky Number Concierge", "Tell us the number, plate, domain or date you’re after — or the one you want to sell. We match you with the right expert in 24 hours.",
                       '<div class="trust" style="margin-top:12px"><span>Free, no obligation</span><span>Reply within 24 h</span><span>Vetted brokers only</span><span>Worldwide</span></div>') + f'''
<section><div class="wrap layout"><div>
<form class="card js-form steps" id="concierge" data-subject="CONCIERGE LEAD" data-ok="Request received! A specialist will reply within 24 hours. Tip: add us to your contacts so the reply doesn’t land in spam.">
  <div class="progress" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="step"><h2 style="font-size:1.4rem">1 · What can we help with?</h2><div class="opt-grid">{opts}</div>
    <div class="row" style="margin-top:18px"><button class="btn" type="button" data-next>Continue →</button><span class="small muted">Takes 60 seconds</span></div></div>
  <div class="step"><h2 style="font-size:1.4rem">2 · The details</h2>
    <div class="field"><label for="q-asset">Number, plate, domain or date you have in mind</label><input id="q-asset" name="asset" placeholder="e.g. anything with 888 · 33077.com · 8 Aug 2027"></div>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="q-budget">Budget</label><select id="q-budget" name="budget" required><option value="">Choose…</option><option>Under $500</option><option>$500 – $2,000</option><option>$2,000 – $10,000</option><option>$10,000 – $50,000</option><option>$50,000+</option><option>I’m selling</option><option>Not sure yet</option></select></div>
    <div class="field"><label for="q-country">Country / region</label><input id="q-country" name="country" required placeholder="e.g. Canada, Hong Kong, UAE"></div></div>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="q-when">Timeline</label><select id="q-when" name="timeline"><option>As soon as possible</option><option>Within a month</option><option>1–3 months</option><option>Just exploring</option></select></div>
    <div class="field"><label for="q-lang">Preferred language</label><select id="q-lang" name="language"><option>English</option><option>中文 (Mandarin)</option><option>粤语 (Cantonese)</option><option>Other</option></select></div></div>
    <div class="field"><label for="q-notes">Anything else?</label><textarea id="q-notes" name="notes" placeholder="Must include 8, avoid 4, birthday digits, zodiac sign…"></textarea></div>
    <div class="row"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn" type="button" data-next>Continue →</button></div></div>
  <div class="step"><h2 style="font-size:1.4rem">3 · Where should we reply?</h2>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="q-name">Name</label><input id="q-name" name="name" required autocomplete="name"></div>
    <div class="field"><label for="q-email">Email</label><input id="q-email" name="email" type="email" required autocomplete="email"></div></div>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="q-phone">Phone / WhatsApp (optional)</label><input id="q-phone" name="phone" type="tel" autocomplete="tel"></div>
    <div class="field"><label for="q-wechat">WeChat ID (optional)</label><input id="q-wechat" name="wechat"></div></div>
    <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that 33077 may share my request with relevant partners to answer it, per the <a href="legal.html#privacy">privacy policy</a>.</label>
    <label class="check" style="margin-top:8px"><input type="checkbox" name="newsletter" value="yes"> Also send me the free “number of the week”.</label>
    <div class="row" style="margin-top:16px"><button class="btn ghost" type="button" data-prev>← Back</button><button class="btn" type="submit">Send my request</button></div></div>
  <input type="hidden" name="form" value="concierge">
</form>
<div class="grid g3" style="margin-top:28px">
  <div class="card"><div class="ico">①</div><h3>Tell us</h3><p class="muted small" style="margin:0">60-second form. No account, no card.</p></div>
  <div class="card"><div class="ico">②</div><h3>We match</h3><p class="muted small" style="margin:0">We pick the right broker or specialist for your market.</p></div>
  <div class="card"><div class="ico">③</div><h3>You decide</h3><p class="muted small" style="margin:0">Compare options and quotes. Zero obligation.</p></div>
</div>
<div class="prose" style="margin-top:28px">{faq}</div>
</div><aside class="sidebar"><div class="sticky">
  <div class="card"><h3>Why people use it</h3><ul class="small" style="padding-left:18px;margin:0"><li>Lucky numbers trade in fragmented, local markets — hard to search alone.</li><li>Prices vary hugely: a 5N .com can sell for $20 or $24,000+.</li><li>A specialist saves time and overpaying.</li></ul></div>
  <div class="card"><h3>Are you a broker?</h3><p class="small muted">Get qualified leads in your market.</p><a class="btn block ghost" href="concierge.html?goal=partner">Become a partner</a></div>
</div></aside></div></section>'''
    B.write("concierge.html", "Lucky Number Concierge — Buy or Sell Lucky Phone Numbers, Plates & Domains | 33077",
            "Free matching with vetted brokers for lucky phone numbers, licence plates, numeric domains, auspicious dates and China-market number audits. Reply within 24 hours.", body, lds=[ld], crumb="Concierge")

    # ------------------------------------------------------------------ SUPPORT
    body = B.page_hero("支持 · Support", "Support 33077", "Keep the tools free and ad-light. Your support funds operations, promotion, marketing, new talent and contest prizes.") + f'''
<section><div class="wrap layout"><div>
  <div class="card" data-goal></div>
  <div class="grid g3" style="margin-top:24px">
    <div class="card tier"><h3>Friend</h3><div class="price num">$3.30<span class="small muted">/mo</span></div><ul class="small"><li>Name on the supporter wall</li><li>Monthly behind-the-scenes note</li></ul><a class="btn ghost block" href="#pledge" data-tier="Friend $3.30/mo">Choose</a></div>
    <div class="card tier feat"><h3>Patron</h3><div class="price num">$7.70<span class="small muted">/mo</span></div><ul class="small"><li>Everything in Friend</li><li>Ad-free experience (when accounts launch)</li><li>Vote on the next tool</li></ul><a class="btn block" href="#pledge" data-tier="Patron $7.70/mo">Choose</a></div>
    <div class="card tier"><h3>Champion</h3><div class="price num">$33.07<span class="small muted">/mo</span></div><ul class="small"><li>Everything in Patron</li><li>Logo or link on the supporters page</li><li>Name a contest prize</li></ul><a class="btn ghost block" href="#pledge" data-tier="Champion $33.07/mo">Choose</a></div>
  </div>
  <div class="card" id="pledge" style="margin-top:24px"><h2 style="font-size:1.5rem">Give once or pledge</h2>
    <div data-paylinks class="row" style="margin-bottom:16px"></div>
    <form class="js-form" data-subject="DONATION / PLEDGE" data-ok="Thank you! We’ll email you a secure payment link within 24 hours.">
      <label>Amount (USD)</label>
      <div class="amounts" data-target="d-amt"><button type="button" data-v="3.30">$3.30</button><button type="button" data-v="7.70">$7.70</button><button type="button" class="on" data-v="8.88">$8.88</button><button type="button" data-v="33.07">$33.07</button><button type="button" data-v="88">$88</button><button type="button" data-v="330">$330</button></div>
      <div class="grid g2" style="gap:14px;margin-top:14px"><div class="field"><label for="d-amt">Or your amount</label><input id="d-amt" name="amount" type="number" min="1" step="0.01" value="8.88" required></div>
      <div class="field"><label for="d-freq">Frequency</label><select id="d-freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
      <div class="field"><label for="d-purpose">Put it towards</label><select id="d-purpose" name="purpose"><option>Where it’s needed most (operations)</option><option>Promotions & marketing</option><option>Hiring writers, translators & creators</option><option>Contest prizes</option><option>New tools & features</option></select></div>
      <div class="grid g2" style="gap:14px"><div class="field"><label for="d-name">Name</label><input id="d-name" name="name" required autocomplete="name"></div><div class="field"><label for="d-email">Email</label><input id="d-email" name="email" type="email" required autocomplete="email"></div></div>
      <div class="field"><label for="d-tier">Membership tier (optional)</label><input id="d-tier" name="tier" placeholder="—"></div>
      <div class="field"><label for="d-msg">Message for the wall (optional)</label><input id="d-msg" name="message" maxlength="120"></div>
      <label class="check"><input type="checkbox" name="public" value="yes" checked> Show my first name on the supporter wall</label>
      <button class="btn" type="submit" style="margin-top:14px">Pledge my support</button>
    </form></div>
  <h2 style="margin-top:32px">Supporter wall</h2><div class="wall"><span>Be the first supporter ❤</span></div>
  <div class="prose" style="margin-top:24px"><h2>Where the money goes</h2><div class="tbl-wrap"><table><tbody><tr><td>Operations & tools</td><td>Hosting, domain, form services, development</td></tr><tr><td>Promotion & marketing</td><td>Qixi, 520 and Lunar New Year campaigns</td></tr><tr><td>Talent</td><td>Paying native-speaker writers, translators and video creators</td></tr><tr><td>Contests & prizes</td><td>Cash prizes and features for the community</td></tr></tbody></table></div>
  <p class="small muted">33077.com is not a registered charity; contributions are not tax-deductible. Totals are published quarterly.</p></div>
</div><aside class="sidebar"><div class="sticky"><div class="card"><h3>Businesses</h3><p class="small muted">Prefer visibility for your support? Sponsor a tool or festival.</p><a class="btn block gold" href="advertise.html">Sponsor instead</a></div></div></aside></div></section>
<script>document.addEventListener("click",function(e){{var a=e.target.closest("[data-tier]");if(a){{var t=document.getElementById("d-tier");t.value=a.getAttribute("data-tier");document.getElementById("d-freq").value="Monthly";document.getElementById("d-amt").value=a.getAttribute("data-tier").match(/[\\d.]+/)[0];}}}});</script>'''
    B.write("support.html", "Support 33077 — Donate or Become a Member", "Support free Chinese number tools: donate once or monthly towards operations, promotion, new talent and contest prizes.", body, crumb="Support")

    # ------------------------------------------------------------------ CONTESTS
    body = B.page_hero("比赛 · Contests", "The 33077 Love Code Challenge", "Invent the most creative Chinese number love code. Winners are announced on Qixi.",
                       '<div class="cd" data-contest-cd style="margin-top:12px"></div><p class="small muted" style="margin-top:6px">Entries close on Qixi 2027 (8 Aug 2027, 23:59 China time).</p>') + f'''
<section><div class="wrap layout"><div>
  <h2>Prizes</h2><div class="grid g3" data-prizes></div>
  <h2 style="margin-top:32px">How to enter</h2>
  <div class="grid g3"><div class="card"><div class="ico">①</div><h3>Build</h3><p class="small muted" style="margin:0">Use the <a href="love-codes.html">Love Code Builder</a> or invent your own digits.</p></div><div class="card"><div class="ico">②</div><h3>Explain</h3><p class="small muted" style="margin:0">Give the 汉字 reading and the story behind it.</p></div><div class="card"><div class="ico">③</div><h3>Share</h3><p class="small muted" style="margin:0">Each share with your entry link = a bonus entry (max 5).</p></div></div>
  <form class="card js-form" id="enter" data-subject="CONTEST ENTRY" data-ok="You’re entered! Share your code to earn bonus entries." style="margin-top:24px">
    <h2 style="font-size:1.4rem">Submit your entry</h2>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="c-code">Your number code</label><input id="c-code" name="code" required inputmode="numeric" pattern="[0-9]{{2,16}}" placeholder="e.g. 53770"></div><div class="field"><label for="c-han">Chinese reading (汉字 / pinyin)</label><input id="c-han" name="reading" required placeholder="我想亲亲你"></div></div>
    <div class="field"><label for="c-meaning">Meaning in English</label><input id="c-meaning" name="meaning" required></div>
    <div class="field"><label for="c-story">Why it works (max 300 characters)</label><textarea id="c-story" name="story" maxlength="300"></textarea></div>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="c-name">Name</label><input id="c-name" name="name" required autocomplete="name"></div><div class="field"><label for="c-email">Email</label><input id="c-email" type="email" name="email" required autocomplete="email"></div></div>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="c-country">Country</label><input id="c-country" name="country" required></div><div class="field"><label for="c-social">Social handle (optional)</label><input id="c-social" name="social"></div></div>
    <label class="check"><input type="checkbox" name="age_rules" value="yes" required> I am 18+ (or have a parent’s permission) and accept the official rules below.</label>
    <button class="btn" type="submit" style="margin-top:14px">Enter the challenge</button>
    <button class="btn ghost" type="button" data-share="I just entered the 33077 Love Code Challenge — invent a Chinese number love code and win prizes!" style="margin-top:14px">Share for bonus entries</button>
  </form>
  {B.ad("content")}
  <h2>Coming next</h2>
  <div class="grid g3"><div class="card"><span class="badge b-mix">Lunar New Year 2027</span><h3 style="margin-top:8px">Lucky Goat Photo Contest</h3><p class="small muted" style="margin:0">Your best Year-of-the-Goat photo with a lucky number in it.</p></div><div class="card"><span class="badge b-love">520 · 2027</span><h3 style="margin-top:8px">520 Story Contest</h3><p class="small muted" style="margin:0">The most romantic real-life “520” moment.</p></div><div class="card"><span class="badge b-good">Anytime</span><h3 style="margin-top:8px">Spot the Lucky Number</h3><p class="small muted" style="margin:0">Photograph lucky numbers in the wild — plates, prices, doors.</p></div></div>
  <div class="card" style="margin-top:24px"><h3>Sponsor a contest</h3><p class="muted">Put your brand’s name on a prize or an entire contest, with placement across the site and newsletter.</p><a class="btn gold" href="advertise.html">Sponsorship options</a></div>
  <div class="prose" id="rules" style="margin-top:32px"><h2>Official rules (summary)</h2><ol class="small">
    <li><b>No purchase necessary.</b> A purchase or donation does not improve your chances.</li>
    <li><b>Eligibility:</b> open worldwide to individuals 18+, or minors with a parent or guardian’s permission, except where prohibited or restricted by law. Void where prohibited.</li>
    <li><b>Entry period:</b> until the closing date shown above. One entry per person, plus up to 5 bonus entries for verified shares.</li>
    <li><b>Judging:</b> a panel scores originality (40%), accuracy of the Chinese reading (30%) and charm (30%). Bonus entries count only toward the People’s Choice mention.</li>
    <li><b>Prizes:</b> as listed above; paid by PayPal or bank transfer within 30 days of verification. Prizes are non-transferable; winners are responsible for any taxes. The organiser may substitute a prize of equal or greater value.</li>
    <li><b>Winners</b> are notified by email and must reply within 14 days, or an alternate is chosen. Winners’ first names, countries and codes are published.</li>
    <li><b>Content:</b> entries must be original and not infringe others’ rights or be offensive. By entering you grant 33077.com a non-exclusive, royalty-free licence to display your entry with credit.</li>
    <li><b>Organiser:</b> 33077.com. This contest is not sponsored, endorsed or administered by any social network. Full terms are in our <a href="legal.html#contests">legal page</a>.</li></ol></div>
</div><aside class="sidebar"><div class="sticky"><div class="card"><h3>Past winners</h3><p class="small muted" style="margin:0">Our first winners will be crowned on Qixi 2027. Could it be you?</p></div>{B.ad("sidebar")}</div></aside></div></section>'''
    B.write("contests.html", "Love Code Challenge — Win Prizes for Your Chinese Number Code | 33077",
            "Invent a Chinese number love code and win cash prizes. Free to enter; winners announced on Qixi 2027.", body, crumb="Contests")

    # ------------------------------------------------------------------ CAREERS
    roles = [("Mandarin / Cantonese content writer", "Freelance · remote", "Write number-meaning pages, festival guides and love-code explainers."),
             ("Translator (简体 / 繁體)", "Freelance · remote", "Localise tools and guides into Simplified and Traditional Chinese."),
             ("Short-form video creator", "Per video · remote", "YouTube Shorts, TikTok and Reels on numbers and festivals."),
             ("Designer / illustrator", "Project · remote", "Share cards, zodiac art and festival campaigns."),
             ("Campus & community ambassador", "Commission · anywhere", "Grow contests and the newsletter in your city or school."),
             ("Partnerships & sales", "Commission · remote", "Bring in sponsors, brokers and advertisers.")]
    body = B.page_hero("招贤 · Careers", "Join the 33077 Team", "We’re building the world’s go-to hub for Chinese number culture. Remote, flexible, paid or revenue-share roles.") + f'''
<section><div class="wrap"><div class="grid g3">{"".join(f'<div class="card"><span class="badge b-mix">{b}</span><h3 style="margin-top:8px">{a}</h3><p class="small muted">{c}</p><a class="btn sm ghost" href="#apply" data-role="{e(a)}">Apply</a></div>' for a, b, c in roles)}</div>
<div class="layout" style="margin-top:32px"><form class="card js-form" id="apply" data-subject="TALENT APPLICATION" data-ok="Application received — thank you! We reply to shortlisted candidates within 7 days.">
  <h2 style="font-size:1.4rem">Apply</h2>
  <div class="field"><label for="j-role">Role</label><select id="j-role" name="role" required><option value="">Choose…</option>{"".join(f"<option>{e(a)}</option>" for a, _, _ in roles)}<option>Other / open application</option></select></div>
  <div class="grid g2" style="gap:14px"><div class="field"><label for="j-name">Name</label><input id="j-name" name="name" required autocomplete="name"></div><div class="field"><label for="j-email">Email</label><input id="j-email" name="email" type="email" required autocomplete="email"></div></div>
  <div class="grid g2" style="gap:14px"><div class="field"><label for="j-country">Country / time zone</label><input id="j-country" name="country" required></div><div class="field"><label for="j-lang">Languages</label><input id="j-lang" name="languages" placeholder="English, 中文…"></div></div>
  <div class="field"><label for="j-port">Portfolio / LinkedIn / channel URL</label><input id="j-port" name="portfolio" type="url" placeholder="https://"></div>
  <div class="field"><label for="j-avail">Availability</label><select id="j-avail" name="availability"><option>A few hours a week</option><option>Part-time</option><option>Full-time</option><option>Per project</option></select></div>
  <div class="field"><label for="j-msg">Why you? (a few lines)</label><textarea id="j-msg" name="message" required></textarea></div>
  <button class="btn" type="submit">Send application</button></form>
<aside class="sidebar"><div class="card"><h3>How we work</h3><ul class="small" style="padding-left:18px;margin:0"><li>Remote-first, async</li><li>Paid per piece, per project or on commission</li><li>Credit on everything you make</li><li>Priority for native speakers and creators with an audience</li></ul></div></aside></div>
</div></section>
<script>document.addEventListener("click",function(e){{var a=e.target.closest("[data-role]");if(a)document.getElementById("j-role").value=a.getAttribute("data-role");}});</script>'''
    B.write("careers.html", "Careers & Talent — Writers, Translators, Creators | 33077", "Join 33077: remote roles for Chinese writers, translators, video creators, designers, ambassadors and partnership sales.", body, crumb="Careers")

    # ------------------------------------------------------------------ ADVERTISE
    pk = [("Tool sponsor", "“Presented by” placement on a tool (Decoder, Love Codes, Lucky Score or Zodiac) and its result cards.", ["Logo + link on every result", "Mention in shares", "Monthly report"]),
          ("Festival sponsor", "Own the 520, Qixi or Lunar New Year campaign across the site, newsletter and contest.", ["Homepage takeover week", "Contest title sponsor", "Social + video mentions"]),
          ("Newsletter", "Sponsor the “number of the week” email.", ["Top slot + 2 lines", "Dedicated send option", "Click report"]),
          ("Lead partner", "Receive Concierge leads in your market (numbers, plates, domains, dates, audits).", ["Qualified, consented leads", "Exclusive region option", "Per-lead or revenue share"])]
    body = B.page_hero("广告 · Advertise", "Advertise & Sponsor on 33077", "Reach people actively searching for lucky numbers, Chinese love codes, zodiac matches and festival gifts — at the moment they decide.") + f'''
<section><div class="wrap">
  <div class="grid g4">{"".join(f'<div class="card tier"><h3>{a}</h3><p class="small muted">{b}</p><ul class="small">{"".join(f"<li>{x}</li>" for x in c)}</ul><a class="btn sm block" href="#adform" data-pkg="{a}">Request rates</a></div>' for a, b, c in pk)}</div>
  <div class="grid g3" style="margin-top:28px"><div class="card stat"><b>High intent</b>Visitors arrive looking up numbers they’re about to buy, gift or choose.</div><div class="card stat"><b>Seasonal peaks</b>520 (May 20), Qixi, 11.11 and Lunar New Year.</div><div class="card stat"><b>Global</b>Chinese diaspora, learners and brands selling to Chinese customers.</div></div>
  <div class="layout" style="margin-top:32px"><form class="card js-form" id="adform" data-subject="ADVERTISING / SPONSORSHIP INQUIRY" data-ok="Thanks! We’ll send the media kit and rates within 24 hours.">
    <h2 style="font-size:1.4rem">Get the media kit</h2>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="a-co">Company</label><input id="a-co" name="company" required></div><div class="field"><label for="a-web">Website</label><input id="a-web" name="website" type="url" placeholder="https://"></div></div>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="a-name">Your name</label><input id="a-name" name="name" required autocomplete="name"></div><div class="field"><label for="a-email">Work email</label><input id="a-email" name="email" type="email" required autocomplete="email"></div></div>
    <div class="grid g2" style="gap:14px"><div class="field"><label for="a-pkg">Interested in</label><select id="a-pkg" name="package">{"".join(f"<option>{a}</option>" for a, _, _ in pk)}<option>Display advertising</option><option>Buying / partnering on the domain</option><option>Something else</option></select></div>
    <div class="field"><label for="a-budget">Budget</label><select id="a-budget" name="budget"><option>Under $500</option><option>$500 – $2,500</option><option>$2,500 – $10,000</option><option>$10,000+</option></select></div></div>
    <div class="field"><label for="a-msg">Goals & timing</label><textarea id="a-msg" name="message"></textarea></div>
    <button class="btn" type="submit">Request media kit</button></form>
  <aside class="sidebar"><div class="card"><h3>Standards</h3><ul class="small" style="padding-left:18px;margin:0"><li>Sponsored content is always labelled</li><li>No gambling, adult or deceptive ads</li><li>Ads never sit between a tool and its result</li></ul></div>
  <div class="card"><h3>Interested in the domain itself?</h3><p class="small muted">Acquisition, partnership or joint venture on 33077.com.</p><a class="btn block gold" href="https://web.works/contact" target="_blank" rel="noopener">Contact the owner</a></div></aside></div>
</div></section>
<script>document.addEventListener("click",function(e){{var a=e.target.closest("[data-pkg]");if(a)document.getElementById("a-pkg").value=a.getAttribute("data-pkg");}});</script>'''
    B.write("advertise.html", "Advertise & Sponsor — Reach Lucky-Number and China-Culture Audiences | 33077", "Sponsorship packages on 33077: tool sponsor, festival sponsor (520, Qixi, Lunar New Year), newsletter and Concierge lead partnerships.", body, crumb="Advertise")

    # ------------------------------------------------------------------ CONTACT
    body = B.page_hero("联系 · Contact", "Contact 33077", "Questions, corrections, partnerships or press — send us a note and we’ll reply within 48 hours.") + '''
<section><div class="wrap layout"><form class="card js-form" data-subject="General contact">
  <div class="field"><label for="k-topic">Topic</label><select id="k-topic" name="topic"><option>General question</option><option>Correction to a meaning</option><option>Buying / partnering on the domain</option><option>Sponsorship / advertising</option><option>Press</option><option>Something else</option></select></div>
  <div class="grid g2" style="gap:14px"><div class="field"><label for="k-name">Name</label><input id="k-name" name="name" required autocomplete="name"></div><div class="field"><label for="k-email">Email</label><input id="k-email" name="email" type="email" required autocomplete="email"></div></div>
  <div class="field"><label for="k-msg">Message</label><textarea id="k-msg" name="message" required></textarea></div>
  <button class="btn" type="submit">Send message</button></form>
<aside class="sidebar"><div class="card"><h3>Faster routes</h3><p><a href="concierge.html">Lucky Number Concierge →</a></p><p><a href="advertise.html">Advertising →</a></p><p><a href="careers.html">Careers →</a></p><p style="margin:0"><a href="https://web.works/contact" target="_blank" rel="noopener">Domain & partnership inquiries →</a></p></div></aside></div></section>'''
    B.write("contact.html", "Contact 33077", "Contact 33077.com for questions, corrections, partnerships, advertising or press.", body, crumb="Contact")

    # ------------------------------------------------------------------ ABOUT
    body = B.page_hero("关于 · About", "About 33077", "A free, independent hub for the culture — and the economy — of Chinese numbers.") + '''
<section><div class="wrap prose">
<h2>Why “33077”?</h2><p>Read as Chinese number slang, <b>3 = 想</b> (miss), <b>0 = 你</b> (you) and <b>77 = 亲亲</b> (kiss kiss): <span class="han">想想你亲亲</span> — “thinking of you, kiss kiss.” It also spans China’s two love festivals, lunar 3/3 (Shangsi) and 7/7 (Qixi). The reading is our own coinage, built from established codes; we say so wherever it appears.</p>
<h2>What we do</h2><ul><li><b>Decode</b> — explain what any number means in Chinese, and why.</li><li><b>Create</b> — help people write love codes, pick names and dates.</li><li><b>Connect</b> — match buyers and sellers of lucky numbers with trusted specialists.</li><li><b>Celebrate</b> — festivals, contests and community.</li></ul>
<h2 id="standards">Editorial standards</h2><ul><li>Meanings come from Chinese homophones and widely used slang; codes we coin are labelled.</li><li>Economic facts link to their source (news, research or market data).</li><li>Luck scores measure cultural perception — they are not predictions or advice.</li><li>Spotted an error? <a href="contact.html">Tell us</a> — we correct quickly and note the change.</li></ul>
<h2>Independence</h2><p>33077 is funded by advertising, sponsorships, Concierge partner fees and reader support. Sponsored content is always labelled, and partners never pay to change a meaning or a score.</p>
<div class="note">Interested in this website, the domain name, sponsorship, advertising or a partnership? <a href="https://web.works/contact" target="_blank" rel="noopener">Contact the owner</a>.</div>
</div></section>'''
    B.write("about.html", "About 33077 — The Chinese Number Code Hub", "Why 33077 means “thinking of you — kiss kiss”, what we do, and our editorial standards.", body, crumb="About")

    # ------------------------------------------------------------------ LEGAL
    body = B.page_hero("法律 · Legal", "Trademark, Copyright & Privacy", "Plain-language disclosures. Last updated 27 September 2026.") + '''
<section><div class="wrap prose">
<h2 id="trademark">Trademark disclosure</h2>
<p>“33077” is a number. On this website it is used <b>descriptively</b> — as a numeral and as the site’s domain name — and <b>no trademark rights are claimed in the number “33077”</b> by this site. 33077.com is <b>not affiliated with, endorsed by or sponsored by</b> any company, brand, product, model number, postal code, stock ticker, registration or organisation that uses the same digits. Any such use by third parties belongs to them.</p>
<p>All other names, logos and trademarks mentioned (including Google, AdSense, YouTube, PayPal, Ko-fi, Buy Me a Coffee, Stripe, Taobao and others) are the property of their respective owners. Their mention is for identification and reference only and does not imply endorsement.</p>
<p>If you believe content here infringes your trademark, please use the <a href="contact.html">contact form</a> with details and we will review it promptly.</p>
<h2 id="copyright">Copyright notice</h2>
<p>© 2026 33077.com. The text, tools, code, design and compilations on this site are original works protected by copyright; all rights reserved. You may quote short excerpts with a link back to the source page. Chinese characters, numbers, homophones and traditional cultural meanings are public knowledge and not owned by anyone; our selection, arrangement, explanations and software are.</p>
<p>Facts and figures are credited to their sources with links. Videos are embedded through YouTube’s official player and remain the property of their creators; we do not host or copy them. Fonts are served by Google Fonts under their open licences.</p>
<p><b>Copyright complaints (DMCA-style):</b> send the work, the URL on our site, your contact details and a good-faith statement via the <a href="contact.html">contact form</a>. We remove infringing material promptly.</p>
<h2 id="privacy">Privacy policy</h2>
<ul><li><b>What we collect:</b> only what you type into forms (e.g. name, email, request details) and basic, non-identifying usage data.</li>
<li><b>How forms work:</b> submissions are delivered to our private inbox through a form-relay service (FormSubmit). We never publish your email or sell your data.</li>
<li><b>Concierge:</b> with your consent, we share your request only with the partner(s) needed to answer it.</li>
<li><b>Cookies & ads:</b> we may show ads from Google AdSense. Google and its partners use cookies to serve ads based on your visits to this and other sites. You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>. See <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses data from partner sites</a>.</li>
<li><b>YouTube:</b> videos use the privacy-enhanced youtube-nocookie.com player and load only when you press play.</li>
<li><b>Local storage:</b> your theme and cookie choice are saved in your browser only.</li>
<li><b>Your rights:</b> ask us to access or delete your data at any time via the <a href="contact.html">contact form</a>. EU/UK, California and Canadian (PIPEDA) residents have additional rights, which we honour.</li>
<li><b>Children:</b> this site is not directed at children under 13, and we do not knowingly collect their data.</li></ul>
<h2 id="terms">Terms of use</h2>
<ul><li>Tools and content are for <b>entertainment and cultural education</b>. They are not financial, investment, legal, medical or religious advice. Luck scores are not predictions.</li>
<li>The Concierge is an introduction service. Any purchase, sale or service is a contract between you and the partner; do your own due diligence.</li>
<li>Don’t misuse the site (spam, scraping at scale, attacks). We may change or discontinue features at any time.</li>
<li>The site is provided “as is” without warranties; to the extent permitted by law, our liability is limited to the amount you paid us (usually zero).</li></ul>
<h2 id="affiliate">Advertising, affiliate & donation disclosure</h2>
<p>We may earn from display ads, sponsorships, affiliate links and Concierge partner fees. Sponsored placements are labelled. Donations support operations, promotion, marketing, hiring and prizes; 33077.com is not a registered charity and donations are not tax-deductible.</p>
<h2 id="contests">Contests</h2>
<p>Every contest has its own official rules on its page. No purchase is necessary to enter or win; void where prohibited. Prizes are awarded as stated in those rules.</p>
</div></section>'''
    B.write("legal.html", "Trademark, Copyright & Privacy Disclosure | 33077", "33077.com trademark disclosure, copyright notice, privacy policy, terms of use and advertising disclosures.", body, crumb="Legal")

    # ------------------------------------------------------------------ 404
    body = '<section class="hero"><div class="wrap" style="text-align:center"><div class="big-num num">4<span class="g">0</span>4</div><h1>Unlucky number!</h1><p class="lead" style="margin:0 auto 20px">四〇四 — even we avoid 4s. This page doesn’t exist.</p><a class="btn" href="index.html">Back to the homepage</a> <a class="btn ghost" href="decoder.html">Decode a number</a></div></section>'
    B.write("404.html", "404 — Unlucky Number | 33077", "Page not found.", body)
