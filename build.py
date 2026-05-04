#!/usr/bin/env python3
"""Generate Mission Hygieia HTML pages."""
import os

# Output goes to the directory where this script is run from.
# - On Netlify, that's the repo root (set as Publish directory: ".")
# - Locally, run `python3 build.py` from inside the repo root
# - Override by setting environment variable: SITE_OUT=/some/path python3 build.py
OUT = os.environ.get("SITE_OUT", os.path.dirname(os.path.abspath(__file__)) or ".")

# ============================================================
# Logo: try logo.png first, fall back to inline SVG mark.
# The inline SVG is a typographic placeholder in Mission blue.
# ============================================================

LOGO_NAV = '''<a href="index.html" class="nav-logo" aria-label="Mission Hygieia home">
      <img class="logo-img" src="img/logo.jpg" alt="Mission Hygieia" />
    </a>'''

LOGO_FOOTER = '''<a href="index.html" class="nav-logo" style="display:inline-block;">
        <img class="logo-img-footer" src="img/logo.jpg" alt="Mission Hygieia" />
      </a>'''

FAVICON = '''<link rel="icon" type="image/jpeg" href="img/logo.jpg" />'''

# ============================================================
# HEAD + NAV + FOOTER templates
# ============================================================

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
""" + FAVICON + """
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,300;0,400;0,500;1,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="styles.css" />
</head>
<body>
"""


def nav(active):
    items = [
        ("index.html", "Home"),
        ("our-kits.html", "Our kits"),
        ("our-team.html", "Team"),
        ("shelters.html", "Shelters"),
        ("blog.html", "Blog"),
        ("contact.html", "Contact"),
    ]
    li = ""
    for href, label in items:
        cls = ' class="active"' if href == active else ""
        li += f'      <li><a href="{href}"{cls}>{label}</a></li>\n'
    donate_active = ' active' if active == 'donate.html' else ''
    return f"""<nav class="nav">
  <div class="nav-inner">
    {LOGO_NAV}
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-menu">
      <span class="nav-toggle-bar"></span>
      <span class="nav-toggle-bar"></span>
      <span class="nav-toggle-bar"></span>
    </button>
    <ul class="nav-links" id="nav-menu">
{li.rstrip()}
      <li><a href="donate.html" class="btn btn-primary{donate_active}" style="padding:8px 18px; font-size:14px;">Donate</a></li>
    </ul>
  </div>
</nav>
<script>
  (function() {{
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-links');
    if (!toggle || !menu) return;
    toggle.addEventListener('click', () => {{
      const isOpen = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(isOpen));
      toggle.classList.toggle('open', isOpen);
    }});
    // Close menu when a link is clicked
    menu.querySelectorAll('a').forEach(a => {{
      a.addEventListener('click', () => {{
        menu.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }});
    }});
  }})();
</script>
"""


FOOTER = f"""<footer class="footer">
  <div class="footer-inner">
    <div class="footer-brand">
      {LOGO_FOOTER}
      <p style="margin-top: var(--s-3);">A 501(c)(3) nonprofit delivering hygiene kits to people experiencing homelessness — locally and globally.</p>
    </div>
    <div class="footer-col">
      <h4>The mission</h4>
      <ul>
        <li><a href="our-kits.html">Our kits</a></li>
        <li><a href="shelters.html">Shelter partners</a></li>
        <li><a href="our-team.html">The team</a></li>
        <li><a href="blog.html">Blog</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Get involved</h4>
      <ul>
        <li><a href="donate.html">Donate</a></li>
        <li><a href="contact.html">Volunteer</a></li>
        <li><a href="contact.html">Start a chapter</a></li>
        <li><a href="contact.html">Partner with us</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <ul>
        <li><a href="mailto:nonprofithygieia@gmail.com">nonprofithygieia@gmail.com</a></li>
        <li><a href="contact.html">Send a message</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-social">
      <a href="https://www.instagram.com/missionhygieia/" aria-label="Mission Hygieia on Instagram" title="Instagram" target="_blank" rel="noopener noreferrer">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.6"/>
          <circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.6"/>
          <circle cx="17.5" cy="6.5" r="1.1" fill="currentColor"/>
        </svg>
      </a>
      <a href="https://www.tiktok.com/@missionhygieia" aria-label="Mission Hygieia on TikTok" title="TikTok" target="_blank" rel="noopener noreferrer">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <path d="M14 3v10.5a3 3 0 1 1-3-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M14 3c.3 2 1.6 3.6 4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </a>
      <a href="https://www.youtube.com/@MissionHygieiaOfficial" aria-label="Mission Hygieia on YouTube" title="YouTube" target="_blank" rel="noopener noreferrer">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="2.5" y="6" width="19" height="12" rx="3" stroke="currentColor" stroke-width="1.6"/>
          <path d="M10.5 9.5v5l4-2.5-4-2.5Z" fill="currentColor"/>
        </svg>
      </a>
    </div>
    <span>© 2026 Mission Hygieia · 501(c)(3) nonprofit organization</span>
    <span>Making hygiene accessible to all.</span>
  </div>
</footer>

</body>
</html>
"""


def write_page(filename, title, description, body):
    html = HEAD.format(title=title, description=description) + nav(filename) + body + FOOTER
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)
    print(f"  wrote {filename}")


# ============================================================
# PAGE BODIES
# ============================================================

INDEX_BODY = """
<!-- Hero -->
<section style="padding-top: var(--s-12); padding-bottom: var(--s-16);">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-text">
        <span class="eyebrow mb-3" style="display:block;">A 501(c)(3) nonprofit organization</span>
        <h1 class="display" style="max-width: 14ch;">
          Small kits.<br />Big <em>dignity</em>.
        </h1>
        <p class="lead mt-4" style="max-width: 56ch;">
          Mission Hygieia delivers hygiene kits to people experiencing homelessness in our community and around the world. Every kit is hand-assembled by volunteers and distributed through partner shelters and aid organizations.
        </p>
        <div class="mt-6" style="display:flex; gap: var(--s-2); flex-wrap: wrap;">
          <a href="donate.html" class="btn btn-primary">Donate</a>
          <a href="contact.html" class="btn btn-tertiary">Volunteer with us</a>
        </div>
      </div>
      <div class="hero-illustration">
        <img src="img/hero-illustration.png" alt="Pencil illustration of a cupped hand holding a water droplet and lotus leaves, with a soap bar and sparkles — a quiet symbol of care and hygiene." />
      </div>
    </div>
  </div>
