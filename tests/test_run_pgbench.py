# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The database runner's rule (tools/run_pgbench.py, docs/POSTGRES_PREREGISTRATION.md), without a database: the decision
each second (where the time goes decides the direction; calm gives back one idle server and never a server in use; the
cushion, the dwell, the cover and the fail-up to the pooler's own setting), pgbench's per-transaction log read into the
gauges, and the paired reading over repetitions (better, WORSE, no difference beyond the noise, same, never more)."""
import math
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_pgbench as R


def main():
    snap = R.NATIVE_POOL
    # the service slow and clients waiting: grow, by the force
    t, d, why = R.decide(0.5, 0.25, 0.8, 0, 10, snap, 0, 99)
    assert (t, d) == (13, 1) and "more" in why, (t, d, why)
    t, d, _ = R.decide(0.6, 1.0, 0.9, 0, 10, snap, 0, 99)
    assert t == 20 and d == 1, "full force adds ten slots"
    # the service slow inside the server: one fewer
    t, d, why = R.decide(0.5, 0.25, 0.2, 3, 10, snap, 0, 99)
    assert (t, d) == (9, -1) and "inside the server" in why
    # calm: one idle server given back, never a server in use
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 0, 99)[:2] == (9, -1)
    assert R.decide(0.1, -0.3, 0.0, 0, 10, snap, 0, 99)[:2] == (10, 0), "no idle server: nothing taken"
    # the cushion
    assert R.decide(0.4, 0.03, 0.9, 5, 10, snap, 0, 99)[:2] == (10, 0)
    assert R.decide(0.4, -0.03, 0.9, 5, 10, snap, 0, 99)[:2] == (10, 0)
    # the dwell: no reversal within five seconds, a reversal after it
    assert R.decide(0.5, 0.3, 0.9, 0, 10, snap, -1, 2.0)[:2] == (10, 0)
    assert R.decide(0.5, 0.3, 0.9, 0, 10, snap, -1, 6.0)[:2] == (13, 1)
    assert R.decide(0.5, 0.3, 0.9, 0, 10, snap, 1, 2.0)[:2] == (13, 1), "the same direction is never held"
    # the cover
    assert R.decide(0.1, -0.3, 0.0, 1, R.FLOOR, snap, 0, 99)[:2] == (R.FLOOR, 0)
    assert R.decide(0.6, 1.0, 0.9, 0, R.CEILING - 3, snap, 0, 99)[:2] == (R.CEILING, 1)
    # fail up: the pooler's own setting at once, whatever the direction rule would say
    t, d, why = R.decide(0.97, 1.0, 0.1, 0, 7, snap, -1, 1.0)
    assert t == snap and d == 0 and "fail up" in why

    # pgbench's log into the gauges: 10 transactions, 8 inside a 50 ms line, over 2 s of load
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "step-00.123"
        us = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 60000, 90000]
        f.write_text("".join(f"{i % 4} {i} {u} 0 1791260718 {i * 1000} 50\n" for i, u in enumerate(us)))
        lat = R.parse_latencies([f])
        assert lat == us
        g = R.latency_gauges(lat, 2.0)
        assert g["transactions"] == 10 and g["tps"] == 5.0 and g["work_inside_line_tps"] == 4.0 and g["inside_line_share"] == 0.8
        assert g["p95_ms"] == 90.0 and g["p50_ms"] == 5.0 and abs(g["mean_ms"] - 18.6) < 1e-9
        g0 = R.latency_gauges([], 2.0)
        assert g0["transactions"] == 0 and math.isnan(g0["p95_ms"])
    s = R.parse_summary("number of failed transactions: 3 (0.030%)\nlatency average = 2.2 ms\ntps = 398.697039 (without initial connection time)\n")
    assert s == {"tps": 398.697039, "failed": 3}

    # the paired reading over repetitions
    def reps(nat, om, key):
        return [{"native": {key: n}, "omni": {key: o}} for n, o in zip(nat, om)]
    r = R.paired(reps([100, 102, 98], [120, 121, 119], "work_inside_line_tps"), "work_inside_line_tps", "higher")
    assert r["reading"] == "better" and r["significant"] and r["ci95"][0] > 0, r
    r = R.paired(reps([100, 102, 98], [120, 121, 119], "p95_ms"), "p95_ms", "lower")
    assert r["reading"] == "**WORSE**", "a higher p95 in all three, clear of the noise, reads WORSE"
    r = R.paired(reps([100, 102, 98], [110, 90, 101], "p95_ms"), "p95_ms", "lower")
    assert r["reading"] == "no difference beyond the noise" and not r["significant"]
    r = R.paired(reps([100.0, 100.0, 100.0], [100.0, 100.0, 100.0 + 1e-9], "tps"), "tps", "higher")
    assert r["reading"] == "same"
    r = R.paired(reps([0, 0, 0], [1, 2, 1], "failed"), "failed", "never more")
    assert r["reading"] == "**WORSE**", "more failed transactions is WORSE whatever the size"
    r = R.paired(reps([20, 20, 20], [11, 12, 10], "pool_mean"), "pool_mean", "shown")
    assert r["reading"] == "shown, not judged"
    assert R.paired(reps([1, 2], [float("nan"), 3], "x"), "x", "lower")["n"] == 1
    print("PASS  database runner: the direction follows where the time goes, calm gives back one idle server and never one in use, "
          "cushion, dwell, cover and fail-up to the pooler's own setting hold; pgbench's log reads into the gauges; the paired "
          "reading says better, WORSE, no difference beyond the noise, same, and never-more")


if __name__ == "__main__":
    main()
