# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Cruise and the emergency brake (rules 7 and 8), through the live controller against the fake kubectl: work waiting
for a place two decisions in a row puts every machine in service, and they stay until the line has been empty two
decisions; with nothing waiting and the sensed service's demand at zero the machines go straight to the floor (two) in
one move, never below it."""
import json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.controller import Controller, parser
FAKE = str(ROOT / "tests" / "fake_cluster" / "kubectl")


def cluster(tmp, pending, util, replicas, used="200m"):
    ready = [{"type": "Ready", "status": "True"}]
    nodes = [{"metadata": {"name": f"w{i}"}, "spec": {}, "status": {"allocatable": {"cpu": "4"}, "conditions": ready}} for i in range(6)]
    pod = lambda where, phase="Running": {"metadata": {"name": f"p-{where}", "namespace": "default", "labels": {"run": "php-apache"},
                                                       "ownerReferences": [{"kind": "ReplicaSet"}]},
                                          "status": {"phase": phase}, "spec": {"nodeName": where, "containers": [{"resources": {"requests": {"cpu": "200m"}}}]}}
    pods = [pod(f"w{i}") for i in range(6)] + [{"metadata": {"name": f"wait-{j}", "namespace": "default"}, "status": {"phase": "Pending"},
                                                 "spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}}}]}} for j in range(pending)]
    cpu = {"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": 50}}}
    hpas = [{"metadata": {"name": "php-apache", "namespace": "default"},
             "spec": {"minReplicas": 1, "maxReplicas": 10, "scaleTargetRef": {"kind": "Deployment", "name": "php-apache"}, "metrics": [cpu]},
             "status": {"currentReplicas": replicas, "desiredReplicas": replicas,
                        "currentMetrics": [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": util}}}]}}]
    st = Path(tmp) / "state.json"
    st.write_text(json.dumps({"nodes": nodes, "pods": pods, "hpas": hpas, "used_per_node": used, "deployments": [], "configmaps": [], "jobs": []}))
    os.environ["FAKE_KUBE_STATE"] = str(st); os.environ["FAKE_KUBE_LOG"] = str(Path(tmp) / "writes.log")


def main():
    t = tempfile.mkdtemp(); sized = Path(t) / "sized"
    a = parser().parse_args(["--kubectl", FAKE, "--mode", "nodepool", "--interval", "0", "--min-nodes", "2", "--max-nodes", "6",
                             "--audit", str(Path(t) / "audit.jsonl"), "--kill-file", str(Path(t) / "kill"),
                             "--sensed", "default/php-apache", "--node-scale-cmd", f"sh -c 'echo {{n}} >> {sized}'"])
    c = Controller(a)
    sizes = lambda: [int(x) for x in sized.read_text().split()] if sized.exists() else []
    events = lambda key: [json.loads(l)[key] for l in (Path(t) / "audit.jsonl").read_text().splitlines() if key in json.loads(l)]

    # cruise: work waiting for a place, two decisions in a row
    cluster(t, pending=4, util=95, replicas=6, used="3500m")
    c.step(); assert "on" not in events("cruise"), "one decision with work waiting is not yet cruise"
    c.step(); assert events("cruise")[-1:] == ["on"], events("cruise")
    assert c.cruise
    # the line empties: cruise holds one decision more, then ends
    cluster(t, pending=0, util=60, replicas=6, used="2500m")
    c.step(); assert c.cruise, "cruise ends only after the line has been empty two decisions"
    c.step(); assert not c.cruise and events("cruise")[-1] == "off", events("cruise")

    # the emergency brake: nothing waiting, the service's demand at zero: straight to the floor, never below it
    cluster(t, pending=0, util=0, replicas=1, used="50m")
    for _ in range(40):
        c.step()
        if events("emergency_brake"):
            break
    eb = events("emergency_brake")
    assert eb, "the emergency brake never engaged at zero demand"
    assert eb[0]["to"] == 2 and eb[0]["from"] > 2, eb
    assert all(n >= 2 for n in sizes()), sizes()
    print(f"cruise: on after two decisions with work waiting, off after two with the line empty; emergency brake: "
          f"{eb[0]['from']} -> {eb[0]['to']} machines in one move at zero demand, never below the floor")
    print("PASS test_cruise_brake")


if __name__ == "__main__":
    main()