</section>

<!-- The Basics — carousel -->
<section class="surface-warm">
  <div class="container">
    <span class="eyebrow mb-6" style="display:block;">The basics</span>

    <div class="carousel" id="basics-carousel">
      <div class="carousel-track">

        <div class="carousel-slide" data-slide="0">
          <span class="eyebrow text-blue mb-3" style="display:block;">Our impact</span>
          <span class="stat-num">880</span>
          <h2 class="mt-2">Kits donated, so far.</h2>
          <p class="lead mt-3" style="max-width: 56ch;">Hand-assembled by volunteers and distributed through our shelter and aid partners.</p>
        </div>

        <div class="carousel-slide" data-slide="1" hidden>
          <span class="eyebrow text-blue mb-3" style="display:block;">Reach</span>
          <span class="stat-num">Local + global</span>
          <h2 class="mt-2">From Northern Virginia to Haiti.</h2>
          <p class="lead mt-3" style="max-width: 56ch;">We serve shelters across the DMV and ship internationally through Medical Missionaries — wherever hygiene access is needed.</p>
        </div>

        <div class="carousel-slide" data-slide="2" hidden>
          <span class="eyebrow text-blue mb-3" style="display:block;">Shelter partners</span>
          <span class="stat-num">6</span>
          <h2 class="mt-2">Shelters donated to.</h2>
          <p class="lead mt-3" style="max-width: 56ch;">From Loudoun and Fairfax to Reston, plus international shipments through Medical Missionaries to Haiti.</p>
        </div>

        <div class="carousel-slide" data-slide="3" hidden>
          <span class="eyebrow text-blue mb-3" style="display:block;">Tax-deductible</span>
          <span class="stat-num">501(c)(3)</span>
          <h2 class="mt-2">Registered nonprofit.</h2>
          <p class="lead mt-3" style="max-width: 56ch;">Mission Hygieia is a 501(c)(3) registered nonprofit organization. Every donation is tax-deductible to the full extent allowed by law.</p>
        </div>

      </div>

      <div class="carousel-controls">
        <button class="carousel-btn" data-go="prev" aria-label="Previous slide">←</button>
        <div class="carousel-dots" role="tablist">
          <button class="carousel-dot active" data-target="0" aria-label="Slide 1"></button>
          <button class="carousel-dot" data-target="1" aria-label="Slide 2"></button>
          <button class="carousel-dot" data-target="2" aria-label="Slide 3"></button>
          <button class="carousel-dot" data-target="3" aria-label="Slide 4"></button>
        </div>
        <button class="carousel-btn" data-go="next" aria-label="Next slide">→</button>
      </div>
    </div>
  </div>
</section>

<!-- How it works -->
<section>
  <div class="container">
    <span class="eyebrow mb-3" style="display:block;">How it works</span>
    <h2 style="max-width: 18ch;">A simple loop. Donors fund it, volunteers build it, shelters distribute it.</h2>

    <div class="how-grid" style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--s-6); margin-top: var(--s-8);">
      <div>
        <span class="eyebrow text-blue">01 — Donate</span>
        <h3 class="mt-2 mb-2">Fund a kit.</h3>
        <p>Your donation covers the supplies and delivery for hygiene kits. We're a registered 501(c)(3), so every dollar is tax-deductible.</p>
      </div>
      <div>
        <span class="eyebrow text-blue">02 — Assemble</span>
        <h3 class="mt-2 mb-2">We build it.</h3>
        <p>Student volunteers gather monthly to pack kits in bulk. Wholesale supply runs mean your dollars buy supplies, not packaging.</p>
      </div>
      <div>
        <span class="eyebrow text-blue">03 — Distribute</span>
        <h3 class="mt-2 mb-2">Shelters hand it out.</h3>
        <p>Our six partners across Loudoun, Fairfax, and Reston distribute kits directly to residents who need them most.</p>
      </div>
    </div>
  </div>
</section>

<!-- Chapter CTA -->
<section class="surface-warm">
  <div class="container">
    <div style="max-width: 60ch;">
      <span class="eyebrow mb-3" style="display:block;">For students</span>
      <h2>Bring Mission Hygieia to your school.</h2>
      <p class="lead mt-3">We'll send the chapter playbook — supply lists, shelter intros, fundraising templates. Most chapters launch their first kit drive within a month.</p>
      <a href="contact.html" class="btn btn-secondary mt-6">Start a chapter</a>
    </div>
  </div>
</section>

<!-- Supporters -->
<section>
  <div class="container">
    <span class="eyebrow mb-6" style="display:block;">Our supporters</span>

    <div class="supporters-row" style="grid-template-columns: 1fr 1fr;">

      <div class="supporter-card">
        <img src="img/bfs.png" alt="Building Futures Society" class="supporter-logo" />
      </div>

      <div class="supporter-card">
        <img src="img/techsur.jpg" alt="TechSur Solutions" class="supporter-logo" />
      </div>

    </div>
  </div>
</section>

<style>
  @media (max-width: 720px) {
    .impact-stats { grid-template-columns: 1fr !important; gap: var(--s-4) !important; }
    .how-grid { grid-template-columns: 1fr !important; }
    .post-link { grid-template-columns: 1fr !important; gap: var(--s-1) !important; }
  }
</style>

<script>
  (function() {
    const carousel = document.getElementById('basics-carousel');
    if (!carousel) return;
    const slides = carousel.querySelectorAll('.carousel-slide');
    const dots = carousel.querySelectorAll('.carousel-dot');
    const prev = carousel.querySelector('[data-go="prev"]');
    const next = carousel.querySelector('[data-go="next"]');
    let current = 0;
    const total = slides.length;

    function show(idx) {
      current = ((idx % total) + total) % total;
      slides.forEach((s, i) => { s.hidden = (i !== current); });
      dots.forEach((d, i) => { d.classList.toggle('active', i === current); });
    }

    prev.addEventListener('click', () => show(current - 1));
    next.addEventListener('click', () => show(current + 1));
    dots.forEach((d, i) => { d.addEventListener('click', () => show(i)); });

    // Auto-advance every 6 seconds; pause on hover
    let timer = setInterval(() => show(current + 1), 6000);
    carousel.addEventListener('mouseenter', () => clearInterval(timer));
    carousel.addEventListener('mouseleave', () => {
      timer = setInterval(() => show(current + 1), 6000);
    });
  })();
