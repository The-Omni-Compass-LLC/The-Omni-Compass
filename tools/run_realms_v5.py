# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Run the realm harness on the Omni v5 law and write its tables (results/realms_v5/).

  python3 tools/run_realms_v5.py                      # the preregistered run: seeds 3000-3009, the v5 catalog (1,002), results/realms_v5/
  python3 tools/run_realms_v5.py --seeds 0 1 --out /tmp/realms5-dev   # a look on development seeds (never reported)
  python3 tools/run_realms_v5.py --catalog realms/catalog.csv         # the v3 muscle set (945) on the v5 law, for comparison

Every muscle alone, native against the v5 law (realms/compass_arm_v5.py, the engine's default V5CFG), then the six
organisms (the four realms, the four stacked with every shared muscle in each, the whole tower), each with native, the v5
law and the v3 law (realms/compass_arm.py) on the same seeds, and every plant inside each organism checked for any work
lost or any extra time over its line. The v5 law carries the two math-only guardrails (the edge, the centre/hole) and holds
a knob native only where its own physics says moving it cannot help without harm (an interactive pool's power cap, a
battery's shave, a cloud pool's machine hand-back). Writes MUSCLES_V5.csv, REALMS_V5.json, REALMS_V5.md, RUN.json,
SHA256SUMS.txt. Evidence class S (modelled). The preregistered seeds run only on committed code.
"""
import argparse, csv, hashlib, json, os, subprocess, sys, time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    from tools.legal import stamp as _legal_stamp
except ImportError:
    from tools.legal import stamp as _legal_stamp  # pragma: no cover

from realms.harness import (catalog, run_muscle_arm, run_organism_arm, run_bodies, Body, paired, paired_organism,
                            label, summarize, TOWER, STACK)

PREREG_SEEDS = list(range(3000, 3010))
REALMS = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized"]
NAMES = {"compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial",
         "distribution_specialized": "Distribution / Specialized", STACK: "The four stacked, every shared muscle in each",
         TOWER: "The whole tower, every muscle once"}
LABELS = ["SUPERIOR WITHIN GUARDRAILS", "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF", "NONINFERIOR / INCONCLUSIVE",
          "NOT ESTABLISHED", "WORSE", "INVALID"]
# the v5 law and the files it stands on; the engine fingerprint is tools/omni_version.py (OMNI_V5.json)
FROZEN = ["realms", "omnicompass", "tools/run_realms_v5.py"]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def tree_sha(paths):
    h = hashlib.sha256()
    for p in sorted(paths):
        h.update(p.encode()); h.update(sha(ROOT / p).encode())
    return h.hexdigest()


def muscle_job(args):
    """Native against the v5 law, per muscle, over the seeds. valid: the v5 arm hands every knob back to native on the
    kill (the dead-man lease), proven each seed."""
    row, seeds = args
    nat = [run_muscle_arm(row, s, "native") for s in seeds]
    v5 = [run_muscle_arm(row, s, "v5") for s in seeds]
    valid = all(r["restore_ok"] for r in v5)
    per = [paired(a, n) for a, n in zip(v5, nat)]
    return {"row": row, "valid": valid, "label": label(per, valid), "summary": summarize(per), "per_seed": per,
            "writes": sum(r["writes"] for r in v5) / len(v5),
            "native_viol_share": sum(n["viol"] / n["steps"] for n in nat) / len(nat)}


def plant_harms(arm, nat, ids):
    """Every plant inside the organism that did less work than native or spent more decisions over its line."""
    out = []
    for i, (a, n) in enumerate(zip(arm["plants"], nat["plants"])):
        dw = a["work"] / n["work"] - 1.0 if n["work"] > 0 else 0.0
        dv = a["viol"] - n["viol"]
        if dw < -1e-9 or dv > 0:
            out.append([ids[i], dw, dv])
    return out


def organism_run(name, rows, seed, arm):
    """One organism, one arm. The four stacked keep each realm's own body on one clock, so every muscle in the stack runs
    exactly the native it runs in its own realm, plant by plant (the founder's order: the native identical in all six)."""
    if name == STACK:
        bodies = [Body(rs, seed) for rs in rows]
        return run_bodies(bodies, arm, [list(range(len(bodies)))])
    return run_organism_arm(rows, seed, arm)


def organism_job(args):
    name, rows, seed = args
    ids = ([f"{r['muscle_id']}@{realm}" for realm, rs in zip(REALMS, rows) for r in rs] if name == STACK
           else [r["muscle_id"] for r in rows])
    nat = organism_run(name, rows, seed, "native")
    v5 = organism_run(name, rows, seed, "v5")
    v3 = organism_run(name, rows, seed, "compass")
    return name, seed, {"v5": paired_organism(v5, nat), "v3": paired_organism(v3, nat), "restore_ok": v5["restore_ok"],
                        "harms_v5": plant_harms(v5, nat, ids), "harms_v3": plant_harms(v3, nat, ids)}


def fmt(m, scale=100.0, unit="%"):
    return f"{m[0] * scale:+.1f}{unit} ({m[1] * scale:+.1f} to {m[2] * scale:+.1f})"


def write_md(out, res, orgs, run):
    L = []
    w = L.append
    w(f"# The realms on Omni v5: {len(res)} muscles on modelled plants, native against the v5 law on top")
    w("")
    w(f"Evidence class **S** (modelled). Run {run['started']}, commit `{run['commit'][:12]}`, seeds "
      f"{run['seeds'][0]}-{run['seeds'][-1]} ({len(run['seeds'])} paired seeds per muscle and per organism), catalog "
      f"`{run['catalog']}`. The engine is **omni-v5** (`tools/omni_version.py`, `OMNI_V5.json`): the v5 compass law "
      "`realms/compass_arm_v5.py` at its default `V5CFG`, on top of each plant's own native controller. Harness `realms/`.")
    w("")
    w("The v5 law carries two math-only guardrails: the **edge** (a per-knob cushion from how fast service has climbed "
      "and how far it wobbles, so nothing riding its limit falls off) and the **centre/hole** (a machine or a cooled zone "
      "is eased only while it can still climb back). Otherwise every knob is free, and a knob stays native wherever the "
      "law cannot improve it without harm. Every process loop moves inside its band, generating units included, but never "
      "closer to its band's edge than its own largest swing toward that edge (the loop reach); a cooled zone never warmer "
      "than its cooling can recover, nor while its cooling headroom is falling toward empty; a power cap only on a pool whose "
      "response line outlasts one decision (an interactive pool's cap is proven on the metered GPU, class P, not here), never "
      "below the largest jump in demand nor past the line; the battery shave and a cloud pool's machine hand-back held native "
      "(round-trip energy bought for service; a hand-back the autoscaler never undoes).")
    w("")
    w("Amendment (12 Oct): this table replaces the first v5 table (commit `c0e80a852`, the whole tower +0.0%). That engine "
      "held every generating unit's loop, every power cap and every inverter native by blanket gates, which threw away "
      "most of what v5 saves. v5 was re-declared with those gates replaced by physics floors (the loop reach, the cooling "
      "headroom's fall read ahead, the latency floor, the power cap only where a pool's line outlasts a decision, a cloud "
      "pool's machine hand-back left to its autoscaler, a motion axis slowed only while the wake forecast over a whole "
      "deadline still finishes inside it), developed on seeds 7100-7209 only; the preregistered seeds 3000-3009 are run "
      "again unchanged.")
    w("")
    w("Primary outcome: work per energy, v5 against native, with its 95% interval over seeds. Guardrails: work not lower "
      "by more than 1%, share of periods in violation not higher by more than 1 percentage point. Labels by rule. These "
      "are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an "
      "independent test. What a row shows is whether the v5 law, applied to that knob, helps or hurts the model.")
    w("")
    w("## The six organisms")
    w("")
    w("Native, the v5 law and the v3 law on the same seeds. Energy saved is native's energy minus the arm's, as a share of "
      "native's (95% interval over seeds); times v3 is v5's saving over v3's. The four stacked keep each realm's own body "
      "on one clock, so every muscle in the stack runs exactly the native it runs in its own realm, plant by plant: the "
      "native is identical in all six.")
    w("")
    w("| Organism | Muscles | Label | Work per energy | Work | Energy saved, v5 | Energy saved, v3 | Times v3 | "
      "Violations (pp) | Valid |")
    w("|---|---:|---|---:|---:|---:|---:|---:|---:|---|")
    for name in [n for n in REALMS + [STACK, TOWER] if n in orgs]:
        o = orgs[name]; s = o["summary"]; s3 = o["v3"]["summary"]
        e5, e3 = -s["energy"][0], -s3["energy"][0]
        saved = lambda m: f"{-m[0] * 100:.2f}% ({-m[2] * 100:.2f} to {-m[1] * 100:.2f})"
        times = f"{e5 / e3:.1f}x" if e3 > 0 else "n/a"
        w(f"| {NAMES[name]} | {o['n']} | **{o['label']}** | {fmt(s['primary'])} | {fmt(s['work'])} | "
          f"{saved(s['energy'])} | {saved(s3['energy'])} | {times} | {fmt(s['viol_pp'], 1.0, '')} | "
          f"{'yes' if o['valid'] else 'NO'} |")
    w("")
    w("## Inside the organisms: every plant that did worse than native")
    w("")
    w("A stricter look than the organism's total: every plant inside each organism, over all seeds, that did less work "
      "than native or spent more decisions over its own line, for v5 and for v3. Reported whatever it shows. A plant can do "
      "worse without Omni ever touching it: the body couples its plants (heat into rooms, the body's power swing onto its "
      "UPS and distribution), so a move on one muscle reaches the others. Holding the body's shared lines (its UPS and "
      "distribution) as one gauge every move answers to is the next engine item.")
    w("")
    w("| Organism | Plants | Plants worse, v5 | Plants worse, v3 | The v5 plants (work change, extra decisions over the line, all seeds) |")
    w("|---|---:|---:|---:|---|")
    for name in [n for n in REALMS + [STACK, TOWER] if n in orgs]:
        o = orgs[name]; h5, h3 = o["plants_worse"]["v5"], o["plants_worse"]["v3"]
        lst = "; ".join(f"{mid} ({v[0] * 100:+.3f}%, {v[1]:+d})" for mid, v in sorted(h5.items(), key=lambda kv: kv[1][0])) or "none"
        w(f"| {NAMES[name]} | {o['n']} | {len(h5)} | {len(h3)} | {lst} |")
    w("")
    w("## Every muscle alone, by home realm")
    w("")
    w("| Realm | Muscles | " + " | ".join(LABELS) + " |")
    w("|---|---:|" + "---:|" * len(LABELS))
    for realm in REALMS:
        rs = [r for r in res if r["row"]["realm"] == realm]
        c = Counter(r["label"] for r in rs)
        w(f"| {NAMES[realm]} | {len(rs)} | " + " | ".join(str(c.get(l, 0)) for l in LABELS) + " |")
    c = Counter(r["label"] for r in res)
    w(f"| **All** | {len(res)} | " + " | ".join(f"**{c.get(l, 0)}**" for l in LABELS) + " |")
    w("")
    w("## No-harm check: muscles worse than native on any axis")
    w("")
    worse = [r for r in res if r["label"] == "WORSE"]
    acted = sum(1 for r in res if r["writes"] > 0)
    w(f"- Omni acts on **{acted}** of {len(res)} muscles; the rest are wired and watched but held native (no signal "
      "pushed where none helps).")
    w(f"- Muscles labelled **WORSE**: **{len(worse)}**"
      + ("." if not worse else ": " + ", ".join(f"{r['row']['muscle']} ({r['row']['knob']})" for r in worse) + "."))
    w("- The v5 arm hands every knob back to native on the kill (the dead-man lease): "
      f"{sum(1 for r in res if r['valid'])} of {len(res)} muscles, "
      f"{sum(1 for o in orgs.values() if o['valid'])} of {len(orgs)} organisms.")
    w("")
    w("## Largest gains and largest losses (single muscles, by mean work per energy)")
    w("")
    srt = sorted(res, key=lambda r: r["summary"]["primary"][0])
    w("| Muscle | Family | Knob | Label | Work per energy | Work | Violations (pp) |")
    w("|---|---|---|---|---:|---:|---:|")
    for r in srt[-10:][::-1] + srt[:10]:
        s = r["summary"]
        w(f"| {r['row']['muscle']} | {r['row']['family']} | {r['row']['knob']} | {r['label']} | {fmt(s['primary'])} | "
          f"{fmt(s['work'])} | {fmt(s['viol_pp'], 1.0, '')} |")
    w("")
    w("Raw per-seed contrasts: `REALMS_V5.json`. One row per muscle: `MUSCLES_V5.csv`. Fingerprints: `RUN.json`, "
      "`SHA256SUMS.txt`.")
    (out / "REALMS_V5.md").write_text("\n".join(_legal_stamp(L)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", type=int, nargs="+", default=PREREG_SEEDS)
    ap.add_argument("--out", default=str(ROOT / "results" / "realms_v5"))
    ap.add_argument("--catalog", default=str(ROOT / "realms" / "catalog_v5.csv"))   # the v5 muscle set (1,002)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--limit", type=int, default=0, help="first N muscles only (a look; never reported)")
    a = ap.parse_args(argv)
    prereg = a.seeds == PREREG_SEEDS and not a.limit and a.catalog == str(ROOT / "realms" / "catalog_v5.csv")
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + FROZEN, cwd=ROOT, capture_output=True,
                           text=True).stdout.strip()
    if prereg and dirty:
        print("the preregistered seeds run only on committed code; uncommitted changes in:\n" + dirty)
        return 1
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows = catalog(a.catalog)
    if a.limit:
        rows = rows[:a.limit]
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    frozen_files = [str(p.relative_to(ROOT)) for d in ("realms", "omnicompass") for p in sorted((ROOT / d).rglob("*"))
                    if p.is_file() and p.suffix in (".py", ".csv", ".json")]
    run = {"started": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "commit": commit, "seeds": a.seeds,
           "preregistered": prereg, "dirty": bool(dirty), "muscles": len(rows), "engine": "omni-v5",
           "catalog": str(Path(a.catalog).relative_to(ROOT)) if Path(a.catalog).is_absolute() else a.catalog,
           "frozen_tree_sha256": tree_sha(frozen_files + ["tools/run_realms_v5.py"]),
           "law_sha256": sha(ROOT / "realms" / "compass_arm_v5.py")}
    t0 = time.time()
    with ProcessPoolExecutor(a.workers) as ex:
        res = list(ex.map(muscle_job, [(r, a.seeds) for r in rows], chunksize=4))
        print(f"muscles: {len(res)} in {time.time() - t0:.0f} s", flush=True)
        groups = {realm: [r for r in rows if realm in r["realms"].split(";")] for realm in REALMS}
        groups[STACK] = [groups[realm] for realm in REALMS]           # each realm's own body, the realm's own native
        groups[TOWER] = rows
        jobs = [(name, rs, s) for name, rs in groups.items() if rs for s in a.seeds]
        raw = defaultdict(dict)
        for name, seed, o in ex.map(organism_job, jobs):
            raw[name][seed] = o
    print(f"organisms done in {time.time() - t0:.0f} s", flush=True)
    orgs = {}
    for name, by_seed in raw.items():
        runs = [by_seed[s] for s in a.seeds]
        valid = all(o["restore_ok"] for o in runs)
        per = [o["v5"] for o in runs]
        per3 = [o["v3"] for o in runs]
        harms = {}
        for arm in ("v5", "v3"):
            agg = defaultdict(lambda: [0.0, 0, 0])
            for o in runs:
                for mid, dw, dv in o["harms_" + arm]:
                    agg[mid][0] += dw / len(runs)
                    agg[mid][1] += dv
                    agg[mid][2] += 1
            harms[arm] = {mid: v for mid, v in agg.items() if v[0] < -1e-9 or v[1] > 0}
        orgs[name] = {"n": sum(len(g) for g in groups[name]) if name == STACK else len(groups[name]), "valid": valid, "label": label(per, valid), "summary": summarize(per),
                      "per_seed": per, "v3": {"label": label(per3, True), "summary": summarize(per3), "per_seed": per3},
                      "plants_worse": harms}
    run["elapsed_s"] = round(time.time() - t0)
    with (out / "MUSCLES_V5.csv").open("w", newline="") as f:
        cols = ["muscle_id", "family", "muscle", "realm", "template", "preset", "knob", "label", "primary", "primary_lo",
                "primary_hi", "work", "work_lo", "energy", "viol_pp", "viol_pp_hi", "writes_per_run",
                "native_viol_share", "valid"]
        wr = csv.writer(f); wr.writerow(cols)
        for r in res:
            s, row = r["summary"], r["row"]
            wr.writerow([row["muscle_id"], row["family"], row["muscle"], row["realm"], row["template"], row["preset"],
                         row["knob"], r["label"], *(f"{x:.5f}" for x in s["primary"]), f"{s['work'][0]:.5f}",
                         f"{s['work'][1]:.5f}", f"{s['energy'][0]:.5f}", f"{s['viol_pp'][0]:.3f}",
                         f"{s['viol_pp'][2]:.3f}", f"{r['writes']:.1f}", f"{r['native_viol_share']:.4f}", r["valid"]])
    (out / "REALMS_V5.json").write_text(json.dumps({"run": run, "organisms": orgs, "muscles": res}, indent=1) + "\n")
    (out / "RUN.json").write_text(json.dumps(run, indent=1) + "\n")
    write_md(out, res, orgs, run)
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt")
    (out / "SHA256SUMS.txt").write_text("".join(f"{sha(p)}  {p.name}\n" for p in files))
    print((out / "REALMS_V5.md").read_text().split("## Every muscle")[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
