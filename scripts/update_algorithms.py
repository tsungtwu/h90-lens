#!/usr/bin/env python3
"""
H90 Lens — Algorithm Data Extractor

Fetches algorithm data from the Eventide H90 online manual and outputs
structured JSON for the H90 Lens web app.

Usage:
    python scripts/update_algorithms.py                  # writes to data/algorithms.json
    python scripts/update_algorithms.py -o output.json   # writes to custom path
    python scripts/update_algorithms.py --dry-run        # prints to stdout without writing
    python scripts/update_algorithms.py --sync-public    # also copy to public/data/

Requirements:
    pip install beautifulsoup4 requests

Data source:
    https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/algorithms/
"""

import argparse
import json
import re
import shutil
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError:
    print("Missing dependencies. Install with:\n  pip install beautifulsoup4 requests", file=sys.stderr)
    sys.exit(1)

DEFAULT_BASE_URL = "https://cdn.eventideaudio.com/manuals/h90/latest/content/algorithms/"

# SSRF prevention — only allow fetching from known Eventide domains
ALLOWED_DOMAINS = {"cdn.eventideaudio.com", "www.eventideaudio.com", "eventideaudio.com"}

# Category page slugs → display category name
CATEGORY_PAGES = {
    "delay.html": "Delay",
    "distortion.html": "Distortion",
    "eq.html": "EQ",
    "granular.html": "Granular",
    "harmonizer.html": "Harmonizer",
    "harmonizer-plus.html": "Harmonizer+",
    "looper.html": "Looper",
    "modulation.html": "Modulation",
    "multi.html": "Multi",
    "reverb.html": "Reverb",
    "synth.html": "Synth",
    "utility.html": "Utility",
}

# Known section headers that should NOT be treated as parameter names
SECTION_HEADERS = {
    "parameters", "performance", "performance parameters", "perform parameters",
    "overview", "description", "controls", "notes", "tempo sync",
    "perform parameters:", "midi",
}

# Footer / navigation text patterns to strip from descriptions
FOOTER_PATTERNS = [
    r"\s*←\s*Previous.*$",
    r"\s*Next\s*→.*$",
    r"\s*Copyright\s+©.*$",
    r"\s*Eventide\s+Audio.*$",
    r"\s*Was this article helpful\?.*$",
]

REQUEST_DELAY = 0.5  # seconds between requests to be polite


def validate_url(url: str) -> None:
    """Validate that URL points to an allowed domain."""
    parsed = urlparse(url)
    if parsed.hostname not in ALLOWED_DOMAINS:
        raise ValueError(f"URL domain '{parsed.hostname}' not in allowed list: {ALLOWED_DOMAINS}")


def fetch_page(url: str) -> BeautifulSoup:
    """Fetch a page and return parsed BeautifulSoup."""
    validate_url(url)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def clean_text(text: str) -> str:
    """Normalize whitespace in extracted text."""
    return re.sub(r"\s+", " ", text).strip()


def strip_footer_artifacts(text: str) -> str:
    """Remove footer/navigation text that may contaminate descriptions."""
    for pattern in FOOTER_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()


def strip_section_header_contamination(text: str) -> str:
    """Remove trailing section headers that bleed into parameter descriptions.

    The H90 manual sometimes has section headers (e.g. "Perform Parameters:")
    that get captured as part of the preceding parameter's description text.
    """
    # Remove trailing "Perform Parameters:" / "Performance Parameters:" / "Tempo Sync" etc.
    for header in SECTION_HEADERS:
        # Match at end of string, case-insensitive, with optional colon
        pattern = rf"\s+{re.escape(header)}:?\s*$"
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()


