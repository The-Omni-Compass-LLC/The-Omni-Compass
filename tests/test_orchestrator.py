# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass's own orchestrator (omni_orchestrator/): the room rule, the brain, the yardstick and the ledger."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omni_orchestrator.brain import OmniBrain, Yardstick, machines_needed  # noqa: E402
from omni_orchestrator.control import Control  # noqa: E402
from omni_orchestrator.scheduler import place, room  # noqa: E402
from omni_orchestrator.workload import chain  # noqa: E402


def machines(*states):
    return {f"m{i}": {"name": f"m{i}", "cpu_m": 500, "state": s} for i, s in enumerate(states, 1)}


def unit(machine, service="web", req=250):
    return {"machine": machine, "service": service, "req_m": req}


class RoomRule(unittest.TestCase):
    def test_a_unit_goes_only_where_its_request_fits(self):
        ms = machines("awake", "awake")
        us = [unit("m1"), unit("m1"), unit("m2"), unit("m2")]
        self.assertIsNone(place(250, "web", ms, us))
        self.assertEqual(room(ms["m1"], us), 0)

    def test_no_unit_goes_to_a_machine_that_is_not_awake(self):
        ms = machines("parked", "booting", "draining", "awake")
        self.assertEqual(place(250, "web", ms, []), "m4")

    def test_pack_fills_the_fullest_machine_that_fits(self):
        ms = machines("awake", "awake", "awake")
        us = [unit("m1"), unit("m2", "other")]
        # the service stands on m1 alone: its next unit goes to another machine, the fullest that fits (m2)
        self.assertEqual(place(250, "web", ms, us, "pack"), "m2")
        us.append(unit("m2"))
        # on two machines now: the best fit wins, m1 (250 m left, the unit fills it)
        self.assertEqual(place(250, "web", ms, us, "pack"), "m1")

    def test_the_busy_rule_keeps_a_unit_off_a_machine_at_its_top(self):
        ms = machines("awake", "awake")
        ms["m1"]["busy_m"], ms["m2"]["busy_m"] = 380.0, 100.0       # m1 at 76% of its 500 m, m2 at 20%
        self.assertEqual(place(250, "web", ms, [], "pack", "requests"), "m1")   # by requests both fit; pack picks the fullest by name
        self.assertEqual(place(250, "web", ms, [], "pack", "busy"), "m2")       # under the busy rule m1 has no room
        ms["m2"]["busy_m"] = 300.0                                      # 60%: 75 m of room under 75%, less than a unit
        self.assertIsNone(place(250, "web", ms, [], "pack", "busy"))

    def test_spread_takes_the_machine_with_fewest_units_of_the_service(self):
        ms = machines("awake", "awake", "awake")
        us = [unit("m1"), unit("m2")]
        self.assertEqual(place(250, "web", ms, us, "spread"), "m3")


class Brain(unittest.TestCase):
    def test_the_yardstick_follows_kubernetes_published_rule(self):
        y = Yardstick(mn=2, mx=12)
        self.assertEqual(y.recommend(0.0, 4, 1.0), 8)            # twice the target: twice the units
        self.assertEqual(y.recommend(15.0, 8, 0.52), 8)          # inside the 10% tolerance
        self.assertEqual(y.recommend(30.0, 8, 0.1), 8)           # a fall only to the highest of the last 300 s
        self.assertEqual(y.recommend(400.0, 8, 0.1), 2)          # the window has passed

    def test_omni_never_holds_fewer_units_than_its_native_twin(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12)
        want, why = b.decide(0.0, 4, 1.5, 100.0, 0)              # calm response, but the units at three times target
        self.assertGreaterEqual(want, why["twin"])
        self.assertEqual(want, 8)                                # the rule's own limit: at most twice the units at once

    def test_past_the_wall_omni_adds_the_most_it_may_at_once(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12, max_step=3)
        want, why = b.decide(0.0, 4, 0.5, 790.0, 5)
        self.assertEqual(why["force"], 1.0)
        self.assertEqual(want, 7)

    def test_omni_gives_back_one_unit_only_after_the_force_held_down(self):
        b = OmniBrain(line_ms=800, beat_s=5, mn=2, mx=12, hold=3)
        b.twin.recommend(-400.0, 2, 0.5)
        got = [b.decide(t, 6, 0.2, 60.0, 0)[0] for t in (0.0, 5.0, 10.0)]
        self.assertEqual(got[:2], [6, 6])
        self.assertLessEqual(got[2], 6)

    def test_machines_hold_room_for_the_next_step_and_never_fall_below_two(self):
        self.assertEqual(machines_needed(1, 250, 500, 2, 2), 2)
        self.assertEqual(machines_needed(8, 250, 500, 2, 2), 5)


class Ledger(unittest.TestCase):
    def test_a_control_plane_started_again_replays_the_same_ledger(self):
        d = tempfile.mkdtemp()
        spec = {"routes": str(Path(d) / "routes.json"), "front_stats": "http://127.0.0.1:1/_stats",
                "machines": [{"name": "m1", "url": "http://127.0.0.1:1", "cpu_m": 500}],
                "services": [{"name": "web", "replicas": 2, "min": 2, "max": 12, "req_m": 250, "limit_m": 250, "k": 10,
                              "line_ms": 800}]}
        c = Control(spec, d, "omni", 5.0)
        c.record({"ev": "desired", "service": "web", "n": 5})
        c.record({"ev": "unit", "u": {"id": "web-0", "seq": 0, "kind": "service", "service": "web", "machine": "m1",
                                      "port": 9100, "req_m": 250, "state": "placed", "born": 0.0}})
        c.record({"ev": "machine", "name": "m1", "state": "draining"})
        again = Control(spec, d, "omni", 5.0)
        self.assertEqual(again.desired["web"], 5)
        self.assertEqual(set(again.units), {"web-0"})
        self.assertEqual(again.machines["m1"]["state"], "draining")
        self.assertEqual(again.port, 9101)                      # no port is ever given twice


class Work(unittest.TestCase):
    def test_the_answer_is_fixed_by_its_seed(self):
        self.assertEqual(chain(7, 100), chain(7, 100))
        self.assertNotEqual(chain(7, 100), chain(8, 100))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
