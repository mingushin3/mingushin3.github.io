#!/usr/bin/env python3
"""Verify a generated card-news HTML. Usage: _verify.py <out.html> [source.md]
Exits 1 if any hard ERROR, else 0. Prints info/warn/err report."""
import sys, os, re

ASSETS = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(ASSETS, "_template.html")


def style_of(html):
    m = re.search(r'<style>.*?</style>', html, re.S)
    return m.group(0) if m else ""


def math_spans(html):
    return re.findall(r'\\\((.*?)\\\)', html, re.S) + re.findall(r'\\\[(.*?)\\\]', html, re.S)


def section_tags(html):
    return re.findall(r'<section\b([^>]*)>', html)


def main():
    out = sys.argv[1]
    md = sys.argv[2] if len(sys.argv) > 2 else None
    html = open(out, encoding="utf-8").read()
    E = []; W = []; I = []

    body_only = re.sub(r'<head>.*?</head>', ' ', html, flags=re.S)
    body_noscript = re.sub(r'<script.*?</script>', ' ', body_only, flags=re.S)

    # ---- 6: template fidelity ----
    for n in ['tex-chtml.js', 'window.MathJax', 'Newsreader', 'Noto+Serif+KR',
              'JetBrains+Mono', 'pretendard', 'id="MathJax-script"',
              'IntersectionObserver', 'class="burger"']:
        if n not in html:
            E.append("TEMPLATE missing: %s" % n)
    if style_of(open(TEMPLATE, encoding="utf-8").read()) != style_of(html):
        E.append("TEMPLATE: <style> differs from canonical")

    # ---- 2: math ----
    if html.count(r'\(') != html.count(r'\)'):
        E.append(r"MATH: \( %d != \) %d" % (html.count(r'\('), html.count(r'\)')))
    if html.count(r'\[') != html.count(r'\]'):
        E.append(r"MATH: \[ %d != \] %d" % (html.count(r'\['), html.count(r'\]')))
    # strip code/pre regions: MathJax skips them (default skipHtmlTags), so '$' there
    # is legitimate (e.g. NONMEM $DES/$ERROR control records), not unconverted math
    body_nocode = re.sub(r'<pre.*?</pre>', ' ', body_noscript, flags=re.S)
    body_nocode = re.sub(r'<code.*?</code>', ' ', body_nocode, flags=re.S)
    d = body_nocode.count('$')
    if d:
        E.append("MATH: %d stray '$' (unconverted?)" % d)
    badlt = 0; badamp = 0
    for s in math_spans(html):
        badlt += s.count('<') + s.count('>')
        badamp += len(re.findall(r'&(?!(?:amp|lt|gt|nbsp|#\d+|[a-zA-Z]{2,6});)', s))
    if badlt:
        E.append("MATH: %d raw <,> inside math (need &lt; &gt;)" % badlt)
    if badamp:
        W.append("MATH: %d possibly-bare & inside math" % badamp)

    # ---- 3 & 4 & 9: TOC / card ids / count ----
    ids = set(); ncards = 0
    for attrs in section_tags(html):
        clm = re.search(r'class="([^"]+)"', attrs)
        if clm and 'card' in clm.group(1):
            ncards += 1
            idm = re.search(r'id="([^"]+)"', attrs)
            if idm:
                ids.add(idm.group(1))
    hrefs = re.findall(r'class="toc-link"\s+href="#([^"]+)"', html)
    dead = [h for h in hrefs if h not in ids]
    orph = [i for i in ids if i not in set(hrefs)]
    if dead:
        E.append("TOC: dead links: %s" % dead[:10])
    if orph:
        W.append("TOC: cards not in TOC: %s" % orph[:10])
    if ncards > 40:
        E.append("CARDS: %d > 40" % ncards)
    elif ncards > 38:
        W.append("CARDS: %d (near cap 40)" % ncards)
    cm = re.search(r'id="counter">01 / (\d+)<', html)
    if cm and int(cm.group(1)) != ncards:
        W.append("COUNTER %s != cards %d" % (cm.group(1), ncards))
    I.append("cards=%d  toclinks=%d" % (ncards, len(hrefs)))

    # ---- 1: raw markdown (outside code/pre/math) ----
    t = body_noscript
    t = re.sub(r'<pre.*?</pre>', ' ', t, flags=re.S)
    t = re.sub(r'<code.*?</code>', ' ', t, flags=re.S)
    t = re.sub(r'<div class="codeblock".*?</div>', ' ', t, flags=re.S)
    t = re.sub(r'<div class="flow".*?</div>', ' ', t, flags=re.S)
    t = re.sub(r'\\\(.*?\\\)', ' ', t, flags=re.S)
    t = re.sub(r'\\\[.*?\\\]', ' ', t, flags=re.S)
    if '**' in t:
        E.append("RAWMD: '**' present (%d)" % t.count('**'))
    if '](' in t:
        E.append("RAWMD: '](' link present")
    if re.search(r'(?m)^\s*#{2,6}\s', t):
        E.append("RAWMD: line-leading '##' heading")
    if re.search(r'(?m)^\s*\|.*\|\s*$', t):
        E.append("RAWMD: pipe-table row present")
    if re.search(r'(?m)^\s*>\s\S', t):
        W.append("RAWMD: blockquote-like '> ' line")
    if '`' in t:
        W.append("RAWMD: backtick present (%d)" % t.count('`'))

    # ---- 5: dark-scope text colors ----
    ALLOW = ['#fff', '#ffffff', 'white', 'var(--cream', 'var(--amber', 'var(--coral-l',
             'var(--coral)', 'var(--tan', 'var(--teal-l', '#eab45c', '#ec9a78',
             '#f4efe6', '#d6cfbf', 'inherit']
    BAD = ['#000', 'black', 'gray', 'grey', 'var(--ink', 'var(--coral-d',
           '#211', '#1f', '#26', '#2f', '#56', '#8a']
    bad_cols = []
    for sec in re.findall(r'<section\b[^>]*class="[^"]*\bdark\b[^"]*"[^>]*>(.*?)</section>', html, re.S):
        for st in re.findall(r'style="([^"]*)"', sec):
            for cmatch in re.findall(r'color\s*:\s*([^;]+)', st):
                v = cmatch.strip().lower()
                if any(b in v for b in BAD) and not any(a in v for a in ALLOW):
                    bad_cols.append(v)
    if bad_cols:
        E.append("DARKCOLOR: dark text in dark scope: %s" % bad_cols[:8])

    # ---- 7 & 8: coverage vs source ----
    if md and os.path.exists(md):
        src = open(md, encoding="utf-8").read()
        # exclude QA checklist / references appendix from coverage+citation counts (meta, not reproduced as cards)
        cut = re.search(r'(?m)^#{1,4}\s.*(검증 체크리스트|통과표|출처 표기|부록\s*[—\-]\s*출처)', src)
        if cut:
            src = src[:cut.start()]
        src_c = re.findall(r'\[[^\]\n]*(?:R&T|G&W|p\.|pp\.|Fig|Eq|§|확인 필요|교과서 외)[^\]\n]*\]', src)
        out_c = len(re.findall(r'class="cite"', html)) + len(re.findall(r'class="flag"', html))
        I.append("citations src~%d  out(.cite+.flag)=%d" % (len(src_c), out_c))
        if src_c and out_c < 0.3 * len(src_c):
            W.append("CITES: out %d < 30%% of src %d" % (out_c, len(src_c)))
        src_dd = len(re.findall(r'\$\$.*?\$\$', src, re.S))
        out_mb = len(re.findall(r'class="mathblock', html))
        I.append("displaymath src=%d  out mathblocks=%d" % (src_dd, out_mb))
        otext = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html))
        miss = []
        for lvl, h in re.findall(r'(?m)^(#{2,4})\s+(.+?)\s*$', src):
            core = re.sub(r'[#*`]', '', re.sub(r'^[\d\.\-\s§A-Za-z]*[\.\s]', '', h)).strip()
            toks = [x for x in re.findall(r'[가-힣A-Za-z0-9]+', core) if len(x) >= 3]
            if not toks:
                continue
            longest = max(toks, key=len)
            if len(longest) >= 4 and longest not in otext:
                miss.append(core[:24])
        if miss:
            W.append("COVERAGE: %d headings core-token absent: %s" % (len(miss), miss[:12]))

    print("=== VERIFY", os.path.basename(out), "===")
    for x in I: print("  i :", x)
    for x in W: print("  W :", x)
    for x in E: print("  E :", x)
    print("RESULT:", "FAIL" if E else "PASS", "(%dE %dW)" % (len(E), len(W)))
    sys.exit(1 if E else 0)


main()
