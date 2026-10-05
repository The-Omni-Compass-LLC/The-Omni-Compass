#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Omni-Compass on top of a distribution grid's own voltage control, in pandapower (docs/PANDAPOWER_PREREGISTRATION.md).

An independent, recognized simulator and data set: pandapower (Fraunhofer IEE and the University of Kassel; BSD) solves
the AC power flow; SimBench (the German benchmark grids, with a year of 15-minute load, solar and wind profiles) gives
the grids and their year. Both are someone else's work; nothing here models the grid.

  native  the substation's on-load tap changer holds the medium-voltage busbar at its setpoint (1.00 per unit) inside a
          deadband of half a tap step, one tap per step at most; solar and wind at unity power factor (as SimBench has
          them). This is how a utility runs it on its own.
  omni    the same tap changer, with the compass law (omnicompass/compass_law.py) on top of its setpoint: it reads the
          worst voltage margin anywhere in the grid (the bus nearest either limit, 0.95 and 1.05 per unit) and moves the
          setpoint inside [0.97, 1.03]: down while every bus has room (conservation voltage reduction), away from the
          nearer limit as soon as one bus nears it, and straight back to native at a violation. At KILL_AT of the year
          the setpoint is handed back. Every move is one whole tap; a move toward saving needs a full week seen under the
          present setpoint whose worst moment still leaves every bus MARGIN after one more tap; a move away from a limit
          is at once, once the utility's tap changer has reached the present setpoint.

Scored by pandapower itself, the same grid and the same year in both arms:
  energy drawn from the upstream grid (MWh), line and transformer losses (MWh), bus-hours outside [0.95, 1.05],
  tap operations (wear), and the lowest and highest voltage seen.

Loads: SimBench's loads are constant power. Lowering the voltage saves energy only where a load draws less at a lower
voltage, so the run is made twice: with a declared ZIP mix (40% constant impedance, 30% constant current, 30% constant
power, a common residential mix) and with SimBench's own constant-power loads, where only losses can change.

  python3 tools/run_pandapower.py --grids 1-MV-rural--0-sw --out out [--step 4]   (step 4: hourly, every 4th quarter hour)
  python3 tools/run_pandapower.py --report-only DIR --out DIR
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw, clamp  # noqa: E402

V_LO, V_HI = 0.95, 1.05            # the voltage limits (EN 50160 band, per unit)
SET_NATIVE = 1.00                  # the tap changer's own setpoint
SET_LO, SET_HI = 0.97, 1.03        # the cover Omni may move the setpoint in
STEP_V = 0.015                     # the setpoint moves in whole tap steps (1.5%), so every change is one tap, never a hunt
MARGIN = 0.01                      # the room every bus keeps from a limit, after any step Omni takes (per unit)
WINDOW_H = 168.0                   # a step toward saving needs a full week seen under the present setpoint (tap wear)
KILL_AT = 0.9
ZIP = (40.0, 30.0)                 # constant-impedance and constant-current shares of every load (percent), the rest power


def tap_control(net, vm, setpoint, ops):
    """The utility's own tap changer: one tap toward the setpoint when the busbar is outside half a tap step of it."""
    for t in net.trafo.index:
        v = vm[net.trafo.at[t, "lv_bus"]]
        half = net.trafo.at[t, "tap_step_percent"] / 200.0
        pos = net.trafo.at[t, "tap_pos"]
        if v > setpoint + half and pos < net.trafo.at[t, "tap_max"]:
            net.trafo.at[t, "tap_pos"] = pos + 1; ops[0] += 1      # a higher tap lowers the medium-voltage side
        elif v < setpoint - half and pos > net.trafo.at[t, "tap_min"]:
            net.trafo.at[t, "tap_pos"] = pos - 1; ops[0] += 1


