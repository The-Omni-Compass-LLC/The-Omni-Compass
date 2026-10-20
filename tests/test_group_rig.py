# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The group of clusters (docs/GROUP_PREREGISTRATION.md): the members' records merge into one arm the table tool reads (the
window from the stream's start to the first member's end, every job once with its submission and its last part done, the
machines summed at each moment, an unfinished part leaving its job unfinished); the stream goes to the orchestrator or to
the members in turn; Karmada's release is pinned; a member's bench opens its window with the others' and sends no stream."""
import csv
import json
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
import sys; sys.path.insert(0, str(ROOT))
import tools.merge_group as MG
import tools.live_reps as LR

T0 = 1_800_000_000


def iso(t):
    return MG.iso(t)


def member(d: Path, name: str, jobs, pods, nodes, shift=0):
    m = d / name; m.mkdir()
    (m / "window_start.txt").write_text(f"{T0 - 5 + shift}\n"); (m / "window_end.txt").write_text(f"{T0 + 600 + shift}\n")
    (m / "preflight.txt").write_text("batch: 24 jobs of 10 pods, 5 at a time, one every 30 s, 3000 MB hashed each, through group\n")
    (m / "jobs.json").write_text(json.dumps({"items": jobs}))
    (m / "pods.json").write_text(json.dumps({"items": pods}))
    with open(m / "capture.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "elapsed_seconds", "nodes_ready", "nodes_total", "alloc_cpu_m", "req_cpu_m", "used_cpu_m",
                    "pods_pending", "hpa_count", "hpa_current_replicas", "hpa_desired_replicas", "power_w"])
        for i, n in enumerate(nodes):
            w.writerow([iso(T0 + 15 * i + shift), 15 * i, n, 6, 24000, 1000, 500, 0, 1, 1, 1, 100.0 * n])
    (m / "latency.csv").write_text("elapsed_seconds,latency_ms,ok\n5,10,1\n10,12,1\n")
    return m


def job(name, created, done=None):
    j = {"metadata": {"name": name, "creationTimestamp": iso(created)}, "spec": {"completions": 10}, "status": {}}
    if done:
        j["status"]["completionTime"] = iso(done)
    return j


def pod(job_name, start):
    return {"metadata": {"name": f"{job_name}-x", "labels": {"job-name": job_name}}, "status": {"startTime": iso(start)}}


