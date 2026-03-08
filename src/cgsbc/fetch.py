"""Download the pre-built CGSBC catalog from openastra.org."""

from __future__ import annotations

import argparse
import json

import requests

CGSBC_CATALOG_URL = "https://openastra.org/cgsbc/catalog/v0.1/latest.json"


def main(args: argparse.Namespace) -> None:
    print(f"Fetching catalog from {CGSBC_CATALOG_URL} ...")
    r = requests.get(CGSBC_CATALOG_URL, timeout=30)
    r.raise_for_status()
    data = r.json()
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {data.get('count', '?')} controls to {args.out}")
