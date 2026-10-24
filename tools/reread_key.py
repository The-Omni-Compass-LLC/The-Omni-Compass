# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every published table read again by the one rule (the founder's order of 24 October 2026: "Any gauge that gives anything
over a 0.5 percent change either way is a change ... it has to show its loss or gain").

The rule is written once, in tools/readings.py (judge_runs for a gauge read over runs, judge_one for one paired comparison);
this tool applies it to the tables already published, because their raw runs are not in this repository: it reads each row's
own numbers, the JSON twin's exact values where the table has one (a three-run table of tools/confirm_abc.py, of the stores'
*_abc.py tools, of the capacity test, an organism report of tools/six_kube_report.py, a model record of tools/toy_gate.py,
tools/beat_ladder.py and tools/solo_study.py), else the printed values (the deterministic simulators' tables: a printed size
of exactly 0.50% counts as at the floor), and rewrites only the Reading cells, the counts under them and the note that says the
table was read again. Every row is kept; every number, run and title is as first written.

  python3 tools/reread_key.py            read every table again and write what changed
  python3 tools/reread_key.py --check    exit 1 if any table would change (the tables already read by the rule pass)
  python3 tools/reread_key.py --report F also write every reading that changed, as JSON, to F
  python3 tools/reread_key.py --ledger F results/REREAD_KEY   the ledger page of a reading again, from its report F
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.readings import (judge_runs, judge_one, rel_change, classify, aim as aim_of, plain, Tally, receipt_key,  # noqa: E402
                            RECEIPT_BEGIN, RECEIPT_END, EVEN_SAME, EVEN_FLOOR, NEVER_MORE, SHOWN, SPENT, HIGHER, LOWER,
                            WORK_PER, SIZE_FLOOR, even_floor, by_word, interval_by_word)

SAME_REL = 1e-6
NOTE_BEGIN = "<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->"
NOTE_END = "<!-- end: read again -->"


def note(exact: bool) -> list[str]:
    src = ("the JSON twin's exact values" if exact else
           "the values the table prints (it keeps no JSON twin; a printed size of exactly 0.50% counts as at the floor)")
    return [NOTE_BEGIN,
            "**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` "
            "judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge "
            "is for, written \"in all three of our runs\" when all three runs moved 0.5% or more the same way with every interval "
            "clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how "
            "many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading "
            f"cells and the counts under them were rewritten, from {src}; every row, run and number is as first written. Where a "
            "paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN "
            "whatever its size), this rule replaces it.",
            NOTE_END]


CHANGES: list[dict] = []          # every reading that changed: file, where, gauge, old, new, the runs' changes
PROBLEMS: list[str] = []          # every table or row this tool could not read, and why


def dump_like(d, original: str) -> str:
    """The data written as its twin was (indent 1; ASCII escapes or not; a closing newline or not), so a twin whose readings did
    not move reads byte for byte as it was."""
    for asc in (True, False):
        for nl in ("\n", ""):
            if json.dumps(json.loads(original), indent=1, ensure_ascii=asc) + nl == original:
                return json.dumps(d, indent=1, ensure_ascii=asc) + nl
    return json.dumps(d, indent=1) + "\n"


def _cls(reading, aim_=None):
    try:
        return classify(plain(reading), aim_)
    except ValueError:
        return "other"


def _record(file, where, gauge, old, new, runs):
    if plain(old) != plain(new):
        CHANGES.append({"file": str(file), "where": where, "gauge": gauge, "old": plain(old), "new": plain(new),
                        "old_class": _cls(old), "new_class": _cls(new), "runs": runs})


def last_cell(line: str) -> str:
    return line.rstrip().rstrip("|").rsplit("|", 1)[1].strip()


def set_last_cell(line: str, new: str) -> str:
    head = line.rstrip().rstrip("|").rsplit("|", 1)[0]
    return f"{head}| {new} |"


def tail_cells(line: str, k: int) -> list[str]:
    """The last k cells of a table row (the label may hold a '|' of its own, as 'mean |torque|')."""
    return [c.strip() for c in line.rstrip().rstrip("|").rsplit("|", k)[1:]]


def table_rows(lines, start):
    """The data rows of the table whose header is lines[start]: their indices."""
    out, i = [], start + 2
    while i < len(lines) and lines[i].startswith("|"):
        out.append(i)
        i += 1
    return out


def model_note() -> list[str]:
    return [NOTE_BEGIN,
            "**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` "
            "judge_one, as `tools/toy_gate.py` reads a model now): a paired change of 0.5% or more either way is a change and never "
            "reads EVEN; it reads its word by the gauge's aim, with \"(not clear of the noise)\" beside it where its 95% interval "
            "over the seeds crosses zero; under 0.5% it reads EVEN, under the floor. Each reading was decided again from the JSON "
            "twin's own mean, interval and relative change, and every row whose words moved is printed again, its numbers wearing "
            "their words' signs; every seed, number and row is as first written. Where a paragraph below says EVEN for an interval "
            "across zero, this rule replaces it. Evidence class S, our own models, never a benchmark result.",
            NOTE_END]


