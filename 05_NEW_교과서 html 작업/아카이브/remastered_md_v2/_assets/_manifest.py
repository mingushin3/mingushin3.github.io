#!/usr/bin/env python3
"""Print a compact coverage manifest for a source md (headings + citations + eq count).
Usage: _manifest.py <source.md>"""
import sys, os, re

md = sys.argv[1]
t = open(md, encoding="utf-8").read()
heads = re.findall(r'(?m)^(#{1,4})\s+(.+?)\s*$', t)
cites = re.findall(r'\[[^\]\n]*(?:R&T|G&W|p\.|pp\.|Fig|Eq|§|확인 필요|교과서 외)[^\]\n]*\]', t)
dd = re.findall(r'\$\$.*?\$\$', t, re.S)
print("# MANIFEST", os.path.basename(md))
print("lines=%d  headings=%d  display_eq=%d  citation_brackets=%d" %
      (t.count(chr(10)) + 1, len(heads), len(dd), len(cites)))
print("\n## Heading outline (every one MUST be represented in the deck):")
for lvl, h in heads:
    print("  " * (len(lvl) - 1) + lvl + " " + h)
print("\n## Distinct citations (preserve as <span class=\"cite\">):")
for c in sorted(set(cites)):
    print("  - " + c)
