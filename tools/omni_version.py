#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Omni v1: the frozen engine, fingerprinted file by file (docs/OMNI_V1.md).

  python3 tools/omni_version.py            check this checkout against OMNI_V1.json: prints "omni-v1" or what differs
  python3 tools/omni_version.py --commit   the same, for the engine as it stood at a git commit (any result's run)

The engine is the compass law, the live controllers, the realms and their organisms, and the runners of the
independent simulators. One SHA-256 per file, and one over the sorted list. A result is a v1 result only if the commit
it ran on carries exactly these bytes.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "OMNI_V1.json"
SCOPE = ("omnicompass", "omni_controller", "realms", "tools/run_kil.py", "tools/run_citylearn.py", "tools/run_pandapower.py")


def engine_files(commit: str | None = None) -> dict[str, str]:
    ref = commit or "HEAD"
    names = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", *SCOPE], cwd=ROOT, capture_output=True,
                           text=True, check=True).stdout.split()
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


def main() -> int:
    commit = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--commit" else None
    files = engine_files(commit)
    if "--write" in sys.argv:
        MANIFEST.write_text(json.dumps({"version": "omni-v1", "digest": digest(files), "files": files}, indent=1) + "\n")
        print(f"OMNI_V1.json written: {len(files)} files, digest {digest(files)[:16]}")
        return 0
    want = json.loads(MANIFEST.read_text())
    if digest(files) == want["digest"]:
        print(f"omni-v1 (digest {want['digest'][:16]}, {len(files)} files)")
        return 0
    for n in sorted(set(files) | set(want["files"])):
        if files.get(n) != want["files"].get(n):
            print(f"differs from v1: {n}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
