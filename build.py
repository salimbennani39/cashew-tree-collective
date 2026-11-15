import os

OUT = os.path.dirname(os.path.abspath(__file__))
IG = "https://www.instagram.com/"
LINKTREE = "https://linktr.ee/Cashewtreecollective"
MAPS = "https://www.google.com/maps/search/?api=1&query=The+Cashew+Tree+Bingin+Bali"
A = "assets/ig/"

NAV = [("index.html", "Home"), ("menu.html", "Menu"), ("music.html", "Thirsty Thursday"),
       ("collective.html", "The Collective"), ("visit.html", "Visit")]


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f2ede4">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
"""


def header(current):
    cur = ' aria-current="page"'
    links = "\n".join(
        '        <a href="%s"%s>%s</a>' % (h, cur if h == current else "", t)
        for h, t in NAV if h != "index.html")
    mlinks = "\n".join(f'    <a class="big" href="{h}">{t}</a>' for h, t in NAV)
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="The Cashew Tree Collective, home">
      <img src="{A}logo.jpg" alt="">
      <span>The Cashew Tree<small>Collective</small></span>
    </a>
    <nav class="nav-links" aria-label="Main">
{links}
    </nav>
    <span class="status" data-status><i></i><b>Open 7:30am – 10pm</b></span>
    <button class="menu-btn" aria-expanded="false" aria-controls="mnav">Menu</button>
  </div>
</header>
<nav class="mobile-nav" id="mnav" aria-label="Mobile">
  <div>
{mlinks}
  </div>
  <div>
    <span class="status" data-status><i></i><b>Open 7:30am – 10pm</b></span>
    <p class="cap">Bingin, Uluwatu · Bali</p>
  </div>
</nav>
<main>
"""


FOOTER = f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <p class="h3" style="max-width:16ch">Come for breakfast. Stay for the band.</p>
      </div>
      <div>
        <h4>Visit</h4>
        <ul>
          <li>Open daily</li>
          <li>7:30am – 10pm</li>
          <li><a href="{MAPS}" target="_blank" rel="noopener">Bingin, Uluwatu, Bali ↗</a></li>
        </ul>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="menu.html">Menu</a></li>
          <li><a href="music.html">Thirsty Thursday</a></li>
          <li><a href="collective.html">The Collective</a></li>
          <li><a href="visit.html">Visit</a></li>
        </ul>
      </div>
      <div>
        <h4>Follow</h4>
        <ul>
          <li><a href="{IG}thecashewtree.collective/" target="_blank" rel="noopener">@thecashewtree.collective</a></li>
          <li><a href="{IG}toko.coastal/" target="_blank" rel="noopener">@toko.coastal</a></li>
          <li><a href="{IG}rotisserie.cashewtree/" target="_blank" rel="noopener">@rotisserie.cashewtree</a></li>
          <li><a href="{IG}pak.g.bingin/" target="_blank" rel="noopener">@pak.g.bingin</a></li>
          <li><a href="{IG}bali_training_centre/" target="_blank" rel="noopener">@bali_training_centre</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-word" aria-hidden="true">The Cashew Tree</div>
    <div class="foot-base">
      <span>© <span data-year>2026</span> The Cashew Tree Collective</span>
      <a href="{LINKTREE}" target="_blank" rel="noopener">linktr.ee/Cashewtreecollective ↗</a>
    </div>
  </div>
