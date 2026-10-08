# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The YCSB-on-MongoDB runner (tools/run_ycsb.py) without a server or YCSB: the decision rule (slow reads grow the cache by
notches only while it is full, calm with nothing evicted gives back one notch after the dwell, the wall adds a quarter of the
cover, the cover holds), the plug's one-writer rule against a fake server console, the server's own reading from serverStatus,
YCSB's raw records and failed-operation summary parsed, and the paired reading over repetitions."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_ycsb as Y


class FakeAdmin:
    def __init__(self, mb):
        self.mb = mb; self.reads = (0, 0)

    def command(self, cmd):
        if cmd == "serverStatus":
            return {"wiredTiger": {"cache": {"maximum bytes configured": self.mb * Y.MB, "bytes currently in the cache": self.mb * Y.MB // 2,
                                             "pages read into cache": 100, "unmodified pages evicted": 5, "modified pages evicted": 1,
                                             "pages evicted by application threads": 0}},
                    "opLatencies": {"reads": {"latency": self.reads[0], "ops": self.reads[1]}}}
        if "setParameter" in cmd:
            cfg = cmd["wiredTigerEngineRuntimeConfig"]; self.mb = int(cfg.split("=")[1].rstrip("M")); return {"ok": 1}
        raise AssertionError(cmd)


class FakeClient:
    def __init__(self, mb):
        self.admin = FakeAdmin(mb)


def main():
    lo, hi = Y.COVER_MB
    # the decision rule
    assert Y.decide(0.5, 0.35, evicted_last_s=10, cur_mb=512, last_change_age=10, full=True)[0] == 512 + Y.STEP_MB * 4, "slow with the cache full grows by ceil(force / 0.1) notches"
    assert Y.decide(0.5, 0.35, evicted_last_s=0, cur_mb=512, last_change_age=10, full=False)[0] == 512, "slow with room to spare: not the cache's to mend"
    assert Y.decide(0.5, 1.0, evicted_last_s=10, cur_mb=2000, last_change_age=10, full=True)[0] == hi, "the cover holds on the way up"
    assert Y.decide(0.96, 0.0, evicted_last_s=0, cur_mb=512, last_change_age=10, full=True)[0] == 512 + Y.FAILUP_MB and "fail up" in Y.decide(0.96, 0.0, 0, 512, 10, True)[1]
    assert Y.decide(0.96, 0.0, evicted_last_s=0, cur_mb=1900, last_change_age=10, full=True)[0] == hi, "the cover holds on a fail-up too"
    assert Y.decide(0.96, 0.0, evicted_last_s=0, cur_mb=512, last_change_age=10, full=False)[0] == 512, "no fail-up for a cache with room"
    assert Y.decide(0.1, -0.5, evicted_last_s=0, cur_mb=512, last_change_age=10, full=False)[0] == 512 - Y.STEP_MB, "calm with nothing evicted gives a notch back"
    assert Y.decide(0.1, -0.5, evicted_last_s=3, cur_mb=512, last_change_age=10, full=True)[0] == 512, "not while pages are being evicted"
    assert Y.decide(0.1, -0.5, evicted_last_s=0, cur_mb=512, last_change_age=2, full=False)[0] == 512, "not within the dwell"
    assert Y.decide(0.1, -0.5, evicted_last_s=0, cur_mb=lo, last_change_age=10, full=False)[0] == lo, "never under the cover"
    assert Y.decide(0.3, 0.02, evicted_last_s=0, cur_mb=512, last_change_age=10, full=True)[0] == 512, "inside the cushion nothing moves"
    # the plug: snapshot once, write and read back, another writer stops it, restore
    fc = FakeClient(512); plug = Y.CacheSize(fc)
    assert plug.attach() == 512 and plug.write(768) == 768 and plug.lever() == 768
    fc.admin.mb = 1024                                           # someone else moved the knob
    try:
        plug.lever(); raise AssertionError("a foreign writer must stop Omni")
    except RuntimeError as e:
        assert "another writer" in str(e)
    assert plug.restore() and fc.admin.mb == 512, "restored to the snapshot and read back"
    # the server's own reading and cache figures from serverStatus
    st = fc.admin.command("serverStatus")
    assert Y.read_latency(st) == (0, 0)
    mb, used, pages, ev = Y.cache_stats(st)
    assert mb == 512 and abs(used - 256) < 1e-9 and pages == 100 and ev == 6
    # YCSB's raw records and its failed-operation summary
    with tempfile.TemporaryDirectory() as t:
        raw = Path(t) / "n.raw"
        raw.write_text("op, timestamp(ms), latency(us)\nREAD,1700000000123,345\nUPDATE,1700000000130,2500\nbad line\nREAD,1700000000140,-1\n")
        recs = Y.parse_raw(raw)
        assert len(recs) == 3 and abs(recs[0][1] - 0.345) < 1e-9 and abs(recs[1][1] - 2.5) < 1e-9, recs
        assert Y.parse_raw(Path(t) / "missing.raw") == []
    assert Y.parse_failed("[OVERALL], RunTime(ms), 20000\n[READ-FAILED], Operations, 3\n[UPDATE-FAILED], Operations, 2\n[READ], Operations, 100\n") == 5
    assert Y.parse_failed("[READ], Operations, 100\n") == 0
    # the paired reading, the same rule as the database and cache benchmarks
    reps = [{"native": {"ops": 2900.0, "cache_mb_mean": 512.0, "failed": 0}, "omni": {"ops": 2950.0, "cache_mb_mean": 900.0, "failed": 0}},
            {"native": {"ops": 2910.0, "cache_mb_mean": 512.0, "failed": 0}, "omni": {"ops": 2955.0, "cache_mb_mean": 880.0, "failed": 0}},
            {"native": {"ops": 2890.0, "cache_mb_mean": 512.0, "failed": 0}, "omni": {"ops": 2945.0, "cache_mb_mean": 920.0, "failed": 0}}]
    assert Y.paired(reps, "ops", "higher")["reading"] == "better"
    assert Y.paired(reps, "cache_mb_mean", "lower")["reading"] == "**WORSE**", "more cache held reads WORSE"
    assert Y.paired(reps, "failed", "never more")["reading"] == "same"
    reps[1]["omni"]["failed"] = 1
    assert Y.paired(reps, "failed", "never more")["reading"] == "**WORSE**"
    assert Y.COVER_MB == (256, 2048) and Y.NATIVE_MB == 512 and lo <= Y.NATIVE_MB <= hi and len(Y.YCSB_SHA256) == 64
    print("PASS  YCSB runner: slow reads with the cache full grow the cache by notches, calm with nothing evicted gives one back after the dwell, the wall adds a quarter "
          "of the cover, the cover holds; the plug snapshots, reads back, stops for another writer and restores; the server's own reading; YCSB's records parsed; the paired reading")


if __name__ == "__main__":
    main()
