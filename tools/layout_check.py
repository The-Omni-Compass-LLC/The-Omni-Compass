#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The repository stays lined up: run by verify.py on every release, so a push that leaves the tree out of line fails.

Checks:
  root      the root holds only the declared set (ROOT_ALLOWED): the front door, the license and IP papers, the
            build files. Anything else belongs under docs/, .github/ or a code folder.
  links     every relative link in every Markdown file points at a file or folder that exists.
  paths     every repository path a Markdown file names in backticks (`results/...`, `docs/...`, `tools/...`, ...)
            exists, so no page cites a file that has gone.
  orphans   every top-level entry of results/ is named by some page or program outside results/, so a result nothing
            uses falls off instead of piling up.

  python3 tools/layout_check.py        (exit 0: lined up; exit 1: what is out of line, one line each)
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT_ALLOWED = {
    # the front door
    "README.md", "CHANGELOG.md", "CITATION.cff", "SECURITY.md",
    # the license and the intellectual property
    "LICENSE", "LICENSES", "NOTICE", "PATENTS.md", "TRADEMARKS.md", "THIRD_PARTY_NOTICES.md", "REUSE.toml",
    "DISCLOSURES.md", "LICENSING_FAQ.md", "CLAUDE.md",
    # the same rules for every AI assistant that reads this repository (Codex, Copilot, Gemini, Cursor)
    "AGENTS.md", "GEMINI.md", ".cursorrules",
    # build, verification and metadata
    "pyproject.toml", "requirements.txt", "requirements-lock.txt", "verify.py", "RELEASE_MANIFEST.json", "OMNI_V1.json", "OMNI_V2.json", "OMNI_V3.json", "codemeta.json",
    "docker-compose.yml", ".gitignore", ".gitattributes", ".dockerignore", ".github", ".fossa.yml", ".snyk",
    # code and evidence
    "omnicompass", "omni_controller", "realms", "cpp", "tools", "scripts", "tests", "deploy", "fleet", "pilot",
    "k8s_controlplane", "k8s_fleet", "omnilab", "hardware", "benchmarks", "tuning", "reference", "fixtures", "sbom",
    "results", "docs", "release",
}
PATH_PREFIXES = ("results/", "docs/", "tools/", "scripts/", "realms/", "omnicompass/", "omni_controller/", "tests/",
                 ".github/", "deploy/", "tuning/", "cpp/")
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")
TICK = re.compile(r"`([A-Za-z0-9_.\-/]+)`")


def tracked():
    out = subprocess.run(["git", "-c", "safe.directory=*", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout
    return [p for p in out.splitlines() if p]


def main():
    files = tracked()
    present = set(files)
    dirs = {str(Path(p).parents[i]) for p in files for i in range(len(Path(p).parents) - 1)}
    problems = []
    for top in sorted({p.split("/")[0] for p in files}):
        if top not in ROOT_ALLOWED:
            problems.append(f"root: {top} is not in the declared root set (move it under docs/, .github/ or a code folder)")
    for p in files:
        if not p.endswith(".md") or p.startswith(("results/live/raw/", "release/", "results/external_review/")) \
                or p == "docs/book/OMNI_COMPASS_BOOK.md":            # quoted reviews; the book is built (build_book.py)
            continue
        text = (ROOT / p).read_text(errors="ignore")
        base = Path(p).parent
        for m in LINK.finditer(text):
            t = m.group(1)
            if "://" in t or t.startswith(("mailto:", "/")):
                continue
            q = (base / t).as_posix()
            q = str(Path(q)).replace("\\", "/")
            norm = Path(*[x for x in Path(q).parts])
            parts = []
            for x in norm.parts:
                if x == "..":
                    parts = parts[:-1]
                elif x != ".":
                    parts.append(x)
            q = "/".join(parts)
            if q and q not in present and q not in dirs:
                problems.append(f"link: {p} -> {t} (no such file)")
        for m in TICK.finditer(text):
            t = m.group(1).rstrip("/.")
            last = t.rsplit("/", 1)[-1]
            if "." in last and not re.search(r"\.(md|py|sh|json|csv|txt|yml|yaml|toml|cpp|hpp|h|pdf|png|jsonl|gz|zip|cff)$", last):
                continue                                         # a module attribute (pkg/module.name), not a file
            if t.startswith(PATH_PREFIXES) and "*" not in t and "<" not in t and "STAMP" not in t:
                if t not in present and t not in dirs:
                    problems.append(f"path: {p} names `{t}` (no such file)")
    corpus = "\n".join((ROOT / p).read_text(errors="ignore") for p in files
                       if not p.startswith(("results/", "release/")) and p != "RELEASE_MANIFEST.json"
                       and p != "docs/book/OMNI_COMPASS_BOOK.md" and p.endswith((".md", ".py", ".sh", ".yml", ".yaml", ".toml", ".json", ".txt")))
    for top in sorted({p.split("/")[1] for p in files if p.startswith("results/") and p.count("/") >= 1}):
        stem = top.rsplit(".", 1)[0] if "." in top else top
        if top.startswith("VERIFY_") or (f"results/{top}" not in corpus and f"results/{stem}" not in corpus and f'"{top}"' not in corpus
                                         and f"'{top}'" not in corpus and top not in corpus
                                         and not (re.sub(r"\d+$", "", top) != top and re.sub(r"\d+$", "", top) in corpus)):
            if not top.startswith("VERIFY_"):
                problems.append(f"orphan: results/{top} is named by no page or program (remove it, or cite it)")
    for x in problems:
        print(x)
    print(f"layout: {len(problems)} out of line" if problems else "layout: lined up")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
