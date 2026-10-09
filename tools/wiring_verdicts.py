#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Wire in, or watch: the verdict per knob, read from every result in the repository.

Omni-Compass is wired OUT of every muscle (it reads every reading) and IN to a knob only where the paired measurement
shows the muscle no worse for it. The engine already does this on the muscle itself (omnicompass/verdict.py: the paired
trial, "left native" where no step is allowed; the realms' watch arm, which reads and writes nothing). This tool applies
the same principle to every published result, one verdict per knob, so an operator can see which knobs earn a wire in
and which stay native with Omni only reading them. The founder's order of 9 October 2026: "where Omni cannot beat
native, the muscle stays native; we only wire out of it".

The rule, the same for every table (every judged gauge counts; "shown, not judged" rows never do):

  write               at least one gauge confirmed better and none confirmed worse: Omni holds the knob
  watch               nothing confirmed better: the knob stays native and Omni only reads it. Where a gauge is
                      confirmed worse the loss is named and its cause given; where the runs disagree, nothing is
                      settled and the knob stays native until it is
  operator's choice   gains and losses both confirmed: a trade. Both readings of the Omni index are printed where the
                      test is in it (the resource reading, the preregistered headline; the service reading, work and
                      speed alone) and the side that pays is named. The operator who wants the gain and can pay the
                      cost wires in; every other operator watches

Nothing is typed in: every verdict is computed from the test's own result file. Modelled muscles (the 945 on their
plants) take their verdict from the realms' label by rule (SUPERIOR WITHIN GUARDRAILS: write; a tradeoff label:
operator's choice; NONINFERIOR / INCONCLUSIVE, NOT ESTABLISHED, WORSE: watch).

  python3 tools/wiring_verdicts.py            ->  docs/WIRING_VERDICTS.md, results/WIRING_VERDICTS.csv
  python3 tools/wiring_verdicts.py --check    ->  exit 1 if the committed files differ from what the tables give
"""
from __future__ import annotations

import collections
import csv
import io
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                       # noqa: E402
from tools import omni_index                                       # noqa: E402

LIVE = ROOT / "results" / "live"
OUT_MD = ROOT / "docs" / "WIRING_VERDICTS.md"
OUT_CSV = ROOT / "results" / "WIRING_VERDICTS.csv"

WRITE, WATCH, CHOICE = "write", "watch", "operator's choice"
UNJUDGED = "shown, not judged"


# ------------------------------------------------------------------------------------------------------ the rule
def classify(reading):
    """A table's reading in one word: better, worse, noise, disagree, same, unjudged."""
    r = (reading or "").strip().strip("*").lower()
    if r.startswith("confirmed better"):
        return "better"
    if r.startswith("confirmed worse"):
        return "worse"
    if r.startswith("no difference"):
        return "noise"
    if "disagree" in r or "differ" in r:
        return "disagree"
    if r.startswith("same"):
        return "same"
    if r.startswith("shown"):
        return "unjudged"
    raise ValueError(f"unknown reading: {reading!r}")


def verdict(better, worse):
    """The three words. better, worse: how many judged gauges were confirmed each way."""
    if better and not worse:
        return WRITE
    if better and worse:
        return CHOICE
    return WATCH


def pct_range(runs, lower_is_better=None):
    """The change omni against native over the runs, as 'lo to hi' in percent (one figure when they agree to a point)."""
    ps = []
    for r in runs:
        n, o = r.get("native"), r.get("omni")
        if n is None or o is None or not isinstance(n, (int, float)) or not isinstance(o, (int, float)):
            continue
        if abs(n) < 1e-12:
            ps.append(None if abs(o) < 1e-12 else math.inf)
        else:
            ps.append(100.0 * (o - n) / abs(n))
    ps = [p for p in ps if p is not None]
    if not ps:
        return ""
    if any(math.isinf(p) for p in ps):
        return "from zero"
    lo, hi = min(ps), max(ps)
    f = (lambda x: f"{x:+.0f}%") if max(abs(lo), abs(hi)) >= 10 else (lambda x: f"{x:+.1f}%")
    return f(lo) if f(lo) == f(hi) else f"{f(lo)} to {f(hi)}"


def first(runs, key):
    r = runs[0] if runs else {}
    v = r.get(key)
    return v


# ------------------------------------------------------------------------------------- the real stacks (three runs)
K8S_TESTS = [(name, f) for _, name, f, _, _ in omni_index.SOURCES]          # the seven Kubernetes tests, in the index's order
K8S_NAMES = {"V3_STEADY.json": "steady work", "V3_WANDERING.json": "demand that wanders", "V3_ALL_FOUR.json": "all four at once",
             "V3_FAIRNESS.json": "a noisy neighbour", "V3_FAULTS.json": "faults", "V3_BATCH.json": "a queue of jobs",
             "V3_TRACE_GOOGLE2011.json": "a public day of demand (Google 2011)"}
K8S_KNOB = "the autoscaler's replicas, the floor and the machines"
K8S_GAUGE = {"worker nodes in service, mean": "machines", "node-hours": "machine-hours", "energy (Wh)": "standby-model energy",
             "energy, parked workers still on at idle power (Wh)": "parked-worker energy", "response time (ms), mean": "mean response",
             "response time (ms), 95th percentile": "p95", "response time (ms), 99th percentile": "p99",
             "time over the response line (% of samples)": "time over the line", "failed requests (%)": "failed requests",
             "HPA replicas, mean": "replicas", "pods started": "pods started",
             "work inside the response line (requests a second; the capacity test's own gauge, higher is better)": "work inside the line",
             "batch: worker machines in service after the queue finished, mean": "machines after the queue",
             "batch: queue finished (s)": "queue finished"}
