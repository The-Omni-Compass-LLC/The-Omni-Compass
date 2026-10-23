# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v17: Omni-Compass by itself (the founder's order of 23 October; docs/SOLO_PREREGISTRATION.md). The pod muscle of its own
sets the replica count of a workload the operator names (--own-replicas) and no autoscaler governs, through the workload's own
scale, by strict C's rule at the compass's target; it holds where an autoscaler governs the workload, never goes below the
operator's count at the max, writes nothing when the replicas are left native, and the reset hands the operator's count back.
In the models, a pool switched to by itself holds its count unless the brain's floor or ceiling moves it."""
import json
import unittest

from omni_controller.controller import Controller, parser, OWN_REPL_ANN, OWN_TARGET_ANN, OWN_RANGE_ANN


class Kube:
    """The workload default/web: its deployment (replicas, CPU request, selector, annotations) and its pods' usage."""
    def __init__(self, replicas=2, busy=1.0, target="50", rng="1,10", hpa=False):
        self.replicas, self.busy, self.hpa, self.writes = replicas, busy, hpa, []
        self.ann = {OWN_TARGET_ANN: target, OWN_RANGE_ANN: rng}
        self.audit = lambda r: None

    def get(self, *args):
        if args[:2] == ("get", "deployment"):
            return {"metadata": {"name": "web", "namespace": "default", "annotations": dict(self.ann)},
                    "spec": {"replicas": self.replicas, "selector": {"matchLabels": {"app": "web"}},
                             "template": {"spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}}}]}}}}
        if args[:2] == ("top", "pods"):
            return "\n".join(f"web-{i} {int(200 * self.busy)}m 10Mi" for i in range(self.replicas))
        if args[:2] == ("get", "hpa"):
            return {"items": self._hpas()}
        raise ValueError(args)

    def _hpas(self):
        return [{"metadata": {"name": "web", "namespace": "default"}, "spec": {"scaleTargetRef": {"name": "web"}}}] if self.hpa else []

    def write(self, args, why):
        self.writes.append(list(args))
        if args[0] == "scale":
            self.replicas = int(args[-1].split("=")[1])
        elif args[0] == "annotate":
            kv = args[-1]
            if kv.endswith("-"):
                self.ann.pop(kv[:-1], None)
            else:
                k, v = kv.split("=", 1); self.ann[k] = v


def governor(k, *extra):
    a = parser().parse_args(["--mode", "nodepool", "--law", "compass", "--own-replicas", "default/web", "--audit", "", *extra])
    return Controller(a, kube=k)


def decide(c, k, slo_clean=True):
    s = {"hpas": k._hpas(), "pending": 0}
    return c._own_pods(s, {"slo_clean": slo_clean, "security_block": 0.0}, 0.6)


class OwnPods(unittest.TestCase):
    def test_busy_pods_get_more_at_once(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        self.assertEqual(decide(c, k), {("default", "web"): 4})       # ceil(2 x 100% / 50%) = 4, up at once
        self.assertEqual(k.writes[0], ["annotate", "deployment", "web", "-n", "default", "--overwrite", f"{OWN_REPL_ANN}=2"])
        self.assertEqual(k.writes[-1], ["scale", "deployment", "web", "-n", "default", "--replicas=4"])

    def test_an_autoscaler_on_the_workload_holds_the_muscle(self):
        k = Kube(replicas=2, busy=1.0, hpa=True); c = governor(k)
        self.assertEqual(decide(c, k), {})
        self.assertEqual(k.writes, [])

    def test_never_below_the_operators_count_at_the_max(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        decide(c, k)                                                   # 2 -> 4, the count of 2 recorded
        k.busy = 0.05
        for _ in range(3 * c.n_strict_window):
            decide(c, k)
        self.assertEqual(k.replicas, 2)                                # back to the operator's count, never under it

    def test_fewer_pods_only_after_the_window(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        decide(c, k); k.busy = 0.05
        decide(c, k)
        self.assertEqual(k.replicas, 4)                                # the window's highest recommendation holds

    def test_replicas_left_native_write_nothing(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k, "--native", "replicas")
        self.assertIsNone(decide(c, k))
        self.assertEqual(k.writes, [])

    def test_no_target_named_writes_nothing(self):
        k = Kube(replicas=2, busy=1.0); k.ann.pop(OWN_TARGET_ANN); c = governor(k)
        self.assertEqual(decide(c, k), {})
        self.assertEqual(k.writes, [])

    def test_the_reset_hands_the_count_back(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        decide(c, k)
        c.restore()
        self.assertEqual(k.replicas, 2)
        self.assertNotIn(OWN_REPL_ANN, k.ann)


class ModelPools(unittest.TestCase):
    def test_a_pool_by_itself_holds_its_count(self):
        from realms import harness as H
        row = next(r for r in H.catalog() if r["template"] == "compute_pool" and r["knob"] == "capacity")
        p = H.make_plant(row, 7101); p.native_off = True
        n0 = p.n + len(p.pending)
        for _ in range(60):
            p.step()
        self.assertEqual(p.n + len(p.pending), n0)

    def test_by_itself_is_the_same_arm_where_native_is_a_setting(self):
        from realms.harness import native_off_pool
        self.assertTrue(native_off_pool("compute_pool", "capacity"))
        self.assertTrue(native_off_pool("compute_pool", "setpoint"))
        self.assertFalse(native_off_pool("compute_pool", "power"))
        self.assertFalse(native_off_pool("thermal_zone", "setpoint"))


if __name__ == "__main__":
    unittest.main()
