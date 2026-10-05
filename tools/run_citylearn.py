#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Omni-Compass on top of CityLearn's own controller: an independent, recognized simulator we did not write.

CityLearn (Intelligent Environments Lab, University of Texas at Austin; github.com/intelligent-environments-lab/citylearn,
MIT license) simulates districts of real buildings from measured data: each building's load, its solar panels, and its
battery, hour by hour for a year. It ships its own controllers. Its rule-based controller (citylearn.agents.rbc.BasicRBC)
is the native arm: it charges and discharges every battery by the hour of the day.

Arms, the same district, the same year, the same weather and loads:
  native  CityLearn's BasicRBC alone
  omni    the same BasicRBC, with the bowl law (omnicompass/bowl.py) on top of its electric battery commands only (a
          cold or hot water tank is a thermal muscle with its own reading and stays native). The reading is the
          district's draw without its batteries the hour before (the demand the batteries answer, not their own effect); its band is the 10th to the 90th percentile of the
          past week's draw (causal: only hours already seen). The bowl's force moves every battery command the same way:
          a positive force (the district drawing hard) pushes toward discharge, a negative force (a quiet district)
          toward charge, by at most GAIN of the command's range, always inside the battery's own limits [-1, 1]. At
          KILL_AT of the year Omni-Compass hands every command back to the native controller, and the file checks it did

Scored by CityLearn's own evaluation (env.evaluate): every cost function as CityLearn defines it, each the controller's
value over the value with no battery at all (lower is better for every one: cost, electricity, carbon, peaks, ramping,
load factor). Nothing here is scored by Omni-Compass's own code.

  python3 tools/run_citylearn.py --datasets citylearn_challenge_2022_phase_all,... --out results/citylearn
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.bowl import Band, Bowl  # noqa: E402

import os
GAIN = float(os.environ.get("CL_GAIN", 0.5))   # the most the bowl moves a battery command, as a share of its range
# the three settings below were chosen on the tuning district (citylearn_challenge_2022_phase_1) only and frozen before
# any other district ran (docs/CITYLEARN_PREREGISTRATION.md)
TAU = float(os.environ.get("CL_TAU", 1.0))     # the battery's response the bowl is damped for (hours)
SLEW = float(os.environ.get("CL_SLEW", 0.05))  # the most Omni-Compass's adjustment may change in one hour
WINDOW_H = 168      # the band's window: the past week of hourly draw
KILL_AT = 0.9       # Omni-Compass hands every command back at 90% of the year
KPIS = ["cost_total", "electricity_consumption_total", "carbon_emissions_total", "daily_peak_average",
        "all_time_peak_average", "ramping_average", "daily_one_minus_load_factor_average",
        "monthly_one_minus_load_factor_average", "zero_net_energy", "annual_normalized_unserved_energy_total",
        "discomfort_proportion"]
WORDS = {"cost_total": "electricity bill", "electricity_consumption_total": "electricity bought",
         "carbon_emissions_total": "carbon", "daily_peak_average": "daily peak draw", "all_time_peak_average": "highest peak",
         "ramping_average": "ramping (swings hour to hour)", "daily_one_minus_load_factor_average": "daily load unevenness",
         "monthly_one_minus_load_factor_average": "monthly load unevenness", "zero_net_energy": "distance from zero net energy",
         "annual_normalized_unserved_energy_total": "energy not served", "discomfort_proportion": "time uncomfortable"}


def percentile(xs, q):
    s = sorted(xs)
    k = (len(s) - 1) * q
    f = int(math.floor(k)); c = min(f + 1, len(s) - 1)
    return s[f] + (s[c] - s[f]) * (k - f)


def schema_of(name, data_dir):
    if data_dir:
        p = Path(data_dir) / name / "schema.json"
        if p.exists():
            return str(p)
    from citylearn.data import DataSet
    return DataSet().get_schema(name)


def run_arm(schema, arm):
    from citylearn.citylearn import CityLearnEnv
    from citylearn.agents.rbc import BasicRBC
    env = CityLearnEnv(schema, central_agent=True)
    agent = BasicRBC(env)
    obs, _ = env.reset()
    steps = env.time_steps
    kill = int(KILL_AT * steps)
    bowl = None
    hist, moved, handed_back, off = [], 0, True, 0.0
    # one wire, one muscle: the bowl steers only the electric batteries from the district's electricity reading; a cold
    # or hot water tank (cooling_storage, dhw_storage) is a thermal muscle that needs its own reading and stays native
    names = [n for agent in env.action_names for n in agent]
    battery = [n == "electrical_storage" for n in names]
    t0, k = time.time(), 0
    while not env.terminated:
        a = agent.predict(obs)
        if arm == "omni":
            # demand the batteries do not cause: the district's draw without storage, the hour before (the bowl reads the
            # room, not its own heater: a reading that includes the battery feeds every battery move straight back)
            seen = len(env.net_electricity_consumption)
            ws = env.net_electricity_consumption_without_storage
            net = float(ws[seen - 1]) if seen and len(ws) >= seen else None
            if net is not None:
                hist.append(float(net))
            if k < kill and len(hist) >= 24:
                w = hist[-WINDOW_H:]
                lo, hi = percentile(w, 0.10), percentile(w, 0.90)
                if hi - lo > 1e-9:
                    band = Band(lo, hi)
                    if bowl is None:
                        bowl = Bowl(band, dt=1.0, tau=TAU)
                    bowl.band = band
                    f = bowl.force(hist[-1])
                    off += max(-SLEW, min(SLEW, -GAIN * f - off))   # the adjustment glides, never jumps more than SLEW
                    if abs(off) > 1e-12:
                        flat = [x for row in a for x in row]
                        if any(battery):
                            flat = [max(-1.0, min(1.0, x + off)) if b else x for x, b in zip(flat, battery)]
                            a = [flat]
                        moved += 1
            elif k >= kill:
                handed_back = handed_back and True          # from here every command is the native controller's own
        obs, _, _, _, _ = env.step(a)
        k += 1
    ev = env.evaluate()
    d = ev[ev["level"] == "district"].set_index("cost_function")["value"].to_dict()
    return {"arm": arm, "buildings": len(env.buildings), "steps": steps,
            "batteries": sum(battery), "thermal_stores_left_native": sum(1 for n in names if n in ("cooling_storage", "dhw_storage")), "seconds": round(time.time() - t0, 1),
            "moved_hours": moved, "handed_back": handed_back and k >= kill,
            "kpis": {x: (None if (d.get(x) is None or (isinstance(d.get(x), float) and math.isnan(d.get(x)))) else float(d[x]))
                     for x in KPIS}}


