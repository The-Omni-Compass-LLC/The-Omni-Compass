#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The modelled machine's service for the CPU power harness (tools/run_cpu_power.py --plant sim), as the model's own queue.

The harness's modelled service was a sleep of the service time in worker processes, its latency measured by the wall clock,
so the machine's own load entered the model's physics: on a loaded runner late wake-ups read as slow requests, the verdict's
costs turned noisy and no notch was ever allowed, while a quiet runner passed (30 October 2026, tests/test_run_cpu_power.py).
Here the service is a queue of one server per worker advanced in modelled time: arrivals are the schedule's own times (each
step's count and the seeded spread, the same in both arms), a request is served when the model's clock reaches it, at the
service time the ceiling of that moment gives, and its latency is the model's, never a sleep. The real machine's path
(work_unit on real cores) is untouched. tools/run_cpu_power.py is inside the engine's fingerprint (omni-v15, every wire that
holds a governor's rules), so this model lives beside it and is driven through the seam the harness's test already uses
(ModelService in place of Service); it goes into the wire itself with the next engine version."""
from __future__ import annotations

import collections
import heapq
import random
import threading
import time

from tools import run_cpu_power as R


class ModelService(R.Service):
    """R.Service with the modelled machine's service as the model's own queue (sim_root set); the real plant as before."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sim = None
        if self.sim_root:
            self.sim = R.SimPlant.__new__(R.SimPlant); R.Plant.__init__(self.sim, self.sim_root)
            self.free = [0.0] * self.n_workers                                 # each modelled server: free from this modelled time (s)
            self.wrng = [random.Random((self.seed or 0) * 7919 + i) for i in range(self.n_workers)]   # each server's spread, seeded as the workers were
            self.arrived, self.pending = collections.deque(), []               # arrived and not yet served; served and not yet done
            self._factor = 1.0

    def _advance(self, now_rel):
        """The model up to modelled time now_rel (s since t0): every arrived request whose service can start is served by the
        first free server at this moment's service time; every served request whose service has ended is recorded. Under the lock."""
        if self.sim is None:
            return
        try:
            self._factor = self.sim.service_factor()
        except (OSError, ValueError):                                          # the modelled file mid-replacement: the last factor stands
            pass
        while self.arrived:
            a = self.arrived[0]
            i = min(range(self.n_workers), key=self.free.__getitem__)
            start = max(a, self.free[i])
            if start > now_rel:
                break                                                          # it waits: its service has not begun, so its time is not yet known
            self.arrived.popleft()
            svc = self.service_ms / 1000.0 * self._factor * self.wrng[i].uniform(0.95, 1.05)
            self.free[i] = start + svc
            heapq.heappush(self.pending, (start + svc, a))
        while self.pending and self.pending[0][0] <= now_rel:
            done, a = heapq.heappop(self.pending)
            self.records.append((a, done - a)); self.done += 1; self.last_done_t = self.t0 + done

    def run(self):
        if self.sim is None:
            return super().run()
        self.t0 = time.monotonic()
        step_start = 0.0
        for step in self.steps:
            rate = step * self.unit; period = 1.0 / rate
            n_step = int(round(rate * self.step_s))                            # the step's requests, the same count in both arms
            next_rel = step_start
            for _ in range(n_step):
                while True:
                    now_rel = time.monotonic() - self.t0
                    if now_rel >= next_rel:
                        break
                    with self.lock:
                        self._advance(now_rel)
                    time.sleep(min(0.002, next_rel - now_rel))
                with self.lock:
                    self.arrived.append(next_rel); self.issued += 1
                    self._advance(now_rel)
                next_rel += period * self.rng.uniform(*self.JITTER)            # a Poisson-like spread around the rate, the same seed in both arms
            step_start += self.step_s
        deadline = time.monotonic() + 5.0                                     # the queue drains for at most five seconds
        while self.done < self.issued and time.monotonic() < deadline:
            with self.lock:
                self._advance(time.monotonic() - self.t0)
            time.sleep(0.05)
        self.stop_flag.set()

    def last_second(self, line_ms, since_s=1.0):
        if self.sim is None:
            return super().last_second(line_ms, since_s)
        if self.t0 is None:
            return 0, 0, None
        now_rel = time.monotonic() - self.t0
        with self.lock:
            self._advance(now_rel)
            lat = [l for t, l in self.records[-5000:] if t + l >= now_rel - since_s]
        if not lat:
            return 0, 0, None
        return len(lat), sum(1 for l in lat if l * 1000.0 <= line_ms), sum(lat) / len(lat)
