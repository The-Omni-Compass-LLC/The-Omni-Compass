# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The sysbench-on-MySQL runner (tools/run_sysbench.py) without a server or sysbench: the decision rule (slow statements grow the
pool by chunks only while it is full, calm with no page read from disk gives back one chunk after the dwell, the wall adds four
chunks, the cover holds), the plug's one-writer rule and its wait for the server's online resize against a fake console, the
server's own reading from the performance schema, sysbench's histogram and summary parsed, quantiles from the histogram, and the
paired reading over repetitions."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_sysbench as S


class FakeCursor:
    def __init__(self, server):
        self.s, self.rows = server, []

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def execute(self, sql):
        s = self.s; q = sql.strip()
        if q.startswith("SHOW GLOBAL STATUS"):
            total = s.mb * S.MB // S.PAGE
            self.rows = [("Innodb_buffer_pool_pages_total", str(total)), ("Innodb_buffer_pool_pages_data", str(int(total * s.fill))),
                         ("Innodb_buffer_pool_pages_free", str(total - int(total * s.fill))), ("Innodb_buffer_pool_reads", str(s.disk_reads)),
                         ("Innodb_buffer_pool_read_requests", "1000"), ("Innodb_buffer_pool_resize_status", s.resize_status)]
        elif q.startswith("SELECT @@innodb_buffer_pool_size"):
            self.rows = [(s.mb * S.MB,)]
        elif "events_statements_summary_global_by_event_name" in q:
            self.rows = [(s.timer_ps, s.count)]
        elif q.startswith("SET GLOBAL innodb_buffer_pool_size"):
            want = int(q.split("=")[1]) // S.MB
            s.pending = want; s.resize_status = "Resizing buffer pool from %d to %d (unit=134217728)." % (s.mb * S.MB, want * S.MB); s.ticks = 2
        else:
            raise AssertionError(sql)

    def fetchall(self):
        # the server's asynchronous resize completes after two reads
        s = self.s
        if s.pending is not None:
            s.ticks -= 1
            if s.ticks <= 0:
                s.mb = s.pending; s.pending = None; s.resize_status = "Completed resizing buffer pool at 260101 12:00:00."
        return self.rows


class FakeServer:
    def __init__(self, mb, fill=0.5):
        self.mb, self.fill, self.disk_reads, self.timer_ps, self.count = mb, fill, 0, 0, 0
        self.resize_status, self.pending, self.ticks = "", None, 0

    def cursor(self):
        return FakeCursor(self)


