#!/usr/bin/env python3
"""
Generate llms.md and llms-full.md from algorithms.json.

These files follow the llms.md convention (llmstxt.org) for agent-friendly
access to site content in markdown format.

Usage:
    python scripts/generate_llms_txt.py
    python scripts/generate_llms_txt.py --json data/algorithms.json --out-dir public
"""

import argparse
import json
import sys
from pathlib import Path


def load_algorithms(json_path: Path) -> list[dict]:
    with open(json_path) as f:
        return json.load(f)


def generate_llms_txt(algos: list[dict], base_url: str) -> str:
    """Generate the brief llms.md with site overview."""
    categories = sorted(set(a["category"] for a in algos))
    lines = [
        "# H90 Lens",
        "",
        "> Quick reference for Eventide H90 harmonizer pedal algorithms.",
        "> Data sourced from H90 Manual v1.12.5.",
        "",
        "## Overview",
        "",
        f"This site catalogs all {len(algos)} algorithms across {len(categories)} categories",
        "from the Eventide H90 multi-effects pedal. Each algorithm includes parameter",
        "names, descriptions, value ranges, and performance parameters.",
        "",
        "## Categories",
        "",
    ]
    for cat in categories:
        count = sum(1 for a in algos if a["category"] == cat)
        lines.append(f"- {cat} ({count})")
    lines += [
        "",
        "## Links",
        "",
        f"- [Full algorithm data (Markdown)]({base_url}llms-full.md)",
        f"- [Algorithm data (JSON)]({base_url}data/algorithms.json)",
        f"- [Web interface]({base_url})",
        "- [Eventide H90 Manual](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/algorithms/index.html)",
        "",
    ]
    return "\n".join(lines)


def generate_llms_full_txt(algos: list[dict]) -> str:
    """Generate the full llms-full.md with all algorithm details."""
    lines = [
        "# H90 Lens — Full Algorithm Reference",
        "",
        "> Eventide H90 Harmonizer — All algorithms with complete parameter details.",
        "> Data sourced from H90 Manual v1.12.5.",
        "",
    ]

    # Group by category
    categories = {}
    for algo in algos:
        categories.setdefault(algo["category"], []).append(algo)

    for cat_name in sorted(categories):
        cat_algos = categories[cat_name]
        lines.append(f"## {cat_name}")
        lines.append("")

        for algo in sorted(cat_algos, key=lambda a: a["name"]):
            lines.append(f"### {algo['name']}")
            lines.append("")

            if algo.get("overview"):
                lines.append(algo["overview"])
                lines.append("")

            # Parameters
            params = algo.get("parameters", [])
            if params:
                lines.append("#### Parameters")
                lines.append("")
                for p in params:
                    name = p["name"]
                    desc = p.get("fullDescription") or p.get("description") or ""
                    range_val = p.get("range")
                    range_str = f" `{range_val}`" if range_val else ""
                    lines.append(f"- **{name}**{range_str}: {desc}")
                lines.append("")

            # Performance parameters
            perf_params = algo.get("performanceParams", [])
            if perf_params:
                lines.append("#### Performance Parameters")
                lines.append("")
                for pp in perf_params:
                    name = pp["name"] if isinstance(pp, dict) else pp
                    desc = pp.get("description", "") if isinstance(pp, dict) else ""
                    if desc:
                        lines.append(f"- **{name}**: {desc}")
                    else:
                        lines.append(f"- **{name}**")
                lines.append("")

            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate llms.md files from algorithms.json")
    parser.add_argument("--json", default="data/algorithms.json", help="Input JSON path")
    parser.add_argument("--out-dir", default="public", help="Output directory")
    parser.add_argument("--base-url", default="/h90-lens/", help="Base URL for links in llms.md")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    json_path = project_root / args.json
    out_dir = project_root / args.out_dir

    if not json_path.exists():
        print(f"ERROR: {json_path} not found", file=sys.stderr)
        sys.exit(1)

    algos = load_algorithms(json_path)
    print(f"Loaded {len(algos)} algorithms from {json_path}", file=sys.stderr)

    out_dir.mkdir(parents=True, exist_ok=True)

    # Generate llms.md
    llms_txt = generate_llms_txt(algos, args.base_url)
    llms_path = out_dir / "llms.md"
    llms_path.write_text(llms_txt)
    print(f"Written {llms_path} ({len(llms_txt)} bytes)", file=sys.stderr)

    # Generate llms-full.md
    llms_full = generate_llms_full_txt(algos)
    full_path = out_dir / "llms-full.md"
    full_path.write_text(llms_full)
    print(f"Written {full_path} ({len(llms_full)} bytes)", file=sys.stderr)


if __name__ == "__main__":
    main()
