#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Redis cache in our own model, closed loop (evidence class S): the store gate's model for the cache's ceiling.

The harness's application (tools/run_redis.py App) asks 1,500 requests a second for keys drawn Zipf(0.5) from the working set of
the moment; each notch of a workload is a keyspace of its own (the prefix k<n>:, n = base keys x notch), so a notch starts cold
and the last notch's keys stay in memory until evicted. A hit is Redis's answer; a miss is the store trip (5 ms) and a write
back. The model runs that exactly: the same sampler, an LRU cache measured in bytes, and the latency of a hit and of a miss
drawn from the omni-v21 native arms' own records. The brains: native holds the operator's 64 MB; a fixed ceiling (any MB) shows
what a cache of that size could do at all; the standing wire is omni-v21's loop (tools/run_redis.py decide, its
tools/knob_verdict.KnobVerdict and the compass law) read from git; the candidate is the checkout's own Brain, if it has one.

  python3 tools/redis_model.py --fixed 64,128,256,512 [--workloads tuning,small,large,burst] [--seeds 3]
"""
from __future__ import annotations

import argparse
import bisect
import json
import random
import statistics
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

MB = 1024 * 1024
RATE = 1500.0
LINE_MS = 2.0
MISS_PENALTY_MS = 5.0
ZIPF_S = 0.5
KEY_OVERHEAD = 96           # Redis's own bytes a key beside its value (dict entry, robj, SDS headers), the order of the shipped allocator's
BASELINE_MB = 1.0           # the server's memory with no keys
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
WORKLOADS = {"tuning": (8192, 2_500, STEPS), "small": (2048, 10_000, STEPS), "large": (32768, 625, STEPS), "burst": (8192, 2_500, BURST)}
HIT_MS = (0.099, 0.114, 0.122, 0.136, 0.286)      # a hit's latency (ms): the 1st, 25th, 50th, 75th and 99th percentiles of
                                                  # 654,827 hits in the omni-v21 native arms (runs 40254205224, 40276907808)
MISS_EXTRA_MS = (0.254, 0.368, 0.48, 0.569, 0.77)  # a miss beyond the 5 ms store trip, the same percentiles of 155,179 misses


def zipf_cum(n, s=ZIPF_S):
    w = [1.0 / (k + 1) ** s for k in range(n)]
    tot = sum(w); acc = 0.0; cum = []
    for x in w:
        acc += x / tot; cum.append(acc)
    return cum


def draw_q(q, rng):
    i = rng.randrange(4)
    return q[i] + (q[i + 1] - q[i]) * rng.random()


class Cache:
    """An LRU cache in bytes (Redis's allkeys-lru approximates it with sampled candidates)."""

    def __init__(self, ceiling_mb, value_bytes):
        self.keys = OrderedDict(); self.size = value_bytes + KEY_OVERHEAD
        self.ceiling = ceiling_mb * MB; self.evicted = 0

    def used(self):
        return BASELINE_MB * MB + len(self.keys) * self.size

    def set_ceiling(self, mb):
        self.ceiling = mb * MB
        self._evict()

    def _evict(self):
        while self.keys and self.used() > self.ceiling:
            self.keys.popitem(last=False); self.evicted += 1

    def get(self, k):
        if k in self.keys:
            self.keys.move_to_end(k)
            return True
        return False

    def put(self, k):
        self.keys[k] = True; self.keys.move_to_end(k)
        self._evict()


def run_arm(workload, ceiling_of, seed, step_s=30.0, start_mb=64.0):
    """ceiling_of(t, second's observation) -> the ceiling (MB) for the next second; None keeps it."""
    value, base, steps = WORKLOADS[workload]
    rng = random.Random(seed); lat_rng = random.Random(seed + 7)
    cache = Cache(start_mb, value)
    lats = []; per_second = []; ceilings = []; used = []
    t = 0.0
    for notch in [int(x) for x in steps.split()]:
        n = base * notch; cum = zipf_cum(n); prefix = n
        for _ in range(int(step_s)):
            sec = []; ev0 = cache.evicted
            for _ in range(int(RATE)):
                k = (prefix, bisect.bisect_left(cum, rng.random()))
                if cache.get(k):
                    l = draw_q(HIT_MS, lat_rng)
                else:
                    l = MISS_PENALTY_MS + draw_q(MISS_EXTRA_MS, lat_rng); cache.put(k)
                sec.append(l)
            t += 1.0
            lats.extend(sec)
            obs = {"reading_s": sum(sec) / len(sec) / 1000.0, "n": len(sec), "inside": sum(1 for x in sec if x <= LINE_MS),
                   "evicted_last_s": cache.evicted - ev0, "ceiling_mb": cache.ceiling / MB, "used_mb": cache.used() / MB}
            per_second.append(obs); ceilings.append(cache.ceiling / MB); used.append(cache.used() / MB)
            new = ceiling_of(t, obs)
            if new is not None and abs(new - cache.ceiling / MB) > 1e-9:
                cache.set_ceiling(new)
    lats.sort()
    q = lambda p: lats[min(len(lats) - 1, int(p * len(lats)))]
    return {"work_inside_line_rps": sum(o["inside"] for o in per_second) / len(per_second), "p95_ms": q(0.95), "p99_ms": q(0.99),
            "mean_ms": sum(lats) / len(lats), "ceiling_mean_mb": statistics.mean(ceilings), "used_mean_mb": statistics.mean(used),
            "hit_share": sum(1 for x in lats if x < MISS_PENALTY_MS) / len(lats)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fixed", default="64,128,256,512")
    ap.add_argument("--workloads", default="tuning,small,large,burst")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--step-s", type=float, default=30.0)
    a = ap.parse_args(argv)
    for wl in a.workloads.split(","):
        print(f"== {wl}")
        for mb in [float(x) for x in a.fixed.split(",")]:
            rs = [run_arm(wl, lambda t, o: None, s, a.step_s, start_mb=mb) for s in range(101, 101 + a.seeds)]
            m = {k: statistics.mean(r[k] for r in rs) for k in rs[0]}
            print(f"   fixed {mb:>5.0f} MB: work inside the line {m['work_inside_line_rps']:7.1f} a second, hits {100 * m['hit_share']:5.1f}%, "
                  f"mean {m['mean_ms']:5.2f} ms, p95 {m['p95_ms']:5.2f}, p99 {m['p99_ms']:5.2f}, used {m['used_mean_mb']:6.1f} MB")


if __name__ == "__main__":
    main()
