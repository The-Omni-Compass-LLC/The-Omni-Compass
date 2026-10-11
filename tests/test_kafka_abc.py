# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Kafka A/B/C rule (tools/kafka_abc.py): confirmed only with the same sign and every interval clear of zero in all three
runs; an interval over zero reads no difference beyond the noise with its count; clear runs pointing different ways read
the runs disagree; any lost message is WORSE; the knob's moves are shown; the tuning workload is shown and not counted."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import kafka_abc as M


def pr(diff, lo, hi, native=100.0):
    return {"native": native, "omni": native + diff, "diff": diff, "ci95": [lo, hi], "n": 3, "significant": lo > 0 or hi < 0, "reading": "x"}


def arm(**kw):
    base = {"work_inside_line_mps": 400.0, "mps": 420.0, "p95_ms": 400.0, "p99_ms": 450.0, "p50_ms": 100.0, "mean_ms": 150.0, "lag_max": 300, "lag_mean": 50.0,
            "lost": 0, "consumers_mean": 2.0, "consumers_max": 2, "cpu_busy_share": 0.5, "cpu_seconds": 120.0, "cpu_s_per_1k_inside": 1.0, "rebalances": 2,
            "handed_back": True, "failups": 0}
    base.update(kw); return base


def rec(name, tuning=False, **omni):
    reps = [{"native": arm(), "omni": arm(**omni)} for _ in range(3)]
    for i, r in enumerate(reps):
        r["omni"]["p95_ms"] += i * 2.0; r["native"]["p95_ms"] += i * 1.0
    return {"workload": name, "tuning": tuning, "service_ms": 2.0, "payload_bytes": 256, "steps": "1 2 3", "step_s": 20.0, "line_ms": 500.0,
            "native_consumers": 2, "cover": [1, 8], "capacity_mps": 950.0, "base_rate_mps": 142.0, "engine": {"version": "omni-v3", "commit": "abc123def456"}, "reps": reps}


def main():
    assert M.verdict([pr(-20, -30, -10)] * 3, "lower") == "**confirmed better**"
    assert M.verdict([pr(+3, +1, +5)] * 3, "lower") == "**confirmed WORSE**", "more consumers held reads WORSE"
    assert M.verdict([pr(+3, +1, +5)] * 3, "higher") == "**confirmed better**"
    assert M.verdict([pr(-20, -30, -10), pr(-20, -30, -10), pr(-2, -10, +6)], "lower") == "no difference beyond the noise (1 of 3 runs)"
    assert M.verdict([pr(-20, -30, -10), pr(+20, +10, +30), pr(-20, -30, -10)], "lower") == "**the runs disagree**"
    assert M.verdict([pr(0, -1, 1, native=0)] * 3, "never more") == "same"
    assert M.verdict([pr(0, -1, 1, native=0), pr(1, 0, 2, native=0), pr(0, -1, 1, native=0)], "never more") == "**confirmed WORSE**", "a lost message in any run is WORSE"
    assert M.verdict([pr(1, 0, 2)] * 3, "shown") == "shown, not judged"
    with tempfile.TemporaryDirectory() as t:
        dirs = []
        for i in (1, 2, 3):
            d = Path(t) / f"run-{i}"
            for name, r in (("light", rec("light", p95_ms=20.0, consumers_mean=5.0, consumers_max=8)), ("tuning", rec("tuning", tuning=True, p95_ms=12.0))):
                (d / f"kafka-{name}").mkdir(parents=True); (d / f"kafka-{name}" / f"{name}.json").write_text(json.dumps(r))
            dirs.append(str(d))
        out = Path(t) / "V3.md"
        assert M.main(dirs + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "## light" in txt and "## tuning" in txt and "shown and not counted" in txt
        assert "Across 1 untouched workloads" in txt, "the tuning workload is not counted"
        assert "| consumers running, mean (the resources held) | 2 | 5 |" in txt and "confirmed WORSE" in txt
        assert json.loads(out.with_suffix(".json").read_text())["workloads"]["light"]["p95_ms"]["reading"] == "confirmed better"
    print("PASS  Kafka A/B/C rule: confirmed only with the same sign and every interval clear of zero in all three runs; an interval over zero "
          "reads no difference beyond the noise with its count; any lost message is WORSE; consumers held more reads WORSE; the tuning workload is not counted")


if __name__ == "__main__":
    main()