def run_arm(code, arm, zip_loads, step):
    import pandapower as pp
    import simbench as sb
    net = sb.get_simbench_net(code)
    prof = sb.get_absolute_values(net, profiles_instead_of_study_cases=True)
    net.trafo["tap_changer_type"] = "Ratio"
    # ZIP loads are applied by hand, never through pandapower's own const_z/const_i columns: pandapower puts a bus's ZIP
    # shares on the bus's whole demand, solar on the same bus included, so the solar would draw less at a lower voltage
    # too (and the solved balance came out backwards). Here each load is set to p0 (z V^2 + i V + p) at its own bus
    # voltage and the flow is solved again until the voltages stop moving.
    zz, ii = (ZIP[0] / 100.0, ZIP[1] / 100.0) if zip_loads else (0.0, 0.0)
    lbus = net.load.bus.values
    n = len(prof[("load", "p_mw")])
    ks = list(range(0, n, step))
    kill = int(KILL_AT * len(ks))
    dt_h = 0.25 * step
    law = CompassLaw(Band(0.0, 1.0), dt=1.0, tau=3.0, kp=1.0, smooth=0.3) if arm == "omni" else None
    if law is not None:
        law.kd *= 3.0
    setpoint, ops = SET_NATIVE, [0]
    last_change_h, hist = 0.0, []                       # when the setpoint last moved; the margins seen since (trailing window)
    e_in = e_loss = e_load = e_gen = 0.0
    viol = steps = 0
    sp_sum, sp_log, worst_bal = 0.0, [], 0.0
    vmin_all, vmax_all = 9.0, 0.0
    t0 = time.time()
    for i, k in enumerate(ks):
        for (elm, col), df in prof.items():
            if elm in net and col in net[elm].columns and df.shape[1] and len(df) > k:
                net[elm].loc[df.columns, col] = df.iloc[k].values
        p0, q0 = net.load.p_mw.values.copy(), net.load.q_mvar.values.copy()
        pp.runpp(net, numba=False)
        if zip_loads:
            for _ in range(8):
                v = net.res_bus.vm_pu.loc[lbus].values
                f = zz * v * v + ii * v + (1.0 - zz - ii)
                net.load["p_mw"], net.load["q_mvar"] = p0 * f, q0 * f
                v_before = net.res_bus.vm_pu.values.copy()
                pp.runpp(net, numba=False, init="results")
                if abs(net.res_bus.vm_pu.values - v_before).max() < 1e-5:
                    break
            net.load["p_mw"], net.load["q_mvar"] = p0, q0        # the nominal draw back, for the next step's profile
        vm = net.res_bus.vm_pu
        if law is not None and i < kill:
            lo_m, hi_m = vm.min() - V_LO, V_HI - vm.max()
            now_h = i * dt_h
            hist.append((now_h, lo_m, hi_m))
            while hist and hist[0][0] < now_h - WINDOW_H:
                hist.pop(0)
            # the compass reads the worst margin now: 0 is a full margin's room, 1 is at a limit (a violation reads past it)
            p = clamp(1.0 - min(lo_m, hi_m) / (V_HI - SET_NATIVE), 0.0, 1.5)
            F = law.force(p if min(lo_m, hi_m) >= 0 else 1.5)
            step_dir = 0
            # the utility's tap changer first has to reach the present setpoint (busbar within half a tap of it); until it
            # has, a voltage is the tap changer still travelling, not the grid asking Omni for anything
            settled = all(abs(vm[net.trafo.at[t, "lv_bus"]] - setpoint) <= net.trafo.at[t, "tap_step_percent"] / 200.0 + 1e-9
                          for t in net.trafo.index)
            if not settled:
                pass
            elif lo_m < MARGIN and hi_m > STEP_V + MARGIN and setpoint < SET_HI - 1e-9:
                step_dir = 1                                    # the lowest bus nears 0.95: one tap up, at once
            elif hi_m < MARGIN and lo_m > STEP_V + MARGIN and setpoint > SET_LO + 1e-9:
                step_dir = -1                                   # the highest bus nears 1.05: one tap down, at once
            elif F <= 0 and now_h - last_change_h >= WINDOW_H and now_h >= WINDOW_H:
                # calm, and the whole trailing window seen under this setpoint: step only where the worst moment of that
                # window would still keep MARGIN after one more tap (the tap moves every bus by about one step)
                lo_w, hi_w = min(h[1] for h in hist), min(h[2] for h in hist)
                if setpoint > SET_NATIVE + 1e-9 and hi_w - STEP_V >= MARGIN and lo_w - STEP_V >= MARGIN:
                    step_dir = -1                               # an earlier raise no longer needed: back toward native
                elif setpoint > SET_LO + 1e-9 and lo_w - STEP_V >= MARGIN:
                    step_dir = -1                               # conservation voltage reduction, one tap
            if step_dir:
                setpoint = clamp(setpoint + STEP_V * step_dir, SET_LO, SET_HI)
                last_change_h = now_h
                hist.clear()                                    # the window starts again under the new setpoint
        elif law is not None:
            setpoint = SET_NATIVE                               # handed back
        tap_control(net, vm, setpoint, ops)
        sp_sum += setpoint; sp_log.append((round(i * dt_h), round(setpoint, 3), round(float(vm.min()), 4), round(float(vm.max()), 4)))
        e_in += float(net.res_ext_grid.p_mw.sum()) * dt_h
        gen = float(net.res_sgen.p_mw.sum())
        e_gen += gen * dt_h
        e_load += float(net.res_load.p_mw.sum()) * dt_h            # what the loads drew at the voltage they saw
        bal = abs(float(net.res_ext_grid.p_mw.sum()) + gen - float(net.res_load.p_mw.sum())
                  - float(net.res_line.pl_mw.sum()) - float(net.res_trafo.pl_mw.sum()))
        worst_bal = max(worst_bal, bal)                             # the solved flow must close: import + solar = load + losses
        e_loss += (float(net.res_line.pl_mw.sum()) + float(net.res_trafo.pl_mw.sum())) * dt_h
        bad = int(((vm < V_LO) | (vm > V_HI)).sum())
        viol += bad; steps += len(vm)
        vmin_all, vmax_all = min(vmin_all, float(vm.min())), max(vmax_all, float(vm.max()))
    return {"arm": arm, "zip_loads": zip_loads, "steps": len(ks), "dt_h": dt_h, "energy_in_mwh": e_in,
            "losses_mwh": e_loss, "load_energy_mwh": e_load, "generation_mwh": e_gen, "violation_bus_share": viol / max(steps, 1), "tap_operations": ops[0],
            "vmin": vmin_all, "vmax": vmax_all, "seconds": round(time.time() - t0, 1),
            "restored": setpoint == SET_NATIVE, "worst_balance_mw": worst_bal, "trafos": len(net.trafo),
            "mean_setpoint": sp_sum / len(ks), "setpoint_changes": [e for j, e in enumerate(sp_log) if j and e[1] != sp_log[j - 1][1]]}


