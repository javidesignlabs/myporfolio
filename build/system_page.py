"""The site documents its own design system.

Most of Javi's design-system work is under NDA; this page is the part that can
be shown. It is rendered from the same tokens and component classes as every
other page — nothing here is a picture of a component.
"""
from data import PROJECTS, PROOF

COLORS = [
    ("--void", "Page background"),
    ("--void-2", "Raised background"),
    ("--panel", "Panels and hover fills"),
    ("--cream", "Primary text"),
    ("--cream-dim", "Secondary text"),
    ("--smoke", "Labels and metadata"),
    ("--lime", "Accent: actions, figures, emphasis"),
    ("--lime-deep", "Accent for small marks"),
    ("--line", "Hairlines"),
    ("--line-hard", "Borders on controls"),
]

TYPE = [
    ("Display · hero", "Syne 800 · fitted to the line width", "sys-hero", "Design that ships"),
    ("Display · section", "Syne 800 · clamp(1.5rem, 4.6vw, 4.2rem)", "t-sect",
     'Case <span class="outline">studies</span>'),
    ("Heading · row", "Syne 700 · clamp(1.15rem, 2.6vw, 2rem)", "sys-h3", "One portal, many markets"),
    ("Body", "Instrument Sans 400 · 1rem / 1.6", "sys-body",
     "Scope is a design decision, so I make it deliberately and early."),
    ("Label", "Space Mono 400 · .72rem · tracked .14em · uppercase", "mono", "Selected work · 2013 — today"),
]

EASES = [("--ease-out", "cubic-bezier(.16,1,.3,1)"), ("--ease-snap", "cubic-bezier(.6,0,.2,1)")]

# Every rule below is something the code actually does — keep it that way.
RULES = [
    ("Tokens first",
     "Every text, surface and border colour on the site resolves to a custom property. The light theme is those values swapped; no component has a light-mode rule of its own."),
    ("Headlines never break a word",
     "Display type is sized per column so a long word fits from 375px up, instead of being hyphenated or clipped."),
    ("Motion is optional",
     "Reveals, the cursor and the screen reel all stand down under prefers-reduced-motion."),
    ("Nothing tracks before consent",
     "Fonts are self-hosted and analytics is injected only after an explicit accept."),
    ("No framework in the browser",
     "Plain HTML, one stylesheet and two small scripts, generated from a single content file."),
]


def system_body(arrow, work_rows):
    swatches = "\n".join(f'''<div class="token" data-token="{name}">
  <span class="token-chip" style="background:var({name})"></span>
  <span class="token-name mono">{name}</span>
  <span class="token-val mono" data-token-val></span>
  <span class="token-use">{use}</span>
</div>''' for name, use in COLORS)

    type_rows = "\n".join(f'''<div class="spec-row">
  <div class="spec-meta"><span class="mono">{label}</span><span class="mono dim">{meta}</span></div>
  <div class="spec-sample {cls}">{sample}</div>
</div>''' for label, meta, cls, sample in TYPE)

    eases = "\n".join(f'''<div class="ease" tabindex="0">
  <span class="mono">{name}</span><span class="mono dim">{val}</span>
  <span class="ease-track"><i style="transition-timing-function:{val}"></i></span>
</div>''' for name, val in EASES)

    rules = "\n".join(f'<li data-reveal><b>{t}</b><span>{d}</span></li>' for t, d in RULES)

    sample = PROJECTS[0]
    n, unit, what, src, how, slug = PROOF[0]

    return f'''
  <section class="page-hero" style="padding-bottom:0;">
    <div class="container">
      <span class="mono">Design system · this site</span>
      <h1 class="t-giant">The system <span class="accent">behind</span> this site</h1>
      <p class="lede" data-reveal>Most of my design-system work sits behind an NDA. This one does not: the site you are reading is built on its own small system, and this page is rendered from the same tokens and components as every other page.</p>
      <div class="theme-demo" data-reveal>
        <div>
          <span class="mono">Try it</span>
          <p>Switch the theme. The colour tokens change; no component is restyled.</p>
        </div>
        <button type="button" class="btn" data-theme-toggle><span data-theme-label>Switch to light</span>{arrow}</button>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="sect-head"><div><span class="mono">01 · Tokens</span><h2 class="t-sect">Colour</h2></div>
        <p class="sys-note">Values are read live from the page, so they follow the theme.</p></div>
      <div class="token-grid">
{swatches}
      </div>
    </div>
  </section>

  <section class="caps">
    <div class="container">
      <div class="sect-head"><div><span class="mono">02 · Tokens</span><h2 class="t-sect">Type</h2></div>
        <p class="sys-note">Three families, each with one job: display, reading, data.</p></div>
      <div class="spec-list">
{type_rows}
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="sect-head"><div><span class="mono">03 · Tokens</span><h2 class="t-sect">Motion</h2></div>
        <p class="sys-note">Two curves. Hover or focus a row to play it.</p></div>
      <div class="ease-list">
{eases}
      </div>
    </div>
  </section>

  <section class="caps">
    <div class="container">
      <div class="sect-head"><div><span class="mono">04 · Components</span><h2 class="t-sect">Built from the <span class="outline">tokens</span></h2></div>
        <p class="sys-note">These are the live components, not pictures of them.</p></div>
      <div class="comp-grid">
        <div class="comp"><span class="mono">Button · primary and ghost</span>
          <div class="comp-stage"><a href="projects.html" class="btn"><span>Explore the work</span>{arrow}</a>
          <a href="about.html" class="btn btn--ghost"><span>About</span>{arrow}</a></div></div>
        <div class="comp"><span class="mono">Metric cell</span>
          <div class="comp-stage"><a class="proof-cell" href="projects/{slug}.html"><div class="num">{n}<small>{unit}</small></div><p class="what">{what}</p><p class="how">{how}</p><span class="mono src">{src} <i>Read the case →</i></span></a></div></div>
        <div class="comp comp--wide"><span class="mono">Work row</span>
          <div class="comp-stage"><div class="work-list" style="width:100%">
{work_rows([sample], "")}
          </div></div></div>
        <div class="comp"><span class="mono">Impact cell</span>
          <div class="comp-stage"><div class="impact-cell" style="border:1px solid var(--line)"><b>{sample["impact"][0][0]}</b><p>{sample["impact"][0][1]}</p></div></div></div>
        <div class="comp"><span class="mono">Label, accent and outline</span>
          <div class="comp-stage comp-stage--col"><span class="mono">Measured, not claimed</span>
          <span class="sys-h3">Complex in, <span class="accent">clear</span> <span class="outline">out</span></span></div></div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="sect-head"><div><span class="mono">05 · Rules</span><h2 class="t-sect">What the system <span class="outline">enforces</span></h2></div></div>
      <ul class="rule-list">
{rules}
      </ul>
    </div>
  </section>
'''