def reading(native, omni):
    if native is None or omni is None:
        return "not scored"
    if abs(omni - native) < 1e-9:
        return "same"
    return "better" if omni < native else "WORSE"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--datasets", default="")
    ap.add_argument("--report-only", default="", help="build the report from the per-district files in this folder")
    ap.add_argument("--out", required=True)
    ap.add_argument("--data-dir", default="", help="a local copy of CityLearn's data/datasets (else CityLearn fetches it)")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    try:
        import citylearn
        version = citylearn.__version__
    except ImportError:
        version = "(see each district file)"
    res = {}
    if a.report_only:
        for f in sorted(Path(a.report_only).glob("*.json")):
            res[f.stem] = json.loads(f.read_text())
    for name in [x for x in a.datasets.split(",") if x]:
        schema = schema_of(name, a.data_dir)
        res[name] = {arm: run_arm(schema, arm) for arm in ("native", "omni")}
        res[name]["citylearn_version"] = version
        res[name]["settings"] = {"gain": GAIN, "tau_h": TAU, "glide_per_h": SLEW, "window_h": WINDOW_H, "kill_at": KILL_AT}
        (out / f"{name}.json").write_text(json.dumps(res[name], indent=1) + "\n")
        print(f"== {name}: native {res[name]['native']['seconds']} s, omni {res[name]['omni']['seconds']} s", flush=True)
    L = ["# Omni-Compass on top of CityLearn's own controller", "",
         f"CityLearn {version} (Intelligent Environments Lab, University of Texas at Austin; MIT license): an "
         "independent simulator of real buildings from measured data, with its own controllers and its own scoring. "
         "Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl "
         f"law on top of its battery commands (gain {GAIN}, response {TAU} h, glide {SLEW} an hour, band from the past week's district draw, handed back at "
         f"{int(KILL_AT * 100)}% of the year). Every number is CityLearn's own score: the controller over no battery at "
         "all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).", ""]
    for name, r in res.items():
        n, o = r["native"], r["omni"]
        if name.startswith("citylearn_challenge_2022_phase_1"):
            name += " (the tuning district: not counted in the confirmation)"
        L += [f"## {name}: {n['buildings']} buildings, {n['steps']:,} hours", "",
              f"Omni-Compass moved the commands in {o['moved_hours']:,} hours; every command handed back at "
              f"{int(KILL_AT * 100)}%: {'yes' if o['handed_back'] else 'NO'}.", "",
              "| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |",
              "|---|---:|---:|---:|---|"]
        for x in KPIS:
            nv, ov = n["kpis"][x], o["kpis"][x]
            if nv is None and ov is None:
                continue
            ch = f"{100 * (ov - nv) / abs(nv):+.2f}%" if nv not in (None, 0) and ov is not None else ""
            rd = reading(nv, ov)
            L.append(f"| {WORDS[x]} (`{x}`) | {'' if nv is None else f'{nv:.4f}'} | {'' if ov is None else f'{ov:.4f}'} | {ch} | "
                     f"{rd + (': less ' + WORDS[x] if rd == 'better' else ': more ' + WORDS[x] if rd == 'WORSE' else '')} |")
        L.append("")
    L += ["## Across every district", "",
          "The tuning district is left out of this table.", "",
          "| CityLearn score | Districts better | Districts worse | Mean change |", "|---|---:|---:|---:|"]
    for x in KPIS:
        pairs = [(r["native"]["kpis"][x], r["omni"]["kpis"][x]) for nm, r in res.items() if nm != "citylearn_challenge_2022_phase_1"
                 if r["native"]["kpis"][x] not in (None, 0) and r["omni"]["kpis"][x] is not None]
        if not pairs:
            continue
        b = sum(1 for nv, ov in pairs if ov < nv - 1e-9); w = sum(1 for nv, ov in pairs if ov > nv + 1e-9)
        m = sum(100 * (ov - nv) / abs(nv) for nv, ov in pairs) / len(pairs)
        L.append(f"| {WORDS[x]} | {b} of {len(pairs)} | {w} of {len(pairs)} | {m:+.2f}% |")
    (out / "CITYLEARN.md").write_text("\n".join(L) + "\n")
    sums = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in sorted(out.glob("*.json"))]
    (out / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
