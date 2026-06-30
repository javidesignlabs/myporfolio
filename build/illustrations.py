# -*- coding: utf-8 -*-
"""Abstract, brand-colored SVG illustrations standing in for project screenshots."""

INK = "#0C0C09"
CREAM = "#F3F1EA"
LIME = "#B6FF3D"
LIME_D = "#8FE01A"
WHITE = "#FFFFFF"
LINE = "#DEDBD1"

PALETTES = {
    "warehouse":     {"bg": "#1B1C16", "a": "#FF8A3D", "b": LIME, "c": "#2B2C22"},
    "design-system": {"bg": CREAM,     "a": "#7FD1D9", "b": "#2C2E63", "c": "#F4E25A"},
    "portal":        {"bg": "#171816", "a": "#FF7A33", "b": LIME, "c": "#2A2B25"},
    "gluecharm":     {"bg": "#10131C", "a": "#5B7BFF", "b": LIME, "c": "#1B2030"},
    "payment":       {"bg": "#1A1418", "a": "#E1485B", "b": LIME, "c": "#2A1F23"},
    "landing":       {"bg": "#0E0F12", "a": "#E1485B", "b": LIME, "c": "#1E2024"},
    "tv":             {"bg": "#101113", "a": "#E1485B", "b": LIME, "c": "#202225"},
    "email":         {"bg": "#15161B", "a": "#E1485B", "b": LIME, "c": "#23252C"},
    "product-card":  {"bg": "#F4EDE7", "a": "#E59FAE", "b": INK, "c": "#D8CFC4"},
    "map":           {"bg": "#EFEAE0", "a": "#E15C8C", "b": INK, "c": LIME},
}


def _wrap(inner, vb="0 0 800 500", bg=CREAM):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice"><rect width="100%" height="100%" fill="{bg}"/>{inner}</svg>'


def warehouse(p):
    bars = "".join(
        f'<rect x="{60+i*70}" y="{260-((i%4)*30)}" width="46" height="{220+((i%4)*30)}" rx="6" fill="{p["c"]}" stroke="{p["b"]}" stroke-opacity=".25"/>'
        for i in range(9)
    )
    boxes = "".join(
        f'<rect x="{72+i*70}" y="{300-((i%3)*40)}" width="22" height="22" rx="3" fill="{p["a"]}"/>'
        for i in range(9)
    )
    return _wrap(f'{bars}{boxes}<rect x="520" y="120" width="220" height="140" rx="16" fill="{INK}"/><rect x="540" y="150" width="120" height="14" rx="7" fill="{p["b"]}"/><rect x="540" y="174" width="160" height="10" rx="5" fill="#3a3b32"/><rect x="540" y="196" width="160" height="10" rx="5" fill="#3a3b32"/>', bg=p["bg"])


def design_system(p):
    swatches = "".join(
        f'<rect x="{60+ (i%4)*110}" y="{60+(i//4)*70}" width="86" height="50" rx="10" fill="{[p["a"],p["b"],p["c"],"#fff"][i%4]}" stroke="{LINE}"/>'
        for i in range(8)
    )
    return _wrap(f'{swatches}<rect x="500" y="80" width="240" height="320" rx="20" fill="{WHITE}" stroke="{LINE}"/><rect x="524" y="116" width="120" height="16" rx="8" fill="{p["b"]}"/><rect x="524" y="150" width="190" height="10" rx="5" fill="{LINE}"/><rect x="524" y="170" width="190" height="10" rx="5" fill="{LINE}"/><rect x="524" y="210" width="190" height="44" rx="22" fill="{p["a"]}"/>', bg=p["bg"])


def portal(p):
    cards = "".join(
        f'<rect x="{90+i*40}" y="{70+i*36}" width="420" height="260" rx="18" fill="{p["c"]}" stroke="{p["b"]}" stroke-opacity=".3" opacity="{1 - i*0.18}"/>'
        for i in range(3)
    )
    return _wrap(f'{cards}<rect x="210" y="200" width="280" height="16" rx="8" fill="{p["b"]}"/><rect x="210" y="232" width="200" height="10" rx="5" fill="#555"/><rect x="210" y="252" width="160" height="36" rx="18" fill="{p["a"]}"/>', bg=p["bg"])


def gluecharm(p):
    nodes = [(120,110),(320,80),(520,150),(380,280),(180,300),(620,300)]
    lines = "".join(f'<line x1="{nodes[0][0]}" y1="{nodes[0][1]}" x2="{x}" y2="{y}" stroke="{p["b"]}" stroke-width="2" opacity=".5"/>' for x,y in nodes[1:])
    circles = "".join(f'<circle cx="{x}" cy="{y}" r="{26 if i==0 else 18}" fill="{p["a"] if i%2 else p["b"]}"/>' for i,(x,y) in enumerate(nodes))
    return _wrap(f'{lines}{circles}', bg=p["bg"])


