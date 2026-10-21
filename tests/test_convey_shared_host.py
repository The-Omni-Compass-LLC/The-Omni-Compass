# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Conveyance on a shared host (Omni v7, omni_controller/muscles.py, convey): on kind, where every node is a container on
one machine, no limit is raised while the machine is at or over 75% busy or cannot be read; limits already given stay and
lowering goes on; a pod starting on the host holds nothing (the toy gate refused that hold: a LOSS on work and speed for
1% of start wait, docs/OMNI_V7.md); each node keeps its own arithmetic, on kind and on separate machines alike. Every case
reads the same conveyance code the live controller runs."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

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
        # coredns with no room of its own (its limit its request; kind's coredns carries no CPU limit at all), so these
        # cases read the v7 rule; a host where another workload has room is omni-v13's (tests/test_convey_handback.py)
        pods = [pod("web-1", "w1"), pod("web-2", "w2"), pod("web-3", "w3"),
                pod("dns", "w1", app="coredns", req="300m", limit="300m", ns="kube-system")] + list(extra)
        return Cluster(nodes, pods)

    def test_each_node_keeps_its_own_arithmetic_under_the_top(self):
        c, stat = self.kind_cluster(), Stat(0.40)
        m, events = muscles(c, stat)
        out = m.convey()
        # w1: (0.95 x 4000 - 300) / 1 = 3500; w2, w3: 0.95 x 4000 = 3800, one serving pod each (the v6 arithmetic)
        self.assertEqual(out, {"default/web-1": 3500, "default/web-2": 3800, "default/web-3": 3800})
        self.assertFalse(any(e.get("convey") == "held" for e in events))

    def test_busy_or_unread_host_holds_every_raise(self):
        for stat in (Stat(0.80), None):
            c = self.kind_cluster()
            m, events = muscles(c, stat)
            self.assertEqual(m.convey(), {})
            self.assertFalse(any(a[0] == "patch" for a, _ in c.writes))
            held = [e for e in events if e.get("convey") == "held"]
            self.assertTrue(held and held[0]["shared_host"] and sorted(held[0]["machines"]) == ["w1", "w2", "w3"])

    def test_a_busy_host_still_lowers(self):
        c, stat = self.kind_cluster([pod("web-4", "w2")]), Stat(0.80)
        for p in c.pods[:3]:
            p["spec"]["containers"][0]["resources"]["limits"]["cpu"] = "3800m"
        m, events = muscles(c, stat)
        out = m.convey()
        # w1: 3800 -> 3500 and w2 (two serving pods now): 3800 -> 1900 are lowerings, written though the host is past its
        # top; web-4's 500 -> 1900 is a raise, held
        self.assertEqual(out, {"default/web-1": 3500, "default/web-2": 1900})
        held = [e for e in events if e.get("convey") == "held"]
        self.assertTrue(held and held[0]["machines"] == ["w2"])

    def test_a_start_holds_nothing(self):
        c, stat = self.kind_cluster([pod("web-4", "w2", ready=False)]), Stat(0.30)
        m, events = muscles(c, stat)
        out = m.convey()
        # the starting pod on w2 is a serving pod like any other (v6's arithmetic): w2's 3800 shared by two
        self.assertEqual(out, {"default/web-1": 3500, "default/web-2": 1900, "default/web-4": 1900, "default/web-3": 3800})
        self.assertFalse(any(e.get("convey") == "held" for e in events))

    def test_an_unreadable_quota_holds_nothing(self):
        """The governor's role cannot list the namespace's quotas (every kind test, and any stack whose role withholds it):
        no budget is known, the raise proceeds as on omni-v6 and Kubernetes' own admission stays the authority; the audit
        says so once a pass. The first v7 trial (Goldilocks, run 38825214203) read this as a zero budget and never raised
        a limit (docs/OMNI_V7.md, section 1)."""
        import subprocess

        class Forbidden(Cluster):
            def get(self, *args):
                if args[1] == "resourcequota":
                    raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="resourcequotas is forbidden")
                return super().get(*args)

        base = self.kind_cluster()
        c, stat = Forbidden(base.nodes, base.pods), Stat(0.30)      # the stat stays alive: its file is the host's busy share
        m, events = muscles(c, stat)
        out = m.convey()
        self.assertEqual(out, {"default/web-1": 3500, "default/web-2": 3800, "default/web-3": 3800})
        said = [e for e in events if "quota" in e]
        self.assertEqual(len(said), 1)
        self.assertIn("no budget known", said[0]["quota"])
        self.assertIn("quota read unavailable", said[0]["reason"])

    def test_separate_machines_are_never_held(self):
        nodes = [node("a", kind=False), node("b", kind=False)]
        c = Cluster(nodes, [pod("web-1", "a"), pod("web-2", "b"), pod("web-3", "b", ready=False)])
        m, events = muscles(c, None)                   # no host sampler at all: not a shared host, nothing to read
        out = m.convey()
        self.assertEqual(out, {"default/web-1": 3800, "default/web-2": 1900, "default/web-3": 1900})
        self.assertFalse(any(e.get("convey") == "held" for e in events))


