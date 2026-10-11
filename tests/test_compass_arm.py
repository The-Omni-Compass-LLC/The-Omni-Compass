# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The compass on a realm muscle keeps its state from one decision to the next (realms/compass_arm.py).

Each muscle's compass is made once, on its first decision, and then carries its position, its velocity and the knob's
continuous value forward. A compass made fresh every decision would forget the knob between decisions, so the knob could
never travel more than one step from native. A renamed attribute did exactly that (2026-10-05); this test keeps it from
coming back."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from realms.compass_arm import compass_apply  # noqa: E402
from realms.presets import PRESETS  # noqa: E402


class Axis:
    """A stand-in reaction wheel (its own preset's physics, where an effort cap pays): calm (no queue, light load), so the
    compass gives effort back step by step."""
    template = "motion_axis"
    P = PRESETS["reaction_wheel"]
    vhist = []

    def observe(self):
        return {"queue_ratio": 0.0, "load_ratio": 0.2, "power_stress": 0.0}


def main():
    p = Axis()
    compass_apply(p, "power")
    law = p._compass_law
    xs = [p._compass_law_x]
    for _ in range(40):
        compass_apply(p, "power")
        assert p._compass_law is law, "the compass was made again: its state would be lost between decisions"
        xs.append(p._compass_law_x)
    assert xs[-1] < xs[1] < 1.0, f"the knob did not travel from native across decisions: {xs[:3]} ... {xs[-1]}"
    assert all(b <= a + 1e-12 for a, b in zip(xs, xs[1:])), "a calm muscle's knob only goes down"
    assert xs[-1] >= 0.4 - 1e-12, "never under the cover"
    print(f"compass arm: one compass per muscle, kept across decisions; a calm axis eased from 1.00 to {xs[-1]:.2f} "
          f"over 40 decisions, never under its cover (0.40)")

    # Omni v4: every knob is wired, the loaded axis's speed knob too; the muscle's own verdict (Gate) decides live, and
    # the physics still says which axes have slack (where the verdict is expected to refuse)
    from realms.compass_arm import lever, speed_slack
    class Busy(Axis):
        P = PRESETS["rail_traction"]                            # a train at its timetable's capacity: duty about 0.8
    class Light(Axis):
        P = PRESETS["flight_axis"]                              # a flight axis: duty about 0.34
    assert not speed_slack(Busy()) and lever(Busy(), "capacity") is not None, "every knob wired: the verdict decides"
    assert speed_slack(Light()) and lever(Light(), "capacity") is not None, "an axis with slack offers its speed knob"
    for name, P in PRESETS.items():
        if "task_rate" in P:
            class Any(Axis):
                pass
            Any.P = P
            print(f"  speed knob on {name}: wired; {'slack to give back' if speed_slack(Any()) else 'no slack: the brain finds nothing to try'}")
    gate_tests()
    print("PASS test_compass_arm")


class Toy:
    """A stand-in process loop for the gate: its give-back (the setpoint eased toward its calm end) saves `saving` of its
    energy per unit of work and adds `hurt` to its load (its service position rises with it)."""
    template = "process_loop"

    def __init__(self, seed, saving=0.0, hurt=0.0):
        import random
        self.P = {"dt": 15.0, "tau": 15.0, "theta": 0.0, "sp": 1.0, "calm": 0.9}
        self.m = {"work": 0.0, "energy_j": 0.0, "viol": 0, "steps": 0}
        self.vhist, self.override = [], {}
        self.rng = random.Random(seed)
        self.saving, self.hurt, self.load = saving, hurt, 0.4

    def observe(self):
        return {"queue_ratio": 0.0, "load_ratio": self.load}

    def step(self):
        import math
        acting = self.override.get("setpoint", 1.0) < 1.0
        work = 10.0 * math.exp(self.rng.gauss(0.0, 0.05))
        self.m["work"] += work
        self.m["energy_j"] += work * 2.0 * math.exp(self.rng.gauss(0.0, 0.05)) * ((1.0 - self.saving) if acting else 1.0)
        self.m["steps"] += 1
        self.load = 0.4 + (self.hurt if acting else 0.0)


def drive(plants, gate, steps, restart_at=None):
    acted = 0
    for k in range(steps):
        if k == restart_at:
            for p in plants:
                p.m = {"work": 0.0, "energy_j": 0.0, "viol": 0, "steps": 0}     # the learning period's meters closed
        out = gate.step(plants, [{"setpoint": 0.95}] * len(plants))
        for p, o in zip(plants, out):
            p.override = o
            acted += int(bool(o))
            p.step()
    return acted


def gate_tests():
    """Omni v4's gate on a realm muscle (realms/compass_arm.py Gate): every copy proven together, only give-backs tried."""
    from realms.compass_arm import Gate, give_back
    # a give-back that saves 3% with no cost to the service: proven across ten copies, then used
    ps = [Toy(i, saving=0.03) for i in range(10)]
    g = Gate(ps, "setpoint")
    acted = drive(ps, g, 700, restart_at=350)
    v = g.muscle.verdicts["give back"]
    assert v.allowed == 1 and acted > 0, (g.body.events[:6], g.body.counts)
    # the same saving with the service pushed up (a part made worse): never allowed
    ps = [Toy(100 + i, saving=0.03, hurt=0.4) for i in range(10)]
    g = Gate(ps, "setpoint")
    drive(ps, g, 700)
    assert g.muscle.verdicts["give back"].allowed == 0, g.body.events[:6]
    assert any(e["verdict"].startswith("step refused") for e in g.body.events), g.body.events[:6]

    # never a spend beyond native: an autoscaler target lowered (more pods) is not offered, a power cap given back is,
    # where the pool's own figures say it saves
    class Pool:
        template = "compute_pool"
        P = dict(PRESETS["server"])
    assert give_back(Pool(), "capacity", {"target": 0.6 * Pool.P["target"]}) == {}, "a spend beyond native is never tried"
    assert give_back(Toy(0), "power", {"power": 0.8}) == {}, "a process loop's cap saves only by not delivering"
    print(f"  gate: a 3% saving proven on ten copies and used ({acted} copy-decisions); a saving that pushes the service up "
          "refused; a spend beyond native never offered")


if __name__ == "__main__":
    main()