def with_blocks(text: str, exact: bool, model: bool = False) -> str:
    """The table with the reading block of today and the note that it was read again, each between its markers."""
    block = "\n".join(receipt_key())
    if RECEIPT_BEGIN in text and RECEIPT_END in text:
        a = text.index(RECEIPT_BEGIN); b = text.index(RECEIPT_END) + len(RECEIPT_END)
        text = text[:a] + block + text[b:]
    nb = "\n".join(model_note() if model else note(exact))
    if NOTE_BEGIN in text and NOTE_END in text:
        a = text.index(NOTE_BEGIN); b = text.index(NOTE_END) + len(NOTE_END)
        return text[:a] + nb + text[b:]
    lines = text.split("\n")
    at = None
    for i, ln in enumerate(lines):
        if ln.startswith(RECEIPT_END):
            at = i + 1
            break
    if at is None:
        for i, ln in enumerate(lines[:12]):
            if ln.startswith("> ©"):
                at = i + 1
                break
    if at is None:
        for i, ln in enumerate(lines[:4]):
            if ln.startswith("# "):
                at = i + 1
                break
    if at is None:
        return text
    return "\n".join(lines[:at] + ["", nb] + lines[at:])


# ------------------------------------------------------------------------------------------------ a gauge over three runs
def _well(rs):
    return (isinstance(rs, list) and len(rs) >= 2 and all(isinstance(r, dict) and all(k in r for k in ("native", "diff", "ci95"))
                                                         and isinstance(r["ci95"], (list, tuple)) and len(r["ci95"]) == 2
                                                         for r in rs))


def _num(x):
    return isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))


def reread(old, rs, aim_, per_run_same=False):
    """A row's reading by the one rule from its runs' own numbers; the reading as it stands where the rule does not move it
    (shown, the same, a count that must never rise, a run of one pair, a receipt of its own kind)."""
    o = plain(old)
    if aim_ is None or aim_ == NEVER_MORE:
        return old
    c = _cls(o, aim_)
    if c in ("unjudged", "other"):
        return old
    if c == "same" and not o.startswith(EVEN_FLOOR):
        return old
    if not _well(rs) or not all(_num(r["native"]) and _num(r["diff"]) for r in rs):
        return old
    if any(not (_num(r["ci95"][0]) and _num(r["ci95"][1])) for r in rs):
        return old                                          # a run of one pair: no interval, its own wording stands
    if all(abs(r["diff"]) <= SAME_REL * max(abs(r["native"]), 1e-12) for r in rs):
        return EVEN_SAME
    same = lambda r: per_run_same and abs(r["diff"]) <= SAME_REL * max(abs(r["native"]), 1e-12)
    clear = [(r["ci95"][0] > 0 or r["ci95"][1] < 0) and not same(r) for r in rs]
    return judge_runs([rel_change(r["native"], r["diff"]) for r in rs], clear, aim_)


def _runs_pct(rs):
    out = []
    for r in rs or []:
        if isinstance(r, dict) and _num(r.get("native")) and _num(r.get("diff")):
            ch = rel_change(r["native"], r["diff"])
            out.append(f"{100 * ch:+.2f}%" if math.isfinite(ch) else f"{r['diff']:+.4g} (native 0)")
    return out


def reread_rows_table(md: Path, js: Path):
    """A table of tools/confirm_abc.py (or the capacity test's tools/capacity_abc.py): the Measure table, row by row with the
    JSON twin's rows, then the line of Readings under it."""
    d = json.loads(js.read_text())
    items = list(d["rows"].items())
    lines = md.read_text().split("\n")
    hdr = next((i for i, ln in enumerate(lines) if ln.startswith("| Measure | A | B | C | Reading |")
                or ln.startswith("| Cap (cores) | Measure | A | B | C | Reading |")), None)
    if hdr is None:
        PROBLEMS.append(f"{md}: no Measure table"); return None
    capacity = lines[hdr].startswith("| Cap")
    idx = table_rows(lines, hdr)
    if len(idx) != len(items):
        PROBLEMS.append(f"{md}: {len(idx)} rows in the page, {len(items)} in its JSON twin; not read"); return None
    from tools.confirm_abc import aim_of_row
    moved = False
    for i, (k, row) in zip(idx, items):
        old = last_cell(lines[i])
        a = aim_of(row["aim"], k) if "aim" in row else (HIGHER if capacity else aim_of_row(k))
        if _cls(old, a) != _cls(row.get("reading", old), a):
            PROBLEMS.append(f"{md}: row {k!r} reads {old!r} in the page and {row.get('reading')!r} in its JSON; not read"); continue
        new = reread(old, row.get("runs"), a)
        if plain(new) != plain(old):
            moved = True
            _record(md, "", (lines[i].split("|")[2].strip() if capacity else k), old, new, _runs_pct(row.get("runs")))
            lines[i] = set_last_cell(lines[i], new)
            row["reading"] = plain(new)
    if moved:
        tally = {}
        for i in idx:
            v = last_cell(lines[i]); tally[v] = tally.get(v, 0) + 1
        for j in range(idx[-1] + 1, min(len(lines), idx[-1] + 6)):
            if lines[j].startswith("Readings: "):
                lines[j] = "Readings: " + ", ".join(f"{n} {plain(v)}" for v, n in sorted(tally.items())) + "."
                break
    return "\n".join(lines), (dump_like(d, js.read_text()) if moved else None)


