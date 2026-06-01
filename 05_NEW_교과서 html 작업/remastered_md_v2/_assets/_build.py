#!/usr/bin/env python3
"""Assemble a body fragment (.body.html) into the canonical template.

Usage: _build.py <body_file> [out_file]
Body file format:
  <!--META
  title: <document title>
  -->
  <aside class="toc">...</aside>
  <main class="deck">... <section class="card" id="sN">...</section> ...</main>
"""
import sys, os, re

ASSETS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(ASSETS)
TEMPLATE = os.path.join(ASSETS, "_template.html")


def main():
    if len(sys.argv) < 2:
        print("usage: _build.py <body_file> [out_file]"); sys.exit(2)
    body_path = sys.argv[1]
    raw = open(body_path, encoding="utf-8").read()
    title = ""
    m = re.search(r'<!--META(.*?)-->', raw, re.S)
    if m:
        tm = re.search(r'(?mi)^\s*title:\s*(.+?)\s*$', m.group(1))
        if tm:
            title = tm.group(1).strip()
        body = raw[m.end():].strip()
    else:
        body = raw.strip()
    if not title:
        title = re.sub(r'\.body\.html$', '', os.path.basename(body_path))
    total = len(re.findall(r'<section\b[^>]*class="[^"]*\bcard\b', body))
    counter = "01 / %02d" % (total if total else 1)
    tpl = open(TEMPLATE, encoding="utf-8").read()
    out = (tpl.replace("{{TITLE}}", title)
              .replace("{{COUNTER}}", counter)
              .replace("{{BODY}}", body))
    if len(sys.argv) >= 3:
        out_path = sys.argv[2]
    else:
        base = re.sub(r'\.body\.html$', '', os.path.basename(body_path))
        out_path = os.path.join(ROOT, base + "_카드뉴스.html")
    open(out_path, "w", encoding="utf-8").write(out)
    print("BUILT %s  (cards=%d)" % (out_path, total))


main()