</script>
"""


OUR_KITS_BODY = """
<section class="page-header">
  <div class="container">
    <span class="eyebrow">Kit supplies</span>
    <h1>What's in <em>each</em> kit.</h1>
    <p class="lead">We tailor each kit's contents based on who's receiving it.</p>
  </div>
</section>

<section>
  <div class="container">
    <figure style="margin: 0 auto var(--s-8); max-width: 480px;">
      <img src="img/kit-illustration.png" alt="A pencil illustration of a hygiene kit: a zippered toiletry pouch, toothbrush, toothpaste, deodorant, shampoo, soap pump, conditioner, soap bar, razor, body wipes, and feminine pads, with delicate leaves arranged around them." style="width: 100%; height: auto; display: block;" />
    </figure>

    <div class="kits-grid" style="display:grid; grid-template-columns: 1fr 1fr; gap: var(--s-8); max-width: 800px; margin: 0 auto;">

      <div>
        <h2 class="mb-4">Male kit</h2>
        <ul class="list-rule">
          <li>Toothbrush</li>
          <li>Toothpaste</li>
          <li>Deodorant</li>
          <li>Shaving kit</li>
          <li>Body soap</li>
          <li>Shampoo and conditioner</li>
          <li>Body lotion</li>
          <li>Body wipes</li>
        </ul>
      </div>

      <div>
        <h2 class="mb-4">Female kit</h2>
        <ul class="list-rule">
          <li>Toothbrush</li>
          <li>Toothpaste</li>
          <li>Deodorant</li>
          <li>Shaving kit</li>
          <li>Body soap</li>
          <li>Shampoo and conditioner</li>
          <li>Body lotion</li>
          <li>Body wipes</li>
          <li>Feminine pads</li>
        </ul>
      </div>

    </div>

    <div style="text-align: center; margin-top: var(--s-8);">
      <a href="donate.html" class="btn btn-primary">Donate</a>
    </div>
  </div>
</section>
"""


OUR_TEAM_BODY = """
<section class="page-header">
  <div class="container">
    <span class="eyebrow">The team</span>
    <h1>The people behind <em>Mission Hygieia</em>.</h1>
    <p class="lead">Mission Hygieia was founded by three students. We work between classes and gather monthly to assemble and deliver hygiene kits.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="team-grid" style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap: var(--s-6);">

      <div>
        <img src="img/akhil.jpg" alt="Portrait of Akhil Koranath" class="team-photo" />
        <span class="eyebrow mt-3" style="display: block;">Co-founder</span>
        <h3 class="mt-1 mb-2">Akhil Koranath</h3>
      </div>

      <div>
        <img src="img/sri.jpg" alt="Portrait of Sri Kasturi" class="team-photo" />
        <span class="eyebrow mt-3" style="display: block;">Co-founder</span>
        <h3 class="mt-1 mb-2">Sri Kasturi</h3>
      </div>

      <div>
        <img src="img/jhansi.jpg" alt="Portrait of Jhansi Chilakapati" class="team-photo" />
        <span class="eyebrow mt-3" style="display: block;">Communications Officer</span>
        <h3 class="mt-1 mb-2">Jhansi Chilakapati</h3>
      </div>

    </div>
  </div>
</section>

<section class="surface-warm">
  <div class="container">
    <div style="max-width: 60ch;">
      <span class="eyebrow mb-3" style="display:block;">Want to join us?</span>
      <h2>Pack kits with us.</h2>
      <p class="lead mt-3">We host an assembly drive once a month. No experience needed, just hands and time.</p>
      <a href="contact.html" class="btn btn-secondary mt-6">Volunteer with us</a>
    </div>
  </div>
</section>

<style>
  @media (max-width: 720px) {
    .team-grid { grid-template-columns: 1fr !important; gap: var(--s-6) !important; }
  }
</style>
"""


SHELTERS_BODY = """
<section class="page-header">
  <div class="container">
    <span class="eyebrow">Shelter partners</span>
    <h1>Six partners doing the <em>real</em> work.</h1>
    <p class="lead">We don't run shelters. We supply them. These are the organizations on the front line — the people who get our kits into the hands that need them.</p>
  </div>
</section>

