#!/usr/bin/env python3
"""Render two HTML files to PDF with headless Chrome/Chromium and compare them.

Usage:
    python3 render_compare.py ORIGINAL.html EDITED.html [--out DIR] [--chrome PATH]

Reports page counts and, when a text extractor is available (pdftotext,
pdfplumber or pypdf), the first page on which the text differs, plus a
per-page line-count delta to show where edited text grew or shrank.
Rendering uses the document's own @page / @media print CSS, without browser
headers or footers.
"""
import argparse
import difflib
import os
import re
import shutil
import subprocess
import sys
import tempfile

CANDIDATES = [
    os.environ.get("CHROME_PATH", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge",
]


def find_chrome(explicit):
    for c in [explicit] + CANDIDATES:
        if not c:
            continue
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
        found = shutil.which(c)
        if found:
            return found
    sys.exit("No Chrome/Chromium found. Pass --chrome PATH or set CHROME_PATH.")


def render(chrome, html_path, pdf_path, profile):
    url = "file://" + os.path.abspath(html_path)
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           "--user-data-dir=" + profile, "--print-to-pdf=" + pdf_path, url]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    if not os.path.exists(pdf_path):
        sys.exit("Rendering failed for " + html_path)


def page_count(pdf_path):
    data = open(pdf_path, "rb").read()
    return len(re.findall(rb"/Type\s*/Page(?!s)", data))


def pages_text(pdf_path):
    if shutil.which("pdftotext"):
        out = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True).stdout
        return out.split("\f")
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            return [p.extract_text() or "" for p in pdf.pages]
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
        return [p.extract_text() or "" for p in PdfReader(pdf_path).pages]
    except ImportError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original")
    ap.add_argument("edited")
    ap.add_argument("--out", help="directory to keep the PDFs (default: temporary)")
    ap.add_argument("--chrome")
    args = ap.parse_args()

    chrome = find_chrome(args.chrome)
    out = args.out or tempfile.mkdtemp(prefix="render_compare_")
    os.makedirs(out, exist_ok=True)
    profile = tempfile.mkdtemp(prefix="chrome_profile_")
    pdfs = []
    for label, path in (("original", args.original), ("edited", args.edited)):
        pdf = os.path.join(out, label + ".pdf")
        render(chrome, path, pdf, profile)
        pdfs.append(pdf)

    a_pages, b_pages = page_count(pdfs[0]), page_count(pdfs[1])
    print(f"PDFs: {pdfs[0]}  {pdfs[1]}")
    print(f"pages: original {a_pages}, edited {b_pages}" + ("" if a_pages == b_pages else "  <-- PAGE COUNT CHANGED"))

    a_text, b_text = pages_text(pdfs[0]), pages_text(pdfs[1])
    if a_text is None or b_text is None:
        print("text comparison skipped: install poppler (pdftotext), pdfplumber or pypdf")
        return
    for i in range(max(len(a_text), len(b_text))):
        a = a_text[i] if i < len(a_text) else ""
        b = b_text[i] if i < len(b_text) else ""
        if a == b:
            continue
        la, lb = len(a.splitlines()), len(b.splitlines())
        ratio = difflib.SequenceMatcher(None, a, b).ratio()
        print(f"page {i + 1}: lines {la} -> {lb} ({lb - la:+d}), text similarity {ratio:.2f}")


if __name__ == "__main__":
    main()
