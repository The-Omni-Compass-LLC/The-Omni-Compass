# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Python's Monte Carlo of the engine's core from the jump generator: N runs, one digest, the live engine's own port held to it.

The founder's words of 24 October: "the Python's Monte Carlo, our 4K Runge-Kutta, 20-step macro, 10-step micro in each macro ... how
each Python run comes out and starts at zero, and how long in steps OmniCompass gets it into the basin and holds it there and
certifies the count"; and "some button that allows them to activate the Python's jump generator ... running it again and again".

Run k draws its seed from the jump generator (seed_k = base + k·0x9E3779B9, mod 2³²) and its starting state and its parameters from
that seed's mulberry32 stream (the live engine's own generator, written here bit for bit, as tools/engine_runs.py does): E, U, I_U,
S, B, Ḃ uniform on the ranges benchmarks/core_evidence.py draws, then the 22 parameters in omnicompass/core.py's PARAMETER_RANGES
order. Each run goes through omnicompass/core.simulate itself (six states, the fourth-order Runge–Kutta step, 20 macro steps of 10
micro steps, the bounded command held across the four stages) in the four ways benchmarks/core_evidence.py runs its population:
controlled (toward the nearest basin), uncontrolled (u = 0: the plant alone, native), aimed at the wrong basin, and with the double
well's μ at 0. A run is conveyed when its U has stayed in one basin (|U ∓ 1| ≤ 0.10) for 5 macro steps in a row and certified at
10. The digest is the SHA-256 of every run's U at every macro step (six decimals), its convey step and its cert step, one line a
run, the four ways in order; the live engine's page runs the same set through its own port of the core and must give the same
digest (--verify). Class S: the engine's own mathematics on draws, never a measurement.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass import core as C  # noqa: E402
from tools.engine_runs import jump, mulberry32  # noqa: E402
from tools.legal import NOTICE, TOP  # noqa: E402

DEFAULT_RUNS = 500
DEFAULT_BASE = 20261024
OUT_DIR = ROOT / "results" / "core_runs"
WAYS = ("controlled", "uncontrolled", "wrong_target", "controlled_mu0")
STATE_RANGES = ((0.0, 1.0), (-1.0, 1.0), (0.0, 1.0), (-1.0, 1.0), (-1.0, 1.0), (-1.0, 1.0))   # E, U, I_U, S, B, Ḃ (core.sample_state)


def draw(k: int, base: int):
    """Run k's starting state and parameters from its own stream, in the one order the page draws them."""
    seed = jump(base, k)
    r = mulberry32(seed)
    st = [lo + (hi - lo) * r() for lo, hi in STATE_RANGES]
    pr = {name: lo + (hi - lo) * r() for name, (lo, hi) in C.PARAMETER_RANGES.items()}
    return seed, C.State(*st), C.Params(**pr)


def one(k: int, base: int) -> dict:
    seed, x0, p = draw(k, base)
    out = {"k": k, "seed": seed}
    for way in WAYS:
        pp = replace(p, mu=0.0) if way == "controlled_mu0" else p
        tgt = -C.nearest_basin_sign(x0.U) if way == "wrong_target" else None
        r = C.simulate(x0, pp, target=tgt, controlled=(way != "uncontrolled"))
        out[way] = {"U": [float(u) for u in r.U_hist], "convey": int(r.convey_confirm) if r.convey else 0, "cert": int(r.cert_complete) if r.cert else 0}
    return out


def f6(v: float) -> str:
    s = f"{float(v):.6f}"
    return "0.000000" if s == "-0.000000" else s


def canonical(runs: list) -> str:
    """One line a run and a way: the way, the run, its seed, U at every macro step (six decimals), the convey step and the cert step
    (0 when never), the four ways in order; as the page writes it too."""
    return "\n".join(f"{w}:{r['k']}:{r['seed']}:" + ",".join(f6(u) for u in r[w]["U"]) + f":{r[w]['convey']}:{r[w]['cert']}" for w in WAYS for r in runs)


def digest(runs: list) -> str:
    return hashlib.sha256(canonical(runs).encode("utf-8")).hexdigest()


def summary(runs: list) -> dict:
    out = {}
    for w in WAYS:
        cv = [r[w]["convey"] for r in runs]
        ce = [r[w]["cert"] for r in runs]
        hist = [0] * (C.MACRO_STEPS + 1)
        for c in cv:
            if c:
                hist[c] += 1
        got = [c for c in cv if c]
        out[w] = {"conveyed": len(got), "certified": sum(1 for c in ce if c), "convey_hist": hist,
                  "mean_convey_step": round(sum(got) / len(got), 6) if got else None,
                  "in_basin_at_end": sum(1 for r in runs if C.basin_sign(r[w]["U"][-1]) != 0)}
    return out


