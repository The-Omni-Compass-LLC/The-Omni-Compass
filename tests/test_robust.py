# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The robustness test's readings (tools/live_reps.py, docs/ROBUSTNESS_PREREGISTRATION.md) without a cluster: the kill and
hand-back marks are read from robust.log, the 120 s after the kill are compared in both arms from the probe's own records,
the governor's memory ratio comes from the process-table samples, a hand-back past the allowance or a memory growth past
the limit reads WORSE, and the three-run rows read confirmed only when every run's every repetition was handed back."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import live_reps as R
from tools import confirm_abc as C


def arm(root, name, rep, t0, kill_at, handed_back, mode="kill", rss=(50000, 52000), second=True, native=False):
    d = root / f"bench-{name}-{rep}"; d.mkdir()
    (d / "window_start.txt").write_text(f"{t0}\n")
    lines = [f"{t0} robust {mode}: window 900 s, start {t0}"]
    if mode == "kill":
        if native:
            lines.append(f"{t0 + kill_at} kill mark (native: nothing to kill)")
        else:
            lines.append(f"{t0 + kill_at} kill: SIGKILL to governor pid 1234 (settings before: target=40)")
            lines.append(f"{t0 + kill_at + handed_back} handed back: every setting at the operator's after {handed_back} s (target=50)" if handed_back is not None
                         else f"{t0 + kill_at + 300} NOT handed back after 300 s: target=40")
            if second:
                lines.append(f"{t0 + 450} second governor started: pid 2345, 7 decisions to the end of the window")
    (d / "robust.log").write_text("\n".join(lines) + "\n")
    # the probe: a sample every 5 s; slow and failed samples only in the 120 s after the kill of the native arm
    rows = ["elapsed_seconds,latency_ms,ok"]
    for e in range(0, 900, 5):
        slow = native and kill_at <= e <= kill_at + 120 and e % 10 == 0
        rows.append(f"{e},{900.0 if slow else 100.0},{0 if (native and e == kill_at + 20) else 1}")
    (d / "latency.csv").write_text("\n".join(rows) + "\n")
    if not native:
        # two hours of samples every 15 s: the first ten minutes at rss[0], the last ten at rss[1], the middle between them
        last_t = 15 * 479
        samples = ["epoch_s,rss_kb,processes"] + [f"{t0 + 15 * i},{rss[0] if 15 * i <= 600 else rss[1] if 15 * i >= last_t - 600 else (rss[0] + rss[1]) // 2},1" for i in range(480)]
        (d / "rss.csv").write_text("\n".join(samples) + "\n")
        (d / "audit.jsonl").write_text("".join(json.dumps({"decision": {"n": i}}) + "\n" for i in range(13)))
        (d / "watchdog.log").write_text(json.dumps({"watchdog": "handed back", "ok": True}) + "\n")
    return d


def main():
    with tempfile.TemporaryDirectory() as t:
        root = Path(t); t0 = 1_800_000_000.0
        n = arm(root, "native", 1, t0, 360, None, native=True)
        o = arm(root, "compass", 1, t0, 360, 12)
        m = R.robust_marks(o)
        assert m["kill_epoch"] == t0 + 360 and m["handed_back_s"] == 12 and m["second_governor"] and m["mode"] == "kill", m
        assert R.robust_marks(n)["kill_epoch"] == t0 + 360 and "handed_back_s" not in R.robust_marks(n), "native carries the mark only"
        wn, wo = R.robust_window(n, 500.0), R.robust_window(o, 500.0)
        over, failed = "robust: time over the line in the 120 s after the kill (% of samples)", "robust: failed requests in the 120 s after the kill (%)"
        assert wn[over] > wo[over] == 0.0 and wn[failed] > wo[failed] == 0.0, (wn, wo)
        assert abs(R.robust_memory(o)["ratio"] - 52000 / 50000) < 1e-9
        L, s = R.robust_table(root, ["native", "compass"])
        assert s["compass"]["handed_back_within_allowance_all"] and s["compass"]["handed_back_s_max"] == 12 and s["compass"]["second_governor_all"]
        assert any("| omni | 1 | kill | 12 | yes | yes | 1 | 1.040 | 13 |" in x for x in L), L
        # a slow hand-back, a leak and a missing second governor read WORSE
        arm(root, "compass", 2, t0, 360, 90, rss=(50000, 70000), second=False)
        L, s = R.robust_table(root, ["native", "compass"])
        assert not s["compass"]["handed_back_within_allowance_all"] and s["compass"]["second_governor_all"] is False and s["compass"]["memory_ratio_max"] > R.ROBUST_MEMORY_LIMIT
        assert any("**no: WORSE**" in x and "(a leak: WORSE)" in x for x in L)
        # never handed back
        arm(root, "compass", 3, t0, 360, None)
        _, s = R.robust_table(root, ["native", "compass"])
        assert s["compass"]["never_handed_back"] == 1 and s["compass"]["handed_back_s_max"] == float("inf")
        # the three-run rows: confirmed only when every run was handed back within the allowance everywhere
        good = {"compass": {"repetitions": 10, "kill_repetitions": 10, "handed_back_within_allowance_all": True, "handed_back_s_mean": 11.0, "handed_back_s_max": 18.0,
                            "never_handed_back": 0, "second_governor_all": True, "memory_ratio_max": 1.03, "allowance_s": 60.0, "memory_limit": 1.25}}
        bad = {"compass": dict(good["compass"], handed_back_within_allowance_all=False, handed_back_s_max=95.0, memory_ratio_max=1.40)}
        runs = [("1", {}, 10, good), ("2", {}, 10, good), ("3", {}, 10, good)]
        lines, rows = C.robust_rows(runs)
        assert len(lines) == 3 and "confirmed: handed back" in lines[0] and "no leak" in lines[2]
        lines, rows = C.robust_rows([("1", {}, 10, good), ("2", {}, 10, bad), ("3", {}, 10, good)])
        assert "WORSE" in lines[0] and "a leak" in lines[2]
        assert C.robust_rows([("1", {}, 10, good), ("2", {}, 10, None), ("3", {}, 10, good)]) == ([], {}), "a run without the block makes no robustness rows"
        assert set(R.ROBUST) <= set(R.KEYS) and R.ROBUST <= C.LOWER
    print("PASS  robustness readings: the kill and hand-back marks, the 120 s after the kill in both arms, the memory ratio; a late hand-back, a leak or a missing "
          "second governor reads WORSE; the three-run rows confirm only when every run's every repetition was handed back within the allowance")


if __name__ == "__main__":
    main()
