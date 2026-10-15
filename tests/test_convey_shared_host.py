# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""One processor is conveyed once (Omni v7, omni_controller/muscles.py, convey): on kind, where every node is a container
on one machine, the serving pods share that machine's CPU counted once; no limit is raised while the machine is at or over
75% busy, cannot be read, or has a pod starting on it; on separate machines each node keeps its own arithmetic and only a
start on that node holds it. Every case reads the same conveyance code the live controller runs."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from omni_controller.capacity import starting
from omni_controller.muscles import Muscles


def node(name, kind=True, cpu="4"):
    return {"metadata": {"name": name}, "spec": {"providerID": f"kind://docker/omni/{name}" if kind else f"azure:///{name}"},
            "status": {"allocatable": {"cpu": cpu}}}


def pod(name, node_name, app="web", req="200m", limit="500m", ready=True, phase="Running", ns="default"):
    return {"metadata": {"name": name, "namespace": ns, "labels": {"app": app}},
            "spec": {"nodeName": node_name, "containers": [{"resources": {"limits": {"cpu": limit}, "requests": {"cpu": req}}}]},
            "status": {"phase": phase, "conditions": [{"type": "Ready", "status": "True" if ready else "False"}]}}


class Cluster:
    def __init__(self, nodes, pods):
        self.nodes, self.pods, self.writes = nodes, pods, []

    def get(self, *args):
        if args[1] == "resourcequota":
            return {"items": []}
        if args[1] == "nodes":
            return {"items": copy.deepcopy(self.nodes)}
        if args[1] == "pods":
            return {"items": copy.deepcopy(self.pods)}
        if args[1] == "deployment":
            return {"metadata": {"annotations": {}}, "spec": {"selector": {"matchLabels": {"app": "web"}},
                    "template": {"spec": {"containers": [{"resources": {"limits": {"cpu": "500m"}}}]}}}}
        raise AssertionError(args)

    def write(self, args, why):
        self.writes.append((args, why))
        if args[0] == "patch":
            target = next(p for p in self.pods if p["metadata"]["name"] == args[2])
            target["spec"]["containers"][0]["resources"]["limits"]["cpu"] = json.loads(args[-1])[0]["value"]


class Stat:
    """A /proc/stat whose busy share between two samples is the one given."""
    def __init__(self, busy):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / "stat"
        self.total, self.idle = 1000, 500
        self.busy = busy
        self._write()

    def _write(self):
        self.path.write_text(f"cpu  {self.total - self.idle} 0 0 {self.idle} 0 0 0 0 0 0\n")

    def advance(self):
        self.total += 1000; self.idle += int(round(1000 * (1.0 - self.busy))); self._write()


def muscles(cluster, stat=None):
    events = []
    m = Muscles(cluster, SimpleNamespace(cap_deployments="default/web", cap_min_change_m=10), events.append)
    m._convey_engaged = lambda: True
    if stat is not None:
        from omni_controller.capacity import HostCpuSampler
        m.host_cpu = HostCpuSampler(stat.path)
        m.host_cpu.sample()          # the first of two samples
        stat.advance()
    return m, events


class SharedHostConvey(unittest.TestCase):
    def kind_cluster(self, extra=()):
        nodes = [node("w1"), node("w2"), node("w3")]
        pods = [pod("web-1", "w1"), pod("web-2", "w2"), pod("web-3", "w3"),
                pod("dns", "w1", app="coredns", req="300m", ns="kube-system")] + list(extra)
        return Cluster(nodes, pods)

    def test_one_host_counts_its_processor_once(self):
        c, stat = self.kind_cluster(), Stat(0.40)
        m, _ = muscles(c, stat)
        out = m.convey()
        # (0.95 x 4000 - 300) / 3 = 1166.7 -> 1160 per serving pod, not 3700 on each of three nodes
        self.assertEqual(out, {"default/web-1": 1160, "default/web-2": 1160, "default/web-3": 1160})
        self.assertLessEqual(sum(out.values()), 0.95 * 4000)

    def test_busy_or_unread_host_holds_every_raise(self):
        for stat in (Stat(0.80), None):
            c = self.kind_cluster()
            m, events = muscles(c, stat)
            self.assertEqual(m.convey(), {})
            self.assertFalse(any(a[0] == "patch" for a, _ in c.writes))
            self.assertTrue(any(e.get("convey") == "held" for e in events))

    def test_a_start_on_the_host_holds_the_raise_and_lowering_still_happens(self):
        c, stat = self.kind_cluster([pod("web-4", "w2", ready=False)]), Stat(0.30)
        m, events = muscles(c, stat)
        self.assertEqual(m.convey(), {})
        held = [e for e in events if e.get("convey") == "held"]
        self.assertTrue(held and held[0]["starting"] == ["host"])
        # a limit above the new share comes down even while a pod starts; the starting serving pod shares too:
        # (0.95 x 4000 - 300) / 4 = 875 -> 870
        for p in c.pods[:3]:
            p["spec"]["containers"][0]["resources"]["limits"]["cpu"] = "3700m"
        stat2 = Stat(0.30)
        m2, _ = muscles(c, stat2)
        out = m2.convey()
        self.assertEqual(out, {"default/web-1": 870, "default/web-2": 870, "default/web-3": 870})

    def test_separate_machines_keep_their_own_arithmetic(self):
        nodes = [node("a", kind=False), node("b", kind=False)]
        c = Cluster(nodes, [pod("web-1", "a"), pod("web-2", "b"), pod("web-3", "b", ready=False)])
        m, events = muscles(c)
        out = m.convey()
        self.assertEqual(out, {"default/web-1": 3800})            # machine a: its own 95%, nothing starting there
        held = [e for e in events if e.get("convey") == "held"]
        self.assertEqual(held[0]["machines"], ["b"])               # machine b: a start in progress holds it

    def test_starting_reads_the_pod_itself(self):
        self.assertTrue(starting(pod("x", "w1", phase="Pending")))
        self.assertTrue(starting(pod("x", "w1", ready=False)))
        self.assertFalse(starting(pod("x", "w1")))
        unplaced = pod("x", "w1", phase="Pending"); unplaced["spec"].pop("nodeName")
        self.assertFalse(starting(unplaced))
        leaving = pod("x", "w1", ready=False); leaving["metadata"]["deletionTimestamp"] = "2026-10-15T00:00:00Z"
        self.assertFalse(starting(leaving))


if __name__ == "__main__":
    unittest.main()