def verify(page: Path, n: int, base: int) -> int:
    """The page's own port of the core (between its CORE-MC markers) run in node on the same set: the digest must be the Python's."""
    s = page.read_text(encoding="utf-8")
    try:
        block = s[s.index("// CORE-MC-BEGIN"):s.index("// CORE-MC-END")]
        gen = s[s.index("function mulberry32"):s.index("\n", s.index("function mulberry32"))]
    except ValueError:
        print("the page carries no port of the core (no CORE-MC markers)")
        return 1
    with tempfile.TemporaryDirectory() as t:
        (Path(t) / "port.js").write_text(gen + "\n" + block + "\nmodule.exports={coreSet,coreCanonical};\n", encoding="utf-8")
        (Path(t) / "drive.js").write_text("const P=require('./port.js');const runs=P.coreSet(%d,%d,0,%d);process.stdout.write(P.coreCanonical(runs));" % (base, n, n), encoding="utf-8")
        js = subprocess.run(["node", str(Path(t) / "drive.js")], capture_output=True, text=True, cwd=t)
    if js.returncode:
        print("the page's port did not run:", js.stderr[-400:])
        return 1
    py = [one(k, base) for k in range(n)]
    a, b = canonical(py), js.stdout
    same = hashlib.sha256(b.encode("utf-8")).hexdigest() == digest(py)
    worst, lines = 0.0, 0
    for la, lb in zip(a.split("\n"), b.split("\n")):
        if la != lb:
            lines += 1
            ua, ub = la.split(":")[3].split(","), lb.split(":")[3].split(",")
            worst = max([worst] + [abs(float(x) - float(y)) for x, y in zip(ua, ub)])
    print(f"the page's core and the Python's, {n} runs from base {base} in four ways: the digests {'match' if same else 'DIFFER'}; "
          f"{lines} of {4 * n} lines differ, largest difference {worst:.1e}")
    return 0 if same else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    ap.add_argument("--base", type=int, default=DEFAULT_BASE, help="the jump generator's base seed")
    ap.add_argument("--verify", default="", help="the live engine page: run its port of the core in node and compare")
    ap.add_argument("--out", default="", help="where to write (default results/core_runs/)")
    a = ap.parse_args()
    if a.verify:
        return verify(Path(a.verify), a.runs, a.base)
    runs = [one(k, a.base) for k in range(a.runs)]
    dg, sm = digest(runs), summary(runs)
    data = {"tool": "tools/core_runs.py", "core": "omnicompass/core.py (simulate: RK4, 20 macro steps of 10 micro steps, the bounded command)",
            "runs": a.runs, "base": a.base, "jump": "seed_k = base + k·0x9E3779B9 mod 2^32", "generator": "mulberry32 (the page's own)",
            "macro": C.MACRO_STEPS, "micro": C.MICRO_STEPS, "dt": C.MACRO_DT, "tol": C.BASIN_TOL, "convey_window": C.CONVEY_WINDOW,
            "cert_window": C.CERT_WINDOW, "kp": C.KP, "authority": C.U_AUTHORITY, "ways": list(WAYS), "digest": dg,
            "digest_of": "SHA-256 of every run's U at every macro step (six decimals), its convey and cert steps, one line a run and a way (canonical())",
            "summary": sm, "written": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    if os.environ.get("GITHUB_RUN_ID"):
        data["github"] = {"run_id": os.environ["GITHUB_RUN_ID"], "workflow": os.environ.get("GITHUB_WORKFLOW", ""),
                          "commit": os.environ.get("GITHUB_SHA", ""), "ref": os.environ.get("GITHUB_REF_NAME", ""),
                          "url": f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{os.environ.get('GITHUB_REPOSITORY', '')}/actions/runs/{os.environ['GITHUB_RUN_ID']}"}
    out = Path(a.out) if a.out else OUT_DIR / f"CORE_RUNS_{a.runs}_{a.base}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    names = {"controlled": "Omni-Compass on top, toward the nearest basin", "uncontrolled": "native: the plant alone, u = 0",
             "wrong_target": "Omni-Compass aimed at the wrong basin", "controlled_mu0": "Omni-Compass on top, the double well's μ at 0"}
    md = [f"# The core's Monte Carlo: {a.runs} runs from the jump generator (base {a.base}), one digest", "", f"> {TOP}", "",
          f"Each run: omnicompass/core.simulate, {C.MACRO_STEPS} macro steps of {C.MICRO_STEPS} fourth-order Runge–Kutta micro steps "
          f"(Δt {C.MACRO_DT} s a macro step), from the starting state and parameters its own stream draws (seed_k = base + k·0x9E3779B9 "
          f"mod 2³², mulberry32, the live engine's own generator). Conveyed: {C.CONVEY_WINDOW} macro steps in a row in one basin "
          f"(|U ∓ 1| ≤ {C.BASIN_TOL}); certified: {C.CERT_WINDOW}. Written {data['written']}. Class S.", "",
          f"**Digest {dg}** (SHA-256 of every run's path at six decimals). The live engine's page runs the same set through its own port "
          "of the core and shows its own digest beside this one.", "",
          "| way | conveyed | certified | mean step conveyed | in a basin at step 20 |", "|---|---:|---:|---:|---:|"]
    for w in WAYS:
        m = sm[w]
        md.append(f"| {names[w]} | {m['conveyed']} of {a.runs} | {m['certified']} of {a.runs} | {m['mean_convey_step'] if m['mean_convey_step'] is not None else '—'} | {m['in_basin_at_end']} of {a.runs} |")
    md += ["", "---", "", f"*{NOTICE}*"]
    out.with_suffix(".md").write_text("\n".join(md), encoding="utf-8")
    print(f"{a.runs} runs from base {a.base}: digest {dg}; controlled {sm['controlled']['conveyed']} conveyed, {sm['controlled']['certified']} certified; "
          f"native (u = 0) {sm['uncontrolled']['conveyed']} conveyed, {sm['uncontrolled']['certified']} certified -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
