"""Generates the self-hosted Open Graph share cards (1200x630 PNG).

Why this exists: the og:image used to point at an asset on Framer's CDN that
was a *template* screenshot — someone else's site showed up every time a link
was shared. Never point og:image at a CDN you don't control.

Run:  python3 ogimages.py      (needs playwright + the woff2 files in assets/fonts)
Output: assets/img/og/<slug>.png and assets/img/og/site.png
"""
import base64, os, pathlib, html as _html
from data import PROFILE, PROJECTS

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img" / "og"
FONTS = ROOT / "assets" / "fonts"

W, H = 1200, 630


def _font(name):
    b = (FONTS / name).read_bytes()
    return "data:font/woff2;base64," + base64.b64encode(b).decode()


def _shell(body, css=""):
    syne = _font("syne-latin-800-normal.woff2")
    inst = _font("instrument-sans-latin-500-normal.woff2")
    mono = _font("space-mono-latin-400-normal.woff2")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Syne;src:url({syne}) format('woff2');font-weight:800;font-display:block}}
@font-face{{font-family:Inst;src:url({inst}) format('woff2');font-weight:500;font-display:block}}
@font-face{{font-family:Mono;src:url({mono}) format('woff2');font-weight:400;font-display:block}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#0B0B09;color:#EFEDE3;
  font-family:Inst,system-ui,sans-serif;overflow:hidden;position:relative}}
.grid{{position:absolute;inset:0;
  background-image:linear-gradient(rgba(239,237,227,.045) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(239,237,227,.045) 1px,transparent 1px);
  background-size:150px 150px}}
.glow{{position:absolute;width:760px;height:760px;right:-240px;top:-300px;border-radius:50%;
  background:radial-gradient(circle,rgba(200,255,77,.17) 0%,rgba(200,255,77,0) 68%)}}
.pad{{position:relative;height:100%;padding:62px 72px;display:flex;flex-direction:column}}
.brand{{display:flex;align-items:center;gap:13px;font-family:Syne;font-weight:800;
  font-size:25px;letter-spacing:-.4px;text-transform:uppercase}}
.dot{{width:13px;height:13px;border-radius:50%;background:#C8FF4D}}
.eyebrow{{font-family:Mono;font-size:18px;letter-spacing:2.6px;color:#85847A;text-transform:uppercase}}
.rule{{height:1px;background:rgba(239,237,227,.14)}}
{css}
</style></head><body><div class="grid"></div><div class="glow"></div>{body}</body></html>"""


def site_card():
    body = f"""<div class="pad">
  <div class="brand"><span class="dot"></span>javidesignlabs</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <div class="eyebrow" style="margin-bottom:26px">Javier de la Cruz</div>
    <h1 style="font-family:Syne;font-weight:800;font-size:84px;line-height:.94;
      letter-spacing:-2.4px;text-transform:uppercase">Senior Product<br>Designer</h1>
    <div style="margin-top:30px;font-size:27px;color:#C8FF4D">Design Systems</div>
  </div>
  <div class="rule" style="margin-bottom:24px"></div>
  <div style="display:flex;justify-content:space-between;font-size:21px;color:#85847A">
    <span>Connecting product, design and engineering</span>
    <span style="font-family:Mono;font-size:18px">Las Palmas &middot; Madrid</span>
  </div>
</div>"""
    return _shell(body)


def case_card(p):
    title = _html.escape(p["title"])
    # size the headline by length so long titles still fit the card
    n = len(p["title"])
    size = 68 if n <= 34 else 58 if n <= 50 else 50 if n <= 66 else 44
    meta = " &middot; ".join(x for x in [p.get("tag"), p.get("company")] if x)
    outcome = _html.escape(p.get("outcome", ""))
    body = f"""<div class="pad">
  <div class="brand"><span class="dot"></span>javidesignlabs</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <div class="eyebrow" style="margin-bottom:26px">{meta}</div>
    <h1 style="font-family:Syne;font-weight:800;font-size:{size}px;line-height:1.02;
      letter-spacing:-1.4px;text-transform:uppercase">{title}</h1>
  </div>
  <div class="rule" style="margin-bottom:24px"></div>
  <div style="display:flex;align-items:center;gap:14px;font-size:22px;color:#C9C7BC">
    <span class="dot" style="width:9px;height:9px;flex:none"></span><span>{outcome}</span>
  </div>
</div>"""
    return _shell(body)


def main():
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [("site", site_card())] + [(p["slug"], case_card(p)) for p in PROJECTS]
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for name, markup in jobs:
            pg.set_content(markup, wait_until="load")
            pg.wait_for_timeout(180)
            pg.screenshot(path=str(OUT / f"{name}.png"))
            print(f"  og/{name}.png")
        b.close()
    print(f"Done — {len(jobs)} share cards in assets/img/og/")


if __name__ == "__main__":
    main()