def main():
    lo, hi = S.COVER_MB
    # the decision rule
    assert S.decide(0.5, 0.35, misses_last_s=0.3, cur_mb=512, last_change_age=20, full=True)[0] == 512 + S.STEP_MB * 4, "slow with the pool full grows by ceil(force / 0.1) chunks"
    assert S.decide(0.5, 0.35, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=False)[0] == 512, "slow with room to spare: not the pool's to mend"
    assert S.decide(0.5, 1.0, misses_last_s=0.3, cur_mb=2000, last_change_age=20, full=True)[0] == hi, "the cover holds on the way up"
    assert S.decide(0.96, 0.0, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=True)[0] == 512 + S.FAILUP_MB and "fail up" in S.decide(0.96, 0.0, 0.0, 512, 20, True)[1]
    assert S.decide(0.96, 0.0, misses_last_s=0.0, cur_mb=1900, last_change_age=20, full=True)[0] == hi, "the cover holds on a fail-up too"
    assert S.decide(0.96, 0.0, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=False)[0] == 512, "no fail-up for a pool with room"
    assert S.decide(0.1, -0.5, misses_last_s=0.004, cur_mb=512, last_change_age=20, full=True)[0] == 512 - S.STEP_MB, "calm with misses under 1% of reads gives a chunk back, full or not (stale pages stay resident)"
    assert S.decide(0.1, -0.5, misses_last_s=0.05, cur_mb=512, last_change_age=20, full=True)[0] == 512, "not while the pool misses more than 1% of its reads: it does not hold the working set"
    assert S.decide(0.1, -0.5, misses_last_s=0.0, cur_mb=512, last_change_age=5, full=False)[0] == 512, "not within the dwell"
    assert S.decide(0.1, -0.5, misses_last_s=0.0, cur_mb=lo, last_change_age=20, full=False)[0] == lo, "never under the cover"
    assert S.decide(0.3, 0.02, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=True)[0] == 512, "inside the cushion nothing moves"
    assert S.miss_share(5, 1000) == 0.005 and S.miss_share(0, 0) == 0.0 and S.miss_share(300, 1000) == 0.3
    # the plug: snapshot once, write in whole chunks and wait for the server's resize, read back, another writer stops it, restore
    srv = FakeServer(512); plug = S.BufferPool(srv)
    assert plug.attach() == 512
    assert plug.write(700) == 640, "a write is rounded to whole chunks (700 MB asks for 5 chunks, 640 MB) and read back once the resize completes"
    assert plug.lever() == 640 and srv.pending is None
    srv.mb = 1024                                               # someone else moved the knob
    try:
        plug.lever(); raise AssertionError("a foreign writer must stop Omni")
    except RuntimeError as e:
        assert "another writer" in str(e)
    srv.mb = 640; srv.resize_status = "Resizing buffer pool from 671088640 to 1073741824 (unit=134217728)."
    assert plug.lever() == 640, "mid-resize the server is still carrying out our write: not a foreign writer"
    srv.resize_status = ""
    assert plug.restore() and srv.mb == 512, "restored to the snapshot and read back"
    assert S.resizing("Resizing buffer pool from 1 to 2.") and S.resizing("Withdrawing blocks to be shrunken.") and not S.resizing("Completed resizing buffer pool at 260101 12:00:00.") and not S.resizing("")
    # the server's own reading and pool figures
    srv.timer_ps, srv.count = 2_000_000_000_000, 1000              # 2 s over 1,000 statements: 2 ms each
    st = S.status(srv)
    assert S.stmt_latency(st) == (2_000_000_000_000, 1000) and S.read_requests(st) == 1000
    mb, used, reads, rs = S.pool_stats(st)
    assert mb == 512 and abs(used - 256) < 1.0 and reads == 0 and not S.resizing(rs), (mb, used, reads, rs)
    assert not S.pool_full(st); srv.fill = 0.95; assert S.pool_full(S.status(srv))
    # sysbench's histogram, summary and quantiles
    txt = ("SQL statistics:\n    queries performed:\n        read:                            59230\n    transactions:                        59230  (2961.50 per sec.)\n"
           "    queries:                             59230  (2961.50 per sec.)\n    ignored errors:                      2      (0.10 per sec.)\n"
           "    reconnects:                          0      (0.00 per sec.)\n\nGeneral statistics:\n    total time:                          20.0005s\n"
           "Latency (ms):\n         min:                                    0.08\n         avg:                                    0.21\n         max:                                   12.10\n"
           "         95th percentile:                        0.42\n         sum:                                12452.50\n\n"
           "Latency histogram (values are in milliseconds)\n       value  ------------- distribution ------------- count\n"
           "       0.100 |****************************************  5000\n       0.200 |**********************                  3000\n"
           "       0.500 |****                                      1500\n       2.000 |*                                        500\n\n"
           "Threads fairness:\n    events (avg/stddev):           1850.9375/12.21\n")
    h = S.parse_histogram(txt)
    assert h == [(0.1, 5000), (0.2, 3000), (0.5, 1500), (2.0, 500)], h
    s = S.parse_summary(txt)
    assert s["transactions"] == 59230 and s["errors"] == 2 and abs(s["seconds"] - 20.0005) < 1e-9 and abs(s["avg_ms"] - 0.21) < 1e-9 and abs(s["p95_ms_sysbench"] - 0.42) < 1e-9, s
    assert S.quantile(h, 0.5) == 0.1 and S.quantile(h, 0.95) == 0.5 and S.quantile(h, 0.99) == 2.0 and S.quantile([], 0.5) != S.quantile([], 0.5)
    assert sum(c for v, c in h if v <= 1.0) == 9500, "transactions inside a 1 ms line, from the histogram"
    # the paired reading, the same rule as the other stores
    reps = [{"native": {"tps": 2900.0, "pool_mb_mean": 512.0, "failed": 0}, "omni": {"tps": 2950.0, "pool_mb_mean": 900.0, "failed": 0}},
            {"native": {"tps": 2910.0, "pool_mb_mean": 512.0, "failed": 0}, "omni": {"tps": 2955.0, "pool_mb_mean": 880.0, "failed": 0}},
            {"native": {"tps": 2890.0, "pool_mb_mean": 512.0, "failed": 0}, "omni": {"tps": 2945.0, "pool_mb_mean": 920.0, "failed": 0}}]
    assert S.paired(reps, "tps", "higher")["reading"] == "better"
    assert S.paired(reps, "pool_mb_mean", "lower")["reading"] == "**WORSE**", "more pool held reads WORSE"
    assert S.paired(reps, "failed", "never more")["reading"] == "same"
    assert S.COVER_MB == (128, 2048) and S.NATIVE_MB == 512 and lo <= S.NATIVE_MB <= hi and S.STEP_MB == S.CHUNK_MB == 128 and S.NATIVE_MB % S.CHUNK_MB == 0
    assert all(s_ >= 1 and r_ > 0 for _, s_, r_, _, _ in S.WORKLOADS.values()) and sum(1 for w in S.WORKLOADS.values() if w[4]) == 1, "one tuning workload"
    print("PASS  sysbench runner: slow statements with the pool full grow the pool by chunks, calm with nothing read from disk gives one back after the dwell, "
          "the wall adds four chunks, the cover holds; the plug snapshots, writes whole chunks, waits for the server's resize, reads back, stops for another "
          "writer and restores; the server's own reading; sysbench's histogram and summary parsed; the paired reading")


if __name__ == "__main__":
    main()