class GroupMerge(unittest.TestCase):
    def test_the_group_alone_reads_each_job_from_its_member(self):
        d = Path(tempfile.mkdtemp()) / "bench-nativebare-1"; d.mkdir(parents=True)
        (d / "stream_start.txt").write_text(f"{T0}\n"); (d / "batch_done.txt").write_text(f"{T0 + 300}\n")
        member(d, "m1", [job("omni-batch-001", T0 + 1, T0 + 100)], [pod("omni-batch-001", T0 + 4)], [6, 6, 5])
        member(d, "m2", [job("omni-batch-002", T0 + 31, None)], [pod("omni-batch-002", T0 + 40)], [6, 5, 5], shift=3)
        out = MG.main(d, 2, "none")
        self.assertIn("2 jobs (1 done)", out)
        with open(d / "capture.csv") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual([r["nodes_ready"] for r in rows], ["12", "11", "10"])            # summed at each moment
        self.assertEqual(rows[0]["power_w"], "1200.0")
        self.assertEqual(float((d / "window_start.txt").read_text()), T0)                   # the stream's start
        self.assertEqual(float((d / "window_end.txt").read_text()), T0 + 600)               # the first member's end
        g = LR.job_stream(d)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, mean (s)"], (3 + 9) / 2)
        self.assertEqual(g["queue: jobs unfinished at the window's end"], 1.0)
        self.assertIn("batch:", (d / "preflight.txt").read_text())

    def test_through_the_orchestrator_a_job_is_sent_when_it_reached_it_and_done_when_its_last_part_is(self):
        d = Path(tempfile.mkdtemp()) / "bench-native-1"; d.mkdir(parents=True)
        (d / "stream_start.txt").write_text(f"{T0}\n")
        (d / "orch_jobs.json").write_text(json.dumps({"items": [job("omni-batch-001", T0), job("omni-batch-002", T0 + 30)]}))
        member(d, "m1", [job("omni-batch-001", T0 + 2, T0 + 90), job("omni-batch-002", T0 + 32, T0 + 200)],
               [pod("omni-batch-001", T0 + 5), pod("omni-batch-002", T0 + 35)], [6, 6])
        member(d, "m2", [job("omni-batch-002", T0 + 32, None)], [pod("omni-batch-002", T0 + 33)], [6, 6])   # a part not done
        MG.main(d, 2, "karmada")
        jobs = {j["metadata"]["name"]: j for j in json.loads((d / "jobs.json").read_text())["items"]}
        self.assertEqual(jobs["omni-batch-001"]["metadata"]["creationTimestamp"], iso(T0))     # sent to the orchestrator
        self.assertEqual(jobs["omni-batch-001"]["status"]["completionTime"], iso(T0 + 90))
        self.assertNotIn("completionTime", jobs["omni-batch-002"]["status"])                  # its part on m2 never ended
        g = LR.job_stream(d)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, mean (s)"], (5 + 3) / 2)

    def test_a_member_without_a_valid_record_fails_the_arm(self):
        d = Path(tempfile.mkdtemp()) / "bench-native-1"; d.mkdir(parents=True)
        member(d, "m1", [], [], [6])
        with self.assertRaises(SystemExit):
            MG.main(d, 2, "none")


class GroupWiring(unittest.TestCase):
    ORCH = (ROOT / "scripts" / "kind_group_orch.sh").read_text()
    BENCH = (ROOT / "scripts" / "kind_bench.sh").read_text()
    QUEUE = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()

    def test_the_stream_goes_to_the_orchestrator_or_to_the_members_in_turn(self):
        self.assertIn('to="$D/kubeconfig-m$(( (i - 1) % N + 1 ))"', self.ORCH)
        self.assertIn('else to="$KC"; where="$ORCH"; fi', self.ORCH)
        self.assertIn('[ "$Q" = group ] && exit 0', self.QUEUE)                              # a member sends nothing

    def test_karmadas_release_is_pinned_and_its_credentials_stay_out_of_the_runs_files(self):
        self.assertRegex(self.ORCH, r'KARMADACTL_SHA256="\$\{KARMADACTL_SHA256:-[0-9a-f]{64}\}"')
        self.assertRegex(self.ORCH, r'KARMADA_CRDS_SHA256="\$\{KARMADA_CRDS_SHA256:-[0-9a-f]{64}\}"')
        self.assertIn('W="${RUNNER_TEMP:-/tmp}/omni-group-', self.ORCH)
        self.assertIn('rm -rf "$W"', self.ORCH)
        self.assertIn('rm -f "$D"/kubeconfig-*', (ROOT / "scripts" / "kind_group.sh").read_text())
        pol = yaml.safe_load((ROOT / "deploy" / "kind" / "karmada-propagation.yaml").read_text().replace("MEMBER_CLUSTERS", "[a, b]"))
        self.assertEqual(pol["spec"]["placement"]["replicaScheduling"],
                         {"replicaSchedulingType": "Divided", "replicaDivisionPreference": "Aggregated"})

    def test_a_member_opens_its_window_with_the_others(self):
        i = self.BENCH.index('if [ -n "${GROUP_BARRIER:-}" ]; then')
        self.assertLess(self.BENCH.index('sleep "$WARMUP"'), i)
        self.assertLess(i, self.BENCH.index('date -u +%s > "$OUT_DIR/window_start.txt"'))
        self.assertIn("|godel|group|vanilla|binpack)", self.BENCH)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