def extract_dd_full_text(dd: Tag) -> str:
    """Extract full description from a <dd> element, preserving inner list items.

    The manual often has option lists inside <dd>:
      <dd>Type of filter. Choices are:
        <ul><li>Lowpass</li><li>Bandpass</li><li>Highpass</li></ul>
      </dd>

    We need to capture these as: "Type of filter. Choices are: Lowpass, Bandpass, Highpass"
    """
    # Check for inner lists (<ul>, <ol>)
    inner_lists = dd.find_all(["ul", "ol"])
    if not inner_lists:
        return clean_text(dd.get_text())

    parts = []
    for child in dd.children:
        if isinstance(child, NavigableString):
            text = clean_text(str(child))
            if text:
                parts.append(text)
        elif isinstance(child, Tag):
            if child.name in ("ul", "ol"):
                # Collect list items and join with commas
                items = [clean_text(li.get_text()) for li in child.find_all("li")]
                items = [item for item in items if item]
                if items:
                    parts.append(", ".join(items))
            else:
                text = clean_text(child.get_text())
                if text:
                    parts.append(text)

    full_text = " ".join(parts)
    return clean_text(full_text)


def is_section_header(text: str) -> bool:
    """Check if text is a known section header (not a parameter name)."""
    return text.lower().rstrip(":") in SECTION_HEADERS or text.lower() in SECTION_HEADERS


def extract_algorithms_from_page(soup: BeautifulSoup, category: str) -> list[dict]:
    """
    Extract all algorithms from a category page.

    The H90 manual pages use a structure like:
    - <h2> or <h3> for algorithm names
    - Following sections contain overview text and parameter tables/lists
    - Parameters are in <dt>/<dd> pairs or table rows
    """
    algorithms = []

    # Remove footer/nav elements before extraction
    for nav in soup.find_all(["nav", "footer"]):
        nav.decompose()

    # Find algorithm sections — they're typically <h2> elements
    algo_headers = soup.find_all(["h2", "h3"], class_=lambda c: c is None or "algorithm" in str(c).lower())

    # If no headers found, try alternate selectors
    if not algo_headers:
        algo_headers = soup.select("h2, article h3")

    # Filter to only algorithm name headers (skip generic headers)
    algo_headers = [
        h for h in algo_headers
        if not is_section_header(clean_text(h.get_text()))
        and len(clean_text(h.get_text())) > 1
    ]

    for i, header in enumerate(algo_headers):
        algo_name = clean_text(header.get_text())
        if not algo_name:
            continue

        # Collect all content between this header and the next
        content_elements = []
        sibling = header.next_sibling
        next_header = algo_headers[i + 1] if i + 1 < len(algo_headers) else None

        while sibling:
            if sibling == next_header:
                break
            if isinstance(sibling, Tag):
                if sibling.name in ("h2", "h3") and sibling in algo_headers:
                    break
                content_elements.append(sibling)
            sibling = sibling.next_sibling

        # Extract overview — usually the first <p> after the header
        overview = ""
        for el in content_elements:
            if el.name == "p":
                text = clean_text(el.get_text())
                if text and len(text) > 10:
                    overview = text
                    break

        # Extract parameters
        parameters = extract_parameters(content_elements)
        perf_params = extract_performance_params(content_elements)

        algorithms.append({
            "name": algo_name,
            "category": category,
            "overview": overview,
            "parameters": parameters,
            "performanceParams": perf_params,
        })

    return algorithms