</footer>
<script src="main.js"></script>
</body>
</html>
"""

# ------------------------------------------------------------------ HOME
VENUES = [
    ("The Cashew Tree", "Garden café & kitchen. Breakfast to late, live music on Thursdays.", "thecashewtree.collective", "spread.jpg"),
    ("Toko Coastal", "Clothing, homewares, kids, jewellery, skincare & beach essentials.", "toko.coastal", "toko.jpg"),
    ("Rotisserie", "Hot rotisserie chicken, burgers, salads & slushies. Free delivery in Bingin.", "rotisserie.cashewtree", "rotisserie.jpg"),
    ("Pak G", "The Collective’s chopsticks-ready kitchen, Bingin.", "pak.g.bingin", None),
    ("Bali Training Centre", "HIIT, functional fitness, kettlebells, Muay Thai & boxing.", "bali_training_centre", "btc.jpg"),
]

venue_rows = "\n".join(f"""      <a class="venue reveal" href="{IG}{h}/" target="_blank" rel="noopener"{f' data-img="{A}{img}"' if img else ''}>
        <span class="idx">0{i+1}</span>
        <span class="name">{n}</span>
        <span class="what">{w}</span>
        <span class="handle">@{h} <span class="arr">↗</span></span>
        {f'<span class="thumb"><img src="{A}{img}" alt="" loading="lazy"></span>' if img else ''}
      </a>""" for i, (n, w, h, img) in enumerate(VENUES))

ig_tiles = "\n".join(f"""      <a href="{IG}thecashewtree.collective/" target="_blank" rel="noopener" class="reveal d{i%3}"><div class="frame r-1x1"><img src="{A}{f}" alt="{alt}" loading="lazy"></div></a>"""
                     for i, (f, alt) in enumerate([
                         ("smoothie-bowls.jpg", "Smoothie bowls served in coconut shells"),
                         ("coconuts.jpg", "Fresh young coconuts"),
                         ("platter.jpg", "Grazing platter with tropical fruit"),
                         ("pineapple-drink.jpg", "Pineapple drink and garlic bread"),
                         ("little-one.jpg", "A little one on the playground"),
                         ("bowls.jpg", "Rice bowls and fresh juice"),
                     ]))

home = head("The Cashew Tree Collective · Bingin, Bali",
            "Garden café in Bingin, Bali. Open daily 7:30am to 10pm, live music every Thursday, a playground for kids, and a collective of local brands.") + header("index.html") + f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow reveal">Bingin · Uluwatu · Bali</span>
      <h1 class="display reveal d1">A garden kitchen for slow mornings &amp; <em>loud</em> Thursdays.</h1>
      <p class="lede reveal d2">Fresh bowls, cold coconuts and long tables under the trees. Open every day from 7:30am to 10pm.</p>
      <div class="btn-row reveal d3">
        <a class="btn solid" href="menu.html">See the menu <span class="arr">→</span></a>
        <a class="btn" href="visit.html">Find us</a>
      </div>
    </div>
    <div class="hero-media">
      <div class="frame r-4x5 main reveal"><img src="{A}bowls.jpg" alt="Grilled chicken rice bowls and a fresh juice on a wooden table" fetchpriority="high"></div>
      <div class="frame r-1x1 float reveal d2"><img src="{A}smoothie-bowls.jpg" alt="Smoothie bowls served in coconut shells"></div>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker-track">
    <span>Open daily 7:30am – 10pm</span><span>Live music every Thursday</span><span>Playground for the little ones</span><span>Fresh coconuts</span><span>Platters for the table</span>
    <span>Open daily 7:30am – 10pm</span><span>Live music every Thursday</span><span>Playground for the little ones</span><span>Fresh coconuts</span><span>Platters for the table</span>
  </div>
</div>

<section class="pad">
  <div class="wrap intro-grid">
    <span class="eyebrow reveal">The place</span>
    <p class="statement reveal d1">Breakfast in the garden, platters at sunset, a band on Thursday, and a playground so <em>everyone</em> gets to stay a little longer.</p>
    <p class="sub reveal d2">The Cashew Tree started as a café under one big tree in Bingin. Today it is a collective: a kitchen, a shop, a rotisserie and a gym, all on the same patch of the Bukit.</p>
  </div>
</section>

<section class="pad-sm">
  <div class="wrap pillars">
    <a class="pillar reveal" href="menu.html">
      <div class="frame r-4x5"><img src="{A}platter.jpg" alt="Grazing platter piled with tropical fruit" loading="lazy"></div>
      <span class="num">01 — EAT</span>
      <h3 class="h3">All-day kitchen</h3>
      <p>Smoothie bowls, fresh rolls, rice bowls and platters made for sharing.</p>
      <span class="link-arrow">The menu →</span>
    </a>
    <a class="pillar reveal d1" href="music.html">
      <div class="frame r-4x5"><img src="{A}live-band.jpg" alt="Drummer playing live at The Cashew Tree" loading="lazy"></div>
      <span class="num">02 — LISTEN</span>
      <h3 class="h3">Thirsty Thursday</h3>
      <p>Every Thursday night: a live band, then a DJ, in the garden.</p>
      <span class="link-arrow">This week’s lineup →</span>
    </a>
    <a class="pillar reveal d2" href="visit.html#playground">
      <div class="frame r-4x5"><img src="{A}playground.jpg" alt="A child holding a coconut beside the mushroom playhouse" loading="lazy"></div>
      <span class="num">03 — PLAY</span>
      <h3 class="h3">The playground</h3>
      <p>A mushroom house, open lawn and room to run while the grown-ups linger.</p>
      <span class="link-arrow">Bring the kids →</span>
    </a>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2 reveal">The <em>Collective</em></h2>
      <a class="link-arrow reveal" href="collective.html">Meet the family →</a>
    </div>
    <div class="venues">
{venue_rows}
    </div>
  </div>
  <div class="venue-preview" aria-hidden="true"><img alt=""></div>
</section>

<section class="pad-sm rule">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow">On Instagram</span>
        <h2 class="h2" style="margin-top:12px">@thecashewtree.collective</h2>
      </div>
      <a class="btn" href="{IG}thecashewtree.collective/" target="_blank" rel="noopener">Follow along <span class="arr">↗</span></a>
    </div>
    <div class="ig-grid">
{ig_tiles}
    </div>
  </div>
</section>
""" + FOOTER

