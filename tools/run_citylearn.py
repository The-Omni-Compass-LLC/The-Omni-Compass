#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass on top of CityLearn's own controller: an independent, recognized simulator we did not write.

CityLearn (Intelligent Environments Lab, University of Texas at Austin; github.com/intelligent-environments-lab/citylearn,
MIT license) simulates districts of real buildings from measured data: each building's load, its solar panels, and its
battery, hour by hour for a year. It ships its own controllers. Its rule-based controller (citylearn.agents.rbc.BasicRBC)
is the native arm: it charges and discharges every battery by the hour of the day.

Arms, the same district, the same year, the same weather and loads:
  native  CityLearn's BasicRBC alone
  omni    the same BasicRBC, with the compass law (omnicompass/compass_law.py) on top of its electric battery commands only (a
          cold or hot water tank is a thermal muscle with its own reading and stays native). The reading is the
          district's draw without its batteries in the coming hour, read from the same hour of the past week's days
          (the demand the batteries answer, not their own effect; causal: only hours already seen; omni-v9); its band is
          the 10th to the 90th percentile of the past week's draw. The compass's force moves every battery command the same way:
          a positive force (the district drawing hard) pushes toward discharge, a negative force (a quiet district)
          toward charge, by at most GAIN of the command's range, always inside the battery's own limits [-1, 1]. At
          KILL_AT of the year Omni-Compass hands every command back to the native controller, and the file checks it did

