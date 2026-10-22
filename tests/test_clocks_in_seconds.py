# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every clock of the governor counts seconds (omni-v16, docs/OMNI_V16.md; the founder's order of 22 October: a full
decision every 15 s, the pace of the pod autoscaler's own sync, every clock counted in seconds, 10 s tested, never above
60). The decision period sets only how often the state is read: at 60 s every discrete value is the one omni-v15 used,
and at any other period each filter, memory, window, count and rate keeps its time."""
import random
import unittest
from unittest.mock import Mock

from omnicompass.adapter import ASSIMILATION, Governor, mode_law
from omnicompass.compass_law import Band, CompassLaw
from omnicompass.core import MACRO_DT
from omnicompass.edge import Edge
from omni_controller.capacity import HostCpuSampler
from omni_controller.controller import CLOSURE_PERIOD_S, CONVEY_PERIOD_S, Controller, parser
from omni_controller.muscles import Muscles


def controller(*extra):
    return Controller(parser().parse_args(["--audit", "", *extra]), kube=Mock())


def observations(n, seed=3):
    rng = random.Random(seed)
    return [{"queue_ratio": rng.uniform(0, 0.3), "load_ratio": rng.uniform(0.3, 1.1), "power_stress": rng.uniform(0, 0.5),
             "drift_ratio": rng.uniform(0, 0.1), "stale": 0.0, "security_block": 0.0} for _ in range(n)]


class TheDefault(unittest.TestCase):
    def test_a_decision_every_15_s_and_quick_checks_every_5(self):
        a = parser().parse_args([])
        self.assertEqual((a.interval, a.floor_interval), (15.0, 5.0))


class AtSixtySecondsEverythingIsV15s(unittest.TestCase):
    """The identity: the period every constant was stated at changes nothing."""

    def test_the_engine_core(self):
        g0, g1 = Governor(law=mode_law("fleet")), Governor(law=mode_law("fleet"), period_s=60.0)
        for o in observations(200):
            d0, d1 = g0.step(o, 0), g1.step(o, 0)
            self.assertEqual(d0, d1)
        self.assertEqual(g0.x, g1.x)
        self.assertEqual(g0.t, g1.t)

    def test_the_edge(self):
        rng = random.Random(5)
        e0, e1 = Edge(react=1.0), Edge(react=1.0, per=1.0, lag=1)
        for _ in range(300):
            p = rng.uniform(0, 1)
            self.assertEqual(e0.update(p), e1.update(p))
            if rng.random() < 0.05:
                e0.learn_fall(0.1); e1.learn_fall(0.1)

    def test_the_compass_law(self):
        rng = random.Random(7)
        c0 = CompassLaw(Band(0, 1, center=0.4), dt=60.0, tau=60.0, kp=1.0, smooth=0.3)
        c1 = CompassLaw(Band(0, 1, center=0.4), dt=60.0, tau=60.0, kp=1.0, smooth=0.3, ref_dt=60.0)
        self.assertEqual(c0.kd, c1.kd)
        for _ in range(200):
            p = rng.uniform(0, 1)
            self.assertEqual(c0.force(p), c1.force(p))

    def test_the_controllers_own_clocks(self):
        c = controller("--interval", "60", "--law", "compass", "--dial", "save")
        self.assertEqual((c.n_closure, c.host_cpu.span, c.edge.lag, c.edge.window), (1, 1, 1, 20))
        self.assertEqual((c.edge.narrow, c.edge.fall_decay), (0.05, 0.9995))
        self.assertEqual(c.g.period_s, 60.0)

    def test_the_host_reading(self):
        s = HostCpuSampler(span=1)
        reads = iter(["cpu 100 0 100 800 0", "cpu 160 0 140 900 0", "cpu 200 0 200 1000 0"])
        s.stat_path = Mock(read_text=lambda: next(reads))
        self.assertIsNone(s.sample())
        self.assertAlmostEqual(s.sample(), 100 / 200)             # since the previous sample, as v15
        self.assertAlmostEqual(s.sample(), 100 / 200)


class EveryClockKeepsItsTime(unittest.TestCase):
    def test_the_engine_takes_in_a_minute_of_observation_a_minute(self):
        # a constant observation: four 15-second blends take in exactly what one 60-second blend takes in
        g = Governor(law=mode_law("fleet"), period_s=15.0)
        r = 15.0 / 60.0
        self.assertAlmostEqual(1.0 - (1.0 - (1.0 - (1.0 - ASSIMILATION) ** r)) ** 4, ASSIMILATION, places=12)
        g.step(observations(1)[0], 0)
        self.assertAlmostEqual(g.t, MACRO_DT * r)

    def test_the_engine_converges_as_its_step_shrinks(self):
        # the same telemetry, a reading held for a minute, taken at 60, 15 and 1 s: each step blends in the reading and then
        # advances the engine, so the two are applied in turn, and the finer the step the nearer the engine comes to the one
        # path of the continuous engine (a one-second step stands for it). At 15 s it is nearer than at 60 s, and close
        path = {}
        for period in (60.0, 15.0, 1.0):
            g = Governor(law=mode_law("fleet"), period_s=period)
            for o in observations(120):
                for _ in range(int(round(60.0 / period))):
                    g.step(o, 0)
            path[period] = g.x
        for k in ("E", "U", "I_U", "S"):
            d60, d15 = abs(getattr(path[60.0], k) - getattr(path[1.0], k)), abs(getattr(path[15.0], k) - getattr(path[1.0], k))
            self.assertLessEqual(d15, d60 + 1e-12, k)
            self.assertLess(d15, 0.02, k)

    def test_the_cushion_keeps_its_minutes(self):
        e = Edge(react=4.0, per=0.25, lag=4)
        self.assertEqual(e.window, 80)                              # 20 minutes of readings
        self.assertAlmostEqual((1.0 - e.narrow) ** 4, 0.95, places=12)
        self.assertAlmostEqual(e.fall_decay ** 4, 0.9995, places=12)

    def test_the_wobble_is_read_one_window_apart(self):
        # readings that are 60-second means taken every 15 s share samples; read a step apart they look four times
        # steadier than they are, a window apart they show the spread of one reading
        rng = random.Random(11)
        raw = [rng.gauss(0.4, 0.08) for _ in range(4 * 400)]
        pos = [sum(raw[i - 3:i + 1]) / 4 for i in range(3, len(raw))]   # each reading: the last four quarter-minutes
        one = Edge(react=4.0, per=0.25, lag=1); win = Edge(react=4.0, per=0.25, lag=4)
        for p in pos:
            c_one, c_win = one.update(p), win.update(p)
        self.assertGreater(1.0 - c_win, 1.0 - c_one)                 # the wider, truer cushion

    def test_the_compass_damps_at_its_levers_rate(self):
        for dt in (60.0, 15.0, 10.0, 5.0):
            c = CompassLaw(Band(0, 1, center=0.4), dt=dt, tau=60.0, kp=1.0, smooth=0.3, ref_dt=60.0)
            self.assertAlmostEqual(c.kd, 60.0)
            # the velocity's memory a minute: with the position still, a minute of readings keeps 0.3 of it at any period
            c.p, c.v = 0.5, 1.0
            for _ in range(int(round(60.0 / dt))):
                c.sense(0.5)
            self.assertAlmostEqual(c.v, 0.3, places=12)

    def test_the_controller_at_15_s(self):
        c = controller("--interval", "15", "--law", "compass", "--dial", "save")
        self.assertEqual((c.n_closure, c.host_cpu.span, c.edge.lag, c.edge.window), (4, 4, 4, 80))
        self.assertEqual(c.n_closure * 15.0, CLOSURE_PERIOD_S)
        self.assertAlmostEqual(c.compass_law.kd, 180.0)               # a minute's damping, as at 60 s
        self.assertEqual(c.g.period_s, 15.0)

    def test_the_controller_at_10_s(self):
        c = controller("--interval", "10", "--law", "compass", "--dial", "save")
        self.assertEqual((c.n_closure, c.host_cpu.span, c.edge.lag, c.edge.window), (6, 6, 6, 120))

    def test_the_host_reads_its_minute(self):
        s = HostCpuSampler(span=4)
        reads = iter([f"cpu {100 * k} 0 0 {300 * k} 0" for k in range(1, 8)])
        s.stat_path = Mock(read_text=lambda: next(reads))
        out = [s.sample() for _ in range(7)]
        self.assertIsNone(out[0])
        self.assertAlmostEqual(out[-1], 0.25)                        # over the last four intervals


class TheConveyanceEvery15Seconds(unittest.TestCase):
    def conveys(self, interval, floor, minutes=3):
        c = controller("--interval", str(interval), "--floor-interval", str(floor), "--mode", "nodepool",
                       "--node-scale-cmd", "true {n}", "--latency-file", "/dev/null")
        c.killed = lambda: False
        times = []
        c.m.convey = lambda *a, **k: times.append(c._clock_s())
        for _ in range(int(minutes * 60 / interval)):
            c.decisions += 1; c.fast_k = 0
            c._convey_due()
            waited = 0.0
            while waited + 1e-9 < interval:
                waited += min(floor, interval - waited)
                if waited + 1e-9 < interval:
                    c.fast_k += 1; c._convey_due()
        return times

    def test_every_15_s_at_every_period(self):
        for interval, floor in ((60, 5), (15, 5), (10, 5), (5, 5)):
            t = self.conveys(interval, floor)
            gaps = {round(b - a, 6) for a, b in zip(t, t[1:])}
            self.assertEqual(gaps, {CONVEY_PERIOD_S}, (interval, floor, t[:6]))


class TheCloudNeverOrdersAMachineThatIsNotThere(unittest.TestCase):
    def test_the_order_is_held_to_the_machines_that_exist(self):
        with open(Controller.step.__code__.co_filename) as f:
            src = f.read()
        self.assertIn('rec_n = max(n, min(rec_n, int(s.get("pool", n))))', src)


class TheWarmReserveInTheCloud(unittest.TestCase):
    """In the cloud a machine given back is the cloud's to delete, and the governor never adds one: the machines the largest
    requests of the reserve horizon need are never given back, and nothing is given back before that horizon is read."""

    def test_nothing_given_back_until_the_horizon_is_read(self):
        from omni_controller.controller import RESERVE_S
        c = controller("--interval", "15", "--give-back-only", "--mode", "nodepool", "--headroom", "0.5")
        per_node = 32000.0
        for k in range(int(RESERVE_S / 15) - 1):
            c.decisions = k + 1; c.fast_k = 0
            self.assertEqual(c._warm_reserve(6, 40000.0, per_node), 6)   # unread: every machine in service kept

    def test_the_largest_requests_of_the_horizon_are_held(self):
        from omni_controller.controller import RESERVE_S
        c = controller("--interval", "15", "--give-back-only", "--mode", "nodepool", "--headroom", "0.5")
        per_node, steps = 32000.0, int(RESERVE_S / 15)
        for k in range(steps + 10):
            c.decisions = k + 1; c.fast_k = 0
            req = 120000.0 if k == 10 else 60000.0                      # one peak early in the horizon
            got = c._warm_reserve(6, req, per_node)
        # 10 decisions past the horizon, the peak is still inside it (it fell at decision 11, the horizon starts at 10)
        self.assertEqual(got, 6)                                         # ceil(120 x 1.5 / 32) = 6
        for k in range(steps + 10, steps + 40):
            c.decisions = k + 1; c.fast_k = 0
            got = c._warm_reserve(6, 60000.0, per_node)
        self.assertEqual(got, 3)                                         # the peak left the horizon: ceil(60 x 1.5 / 32)


class TheMusclesInSeconds(unittest.TestCase):
    def muscles(self, interval):
        a = parser().parse_args(["--audit", "", "--interval", str(interval)])
        return Muscles(Mock(), a, lambda r: r)

    def test_cold_start_waits_180_s(self):
        self.assertEqual(self.muscles(60)._coldstart_n(), 3)
        self.assertEqual(self.muscles(15)._coldstart_n(), 12)

    def test_moves_away_from_native_once_a_minute(self):
        m = self.muscles(15)
        got = []
        for k in range(12):
            m.clock_s = 15.0 * k
            got.append(m._spaced("admit"))
        self.assertEqual([k for k, ok in enumerate(got) if ok], [0, 4, 8])


if __name__ == "__main__":
    unittest.main()