# ------------------------------------------------------------------ MENU
def course(eyebrow, title, text, img, alt, items):
    lis = "\n".join(f"          <li><span>{a}</span><span>{b}</span></li>" for a, b in items)
    return f"""<section class="course wrap">
      <div class="frame r-4x5 reveal"><img src="{A}{img}" alt="{alt}" loading="lazy"></div>
      <div class="body reveal d1">
        <span class="eyebrow">{eyebrow}</span>
        <h2 class="h2">{title}</h2>
        <p class="lede">{text}</p>
        <ul>
{lis}
        </ul>
      </div>
    </section>"""

menu = head("Menu · The Cashew Tree Collective",
            "All-day menu at The Cashew Tree, Bingin: smoothie bowls, fresh rolls, rice bowls, platters, coconuts, juices and cocktails.") + header("menu.html") + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow reveal">Menu · 7:30am – 10pm</span>
    <h1 class="display reveal d1">Made for <em>sharing</em>,<br>served all day.</h1>
    <p class="lede reveal d2">A taste of what comes out of the kitchen. The full menu, specials and prices live on our link page.</p>
  </div>
</section>

<div>
{course("Mornings", "Bowls in <em>coconut</em> shells", "Smoothie bowls served in the shell, piled high with mango, banana, dragon fruit and frangipani on top.", "smoothie-bowls.jpg", "Smoothie bowls in coconut shells topped with fruit and flowers",
        [("Smoothie bowls", "Tropical fruit"), ("Fresh juices", "Pressed daily"), ("Coffee", "From 7:30am")])}
{course("Lunch & dinner", "Bowls, rolls &amp; <em>plates</em>", "Grilled chicken over rice with avocado and sesame drizzle, fresh rolls with dipping sauces, and big salads.", "spread.jpg", "Table spread with fresh rolls, rice bowls and juices",
        [("Rice bowls", "Grilled & fresh"), ("Fresh rolls & wraps", "With dips"), ("Salads", "Garden greens")])}
{course("For the table", "<em>Platters</em>", "Grazing boards with fruit, cheese, crackers and more. Made for birthdays, sunsets and long lunches.", "platter.jpg", "Grazing platter with watermelon, papaya, grapes and cheese",
        [("Grazing platters", "To share"), ("Fruit platters", "Tropical"), ("Celebration boards", "On request")])}
{course("To drink", "Coconuts &amp; <em>cocktails</em>", "Young coconuts straight from the tree, fresh juices, smoothies, and a cocktail list for Thursday nights.", "coconuts.jpg", "Fresh young coconuts and juice shots",
        [("Young coconut", "Whole"), ("Juices & smoothies", "Fresh"), ("Cocktails", "Ask the bar")])}
</div>

<section class="cta-band pad">
  <div class="wrap">
    <span class="eyebrow" style="color:rgba(242,237,228,.6)">Full menu</span>
    <h2 class="h2" style="margin-top:16px">Prices, specials &amp; the <em>new</em> menu</h2>
    <p class="lede">Updated by the team every week.</p>
    <a class="btn" href="{LINKTREE}" target="_blank" rel="noopener">Open the full menu <span class="arr">↗</span></a>
  </div>