STORE_RUNNER = {"KAFKA": "run_kafka", "PGBENCH": "run_pgbench", "REDIS": "run_redis", "YCSB": "run_ycsb",
                "SYSBENCH": "run_sysbench", "CPU_POWER": "run_cpu_power"}


def _store_aims(stem: str) -> dict:
    """The declared direction of every gauge of a store's runner (its GAUGES), for a twin written before rows kept their aim."""
    import importlib
    mod = next((m for k, m in STORE_RUNNER.items() if k in stem), None)
    if not mod:
        return {}
    return {k: dr for k, _, dr in importlib.import_module(f"tools.{mod}").GAUGES}


def reread_workloads_table(md: Path, js: Path):
    """A table of the stores' *_abc.py tools: a section per workload, row by row with the JSON twin, then the count under it."""
    d = json.loads(js.read_text())
    declared = _store_aims(md.stem)
    wls = d.get("workloads") or {}
    lines = md.read_text().split("\n")
    heads = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    moved = False
    sections = []                                           # (workload, tuning?, row indices, json rows)
    for wl, rows in wls.items():
        h = next((i for i in heads if re.match(rf"## {re.escape(wl)}(?:$|[ :(])", lines[i])), None)
        if h is None:
            PROBLEMS.append(f"{md}: no section for workload {wl!r}"); continue
        nxt = next((i for i in heads if i > h), len(lines))
        t = next((i for i in range(h, nxt) if lines[i].startswith("| Gauge |")), None)
        if t is None:
            PROBLEMS.append(f"{md}: workload {wl!r} has no table"); continue
        idx = table_rows(lines, t)
        items = list(rows.items())
        if len(idx) != len(items):
            PROBLEMS.append(f"{md}: workload {wl!r}: {len(idx)} rows in the page, {len(items)} in its JSON; not read"); continue
        sections.append((wl, "tuning workload" in lines[h] or "(the tuning" in lines[h], idx, items))
        for i, (k, row) in zip(idx, items):
            old = last_cell(lines[i])
            a = aim_of(row["aim"] if "aim" in row else declared.get(k), k)
            if _cls(old, a) != _cls(row.get("reading", old), a):
                PROBLEMS.append(f"{md}: {wl}/{k} reads {old!r} in the page and {row.get('reading')!r} in its JSON; not read"); continue
            new = reread(old, row.get("runs"), a, per_run_same=True)
            if plain(new) != plain(old):
                moved = True
                label = lines[i].rstrip().rstrip("|").rsplit("|", 6)[0].lstrip("|").strip()
                _record(md, wl, label, old, new, _runs_pct(row.get("runs")))
                lines[i] = set_last_cell(lines[i], new)
                row["reading"] = plain(new)
    if moved:
        tally = Tally()
        for wl, tuning, idx, items in sections:
            if tuning:
                continue
            for i, (k, row) in zip(idx, items):
                tally.add(last_cell(lines[i]), row["aim"] if "aim" in row else declared.get(k), k)
        for j, ln in enumerate(lines):
            m = re.match(r"^\*\*Across (\d+) (.+?): \d+ gauge-rows GAIN", ln)
            if m:
                lines[j] = tally.sentence(int(m.group(1)), m.group(2))
    return "\n".join(lines), (dump_like(d, js.read_text()) if moved else None)


# ------------------------------------------------------------------------------------- the deterministic simulators' tables
PCT = re.compile(r"^[+\-−]?\d+\.\d+%$")
ACROSS_RE = re.compile(r"^## Across")


def _across_cell(cell: str):
    m = re.match(r"^(\d+)(?: \((.*)\))?$", cell.strip())
    if not m:
        return None
    return int(m.group(1)), ([x.strip() for x in m.group(2).split(",")] if m.group(2) else [])


def _across_fmt(n, names):
    return f"{n}" + (f" ({', '.join(names)})" if names else "")


def _never_more_labels():
    """The labels of the deterministic simulators' gauges that must never rise: they keep their strict rule, floor or not."""
    out = set()
    for mod in ("run_mujoco", "run_swarm", "pandapower_abc"):
        try:
            import importlib
            m = importlib.import_module(f"tools.{mod}")
        except Exception:                                   # noqa: BLE001  a simulator not installed here: its labels are known below
            continue
        out |= {label for _, label, dr in getattr(m, "GAUGES", ()) if dr == NEVER_MORE}
        if hasattr(m, "COLLISIONS"):
            out.add(m.COLLISIONS[1])
    return out


