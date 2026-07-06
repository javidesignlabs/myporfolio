# -*- coding: utf-8 -*-
"""Shared HTML fragment builders — v2 design."""

from data import NAV, PROFILE

ARROW = '<svg viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12 12 2M12 2H4M12 2v8"/></svg>'
PLUS = '<svg viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M7 2v10M2 7h10"/></svg>'


def header(root="", active=""):
    nav_links = "\n".join(
        f'        <a href="{root}{href}">{label}</a>'
        for label, href in NAV
    )
    mobile_links = "\n".join(
        f'      <a href="{root}{href}"><span>{label}</span><span class="mono">0{i+1}</span></a>'
        for i, (label, href) in enumerate(NAV)
    )
    return f'''  <header class="site-header">
    <div class="container">
      <a href="{root}index.html" class="brand"><i></i>javidesignlabs</a>
      <nav class="main-nav" aria-label="Primary">
{nav_links}
      </nav>
      <a href="{PROFILE['cal']}" target="_blank" rel="noopener" class="btn"><span>Book a call</span>{ARROW}</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false"><span></span></button>
    </div>
  </header>
  <nav class="mobile-nav" aria-label="Mobile">
      <a href="{root}index.html"><span>Home</span><span class="mono">00</span></a>
{mobile_links}
      <a href="{PROFILE['cal']}" target="_blank" rel="noopener"><span>Book a call</span><span class="mono">↗</span></a>
      <a href="mailto:{PROFILE['mailto']}"><span>Say hello</span><span class="mono">→</span></a>
  </nav>
  <a class="fab-call" href="{PROFILE['cal']}" target="_blank" rel="noopener">Book a call {ARROW}</a>'''


def footer(root="", bg_word="JAVI"):
    return f'''  <footer class="site-footer">
    <span class="big-bg-word" aria-hidden="true">{bg_word}</span>
    <div class="container footer-cta fit-bound">
      <span class="mono">Available for new projects — Las Palmas ↔ Madrid</span>
      <h2 class="t-hero"><a href="mailto:{PROFILE['mailto']}"><span class="fit" data-max="200">Let's work</span><br><span class="fit outline" data-max="200">together</span></a></h2>
      <a class="footer-email" href="mailto:{PROFILE['mailto']}">{PROFILE['email_display']}</a>
    </div>
    <div class="container footer-meta">
      <div class="footer-person">
        <img src="{PROFILE['avatar_footer']}" alt="Javier de la Cruz">
        <div>
          <b>Javier de la C.</b>
          <small>Senior Product Designer</small>
        </div>
      </div>
      <div class="footer-links">
        <a href="{PROFILE['linkedin']}" target="_blank" rel="noopener">LinkedIn</a>
        <a href="{PROFILE['x']}" target="_blank" rel="noopener">X</a>
        <a href="{PROFILE['cal']}" target="_blank" rel="noopener">Book a call</a>
        <a href="{PROFILE['resume']}" target="_blank" rel="noopener">Resume</a>
      </div>
      <a href="#top" class="to-top">Back to top ↑</a>
    </div>
    <div class="container footer-meta" style="border-top:none;padding-top:0;">
      <span class="mono">© <span id="year"></span> Javi de la Cruz — javidesignlabs</span>
      <a class="mono" href="{root}privacy.html" style="color:var(--smoke);">Privacy</a>
    </div>
  </footer>'''


def page_shell(title, description, root, body, active="", bg_word="JAVI", path="", jsonld=""):
    base = PROFILE["base_url"].rstrip("/")
    canonical = f"{base}/{path}" if path else f"{base}/"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self'; img-src 'self' data: https://framerusercontent.com; connect-src 'self'; base-uri 'self'; form-action 'none'; object-src 'none'">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://framerusercontent.com/assets/uS6WF7ZvN6a9RVXQZqkFvQBQIRs.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="{root}assets/fonts/syne-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/instrument-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/style.css">
{jsonld}
</head>
<body id="top">
{header(root, active)}
<main>
{body}
</main>
{footer(root, bg_word)}
<script src="{root}assets/js/main.js"></script>
</body>
</html>'''
