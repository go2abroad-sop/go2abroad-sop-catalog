#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GO2ABROAD SOP local catalog explorer (JSONL shards + 11-language URLs)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORDS_DIR = ROOT / "catalog" / "records"
FEATURED = ROOT / "featured_multilingual.json"
MANIFEST = ROOT / "sop_catalog_open.json"
BASE_URL = "https://sop.go2abroad.space"
LANGS = ["en", "zh", "de", "ja", "fr", "es", "pt", "it", "ko", "ar", "hi"]


def iter_records(country: str | None = None):
    if not RECORDS_DIR.exists():
        return
    files = sorted(RECORDS_DIR.glob("*.jsonl"))
    if country:
        files = [RECORDS_DIR / f"{country.upper()}.jsonl"]
    for path in files:
        if not path.exists():
            continue
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                yield json.loads(line)


def main() -> int:
    parser = argparse.ArgumentParser(description="Query GO2ABROAD SOP open catalog shards")
    parser.add_argument("--industry", help="ISIC code, e.g. 3011")
    parser.add_argument("--country", help="ISO3 country, e.g. DEU")
    parser.add_argument("--sop", help="Exact sop_id")
    parser.add_argument("--lang", default="en", choices=LANGS)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--all-langs", action="store_true")
    args = parser.parse_args()

    if not RECORDS_DIR.exists() and FEATURED.exists():
        data = json.loads(FEATURED.read_text(encoding="utf-8"))
        records = data.get("featured") or []
    else:
        records = list(iter_records(args.country))

    results = []
    for item in records:
        sop_id = item.get("sop_id") or ""
        if args.sop and sop_id != args.sop:
            continue
        if args.industry and str(item.get("industry_isic", "")) != args.industry:
            continue
        if args.country and str(item.get("country", "")).upper() != args.country.upper():
            continue
        results.append(item)
        if len(results) >= args.limit:
            break

    print(f"Found {len(results)} record(s)\n" + "-" * 72)
    for row in results:
        sop_id = row["sop_id"]
        role = row.get("role") or (row.get("roles") or {}).get(args.lang) or ""
        intro = row.get("intro") or ""
        urls = row.get("urls") or {}
        print(f"[{sop_id}] ISIC={row.get('industry_isic')} Country={row.get('country')} Track={row.get('track')}")
        if role:
            print(f"  Role:  {role}")
        if intro:
            print(f"  Intro: {intro}")
        if args.all_langs:
            for code in LANGS:
                print(f"  {code}: {urls.get(code) or f'{BASE_URL}/{code}/sop/{sop_id}.html'}")
        else:
            print(f"  URL:   {urls.get(args.lang) or f'{BASE_URL}/{args.lang}/sop/{sop_id}.html'}")
        print()
    if MANIFEST.exists():
        print(f"Manifest: {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