def reread_deterministic(md: Path):
    """A deterministic simulator's table (CityLearn, MuJoCo, pandapower, the swarms): every judged row whose three printed
    changes are all under 0.5% reads EVEN, under the floor (a gauge that must never rise keeps its strict rule); the Across
    table under it is counted again."""
    strict = _never_more_labels()
    lines = md.read_text().split("\n")
    moved = []                                    # (group header, case, label, old class)
    group = case = ""
    tuning = False
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            group = ln[3:]
            if ACROSS_RE.match(ln):
                group = ""
        elif ln.startswith("### "):
            case = ln[4:].split(":")[0].strip()
            tuning = "tuning" in ln[4:].split(":")[0] or "(the tuning" in ln
        elif ln.startswith("|") and group and case:
            try:
                cells = tail_cells(ln, 4)
            except (IndexError, ValueError):
                continue
            if len(cells) < 4:
                continue
            old = cells[-1]
            c = _cls(old)
            if c not in ("gain", "loss", "given") or "in all three of our runs" not in old:
                continue
            nums = cells[:3]
            if not all(PCT.match(x) for x in nums):
                continue
            sizes = [abs(float(x.replace("−", "-")[:-1])) for x in nums]
            if max(sizes) >= 100 * SIZE_FLOOR:
                continue
            new = even_floor(max(sizes) / 100)
            hdr = next((j for j in range(i - 1, -1, -1) if lines[j].startswith("|") and j + 1 < len(lines)
                        and lines[j + 1].startswith("|---")), None)
            ncell = len(lines[hdr].strip().strip("|").split("|")) if hdr is not None else 5
            label = ln.rstrip().rstrip("|").rsplit("|", ncell - 1)[0].lstrip("|").strip()
            if label in strict:
                continue
            _record(md, f"{group.split(':')[0]} / {case}", label, old, new, nums)
            lines[i] = set_last_cell(ln, new)
            moved.append((group, case, label, c, tuning))
    if not moved:
        return "\n".join(lines), None
    # the Across tables: one row per gauge (and load model), its columns GAIN | LOSS | power given | EVEN | the runs differ
    for group, case, label, c, tuning in moved:
        if tuning:
            continue
        short = re.sub(r"\s*\(`[^`]*`\)\s*$", "", label)
        done = False
        for j, ln in enumerate(lines):
            if not ln.startswith("|"):
                continue
            k = lines[:j]
            if not any(ACROSS_RE.match(x) for x in k):
                continue
            cells = [x.strip() for x in ln.strip().strip("|").split("|")]
            if len(cells) < 6:
                continue
            nums = cells[-5:]
            lab = cells[:-5]
            if lab[-1] != short and lab[-1] != label:
                continue
            if len(lab) == 2 and not group.startswith(lab[0]):
                continue
            parsed = [_across_cell(x) for x in nums]
            if any(p is None for p in parsed):
                continue
            col = 0 if c == "gain" else next((ci for ci in (1, 2) if case in parsed[ci][1]), 1 if c == "loss" else 2)
            n, names = parsed[col]
            if n < 1:
                PROBLEMS.append(f"{md}: the Across count of {short!r} ({['GAIN', 'LOSS', 'power given'][col]}) is already 0"); break
            parsed[col] = (n - 1, [x for x in names if x != case])
            parsed[3] = (parsed[3][0] + 1, [])
            lines[j] = "| " + " | ".join(lab + [_across_fmt(*p) for p in parsed]) + " |"
            done = True
            break
        if not done:
            PROBLEMS.append(f"{md}: no Across row for {short!r} ({group.split(':')[0]}) to count {case} again")
    return "\n".join(lines), None


# ------------------------------------------------------------------------------------------------- the organism reports
def reread_organisms(md: Path, js: Path):
    """An organism report of tools/six_kube_report.py: each organism's line and its rows, from the JSON twin's rows (a report
    written before the rows kept their word has it derived the same way the tool derives it, by the gauge's aim)."""
    from tools import six_kube_report as SK
    d = json.loads(js.read_text())
    orgs = d.get("organisms") or {}
    lines = md.read_text().split("\n")
    heads = [i for i, ln in enumerate(lines) if ln.startswith("### ")]
    moved = False
    for pos, (o, rec) in enumerate(orgs.items()):
        try:
            name = SK.name_of(o)
        except Exception:                                   # noqa: BLE001  a name the tool no longer knows: matched by order
            name = None
        h = next((i for i in heads if name and lines[i].startswith(f"### {name}: ")), heads[pos] if pos < len(heads) else None)
        if h is None:
            PROBLEMS.append(f"{md}: no section line for {o!r}"); continue
        rows = {k: dict(v) for k, v in (rec.get("rows") or {}).items()}
        need = ("n", "native", "diff", "lo", "hi")
        if not all(all(x in v for x in need) for v in rows.values()):
            PROBLEMS.append(f"{md}: {o!r} rows lack the fields the rule reads; not read"); continue
        for k, v in rows.items():
            if "word" not in v:
                v["word"] = SK.gel_word(v["diff"] < 0, SK.aim_of(k))
        t = next((i for i in range(h, min(len(lines), h + 8)) if lines[i].startswith("| Gauge |")), None)
        if t is not None:
            idx = table_rows(lines, t)
            if len(idx) != len(rows):
                PROBLEMS.append(f"{md}: {o!r}: {len(idx)} rows in the page, {len(rows)} in its JSON; rows not read")
            else:
                for i, (k, v) in zip(idx, rows.items()):
                    old = last_cell(lines[i])
                    if _cls(old, SK.aim_of(k)) not in ("noise", "gain", "loss", "given") and not old.startswith(EVEN_FLOOR):
                        continue
                    if v.get("neutral") or k in SK.SHOWN or v.get("same"):
                        continue
                    new = SK.row_reading(v)
                    if new != old:
                        moved = True
                        pct = v.get("pct")
                        _record(md, o, SK.LABEL.get(k, k), old, new,
                                [f"{pct:+.1f}% ({v['lo']:+.4g} to {v['hi']:+.4g})" if _num(pct) else f"{v['diff']:+.4g}"])
                        lines[i] = set_last_cell(lines[i], new)
        if rec.get("repetitions", 0) >= 2:
            judged = {k: v for k, v in rows.items() if not v.get("neutral") and k not in SK.SHOWN and not v.get("same")}
            head, _, rest = lines[h].partition(": ")
            facts = lambda t: "".join("; " + f for f in re.findall(r"; ((?:OFF THE CLOCK|INVALID)[^;]*)", t))   # kept as recorded
            nv = SK.organism_line(judged)
            new_line = f"{head}: {nv}{facts(rest)}"
            if new_line != lines[h]:
                moved = True
                _record(md, o, "the organism's line", re.split(r"; (?:OFF THE CLOCK|INVALID)", rest)[0], nv, [])
                lines[h] = new_line
                rec["verdict"] = nv + facts(rec.get("verdict", ""))
    return "\n".join(lines), (dump_like(d, js.read_text()) if moved else None)