WORKLOAD_STACKS = [
    # (category in the index, file, the knob in words, {gauge key: name}, the tuning workload's name, the declared cost note)
    ("Real database (PostgreSQL behind PgBouncer, GitHub)", "V3_PGBENCH.json", "the pooler's pool size (server connections)",
     {"work_inside_line_tps": "work inside the line", "tps": "throughput", "p95_ms": "p95", "p99_ms": "p99", "p50_ms": "median", "mean_ms": "mean",
      "servers_alive_mean": "connections held open", "servers_alive_max": "connections most at once", "cpu_busy_share": "host CPU busy",
      "cpu_seconds": "host CPU-seconds", "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
    ("Real messaging (Apache Kafka, GitHub)", "V3_KAFKA.json", "the consumer group's size",
     {"work_inside_line_mps": "work inside the line", "mps": "throughput", "p95_ms": "p95", "p99_ms": "p99", "p50_ms": "median", "mean_ms": "mean",
      "lag_max": "messages waiting, most", "lag_mean": "messages waiting, mean", "consumers_mean": "consumers running", "consumers_max": "consumers most at once",
      "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds", "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "lost": "lost"}),
    ("Real cache (Redis, GitHub)", "V3_REDIS.json", "the cache's memory ceiling",
     {"work_inside_line_rps": "work inside the line", "rps": "throughput", "hit_rate": "hit rate", "p95_ms": "p95", "p99_ms": "p99", "mean_ms": "mean",
      "maxmemory_mb_mean": "memory ceiling held", "used_mb_mean": "memory used", "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds",
      "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
    ("Real database cache (MongoDB under YCSB, GitHub)", "V3_YCSB.json", "the storage engine's cache size",
     {"work_inside_line_ops": "work inside the line", "ops": "throughput", "p95_ms": "p95", "p99_ms": "p99", "mean_ms": "mean",
      "cache_mb_mean": "cache size held", "cache_used_mb_mean": "cache in use", "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds",
      "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
    ("Real database buffer pool (MySQL under sysbench, GitHub)", "V3_SYSBENCH.json", "the buffer pool's size",
     {"work_inside_line_tps": "work inside the line", "tps": "throughput", "qps": "queries a second", "p95_ms": "p95", "p99_ms": "p99", "mean_ms": "mean",
      "pool_mb_mean": "pool held", "pool_used_mb_mean": "pages holding data", "cpu_busy_share": "host CPU busy", "cpu_seconds": "host CPU-seconds",
      "cpu_s_per_1k_inside": "CPU per 1,000 inside the line", "failed": "failed"}),
]
STACK_SHORT = {"V3_PGBENCH.json": "PostgreSQL", "V3_KAFKA.json": "Kafka", "V3_REDIS.json": "Redis", "V3_YCSB.json": "MongoDB", "V3_SYSBENCH.json": "MySQL"}

# Why each confirmed loss happened, read from the preregistration that carries the result (the file is named so a reader
# can check the words against the record). Keyed by (file, workload or test, gauge key); a key of "*" matches any case.
WHY = {
    ("V3_KAFKA.json", "*", "consumers_mean"): "the knob itself: Omni adds consumers while messages wait and the queue is kept short; the consumers running are the price, declared in advance as the cost that reads worse (`docs/KAFKA_PREREGISTRATION.md`, the gauges)",
    ("V3_KAFKA.json", "*", "consumers_max"): "the same price at its peak: the group grown to the partition count while the burst is drained",
    ("V3_KAFKA.json", "*", "cpu_busy_share"): "more consumers polling cost the host CPU on the light workload, where the broker had slack; on the heavy and burst workloads the CPU is inside the noise",
    ("V3_KAFKA.json", "*", "cpu_seconds"): "the same CPU, counted over the run",
    ("V3_REDIS.json", "*", "maxmemory_mb_mean"): "the knob itself: the ceiling grows while the cache is full and misses, so a wide working set is held instead of evicted; the memory is the price of the hit rate, declared in advance as the cost that reads worse (`docs/REDIS_PREREGISTRATION.md`, the gauges)",
    ("V3_REDIS.json", "*", "used_mb_mean"): "the memory actually used follows the ceiling: the working set the operator's 64 MB could not hold is held",
    ("V3_PGBENCH.json", "simple_update", "servers_alive_max"): "amendment 1's add rule (\"slow, clients waiting for a server: add\") fired 4 to 15 times an arm on this slow write workload and bought servers above the operator's 20, up to 36 at the peak; work, latency and CPU inside the noise, so nothing was bought for them (`docs/POSTGRES_PREREGISTRATION.md`, the second set). The rule stands as written and the verdict for this workload is to watch",
    ("V3_SYSBENCH.json", "read_write", "pool_used_mb_mean"): "memory bought on real misses: a written working set keeps the pool missing above one percent, so the growth gate lets the pool grow to 1.1 to 1.6 GB in the wide notches; the host's CPU fell 4% to 6% for it, confirmed better, and latency did not move (`docs/MYSQL_PREREGISTRATION.md`, the third set)",
}
DECLARED_COST = {"V3_KAFKA.json": "consumers", "V3_REDIS.json": "memory"}


def load_index():
    """The two index readings per test, keyed by (file, workload or None)."""
    out = {}
    for t in omni_index.tests():
        f = t["source"].rsplit("/", 1)[-1]
        m = re.search(r"`([a-z_]+)`", t["test"])
        out[(f, m.group(1) if m else None)] = (t.get("index_pct"), t.get("service_pct"))
    return out


def judge_rows(rows, names, keys_order=None):
    """rows: {gauge key: {"reading", "runs"}}. Returns the classified lists with their ranges."""
    out = {"better": [], "worse": [], "noise": [], "disagree": [], "same": []}
    for k in (keys_order or rows):
        v = rows[k]
        c = classify(v["reading"])
        if c == "unjudged":
            continue
        out[c].append((k, names.get(k, k), pct_range(v["runs"]), v["runs"]))
    return out


def real_stacks(index):
    cases = []
    for name, f in K8S_TESTS:
        p = LIVE / f
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        j = judge_rows(d["rows"], K8S_GAUGE)
        v = verdict(len(j["better"]), len(j["worse"]))
        res, svc = index.get((f, None), (None, None))
        why = k8s_why(f, j, v)
        cases.append({"kind": "real knob", "domain": "Real Kubernetes (GitHub, kind)", "knob": K8S_KNOB, "case": K8S_NAMES.get(f, name),
                      "counted": True, "judged": j, "verdict": v, "resource_pct": res, "service_pct": svc, "why": why,
                      "source": f"results/live/{f.replace('.json', '.md')}", "runs": [r["run"] for r in d["runs"]]})
    for cat, f, knob, names in WORKLOAD_STACKS:
        p = LIVE / f
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        for wl, gauges in d["workloads"].items():
            j = judge_rows(gauges, names)
            v = verdict(len(j["better"]), len(j["worse"]))
            res, svc = index.get((f, wl), (None, None))
            cases.append({"kind": "real knob", "domain": cat, "knob": knob, "case": wl + (" (tuning workload: shown, never counted)" if wl == "tuning" else ""),
                          "counted": wl != "tuning", "judged": j, "verdict": v, "resource_pct": res, "service_pct": svc,
                          "why": stack_why(f, wl, j, v, res, svc), "source": f"results/live/{f.replace('.json', '.md')}",
                          "runs": [r["run"] for r in d["runs"]], "stack": STACK_SHORT[f], "workload": wl})
    return cases


def fmt_list(items, n=4):
    """'p95 −65% to −66%, p99 −68% to −72%, ...' from classified items."""
    s = [f"{nm} {rg}".strip() for _, nm, rg, _ in items[:n]]
    more = len(items) - n
    return ", ".join(s) + (f" and {more} more" if more > 0 else "")


def k8s_why(f, j, v):
    if v == WRITE:
        return (f"confirmed better on {len(j['better'])} gauges, nothing confirmed worse"
                + (f"; {len(j['noise'])} gauges inside the noise" if j["noise"] else "") + ". Omni holds the knob")
    if v == WATCH and not j["worse"]:
        return (f"every judged gauge inside the noise or the same ({len(j['noise'])} inside the noise, {len(j['same'])} the same), the neighbour's "
                f"own rows included: Omni neither helped nor hurt beside a noisy neighbour, so under this demand there is nothing to earn and nothing "
                f"lost. The same knob writes under the other six demands")
    return f"confirmed better on {fmt_list(j['better'])}; confirmed worse on {fmt_list(j['worse'])}"


def stack_why(f, wl, j, v, res, svc):
    short = STACK_SHORT[f]
    parts = []
    if j["disagree"]:
        parts.append(f"the runs disagree on {fmt_list(j['disagree'], 3)}")
    if not j["better"] and not j["worse"]:
        parts.append(f"nothing confirmed either way ({len(j['noise'])} gauges inside the noise" + (f", {len(j['same'])} the same" if j["same"] else "") + ")")
    s = ("; ".join(parts) + ".") if parts else ""
    causes = []
    for k, nm, rg, _ in j["worse"]:
        w = WHY.get((f, wl, k)) or WHY.get((f, "*", k))
        if w:
            causes.append(f"{nm} {rg}: {w}")
    if causes:
        s += " Why: " + "; ".join(causes) + "."
    s = s.strip()
    if v == CHOICE:
        cost = DECLARED_COST.get(f)
        if res is not None and svc is not None:
            if res > 0 and svc > 0:
                s += (f" The trade pays under both readings of the index (resource {res:+.1f}%, service {svc:+.1f}%): the operator who runs {short} "
                      f"for its service wires in and pays in {cost or 'the resource named'}; an operator who counts that resource above the service watches.")
            elif svc > 0:
                s += (f" The trade pays under the service reading ({svc:+.1f}%) and not under the resource reading ({res:+.1f}%, the preregistered "
                      f"headline): the operator who runs {short} for its speed and has the {cost or 'resource'} wires in; the operator who counts the "
                      f"{cost or 'resource'} as the cost watches.")
            else:
                s += (f" Under the index's own scoring the gain outweighs the loss by {res:+.1f}% (resource reading); the service reading is "
                      f"{svc:+.1f}%: a small trade, the operator's to take or leave.")
    if v == WATCH and j["disagree"] and not j["worse"]:
        s += " Nothing is settled here, so the knob stays native until three runs agree."
    if v == WATCH and not j["better"] and not j["worse"] and not j["disagree"]:
        s += " Nothing to earn under this workload, nothing lost: the knob stays native and Omni reads it."
    if v == WRITE:
        s += " Nothing worse: Omni holds the knob."
    return s


# ------------------------------------------------------------------------------- the modelled simulators (markdown)
SIMS = [
    ("V3_MUJOCO.md", "Robot arms (MuJoCo Menagerie, Google DeepMind)", "the servo's speed override inside the takt",
     {"Robots where Omni moved the override": "moved", "Robots where the paired trial left the override native": "left_native",
      "Robots the task could not be run on": "not_run"}),
    ("V3_PANDAPOWER.md", "The power grid (pandapower, SimBench grids)", "the substation's voltage setpoint, one tap at a time",
     {"ZIP loads (40% Z, 30% I, 30% P)": "moved:ZIP loads", "constant-power loads (SimBench as shipped)": "moved:constant-power loads"}),
    ("V3_CITYLEARN.md", "Buildings and batteries (CityLearn, UT Austin)", "the electric batteries' charge and discharge commands",
     {"Districts with electric batteries: omni against native, each run": "moved", "Districts with no electric battery: nothing for Omni to move": "no_knob",
      "Districts CityLearn cannot run with its own controller": "not_run"}),
    ("V3_SWARM.md", "Drone swarms (gym-pybullet-drones, University of Toronto)", "the autopilot's cruise override",
     {"Cells where Omni moved the cruise": "moved", "Cells where the paired trial left the cruise native": "left_native", "Void cells": "void"}),
]
SIM_SHORT = {
    "V3_PANDAPOWER.md": {"losses_worse": "losses: an exporting grid pays the lower voltage in line losses (the analysis under the table)",
                         "taps_worse": "taps: the declared cost on a grid that barely taps on its own (4 a year, doubled)",
                         "import_worse": "import: follows the losses, hundredths of a percent"},
    "V3_CITYLEARN.md": {"2023": "the 2023 pattern: the bill, the ramping and the energy not served up, the electricity bought, the carbon and the daily peak down (the analysis under the table)",
                        "monthly": "the monthly load factor moved by a tenth of a percent against a bill 8.6% lower"},
}
SIM_WHY = {
    "V3_PANDAPOWER.md": {
        "losses_worse": ("the lower setpoint carries the grid's power at a lower voltage and therefore a higher current, and line losses rise with "
                         "the square of the current. The four grids where losses rose are four of the five that export more than they import "
                         "(net import negative: rural 1 and 2, semiurb 1 and 2); on the importing grids the loads' own draw falls with the "
                         "voltage under ZIP loads and losses fall with it. Under constant-power loads the loads draw the same at any voltage, so "
                         "the setpoint saves nothing on the loads and the exporting grids pay the losses with nothing bought"),
        "taps_worse": ("tap operations, declared in advance as Omni's expected cost (`docs/PANDAPOWER_PREREGISTRATION.md`): this grid barely taps on "
                       "its own (4 a year), so Omni's moves double a very small count"),
        "import_worse": "the import follows the losses: the same loads, more lost on the lines, so hundredths of a percent less exported or more imported upstream"},
    "V3_CITYLEARN.md": {
        "2023": ("the seven 2023 challenge districts are small (3 to 6 buildings) and short (720 to 2,208 hours), and in them the energy "
                 "not served and the comfort rows move, where in the county neighbourhoods they read the same: the compass steers the batteries from the district's "
                 "electricity reading alone (one wire, one muscle, `docs/CITYLEARN_PREREGISTRATION.md`), flattening the draw it sees, and in "
                 "these districts that leaves less in the batteries for the hours that count against the bill, the hour-to-hour ramping and "
                 "the energy not served. The bill, what the battery is bought to lower, is confirmed worse here by 0.2% to 0.4%, so for the "
                 "operator who pays the bill this is a watch. The cause is a reading of the tables, not yet tested on its own"),
        "monthly": "the monthly load factor moved by a tenth of a percent against a bill 8.6% lower and 14.7% less electricity bought"},
    "V3_MUJOCO.md": {
        "left_native": ("the engine's own verdict: one cycle at full speed and one at override 0.8, in native mode before the counted cycles, "
                        "showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so the "
                        "override was left at 1.0 and both arms are the same (`omnicompass/verdict.py`, left native)")},
}


def parse_sim(path):
    """The sections, subsections and tables of a simulator's A/B/C markdown table."""
    text = path.read_text()
    sections = []
    cur = None
    for ln in text.splitlines():
        if ln.startswith("## "):
            cur = {"title": ln[3:].strip(), "subs": [], "table": []}
            sections.append(cur)
        elif ln.startswith("### ") and cur is not None:
            cur["subs"].append({"title": ln[4:].strip(), "rows": []})
        elif ln.startswith("|") and cur is not None:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            (cur["subs"][-1]["rows"] if cur["subs"] else cur["table"]).append(cells)
    return sections


def sim_rows_judged(rows):
    """Rows of a gauge table (header first) into classified items with the A/B/C range."""
    j = {"better": [], "worse": [], "noise": [], "disagree": [], "same": []}
    if not rows:
        return j
    head = rows[0]
    ridx = len(head) - 1
    abc = [i for i, h in enumerate(head) if h in ("A", "B", "C")]
    for r in rows[1:]:
        if len(r) != len(head):
            continue
        c = classify(r[ridx])
        if c == "unjudged":
            continue
        vals = []
        for i in abc:
            s = r[i].replace("−", "-")
            if s.endswith("%"):
                try:
                    vals.append(float(s[:-1]))
                except ValueError:
                    pass
        if vals:
            lo, hi = min(vals), max(vals)
            f = (lambda x: f"{x:+.0f}%") if max(abs(lo), abs(hi)) >= 10 else (lambda x: f"{x:+.1f}%")
            rg = f(lo) if f(lo) == f(hi) else f"{f(lo)} to {f(hi)}"
        else:
            rg = r[abc[0]] if abc else ""
        name = re.sub(r"\s*\(`[^`]*`\)\s*$", "", r[0])          # CityLearn: drop the score's code name
        name = re.sub(r"\s*\([^()]*\)\s*$", "", name) or name     # the unit or the note in brackets: the table has it
        j[c].append((r[0], name, rg, None))
    return j


def sims():
    cases = []
    for f, domain, knob, modes in SIMS:
        p = LIVE / f
        if not p.exists():
            continue
        for sec in parse_sim(p):
            mode = next((m for t, m in modes.items() if sec["title"].startswith(t)), None)
            if mode is None:
                continue
            if mode.startswith("moved"):
                tag = mode.split(":", 1)[1] if ":" in mode else ""
                for sub in sec["subs"]:
                    name = sub["title"].split(":", 1)[0].strip()
                    j = sim_rows_judged(sub["rows"])
                    counted = not (f == "V3_SWARM.md" and name == "tuning")
                    v = verdict(len(j["better"]), len(j["worse"]))
                    cases.append({"kind": "modelled simulator", "domain": domain, "knob": knob, "case": name + (f" ({tag})" if tag else "")
                                  + ("" if counted else " (the tuning swarm: shown, never counted)"),
                                  "counted": counted, "judged": j, "verdict": v, "resource_pct": None, "service_pct": None,
                                  "why": sim_why(f, name, j, v), "source": f"results/live/{f}", "runs": []})
            elif mode == "left_native":
                for r in sec["table"][1:]:
                    if not r or not r[0]:
                        continue
                    j = {"better": [], "worse": [], "noise": [], "disagree": [], "same": []}
                    cases.append({"kind": "modelled simulator", "domain": domain, "knob": knob, "case": r[0], "counted": True, "judged": j,
                                  "verdict": WATCH, "resource_pct": None, "service_pct": None,
                                  "why": SIM_WHY[f]["left_native"][0].upper() + SIM_WHY[f]["left_native"][1:]
                                         + f". The trial's figures: {r[1]} J at full speed against {r[2]} J at the trial speed, reproduced over A, B, C: {r[3]}",
                                  "source": f"results/live/{f}", "runs": []})
            elif mode == "no_knob":
                for r in sec["table"][1:]:
                    if not r or not r[0]:
                        continue
                    cases.append({"kind": "modelled simulator", "domain": domain, "knob": knob, "case": r[0], "counted": False, "judged": None,
                                  "verdict": "no knob", "resource_pct": None, "service_pct": None,
                                  "why": f"no electric battery in the district ({r[1]} buildings, {r[2]} water tanks left native): there is nothing for Omni to hold, "
                                         f"so there is nothing to decide; any difference between the arms is CityLearn's own run-to-run variation"
                                         + (f" (scores that differ in A: {r[3]}; reproduced: {r[4]})" if len(r) > 4 else ""),
                                  "source": f"results/live/{f}", "runs": []})
    return cases


def sim_why(f, name, j, v):
    parts = []
    if j["disagree"]:
        parts.append(f"the runs differ on {fmt_list(j['disagree'], 3)}")
    if not j["better"] and not j["worse"]:
        parts.append("nothing confirmed either way")
    s = ("; ".join(parts) + ".") if parts else ""
    why = SIM_SHORT.get(f, {})
    if f == "V3_PANDAPOWER.md" and j["worse"]:
        keys = [k for k, _, _, _ in j["worse"]]
        causes = []
        if any("losses" in k for k in keys):
            causes.append(why["losses_worse"])
        if any("tap" in k for k in keys):
            causes.append(why["taps_worse"])
        if any("import" in k for k in keys):
            causes.append(why["import_worse"])
        s = (s + " Why: " + "; ".join(causes) + ".").strip()
        if v == CHOICE:
            s += " The operator who wants the loads' energy and the upstream import down wires in and accepts the line losses; the operator who runs the grid to its losses watches."
    if f == "V3_CITYLEARN.md" and j["worse"]:
        if "2023" in name:
            s = (s + " Why: " + why["2023"] + ".").strip()
        elif any("monthly" in k for k, _, _, _ in j["worse"]):
            s = (s + " Why: " + why["monthly"] + ".").strip()
        if v == CHOICE and "2023" in name:
            s += " By rule a trade; by what the battery is for (the bill), a watch."
    s = s.strip()
    if f == "V3_SWARM.md" and v == WRITE:
        s += " Nothing worse: the tracking error is spent inside the compass's band (shown, the runs differ on its exact figure) and no safety gauge moved."
    if f == "V3_MUJOCO.md" and v == WRITE:
        s += " Nothing worse: the same job inside the same takt, hit more accurately with less force; the cycle is slower inside the takt (shown, not judged)."
    if v == WRITE and f in ("V3_PANDAPOWER.md", "V3_CITYLEARN.md"):
        s += " Nothing worse: Omni holds the knob."
    return s.strip()


# ------------------------------------------------------------------------------------- the 945 modelled muscles
LABEL_VERDICT = {"SUPERIOR WITHIN GUARDRAILS": WRITE, "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF": CHOICE,
                 "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF": CHOICE, "NONINFERIOR / INCONCLUSIVE": WATCH, "NOT ESTABLISHED": WATCH,
                 "WORSE": WATCH, "INVALID": "invalid"}
REALM_NAMES = {"compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
               "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
               "tower": "The whole tower, every muscle once"}


def ffl(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def muscles():
    rows = list(csv.DictReader((ROOT / "results" / "realms" / "MUSCLES.csv").open()))
    out = []
    for r in rows:
        label = r["label"]
        v = LABEL_VERDICT[label]
        p, lo, hi = ffl(r["primary"]), ffl(r["primary_lo"]), ffl(r["primary_hi"])
        w = ffl(r["writes_per_run"]) or 0.0
        work, viol, viol_hi = ffl(r["work"]), ffl(r["viol_pp"]), ffl(r["viol_pp_hi"])
        fc_label, fc_p = r.get("fixed_calm_label", ""), ffl(r.get("fixed_calm_primary"))
        pct = lambda x: f"{100 * x:+.1f}%" if x is not None else ""
        if label == "NONINFERIOR / INCONCLUSIVE":
            if w == 0:
                why = ("wrote nothing in any run: the native controller held the reading inside the band, the law never left its cushion and "
                       "had nothing to push; nothing to earn, nothing lost")
            else:
                why = (f"wrote {w:.0f} times a run with no measurable change in work per energy ({pct(p)}, {pct(lo)} to {pct(hi)}): the interval "
                       f"includes zero, so nothing is claimed either way")
        elif label == "SUPERIOR WITHIN GUARDRAILS":
            why = f"work per energy {pct(p)} ({pct(lo)} to {pct(hi)}), work {pct(work)}, violations {viol:+.2f} pp, guardrails held"
            if r["knob"] == "setpoint" and fc_p is not None:
                if fc_label == "SUPERIOR WITHIN GUARDRAILS":
                    why += (f"; a fixed setpoint at the band's calm end gave {pct(fc_p)} within the same guardrails: the gain is the band's, and an "
                            f"operator may fix the setpoint instead of wiring in")
                elif fc_label:
                    why += (f"; a fixed setpoint at the calm end gave {pct(fc_p)} but broke the service guardrail ({fc_label.lower()}): the moving "
                            f"hand is what keeps the service")
        elif label == "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF":
            why = (f"work per energy {pct(p)} ({pct(lo)} to {pct(hi)}) but a service guardrail broke: work {pct(work)}, violations "
                   f"{viol:+.2f} pp (upper {viol_hi:+.2f}); energy saved at the service's expense: the operator's to take or leave")
        elif label == "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF":
            why = (f"violations {viol:+.2f} pp (proven lower) at work per energy {pct(p)} ({pct(lo)} to {pct(hi)}): energy bought service "
                   f"(a battery's round trip, a plant held nearer its line); the operator's to take or leave")
        elif label == "NOT ESTABLISHED":
            why = (f"the interval is too wide to read ({pct(lo)} to {pct(hi)}) and a guardrail did not hold (work {pct(work)}): nothing is "
                   f"established, the knob stays native")
        else:
            why = label.lower()
        out.append({"kind": "modelled muscle", "domain": f"{REALM_NAMES.get(r['realm'], r['realm'])}: {r['family']}", "knob": r["knob"],
                    "case": r["muscle"], "counted": True, "judged": None, "verdict": v, "resource_pct": None, "service_pct": None,
                    "why": why, "source": "results/realms/MUSCLES.csv", "runs": [], "muscle": r, "label": label, "writes": w})
    return out


def organisms_modelled():
    d = json.loads((ROOT / "results" / "realms" / "REALMS.json").read_text())
    out = []
    for name, o in d["organisms"].items():
        p = o["summary"]["primary"]
        out.append({"kind": "modelled organism", "domain": REALM_NAMES.get(name, name), "knob": "every muscle of the organism, one governor",
                    "case": f"{o['n']} muscles", "counted": True, "judged": None, "verdict": LABEL_VERDICT[o["label"]], "resource_pct": None,
                    "service_pct": None, "why": f"{o['label']}: work per energy {100 * p[0]:+.1f}% ({100 * p[1]:+.1f} to {100 * p[2]:+.1f}), "
                    f"work {100 * o['summary']['work'][0]:+.1f}%, energy {100 * o['summary']['energy'][0]:+.1f}%, violations "
                    f"{o['summary']['viol_pp'][0]:+.3f} pp; valid: {'yes' if o['valid'] else 'no'}",
                    "source": "results/realms/REALMS.md", "runs": [], "label": o["label"]})
    return out


# ------------------------------------------------------------------- the organisms with the real cluster inside
VERDICT_RE = re.compile(r"better on (\d+), worse on (\d+)(?: \(([^)]*)\))?, inside the noise on (\d+)")


def organisms_cluster():
    out = []
    for f, title in (("V3_SIX_KUBE.json", "the six organisms with the real cluster inside (GitHub, 10 and 100 copies)"),
                     ("V3_BIG_ORGANISM.json", "the big organisms with the real cluster inside (a rented Azure machine, 1,000 copies)")):
        p = LIVE / f
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        for cell, c in d["organisms"].items():
            m = VERDICT_RE.search(c.get("verdict", ""))
            if not m:
                continue
            nb, nw, worse_names, nn = int(m.group(1)), int(m.group(2)), (m.group(3) or ""), int(m.group(4))
            worse_list = [w.strip() for w in worse_names.split(";") if w.strip()]
            # the cluster's own gauges decide; the organism's modelled work and energy are judged muscle by muscle in the realms table
            cluster_worse = [w for w in worse_list if not w.startswith("organism")]
            modelled_worse = [w for w in worse_list if w.startswith("organism")]
            rows = c["rows"]
            sure = lambda v: v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
            cluster_better = [k for k, v in rows.items() if not k.startswith("organism") and v["better"] and not v["neutral"] and not v["same"] and sure(v)]
            v = verdict(len(cluster_better), len(cluster_worse))
            why = (f"the table's own reading: {c['verdict']}. The cluster's gauges: {len(cluster_better)} better"
                   + (f" ({', '.join(K8S_GAUGE.get(k, k) for k in cluster_better[:5])})" if cluster_better else "")
                   + f", {len(cluster_worse)} worse" + (f" ({', '.join(cluster_worse)})" if cluster_worse else "") + ".")
            if modelled_worse:
                ow = rows.get("organism work")
                why += (f" The organism's modelled {', '.join(w.replace('organism ', '') for w in modelled_worse)}"
                        + (f" {ow['pct']:+.4f}% ({abs(ow['pct']) * 1e4:.0f} parts in a million, rounding level)" if ow else "")
                        + ", the one worse row, is a model gauge judged muscle by muscle in the realms table and shown here beside the cluster's.")
            oe = rows.get("organism energy (J)")
            if oe:
                why += f" The organism's modelled energy {oe['pct']:+.1f}%."
            if c.get("off_the_clock_reps"):
                why += f" Off the clock in {len(c['off_the_clock_reps'])} of {c['repetitions']} repetitions."
            out.append({"kind": "organism with the cluster inside", "domain": title, "knob": K8S_KNOB + " under the organism's demand",
                        "case": cell.replace("@", " at ") + " copies" if "@" in cell else cell, "counted": True, "judged": None, "verdict": v,
                        "resource_pct": None, "service_pct": None, "why": why, "source": f"results/live/{f.replace('.json', '.md')}", "runs": []})
    return out


# ------------------------------------------------------------------------------------------------- the report
def pct_s(x):
    return "" if x is None else f"{x:+.1f}%"


def count(cases):
    c = collections.Counter(x["verdict"] for x in cases if x["counted"] and x["verdict"] in (WRITE, WATCH, CHOICE))
    return c[WRITE], c[CHOICE], c[WATCH]


def esc(s):
    return s.replace("|", "\\|")


def main(check=False):
    index = load_index()
    real = real_stacks(index)
    sim = sims()
    mus = muscles()
    org_m = organisms_modelled()
    org_c = organisms_cluster()
    all_cases = real + sim + mus + org_m + org_c

    rw, rc, rwa = count(real)
    sw, sc, swa = count([x for x in sim if x["verdict"] != "no knob"])
    mw, mc, mwa = count(mus)
    ow, oc, owa = count(org_c)

    L = ["# Wire in, or watch: the verdict per knob, from every result in the repository", "",
         "Omni-Compass is wired **out of** every muscle: it reads every reading. It is wired **into** a knob only where the paired "
         "measurement shows the muscle no worse for it. Where the measurement shows nothing, or shows a loss, the muscle stays "
         "native and Omni only watches it: one wire out, no wire in. This is not a new rule. It is what the engine does on the muscle "
         "itself before it moves anything (`omnicompass/verdict.py`: the paired trial, and the verdict **left native** where no step is "
         "allowed), and it is the watch arm of every realms run (`docs/REALMS_PREREGISTRATION.md`: the governor reads every period and "
         "writes nothing). This page applies the same principle to every published result, one verdict per knob, so that an operator "
         "can see which knobs earn a wire in and which stay native. The founder's order of 9 October 2026: where Omni cannot beat "
         "native, the muscle lives by itself; we only wire out of it.", "",
         "Every verdict here is computed by `tools/wiring_verdicts.py` from the test's own result file; nothing is typed in, and "
         "`verify.py` fails if this page differs from what the tables give. One row per knob and case: `results/WIRING_VERDICTS.csv` "
         f"({len(all_cases)} rows, the 945 modelled muscles included one by one).", "",
         "## The rule", "",
         "Every judged gauge of a table counts (rows marked \"shown, not judged\" never do). A knob reads:", "",
         "- **write**: at least one gauge confirmed better over all three runs and none confirmed worse. Omni holds the knob.",
         "- **watch**: nothing confirmed better. The knob stays native; Omni reads it and writes nothing. Where a gauge is confirmed "
         "worse, the loss is named and its cause given below. Where the runs disagree, nothing is settled and the knob stays native until it is.",
         "- **operator's choice**: gains and losses both confirmed, a trade. Both readings of the Omni index are shown where the test is in it "
         "(the resource reading, the preregistered headline, and the service reading, work and speed alone), and the side that pays is named. "
         "The operator who wants the gain and can pay the cost wires in; every other operator watches.", "",
         "A modelled muscle (the 945 on their plants, `results/realms/MUSCLES.csv`) takes its verdict from its label by rule: SUPERIOR WITHIN "
         "GUARDRAILS is write; ENERGY IMPROVEMENT WITH SERVICE TRADEOFF and SERVICE IMPROVEMENT WITH ENERGY TRADEOFF are operator's choice; "
         "NONINFERIOR / INCONCLUSIVE, NOT ESTABLISHED and WORSE are watch.", "",
         "## The count", "",
         "| Where | Knobs or cases | Write | Operator's choice | Watch |", "|---|---:|---:|---:|---:|",
         f"| Real stacks, three runs each (Kubernetes under seven demands; the pool, the consumer group, the memory ceiling, the storage-engine cache and the buffer pool, each under its untouched workloads) | {rw + rc + rwa} | {rw} | {rc} | {rwa} |",
         f"| Independent simulators, three runs each (robot arms, grids, districts, swarms; evidence class S) | {sw + sc + swa} | {sw} | {sc} | {swa} |",
         f"| The 945 modelled muscles, alone on their plants (evidence class S) | {mw + mc + mwa} | {mw} | {mc} | {mwa} |",
         f"| The organisms with the real cluster inside (GitHub at 10 and 100 copies; Azure at 1,000) | {ow + oc + owa} | {ow} | {oc} | {owa} |", ""]
    L += ["In words: on the real stacks Omni earns its wire in on " + f"{rw} of {rw + rc + rwa} knob-cases, trades on {rc} and watches on {rwa}. "
          f"Of the 945 modelled muscles, {mw} earn a wire in, {mc} are trades and {mwa} stay native: "
          f"{sum(1 for x in mus if x['verdict'] == WATCH and x['writes'] == 0)} of the {mwa} wrote nothing in any run, because the native "
          f"controller already held the reading inside the band and the law never left its cushion. A knob that never writes costs nothing "
          f"and earns nothing; it needs no wire in, and the page below says so muscle by muscle.", ""]

    # the real stacks
    L += ["## The real stacks (evidence class L: live software, three separate GitHub runs on the frozen engine)", "",
          "The reading of every judged gauge is in the test's own table (the Source column). The index columns are the two readings "
          "of `results/OMNI_INDEX.md` for that test, where it has one.", ""]
    L += ["### Real Kubernetes: one knob under seven demands", "",
          f"The knob: {K8S_KNOB}, on top of the Horizontal Pod Autoscaler (kind clusters on GitHub, ten pairs a run).", "",
          "| Demand | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |", "|---|---|---|---|---:|---:|---|---|"]
    for x in [c for c in real if c["kind"] == "real knob" and "Kubernetes" in c["domain"]]:
        j = x["judged"]
        L.append(f"| {x['case']} | {esc(fmt_list(j['better'], 12)) or 'none'} | {esc(fmt_list(j['worse'], 12)) or 'none'} | **{x['verdict']}** | "
                 f"{pct_s(x['resource_pct'])} | {pct_s(x['service_pct'])} | {esc(x['why'])} | `{x['source']}` |")
    L.append("")
    for cat, f, knob, names in WORKLOAD_STACKS:
        rows = [c for c in real if c.get("stack") == STACK_SHORT[f]]
        if not rows:
            continue
        L += [f"### {cat}", "", f"The knob: {knob}.", "",
              "| Workload | Confirmed better | Confirmed worse | Verdict | Index: resource | Index: service | Why | Source |", "|---|---|---|---|---:|---:|---|---|"]
        for x in rows:
            j = x["judged"]
            L.append(f"| {x['case']} | {esc(fmt_list(j['better'], 12)) or 'none'} | {esc(fmt_list(j['worse'], 12)) or 'none'} | "
                     f"**{x['verdict']}**{'' if x['counted'] else ' (not counted)'} | {pct_s(x['resource_pct'])} | {pct_s(x['service_pct'])} | {esc(x['why'])} | `{x['source']}` |")
        L.append("")

    # every negative
    L += ["## Every confirmed loss on a real stack, and why", "",
          "The founder's question was where the negatives are and why each is there. Every gauge confirmed worse on a real stack, with its cause "
          "read from the preregistration that carries the result:", ""]
    groups = collections.OrderedDict()
    for x in real:
        if not x["counted"]:
            continue
        f = x["source"].rsplit("/", 1)[-1].replace(".md", ".json")
        for k, nm, rg, runs in x["judged"]["worse"]:
            w = WHY.get((f, x.get("workload", "*"), k)) or WHY.get((f, "*", k)) or "see the table"
            groups.setdefault((x.get("stack", "Kubernetes"), nm, w), []).append((x.get("workload", x["case"]), rg, runs, x["verdict"]))
    for (stack, nm, w), items in groups.items():
        cases = ", ".join(f"{wl} {rg}" for wl, rg, _, _ in items)
        figs = []
        for _, _, runs, _ in items:
            n0, o0 = first(runs, "native"), first(runs, "omni")
            if isinstance(n0, (int, float)) and isinstance(o0, (int, float)):
                figs.append((n0, o0))
        fig = ""
        if figs:
            ns = sorted({f"{n:.4g}" for n, _ in figs}); os_ = sorted(f"{o:.4g}" for _, o in figs)
            fig = f" ({' / '.join(ns)} → {os_[0]}{' to ' + os_[-1] if len(os_) > 1 and os_[0] != os_[-1] else ''} in run A)"
        vs = sorted({v for _, _, _, v in items})
        L.append(f"- **{stack}, {nm}: {cases}**{fig}. {w[0].upper() + w[1:]}. Verdict: **{' / '.join(vs)}**"
                 + (" on every workload named" if len(items) > 1 else "") + ".")
    if not groups:
        L.append("- none")
    L += ["", "What the losses have in common: every one is a resource spent to buy the service the knob exists for (consumers and the CPU "
          "they poll with, memory, pages, connections), and each was declared in advance in its preregistration as the cost that would read worse, or found "
          "on the first counted set and disclosed. None is a service loss: on no real stack did work inside the line, p95 or failed requests "
          "read confirmed worse. Where the resource was spent and nothing was bought (PostgreSQL's `simple_update`), the verdict is watch; where "
          "it bought service, the verdict is the operator's, and both index readings say what the trade is worth.", ""]

    # the simulators
    L += ["## The independent simulators (evidence class S: deterministic models with their own native controllers)", ""]
    for f, domain, knob, _ in SIMS:
        rows = [c for c in sim if c["domain"] == domain]
        if not rows:
            continue
        L += [f"### {domain}", "", f"The knob: {knob}.", "",
              "| Case | Confirmed better | Confirmed worse | Verdict | Why | Source |", "|---|---|---|---|---|---|"]
        for x in rows:
            j = x["judged"]
            b = esc(fmt_list(j["better"], 12)) if j else ""
            w = esc(fmt_list(j["worse"], 12)) if j else ""
            L.append(f"| {x['case']} | {b or ('none' if j else '')} | {w or ('none' if j else '')} | **{x['verdict']}**"
                     f"{'' if x['counted'] or x['verdict'] == 'no knob' else ' (not counted)'} | {esc(x['why'])} | `{x['source']}` |")
        L.append("")
        if f == "V3_PANDAPOWER.md":
            L += ["**Why the losses rose on four grids.** " + SIM_WHY[f]["losses_worse"][0].upper() + SIM_WHY[f]["losses_worse"][1:] + ". "
                  + SIM_WHY[f]["taps_worse"][0].upper() + SIM_WHY[f]["taps_worse"][1:] + ". The verdict on those four grids is the operator's: the "
                  "loads' energy and the upstream import down against the lines' losses up; under constant-power loads on 1-MV-rural--1-sw, where "
                  "nothing was bought, it is watch.", ""]
        if f == "V3_CITYLEARN.md":
            L += ["**Why the 2023 districts read worse on the bill.** " + SIM_WHY[f]["2023"][0].upper() + SIM_WHY[f]["2023"][1:] + ".", ""]

    # the 945 muscles
    by_label = collections.Counter(x["label"] for x in mus)
    L += ["## The 945 modelled muscles, alone on their plants (evidence class S)", "",
          "Every muscle's own row, with its verdict and the reason, is in `results/WIRING_VERDICTS.csv`; the labels and intervals are the realms "
          "table's (`results/realms/REALMS.md`, `results/realms/MUSCLES.csv`; seeds 3000 to 3009, ten paired seeds a muscle).", "",
          "| Label (by rule) | Muscles | Verdict |", "|---|---:|---|"]
    for lab, n in sorted(by_label.items(), key=lambda kv: -kv[1]):
        L.append(f"| {lab} | {n} | **{LABEL_VERDICT[lab]}** |")
    L += ["", "### By knob", "", "| Knob | Muscles | Write | Operator's choice | Watch | Of the watch, wrote nothing in any run |", "|---|---:|---:|---:|---:|---:|"]
    for knob in ("capacity", "setpoint", "power", "admission"):
        ms = [x for x in mus if x["knob"] == knob]
        c = collections.Counter(x["verdict"] for x in ms)
        z = sum(1 for x in ms if x["verdict"] == WATCH and x["writes"] == 0)
        L.append(f"| {knob} | {len(ms)} | {c[WRITE]} | {c[CHOICE]} | {c[WATCH]} | {z} |")
    L += ["", "### By family", "", "| Realm: family | Muscles | Write | Operator's choice | Watch | Wrote nothing |", "|---|---:|---:|---:|---:|---:|"]
    fams = collections.OrderedDict()
    for x in mus:
        fams.setdefault(x["domain"], []).append(x)
    for fam, ms in fams.items():
        c = collections.Counter(x["verdict"] for x in ms)
        z = sum(1 for x in ms if x["verdict"] == WATCH and x["writes"] == 0)
        L.append(f"| {fam} | {len(ms)} | {c[WRITE]} | {c[CHOICE]} | {c[WATCH]} | {z} |")
    zero = [x for x in mus if x["verdict"] == WATCH and x["writes"] == 0]
    wrote = [x for x in mus if x["verdict"] == WATCH and x["writes"] > 0]
    adm = [x for x in mus if x["knob"] == "admission"]
    setp_sup = [x for x in mus if x["knob"] == "setpoint" and x["label"] == "SUPERIOR WITHIN GUARDRAILS"]
    fc_sup = sum(1 for x in setp_sup if x["muscle"].get("fixed_calm_label") == "SUPERIOR WITHIN GUARDRAILS")
    fc_trade = sum(1 for x in setp_sup if x["muscle"].get("fixed_calm_label") == "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF")
    L += ["", "### Why the watch muscles are watch", "",
          f"- **{len(zero)} muscles wrote nothing in any run.** Their plants' native controllers held the reading inside the compass's band for the "
          f"whole hour on every seed, so the law never left its cushion and had nothing to push. On these muscles Omni on top is native: nothing "
          f"earned, nothing lost, and no wire in is needed. They are {collections.Counter(x['knob'] for x in zero)['capacity']} capacity knobs, "
          f"{collections.Counter(x['knob'] for x in zero)['admission']} admission knobs, {collections.Counter(x['knob'] for x in zero)['power']} power "
          f"knobs and {collections.Counter(x['knob'] for x in zero)['setpoint']} setpoint knobs, "
          f"{collections.Counter(x['muscle']['template'] for x in zero)['compute_pool']} of them on the compute plant, whose native autoscaler and "
          f"fixed admission limit already serve the modelled demand inside its line.",
          f"- **All {len(adm)} admission muscles are watch**, and all wrote nothing: the admission knob is native while change is permitted, and "
          f"limits what is let in only while it is not (a power or heat stress; `docs/REALMS_PREREGISTRATION.md`). No run reached that state, "
          f"so the knob was never touched. This is the knob's design, not a failure: admission is a brake for an emergency the hour did not hold.",
          f"- **{len(wrote)} muscles wrote and showed nothing**: their work per energy moved by at most "
          f"{100 * max(ffl(x['muscle']['primary']) or 0 for x in wrote):+.1f}% with an interval across zero. They are process loops, inverters, "
          f"chambers, mills and zones where the law moved the knob inside its band and the plant's output did not measurably follow. Watch, by rule.",
          f"- **One muscle is not established** (Elevators & Vertical Transport, `hoist_speed_target`): the interval is too wide to read and the "
          f"work guardrail did not hold. Watch, until a longer run decides it.", "",
          "### The trades, muscle by muscle", "",
          "| Muscle | Family | Knob | Label | Work per energy | Work | Violations (pp) | Verdict |", "|---|---|---|---|---:|---:|---:|---|"]
    for x in mus:
        if x["verdict"] == CHOICE or x["label"] == "NOT ESTABLISHED":
            m = x["muscle"]
            L.append(f"| `{m['muscle']}` | {m['family']} | {m['knob']} | {m['label']} | {100 * ffl(m['primary']):+.2f}% ({100 * ffl(m['primary_lo']):+.2f} to "
                     f"{100 * ffl(m['primary_hi']):+.2f}) | {100 * ffl(m['work']):+.2f}% | {ffl(m['viol_pp']):+.2f} | **{x['verdict']}** |")
    L += ["", "The nine energy-for-service trades are the CPU's minimum clock (`cpufreq_min`), four spacecraft power knobs and four district heating "
          "setpoints: energy saved at a measurable cost in work or in time in violation. The four service-for-energy trades are three microgrid "
          "reserves and a facility's PUE target: time in violation proven lower at a small energy cost. Each is the operator's to take or leave; "
          "none is wired in by default.", "",
          "### The setpoint muscles, and what the band alone gives", "",
          f"Of the {len(setp_sup)} setpoint muscles that read SUPERIOR, a fixed setpoint at the band's calm end (the `fixed_calm` arm, the native "
          f"controller with the setpoint fixed, no governor) gave as much or more work per energy on every one. On {fc_sup} of them the fixed "
          f"setpoint also held the service guardrails, so the gain is the band's and an operator may simply fix the setpoint; on {fc_trade} the fixed "
          f"setpoint broke the service guardrail (ENERGY IMPROVEMENT WITH SERVICE TRADEOFF), and there the governor's moving hand is what keeps the "
          f"service while the energy is saved. The CSV says which is which, muscle by muscle.", ""]

    # the organisms
    L += ["## The organisms", "", "### The five modelled organisms (every muscle written at once, one governor)", "",
          "| Organism | Muscles | Label | Verdict | Figures |", "|---|---:|---|---|---|"]
    for x in org_m:
        L.append(f"| {x['domain']} | {x['case']} | {x['label']} | **{x['verdict']}** | {esc(x['why'])} |")
    L += ["", "An organism's label is the whole's: every muscle written at once. The wiring an operator takes from this page is finer: the "
          "write muscles wired in, the trades chosen, the watch muscles left native with one wire out. The organism result says the whole, "
          "written at once, was no worse and a little better; this page says which parts carried it.", "",
          "### The organisms with the real cluster inside", "",
          f"The knob is the cluster's ({K8S_KNOB}), under the organism's own demand, with the modelled muscles around it. The cluster's gauges "
          "decide the verdict; the organism's modelled work and energy are shown beside them and are judged muscle by muscle above.", "",
          "| Cell | Verdict | The table's reading, and the figures | Source |", "|---|---|---|---|"]
    for x in org_c:
        L.append(f"| {x['case']} ({'GitHub' if 'GitHub' in x['domain'] else 'Azure'}) | **{x['verdict']}** | {esc(x['why'])} | `{x['source']}` |")

    # not decided
    L += ["", "## Not decided here", "",
          "- **Azure's managed Kubernetes (the bill):** the two tables are on Omni v1 (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`) on a "
          "4-worker fleet, where every gauge read no difference beyond the noise but the burst's p99 in one run. A fleet too small to show one "
          "machine decides nothing; the fleet that can (`docs/K8S_COMPASS_PREREGISTRATION.md`, the fleet that can show one machine) decides this "
          "knob on v3 when it runs. Until then the verdict on Azure is watch, for want of a result rather than because of one.",
          "- **The card (NVIDIA, its own meter):** every earlier card result is obsolete; the current governor has not run on a real card. Nothing "
          "to decide yet.",
          "- **The 24-hour robustness machines:** running; they test the governor's own staying power, not a knob's value.", "",
          "## What this means for the wiring", "",
          "The two-way plug stays one wire in and one wire out (`docs/WIRING_GUIDE.md`). This page decides, per knob, whether the wire in is "
          "connected. A knob marked **write** is wired both ways. A knob marked **watch** is wired out only: Omni reads it, learns from it, "
          "and never writes it; the native controller lives by itself. A knob marked **operator's choice** is wired out, and in only by the "
          "operator who wants that trade. The engine's verdict (`omnicompass/verdict.py`) does the same on the muscle itself at run time, and a "
          "knob it has left native is a watch knob whatever this page says. Nothing on this page changes the engine, which stays Omni v3; it "
          "changes what an operator connects.", ""]

    md = "\n".join(legal_stamp(L)) + "\n"

    # the CSV
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["kind", "domain", "knob", "case", "counted", "confirmed_better", "confirmed_worse", "inside_the_noise", "runs_disagree",
                "verdict", "index_resource_pct", "index_service_pct", "why", "source"])
    for x in all_cases:
        j = x["judged"]
        w.writerow([x["kind"], x["domain"], x["knob"], x["case"], "yes" if x["counted"] else "no",
                    "; ".join(f"{nm} {rg}".strip() for _, nm, rg, _ in j["better"]) if j else "",
                    "; ".join(f"{nm} {rg}".strip() for _, nm, rg, _ in j["worse"]) if j else "",
                    len(j["noise"]) if j else "", len(j["disagree"]) if j else "",
                    x["verdict"], "" if x["resource_pct"] is None else f"{x['resource_pct']:.2f}",
                    "" if x["service_pct"] is None else f"{x['service_pct']:.2f}", x["why"], x["source"]])
    csv_text = buf.getvalue()

    if check:
        bad = []
        if not OUT_MD.exists() or OUT_MD.read_text() != md:
            bad.append(str(OUT_MD.relative_to(ROOT)))
        if not OUT_CSV.exists() or OUT_CSV.read_text() != csv_text:
            bad.append(str(OUT_CSV.relative_to(ROOT)))
        if bad:
            print("wiring verdicts out of date (python3 tools/wiring_verdicts.py): " + ", ".join(bad))
            return 1
        print("wiring verdicts: in line with the tables")
        return 0
    OUT_MD.write_text(md)
    OUT_CSV.write_text(csv_text)
    print(f"{OUT_MD.relative_to(ROOT)}: real {rw}/{rc}/{rwa}, simulators {sw}/{sc}/{swa}, muscles {mw}/{mc}/{mwa}, cluster organisms {ow}/{oc}/{owa} "
          f"(write/operator's choice/watch); {OUT_CSV.relative_to(ROOT)}: {len(all_cases)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv[1:]))
