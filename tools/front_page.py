# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The front page keeps itself current (the founder's order of 10 October 2026: the newest result is always at the front, and
the repository, not a person, moves it there).

Reads every archived live run under results/live/raw/run-<id>/ of the five live products (Redis, Kafka, PostgreSQL, MySQL,
MongoDB), groups the runs into sets of three by what they are (the product, the verdict's objective, the engine the run
carried, the workloads it ran), takes the three newest complete runs of each kind as A, B and C, and where that set is newer
than the table on the front page: moves the table whole into docs/history as the next numbered set, rebuilds it with the
product's own three-run tool, then rebuilds the index, the wiring page, the benefit sheet and the dossier, and writes one
line per rebuilt table into the README's latest block. Nothing is ever deleted: every superseded table is kept in history,
every raw file stays archived.

  python tools/front_page.py            # the plan only: what would be rebuilt, as JSON; nothing changes
  python tools/front_page.py --apply    # do it
  python tools/front_page.py --summary  # one line for a commit message

Run by the front-page workflow after every finished live run (.github/workflows/front-page.yml) and by hand after a pull."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "results" / "live" / "raw"
LIVE = ROOT / "results" / "live"
HISTORY = ROOT / "docs" / "history"
STATE = LIVE / "FRONT_PAGE_STATE.json"
README = ROOT / "README.md"
BEGIN, END = "<!-- front-page:begin -->", "<!-- front-page:end -->"

# the five live products: the artifact prefix the run's files carry, the table's base name, the three-run tool
PRODUCTS = {
    "redis": ("REDIS", "tools/redis_abc.py"),
    "kafka": ("KAFKA", "tools/kafka_abc.py"),
    "pgbench": ("PGBENCH", "tools/pgbench_abc.py"),
    "sysbench": ("SYSBENCH", "tools/sysbench_abc.py"),
    "ycsb": ("YCSB", "tools/ycsb_abc.py"),
}
AFTER = ["tools/omni_index.py", "tools/wiring_verdicts.py", "tools/benefit_sheet.py", "tools/dossier.py"]


def _run_id(d: Path):
    m = re.fullmatch(r"run-(\d+)", d.name)
    return int(m.group(1)) if m else None


def _find(obj, key, depth=0):
    """The first value of `key` anywhere inside a JSON document (the objective sits at the top of a Redis or Kafka workload
    record and inside each repetition's arm record of a database run; the engine sits in the workload summary)."""
    if depth > 6:
        return None
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for v in obj.values():
            r = _find(v, key, depth + 1)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj[:50]:
            r = _find(v, key, depth + 1)
            if r is not None:
                return r
    return None


def describe(run_dir: Path):
    """What one archived run is: (product, objective, engine version, workloads) or None when it is not a complete live
    product run (no report directory, or no workload directory). The workloads are the run's own artifact directories
    (`<product>-<workload>`); the objective and the engine are read from the records inside them, wherever each product keeps
    them; a record that names neither reads as the resource objective on the engine the table was built for."""
    product = None
    for p in PRODUCTS:
        if (run_dir / f"{p}-report").is_dir():
            product = p
            break
    if product is None:
        return None
    workloads, objective, engine = set(), None, None
    for sub in sorted(run_dir.iterdir()):
        if not sub.is_dir() or not sub.name.startswith(f"{product}-") or sub.name == f"{product}-report":
            continue
        workloads.add(sub.name[len(product) + 1:])
        if objective is not None and engine is not None:
            continue
        for f in sorted(sub.rglob("*.json"))[:400]:
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if objective is None:
                o = _find(d, "objective")
                if isinstance(o, str) and o:
                    objective = o
            if engine is None:
                e = _find(d, "engine")
                if isinstance(e, dict) and e.get("version"):
                    engine = str(e["version"])
                elif isinstance(e, str) and e.startswith("omni-v"):
                    engine = e
            if objective is not None and engine is not None:
                break
    if not workloads:
        return None
    return product, objective or "resource", engine_version(engine or "omni-v3"), tuple(sorted(workloads))


def engine_version(text):
    """The engine a record names, reduced to its version: "omni-v3 (digest b53d05449ee04c4b, 40 files)" is "omni-v3"; a record
    whose engine is not a declared version ("differs from v2: ...") reads "unversioned" and never joins a versioned set."""
    m = re.search(r"omni-v(\d+)", str(text or ""))
    return f"omni-v{m.group(1)}" if m else "unversioned"


def table_name(product, objective, engine):
    base = PRODUCTS[product][0]
    m = re.search(r"omni-v(\d+)", engine_version(engine))
    v = m.group(1) if m else "0"
    return f"V{v}_{base}" + ("" if objective == "resource" else f"_{objective.upper().replace('-', '_')}")