# ------------------------------------------------------------------------------------------------------- the model records
def _model_aims():
    from tools import toy_gate as TG
    aims = {}
    for m in (TG.GAUGES, TG.PACE_GAUGES, TG.CONVEY_GAUGES, TG.CONVEY_BATCH_GAUGES, TG.CARD_GAUGES):
        aims.update(m)
    return aims


def model_word(leaf, aim, spent):
    """A model's paired reading by the one rule (tools/toy_gate.model_word) from its own mean, interval and relative change."""
    from tools.toy_gate import model_word as mw
    w = leaf.get("word", "")
    if w.startswith("EVEN (identical)"):
        return w
    rel = leaf.get("relative")
    m = leaf["mean_change"]
    lo, hi = leaf["ci95"]
    if rel is None or (isinstance(rel, float) and rel != rel):
        base = 0.0
    else:
        base = m / rel if rel else 1.0
    if rel == 0:
        m, base = 0.0, 1.0
    return mw(m, base, not (lo <= 0.0 <= hi), aim, spent)


def _walk_leaves(x, path, aims, out):
    if isinstance(x, dict):
        if {"mean_change", "ci95", "word"} <= set(x):
            g = next((p for p in reversed(path) if p in aims), None)
            out.append((path, x, g))
            return
        for k, v in x.items():
            _walk_leaves(v, path + [k], aims, out)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            _walk_leaves(v, path + [i], aims, out)


def _cell_new(d):
    if d is None:
        return ""
    return f"{by_word(100 * d['relative'], d['word'], digits=2)} {d['word']}" if _num(d.get("relative")) else d["word"]


def _cell_raw(d):
    if d is None:
        return ""
    return f"{100 * d['relative']:+.2f}% {d['word']}" if _num(d.get("relative")) else d["word"]


def _gate_rows(t):
    """(the row's gauge, its leaves in column order, the row's fixed numbers) for every row a toy's page prints."""
    out = []
    if "gauges" in t:
        for g, x in t["gauges"].items():
            if all(k in x for k in ("cand_vs_base", "base_vs_native", "cand_vs_native")):
                out.append((f"| {g} | {x['native']:.3f} | {x['base']:.3f} | {x['cand']:.3f} | ",
                            [x["cand_vs_base"], x["base_vs_native"], x["cand_vs_native"]]))
    first = t.get("candidate_as_first_pushed")
    if first:
        for g, x in first["gauges"].items():
            out.append((f"| {g} | {x['native']:.3f} | {x['base']:.3f} | {x['cand']:.3f} | ", [x["cand_vs_base"], x["cand_vs_native"]]))
    if "reference_rows" in t:
        for g, x in t["reference_rows"].items():
            out.append((f"| {g} | {x['native']:.3f} | {x['ref']:.3f} | ", [x["ref_vs_native"]]))
        for per, rows in t.get("against_reference", {}).items():
            for g, x in rows.items():
                out.append((f"| {g} | {x['native']:.3f} | {x['ref']:.3f} | {x['pace']:.3f} | ", [x["pace_vs_ref"], x["pace_vs_native"]]))
    return out


