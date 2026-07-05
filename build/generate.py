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
          <span class="mono">Product Designer</span>
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
      <h1 class="t-hero">
        <span class="hero-line"><span>Design that</span></span>
        <span class="hero-line"><span class="row"><span class="outline">ships</span> &amp;</span></span>
        <span class="hero-line"><span><span class="accent">performs</span></span></span>
      </h1>
      <div class="hero-sub">
        <p data-reveal>I'm Javi — I turn complex data and messy workflows into intuitive digital products. 10+ years across SaaS, e-commerce, design systems and TV apps.</p>
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
        <p data-reveal>My 360º approach covers information architecture, design systems, usability and interface optimization for B2B and B2C environments.</p>
        <p data-reveal>I work embedded with engineering — Figma to production, tokens to components — bringing a proactive mindset to agile teams.</p>
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
    write("index.html", page_shell(
        "Javier de la Cruz — Product Designer | javidesignlabs",
        "Product Designer based between Las Palmas & Madrid. 10+ years turning complex data into intuitive digital products across SaaS, e-commerce and design systems.",
        root, body, active="index.html", bg_word="JAVI"
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
        root, body, active="projects.html", bg_word="WORK"
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
        <p data-reveal>I'm a <b>product designer</b> with over 10 years of experience designing digital products — specialized in <b>web, mobile and SaaS platforms</b>.</p>
        <p data-reveal>My 360º approach covers information architecture, design systems, usability, and interface optimization for B2B and B2C environments. I excel in cross-functional collaboration, bringing a proactive mindset and a strong commitment to innovation in agile settings.</p>
        <p data-reveal>Based between <b>Las Palmas de Gran Canaria and Madrid</b>, currently designing at BASF.</p>
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
        "Product designer with 10+ years across SaaS, e-commerce and design systems. Based between Las Palmas and Madrid.",
        root, body, active="about.html", bg_word="JAVI"
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
        root, body, bg_word="CASE"
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
    print("Done — 14 pages generated.")
