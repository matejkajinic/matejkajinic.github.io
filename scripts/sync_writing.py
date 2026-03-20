#!/usr/bin/env python3
"""Sync writing pages from external public GitHub repositories."""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import posixpath
import re
import sys
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError


ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "writing_sources.yml"
OUTPUT_DIR = ROOT / "_writing"


def parse_sources(path: pathlib.Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("- "):
            if current:
                entries.append(current)
            current = {}
            payload = line[2:].strip()
            if payload:
                key, value = payload.split(":", 1)
                current[key.strip()] = value.strip().strip("'\"")
            continue

        if current is None or ":" not in line:
            continue

        key, value = line.split(":", 1)
        current[key.strip()] = value.strip().strip("'\"")

    if current:
        entries.append(current)
    return entries


def fetch_text(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "matejkajinic-github-io-sync",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8")


def yaml_line(key: str, value: str) -> str:
    escaped = value.replace("'", "''")
    return f"{key}: '{escaped}'"


def build_front_matter(entry: dict[str, str], commit: dict[str, str]) -> str:
    lines = [
        "---",
        "layout: article",
        yaml_line("title", entry["title"]),
        yaml_line("description", entry["description"]),
        yaml_line("github_repo", entry["repo"]),
        yaml_line("github_url", f"https://github.com/{entry['repo']}"),
        yaml_line("source_path", entry["path"]),
    ]
    if commit.get("sha"):
        lines.append(yaml_line("last_commit_sha", commit["sha"]))
    if commit.get("date"):
        lines.append(yaml_line("last_commit_date", commit["date"]))
    lines.append("---")
    return "\n".join(lines)


def render_source_content(source_path: str, text: str) -> str:
    if not source_path.endswith(".ipynb"):
        return text

    notebook = json.loads(text)
    blocks: list[str] = []
    for cell in notebook.get("cells", []):
        source = "".join(cell.get("source", []))
        if not source.strip():
            continue
        if cell.get("cell_type") == "markdown":
            blocks.append(source.rstrip())
            continue
        if cell.get("cell_type") == "code":
            blocks.append(f"```python\n{source.rstrip()}\n```")
    return "\n\n".join(blocks).strip() + "\n"


def rewrite_relative_image_links(repo: str, source_path: str, text: str) -> str:
    source_dir = posixpath.dirname(source_path)

    def to_raw_url(url: str) -> str:
        trimmed = url.strip()
        if not trimmed:
            return trimmed
        lower = trimmed.lower()
        if (
            "://" in trimmed
            or lower.startswith("data:")
            or lower.startswith("mailto:")
            or trimmed.startswith("#")
        ):
            return trimmed

        normalized = trimmed.lstrip("./")
        if source_dir:
            normalized = posixpath.normpath(posixpath.join(source_dir, normalized))
        else:
            normalized = posixpath.normpath(normalized)
        encoded = urllib.parse.quote(normalized, safe="/")
        return f"https://raw.githubusercontent.com/{repo}/HEAD/{encoded}"

    def replace_markdown_image(match: re.Match[str]) -> str:
        alt_text = match.group(1)
        destination = match.group(2)
        suffix = match.group(3) or ""
        return f"![{alt_text}]({to_raw_url(destination)}{suffix})"

    def replace_html_img(match: re.Match[str]) -> str:
        prefix = match.group(1)
        destination = match.group(2)
        suffix = match.group(3)
        return f'{prefix}{to_raw_url(destination)}{suffix}'

    markdown_pattern = r"!\[([^\]]*)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)"
    html_pattern = r'(<img[^>]*\ssrc=["\'])([^"\']+)(["\'][^>]*>)'

    updated = re.sub(markdown_pattern, replace_markdown_image, text)
    updated = re.sub(html_pattern, replace_html_img, updated, flags=re.IGNORECASE)
    return updated


def normalize_compact_tables(text: str) -> str:
    fixed_lines: list[str] = []
    for line in text.splitlines():
        # Some READMEs include whole markdown tables collapsed into one line:
        # "| H1 | H2 | | :--- | :--- | | row1 | row2 | ..."
        # Split these back into per-row lines for reliable rendering.
        if line.startswith("|") and " | | " in line and line.count("|") >= 12:
            rebuilt = line.replace(" | | ", " |\n| ").replace("|| ", "|\n| ")
            fixed_lines.append(rebuilt)
            continue
        fixed_lines.append(line)
    return "\n".join(fixed_lines)


def fetch_commit(repo: str, source_path: str) -> dict[str, str]:
    encoded_path = urllib.parse.quote(source_path, safe="/")
    url = (
        f"https://api.github.com/repos/{repo}/commits"
        f"?path={encoded_path}&per_page=1"
    )
    payload = json.loads(fetch_text(url))
    if not payload:
        return {}

    latest = payload[0]
    return {
        "sha": latest.get("sha", ""),
        "date": latest.get("commit", {}).get("committer", {}).get("date", ""),
    }


def sync() -> int:
    if not SOURCES_FILE.exists():
        print(f"Missing source map: {SOURCES_FILE}", file=sys.stderr)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entries = parse_sources(SOURCES_FILE)
    if not entries:
        print("No entries found in writing_sources.yml", file=sys.stderr)
        return 1

    now = dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    failures: list[str] = []
    for entry in entries:
        try:
            slug = entry["slug"]
            source_path = entry.get("path", "README.md")
            repo = entry["repo"]
            raw_path = urllib.parse.quote(source_path, safe="/")
            raw_url = f"https://raw.githubusercontent.com/{repo}/HEAD/{raw_path}"

            content = fetch_text(raw_url)
            rendered = render_source_content(source_path, content)
            rendered = rewrite_relative_image_links(repo, source_path, rendered)
            rendered = normalize_compact_tables(rendered)
            commit = fetch_commit(repo, source_path)
            front_matter = build_front_matter(entry, commit)
            output = (
                f"{front_matter}\n\n"
                f"<!-- Generated at {now} by scripts/sync_writing.py -->\n\n"
                f"{rendered}\n"
            )
            (OUTPUT_DIR / f"{slug}.md").write_text(output, encoding="utf-8")
            print(f"Synced {slug}")
        except (KeyError, ValueError, HTTPError, URLError) as exc:
            failures.append(f"{entry.get('slug', '<unknown>')}: {exc}")
            print(f"Failed {entry.get('slug', '<unknown>')}: {exc}", file=sys.stderr)

    if failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(sync())