<section>
  <div class="container">
    <ul class="list-rule">

      <li>
        <div class="shelter-row" style="display:grid; grid-template-columns: 1fr 200px; gap: var(--s-4); align-items: baseline;">
          <div>
            <h3 class="mb-2">Katherine Hanley Family Shelter</h3>
            <p class="caption mb-2"><span class="tag">Family shelter</span> &nbsp; <span class="tag">Fairfax, VA</span></p>
            <p>The first shelter we ever supplied. Provides emergency shelter and supportive services to families experiencing homelessness in Fairfax County.</p>
          </div>
          <div style="text-align: right;">
            <a href="tel:5715226800" class="btn-quiet">(571) 522-6800</a>
          </div>
        </div>
      </li>

      <li>
        <div class="shelter-row" style="display:grid; grid-template-columns: 1fr 200px; gap: var(--s-4); align-items: baseline;">
          <div>
            <h3 class="mb-2">Good Shepherd Alliance</h3>
            <p class="caption mb-2"><span class="tag">Transitional housing</span> &nbsp; <span class="tag">Loudoun County</span></p>
            <p>Runs transitional housing programs for individuals and families across Loudoun County, with a focus on long-term stability.</p>
          </div>
          <div style="text-align: right;">
            <a href="tel:7037241555" class="btn-quiet">(703) 724-1555</a>
          </div>
        </div>
      </li>

      <li>
        <div class="shelter-row" style="display:grid; grid-template-columns: 1fr 200px; gap: var(--s-4); align-items: baseline;">
          <div>
            <h3 class="mb-2">Mobile Hope</h3>
            <p class="caption mb-2"><span class="tag">Youth services</span> &nbsp; <span class="tag">Loudoun County</span></p>
            <p>Serves youth experiencing homelessness through a fleet of mobile units that meet kids where they are. One of our most active partners.</p>
          </div>
          <div style="text-align: right;">
            <a href="tel:7037711400" class="btn-quiet">(703) 771-1400</a>
          </div>
        </div>
      </li>

      <li>
        <div class="shelter-row" style="display:grid; grid-template-columns: 1fr 200px; gap: var(--s-4); align-items: baseline;">
          <div>
            <h3 class="mb-2">Medical Missionaries</h3>
            <p class="caption mb-2"><span class="tag">International aid</span> &nbsp; <span class="tag">Haiti</span></p>
            <p>Provides medical care, clean water, and basic supplies to communities in Haiti. We send shelf-stable kits with their international shipments.</p>
          </div>
          <div style="text-align: right;">
            <a href="tel:7033351800" class="btn-quiet">(703) 335-1800</a>
          </div>
        </div>
      </li>

      <li>
        <div class="shelter-row" style="display:grid; grid-template-columns: 1fr 200px; gap: var(--s-4); align-items: baseline;">
          <div>
            <h3 class="mb-2">Loudoun Homeless Services</h3>
            <p class="caption mb-2"><span class="tag">Coordinated entry</span> &nbsp; <span class="tag">Loudoun County</span></p>
            <p>The county's coordinated entry point. Loudoun Homeless Services assesses, refers, and places individuals and families into the right program.</p>
          </div>
          <div style="text-align: right;">
            <a href="tel:5712583033" class="btn-quiet">(571) 258-3033</a>
          </div>
        </div>
      </li>

      <li>
        <div class="shelter-row" style="display:grid; grid-template-columns: 1fr 200px; gap: var(--s-4); align-items: baseline;">
          <div>
            <h3 class="mb-2">Embry Rucker Community Shelter</h3>
            <p class="caption mb-2"><span class="tag">Emergency shelter</span> &nbsp; <span class="tag">Reston, VA</span></p>
            <p>Provides emergency shelter, day-shelter services, and case management for adults experiencing homelessness in Reston and surrounding areas.</p>
          </div>
          <div style="text-align: right;">
            <a href="tel:7034371975" class="btn-quiet">(703) 437-1975</a>
          </div>
        </div>
      </li>

    </ul>
  </div>
</section>

<section class="surface-warm">
  <div class="container">
    <div style="display:grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: var(--s-6);">
      <div class="stat">
        <span class="stat-num">5</span>
        <span class="eyebrow">Virginia partners</span>
      </div>
      <div class="stat">
        <span class="stat-num">1</span>
        <span class="eyebrow">International</span>
      </div>
      <div class="stat">
        <span class="stat-num">3</span>
        <span class="eyebrow">Counties served</span>
      </div>
      <div class="stat">
        <span class="stat-num">4–6</span>
        <span class="eyebrow">Weeks between drops</span>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width: 60ch;">
      <span class="eyebrow mb-3" style="display:block;">For shelter directors</span>
      <h2>Run a shelter? Let's talk.</h2>
      <p class="lead mt-3">If you serve people experiencing homelessness and your residents need hygiene supplies, we'd like to add you to our route. No paperwork burden — just a conversation about what your residents need most.</p>
      <a href="contact.html" class="btn btn-secondary mt-6">Become a partner</a>
    </div>
  </div>
</section>

<style>
  @media (max-width: 720px) {
    .shelter-row { grid-template-columns: 1fr !important; gap: var(--s-2) !important; }
    .shelter-row > div:last-child { text-align: left !important; }
  }
