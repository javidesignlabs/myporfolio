# -*- coding: utf-8 -*-
"""Reusable HTML fragment builders."""

from data import NAV, PROFILE

ARROW_ICON = '<svg viewBox="0 0 16 16" fill="none"><path d="M4 12 12 4M12 4H5M12 4v7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_ICON_INK = ARROW_ICON.replace('currentColor', 'var(--ink)')
PLUS_ICON = '<svg viewBox="0 0 16 16" fill="none"><path d="M8 3v10M3 8h10" stroke="var(--ink)" stroke-width="1.6" stroke-linecap="round"/></svg>'
UP_ICON = '<svg viewBox="0 0 16 16" fill="none"><path d="M8 12V4M4 7l4-4 4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
LOGO_SVG = '''<svg viewBox="0 0 30 30" fill="none"><path d="M6 22V8l5 4v10c0 3-2 5-5 5" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/><path d="M15 4v6M21 6l-3 4M27 9l-5 3" stroke="var(--lime-dim)" stroke-width="2.4" stroke-linecap="round"/></svg>'''

AVATAR_SVG = '''<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="64" height="64" rx="32" fill="#15150F"/>
<circle cx="32" cy="25" r="11" fill="#B6FF3D"/>
<path d="M12 56c2-12 10-18 20-18s18 6 20 18" fill="#B6FF3D" opacity=".85"/>
</svg>'''


def asset(root, path):
    return f"{root}assets/{path}"


def header(root="", active=""):
    nav_links = "\n".join(
        f'        <a href="{root}{href}"{" class=\"active\"" if href == active else ""}>{label}</a>'
        for label, href in NAV
    )
    mobile_links = "\n".join(
        f'      <a href="{root}{href}">{label}</a>' for label, href in NAV
    )
    return f'''  <header class="site-header">
    <div class="container">
      <a href="{root}index.html" class="brand">{LOGO_SVG}<span>designlabs</span></a>
      <nav class="main-nav" aria-label="Primary">
{nav_links}
      </nav>
      <div class="header-right">
        <span class="header-email">Email: <b>hello@javidesignlabs.com</b></span>
        <a href="{root}about.html" class="btn btn-dark">Contact me<span class="btn-ico">{ARROW_ICON.replace("currentColor","var(--ink)")}</span></a>
        <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false"><span></span></button>
      </div>
    </div>
    <nav class="mobile-nav" aria-label="Mobile">
{mobile_links}
      <a href="{root}about.html">Contact me</a>
    </nav>
  </header>'''


def marquee(items, light=False, reverse=False):
    cls = "marquee light" if light else "marquee"
    if reverse:
        cls += " reverse"
    spans = "".join(f"<span>{t}</span>" for t in items)
    return f'''  <div class="{cls}">
    <div class="marquee-track">{spans}{spans}</div>
  </div>'''


MARQUEE_ITEMS = [
    '<b>User-Centered</b> Design',
    '<b>Data-Driven</b> Design Decisions',
    '<b>Figma</b> &amp; Prototyping Expert',
    '<b>SaaS</b> Platform UX',
]


def footer(root=""):
    return f'''  <footer class="site-footer">
    <div class="footer-top">
      <div class="container">
        <a href="#top" class="back-to-top">Back to top <span class="circle">{UP_ICON}</span></a>
      </div>
    </div>
    {marquee(MARQUEE_ITEMS)}
    <div class="footer-cta">
      <div class="container">
        <div>
          <h2>Let's work<br>together</h2>
          <p class="sub">Let's make an impact</p>
        </div>
        <div class="footer-right">
          <div class="footer-person">
            <img src="{PROFILE['avatar_footer']}" alt="Javier de la C.">
            <div>
              <b>Javier de la C.</b>
              <span>Product Designer</span>
              <a class="li" href="{PROFILE['linkedin']}" target="_blank" rel="noopener" aria-label="LinkedIn">in</a>
            </div>
          </div>
          <div class="footer-contact">
            <span class="eyebrow">Contact me</span>
            <p class="email">{PROFILE['email_display']}</p>
            <a href="{PROFILE['cal']}" target="_blank" rel="noopener" class="btn">Book a call<span class="btn-ico">{ARROW_ICON_INK}</span></a>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <span>&copy; <span id="year"></span> Javi de la Cruz — designlabs</span>
        <a href="{root}404.html">404</a>
      </div>
    </div>
  </footer>
  <script>document.getElementById('year').textContent = new Date().getFullYear();</script>'''


def _svg_data_uri(svg):
    import urllib.parse
    return urllib.parse.quote(svg)


def page_shell(title, description, root, body, active="", extra_head=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
{extra_head}
</head>
<body id="top">
{header(root, active)}
{body}
{footer(root)}
<script src="{root}assets/js/main.js"></script>
</body>
</html>'''
