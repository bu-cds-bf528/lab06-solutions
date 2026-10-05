#!/usr/bin/env python3
"""
Lab-agnostic log enforcement check.

Reads every briefs/*.md file, extracts its YAML-ish frontmatter (id,
target_files), and checks: for any brief whose target_files overlap with
what has changed in the working tree, logs/<id>.md must also have changed.

No third-party dependencies (no PyYAML) — the frontmatter parsing here only
needs to handle simple `key: value` lines and `- item` list entries, which
is all the brief template uses.

Used two ways:
  - As a Claude Code Stop hook (reads JSON on stdin, checks stop_hook_active,
    exits 2 with a message on stderr to block).
  - As a CI check (pass --ci and a --base <ref> to diff against; exits 1 on
    failure instead of 2, no stdin expected).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BRIEFS_DIR = REPO_ROOT / "briefs"
LOGS_DIR = REPO_ROOT / "logs"


def parse_frontmatter(text):
    """Minimal frontmatter parser: handles `key: value` and `key:\n  - item`."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip("\n")
    data = {}
    current_list_key = None
    for line in block.splitlines():
        if line.startswith("  - ") or line.startswith("- "):
            if current_list_key:
                data.setdefault(current_list_key, []).append(line.strip("- ").strip())
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value:
                data[key] = value
                current_list_key = None
            else:
                current_list_key = key
                data.setdefault(key, [])
    return data


def load_briefs():
    briefs = []
    if not BRIEFS_DIR.exists():
        return briefs
    for path in BRIEFS_DIR.glob("*.md"):
        if path.name.startswith("_"):
            continue  # template/example files, not real briefs
        meta = parse_frontmatter(path.read_text())
        if "id" in meta and "target_files" in meta:
            briefs.append(meta)
    return briefs


def changed_files(base_ref=None):
    if base_ref:
        cmd = ["git", "diff", "--name-only", f"{base_ref}...HEAD"]
    else:
        cmd = ["git", "diff", "--name-only", "HEAD"]
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    return set(line.strip() for line in result.stdout.splitlines() if line.strip())


def main():
    ci_mode = "--ci" in sys.argv
    base_ref = None
    if "--base" in sys.argv:
        base_ref = sys.argv[sys.argv.index("--base") + 1]

    if not ci_mode:
        # Stop hook: read stdin, bail out if we already tried this once.
        try:
            stdin_data = json.loads(sys.stdin.read() or "{}")
        except json.JSONDecodeError:
            stdin_data = {}
        if stdin_data.get("stop_hook_active"):
            sys.exit(0)

    changed = changed_files(base_ref)
    if not changed:
        sys.exit(0)

    problems = []
    for brief in load_briefs():
        brief_id = brief["id"]
        targets = set(brief.get("target_files", []))
        if not targets:
            continue
        touched = targets & changed
        if not touched:
            continue
        log_path = f"logs/{brief_id}.md"
        if log_path not in changed:
            problems.append(
                f"Brief '{brief_id}': changed {sorted(touched)} but {log_path} "
                f"was not updated."
            )

    if problems:
        msg = "Log check failed:\n" + "\n".join(f"- {p}" for p in problems)
        print(msg, file=sys.stderr)
        sys.exit(1 if ci_mode else 2)

    sys.exit(0)


if __name__ == "__main__":
    main()