</style>
"""


# ============================================================
# BLOG POSTS — data-driven so adding new posts means appending to this list
# Order: newest first (this is also the order shown on the blog index)
# ============================================================

BLOG_POSTS = [
    {
        "slug": "loudoun-homeless-shelter-donation",
        "title": "Loudoun Homeless Shelter Donation",
        "date_iso": "2026-03-31",
        "date_display": "Mar 31, 2026",
        "image": "blog-loudoun.jpg",
        "alt": "A Mission Hygieia volunteer holding a box of donated kits in front of a vehicle, ready for delivery.",
        "summary": "Mission Hygieia donated 70 kits to a local homeless shelter that supports homeless individuals.",
        "body": [
            "On 03/31/2026, the Mission Hygieia team donated 70 kits to a local homeless shelter that supports homeless individuals.",
            "They provide the utmost care towards the members that take shelter. The staff members were extremely kind and assisted us the entire time.",
        ],
    },
    {
        "slug": "charm-bracelet-fundraiser",
        "title": "Charm Bracelet Fundraiser",
        "date_iso": "2026-02-02",
        "date_display": "Feb 2, 2026",
        "image": "blog-charm-bracelet.jpg",
        "alt": "Volunteers and donors gathered around tables of decorated charm bracelets.",
        "summary": "An immense success — a charm-bracelet-making fundraiser that generated a large crowd of donors.",
        "body": [
            "On 1/16/2026, the Mission Hygieia team held a charm-bracelet-making fundraiser.",
            "It was an immense success and generated a large crowd of donors. People engaged in creating stainless steel, custom bracelets to express themselves while making an impact.",
        ],
    },
    {
        "slug": "foodnotbombs-nova-donation",
        "title": "FoodNotBombs NOVA Donation",
        "date_iso": "2025-12-22",
        "date_display": "Dec 22, 2025",
        "image": "blog-foodnotbombs-3.jpeg",
        "alt": "Mission Hygieia volunteers walking into the FoodNotBombs NOVA Sunday meal site.",
        "summary": "200 kits donated to FoodNotBombs NOVA, who provide over 100 meals every Sunday.",
        "body": [
            "On 12/22/2025, the Mission Hygieia team donated 200 kits to a local non-profit supporting underprivileged communities.",
            "Food Not Bombs NOVA provides over 100 meals each week, every Sunday at 2:30 pm. This time, they will be including our hygiene kits.",
        ],
    },
    {
        "slug": "embry-rucker-donation",
        "title": "Embry Rucker Donation",
        "date_iso": "2025-12-07",
        "date_display": "Dec 7, 2025",
        "image": "blog-embry-rucker.jpeg",
        "alt": "Two Mission Hygieia volunteers carrying boxes of kits outside the Embry Rucker Community Shelter in Reston.",
        "summary": "100 kits donated to the Embry Rucker Homeless Shelter in Reston, VA.",
        "body": [
            "On 12/6/2025, the Mission Hygieia team donated 100 kits to the Embry Rucker Homeless Shelter in Reston, VA.",
            "The staff and team that helped us with the process of drop-off were incredibly kind and supported us throughout the entire process.",
        ],
    },
    {
        "slug": "medical-missionaries",
        "title": "Medical Missionaries",
        "date_iso": "2025-09-20",
        "date_display": "Sep 20, 2025",
        "image": "blog-medical-missionaries.jpeg",
        "alt": "Medical Missionaries logo — a globe surrounded by people holding hands, on a navy background.",
        "summary": "25 hygiene kits donated to families in Haiti through the Medical Missionaries.",
        "body": [
            "At Mission Hygieia, we're proud to have assembled and donated 25 hygiene kits to families in Haiti, helping provide essential items to those in need.",
            "Each kit represents our commitment to promoting health, dignity, and compassion across communities. We're deeply thankful to the Medical Missionaries for giving us the opportunity to support their incredible work and make a small difference together.",
        ],
    },
    {
        "slug": "mobile-hope",
        "title": "Mobile Hope",
        "date_iso": "2025-06-26",
        "date_display": "Jun 26, 2025",
        "image": "blog-mobile-hope.jpeg",
        "alt": "Mobile Hope of Loudoun delivery van — large heart graphic on the side panel.",
        "summary": "Personalized hygiene kits donated to Mobile Hope of Leesburg for the homeless they serve.",
        "body": [
            "This week we were honored to donate personalized hygiene kits to Mobile Hope of Leesburg — each packed with essentials to bring comfort to those in need.",
            "Thank you to Mobile Hope for welcoming us and for the incredible work they do every day in serving the homeless. We're grateful for the opportunity to support our mission.",
        ],
    },
    {
        "slug": "good-shepard-alliance",
        "title": "Good Shepard Alliance",
        "date_iso": "2025-02-22",
        "date_display": "Feb 22, 2025",
        "image": "blog-foodnotbombs-1.jpeg",
        "alt": "Mission Hygieia volunteer holding a cardboard box of donated kits.",
        "summary": "Hygiene kits donated to the Good Shepard Alliance Shelter.",
        "body": [
            "We donated our hygiene kits this Saturday at Good Shepard Alliance Shelter.",
            "I want to thank them for allowing us to donate, as well as those who donated to us so we are able to fund our kits.",
        ],
    },
    {
        "slug": "valentines-day-fundraiser",
        "title": "Valentine's Day Fundraiser",
        "date_iso": "2025-01-24",
        "date_display": "Jan 24, 2025",
        "image": "blog-valentines.jpeg",
        "alt": "Kids at a Mission Hygieia fundraiser table painting cups.",
        "summary": "A cup-painting fundraiser at Brambleton, with a great community turnout.",
        "body": [
            "This Friday, we held our Valentine's Fundraiser, in which we designed cups with paint.",
            "I want to thank Brambleton for letting us use their space for our fundraiser and appreciate everyone who showed up.",
        ],
    },
    {
        "slug": "krispy-kreme-fundraiser",
        "title": "Krispy Kreme Fundraiser",
        "date_iso": "2024-12-07",
        "date_display": "Dec 7, 2024",
        "image": "blog-krispy-kreme.jpeg",
        "alt": "An open box of Krispy Kreme glazed doughnuts.",
        "summary": "Started a Krispy Kreme donut + coffee fundraiser to raise money for kits.",
        "body": [
            "This Saturday, we started our Krispy Kreme fundraiser, where we sell Krispy Kreme donuts and coffee to raise money for kits.",
            "I want to thank Krispy Kreme for letting us fundraise and anyone who supported us and bought items.",
        ],
    },
    {
        "slug": "katherine-hanley-shelter",
        "title": "Katherine Hanley Shelter",
        "date_iso": "2024-12-01",
        "date_display": "Dec 1, 2024",
        "image": "blog-katherine-hanley.jpeg",
        "alt": "Signage at the entrance to Katherine K. Hanley Family Shelter at 12970 Katherine Hanley Court.",
        "summary": "Hygiene kits donated to the Katherine Hanley Shelter.",
        "body": [
            "We donated our hygiene kits this Sunday at Katherine Hanley Shelter.",
            "I want to thank them for allowing us to donate and others who donated to us so that we could fund these kits.",
        ],
    },
    {
        "slug": "henna-for-hygieia",
        "title": "Henna For Hygieia",
        "date_iso": "2024-10-05",
        "date_display": "Oct 5, 2024",
        "image": "blog-henna.jpeg",
        "alt": "Two hands with intricate floral henna designs.",
        "summary": "A henna fundraiser at Brambleton Town Center — donors received custom henna designs.",
        "body": [
            "This Saturday at Brambleton Town Center, we did a henna fundraiser, in which those who would spend 5 dollars for a donation would receive a variation of their choosing of different images of henna on their hand.",
            "Overall, it was a very successful fundraiser, and thank you to everyone who came out to support us.",
        ],
    },
    {
        "slug": "club-expo",
        "title": "Club Expo",
        "date_iso": "2024-09-11",
        "date_display": "Sep 11, 2024",
        "image": "blog-club-expo.jpeg",
        "alt": "Mission Hygieia booth at Rock Ridge High School Club Expo, with informational poster, kit display, and laptops.",
        "summary": "Mission Hygieia officially became a club at Rock Ridge High School.",
        "body": [
            "Thank you very much, Rock Ridge High School, for letting us have the opportunity to make a club. The expo was a huge success.",
            "Many people who came by were very interested in the club and loved the idea of sending kits to the homeless, and some even signed up. Our interest meeting will be on Thursday, September 19th, from 4:30 to 5:00 pm.",
            "Again, thank you, Rock Ridge High School, for allowing us to make this club.",
        ],
    },
    {
        "slug": "bake-sale",
        "title": "Bake Sale",
        "date_iso": "2024-08-13",
        "date_display": "Aug 13, 2024",
        "image": "blog-bake-sale.jpeg",
        "alt": "A tray of green and pink cupcakes with white frosting and gold accents.",
        "summary": "A successful bake sale outside Bunny Tea — homemade brownies, cake pops, cupcakes.",
        "body": [
            "We had a successful bake sale today. We made many homemade treats like brownies, cake pops, and cupcakes.",
            "We want to thank Bunny Tea for letting us set up outside, and everyone who bought a treat. Thank you.",
        ],
    },
    {
        "slug": "delivering-goods",
        "title": "Delivering Goods",
        "date_iso": "2024-08-13",
        "date_display": "Aug 13, 2024",
        "image": "blog-foodnotbombs-2.jpeg",
        "alt": "Mission Hygieia volunteer with a 50-kit box ready for delivery.",
        "summary": "Our first YouTube video and a desserts delivery to the Loudoun Homeless Shelter.",
        "body": [
            "Over the last weekend, we shot our first YouTube video. We did the Blind, Deaf, and Mute baking challenge. Please check our social media to watch the videos.",
            "All the desserts we made were distributed at the Loudoun Homeless Shelter.",
        ],
    },
    {
        "slug": "time-to-pack",
        "title": "Time To Pack",
        "date_iso": "2024-08-12",
        "date_display": "Aug 12, 2024",
        "image": "blog-time-to-pack.jpeg",
        "alt": "Mission Hygieia female kit contents laid out: lotion, bath soaps, body wipes, washcloths, shampoo, razor, toothbrush, toothpaste, and the navy drawstring tote.",
        "summary": "Packed our first 100 kits — 50 male and 50 female.",
        "body": [
            "Today we have been lucky enough to receive all the necessities to complete our kits. Mission Hygieia is very thankful to those who have donated funds to help us build stock.",
            "We packed our first 100 kits — 50 male and 50 female. Stay tuned for updates on the delivery of the kits.",
        ],
    },
    {
        "slug": "bunny-tea",
        "title": "Bunny Tea",
        "date_iso": "2024-08-06",
        "date_display": "Aug 6, 2024",
        "image": "blog-bunny-tea-event.jpg",
        "alt": "Bunny Tea promotional graphic — two illustrated boba drinks with the location 22855 Brambleton Plaza Ste G-103, Brambleton VA.",
        "summary": "Spin-the-wheel donation game at Bunny Tea — our second fundraiser.",
        "body": [
            "Our second fundraiser was the following week at Bunny Tea, a cozy boba tea cafe. We conducted a spin-the-wheel game for new donations.",
            "Participants could spin a wheel for $5 and win a prize. This idea worked wonderfully and we thank everyone for their donation and questions.",
        ],
        "extra_images": [
            ("blog-bunny-tea.jpeg", "Bunny Tea storefront sign featuring the rabbit-and-boba-cup logo."),
        ],
    },
    {
        "slug": "kokee-tea",
        "title": "Kokee Tea",
        "date_iso": "2024-07-31",
        "date_display": "Jul 31, 2024",
        "image": "blog-kokee-tea-event.jpg",
        "alt": "Mission Hygieia fundraising table outside Kokee Tea — informational poster, kit display, candy prize basket, and a Hygieia x Kokee fundraiser flyer.",
        "summary": "The first ever Mission Hygieia fundraiser — held at Kokee Tea.",
        "body": [
            "We began the journey of Mission Hygieia with a fundraiser at Kokee Tea. They were wonderful hosts, and we appreciate their partnership with us.",
            "This event marked our first fundraiser for Mission Hygieia, and we were thrilled by the interest and support from the community. As a team, we are grateful for the donations received that day.",
        ],
    },
]


def _build_blog_index():
    """Generate the blog index page body from BLOG_POSTS."""
    items = []
    for p in BLOG_POSTS:
        items.append(f'''      <li>
        <a href="{p["slug"]}.html" class="post-link" style="display:grid; grid-template-columns: 150px 1fr auto; gap: var(--s-4); align-items: center; text-decoration: none; color: inherit;">
          <img src="img/{p["image"]}" alt="" class="post-thumb" />
          <div>
            <span class="eyebrow">{p["date_display"]} · 1 min read</span>
            <h3 class="mt-2 mb-1">{p["title"]}</h3>
            <p class="caption">{p["summary"]}</p>
          </div>
          <span class="text-blue" aria-hidden="true">→</span>
        </a>
      </li>''')
    list_html = "\n\n".join(items)
    return f"""
