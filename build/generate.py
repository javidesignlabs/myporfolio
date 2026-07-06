# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from data import PROJECTS, CAREER, FEEDBACK, PROCESS_STEPS, PROFILE, CLIENTS, PROOF, CAPABILITIES
from templates import page_shell, ARROW, PLUS

OUT = os.path.join(os.path.dirname(__file__), "..")

# Short year labels per project (real eras from the case studies)
YEARS = {
    "saas-supply-chain": "2022–23",
    "bolttech-design-system": "2021–23",
    "partner-portals": "2021–23",
    "saas-process-modeling": "2022–23",
    "payment-renewal": "2019",
    "landing-pages-dorna": "2016–21",
    "roku-tv-app": "2016–21",
    "email-marketing-dorna": "2016–21",
    "desigual-product-card": "2013–16",
    "desigual-store-locator": "2014",
}


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def client_strip():
    spans = "".join(f"<span>{c}</span>" for c in CLIENTS)
    return f'''  <div class="client-strip" aria-hidden="true">
    <div class="client-track">{spans}{spans}</div>
  </div>'''


def work_rows(projects, root):
    rows = []
    for p in projects:
        rows.append(f'''<a class="work-row" href="{root}projects/{p["slug"]}.html" data-img="{p["cover_img"]}" data-reveal>
  <span class="work-thumb-inline"><img src="{p["cover_img"]}" alt="" loading="lazy"></span>
  <span class="year">{YEARS[p["slug"]]}</span>
  <h3>{p["title"]}</h3>
  <span class="cat">{p["tag"]} · {p["company"]}</span>
  <span class="go">{ARROW}</span>
</a>''')
    return "\n".join(rows)