def plan(root: Path = ROOT):
    """Every table whose three newest complete runs differ from the runs it was last built from."""
    raw = root / "results" / "live" / "raw"
    state = {}
    sp = root / "results" / "live" / "FRONT_PAGE_STATE.json"
    if sp.exists():
        try:
            state = json.loads(sp.read_text(encoding="utf-8"))
        except ValueError:
            state = {}
    kinds = {}
    for d in sorted(raw.glob("run-*")) if raw.is_dir() else []:
        rid = _run_id(d)
        if rid is None:
            continue
        desc = describe(d)
        if desc is None:
            continue
        kinds.setdefault(desc, []).append(rid)
    out = []
    for (product, objective, engine, workloads), ids in sorted(kinds.items()):
        ids = sorted(ids)
        if len(ids) < 3:
            continue
        a, b, c = ids[-3:]
        name = table_name(product, objective, engine)
        built = state.get(name, {}).get("runs")
        table = root / "results" / "live" / f"{name}.md"
        if built == [a, b, c] and table.exists():
            continue
        out.append({"table": name, "product": product, "objective": objective, "engine": engine, "workloads": list(workloads),
                    "runs": [a, b, c], "tool": PRODUCTS[product][1], "previous": built, "table_exists": table.exists()})
    return out


def next_history_name(name: str, history: Path = HISTORY):
    n = 1 + len(list(history.glob(f"{name}_set*.md")))
    return history / f"{name}_set{n}.md"


def apply(items, root: Path = ROOT):
    """Rebuild each planned table (the old one kept whole in docs/history), then the pages read from every table, then the
    README's latest lines. Returns the lines written."""
    py = sys.executable
    lines = []
    state = {}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text(encoding="utf-8"))
        except ValueError:
            state = {}
    for it in items:
        name = it["table"]
        table = LIVE / f"{name}.md"
        if table.exists():
            dest = next_history_name(name)
            HISTORY.mkdir(parents=True, exist_ok=True)
            dest.write_text(table.read_text(encoding="utf-8"), encoding="utf-8")   # kept whole, then replaced
        dirs = [str(RAW / f"run-{r}") for r in it["runs"]]
        r = subprocess.run([py, str(root / it["tool"]), *dirs, "--out", str(table)], capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit(f"{it['tool']} failed on {name}: {(r.stdout + r.stderr)[-800:]}")
        summary = (r.stdout.strip().splitlines() or [""])[-1][:160]
        state[name] = {"runs": it["runs"], "built": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                       "engine": it["engine"], "objective": it["objective"], "summary": summary}
        lines.append(f"- {state[name]['built']}: `{name}` rebuilt from runs {it['runs'][0]}, {it['runs'][1]}, {it['runs'][2]}"
                     f" ({it['product']}, the {it['objective']} objective, {it['engine']}): {summary}")
    if items:
        STATE.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        for tool in AFTER:
            r = subprocess.run([py, str(root / tool)], capture_output=True, text=True)
            if r.returncode != 0:
                raise SystemExit(f"{tool} failed: {(r.stdout + r.stderr)[-800:]}")
        write_readme(lines)
    return lines


def write_readme(lines, readme: Path = README, keep: int = 8):
    """The README's latest block: the newest lines first, at most `keep`, between the two markers. Without the markers the
    README is left alone (and said so)."""
    if not lines:
        return False
    s = readme.read_text(encoding="utf-8")
    if BEGIN not in s or END not in s:
        print("README has no front-page markers; the latest lines were not written", file=sys.stderr)
        return False
    head, rest = s.split(BEGIN, 1)
    old, tail = rest.split(END, 1)
    kept = [ln for ln in old.strip().splitlines() if ln.strip()]
    block = "\n".join(list(reversed(lines)) + kept)[:100000]
    block_lines = [ln for ln in block.splitlines() if ln.strip()][:keep]
    readme.write_text(head + BEGIN + "\n" + "\n".join(block_lines) + "\n" + END + tail, encoding="utf-8")
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--apply", action="store_true", help="rebuild what the plan names; without it, print the plan only")
    ap.add_argument("--summary", action="store_true", help="one line naming the tables the plan would rebuild")
    a = ap.parse_args(argv)
    items = plan()
    if a.summary:
        print(", ".join(it["table"] for it in items) if items else "nothing to rebuild")
        return 0
    if not a.apply:
        print(json.dumps(items, indent=1))
        return 0
    lines = apply(items)
    print("\n".join(lines) if lines else "nothing to rebuild: every table is built from its three newest runs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
