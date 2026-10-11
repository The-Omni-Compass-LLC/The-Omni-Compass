#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A10 card modelled (realms/gpu_card.py, fitted to the paid run of 2 October; evidence class S). Each base runs alone
and with the card's brain on top, on the same seeds (5000-5009 tuning, 5100-5109 fresh; `fresh` as the second argument),
600 s each, for two kinds of work: compute-bound (the bench's pinned matrix products) and AI token generation (85% of a
request's time waiting on memory, assumed). Bases: the card's own firmware (native) and an operator's fixed 105 W power
cap. Writes results/sim/gpu_two_wire/."""
import json, math, subprocess, sys, time

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.gpu_card import run  # noqa: E402
from realms.harness import T95  # noqa: E402

SEEDS = list(range(5000, 5010))       # tuning seeds (the gains were chosen on these)
FRESH = list(range(5100, 5110))       # fresh seeds, never used while tuning
PAIRS = (("native", "omni", "the card's firmware alone", "firmware + Omni on top"),
         ("cap", "cap_omni", "a fixed 105 W power cap alone", "the cap + Omni on top"))
WORK = ((0.0, "compute-bound work (matrix products)"), (0.85, "AI token generation (85% of each request waiting on memory)"))
ROWS = [("work_per_kj", "work per energy (requests per kJ)", "{:.1f}"), ("energy_j", "energy (J)", "{:.0f}"),
        ("served", "requests served", "{:.0f}"), ("p50_ms", "response, median (ms)", "{:.1f}"),
        ("p95_ms", "response, 95th percentile (ms)", "{:.1f}"), ("p99_ms", "response, 99th percentile (ms)", "{:.1f}"),
        ("viol_share", "requests over the service line (%)", "{:.2%}"), ("first_p50_ms", "first request after a rest, median (ms)", "{:.1f}"),
        ("svc_p50_ms", "the card's own time per request, median (ms)", "{:.1f}"), ("clock_mean", "clock, mean share of top", "{:.3f}"),
        ("clock_jitter", "clock, standard deviation", "{:.3f}"), ("t_peak", "temperature, peak (C)", "{:.1f}"),
        ("t_mean", "temperature, mean (C)", "{:.1f}")]


def ci(xs):
    n = len(xs); m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1)) if n > 1 else 0.0
    h = T95.get(n - 1, 2.0) * sd / math.sqrt(n)
    return m, m - h, m + h


def paired_cells(res, base, top):
    out = {}
    for k, name, f in [("work_per_kj", "work per energy", None), ("energy_j", "energy", None), ("p50_ms", "response, median", None),
                       ("p95_ms", "response, p95", None), ("p99_ms", "response, p99", None),
                       ("viol_share", "time over the line (pp)", "pp"), ("served", "requests served", None)]:
        if f == "pp":
            d = [100 * (x[k] - n[k]) for x, n in zip(res[top], res[base])]
            m, lo, hi = ci(d); out[name] = f"{m:+.3f} ({lo:+.3f} to {hi:+.3f})"
        else:
            # a ratio is summarised on the log scale (the geometric mean of the per-seed ratios and its interval), so one
            # seed's large ratio cannot stand for the others
            d = [math.log(x[k] / n[k]) for x, n in zip(res[top], res[base]) if n[k] > 0 and x[k] > 0]
            m, lo, hi = ci(d); out[name] = f"{math.exp(m) - 1:+.2%} ({math.exp(lo) - 1:+.2%} to {math.exp(hi) - 1:+.2%})"
    return out


def main(out=ROOT / "results" / "sim" / "gpu_two_wire", fresh=""):
    global SEEDS
    if fresh:
        SEEDS = FRESH
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    arms = [a for p in PAIRS for a in p[:2]]
    res = {memb: {arm: [{k: v for k, v in run(s, arm, memb=memb).items() if k not in ("svc", "resp")} for s in SEEDS]
                  for arm in arms} for memb, _ in WORK}
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    L = ["# The GPU card in simulation: each base alone, and with Omni-Compass on top", "",
         f"Evidence class **S** (a model, not a meter). Seeds {SEEDS[0]}-{SEEDS[-1]}, 600 s each, commit `{commit}`, "
         f"{time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}. Model: `realms/gpu_card.py`; the law: `omnicompass/compass_law.py` "
         "and the verdict `omnicompass/verdict.py`.", "",
         "Omni-Compass never runs the card. It sits on top of what already runs it (the card's own firmware, or an operator's "
         "power cap) and moves the clock ceiling that base already accepts (the power limit stays where the base set it): "
         "it parks the clock when the work stops and races it back the moment work arrives, and a level is used only after "
         "a paired trial on the card shows it adds at most 0.5% to the card's own time on the first request after a rest "
         "(docs/GPU_PREREGISTRATION.md, amendment 13). Every comparison below is a base alone against the same base with "
         "Omni on top, on the same seeds and the same requests.", ""]
    for memb, wname in WORK:
        r = res[memb]
        L += [f"## {wname[0].upper() + wname[1:]}", "", "### Mean over seeds", "",
              "| Gauge | " + " | ".join(f"{p[2][0].upper() + p[2][1:]} | {p[3][0].upper() + p[3][1:]}" for p in PAIRS) + " |",
              "|---|" + "---:|" * (2 * len(PAIRS))]
        for k, name, f in ROWS:
            L.append(f"| {name} | " + " | ".join(f.format(sum(x[k] for x in r[a]) / len(SEEDS)) for a in arms) + " |")
        L += ["", "### With Omni on top against the same base alone (ratios: geometric mean over seeds, 95% interval; "
              "time over the line: mean difference)", "",
              "| Gauge | " + " | ".join(f"{p[3]} vs {p[2]}" for p in PAIRS) + " |", "|---|" + "---:|" * len(PAIRS)]
        cells = [paired_cells(r, p[0], p[1]) for p in PAIRS]
        for name in cells[0]:
            L.append(f"| {name} | " + " | ".join(c[name] for c in cells) + " |")
        ev = [x["verdict_events"] for p in PAIRS for x in r[p[1]]]
        L += ["", f"Verdict over all Omni runs: {sum(e['trials'] for e in ev)} trials, {sum(e['allowed'] for e in ev)} steps "
              f"allowed, {sum(e['refused'] for e in ev)} refused.", ""]
    L += ["Requests served are the same work in every arm (the stream is the seed's). The compute model is fitted to one "
          "A10's own meter (energy within 0.1% of both arms of the paid run); the token-generation model's power and memory "
          "share are assumed. A model written by the same people who wrote the brain is not an independent test: the number "
          "that counts is a rented card's own meter."]
    (out / "RESULT.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    (out / "RESULT.json").write_text(json.dumps({"seeds": SEEDS, "commit": commit,
                                                  "work": {str(m): v for m, v in res.items()}}, indent=1) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(*sys.argv[1:])
