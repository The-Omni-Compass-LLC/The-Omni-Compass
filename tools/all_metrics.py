"""Every number from every result file in the repository, in one place, each labelled with what kind of evidence it is.

Writes, into OUT (default ALL_METRICS/):
  ALL_METRICS_LONG.csv   one row per number: file, kind of evidence, where in the file, value (opens in any spreadsheet)
  INDEX.md               every result file, its kind of evidence, and its headline (tally of better/equal/worse when it has one)
  GPU/                   everything GPU: the device simulation, the real-GPU harness runs if any exist, and the status
Kinds of evidence (from where the file lives and what it is called):
  live-kubernetes        measured on real Kubernetes (kind) in GitHub Actions
  real-gpu               measured by a real GPU's own meter (results/gpu/)
  simulation-heldout     simulation on scenarios never used for tuning, settings frozen before the run
  simulation-dev         simulation used to choose settings (development; not a result)
  simulation             simulation (other)
  settings               preregistrations, frozen settings, amendments (no measurements)
Usage: python tools/all_metrics.py [OUT]"""
from __future__ import annotations

import csv, json, math, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def kind(p: Path) -> str:
    s = str(p.relative_to(ROOT)).upper()
    if s.startswith("RESULTS/LIVE"):
        return "live-kubernetes"
    if s.startswith("RESULTS/GPU"):
        return "real-gpu"
    if any(k in s for k in ("PREREGISTRATION", "SETTINGS", "AMENDMENT", "LOCK_")):
        return "settings"
    if any(k in s for k in ("HELDOUT", "CONFIRMATORY", "PLANETLAB", "THREE_WAY", "PROTOCOL", "TOWER_OFF_ON", "SOAK",
                            "MULTIPLICITY", "GLOBAL_LEAGUE")):
        return "simulation-heldout"
    if "_DEV" in s or "SEARCH" in s or "/DEVELOPMENT" in s:
        return "simulation-dev"
    return "simulation"


