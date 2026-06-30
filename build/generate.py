# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from data import PROJECTS, CAREER, FEEDBACK, PROCESS_STEPS, PROFILE
from templates import page_shell, marquee, MARQUEE_ITEMS, ARROW_ICON, ARROW_ICON_INK, PLUS_ICON, AVATAR_SVG, _svg_data_uri
import illustrations as ill

OUT = os.path.join(os.path.dirname(__file__), "..")

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def avatar_uri():
    return PROFILE["avatar_hero"]

def svg_uri(svg):
    return f"data:image/svg+xml;utf8,{_svg_data_uri(svg)}"

# ---------------------------------------------------------------
# Project card (used in grids)
# ---------------------------------------------------------------
def project_card(p, root):
    return f'''<a class="project-card" href="{root}projects/{p["slug"]}.html">
  <div class="thumb"><img src="{p["cover_img"]}" alt="{p["title"]}"></div>
  <div class="body">
    <span class="tag">[ {p["tag"]} ]</span>
    <h3>{p["title"]}</h3>
    <div class="meta"><span>{p["role"]}</span><span class="arrow">{ARROW_ICON}</span></div>
  </div>
</a>'''

def other_projects_block(current_slug, root, n=3):
    others = [p for p in PROJECTS if p["slug"] != current_slug][:n]
    cards = "\n".join(project_card(p, root) for p in others)
    return f'''  <section class="other-projects dark">
    <div class="container">
      <span class="eyebrow">Latest projects</span>
      <div class="section-head"><h2>Some of my other stuff</h2></div>
      <div class="other-grid">
{cards}
      </div>
    </div>
  </section>'''

# ---------------------------------------------------------------
# HOME
# ---------------------------------------------------------------
def build_home():
    root = ""
    featured = PROJECTS[:4]
    cards = "\n".join(project_card(p, root) for p in featured[:3])
    process = "\n".join(
        f'''<div class="process-item">
  <span class="label">{name}</span>
  <span class="num">/{num}</span>
  <p>{text}</p>
</div>''' for name, num, text in PROCESS_STEPS
    )
    feedback = "\n".join(f'<div class="feedback-card">&ldquo;{t}&rdquo;</div>' for t in FEEDBACK)

    body = f'''
  <section class="hero">
    <div class="hero-bg"></div>
    <div class="container hero-inner">
      <div class="hero-card">
        <img src="{avatar_uri()}" alt="Javier de la Cruz">
        <div class="who"><b>Javier de la Cruz</b><span>Product Designer</span></div>
      </div>
      <h1>Hi! I'm <span class="tag">Javier de la Cruz</span> a Product Designer based between Las Palmas &amp; Madrid crafting intuitive and user-centric digital experiences</h1>
      <a href="projects.html" class="btn">Explore What I've Built<span class="btn-ico">{ARROW_ICON_INK}</span></a>
      <img class="hero-visual" src="{PROFILE['hero_graphic']}" alt="">
    </div>
  </section>

  {marquee(['<b>2023 - Act.</b> | Product Designer Inari.io', '<b>2021 - 2023</b> | Product Designer Bolttech'])}

  <section class="dark">
    <div class="container">
      <span class="eyebrow">About my work</span>
      <div class="section-head">
        <h2>I transform complex data into intuitive experiences</h2>
      </div>
      <a href="about.html" class="btn" style="margin-bottom:52px;display:inline-flex;">Chat with Me<span class="btn-ico">{ARROW_ICON_INK}</span></a>
      <div class="project-grid">
{cards}
        <div class="cta-card">
          <a href="projects.html" class="btn">View all projects<span class="btn-ico">{ARROW_ICON_INK}</span></a>
        </div>
      </div>
    </div>
  </section>

  {marquee(['<b>User-Centered</b> Design', '<b>Crafting Seamless</b> Experiences'], light=True)}

  <section>
    <div class="container">
      <div class="section-head"><h2>How is my design process</h2></div>
      <div class="process-list">
{process}
      </div>
    </div>
  </section>

  <section class="dark" style="padding-top:0;">
    <div class="container">
      <div class="feedback-grid">
{feedback}
      </div>
    </div>
  </section>
'''
    html = page_shell(
        "Javier de la Cruz — Product Designer | designlabs",
        "Product Designer based between Las Palmas & Madrid, crafting intuitive and user-centric digital experiences.",
        root, body, active="index.html"
    )
    write("index.html", html)

# ---------------------------------------------------------------
# PROJECTS LISTING
# ---------------------------------------------------------------
def build_projects():
    root = ""
    cards = "\n".join(project_card(p, root) for p in PROJECTS)
    body = f'''
  <section style="padding-top:56px;">
    <div class="container">
      <span class="eyebrow">My work / projects</span>
      <div class="section-head"><h2>Selected work</h2></div>
      <div class="project-grid">
{cards}
      </div>
    </div>
  </section>
'''
    html = page_shell(
        "Projects — designlabs",
        "Selected case studies: design systems, SaaS platforms, e-commerce and TV app experiences.",
        root, body, active="projects.html"
    )
    write("projects.html", html)