def extract_parameters(elements: list[Tag]) -> list[dict]:
    """Extract parameter info from content elements."""
    params = []
    seen_names = set()

    for el in elements:
        # Try <dl> definition lists (most common pattern in H90 manual)
        for dl in ([el] if el.name == "dl" else el.find_all("dl")):
            dts = dl.find_all("dt", recursive=False) if dl.name == "dl" else dl.find_all("dt")
            dds = dl.find_all("dd", recursive=False) if dl.name == "dl" else dl.find_all("dd")
            for dt, dd in zip(dts, dds):
                name = clean_text(dt.get_text())
                # Skip section headers masquerading as parameter names
                if is_section_header(name):
                    continue
                full_desc = extract_dd_full_text(dd)
                full_desc = strip_section_header_contamination(full_desc)
                full_desc = strip_footer_artifacts(full_desc)
                if name and name not in seen_names:
                    seen_names.add(name)
                    params.append(build_param(name, full_desc))

        # Try table rows
        for table in ([el] if el.name == "table" else el.find_all("table")):
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all(["td", "th"])
                if len(cells) >= 2:
                    name = clean_text(cells[0].get_text())
                    full_desc = clean_text(cells[1].get_text())
                    # Skip header rows and section headers
                    if name.lower() in ("parameter", "name", "control", ""):
                        continue
                    if is_section_header(name):
                        continue
                    full_desc = strip_section_header_contamination(full_desc)
                    full_desc = strip_footer_artifacts(full_desc)
                    if name and name not in seen_names:
                        seen_names.add(name)
                        range_val = clean_text(cells[2].get_text()) if len(cells) >= 3 else None
                        params.append(build_param(name, full_desc, range_val))

        # Try <h4> + <p> pattern
        for h4 in ([el] if el.name == "h4" else el.find_all("h4")):
            name = clean_text(h4.get_text())
            if is_section_header(name):
                continue
            desc_parts = []
            sib = h4.next_sibling
            while sib:
                if isinstance(sib, Tag):
                    if sib.name in ("h4", "h3", "h2"):
                        break
                    text = clean_text(sib.get_text())
                    # Stop if we hit a section header in text
                    if is_section_header(text):
                        break
                    desc_parts.append(text)
                sib = sib.next_sibling
            full_desc = " ".join(desc_parts)
            full_desc = strip_section_header_contamination(full_desc)
            full_desc = strip_footer_artifacts(full_desc)
            if name and name not in seen_names and full_desc:
                seen_names.add(name)
                params.append(build_param(name, full_desc))

    return params


def build_param(name: str, full_desc: str, range_val: str | None = None) -> dict:
    """Build a parameter dict with short description, full description, and range."""
    if not range_val:
        range_val = extract_range(full_desc)

    short_desc = make_short_description(full_desc)

    return {
        "name": name,
        "description": short_desc,
        "range": range_val if range_val else None,
        "fullDescription": full_desc,
    }


def extract_range(text: str) -> str | None:
    """Try to extract a range value from description text."""
    patterns = [
        r"(\d+\s*[-–]\s*\d+\s*(?:ms|Hz|%|dB|sec|s))",
        r"(\d+\s+to\s+\d+\s*(?:ms|Hz|%|dB|sec|s))",
        r"(-?\d+(?:\.\d+)?\s*(?:oct|st|ct)\s+to\s+[+-]?\d+(?:\.\d+)?\s*(?:oct|st|ct))",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    return None


def make_short_description(full_desc: str) -> str:
    """Create a concise description from the full text."""
    # Take first sentence
    sentences = re.split(r"(?<=[.;])\s+", full_desc)
    short = sentences[0].strip() if sentences else full_desc
    # Truncate if still too long
    if len(short) > 80:
        short = short[:77] + "..."
    return short


def extract_performance_params(elements: list[Tag]) -> list[dict]:
    """Extract performance parameters from content elements."""
    params = []
    in_perf_section = False

    for el in elements:
        text = clean_text(el.get_text()).lower()

        # Detect performance parameter section header
        if "performance" in text and el.name in ("h3", "h4", "h5", "p", "strong", "dt"):
            in_perf_section = True
            continue

        if in_perf_section:
            # Look for <dl> lists
            for dl in ([el] if el.name == "dl" else el.find_all("dl")):
                dts = dl.find_all("dt")
                dds = dl.find_all("dd")
                for dt, dd in zip(dts, dds):
                    name = clean_text(dt.get_text())
                    desc = clean_text(dd.get_text())
                    desc = strip_footer_artifacts(desc)
                    if name:
                        params.append({"name": name, "description": desc})

            # Look for <li> items
            for li in el.find_all("li"):
                li_text = clean_text(li.get_text())
                if ":" in li_text:
                    name, desc = li_text.split(":", 1)
                    params.append({"name": name.strip(), "description": desc.strip()})
                elif li_text:
                    params.append({"name": li_text, "description": ""})

            # Stop if we hit another section
            if el.name in ("h2", "h3") and "performance" not in text:
                in_perf_section = False

    return params


def fetch_all_algorithms(base_url: str) -> list[dict]:
    """Fetch and extract algorithms from all category pages."""
    all_algos = []

    for page_slug, category in CATEGORY_PAGES.items():
        url = urljoin(base_url, page_slug)
        print(f"Fetching {category} ({url})...", file=sys.stderr)

        try:
            soup = fetch_page(url)
            algos = extract_algorithms_from_page(soup, category)
            print(f"  Found {len(algos)} algorithms", file=sys.stderr)
            all_algos.extend(algos)
        except requests.RequestException as e:
            print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"  ERROR parsing {category}: {e}", file=sys.stderr)

        time.sleep(REQUEST_DELAY)

    return all_algos