ROWS = [("load_energy_mwh", "energy the loads drew (MWh)"), ("losses_mwh", "line and transformer losses (MWh)"),
        ("energy_in_mwh", "net import from the upstream grid (MWh; negative: the grid exports)"),
        ("generation_mwh", "solar and wind fed in (MWh)"),
        ("violation_bus_share", "bus-steps outside 0.95-1.05 per unit (share)"), ("tap_operations", "tap operations (wear)"),
        ("vmin", "lowest voltage seen (per unit)"), ("vmax", "highest voltage seen (per unit)"),
        ("mean_setpoint", "busbar setpoint, mean over the year (per unit)")]
LOWER = {"load_energy_mwh", "energy_in_mwh", "losses_mwh", "violation_bus_share", "tap_operations"}


def reading(k, n, o):
    if k in ("vmin", "vmax", "generation_mwh", "mean_setpoint"):
        return "shown"
    if abs(o - n) <= 1e-6 * max(abs(n), 1e-12):
        return "same"
    return "better" if (o < n) == (k in LOWER) else "WORSE"


def report(res, out):
    L = ["# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)", "",
         "pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their "
         "year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: "
         "the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. "
         "Evidence class: an independent recognized simulator and data set (not our model).", ""]
    for code, r in res.items():
        for zl in ("zip", "constant_power"):
            if zl not in r:
                continue
            n, o = r[zl]["native"], r[zl]["omni"]
            L += [f"## {code}, loads {'ZIP (40% Z, 30% I, 30% P)' if zl == 'zip' else 'constant power (SimBench as shipped)'}", "",
                  f"{n['steps']} steps of {n['dt_h']:g} h. Omni handed the setpoint back: {'yes' if o['restored'] else 'NO'}. "
                  f"Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): {o.get('setpoint_changes', [])}; "
                  f"each change is one tap on each of the {o.get('trafos', '?')} substation transformers, the hand-back at "
                  f"{KILL_AT:.0%} of the year included. Worst power balance of any solved step: "
                  f"{max(n.get('worst_balance_mw', 0), o.get('worst_balance_mw', 0)):.1e} MW.", "",
                  "| | native | omni | Change | Reading |", "|---|---:|---:|---:|---|"]
            for k, lab in ROWS:
                ch = (o[k] - n[k]) / abs(n[k]) * 100 if abs(n[k]) > 1e-12 else float("nan")
                chs = f"{ch:+.2f}%" if not math.isnan(ch) else f"{o[k] - n[k]:+.4g}"
                L.append(f"| {lab} | {n[k]:.6g} | {o[k]:.6g} | {chs} | {reading(k, n[k], o[k])} |")
            L.append("")
    (Path(out) / "PANDAPOWER.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    print("\n".join(L))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grids", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--step", type=int, default=4)
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    res = {}
    if a.report_only:
        for f in sorted(Path(a.report_only).glob("*.json")):
            res[f.stem] = json.loads(f.read_text())
    for code in [g for g in a.grids.split(",") if g]:
        res[code] = {}
        for zl in (True, False):
            key = "zip" if zl else "constant_power"
            res[code][key] = {}
            for arm in ("native", "omni"):
                try:
                    res[code][key][arm] = run_arm(code, arm, zl, a.step)
                except Exception as e:                       # a grid an arm cannot run is reported, never left out
                    res[code][key][arm] = {"arm": arm, "error": f"{type(e).__name__}: {e}"[:600]}
                r = res[code][key][arm]
                print(f"== {code} {key} {arm}: " + (f"{r['seconds']} s" if "seconds" in r else f"ERROR {r['error']}"), flush=True)
            if any("error" in res[code][key][x] for x in ("native", "omni")):
                del res[code][key]
        (out / f"{code}.json").write_text(json.dumps(res[code], indent=1) + "\n")
    report(res, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
