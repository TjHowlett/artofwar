"""Copies the four aow-*.json files into index.html so the page works as one standalone file.

Run this from anywhere after you change any aow-*.json file:

    python embed-data.py

It only replaces the four <script type="application/json" ...> blocks in index.html.
Nothing else in the page is touched.
"""
import json
import re
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
page = here / "index.html"

blocks = {
    "data-points": "aow-points.json",
    "data-themes": "aow-themes.json",
    "data-links": "aow-links.json",
    "data-sources": "aow-sources.json",
}

html = page.read_text(encoding="utf-8")

for block_id, filename in blocks.items():
    data = json.loads((here / filename).read_text(encoding="utf-8"))
    # Compact, and "<" written as < so nothing in the data can close the script tag early.
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    pattern = re.compile(
        r'(<script type="application/json" id="' + block_id + r'">)(.*?)(</script>)', re.DOTALL
    )
    if not pattern.search(html):
        sys.exit("Could not find the " + block_id + " block in index.html")
    html = pattern.sub(lambda m: m.group(1) + text + m.group(3), html, count=1)
    print(f"{block_id}: {len(data)} items from {filename}")

page.write_text(html, encoding="utf-8", newline="\n")
print(f"index.html is now {page.stat().st_size / 1024:.0f} KB")
