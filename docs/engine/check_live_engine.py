# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Checks the live engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html) against the engine's own Python.

The page carries a JavaScript port of the governor (omnicompass/adapter.py, core.py), the nerves
(nervous_system.py), the compass law (compass_law.py) and the verdict (verdict.py). This script draws seeded inputs,
runs the Python, runs the page's own script on the same inputs under Node, and compares every number:

  governor   200 trajectories x 40 decisions: the six states, push, rho*, kappa, h, sigma, nu, calm
  nerves     the expand and hand-back grant of six organs at every one of those decisions
  compass    60 trajectories x 80 readings: the force F and k_d
  verdict    300 intervals and medians; 400 whole trials, the decision and the number of costs measured

Usage: python3 docs/engine/check_live_engine.py   (needs node on the PATH). Exit 0 when nothing differs past 1e-12.
"""
from __future__ import annotations

import json
import math
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from omnicompass.adapter import Governor                     # noqa: E402
from omnicompass.compass_law import Band, CompassLaw         # noqa: E402
from omnicompass.nervous_system import from_governor         # noqa: E402
from omnicompass.verdict import Verdict, change_interval, median  # noqa: E402

ORGANS = ("pods", "nodes", "cpufreq", "gpu", "power", "routing")


def port_js(page: Path) -> str:
    s = page.read_text(encoding="utf-8")
    js = s[s.index("<script>") + 8:s.rindex("</script>")]
    a = js.index("// ============================================================== the engine")
    b = js.index("// ============================================================== the body")
    v0, v1 = js.index("const median = xs"), js.index("function runTrialSync")
    return js[a:b] + "\n" + js[v0:v1] + "\nmodule.exports={Brain,CompassLaw,median,interval,judge};\n"


def cases(seed: int = 20261017) -> dict:
    rng = random.Random(seed)
    out = {"brain": [], "law": [], "verdict": [], "trial": []}
    for _ in range(200):
        g, seq = Governor(), []
        for _ in range(40):
            o = {"q": rng.choice([0, 0, rng.uniform(0, 0.6)]), "load": rng.uniform(0.2, 1.4), "power": rng.uniform(0, 1.1),
                 "thermal": rng.uniform(0, 1.1), "network": rng.uniform(0, 0.4), "drift": rng.uniform(0, 0.5),
                 "stale": rng.choice([0, 0, 0, 1]), "security": rng.choice([0, 0, 0, 1]), "sloClean": rng.random() < 0.8}
            obs = {"queue_ratio": o["q"], "load_ratio": o["load"], "power_stress": o["power"], "thermal": o["thermal"],
                   "network_stress": o["network"], "drift_ratio": o["drift"], "stale": o["stale"],
                   "security_block": o["security"], "slo_clean": o["sloClean"]}
            d = g.step(obs, 0)
            a = from_governor(g, obs, d)
            L = g.law
            rho = min(L.rho0, max(L.rho_min, L.rho0 - L.kI * g.x.I_U - L.kE * g.x.E))
            seq.append({"in": o, "x": list(g.x.as_tuple()), "push": g.last_push, "rho": rho, **a["scalars"],
                        "organs": {k: [a["organs"][k]["expand"], a["organs"][k]["contract"]] for k in ORGANS}})
        out["brain"].append(seq)
    for _ in range(60):
        tau = rng.uniform(1, 8)
        law, rs, fs, r = CompassLaw(Band(0.2, 1.0), dt=1.0, tau=tau), [], [], rng.uniform(0.2, 1.1)
        for _ in range(80):
            r = max(0.0, r + rng.gauss(0, 0.06))
            rs.append(r)
            fs.append(law.force(r))
        out["law"].append({"tau": tau, "r": rs, "F": fs, "kd": law.kd})
    for _ in range(300):
        ref = [math.exp(rng.gauss(0, 0.25)) for _ in range(rng.randint(30, 90))]
        got = [math.exp(rng.gauss(0.02, 0.25)) for _ in range(rng.randint(30, 90))]
        out["verdict"].append({"ref": ref, "got": got, "iv": change_interval(ref, got), "m": [median(ref), median(got)]})
    for _ in range(400):
        cost = rng.choice([-0.04, 0, 0.01, 0.02, 0.03, 0.05, 0.08])
        tol, sig = rng.choice([0.005, 0.01, 0.02, 0.03]), rng.choice([0.1, 0.25, 0.4])
        ref = [math.exp(rng.gauss(0, sig)) for _ in range(30)]
        extra = [math.exp(rng.gauss(0, sig)) * (1 + cost) for _ in range(90)]
        v = Verdict(tolerance=tol, min_samples=30, probe_every=1, max_trial=10 ** 6, judge="interval")
        v.tick(True); v.observe(ref); v.tick(True); v.observe(extra[:30])
        used = 30
        while True:
            _, _, ev = v.tick(True)
            if ev and ev.get("verdict", "").startswith("step"):
                break
            v.observe([extra[used]]); used += 1
        out["trial"].append({"ref": ref, "extra": extra, "tol": tol, "allowed": ev["verdict"] == "step allowed", "used": used})
    return out


COMPARE = r"""
const P = require('./port.js'); const C = require('./cases.json');
const w = {state: 0, push: 0, rho: 0, nerves: 0, force: 0, kd: 0, interval: 0, median: 0}; let grants = 0, grantMis = 0, trialMis = 0;
for (const seq of C.brain) { const b = new P.Brain(); for (const st of seq) { const o = b.step(st.in);
  for (let i = 0; i < 6; i++) w.state = Math.max(w.state, Math.abs(o.xn[i] - st.x[i]));
  w.push = Math.max(w.push, Math.abs(o.push - st.push)); w.rho = Math.max(w.rho, Math.abs(o.rho - st.rho));
  for (const k of ["kappa", "h", "sigma", "nu", "calm"]) w.nerves = Math.max(w.nerves, Math.abs(o[k] - st[k]));
  for (const k in st.organs) { grants++; if (o.organs[k].expand !== st.organs[k][0] || o.organs[k].contract !== st.organs[k][1]) grantMis++; } } }