if __name__ == "__main__":
    unittest.main()


class ReadingOlderThanThePod(unittest.TestCase):
    """omni-v14: on a shared host beside another workload with room of its own, no limit is raised on a reading that began
    before that workload's newest pod ran (Pending, or not running at the previous reading): the reading does not hold its
    load. The next reading, which does, may raise; lowering and the hand-back are never held (docs/OMNI_V14.md)."""

    def cluster(self, batch):
        nodes = [node("w1"), node("w2"), node("w3")]
        pods = [pod("web-1", "w1"), pod("dns", "w1", app="coredns", req="300m", limit="300m", ns="kube-system")] + batch
        return Cluster(nodes, pods)

    def test_a_new_batch_pod_holds_the_raise_for_one_reading(self):
        b1 = pod("batch-1", "w2", app="batch", req="500m", limit="1000m")
        c, stat = self.cluster([b1]), Stat(0.40)
        m, events = muscles(c, stat)
        m.convey()                                     # the first reading with the batch pod running: it is new here
        self.assertFalse(any(a[0] == "patch" for a, _ in c.writes))
        self.assertTrue(any(e.get("reading_older_than_newest_pod") for e in events))
        stat.advance()
        out = m.convey()                               # the next reading covers the pod's run: the raise goes ahead
        self.assertEqual(out, {"default/web-1": 3500})
        c.pods.append(pod("batch-2", "w3", app="batch", req="500m", limit="1000m"))
        stat.advance()
        self.assertEqual(m.convey(), {})               # another pod of the workload starts: nothing more is raised on it

    def test_a_pending_pod_of_the_workload_holds_the_raise(self):
        b1 = pod("batch-1", "w2", app="batch", req="500m", limit="1000m", phase="Pending", ready=False)
        c, stat = self.cluster([b1]), Stat(0.40)
        m, events = muscles(c, stat)
        m.room_running = {("default", "web"): set()}   # a reading before this one saw no pod of the workload running
        self.assertEqual(m.convey(), {})
        self.assertTrue(any(e.get("reading_older_than_newest_pod") for e in events))

    def test_lowering_is_never_held(self):
        b1 = pod("batch-1", "w2", app="batch", req="500m", limit="1000m")
        c, stat = self.cluster([b1, pod("web-2", "w1")]), Stat(0.40)
        for p in c.pods:
            if p["metadata"]["name"] in ("web-1", "web-2"):
                p["spec"]["containers"][0]["resources"]["limits"]["cpu"] = "3500m"
        m, events = muscles(c, stat)
        # w1 carries two serving pods now: (0.95 x 4000 - 300) / 2 = 1750 each, a lowering written on the new pod's reading
        self.assertEqual(m.convey(), {"default/web-1": 1750, "default/web-2": 1750})

    def test_no_other_workload_with_room_keeps_omni_v13s_raise(self):
        c, stat = self.cluster([pod("batch-1", "w2", app="batch", req="500m", limit="500m")]), Stat(0.40)
        m, events = muscles(c, stat)
        self.assertEqual(m.convey(), {"default/web-1": 3500})