def walk(x, path=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from walk(v, f"{path}/{k}" if path else str(k))
    elif isinstance(x, list):
        if len(x) > 2000:
            return
        for i, v in enumerate(x):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(x, bool):
        return
    elif isinstance(x, (int, float)) and math.isfinite(x):
        yield path, x


def headline(d):
    if isinstance(d, dict):
        if "tally" in d and isinstance(d["tally"], dict):
            t = d["tally"]
            if "better" in t:
                return f"better {t['better']} / equal {t.get('equal', '?')} / worse {t.get('worse', '?')}"
            return "; ".join(f"{k}: better {v.get('better')} / equal {v.get('equal')} / worse {v.get('worse')}"
                             for k, v in t.items() if isinstance(v, dict))
        for k in ("losing_cells", "note", "verdict"):
            if k in d:
                v = d[k]
                return f"{k}: {len(v) if isinstance(v, list) else v}"
        for v in d.values():
            if isinstance(v, dict) and "losing_cells" in v:
                return f"losing cells: {len(v['losing_cells'])}"
    return ""


def main(out="ALL_METRICS"):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    files = sorted([p for p in (ROOT / "results").rglob("*") if p.suffix in (".json", ".csv") and "raw" not in p.parts]
                   + list((ROOT / "tuning").glob("*.json")))
    rows, index = [], []
    for p in files:
        rel = str(p.relative_to(ROOT)); k = kind(p); n = 0; h = ""
        try:
            if p.suffix == ".json":
                d = json.loads(p.read_text())
                h = headline(d)
                for path, v in walk(d):
                    rows.append((rel, k, path, v)); n += 1
            else:
                for i, r in enumerate(csv.DictReader(open(p))):
                    if i > 5000:
                        break
                    tag = ",".join(f"{a}={b}" for a, b in list(r.items())[:4] if b and not _num(b))
                    for a, b in r.items():
                        if _num(b):
                            rows.append((rel, k, f"row {i} [{tag}] {a}", float(b))); n += 1
        except Exception as e:  # noqa: BLE001
            h = f"unreadable: {type(e).__name__}"
        index.append((rel, k, n, h))
    with open(out / "ALL_METRICS_LONG.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["file", "kind_of_evidence", "where_in_file", "value"]); w.writerows(rows)
    order = ["real-gpu", "live-kubernetes", "simulation-heldout", "simulation", "simulation-dev", "settings"]
    L = ["# Every metric, every run", "",
         f"{len(rows):,} numbers from {len(files)} result files. Every number is in `ALL_METRICS_LONG.csv` (opens in any "
         "spreadsheet), one row per number, with the file it came from and the kind of evidence it is.", "",
         "**Kinds of evidence, strongest first:**", "",
         "| Kind | What it means |", "|---|---|",
         "| real-gpu | measured by a real GPU's own power meter |",
         "| live-kubernetes | measured on real Kubernetes (kind) in GitHub Actions |",
         "| simulation-heldout | simulation on scenarios never used for tuning, settings frozen first |",
         "| simulation | simulation (other) |",
         "| simulation-dev | simulation used to choose settings: development, not a result |",
         "| settings | preregistrations and frozen settings: no measurements |", ""]
    for k in order:
        sel = [r for r in index if r[1] == k]
        if not sel:
            L += [f"## {k}", "", "_No files yet._" if k == "real-gpu" else "_None._", ""]
            continue
        L += [f"## {k} ({len(sel)} files)", "", "| File | Numbers | Headline |", "|---|---:|---|"]
        L += [f"| `{r[0]}` | {r[2]:,} | {r[3]} |" for r in sel]
        L.append("")
    (out / "INDEX.md").write_text("\n".join(L))
    gpu(out / "GPU")
    print(f"{len(rows):,} numbers from {len(files)} files -> {out}/")


def gpu(g: Path):
    """The GPU folder: the device simulation as a readable table, any real-GPU runs, and the plain status."""
    g.mkdir(parents=True, exist_ok=True)
    L = ["# GPU: everything measured or simulated", ""]
    real = sorted((ROOT / "results" / "gpu").glob("*/GPU_REPS.md")) if (ROOT / "results" / "gpu").exists() else []
    if real:
        L += ["## Real GPU runs (the GPU's own power meter)", ""]
        for r in real:
            dst = g / "real" / r.parent.name; shutil.copytree(r.parent, dst, dirs_exist_ok=True)
            L += [f"### {r.parent.name}", "", r.read_text(), ""]
    else:
        L += ["## Real GPU runs", "",
              "**None yet.** The GPU test (`scripts/gpu_paired.sh`) has not been run on a real GPU. It is ready for three",
              "routes: your own machine with a smart plug, GitHub's GPU machines (`.github/workflows/gpu-bench.yml`), or a",
              "rented cloud GPU (`docs/GPU_RUN_GUIDE.md`). Its result will appear here.", ""]
    sim = ROOT / "results" / "hardware" / "SUMMARY_HELDOUT.json"
    if sim.exists():
        d = json.loads(sim.read_text())
        L += ["## GPU device simulation (THEORETICAL: a model fitted to MLPerf measurements, not a meter)", "",
              f"{d.get('scenarios', '?')} held-out scenarios, seed {d.get('seed', '?')}. Each vessel is one device model.",
              "", "Columns: **A** native (the device's own setting), **S** a fixed manual cap at 70% (common operator "
              "practice), **B** Omni on top, **C** Omni alone. Lower is better for energy, heat, power and response "
              "time; work should be equal.", "",
              "Read honestly: in this model the plain fixed 70% cap (S) saves about as much energy as Omni, but it "
              "breaks the response-time target far more often. Omni's case in the model is the same saving without "
              "the service penalty. The real-GPU test is what checks whether that holds on a real chip.", ""]
        for v, body in d.get("vessels", {}).items():
            means = body.get("means", {})
            arms = list(means)
            keys = sorted({k for a in arms for k, x in means[a].items() if isinstance(x, (int, float))})
            L += [f"### {v}", "", "| Gauge | " + " | ".join(arms) + " |", "|---|" + "---:|" * len(arms)]
            L += [f"| {k} | " + " | ".join(f"{means[a].get(k, float('nan')):.4g}" for a in arms) + " |" for k in keys]
            L.append("")
        shutil.copy(sim, g / "SIMULATION_SUMMARY_HELDOUT.json")
        for f in ("SUMMARY.json", "CALIBRATION_MLPERF.json"):
            if (ROOT / "results" / "hardware" / f).exists():
                shutil.copy(ROOT / "results" / "hardware" / f, g / f"SIMULATION_{f}")
    L += ["## The harness itself", "",
          "`python tests/test_gpu_bench.py` runs the whole GPU test against a stand-in GPU and a stand-in smart plug.",
          "It proves the test, the controls and the validity checks work; the stand-in has no power physics, so its",
          "numbers are not results and are not reported here.", ""]
    (g / "GPU_METRICS.md").write_text("\n".join(L))


def _num(s):
    try:
        return math.isfinite(float(s))
    except (TypeError, ValueError):
        return False


if __name__ == "__main__":
    main(*sys.argv[1:])