def merge_with_existing(new_algos: list[dict], existing_path: Path) -> list[dict]:
    """
    Merge newly extracted data with existing JSON, preserving any manual edits.

    Strategy:
    - If an algorithm exists in both, update fullDescription fields from new data
    - Keep existing short descriptions and ranges (they may have been manually refined)
    - Add any new algorithms not in existing data
    """
    if not existing_path.exists():
        return new_algos

    with open(existing_path) as f:
        existing = json.load(f)

    existing_map = {a["name"]: a for a in existing}
    new_map = {a["name"]: a for a in new_algos}

    merged = []
    for algo in existing:
        name = algo["name"]
        if name in new_map:
            new_algo = new_map[name]
            existing_params_map = {p["name"]: p for p in algo.get("parameters", [])}
            for new_p in new_algo.get("parameters", []):
                if new_p["name"] in existing_params_map:
                    existing_params_map[new_p["name"]]["fullDescription"] = new_p.get("fullDescription", new_p["description"])
                else:
                    algo.setdefault("parameters", []).append(new_p)

            new_perf_map = {p["name"]: p for p in new_algo.get("performanceParams", [])}
            for pp in algo.get("performanceParams", []):
                pp_name = pp["name"] if isinstance(pp, dict) else pp
                if pp_name in new_perf_map:
                    if isinstance(pp, dict):
                        pp["description"] = new_perf_map[pp_name].get("description", pp.get("description", ""))

            if len(new_algo.get("overview", "")) > len(algo.get("overview", "")):
                algo["overview"] = new_algo["overview"]

        merged.append(algo)

    for name, algo in new_map.items():
        if name not in existing_map:
            merged.append(algo)
            print(f"  NEW algorithm added: {name}", file=sys.stderr)

    return merged


def main():
    parser = argparse.ArgumentParser(description="Extract H90 algorithm data from the Eventide manual")
    parser.add_argument("-o", "--output", default="data/algorithms.json", help="Output JSON file path (default: data/algorithms.json)")
    parser.add_argument("--dry-run", action="store_true", help="Print JSON to stdout without writing file")
    parser.add_argument("--fresh", action="store_true", help="Ignore existing data and extract everything from scratch")
    parser.add_argument("--sync-public", action="store_true", help="Also copy output to public/data/algorithms.json")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Base URL for manual pages")
    args = parser.parse_args()

    base_url = args.base_url
    validate_url(base_url)

    project_root = Path(__file__).resolve().parent.parent
    output_path = project_root / args.output

    print("H90 Lens — Algorithm Data Extractor", file=sys.stderr)
    print(f"Source: {base_url}", file=sys.stderr)
    print(f"Output: {output_path}", file=sys.stderr)
    print(file=sys.stderr)

    new_algos = fetch_all_algorithms(base_url)
    print(f"\nExtracted {len(new_algos)} algorithms total", file=sys.stderr)

    if args.fresh or not output_path.exists():
        result = new_algos
    else:
        print(f"Merging with existing {output_path}...", file=sys.stderr)
        result = merge_with_existing(new_algos, output_path)

    result.sort(key=lambda a: (a["category"], a["name"]))

    # Validate
    categories = set(a["category"] for a in result)
    print(f"\nResult: {len(result)} algorithms across {len(categories)} categories", file=sys.stderr)
    for cat in sorted(categories):
        count = sum(1 for a in result if a["category"] == cat)
        print(f"  {cat}: {count}", file=sys.stderr)

    json_str = json.dumps(result, indent=2, ensure_ascii=False)

    if args.dry_run:
        print(json_str)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(json_str + "\n")
        print(f"\nWritten to {output_path}", file=sys.stderr)

        # Sync to public/ for Vite static serving
        if args.sync_public:
            public_path = project_root / "public" / "data" / "algorithms.json"
            public_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(output_path, public_path)
            print(f"Synced to {public_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