def payment(p):
    return _wrap(f'''<rect x="120" y="90" width="320" height="200" rx="20" fill="{p["c"]}" stroke="{p["b"]}" stroke-opacity=".3"/>
<rect x="148" y="130" width="80" height="56" rx="10" fill="{p["a"]}"/>
<rect x="148" y="206" width="240" height="10" rx="5" fill="#555"/>
<rect x="148" y="226" width="160" height="10" rx="5" fill="#3c3c3c"/>
<circle cx="560" cy="200" r="110" fill="none" stroke="{p["b"]}" stroke-width="3" stroke-dasharray="10 10"/>
<path d="M510 200l36 36 70-80" fill="none" stroke="{p["b"]}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>''', bg=p["bg"])


def landing(p):
    return _wrap(f'''<rect x="90" y="70" width="380" height="240" rx="16" fill="{p["c"]}"/>
<rect x="90" y="70" width="380" height="34" rx="16" fill="{INK}"/>
<circle cx="112" cy="87" r="5" fill="{p["a"]}"/><circle cx="128" cy="87" r="5" fill="{p["b"]}"/><circle cx="144" cy="87" r="5" fill="#666"/>
<rect x="118" y="140" width="220" height="20" rx="6" fill="{WHITE}"/>
<rect x="118" y="172" width="160" height="10" rx="5" fill="#777"/>
<rect x="118" y="220" width="120" height="36" rx="18" fill="{p["a"]}"/>
<rect x="500" y="120" width="220" height="320" rx="28" fill="{INK}"/>
<rect x="520" y="150" width="180" height="100" rx="12" fill="{p["c"]}"/>
<rect x="520" y="266" width="180" height="14" rx="7" fill="{p["b"]}"/>
<rect x="520" y="292" width="120" height="10" rx="5" fill="#666"/>''', bg=p["bg"])


def tv(p):
    tiles = "".join(
        f'<rect x="{200+(i%3)*150}" y="{170+(i//3)*100}" width="130" height="80" rx="10" fill="{p["c"]}"/>'
        for i in range(6)
    )
    return _wrap(f'<rect x="160" y="90" width="480" height="320" rx="20" fill="{INK}" stroke="{p["a"]}" stroke-opacity=".4"/>{tiles}<circle cx="400" cy="130" r="6" fill="{p["b"]}"/>', bg=p["bg"])


def email(p):
    return _wrap(f'''<rect x="140" y="120" width="520" height="260" rx="18" fill="{p["c"]}"/>
<path d="M140 138l260 170 260-170" fill="none" stroke="{p["a"]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="600" cy="150" r="34" fill="{p["b"]}"/>
<path d="M586 150l10 10 18-20" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>''', bg=p["bg"])


def product_card(p):
    return _wrap(f'''<rect x="120" y="70" width="220" height="290" rx="18" fill="{WHITE}" stroke="{LINE}"/>
<path d="M150 110l80-26 80 26v60l-80 26-80-26z" fill="{p["a"]}"/>
<circle cx="170" cy="270" r="10" fill="#E1485B"/><circle cx="196" cy="270" r="10" fill="{INK}"/><circle cx="222" cy="270" r="10" fill="#3C7A5A"/>
<rect x="150" y="300" width="160" height="10" rx="5" fill="{LINE}"/>
<rect x="150" y="320" width="100" height="28" rx="14" fill="{p["b"]}"/>
<rect x="420" y="100" width="260" height="260" rx="20" fill="{p["c"]}"/>
<path d="M460 140l90-20 90 20v100l-90 20-90-20z" fill="{WHITE}" opacity=".8"/>''', bg=p["bg"])


def store_map(p):
    grid = "".join(f'<line x1="{60+i*68}" y1="60" x2="{60+i*68}" y2="380" stroke="#cfc6b4" stroke-width="1"/>' for i in range(11))
    grid += "".join(f'<line x1="60" y1="{60+i*40}" x2="740" y2="{60+i*40}" stroke="#cfc6b4" stroke-width="1"/>' for i in range(9))
    pins = [(220,160),(360,220),(500,140),(440,300),(610,250)]
    pin_shapes = "".join(
        f'<path d="M{x} {y-30}c16 0 28 12 28 28 0 20-28 46-28 46s-28-26-28-46c0-16 12-28 28-28z" fill="{p["a"] if i%2 else p["b"]}"/><circle cx="{x}" cy="{y-2}" r="9" fill="{WHITE}"/>'
        for i,(x,y) in enumerate(pins)
    )
    return _wrap(f'{grid}{pin_shapes}', bg=p["bg"])


_FUNCS = {
    "warehouse": warehouse,
    "design-system": design_system,
    "portal": portal,
    "gluecharm": gluecharm,
    "payment": payment,
    "landing": landing,
    "tv": tv,
    "email": email,
    "product-card": product_card,
    "map": store_map,
}


def illustration(kind):
    p = PALETTES[kind]
    return _FUNCS[kind](p)


HERO_404 = _wrap('''<circle cx="400" cy="250" r="190" fill="none" stroke="#DEDBD1" stroke-width="2" stroke-dasharray="6 10"/>
<text x="400" y="280" font-family="Plus Jakarta Sans, sans-serif" font-size="120" font-weight="700" fill="#0C0C09" text-anchor="middle">404</text>''', bg=CREAM)

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 30"><rect width="30" height="30" rx="7" fill="#0C0C09"/><path d="M8 22V10l4 3v9c0 2.4-1.6 4-4 4" stroke="#B6FF3D" stroke-width="2.2" stroke-linecap="round" fill="none"/></svg>'''