</section>
""" + FOOTER

# ------------------------------------------------------------------ MUSIC
LINEUPS = [
    ("poster-1211.jpg", "12 Nov 2026", "Rainbow &amp; Cloud", "DJ Boyd"),
    ("poster-0511.jpg", "5 Nov 2026", "Reyna &amp; The Paper Hearts", "DJ Dex"),
    ("poster-2910.jpg", "29 Oct 2026", "Nyra", "DJ Mamen"),
]
lineup_cards = "\n".join(f"""      <article class="lineup reveal d{i}">
        <div class="frame r-3x4"><img src="{A}{p}" alt="Thirsty Thursday poster, {d}: {band} and {dj}" loading="lazy"></div>
        <div class="meta"><span>{d}</span><span>Live + DJ</span></div>
        <h3 class="h3">{band} <span style="color:var(--muted)">/ {dj}</span></h3>
      </article>""" for i, (p, d, band, dj) in enumerate(LINEUPS))

music = head("Thirsty Thursday · The Cashew Tree Collective",
             "Live music every Thursday night at The Cashew Tree, Bingin. A live band, then a DJ, in the garden.") + header("music.html") + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow reveal">Every Thursday night</span>
    <h1 class="display reveal d1">Thirsty <em>Thursday</em></h1>
    <p class="lede reveal d2">A live band, then a DJ. Cocktails at the bar, food from the kitchen, and the whole of Bingin in the garden.</p>
  </div>
</section>

<section class="pad-sm rule">
  <div class="wrap next-show">
    <div class="frame r-9x16 reveal" style="max-height:80vh"><img src="{A}live-band.jpg" alt="Drummer on stage at The Cashew Tree" loading="lazy"></div>
    <div class="body reveal d1">
      <span class="eyebrow">Next show</span>
      <div class="next-date" data-next-thursday>Thursday</div>
      <p class="lede" data-next-sub>Every Thursday at The Cashew Tree.</p>
      <dl class="facts">
        <div><dt>Where</dt><dd>The garden</dd></div>
        <div><dt>Line-up</dt><dd>Band + DJ</dd></div>
        <div><dt>Entry</dt><dd>Walk in</dd></div>
      </dl>
      <div class="btn-row" style="margin-top:40px">
        <a class="btn solid" href="{IG}thecashewtree.collective/" target="_blank" rel="noopener">This week on Instagram <span class="arr">↗</span></a>
      </div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h2 reveal">Recent <em>line-ups</em></h2>
      <span class="eyebrow reveal">Posters by the Collective</span>
    </div>
    <div class="lineups">
{lineup_cards}
    </div>
  </div>
</section>
""" + FOOTER

# ------------------------------------------------------------------ COLLECTIVE
HOUSES = [
    ("The Cashew Tree", "Café & kitchen", "The heart of it all. A garden café open from first coffee to last cocktail, with live music on Thursdays and a playground out back.",
     ["Open 7:30am – 10pm", "Live music Thu", "Playground"], "thecashewtree.collective", ("img", "spread.jpg")),
    ("Toko Coastal", "Shop", "Curated for the coastal hearts. A small shop of things you want to take home from Bingin.",
     ["Clothing", "Homewares", "Kids", "Jewellery", "Skincare", "Beach essentials", "Open 9am – 9pm"], "toko.coastal", ("img", "toko.jpg")),
    ("Rotisserie by Cashew Tree", "Quick bites", "Hot rotisserie chicken, ready before and after the surf. Order on WhatsApp and it comes to you.",
     ["Rotisserie chicken", "Burgers", "Salad", "Slushies", "Free delivery in Bingin"], "rotisserie.cashewtree", ("img", "rotisserie.jpg")),
    ("Pak G", "Kitchen", "The chopsticks-ready corner of the Collective, right here in Bingin.",
     ["Bingin"], "pak.g.bingin", ("type", "G")),
    ("Bali Training Centre", "Fitness", "Uluwatu’s number one fitness centre, now part of the Collective. Train hard, then come next door for a coconut.",
     ["H.I.I.T", "Functional fitness", "Kettlebells", "Muay Thai", "BTC Boxing"], "bali_training_centre", ("img", "btc.jpg")),
]