for (const c of C.law) { const L = new P.CompassLaw(c.tau); w.kd = Math.max(w.kd, Math.abs(L.kd - c.kd));
  c.r.forEach((r, k) => { w.force = Math.max(w.force, Math.abs(L.force(r) - c.F[k])); }); }
for (const c of C.verdict) { const iv = P.interval(c.ref, c.got);
  w.interval = Math.max(w.interval, Math.abs(iv[0] - c.iv[0]), Math.abs(iv[1] - c.iv[1]));
  w.median = Math.max(w.median, Math.abs(P.median(c.ref) - c.m[0]), Math.abs(P.median(c.got) - c.m[1])); }
for (const c of C.trial) { const Pp = {tol: c.tol, min: 30}; const got = c.extra.slice(0, 30); let J = P.judge(c.ref, got, Pp);
  while (J.reading !== "LOSS" && J.wide && got.length < 90) { got.push(c.extra[got.length]); J = P.judge(c.ref, got, Pp); }
  if (J.allowed !== c.allowed || got.length !== c.used) trialMis++; }
console.log(JSON.stringify({worst: w, grants, grantMis, trials: C.trial.length, trialMis}));
"""


def main() -> int:
    node = shutil.which("node")
    if not node:
        print("node is not on the PATH; the page's script cannot be run")
        return 2
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "port.js").write_text(port_js(HERE / "OMNI_COMPASS_LIVE_ENGINE.html"), encoding="utf-8")
        (t / "cases.json").write_text(json.dumps(cases()), encoding="utf-8")
        (t / "compare.js").write_text(COMPARE, encoding="utf-8")
        r = json.loads(subprocess.run([node, "compare.js"], cwd=t, capture_output=True, text=True, check=True).stdout)
    for k, v in r["worst"].items():
        print(f"{k:9s} largest difference {v:.1e}")
    print(f"grants    {r['grantMis']} of {r['grants']} differ")
    print(f"trials    {r['trialMis']} of {r['trials']} differ")
    ok = max(r["worst"].values()) < 1e-12 and r["grantMis"] == 0 and r["trialMis"] == 0
    print("the page's engine matches the Python" if ok else "the page's engine differs from the Python")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
