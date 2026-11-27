#!/usr/bin/env python3
"""Compare an original and an edited document for content that editing must not change.

Usage:
    python3 invariance_check.py ORIGINAL EDITED [--format html|md|text] [--json]

Checks (stdlib only):
  numbers        every number token in the visible text (multiset)
  code spans     inline code: <code>…</code> in HTML, `…` in Markdown
  code blocks    <pre>…</pre> in HTML, fenced ``` blocks in Markdown (verbatim)
  formulas       math blocks: $$…$$ / $…$ in Markdown; elements with class
                 "formula"/"math"/"katex" in HTML (digits and operators only;
                 explanatory words may change)
  headings       count of headings per level
  tables         number of tables and rows per table
  html tags      tag counts (HTML only)
  scripts        <script> blocks verbatim (HTML only)

Exit code 0 if no differences, 1 if differences were found. Every reported
difference must be explained by an intended edit; otherwise revert it.
"""
import argparse
import collections
import html as htmllib
import json
import re
import sys

NUM = re.compile(r"(?<![\w.])[-+−]?\d+(?:[.,  ]\d{3})*(?:[.,]\d+)?%?")
# Digits and operators only: punctuation from explanatory words inside a
# formula block (parentheses, commas, underscores of identifiers) is ignored.
SYMBOLS = re.compile(r"[\d=<>≤≥≈±×÷∑Σ∫√∞∈∀∃⌊⌋⌈⌉+\-−*/^\[\]{}|]")


def detect_format(path, text):
    p = path.lower()
    if p.endswith((".html", ".htm")):
        return "html"
    if p.endswith((".md", ".markdown")):
        return "md"
    if re.search(r"<(html|body|div|p|table)\b", text, re.I):
        return "html"
    return "text"


def strip_tags(s):
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return htmllib.unescape(s)


def counter(items):
    return collections.Counter(i.strip() for i in items if i.strip())


def analyse(text, fmt):
    r = {}
    if fmt == "html":
        visible = strip_tags(text)
        r["code spans"] = counter(htmllib.unescape(x) for x in re.findall(r"<code\b[^>]*>(.*?)</code>", text, re.S | re.I))
        r["code blocks"] = counter(re.findall(r"<pre\b[^>]*>.*?</pre>", text, re.S | re.I))
        formulas = re.findall(r"<(\w+)\b[^>]*class=\"[^\"]*\b(?:formula|math|katex)\b[^\"]*\"[^>]*>(.*?)</\1>", text, re.S | re.I)
        r["formulas"] = counter("".join(SYMBOLS.findall(strip_tags(f[1]))) for f in formulas)
        r["headings"] = counter(m.lower() for m in re.findall(r"<(h[1-6])\b", text, re.I))
        tables = re.findall(r"<table\b.*?</table>", text, re.S | re.I)
        row = re.compile(r"<tr\b", re.I)
        r["tables"] = counter("table %d: %d rows" % (i + 1, len(row.findall(t))) for i, t in enumerate(tables))
        r["html tags"] = counter(t.lower() for t in re.findall(r"<([a-zA-Z][a-zA-Z0-9]*)", text))
        r["scripts"] = counter(re.findall(r"<script\b.*?</script>", text, re.S | re.I))
    elif fmt == "md":
        blocks = re.findall(r"```.*?```", text, re.S)
        rest = re.sub(r"```.*?```", " ", text, flags=re.S)
        r["code blocks"] = counter(blocks)
        r["code spans"] = counter(re.findall(r"`([^`\n]+)`", rest))
        math = re.findall(r"\$\$(.+?)\$\$", rest, re.S) + re.findall(r"(?<!\$)\$([^$\n]+)\$(?!\$)", rest)
        r["formulas"] = counter("".join(SYMBOLS.findall(m)) for m in math)
        r["headings"] = counter("h%d" % len(m) for m in re.findall(r"^(#{1,6})\s", rest, re.M))
        tables, current = [], 0
        for line in rest.splitlines():
            if line.strip().startswith("|"):
                current += 1
            elif current:
                tables.append(current)
                current = 0
        if current:
            tables.append(current)
        r["tables"] = counter(f"table {i + 1}: {n} rows" for i, n in enumerate(tables))
        visible = rest
    else:
        visible = text
    r["numbers"] = counter(NUM.findall(visible))
    return r


def diff(a, b):
    out = {}
    for key in a:
        removed, added = a[key] - b[key], b[key] - a[key]
        if removed or added:
            out[key] = {"removed": dict(removed), "added": dict(added)}
    return out


def short(s, n=160):
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= n else s[: n - 1] + "…"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original")
    ap.add_argument("edited")
    ap.add_argument("--format", choices=["html", "md", "text"])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    a_text = open(args.original, encoding="utf-8").read()
    b_text = open(args.edited, encoding="utf-8").read()
    fmt = args.format or detect_format(args.original, a_text)
    d = diff(analyse(a_text, fmt), analyse(b_text, fmt))
    if args.json:
        print(json.dumps({"format": fmt, "differences": d}, ensure_ascii=False, indent=2))
    else:
        print(f"format: {fmt}")
        if not d:
            print("OK: no differences in numbers, code, formulas, headings or tables.")
        for key, v in d.items():
            print(f"\n[{key}]")
            for label in ("removed", "added"):
                for item, count in v[label].items():
                    print(f"  {label:7} x{count}: {short(item)}")
    sys.exit(1 if d else 0)


if __name__ == "__main__":
    main()