<section class="page-header">
  <div class="container">
    <span class="eyebrow">Blog</span>
    <h1>Stories from the <em>field</em>.</h1>
    <p class="lead">Updates from our shelter donations, fundraisers, and the work behind every kit.</p>
  </div>
</section>

<section>
  <div class="container">
    <ul class="list-rule">

{list_html}

    </ul>
  </div>
</section>

<style>
  .post-thumb {{
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 8px;
    display: block;
  }}
  @media (max-width: 720px) {{
    .post-link {{ grid-template-columns: 1fr !important; gap: var(--s-2) !important; }}
    .post-thumb {{ aspect-ratio: 16 / 9; }}
  }}
</style>
"""


def _build_blog_post_body(p):
    """Generate an individual post page body from a post dict."""
    body_html = "\n      ".join(
        f'<p class="{("lead" if i==0 else "mt-4")}">{para}</p>'
        for i, para in enumerate(p["body"])
    )

    extra_imgs_html = ""
    for img_file, img_alt in p.get("extra_images", []):
        extra_imgs_html += f'''
    <figure style="margin: var(--s-6) 0 0; max-width: 540px;">
      <img src="img/{img_file}" alt="{img_alt}" style="width: 100%; height: auto; border-radius: 8px; display: block;" />
    </figure>'''

    return f"""
<section class="page-header page-header--post">
  <div class="container">
    <a href="blog.html" class="btn-quiet" style="display:inline-block; margin-bottom: var(--s-3);">← All posts</a>
    <span class="eyebrow">{p["date_display"]} · 1 min read</span>
    <h1 style="margin-top: var(--s-2); max-width: 22ch;">{p["title"]}</h1>
  </div>
</section>