# ----------------------------------------------------------------
# HOME
# ----------------------------------------------------------------
def build_home():
    root = ""
    featured = PROJECTS[:6]

    proof_cells = "\n".join(f'''<div class="proof-cell" data-reveal>
  <div class="num">{n}<small>{unit}</small></div>
  <p class="what">{what}</p>
  <span class="mono src">{src}</span>
</div>''' for n, unit, what, src in PROOF)

    caps_items = "\n".join(
        f'<li data-reveal><span class="mono">0{i+1}</span>{c}</li>'
        for i, c in enumerate(CAPABILITIES)
    )

    steps = "\n".join(f'''<div class="step" data-reveal>
  <span class="n">/{num}</span>
  <div>
    <h3>{name}</h3>
    <p>{text}</p>
  </div>
</div>''' for name, num, text in PROCESS_STEPS)

    quotes = "\n".join(f'''<div class="quote-cell" data-reveal>
  <blockquote>{q}</blockquote>
  <span class="mono">Feedback from my team</span>
</div>''' for q in FEEDBACK)

    body = f'''
  <section class="hero" style="padding-top:0;padding-bottom:0;">
    <div class="hero-grid-bg" aria-hidden="true"></div>
    <div class="container hero-inner">
      <div class="hero-top">
        <div class="hero-meta">
          <span class="mono">Senior Product Designer · Design Systems</span>
          <span class="mono">Las Palmas ↔ Madrid · Since 2011</span>
        </div>
        <div class="hero-card">
          <img src="{PROFILE['avatar_hero']}" alt="Javier de la Cruz">
          <div>
            <b>Javier de la Cruz</b>
            <small>Open to collaborate</small>
          </div>
        </div>
      </div>
      <h1 class="t-hero fit-bound">
        <span class="hero-line"><span class="fit" data-max="230">Design that</span></span>
        <span class="hero-line"><span class="fit" data-max="230"><span class="outline">ships</span> &amp;</span></span>
        <span class="hero-line"><span class="fit" data-max="230"><span class="accent">performs</span></span></span>
      </h1>
      <div class="hero-sub">
        <p data-reveal>I'm Javi — Senior Product Designer specialized in design systems, connecting Product, Design and Engineering to ship scalable digital experiences. 10+ years across SaaS, e-commerce and TV apps.</p>
        <a href="projects.html" class="btn" data-reveal><span>Explore the work</span>{ARROW}</a>
      </div>
    </div>
    {client_strip()}
  </section>

  <section class="proof">
    <div class="container">
      <div class="sect-head">
        <div>
          <span class="mono">Measured, not claimed</span>
          <h2 class="t-sect">Results with <span class="outline">receipts</span></h2>
        </div>
      </div>
      <div class="proof-grid">
{proof_cells}
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="sect-head">
        <div>
          <span class="mono">Selected work · 2014 — today</span>
          <h2 class="t-sect">Case <span class="outline">studies</span></h2>
        </div>
        <a href="projects.html" class="btn btn--ghost"><span>All projects</span>{ARROW}</a>
      </div>
      <div class="work-list">
{work_rows(featured, root)}
      </div>
    </div>
  </section>

  <section class="caps">
    <div class="container caps-grid">
      <div class="caps-copy">
        <span class="mono" style="display:block;margin-bottom:18px;">What I do</span>
        <h2 class="t-sect" style="margin-bottom:26px;">Complex in, <span class="accent">clear</span> out</h2>
        <p data-reveal>I help teams build better digital products through scalable design systems, reusable component libraries and user-centered experiences.</p>
        <p data-reveal>My role combines UX design, design system strategy, stakeholder collaboration and design operations — ensuring consistency across products while accelerating delivery for both designers and developers.</p>
      </div>
      <ul class="caps-list">
{caps_items}
      </ul>
    </div>
  </section>

  <section>
    <div class="container process-wrap">
      <div class="process-side">
        <span class="mono">Method</span>
        <h2 class="t-sect">How I <span class="outline">work</span></h2>
        <p data-reveal>Six steps, one loop. Every project starts with the problem and ends with measured results — then iterates.</p>
      </div>
      <div>
{steps}
      </div>
    </div>
  </section>

  <section class="quotes">
    <div class="container">
      <div class="sect-head">
        <div>
          <span class="mono">People I've shipped with</span>
          <h2 class="t-sect">Team <span class="outline">feedback</span></h2>
        </div>
      </div>
      <div class="quote-rail">
{quotes}
      </div>
    </div>
  </section>
'''
    jsonld = person_jsonld()
    write("index.html", page_shell(
        "Javier de la Cruz — Senior Product Designer · Design Systems | javidesignlabs",
        "Senior Product Designer specialized in Design Systems, based between Las Palmas & Madrid. 10+ years creating scalable digital experiences by connecting Product, Design and Engineering.",
        root, body, active="index.html", bg_word="JAVI", path="", jsonld=jsonld
    ))


# ----------------------------------------------------------------
# PROJECTS LISTING
# ----------------------------------------------------------------
def build_projects():
    root = ""
    body = f'''
  <section class="page-hero">
    <div class="container">
      <span class="mono">Selected work · {len(PROJECTS)} case studies</span>
      <h1 class="t-giant">Every project, <span class="outline">documented</span></h1>
      <p class="lede" data-reveal>Context, problem, research, design and measured impact — the full story behind each build, from MotoGP to Bolttech.</p>
    </div>
  </section>
  <section style="padding-top:0;">
    <div class="container">
      <div class="work-list">
{work_rows(PROJECTS, root)}
      </div>
    </div>
  </section>
'''
    write("projects.html", page_shell(
        "Projects — javidesignlabs",
        "10 documented case studies: design systems, SaaS platforms, e-commerce and TV apps.",
        root, body, active="projects.html", bg_word="WORK", path="projects.html"
    ))


