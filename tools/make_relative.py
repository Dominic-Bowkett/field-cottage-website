#!/usr/bin/env python3
"""Convert root-absolute internal paths (/assets, /about.html, /) to relative
paths so the site works both under a GitHub project subpath and at a custom
domain root. Leaves absolute https:// URLs (canonical/og/sitemap) untouched.
"""
import re, glob, os

def convert(text, prefix):
    # attribute values: href="/..." and src="/..."
    text = re.sub(r'(\b(?:href|src)=")/', r'\1' + prefix, text)
    # CSS url('/...') / url("/...") / url(/...)
    text = re.sub(r'(url\(["\']?)/', r'\1' + prefix, text)
    return text

root_files = [f for f in glob.glob("*.html")]
blog_files = [f for f in glob.glob("blog/*.html")]

for f in root_files:
    s = open(f, encoding="utf-8").read()
    open(f, "w", encoding="utf-8").write(convert(s, "./"))
    print("root  ->", f)

for f in blog_files:
    s = open(f, encoding="utf-8").read()
    open(f, "w", encoding="utf-8").write(convert(s, "../"))
    print("blog  ->", f)

print("done")