<section style="padding-top: 0; border-top: none;">
  <div class="container">
    <div class="post-body-grid">
      <figure class="post-body-figure" style="margin: 0;">
        <img src="img/{p["image"]}" alt="{p["alt"]}" style="width: 100%; height: auto; border-radius: 8px; display: block;" />
      </figure>
      <div class="post-body-text">
        {body_html}{extra_imgs_html}
      </div>
    </div>
  </div>
</section>

<section class="surface-warm">
  <div class="container">
    <div style="max-width: 60ch;">
      <span class="eyebrow mb-3" style="display:block;">Help us deliver more</span>
      <h2>Help us deliver more kits.</h2>
      <p class="lead mt-3">Every donation goes directly to supplies and delivery — no overhead, no paid staff.</p>
      <a href="donate.html" class="btn btn-primary mt-6">Donate</a>
    </div>
  </div>
</section>
"""


BLOG_BODY = _build_blog_index()


CONTACT_BODY = """
<section class="page-header">
  <div class="container">
    <span class="eyebrow">Get in touch</span>
    <h1>Say <em>hello</em>.</h1>
    <p class="lead">Volunteer, sponsor a stack, start a chapter at your school, or just send a note. We read everything that comes in.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="contact-grid" style="display:grid; grid-template-columns: 1fr 1.4fr; gap: var(--s-8); align-items: start;">

      <div>
        <span class="eyebrow mb-3" style="display:block;">By email</span>
        <h3 class="mb-2"><a href="mailto:nonprofithygieia@gmail.com">nonprofithygieia@gmail.com</a></h3>
        <p class="caption">We try to write back within a couple of days. Slower during finals weeks.</p>

        <hr class="divider" />

        <span class="eyebrow mb-3" style="display:block;">What brings you here?</span>
        <ul class="list-rule">
          <li>
            <h4 class="mb-1">Volunteer</h4>
            <p class="caption">Pack kits with us. We host an assembly drive once a month, usually a Saturday afternoon.</p>
          </li>
          <li>
            <h4 class="mb-1">Start a chapter</h4>
            <p class="caption">Bring Mission Hygieia to your school. We'll send the playbook.</p>
          </li>
          <li>
            <h4 class="mb-1">Shelter partnership</h4>
            <p class="caption">You serve people who need kits. Let's get you on the route.</p>
          </li>
          <li>
            <h4 class="mb-1">Corporate sponsor</h4>
            <p class="caption">Looking to fund a stack of kits or sponsor an assembly drive? Tell us about your company.</p>
          </li>
        </ul>
      </div>

      <div>
        <h2 class="mb-4">Send us a message.</h2>

        <form onsubmit="event.preventDefault(); alert('Thanks. We will be in touch.');">
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap: var(--s-3);">
            <div class="form-row">
              <label for="name">Your name</label>
              <input type="text" id="name" required />
            </div>
            <div class="form-row">
              <label for="email">Email</label>
              <input type="email" id="email" required />
            </div>
          </div>

          <div class="form-row">
            <label for="reason">What's this about?</label>
            <select id="reason">
              <option>I want to volunteer</option>
              <option>I want to start a chapter</option>
              <option>I run a shelter</option>
              <option>I represent a company / corporate sponsor</option>
              <option>Press inquiry</option>
              <option>Just saying hi</option>
            </select>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap: var(--s-3);">
            <div class="form-row">
              <label for="org">Organization (optional)</label>
              <input type="text" id="org" placeholder="School, company, or shelter" />
            </div>
            <div class="form-row">
              <label for="location">Where are you?</label>
              <input type="text" id="location" placeholder="City, state" />
            </div>
          </div>

          <div class="form-row">
            <label for="message">Your message</label>
            <textarea id="message" required></textarea>
          </div>

          <div style="display:flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: var(--s-2); margin-top: var(--s-4);">
            <p class="caption">We never share your email. Promise.</p>
            <button type="submit" class="btn btn-secondary">Send message</button>
          </div>
        </form>
      </div>

    </div>
  </div>
</section>

<section class="surface-warm">
  <div class="container">
    <span class="eyebrow mb-3" style="display:block;">Quick answers</span>
    <h2>Things we get asked a lot.</h2>

    <div class="container-read" style="margin: var(--s-6) auto 0; padding: 0;">
      <details style="border-bottom: 1px solid var(--rule); padding: var(--s-3) 0;">
        <summary style="cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 17px; color: var(--ink); list-style: none; display:flex; justify-content: space-between; align-items: center;">
          <span>How much of my donation actually goes to kits?</span>
          <span style="color: var(--blue);">+</span>
        </summary>
        <p class="mt-3">Most of it. We buy supplies wholesale, our team is unpaid, and we don't have an office. The remainder covers shipping to shelters, the bag itself, and basic operating costs.</p>
      </details>

      <details style="border-bottom: 1px solid var(--rule); padding: var(--s-3) 0;">
        <summary style="cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 17px; color: var(--ink); list-style: none; display:flex; justify-content: space-between; align-items: center;">
          <span>Are you a registered 501(c)(3)?</span>
          <span style="color: var(--blue);">+</span>
        </summary>
        <p class="mt-3">Yes. We incorporated as a 501(c)(3) in February 2025. All donations are tax-deductible to the full extent allowed by law. You'll receive a receipt by email after donating.</p>
      </details>

      <details style="border-bottom: 1px solid var(--rule); padding: var(--s-3) 0;">
        <summary style="cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 17px; color: var(--ink); list-style: none; display:flex; justify-content: space-between; align-items: center;">
          <span>I want to start a chapter at my school. What does that involve?</span>
          <span style="color: var(--blue);">+</span>
        </summary>
        <p class="mt-3">A small commitment, mostly. You'll need three to five students, a faculty sponsor, and ideally one shelter partner near you. We'll send our chapter playbook and do a video call to walk you through it. Most chapters run their first kit drive within a month.</p>
      </details>

      <details style="border-bottom: 1px solid var(--rule); padding: var(--s-3) 0;">
        <summary style="cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 17px; color: var(--ink); list-style: none; display:flex; justify-content: space-between; align-items: center;">
          <span>Can I donate physical supplies instead of money?</span>
          <span style="color: var(--blue);">+</span>
        </summary>
        <p class="mt-3">Sometimes — but cash usually goes further. Because we buy in bulk, every dollar stretches significantly compared to retail prices. If you want to donate supplies (especially full unopened cases of soap, toothpaste, or feminine products), email us first so we can coordinate.</p>
      </details>

      <details style="border-bottom: 1px solid var(--rule); padding: var(--s-3) 0;">
        <summary style="cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 17px; color: var(--ink); list-style: none; display:flex; justify-content: space-between; align-items: center;">
          <span>Are volunteer hours certified for school requirements?</span>
          <span style="color: var(--blue);">+</span>
        </summary>
        <p class="mt-3">Yes. We track volunteer hours and provide signed verification for service-hour requirements (NHS, IB CAS, and similar). Just let us know what form your school uses.</p>
      </details>
    </div>
  </div>