# ---------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------
def build_about():
    root = ""
    timeline = "\n".join(
        f'''<div class="timeline-item">
  <div class="timeline-row">
    <span class="when">{when}</span>
    <span class="what">{what}</span>
    <span class="plus">{PLUS_ICON}</span>
  </div>
  <div class="timeline-panel"><p>{desc}</p></div>
</div>''' for when, what, desc in CAREER
    )
    body = f'''
  <section class="about-hero">
    <div class="container">
      <h1 style="margin-bottom:48px;">About me</h1>
    </div>
    <div class="container two-col">
      <div class="about-card">
        <img src="{PROFILE['avatar_about']}" alt="Javier de la Cruz">
        <a class="x" href="{PROFILE['x']}" target="_blank" rel="noopener">𝕏</a>
        <a class="mail" href="mailto:{PROFILE['mailto']}">{PROFILE['email_display']}</a>
        <p>I'm Javi, a passionate product designer with a love for creating visually stunning and user-friendly digital experiences.</p>
        <a href="{PROFILE['cal']}" target="_blank" rel="noopener" class="btn">Book a call<span class="btn-ico">{ARROW_ICON_INK}</span></a>
      </div>
      <div class="about-copy">
        <p>With over 10 years of experience designing digital products, I specialize in web, mobile, and SaaS platforms.</p>
        <p>My 360&deg; approach covers information architecture, design systems, usability, and interface optimization for B2B and B2C environments. I excel in cross-functional collaboration, bringing a proactive mindset and a strong commitment to innovation in agile settings.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="career">
        <span class="eyebrow">About me</span>
        <h2>My Career</h2>
        <a href="{PROFILE['resume']}" target="_blank" rel="noopener" class="btn">Download my resume<span class="btn-ico">{ARROW_ICON_INK}</span></a>
      </div>
      <div class="timeline">
{timeline}
      </div>
    </div>
  </section>
'''
    html = page_shell(
        "About me — Javier de la Cruz | designlabs",
        "Product designer with 10+ years of experience across SaaS, e-commerce and design systems.",
        root, body, active="about.html"
    )
    write("about.html", html)

# ---------------------------------------------------------------
# 404
# ---------------------------------------------------------------
def build_404():
    root = ""
    body = f'''
  <section class="error-hero">
    <div class="container">
      {ill.HERO_404}
      <h2>Page not found</h2>
      <p>Sorry, this page is out of my design grid</p>
      <a href="index.html" class="btn">Back to homepage<span class="btn-ico">{ARROW_ICON_INK}</span></a>
    </div>
  </section>
'''
    html = page_shell(
        "404 — Page not found | designlabs",
        "This page is out of my design grid.",
        root, body
    )
    write("404.html", html)

# ---------------------------------------------------------------
# PROJECT DETAIL PAGES
# ---------------------------------------------------------------
def build_project(p):
    root = "../"
    cover = f'<img src="{p["cover_img"]}" alt="{p["title"]}">'

    intro = "".join(f'<p>{t}</p>' for t in p["intro"])
    intro = intro.replace("</p><p>", "</p>\n          <p>")

    problem_li = "\n".join(f"<li>{li}</li>" for li in p["problem"])
    resp_li = "\n".join(f"<li>{li}</li>" for li in p["responsibilities"])

    research_blocks = "\n".join(
        f"<p><b>{title}.</b> {desc}</p>" for title, desc in p["research"]
    )
    design_blocks = "\n".join(
        f"<p><b>{title}.</b> {desc}</p>" for title, desc in p["design_blocks"]
    )

    impact_cards = "\n".join(
        f'<div class="impact-card"><b>{title}</b><p>{desc}</p></div>' for title, desc in p["impact"]
    )
    qualitative = ""
    if p["qualitative"]:
        qli = "\n".join(f"<li>{li}</li>" for li in p["qualitative"])
        qualitative = f'<div class="proj-block"><h3>Qualitative impact</h3><ul>{qli}</ul></div>'

    learnings_li = "\n".join(f"<li>{li}</li>" for li in p["learnings"])

    website_btn = ""
    if p["website"]:
        website_btn = f'<a href="{p["website"]}" target="_blank" rel="noopener" class="btn" style="margin-top:6px;">Visit website<span class="btn-ico">{ARROW_ICON_INK}</span></a>'

    body = f'''
  <section class="proj-hero">
    <div class="container">
      <h1>{p["title"]}</h1>
      <p class="kicker">{p["subtitle"]}</p>
    </div>
  </section>

  <section style="padding-top:0;">
    <div class="container proj-layout">
      <aside class="proj-meta">
        <div class="field"><label>My role</label><span>{p["role"]}</span></div>
        <div class="field"><label>Category</label><span>{p["category"]}</span></div>
        <div class="field"><label>Company</label><span>{p["company"]}</span></div>
        {website_btn}
      </aside>
      <div>
        <div class="proj-cover">{cover}</div>

        <div class="proj-block">
          {intro}
        </div>

        <div class="proj-block">
          <h3>Context</h3>
          <p>{p["context"]}</p>
        </div>

        <div class="proj-block">
          <h3>Problem</h3>
          <ul>{problem_li}</ul>
        </div>

        <div class="proj-block">
          <h3>Objective</h3>
          <p>{p["objective"]}</p>
        </div>

        <div class="proj-block">
          <h3>Responsibilities</h3>
          <ul>{resp_li}</ul>
        </div>

        <div class="proj-block">
          <h3>Research</h3>
          {research_blocks}
        </div>

        <div class="proj-block">
          <h3>Design &amp; implementation</h3>
          {design_blocks}
        </div>

        <div class="proj-block">
          <h3>Impact</h3>
          <div class="impact-grid">{impact_cards}</div>
        </div>

        {qualitative}

        <div class="proj-block">
          <h3>Key learnings</h3>
          <ul>{learnings_li}</ul>
        </div>
      </div>
    </div>
  </section>

{other_projects_block(p["slug"], root)}
'''
    html = page_shell(
        f'{p["title"]} — designlabs',
        p["subtitle"],
        root, body
    )
    write(f"projects/{p['slug']}.html", html)

# ---------------------------------------------------------------
def copy_static():
    import shutil
    write("assets/img/favicon.svg", ill.FAVICON)

if __name__ == "__main__":
    build_home()
    build_projects()
    build_about()
    build_404()
    for p in PROJECTS:
        build_project(p)
    copy_static()
    print("Done.")