def reread_toy_gate(md: Path, js: Path):
    """A record of tools/toy_gate.py: every paired reading in the JSON again by the rule, and every printed row whose words
    moved printed again (the number wearing its word's sign)."""
    import copy
    d = json.loads(js.read_text())
    old = copy.deepcopy(d)
    aims = _model_aims()
    leaves = []
    _walk_leaves(d, [], aims, leaves)
    moved = False
    for path, leaf, g in leaves:
        if g is None:
            if not leaf["word"].startswith("EVEN (identical)"):
                PROBLEMS.append(f"{js}: no aim known for the reading at {'/'.join(map(str, path))}")
            continue
        aim, spent = aims[g]
        new = model_word(leaf, aim, spent)
        if new != leaf["word"]:
            moved = True
            toy = path[1] if len(path) > 1 and path[0] == "toys" else ""
            _record(md, f"{toy} {'/'.join(map(str, path[2:]))}".strip(), g, leaf["word"], new,
                    [f"{100 * leaf['relative']:+.2f}%" if _num(leaf.get("relative")) else "n/a",
                     f"interval {leaf['ci95'][0]:+.4g} to {leaf['ci95'][1]:+.4g}"])
            leaf["word"] = new
    if not moved:
        return None
    lines = md.read_text().split("\n")
    for toy in d.get("toys", {}):
        h = next((i for i, ln in enumerate(lines) if ln.startswith(f"## {toy}") and
                  (ln == f"## {toy}" or ln[len(f"## {toy}")] in " (")), None)
        if h is None:
            continue
        nxt = next((i for i in range(h + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        for (prefix, new_leaves), (_, old_leaves) in zip(_gate_rows(d["toys"][toy]), _gate_rows(old["toys"][toy])):
            if [x and x["word"] for x in new_leaves] == [x and x["word"] for x in old_leaves]:
                continue
            cand = {prefix + " | ".join(f(x) for x in old_leaves) + " |" for f in (_cell_new, _cell_raw)}
            hit = next((i for i in range(h, nxt) if lines[i] in cand), None)
            if hit is None:
                PROBLEMS.append(f"{md}: {toy}: the row {prefix.split('|')[1].strip()!r} is not printed as its JSON reads; not rewritten")
                continue
            lines[hit] = prefix + " | ".join(_cell_new(x) for x in new_leaves) + " |"
    return "\n".join(lines), dump_like(d, js.read_text())


def reread_ladder(md: Path, js: Path):
    """The heartbeat dial's record (tools/beat_ladder.py): every paired reading again by the rule, the page rendered again by the
    tool from its JSON (the page as first written renders from it byte for byte)."""
    from tools import beat_ladder as BL
    d = json.loads(js.read_text())
    aims = _model_aims()
    leaves = []
    _walk_leaves(d, [], aims, leaves)
    moved = False
    for path, leaf, g in leaves:
        if g is None:
            continue
        aim, spent = aims[g]
        new = model_word(leaf, aim, spent)
        if new != leaf["word"]:
            moved = True
            _record(md, "/".join(map(str, path[1:])), g, leaf["word"], new,
                    [f"{100 * leaf['relative']:+.2f}%" if _num(leaf.get("relative")) else "n/a"])
            leaf["word"] = new
    if not moved:
        return None
    nan = json.loads(json.dumps(d))

    def fix(x):
        if isinstance(x, dict):
            if "word" in x and "relative" in x and x["relative"] is None:
                x["relative"] = float("nan")
            for v in x.values():
                fix(v)
        elif isinstance(x, list):
            for v in x:
                fix(v)
    fix(nan)
    tmp = md.with_suffix(".reread.md")
    BL.render(nan, nan["sources"], str(tmp))
    text = tmp.read_text(); tmp.unlink()
    return text, dump_like(d, js.read_text())


def reread_solo(md: Path, js: Path):
    """Omni-Compass by itself in our model (tools/solo_study.py): the pairs' readings again by the rule, their rows printed again."""
    from tools import solo_study as SS
    d = json.loads(js.read_text())
    aims = _model_aims()
    lines = md.read_text().split("\n")
    pct = lambda r: (by_word(100 * r["relative"], r["word"]) if _num(r.get("relative")) else "—")
    iv = lambda r, b: interval_by_word(100 * r["ci95"][0] / b, 100 * r["ci95"][1] / b, r["word"]) if b else "—"
    moved = False
    for x, y in SS.PAIRS:
        h = next((i for i, ln in enumerate(lines) if ln == f"## {SS.NAME[x]} against {SS.NAME[y]}"), None)
        for g, rec in d["gauges"].items():
            r = rec.get(f"{x}_vs_{y}")
            if not r or g not in aims:
                continue
            aim, spent = aims[g]
            new = model_word(r, aim, spent)
            if new == r["word"]:
                continue
            b = rec["means"][y]
            oldrow = f"| {SS.GAUGE_NAME[g]} | {pct(r)} | {iv(r, b)} | **{r['word']}** |"
            _record(md, f"{SS.NAME[x]} against {SS.NAME[y]}", g, r["word"], new,
                    [f"{100 * r['relative']:+.2f}%" if _num(r.get("relative")) else "n/a"])
            r["word"] = new
            moved = True
            newrow = f"| {SS.GAUGE_NAME[g]} | {pct(r)} | {iv(r, b)} | **{r['word']}** |"
            hit = next((i for i in range(h or 0, len(lines)) if lines[i] == oldrow), None) if h is not None else None
            if hit is None:
                PROBLEMS.append(f"{md}: the row {SS.GAUGE_NAME[g]!r} under {SS.NAME[x]} against {SS.NAME[y]} is not printed as its JSON reads")
                continue
            lines[hit] = newrow
    if not moved:
        return None
    return "\n".join(lines), dump_like(d, js.read_text())


# ------------------------------------------------------------------------------------------------------------------ all
DETERMINISTIC = ("CITYLEARN", "MUJOCO", "PANDAPOWER", "SWARM")


def plan(root: Path = ROOT):
    """Every table this tool reads again: (kind, page, JSON twin or None)."""
    out = []
    for md in sorted((root / "results" / "live").glob("*.md")):
        js = md.with_suffix(".json")
        if any(s in md.stem for s in DETERMINISTIC) and not js.exists():
            out.append(("deterministic", md, None)); continue
        if not js.exists():
            continue
        try:
            d = json.loads(js.read_text())
        except ValueError:
            continue
        if not isinstance(d, dict):
            continue
        if "rows" in d and isinstance(d["rows"], dict):
            out.append(("rows", md, js))
        elif "workloads" in d and isinstance(d["workloads"], dict) and "runs" in d:
            out.append(("workloads", md, js))
        elif "organisms" in d:
            out.append(("organisms", md, js))
    for md in sorted((root / "results" / "toy_gate").glob("*.md")):
        js = md.with_suffix(".json")
        if not js.exists():
            continue
        if md.stem.endswith("LADDER"):
            out.append(("ladder", md, js))
        elif md.stem.startswith("SOLO_"):
            out.append(("solo", md, js))
        elif md.stem != "HEARTBEAT_SWEEP":
            d = json.loads(js.read_text())
            if "toys" in d:
                out.append(("toy_gate", md, js))
    return out


HANDLERS = {"rows": reread_rows_table, "workloads": reread_workloads_table, "organisms": reread_organisms,
            "toy_gate": reread_toy_gate, "ladder": reread_ladder, "solo": reread_solo}


def run(root: Path = ROOT, write: bool = True):
    """Read every table again; returns the pages and twins that changed (or would)."""
    CHANGES.clear(); PROBLEMS.clear()
    changed = []
    for kind, md, js in plan(root):
        before_md = md.read_text()
        before_js = js.read_text() if js else None
        res = reread_deterministic(md) if kind == "deterministic" else HANDLERS[kind](md, js)
        text, jtext = (res if res else (before_md, None))
        if kind in ("rows", "workloads", "organisms", "deterministic"):
            text = with_blocks(text, exact=js is not None)
        elif text != before_md or NOTE_BEGIN in text:
            text = with_blocks(text, exact=True, model=True)
        if text != before_md or (jtext is not None and jtext != before_js):
            changed.append(str(md.relative_to(root)))
            if write:
                md.write_text(text)
                if jtext is not None and jtext != before_js:
                    js.write_text(jtext)
    # the heartbeat sweep's record is its tool's own reading of its committed runs: written again from them
    hs_md = root / "results" / "toy_gate" / "HEARTBEAT_SWEEP.md"
    runs = root / "results" / "toy_gate" / "HEARTBEAT_SWEEP_RUNS.jsonl"
    if runs.exists() and hs_md.exists():
        import tempfile
        from tools import heartbeat_sweep as HS
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "HEARTBEAT_SWEEP.md"
            HS.table(str(runs), str(out))
            new_md, new_js = out.read_text(encoding="utf-8"), out.with_suffix(".json").read_text(encoding="utf-8")
        if new_md != hs_md.read_text(encoding="utf-8") or new_js != hs_md.with_suffix(".json").read_text(encoding="utf-8"):
            changed.append(str(hs_md.relative_to(root)))
            _record_sweep(hs_md, new_js)
            if write:
                hs_md.write_text(new_md, encoding="utf-8")
                hs_md.with_suffix(".json").write_text(new_js, encoding="utf-8")
    return changed


def _record_sweep(md: Path, new_js: str):
    """The heartbeat sweep's readings that moved, from its record before and after."""
    try:
        old = json.loads(md.with_suffix(".json").read_text(encoding="utf-8")); new = json.loads(new_js)
    except ValueError:
        return
    lo, ln = [], []
    _walk_leaves(old, [], _model_aims(), lo); _walk_leaves(new, [], _model_aims(), ln)
    for (p, a, g), (_, b, _) in zip(lo, ln):
        if a["word"] != b["word"]:
            _record(md, "/".join(map(str, p)), g or str(p[-2] if len(p) > 1 else p), a["word"], b["word"],
                    [f"{100 * a['relative']:+.2f}%" if _num(a.get("relative")) else "n/a"])


WORD = {"gain": "GAIN", "loss": "LOSS", "given": "power given", "noise": "EVEN", "same": "EVEN", "disagree": "the runs disagree",
        "unjudged": "shown", "other": "other"}


def write_ledger(report: Path, out: Path, root: Path = ROOT):
    """The ledger of a reading again (results/REREAD_KEY.md and its JSON): how many readings moved, from which word to which,
    every row that now reads LOSS and every LOSS that now reads EVEN, under the floor, named with its runs; the rest counted
    page by page (every row is in the JSON)."""
    from tools.legal import stamp
    from tools.readings import OWN_RUNS
    rep = json.loads(Path(report).read_text())
    rows = [dict(c, file=str(Path(c["file"]).resolve().relative_to(root.resolve()))) for c in rep["changes"]
            if c["gauge"] != "the organism's line"]
    lines_moved = [c for c in rep["changes"] if c["gauge"] == "the organism's line"]
    model = lambda c: c["file"].startswith("results/toy_gate/")
    pair = lambda c: (WORD[c["old_class"]], WORD[c["new_class"]])
    L = ["# Every reading that moved under the rule of 24 October 2026", "",
         "The founder's order of 24 October 2026: \"Any gauge that gives anything over a 0.5 percent change either way is a change. I "
         "don't want to see even on shit that shows a 0.5% change up or down, it has to show its loss or gain.\" The rule is written "
         "once (`tools/readings.py` judge_runs and judge_one) and every published table was read again by it (`tools/reread_key.py`), "
         "from each row's own numbers; every row, run and number is kept. This page counts what moved and names every row that now "
         "reads LOSS, and every LOSS that now reads EVEN under the 0.5% floor (the floor of 20 October, now applied in every table: "
         "the stores' and the deterministic simulators' tools had not applied it). Every reading whose word moved is in the JSON "
         "twin, one a line.", "",
         OWN_RUNS, ""]
    for title, sel in (("The three-run tables and organism reports (`results/live/`)", lambda c: not model(c)),
                       ("Our own models (`results/toy_gate/`, evidence class S, never a benchmark result)", model)):
        xs = [c for c in rows if sel(c)]
        cnt = {}
        for c in xs:
            cnt[pair(c)] = cnt.get(pair(c), 0) + 1
        L += [f"## {title}", "", "| Before | Now | Readings |", "|---|---|---:|"]
        L += [f"| {a} | {b} | {n:,} |" for (a, b), n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))]
        L.append("")
    def table(xs):
        out = ["| Page | Where | Gauge | Before | Now | The runs' changes |", "|---|---|---|---|---|---|"]
        for c in xs:
            out.append(f"| `{c['file']}` | {c['where'] or ' '} | {c['gauge']} | {c['old']} | {c['new']} | {'; '.join(c['runs'])} |")
        return out + [""]
    loss = [c for c in rows if c["new_class"] == "loss"]
    L += ["## Every row that now reads LOSS", "",
          f"{sum(not model(c) for c in loss):,} in the three-run tables and organism reports, {sum(model(c) for c in loss):,} in our own "
          "models. Each one's cause is looked for as every LOSS's is (our own wiring first, then native's setup, then the scoring), and "
          "every one on the engine that stands goes on the next version's list.", ""]
    L += table([c for c in loss if not model(c)] + [c for c in loss if model(c)])
    hid = [c for c in rows if c["old_class"] == "loss" and c["new_class"] in ("same", "noise")]
    L += ["## Every LOSS that now reads EVEN, under the floor", "",
          "A LOSS whose change was under 0.5% in every run now reads EVEN, under the floor, by the founder's floor; each is named "
          "here so none is lost from sight.", ""]
    L += table(hid)
    per = {}
    for c in rows:
        k = c["file"]
        per.setdefault(k, {})
        per[k][pair(c)] = per[k].get(pair(c), 0) + 1
    L += ["## Page by page", "", "| Page | What moved |", "|---|---|"]
    for k in sorted(per):
        L.append(f"| `{k}` | " + "; ".join(f"{n} {a} to {b}" for (a, b), n in sorted(per[k].items(), key=lambda kv: -kv[1])) + " |")
    L += ["", f"The organism reports' lines (the count of words under each organism) were written again too: {len(lines_moved)} lines.", ""]
    Path(out).with_suffix(".md").write_text("\n".join(stamp(L)) + "\n")
    moved = [{k: c[k] for k in ("file", "where", "gauge", "old", "new", "runs")} for c in rows if pair(c)[0] != pair(c)[1]]
    Path(out).with_suffix(".json").write_text(
        "{\"changes\": [\n" + ",\n".join(json.dumps(c, ensure_ascii=False) for c in moved) + "\n],\n\"problems\": "
        + json.dumps(rep.get("problems", []), ensure_ascii=False) + "}\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if any table would change")
    ap.add_argument("--report", help="write every reading that changed, and every table not read, as JSON to this file")
    ap.add_argument("--ledger", nargs=2, metavar=("REPORT.json", "OUT"),
                    help="write the ledger page OUT.md and OUT.json from a report a reading again wrote")
    a = ap.parse_args(argv)
    if a.ledger:
        write_ledger(Path(a.ledger[0]), Path(a.ledger[1]))
        return 0
    changed = run(write=not a.check)
    if a.report:
        Path(a.report).write_text(json.dumps({"changes": CHANGES, "problems": PROBLEMS}, indent=1) + "\n")
    by = {}
    for c in CHANGES:
        by[(c["old_class"], c["new_class"])] = by.get((c["old_class"], c["new_class"]), 0) + 1
    for (o, n), k in sorted(by.items()):
        print(f"{k:5d}  {o} -> {n}")
    for p in PROBLEMS:
        print(f"not read: {p}")
    if a.check:
        for p in changed:
            print(f"{p}: not yet read by the rule of 24 October 2026 (python3 tools/reread_key.py)")
        return 1 if changed else 0
    print(f"{len(changed)} pages read again by the rule of 24 October 2026")
    return 0


if __name__ == "__main__":
    sys.exit(main())
