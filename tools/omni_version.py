#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The frozen engines, fingerprinted file by file: Omni v3 (OMNI_V3.json, docs/OMNI_V3.md), v2 (OMNI_V2.json,
docs/OMNI_V2.md) and v1 (OMNI_V1.json, docs/OMNI_V1.md).

  python3 tools/omni_version.py                 check this checkout: prints "omni-v3", "omni-v2" or "omni-v1", or what differs from the newest
  python3 tools/omni_version.py --commit <sha>  the same, for the engine as it stood at a git commit (any result's run)
  python3 tools/omni_version.py --write v3      write OMNI_V3.json from this checkout (only when a new version is declared)

The engine is the compass law, the live controllers, the realms and their organisms, and the runners of the
independent simulators. One SHA-256 per file, and one over the sorted list. A result is a v2 result only if the commit
it ran on carries exactly v2's bytes; a v1 result only if it carries v1's. No result is read across versions.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = {"v3": ROOT / "OMNI_V3.json", "v2": ROOT / "OMNI_V2.json", "v1": ROOT / "OMNI_V1.json"}     # newest first
SCOPE = ("omnicompass", "omni_controller", "realms", "tools/run_kil.py", "tools/run_citylearn.py", "tools/run_pandapower.py")


def engine_files(commit: str | None = None) -> dict[str, str]:
    ref = commit or "HEAD"
    # a commit's engine is what its tree holds; this checkout's engine is every tracked or staged file (so a file added
    # for a new version is fingerprinted before its first commit, never after)
    cmd = ["git", "ls-tree", "-r", "--name-only", ref, "--", *SCOPE] if commit else ["git", "ls-files", "--", *SCOPE]
    names = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    out = {}
    for n in sorted(names):
        if not n.endswith((".py", ".csv")) or "__pycache__" in n:
            continue
        data = (subprocess.run(["git", "show", f"{ref}:{n}"], cwd=ROOT, capture_output=True, check=True).stdout
                if commit else (ROOT / n).read_bytes())
        out[n] = hashlib.sha256(data).hexdigest()
    return out


def digest(files: dict[str, str]) -> str:
    return hashlib.sha256("".join(f"{h}  {n}\n" for n, h in sorted(files.items())).encode()).hexdigest()


def version_of(files: dict[str, str]) -> str | None:
    """'omni-v2', 'omni-v1' or None, for a set of engine files."""
    d = digest(files)
    for v, path in VERSIONS.items():
        if path.exists() and json.loads(path.read_text())["digest"] == d:
            return f"omni-{v}"
    return None


def version_before(files: dict[str, str]) -> tuple[str | None, list[str]]:
    """('omni-vN', [files not yet written]) for a commit that holds a strict subset of a version's engine files, every
    one of them that version's bytes (the commits between a version's freeze and a runner added inside it); else (None, [])."""
    for v, path in VERSIONS.items():
        if not path.exists():
            continue
        want = json.loads(path.read_text())["files"]
        missing = sorted(set(want) - set(files))
        if missing and set(files) <= set(want) and all(want[n] == h for n, h in files.items()):
            return f"omni-{v}", missing
    return None, []


def main() -> int:
    args = sys.argv[1:]
    commit = args[args.index("--commit") + 1] if "--commit" in args and len(args) > args.index("--commit") + 1 else None
    if "--commit" in args and not (commit or "").strip():
        print("--commit needs a commit; an empty one is not the working tree", file=sys.stderr); return 2
    files = engine_files(commit)
    if "--write" in args:
        v = args[args.index("--write") + 1] if len(args) > args.index("--write") + 1 and not args[args.index("--write") + 1].startswith("-") else next(iter(VERSIONS))
        if v not in VERSIONS:
            print(f"unknown version {v}; one of {sorted(VERSIONS)}", file=sys.stderr); return 2
        VERSIONS[v].write_text(json.dumps({"version": f"omni-{v}", "digest": digest(files), "files": files}, indent=1) + "\n")
        print(f"{VERSIONS[v].name} written: {len(files)} files, digest {digest(files)[:16]}")
        return 0
    v = version_of(files)
    if v:
        print(f"{v} (digest {digest(files)[:16]}, {len(files)} files)")
        return 0
    v, missing = version_before(files)
    if v:
        # a commit from before a runner was written, every other engine file that version's bytes: the version's result
        # for every test but the one that runner serves (which could not have run there), and the line says so
        print(f"{v} ({len(files)} of {len(files) + len(missing)} files, all {v[5:]} bytes; not yet in this commit: {', '.join(missing)})")
        return 0
    newest = next(iter(VERSIONS))
    want = json.loads(VERSIONS[newest].read_text())
    for n in sorted(set(files) | set(want["files"])):
        if files.get(n) != want["files"].get(n):
            print(f"differs from {newest}: {n}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