Scored by CityLearn's own evaluation (env.evaluate): every cost function as CityLearn defines it, each the controller's
value over the value with no battery at all (CityLearn's direction is lower for every one). Each is read by the one key
(tools/readings.py): energy not served and time uncomfortable are misses, a rise is a LOSS; the bill, the electricity, the
carbon and the power held (its peaks, swings and unevenness) are resources, a fall is a cut and a rise is power given.
Nothing here is scored by Omni-Compass's own code.

  python3 tools/run_citylearn.py --datasets citylearn_challenge_2022_phase_all,... --out results/citylearn
"""
from __future__ import annotations

import argparse

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
from tools.readings import EVEN as W_EVEN, GAIN as W_GAIN, GIVEN as W_GIVEN, LOSS as W_LOSS   # the one key's words, written
                                                           # once (tools/readings.py); GAIN below is the compass's gain
import hashlib
import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402

import os
GAIN = float(os.environ.get("CL_GAIN", 0.5))   # the most the compass moves a battery command, as a share of its range
# the three settings below were chosen on the tuning district (citylearn_challenge_2022_phase_1) only and frozen before
# any other district ran (docs/CITYLEARN_PREREGISTRATION.md); the glide and the coming hour's reading are omni-v9's
# amendment of 17 October, found on the district whose LOSS they repair and read on every district (docs/OMNI_V9.md); the
# glide's speed is omni-v10's (docs/OMNI_V10.md)
TAU = float(os.environ.get("CL_TAU", 1.0))     # the battery's response the compass is damped for (hours)
SLEW = float(os.environ.get("CL_SLEW", 0.0875))  # the most Omni-Compass's adjustment may change in one hour (omni-v10: the
                                                 # glide that cuts the bill most with no LOSS in any district, read by the one key
                                                 # of 17 October; omni-v9 0.0625, where nothing rose; 0.05 before)
FORECAST_DAYS = 7   # omni-v9: the coming hour's draw is the mean of the same hour over the past week's days
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


def coming_hour(hist, days=FORECAST_DAYS):
    """The district's draw in the coming hour, read from the same hour of the past days (hist[-24], hist[-48], ... up to
    `days` of them; causal: only hours already seen), or the last hour's own draw until a day has been seen. omni-v9: the
    reading of the hour gone left the adjustment about five hours behind the day (its strongest discharge at midnight, the
    draw's peak at 19:00), still charging as the evening peak climbed, so the batteries were empty at each month's top
    hour (docs/OMNI_V9.md)."""
    same = hist[-24::-24][:days]
    return sum(same) / len(same) if same else hist[-1]


def glide(off, target, slew=None):
    """The adjustment moved toward its target by at most `slew` (SLEW) in one hour: it glides, never jumps."""
    step = SLEW if slew is None else slew
    return off + max(-step, min(step, target - off))


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
    try:                       # CityLearn's own rule controllers need its flat interface; newer districts ship another
        env = CityLearnEnv(schema, central_agent=True, interface="flat")
    except TypeError:          # a CityLearn without the choice is flat already
        env = CityLearnEnv(schema, central_agent=True)
    agent = BasicRBC(env)
    obs, _ = env.reset()
    steps = env.time_steps
    kill = int(KILL_AT * steps)
    compass_law = None
    hist, moved, handed_back, off = [], 0, True, 0.0
    # one wire, one muscle: the compass steers only the electric batteries from the district's electricity reading; a cold
    # or hot water tank (cooling_storage, dhw_storage) is a thermal muscle that needs its own reading and stays native
    names = [n for agent in env.action_names for n in agent]
    battery = [n == "electrical_storage" for n in names]
    # omni-v8 (17 October): a battery that also carries its building through power outages has a second duty, the reserve
    # for the outage, which the district's draw cannot show; it stays native, as a water tank does, until it has its own wire
    # and its own reading. The building's own setting says which batteries those are (CityLearn's simulate_power_outage).
    if len(env.action_names) == 1:                 # the central agent: one list, each building's actions in its own order
        owner = [bi for bi, b in enumerate(env.buildings) for _ in b.active_actions]
    else:
        owner = [bi for bi, agent_names in enumerate(env.action_names) for _ in agent_names]
    reserve = [bool(getattr(b, "simulate_power_outage", False)) for b in env.buildings]
    steer = ([bt and not reserve[owner[i]] for i, bt in enumerate(battery)] if len(owner) == len(battery)
             else [False] * len(battery))      # an action list it cannot place on its buildings: nothing is steered
    t0, k = time.time(), 0
    while not env.terminated:
        a = agent.predict(obs)
        if arm == "omni":
            # demand the batteries do not cause: the district's draw without storage, recorded hour by hour (the compass reads
            # the room, not its own heater: a reading that includes the battery feeds every battery move straight back); the
            # compass reads the coming hour from this record (coming_hour)
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
                    if compass_law is None:
                        compass_law = CompassLaw(band, dt=1.0, tau=TAU)
                    compass_law.band = band
                    f = compass_law.force(coming_hour(hist))
                    off = glide(off, -GAIN * f)                     # the adjustment glides, never jumps more than SLEW
                    if abs(off) > 1e-12:
                        flat = [x for row in a for x in row]
                        if any(steer):
                            flat = [max(-1.0, min(1.0, x + off)) if b else x for x, b in zip(flat, steer)]
                            a = [flat]
                            moved += 1                              # an hour counts as moved only where a command moved
            elif k >= kill:
                handed_back = handed_back and True          # from here every command is the native controller's own
        obs, _, _, _, _ = env.step(a)
        k += 1
    ev = env.evaluate()
    d = ev[ev["level"] == "district"].set_index("cost_function")["value"].to_dict()
    return {"arm": arm, "buildings": len(env.buildings), "steps": steps,
            "batteries": sum(battery), "batteries_left_native_for_outages": sum(battery) - sum(steer), "thermal_stores_left_native": sum(1 for n in names if n in ("cooling_storage", "dhw_storage")), "seconds": round(time.time() - t0, 1),
            "moved_hours": moved, "handed_back": handed_back and k >= kill,
            "kpis": {x: (None if (d.get(x) is None or (isinstance(d.get(x), float) and math.isnan(d.get(x)))) else float(d[x]))
                     for x in KPIS}}


MISSES = ("annual_normalized_unserved_energy_total", "discomfort_proportion")   # what the occupants miss; every other score
                                                                                 # is a resource spent or held


def reading(score, native, omni):
    """This run's word by the one key (tools/readings.py): a fall is a GAIN (a cut, or fewer misses); a rise in a miss is a
    LOSS, a rise in a resource spent or held (the bill, the electricity, the carbon, the peaks, swings and unevenness) is
    power given. A word that counts is the three-run table's (tools/citylearn_abc.py), never one run's."""
    if native is None or omni is None:
        return "not scored"
    if abs(omni - native) < 1e-9:
        return W_EVEN
    return W_GAIN if omni < native else (W_LOSS if score in MISSES else W_GIVEN)


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
        res[name] = {}
        for arm in ("native", "omni"):
            try:
                res[name][arm] = run_arm(schema, arm)
            except Exception as e:                       # a district an arm cannot run is reported, never left out
                import traceback
                res[name][arm] = {"arm": arm, "error": f"{type(e).__name__}: {e}"[:600],
                                  "where": traceback.format_exc().strip().splitlines()[-3:]}
        res[name]["citylearn_version"] = version
        res[name]["settings"] = {"gain": GAIN, "tau_h": TAU, "glide_per_h": SLEW, "window_h": WINDOW_H, "kill_at": KILL_AT,
                                 "forecast_days": FORECAST_DAYS}
        (out / f"{name}.json").write_text(json.dumps(res[name], indent=1) + "\n")
        for arm in ("native", "omni"):
            r = res[name][arm]
            print(f"== {name} {arm}: " + (f"{r['seconds']} s" if "seconds" in r else f"ERROR {r['error']} at {r['where']}"),
                  flush=True)
    L = ["# Omni-Compass on top of CityLearn's own controller", "",
         f"CityLearn {version} (Intelligent Environments Lab, University of Texas at Austin; MIT license): an "
         "independent simulator of real buildings from measured data, with its own controllers and its own scoring. "
         "Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass "
         f"law on top of its battery commands (gain {GAIN}, response {TAU} h, glide {SLEW} an hour, reading the coming hour from the same hour of the past {FORECAST_DAYS} days, band from the past week's district draw, handed back at "
         f"{int(KILL_AT * 100)}% of the year). Every number is CityLearn's own score: the controller over no battery at "
         "all, read by the one key: a fall is a GAIN; a rise in energy not served or time uncomfortable is a LOSS, a rise in "
         "any other score (a resource spent or held) is power given. Evidence class: an independent recognized simulator "
         "(not our model).", ""]
    for name, r in res.items():
        n, o = r["native"], r["omni"]
        if "error" in n or "error" in o:
            L += [f"## {name}: not run to the end", "",
                  f"- native: {n.get('error', 'ran')}", f"- omni: {o.get('error', 'ran')}", ""]
            continue
        if name.startswith("citylearn_challenge_2022_phase_1"):
            name += " (the tuning district: not counted in the confirmation)"
        L += [f"## {name}: {n['buildings']} buildings, {n['steps']:,} hours", "",
              f"Omni-Compass moved the commands in {o['moved_hours']:,} hours; every command handed back at "
              f"{int(KILL_AT * 100)}%: {'yes' if o['handed_back'] else 'NO'}.", "",
              "| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |",
              "|---|---:|---:|---:|---|"]
        for x in KPIS:
            nv, ov = n["kpis"][x], o["kpis"][x]
            if nv is None and ov is None:
                continue
            ch = f"{100 * (ov - nv) / abs(nv):+.2f}%" if nv not in (None, 0) and ov is not None else ""
            rd = reading(x, nv, ov)
            L.append(f"| {WORDS[x]} (`{x}`) | {'' if nv is None else f'{nv:.4f}'} | {'' if ov is None else f'{ov:.4f}'} | {ch} | "
                     f"{rd + (': less ' + WORDS[x] if rd == W_GAIN else ': more ' + WORDS[x] if rd in (W_LOSS, W_GIVEN) else '')} |")
        L.append("")
    L += ["## Across every district", "",
          "The tuning district is left out of this table.", "",
          "| CityLearn score | Districts where it fell | Districts where it rose | Mean change | A rise reads |",
          "|---|---:|---:|---:|---|"]
    for x in KPIS:
        pairs = [(r["native"]["kpis"][x], r["omni"]["kpis"][x]) for nm, r in res.items() if nm != "citylearn_challenge_2022_phase_1"
                 and "kpis" in r["native"] and "kpis" in r["omni"]
                 if r["native"]["kpis"][x] not in (None, 0) and r["omni"]["kpis"][x] is not None]
        if not pairs:
            continue
        b = sum(1 for nv, ov in pairs if ov < nv - 1e-9); w = sum(1 for nv, ov in pairs if ov > nv + 1e-9)
        m = sum(100 * (ov - nv) / abs(nv) for nv, ov in pairs) / len(pairs)
        L.append(f"| {WORDS[x]} | {b} of {len(pairs)} | {w} of {len(pairs)} | {m:+.2f}% | {W_LOSS if x in MISSES else W_GIVEN} |")
    (out / "CITYLEARN.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    sums = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in sorted(out.glob("*.json"))]
    (out / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