# ----------------------------------------------------------------
# ABOUT
# ----------------------------------------------------------------
def build_about():
    root = ""
    timeline = "\n".join(f'''<div class="tl-item" data-reveal>
  <div class="tl-row" role="button" tabindex="0">
    <span class="when">{when}</span>
    <span class="what">{what}</span>
    <span class="plus">{PLUS}</span>
  </div>
  <div class="tl-panel"><p>{desc}</p></div>
</div>''' for when, what, desc in CAREER)

    body = f'''
  <section class="page-hero" style="padding-bottom:0;">
    <div class="container">
      <span class="mono">About &amp; contact</span>
      <h1 class="t-giant">Hi, I'm <span class="accent">Javi</span></h1>
    </div>
  </section>

  <section>
    <div class="container about-grid">
      <div class="about-photo" data-reveal>
        <img src="{PROFILE['avatar_about']}" alt="Javier de la Cruz">
        <div class="strip">
          <span class="mono">Javier de la Cruz</span>
          <span class="mono"><b>●</b> Available</span>
        </div>
      </div>
      <div class="about-copy">
        <p data-reveal>I'm a <b>Senior Product Designer specialized in Design Systems</b>, helping organizations create scalable digital experiences by connecting <b>Product, Design and Engineering</b>.</p>
        <p data-reveal>With 10+ years across web, mobile and SaaS platforms, my work combines UX design, design system strategy, stakeholder collaboration and design operations — ensuring consistency across products while accelerating delivery for designers and developers alike.</p>
        <p data-reveal>Based between <b>Las Palmas de Gran Canaria and Madrid</b>, currently at <b>BASF Digital Solutions</b>.</p>
        <div class="about-ctas" data-reveal>
          <a href="{PROFILE['cal']}" target="_blank" rel="noopener" class="btn"><span>Book a call</span>{ARROW}</a>
          <a href="{PROFILE['resume']}" target="_blank" rel="noopener" class="btn btn--ghost"><span>Download resume</span>{ARROW}</a>
          <a href="mailto:{PROFILE['mailto']}" class="btn btn--ghost"><span>{PROFILE['email_display']}</span>{ARROW}</a>
        </div>
      </div>
    </div>
  </section>

  <section style="padding-top:0;">
    <div class="container">
      <div class="sect-head">
        <div>
          <span class="mono">2006 — today</span>
          <h2 class="t-sect">My <span class="outline">career</span></h2>
        </div>
      </div>
      <div class="timeline">
{timeline}
      </div>
    </div>
  </section>
'''
    write("about.html", page_shell(
        "About — Javier de la Cruz | javidesignlabs",
        "Senior Product Designer specialized in Design Systems. 10+ years across SaaS, e-commerce and component libraries. Based between Las Palmas and Madrid.",
        root, body, active="about.html", bg_word="JAVI", path="about.html", jsonld=person_jsonld()
    ))


# ----------------------------------------------------------------
# 404
# ----------------------------------------------------------------
def build_404():
    body = f'''
  <section class="err">
    <div class="hero-grid-bg" aria-hidden="true"></div>
    <div class="container">
      <span class="mono">Error 404</span>
      <h1 class="t-hero">Off the <span class="outline">grid</span></h1>
      <p>This page is outside my design grid. Let's get you back on track.</p>
      <a href="index.html" class="btn"><span>Back to homepage</span>{ARROW}</a>
    </div>
  </section>
'''
    write("404.html", page_shell(
        "404 — javidesignlabs", "Page not found.",
        "", body, bg_word="404"
    ))