</section>

<style>
  @media (max-width: 720px) {
    .contact-grid { grid-template-columns: 1fr !important; gap: var(--s-6) !important; }
  }
</style>
"""




DONATE_BODY = """
<section class="page-header">
  <div class="container">
    <span class="eyebrow">Donate</span>
    <h1>Donate via Zelle for <em>maximum</em> impact.</h1>
    <p class="lead">One of the best ways to support Mission Hygieia is by donating through Zelle. There are no processing fees, so 100% of your contribution goes directly to the people we serve.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="container-read" style="padding: 0; margin: 0;">
      <span class="eyebrow mb-3" style="display:block;">How to donate via Zelle</span>
      <h2>Six steps. About two minutes.</h2>

      <ol class="donate-steps mt-6">
        <li>
          <span class="donate-step-num">1</span>
          <div>
            <h3 class="mb-1">Log into your bank account</h3>
            <p>Sign in to your online banking or mobile banking app, where Zelle is available.</p>
          </div>
        </li>
        <li>
          <span class="donate-step-num">2</span>
          <div>
            <h3 class="mb-1">Select "Send money"</h3>
            <p>Locate the option to send money using Zelle within your banking app.</p>
          </div>
        </li>
        <li>
          <span class="donate-step-num">3</span>
          <div>
            <h3 class="mb-1">Enter our Zelle email address</h3>
            <p>For the recipient, enter our Zelle email address: <a href="mailto:fundraiser.mh@gmail.com"><strong>fundraiser.mh@gmail.com</strong></a></p>
          </div>
        </li>
        <li>
          <span class="donate-step-num">4</span>
          <div>
            <h3 class="mb-1">Specify the donation amount</h3>
            <p>Enter the amount you wish to donate.</p>
          </div>
        </li>
        <li>
          <span class="donate-step-num">5</span>
          <div>
            <h3 class="mb-1">Include a note (optional)</h3>
            <p>Please include a note if you'd like to provide any specific information or designations for your donation.</p>
          </div>
        </li>
        <li>
          <span class="donate-step-num">6</span>
          <div>
            <h3 class="mb-1">Confirm and send</h3>
            <p>Double-check the details, and when you're ready, confirm the transaction.</p>
          </div>
        </li>
      </ol>

      <div class="callout mt-8">
        <p>Your generous contribution through Zelle ensures that 100% of your donation directly supports our initiatives. We deeply appreciate your commitment to making a meaningful difference in the lives of those we serve.</p>
      </div>
    </div>
  </div>
</section>

<section class="surface-warm">
  <div class="container">
    <div style="max-width: 60ch;">
      <span class="eyebrow mb-3" style="display:block;">Questions?</span>
      <h2>Get in touch.</h2>
      <p class="lead mt-3">If you have any questions about donating, partnerships, or other ways to support our work, send us a note.</p>
      <a href="contact.html" class="btn btn-secondary mt-6">Contact us</a>
    </div>
  </div>
</section>

<style>
  .donate-steps {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .donate-steps > li {
    display: grid;
    grid-template-columns: 56px 1fr;
    gap: var(--s-3);
    padding: var(--s-3) 0;
    border-top: 1px solid var(--rule);
    align-items: start;
  }
  .donate-steps > li:last-child {
    border-bottom: 1px solid var(--rule);
  }
  .donate-step-num {
    font-family: 'Lora', Georgia, serif;
    font-weight: 300;
    font-size: 36px;
    line-height: 1;
    color: var(--blue);
    width: 48px;
    height: 48px;
    border: 1px solid var(--blue);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  @media (max-width: 480px) {
    .donate-steps > li { grid-template-columns: 44px 1fr; gap: var(--s-2); }
    .donate-step-num { font-size: 28px; width: 40px; height: 40px; }
  }
</style>
"""


# ============================================================
# WRITE PAGES
# ============================================================
print("Generating pages...")
write_page("index.html",
           "Mission Hygieia — Hygiene kits for people experiencing homelessness",
           "A 501(c)(3) nonprofit delivering hygiene kits to people experiencing homelessness — locally and globally.",
           INDEX_BODY)
write_page("our-kits.html",
           "Our Kits — Mission Hygieia",
           "What's inside a Mission Hygieia hygiene kit and why every item matters.",
           OUR_KITS_BODY)
write_page("our-team.html",
           "Our Team — Mission Hygieia",
           "Meet the student founders behind Mission Hygieia.",
           OUR_TEAM_BODY)
write_page("shelters.html",
           "Shelter Partners — Mission Hygieia",
           "The shelters and aid organizations that distribute Mission Hygieia kits — locally and internationally.",
           SHELTERS_BODY)
write_page("contact.html",
           "Contact — Mission Hygieia",
           "Volunteer, partner, start a chapter, or just say hello.",
           CONTACT_BODY)
write_page("donate.html",
           "Donate — Mission Hygieia",
           "Donate via Zelle to support Mission Hygieia. 100% of your donation supports our mission. 501(c)(3) tax-deductible.",
           DONATE_BODY)
write_page("blog.html",
           "Blog — Mission Hygieia",
           "Stories from the field — shelter donations, fundraisers, and the work behind every kit.",
           BLOG_BODY)

# Generate one HTML page per blog post from BLOG_POSTS data
for _post in BLOG_POSTS:
    write_page(f'{_post["slug"]}.html',
               f'{_post["title"]} — Mission Hygieia',
               _post["summary"],
               _build_blog_post_body(_post))

print("Done.")
