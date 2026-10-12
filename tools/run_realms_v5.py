# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Run the realm harness on Omni v5 at the max and write its tables (results/realms_v5/).

  python3 tools/run_realms_v5.py                      # the preregistered run: seeds 3000-3009, the v5 catalog (1,097), results/realms_v5/
  python3 tools/run_realms_v5.py --seeds 7100 7101 --out /tmp/realms5-dev   # a look on development seeds (never reported)

Two arms, native and omni (Omni-Compass on top of native), on the same seeds. The omni arm is the engine's default, the
max (realms/compass_arm_v5.py, V5CFG): every muscle pushed toward its own limit for the most work, faster, never past its
limit and never below native; the energy that takes is shown as power given. Three panels:

  every muscle alone      each plant with only its own native controller around it (its own natural clock and horizon)
  the organisms           the four realms, the four stacked (each realm's own body on one clock) and the whole tower, on
                          one 15 s clock for an hour around each battery site's daily peak, every plant coupled (the
                          machines' power is heat in the rooms, the body's power swing is load on every site's line):
                          the bone (realms/compass_arm_v5.py, Bone) grants the max only the power the lines and the
                          rooms have room for
  the climb               the same organisms with their work demand stepping by one, up and down (1 2 3 2 3 4 ..., level
                          4 their own load, level 8 twice it): past what native can carry, so the most each arm can do shows

Judged on work and on time over the line (misses); energy is shown, as power given, beside the work it bought. Every plant
inside each organism that did less work or spent more decisions over its line than native is listed, whatever it shows.
Writes MUSCLES_V5.csv, REALMS_V5.json, REALMS_V5.md, RUN.json, SHA256SUMS.txt. Evidence class S (modelled). The
preregistered seeds run only on committed code.
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

from realms.harness import (catalog, run_muscle_arm, run_bodies, Body, paired, paired_organism, interval, scale_load,
                            TOWER, STACK, KILL_AT, WALK)

PREREG_SEEDS = list(range(3000, 3010))
REALMS = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized"]
NAMES = {"compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial",
         "distribution_specialized": "Distribution / Specialized", STACK: "The four stacked, every shared muscle in each",
         TOWER: "The whole tower, every muscle once"}
LABELS = ["MORE WORK AND FEWER MISSES", "MORE WORK", "FEWER MISSES", "SAME AS NATIVE", "MIXED", "WORSE", "INVALID"]
LOADS = {"normal": "the organism's own load", "climb": "the climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it)"}
# the engine and the files it stands on; the engine fingerprint is tools/omni_version.py (OMNI_V5.json)
FROZEN = ["realms", "omnicompass", "tools/run_realms_v5.py"]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def tree_sha(paths):
    h = hashlib.sha256()
    for p in sorted(paths):
        h.update(p.encode()); h.update(sha(ROOT / p).encode())
    return h.hexdigest()


def label_max(per_seed, valid=True):
    """The max's label by rule, judged on work and on time over the line (95% intervals over seeds):
      MORE WORK AND FEWER MISSES   both clear of zero the right way
      MORE WORK / FEWER MISSES     one clear the right way, the other not clear the wrong way
      SAME AS NATIVE               neither clear of zero (no difference beyond the noise)
      MIXED                        one clear the right way, the other clear the wrong way
      WORSE                        one clear the wrong way and nothing clear the right way
      INVALID                      a knob not handed back to native by the lease"""
    if not valid:
        return "INVALID"
    w = interval([c["work"] for c in per_seed])
    v = interval([c["viol_pp"] for c in per_seed])
    more, less = w[1] > 1e-12, w[2] < -1e-12
    fewer, extra = v[2] < -1e-12, v[1] > 1e-12
    good, bad = more or fewer, less or extra
    if bad:
        return "MIXED" if good else "WORSE"
    if more and fewer:
        return "MORE WORK AND FEWER MISSES"
    if more:
        return "MORE WORK"
    if fewer:
        return "FEWER MISSES"
    return "SAME AS NATIVE"


def summarize(per_seed):
    return {k: interval([c[k] for c in per_seed]) for k in ("primary", "work", "energy", "viol_pp")}


def muscle_job(args):
    """Native against the max, per muscle, over the seeds. valid: the lease hands every knob back to native after the
    brain goes silent, proven each seed."""
    row, seeds = args
    nat = [run_muscle_arm(row, s, "native") for s in seeds]
    mx = [run_muscle_arm(row, s, "v5") for s in seeds]
    valid = all(r["restore_ok"] for r in mx)
    per = [paired(a, n) for a, n in zip(mx, nat)]
    return {"row": row, "valid": valid, "label": label_max(per, valid), "summary": summarize(per), "per_seed": per,
            "writes": sum(r["writes"] for r in mx) / len(mx),
            "native_viol_share": sum(n["viol"] / n["steps"] for n in nat) / len(nat),
            "viol_native": sum(n["viol"] for n in nat), "viol_max": sum(m["viol"] for m in mx)}


def plant_harms(arm, nat, ids):
    """Every plant inside the organism that did less work than native or spent more decisions over its line."""
    out = []
    for i, (a, n) in enumerate(zip(arm["plants"], nat["plants"])):
        dw = a["work"] / n["work"] - 1.0 if n["work"] > 0 else 0.0
        dv = a["viol"] - n["viol"]
        if dw < -1e-9 or dv > 0:
            out.append([ids[i], dw, dv])
    return out


def organism_run(name, rows, seed, arm, load):
    """One organism, one arm, one load. The four stacked keep each realm's own body on one clock, so every muscle in the
    stack runs exactly the native it runs in its own realm, plant by plant (the founder's order: the native identical in
    all six)."""
    if name == STACK:
        bodies = [Body(rs, seed) for rs in rows]
    else:
        bodies = [Body(rows, seed)]
    if load != "normal":
        for b in bodies:
            scale_load(b, load)
    return run_bodies(bodies, arm, [list(range(len(bodies)))])


def organism_job(args):
    name, rows, seed, load = args
    ids = ([f"{r['muscle_id']}@{realm}" for realm, rs in zip(REALMS, rows) for r in rs] if name == STACK
           else [r["muscle_id"] for r in rows])
    nat = organism_run(name, rows, seed, "native", load)
    mx = organism_run(name, rows, seed, "v5", load)
    vn = sum(p["viol"] for p in nat["plants"]); vm = sum(p["viol"] for p in mx["plants"])
    return name, seed, load, {"max": paired_organism(mx, nat), "restore_ok": mx["restore_ok"],
                              "harms": plant_harms(mx, nat, ids), "viol_native": vn, "viol_max": vm,
                              "steps": sum(p["steps"] for p in nat["plants"])}


def fmt(m, scale=100.0, unit="%"):
    return f"{m[0] * scale:+.2f}{unit} ({m[1] * scale:+.2f} to {m[2] * scale:+.2f})"


def misses_line(o):
    vn, vm, st = o["viol_native"], o["viol_max"], o["steps"]
    cut = (1.0 - vm / vn) * 100.0 if vn else 0.0
    return f"{100.0 * vn / st:.2f}% → {100.0 * vm / st:.2f}% ({'−' if cut >= 0 else '+'}{abs(cut):.1f}%)"


def write_md(out, res, orgs, run):
    L = []
    w = L.append
    w(f"# The realms on Omni v5 at the max: {len(res)} muscles and six organisms, native against Omni on top")
    w("")
    w(f"Evidence class **S** (modelled). Run {run['started']}, commit `{run['commit'][:12]}`, seeds "
      f"{run['seeds'][0]}-{run['seeds'][-1]} ({len(run['seeds'])} paired seeds per muscle, per organism and per load), "
      f"catalog `{run['catalog']}`. The engine is **omni-v5** (`tools/omni_version.py`, `OMNI_V5.json`) at its default, "
      "**the max** (`realms/compass_arm_v5.py`, `V5CFG`), on top of each plant's own native controller. Harness `realms/`.")
    w("")
    w("**The max.** Every muscle is pushed toward its own limit for the most work, faster: a pool's machines are started "
      "before the rush lands (the recent peak arrivals widened by the largest rise the pool has shown within one machine "
      "start, at 95% utilisation), never fewer than its twin runs (the brain's model of native: the same pool under its "
      "own autoscaler alone, on the same arrivals); a room is cooled ahead of the heat as it nears its limit or its cooling "
      "nears flat out; a battery's line is clipped from its charge, a UPS lending only the charge above its outage floor. "
      "A muscle native already runs flat out (full clock, full speed, full actuator) is wired, watched and native: there "
      "is nothing above native to give it. Nothing is taken from one muscle to give to another; the max never shaves. "
      "The energy the max takes is reported as **power given**, beside the work and the speed it bought.")
    w("")
    w("**The bone.** Inside an organism the max may give only the power the body can carry: a site's grid line and a "
      "room's cooling are loaded by the whole body (the machines' power is heat in every room, the body's power swing is "
      "load on every site's line), so machines and cooling are granted out of the room the most loaded line has left, "
      "read one decision ahead (its latest reading plus the larger of 3.09 of its own step-to-step wobbles and the largest "
      "single climb it has shown). With no room, every pool goes at once to exactly its twin's machines (a floor and a "
      "ceiling at native's count: what the max added goes back, nothing native has is taken). The organisms run the hour "
      "around each battery site's daily peak, where the UPS lines carry most of their rating: the bone is tight there, "
      "and the max gives only what it can carry.")
    w("")
    w(f"**The lease.** At {int(KILL_AT * 100)}% of every run the brain is cut; the plug walks every setting back to "
      f"native over {WALK} decisions (a jump the body would have to absorb at once is the swing the founder ordered "
      "gone), and the run goes on native until it ends; every knob must be back at the operator's own before then "
      "(valid). The security kill switch is instant (`omnicompass/master.py`).")
    w("")
    w("These are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not "
      "an independent test. What a row shows is whether the max, applied to that knob, helps or hurts the model.")
    w("")
    for load in run["loads"]:
        w(f"## The six organisms: {LOADS[load]}")
        w("")
        w("Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant "
          "decisions over their line, native → omni (the change in misses). Power given: the organism's energy against "
          "native's. 95% intervals over seeds.")
        w("")
        w("| Organism | Muscles | Label | Work | Misses, native → omni | Misses (pp) | Power given | Work per energy | Valid |")
        w("|---|---:|---|---:|---|---:|---:|---:|---|")
        for name in [n for n in REALMS + [STACK, TOWER] if n in orgs[load]]:
            o = orgs[load][name]; s = o["summary"]
            w(f"| {NAMES[name]} | {o['n']} | **{o['label']}** | {fmt(s['work'], 100.0)} | {misses_line(o['totals'])} | "
              f"{fmt(s['viol_pp'], 1.0, '')} | {fmt(s['energy'])} | {fmt(s['primary'])} | {'yes' if o['valid'] else 'NO'} |")
        w("")
    w("## Inside the organisms: every plant that did worse than native")
    w("")
    w("A stricter look than an organism's total: every plant inside each organism, over all seeds, that did less work "
      "than native or spent more decisions over its own line, under each load. Reported whatever it shows.")
    w("")
    w("| Load | Organism | Plants | Plants worse | The plants (work change, extra decisions over the line, all seeds) |")
    w("|---|---|---:|---:|---|")
    for load in run["loads"]:
        for name in [n for n in REALMS + [STACK, TOWER] if n in orgs[load]]:
            o = orgs[load][name]; h = o["plants_worse"]
            lst = "; ".join(f"{mid} ({v[0] * 100:+.3f}%, {v[1]:+d})" for mid, v in sorted(h.items(), key=lambda kv: kv[1][0])) or "none"
            w(f"| {load} | {NAMES[name]} | {o['n']} | {len(h)} | {lst} |")
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
    w("## Every muscle alone, by kind of plant and knob")
    w("")
    w("| Plant | Knob | Muscles | Omni acts on | Misses, native → omni | Work | Power given |")
    w("|---|---|---:|---:|---|---:|---:|")
    groups = defaultdict(list)
    for r in res:
        groups[(r["row"]["template"], r["row"]["knob"])].append(r)
    for (t, k), rs in sorted(groups.items()):
        steps = sum(len(r["per_seed"]) for r in rs)
        vn = sum(r["viol_native"] for r in rs); vm = sum(r["viol_max"] for r in rs)
        share = lambda v: 100.0 * v / max(1, sum(r["steps_total"] for r in rs))
        wk = sum(r["summary"]["work"][0] for r in rs) / len(rs)
        en = sum(r["summary"]["energy"][0] for r in rs) / len(rs)
        w(f"| {t} | {k} | {len(rs)} | {sum(1 for r in rs if r['writes'] > 0)} | {share(vn):.2f}% → {share(vm):.2f}% | "
          f"{wk * 100:+.3f}% | {en * 100:+.2f}% |")
    w("")
    w("## No-harm check")
    w("")
    worse = [r for r in res if r["label"] in ("WORSE", "MIXED")]
    acted = sum(1 for r in res if r["writes"] > 0)
    w(f"- Omni acts on **{acted}** of {len(res)} muscles alone; the rest are wired and watched and held native (native "
      "already runs them flat out, or their knob gives nothing above native).")
    w(f"- Muscles alone labelled **WORSE** or **MIXED**: **{len(worse)}**"
      + ("." if not worse else ": " + ", ".join(f"{r['row']['muscle']} ({r['row']['knob']}, {r['label']})" for r in worse) + "."))
    w("- The lease hands every knob back to native before each run ends: "
      f"{sum(1 for r in res if r['valid'])} of {len(res)} muscles; "
      + ", ".join(f"{sum(1 for o in orgs[load].values() if o['valid'])} of {len(orgs[load])} organisms under {load}"
                  for load in run["loads"]) + ".")
    w("")
    w("## Largest changes (muscles alone, by mean change in misses)")
    w("")
    srt = sorted(res, key=lambda r: r["summary"]["viol_pp"][0])
    w("| Muscle | Family | Knob | Label | Misses (pp) | Work | Power given |")
    w("|---|---|---|---|---:|---:|---:|")
    for r in srt[:10] + srt[-10:][::-1]:
        s = r["summary"]
        w(f"| {r['row']['muscle']} | {r['row']['family']} | {r['row']['knob']} | {r['label']} | {fmt(s['viol_pp'], 1.0, '')} | "
          f"{fmt(s['work'])} | {fmt(s['energy'])} |")
    w("")
    w("Raw per-seed contrasts: `REALMS_V5.json`. One row per muscle: `MUSCLES_V5.csv`. Fingerprints: `RUN.json`, "
      "`SHA256SUMS.txt`.")
    (out / "REALMS_V5.md").write_text("\n".join(_legal_stamp(L)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", type=int, nargs="+", default=PREREG_SEEDS)
    ap.add_argument("--out", default=str(ROOT / "results" / "realms_v5"))
    ap.add_argument("--catalog", default=str(ROOT / "realms" / "catalog_v5.csv"))   # the v5 muscle set (1,097)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--loads", default="normal,climb", help="organism loads, comma separated (normal, climb)")
    ap.add_argument("--limit", type=int, default=0, help="first N muscles only (a look; never reported)")
    a = ap.parse_args(argv)
    loads = [x for x in a.loads.split(",") if x]
    prereg = (a.seeds == PREREG_SEEDS and not a.limit and a.catalog == str(ROOT / "realms" / "catalog_v5.csv")
              and loads == ["normal", "climb"])
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
           "preregistered": prereg, "dirty": bool(dirty), "muscles": len(rows), "engine": "omni-v5", "dial": "max",
           "loads": loads, "kill_at": KILL_AT, "walk": WALK,
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
        jobs = [(name, rs, s, load) for load in loads for name, rs in groups.items() if rs for s in a.seeds]
        raw = defaultdict(lambda: defaultdict(dict))
        for name, seed, load, o in ex.map(organism_job, jobs):
            raw[load][name][seed] = o
    print(f"organisms done in {time.time() - t0:.0f} s", flush=True)
    for r in res:
        r["steps_total"] = 0
    # the steps each muscle alone ran (for the share of decisions over the line in the plant/knob table)
    from realms.presets import STEPS_SINGLE
    for r in res:
        r["steps_total"] = STEPS_SINGLE[r["row"]["template"]] * len(a.seeds)
    orgs = {}
    for load, by_name in raw.items():
        orgs[load] = {}
        for name, by_seed in by_name.items():
            runs = [by_seed[s] for s in a.seeds]
            valid = all(o["restore_ok"] for o in runs)
            per = [o["max"] for o in runs]
            agg = defaultdict(lambda: [0.0, 0, 0])
            for o in runs:
                for mid, dw, dv in o["harms"]:
                    agg[mid][0] += dw / len(runs)
                    agg[mid][1] += dv
                    agg[mid][2] += 1
            harms = {mid: v for mid, v in agg.items() if v[0] < -1e-9 or v[1] > 0}
            orgs[load][name] = {"n": sum(len(g) for g in groups[name]) if name == STACK else len(groups[name]),
                                "valid": valid, "label": label_max(per, valid), "summary": summarize(per),
                                "per_seed": per, "plants_worse": harms,
                                "totals": {"viol_native": sum(o["viol_native"] for o in runs),
                                           "viol_max": sum(o["viol_max"] for o in runs),
                                           "steps": sum(o["steps"] for o in runs)}}
    run["elapsed_s"] = round(time.time() - t0)
    with (out / "MUSCLES_V5.csv").open("w", newline="") as f:
        cols = ["muscle_id", "family", "muscle", "realm", "template", "preset", "knob", "label", "work", "work_lo",
                "work_hi", "viol_pp", "viol_pp_lo", "viol_pp_hi", "power_given", "work_per_energy", "writes_per_run",
                "native_viol_share", "valid"]
        wr = csv.writer(f); wr.writerow(cols)
        for r in res:
            s, row = r["summary"], r["row"]
            wr.writerow([row["muscle_id"], row["family"], row["muscle"], row["realm"], row["template"], row["preset"],
                         row["knob"], r["label"], *(f"{x:.5f}" for x in s["work"]), *(f"{x:.3f}" for x in s["viol_pp"]),
                         f"{s['energy'][0]:.5f}", f"{s['primary'][0]:.5f}", f"{r['writes']:.1f}",
                         f"{r['native_viol_share']:.4f}", r["valid"]])
    (out / "REALMS_V5.json").write_text(json.dumps({"run": run, "organisms": orgs, "muscles": res}, indent=1) + "\n")
    (out / "RUN.json").write_text(json.dumps(run, indent=1) + "\n")
    write_md(out, res, orgs, run)
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt")
    (out / "SHA256SUMS.txt").write_text("".join(f"{sha(p)}  {p.name}\n" for p in files))
    print((out / "REALMS_V5.md").read_text().split("## Inside the organisms")[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