# ----------------------------------------------------------------
# PROJECT DETAIL
# ----------------------------------------------------------------
def build_project(p, next_p):
    root = "../"
    problem_li = "\n".join(f"<li>{li}</li>" for li in p["problem"])
    resp_li = "\n".join(f"<li>{li}</li>" for li in p["responsibilities"])
    research = "\n".join(f"<p><b>{t}.</b> {d}</p>" for t, d in p["research"])
    design = "\n".join(f"<p><b>{t}.</b> {d}</p>" for t, d in p["design_blocks"])
    impact = "\n".join(f'<div class="impact-cell" data-reveal><b>{t}</b><p>{d}</p></div>' for t, d in p["impact"])
    qual = ""
    if p["qualitative"]:
        qli = "\n".join(f"<li>{li}</li>" for li in p["qualitative"])
        qual = f'<div class="pblock" data-reveal><span class="mono">Qualitative impact</span><ul>{qli}</ul></div>'
    learn_li = "\n".join(f"<li>{li}</li>" for li in p["learnings"])
    intro = "\n".join(f"<p>{t}</p>" for t in p["intro"])

    website_btn = ""
    if p["website"]:
        website_btn = f'<a href="{p["website"]}" target="_blank" rel="noopener" class="btn"><span>Visit website</span>{ARROW}</a>'

    body = f'''
  <section class="page-hero" style="padding-bottom:0;">
    <div class="container">
      <span class="mono">{YEARS[p["slug"]]} · {p["tag"]} · {p["company"]}</span>
      <h1 class="t-giant">{p["title"]}</h1>
      <p class="lede" data-reveal>{p["subtitle"]}</p>
      <div class="proj-cover" data-reveal>
        <img src="{p["cover_img"]}" alt="{p["title"]}">
      </div>
    </div>
  </section>

  <section>
    <div class="container proj-body">
      <aside class="proj-rail">
        <div class="rail-field"><span class="mono">My role</span><span>{p["role"]}</span></div>
        <div class="rail-field"><span class="mono">Category</span><span>{p["category"]}</span></div>
        <div class="rail-field"><span class="mono">Company</span><span>{p["company"]}</span></div>
        <div class="rail-field"><span class="mono">Timeline</span><span>{YEARS[p["slug"]]}</span></div>
        {website_btn}
      </aside>
      <div class="proj-content">
        <div class="pblock" data-reveal>
          <span class="mono">Overview</span>
          {intro}
        </div>
        <div class="pblock" data-reveal>
          <span class="mono">Context</span>
          <p>{p["context"]}</p>
        </div>
        <div class="pblock" data-reveal>
          <span class="mono">Problem</span>
          <ul>{problem_li}</ul>
        </div>
        <div class="pblock" data-reveal>
          <span class="mono">Objective</span>
          <p>{p["objective"]}</p>
        </div>
        <div class="pblock" data-reveal>
          <span class="mono">Responsibilities</span>
          <ul>{resp_li}</ul>
        </div>
        <div class="pblock" data-reveal>
          <span class="mono">Research</span>
          {research}
        </div>
        <div class="pblock" data-reveal>
          <span class="mono">Design &amp; implementation</span>
          {design}
        </div>
        <div class="pblock" data-reveal>
          <span class="mono">Impact</span>
          <div class="impact-grid">
{impact}
          </div>
        </div>
        {qual}
        <div class="pblock" data-reveal>
          <span class="mono">Key learnings</span>
          <ul>{learn_li}</ul>
        </div>
      </div>
    </div>
  </section>

  <section class="next-proj" style="padding-bottom:0;">
    <div class="container">
      <a href="{root}projects/{next_p["slug"]}.html">
        <span class="mono">Next case study →</span>
        <h2 class="t-sect">{next_p["title"]}</h2>
      </a>
    </div>
  </section>
'''
    write(f'projects/{p["slug"]}.html', page_shell(
        f'{p["title"]} — javidesignlabs',
        p["subtitle"],
        root, body, bg_word="CASE", path=f'projects/{p["slug"]}.html', jsonld=project_jsonld(p)
    ))




# ----------------------------------------------------------------
# SEO: JSON-LD, sitemap, robots
# ----------------------------------------------------------------
import json as _json

def person_jsonld():
    base = PROFILE["base_url"].rstrip("/")
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Javier de la Cruz",
        "alternateName": "Javi de la Cruz",
        "jobTitle": "Senior Product Designer",
        "url": base + "/",
        "image": PROFILE["avatar_about"],
        "email": "mailto:" + PROFILE["mailto"],
        "sameAs": [PROFILE["linkedin"], PROFILE["x"]],
        "worksFor": {"@type": "Organization", "name": "BASF Digital Solutions"},
        "address": [
            {"@type": "PostalAddress", "addressLocality": "Las Palmas de Gran Canaria", "addressCountry": "ES"},
            {"@type": "PostalAddress", "addressLocality": "Madrid", "addressCountry": "ES"},
        ],
        "knowsAbout": ["Design Systems", "Component Libraries", "Design Tokens", "DesignOps", "Product Design", "UX/UI Design", "SaaS", "Figma", "User Research"],
    }
    return '<script type="application/ld+json">' + _json.dumps(data, ensure_ascii=False) + "</script>"