def house(i, h):
    name, kind, text, tags, handle, media = h
    tg = "".join(f"<span>{t}</span>" for t in tags)
    if media[0] == "img":
        m = f'<div class="frame r-4x5"><img src="{A}{media[1]}" alt="{name}" loading="lazy"></div>'
    else:
        m = f'<div class="type-card"><span class="eyebrow" style="color:rgba(242,237,228,.7)">The Collective</span><span class="glyph">Pak {media[1]}</span><span>@{handle}</span></div>'
    return f"""  <article class="house wrap">
    <span class="idx">0{i+1}</span>
    <div class="body reveal">
      <span class="eyebrow">{kind}</span>
      <h2 class="h2">{name}</h2>
      <p>{text}</p>
      <div class="tags">{tg}</div>
      <a class="btn" href="{IG}{handle}/" target="_blank" rel="noopener">@{handle} <span class="arr">↗</span></a>
    </div>
    <div class="media reveal d1">{m}</div>
  </article>"""


collective = head("The Collective · The Cashew Tree Collective",
                  "The Cashew Tree Collective in Bingin, Bali: The Cashew Tree café, Toko Coastal, Rotisserie, Pak G and Bali Training Centre.") + header("collective.html") + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow reveal">Five houses, one tree</span>
    <h1 class="display reveal d1">The <em>Collective</em></h1>
    <p class="lede reveal d2">What started as a café is now a small village in Bingin. Eat, shop, train and stay all day.</p>
  </div>
</section>
{chr(10).join(house(i, h) for i, h in enumerate(HOUSES))}
""" + FOOTER

# ------------------------------------------------------------------ VISIT
visit = head("Visit · The Cashew Tree Collective",
             "Visit The Cashew Tree in Bingin, Uluwatu, Bali. Open daily 7:30am to 10pm. Live music Thursdays and a kids playground.") + header("visit.html") + f"""
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow reveal">Visit</span>
    <h1 class="display reveal d1">Find us under<br>the <em>tree</em>.</h1>
  </div>
</section>

<section class="pad-sm rule">
  <div class="wrap visit-grid">
    <div class="info reveal">
      <dl>
        <div class="row"><dt>Hours</dt><dd>7:30am – 10pm<small>Every day</small></dd></div>
        <div class="row"><dt>Live music</dt><dd>Thursday nights<small><a href="music.html" class="link-arrow">Thirsty Thursday →</a></small></dd></div>
        <div class="row"><dt>Where</dt><dd>Bingin, Uluwatu<small>Bukit Peninsula, Bali</small></dd></div>
        <div class="row"><dt>Say hi</dt><dd><a href="{IG}thecashewtree.collective/" target="_blank" rel="noopener">@thecashewtree.collective</a><small>DMs open for bookings &amp; events</small></dd></div>
      </dl>
      <div class="btn-row" style="margin-top:36px">
        <a class="btn solid" href="{MAPS}" target="_blank" rel="noopener">Get directions <span class="arr">↗</span></a>
        <a class="btn" href="{LINKTREE}" target="_blank" rel="noopener">All links</a>
      </div>
    </div>
    <div class="map reveal d1">
      <iframe title="Map to The Cashew Tree, Bingin" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://maps.google.com/maps?q=The%20Cashew%20Tree%20Bingin%20Bali&z=15&output=embed"></iframe>
    </div>
  </div>
</section>

<section class="pad" id="playground">
  <div class="wrap duo">
    <div class="a frame r-3x4 reveal"><img src="{A}playground.jpg" alt="Child with a coconut at the mushroom playhouse" loading="lazy"></div>
    <div class="b frame r-3x4 reveal d1"><img src="{A}little-one.jpg" alt="A toddler sitting on the playground" loading="lazy"></div>
    <div class="body reveal d2">
      <span class="eyebrow">For families</span>
      <h2 class="h2" style="margin:14px 0 20px">The <em>playground</em></h2>
      <p class="lede">A mushroom house, soft lawn and plenty of shade. The kids play, you finish your coffee while it is still hot.</p>
    </div>
  </div>
</section>
""" + FOOTER

for name, html in [("index.html", home), ("menu.html", menu), ("music.html", music),
                   ("collective.html", collective), ("visit.html", visit)]:
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)
    print("wrote", name)