def project_jsonld(p):
    base = PROFILE["base_url"].rstrip("/")
    data = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": p["title"],
        "description": p["subtitle"],
        "url": f'{base}/projects/{p["slug"]}.html',
        "image": p["cover_img"],
        "author": {"@type": "Person", "name": "Javier de la Cruz", "url": base + "/"},
        "about": p["category"],
    }
    return '<script type="application/ld+json">' + _json.dumps(data, ensure_ascii=False) + "</script>"


def build_seo_files():
    base = PROFILE["base_url"].rstrip("/")
    urls = ["", "projects.html", "about.html", "privacy.html"] + [f'projects/{p["slug"]}.html' for p in PROJECTS]
    entries = "\n".join(
        f"  <url><loc>{base}/{u}</loc></url>" for u in urls
    )
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n'
    write("sitemap.xml", sitemap)
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n"
    write("robots.txt", robots)


def build_privacy():
    body = f'''
  <section class="page-hero" style="padding-bottom:0;">
    <div class="container">
      <span class="mono">Legal</span>
      <h1 class="t-giant">Privacy</h1>
      <p class="lede" data-reveal>The short version: this site doesn't track you.</p>
    </div>
  </section>
  <section>
    <div class="container proj-body">
      <aside class="proj-rail">
        <div class="rail-field"><span class="mono">Site owner</span><span>Javier de la Cruz</span></div>
        <div class="rail-field"><span class="mono">Contact</span><span>{PROFILE['email_display']}</span></div>
        <div class="rail-field"><span class="mono">Location</span><span>Las Palmas / Madrid, Spain</span></div>
      </aside>
      <div class="proj-content">
        <div class="pblock">
          <span class="mono">Cookies</span>
          <p>This website does not set any cookies — no analytics cookies, no tracking cookies, no advertising cookies, and no technical cookies. That is why you don't see a cookie banner: there is nothing to consent to.</p>
        </div>
        <div class="pblock">
          <span class="mono">Analytics &amp; tracking</span>
          <p>No analytics or tracking tools of any kind are used. Your visit is not recorded, profiled, or shared with third parties by this site.</p>
        </div>
        <div class="pblock">
          <span class="mono">Fonts</span>
          <p>All fonts are self-hosted on this site. No requests are made to Google Fonts or any other third-party font service, so your IP address is never shared with a font provider.</p>
        </div>
        <div class="pblock">
          <span class="mono">Third-party content</span>
          <p>Project images and photos on this site are served from Framer's content delivery network (framerusercontent.com). When your browser loads those images, it makes a standard HTTP request to that CDN, which — like any web request — includes your IP address. No other data is transmitted.</p>
          <p>External links (LinkedIn, X, Cal.com, Dropbox, client websites) take you to third-party sites governed by their own privacy policies.</p>
        </div>
        <div class="pblock">
          <span class="mono">Hosting</span>
          <p>This site is hosted on GitHub Pages. GitHub may collect technical information such as IP addresses in its server logs for security purposes, as described in <b>GitHub's privacy statement</b>.</p>
        </div>
        <div class="pblock">
          <span class="mono">Contact</span>
          <p>If you email me or book a call, I will use your contact details only to reply to you. Questions about this policy: {PROFILE['email_display']}.</p>
        </div>
      </div>
    </div>
  </section>
'''
    write("privacy.html", page_shell(
        "Privacy — javidesignlabs",
        "This site sets no cookies and uses no tracking. Fonts are self-hosted; here's exactly what happens when you visit.",
        "", body, bg_word="LEGAL", path="privacy.html"
    ))


# ----------------------------------------------------------------
def favicon():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0B0B09"/><circle cx="16" cy="16" r="6" fill="#C8FF4D"/></svg>'''
    write("assets/img/favicon.svg", svg)


if __name__ == "__main__":
    build_home()
    build_projects()
    build_about()
    build_404()
    for i, p in enumerate(PROJECTS):
        build_project(p, PROJECTS[(i + 1) % len(PROJECTS)])
    favicon()
    build_privacy()
    build_seo_files()
    print("Done — 15 pages + sitemap.xml + robots.txt generated.")
