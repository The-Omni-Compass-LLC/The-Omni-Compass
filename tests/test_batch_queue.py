# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The batch stream under a queueing system (BATCH_QUEUE: Kueue or Volcano; docs/BATCH_QUEUE_PREREGISTRATION.md): every
job's wait runs from its submission to its first pod running, the same measure whether the queueing system holds the job
(Kueue) or its pods (Volcano); a job not started or not done by the window's end counts the window's end, never less; and
the stream's job template renders for both systems."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.live_reps as LR

T0 = 1_760_000_000          # an epoch; times below are written as UTC stamps from it


def stamp(t):
    import datetime as dt
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def job(name, sub, done=None):
    st = {"completionTime": stamp(done)} if done is not None else {}
    return {"metadata": {"name": name, "creationTimestamp": stamp(sub)}, "status": st}


def pod(job_name, start):
    return {"metadata": {"labels": {"job-name": job_name}}, "status": {"startTime": stamp(start)}}


class JobStream(unittest.TestCase):
    def write(self, d, jobs, pods, end):
        (d / "window_end.txt").write_text(f"{end}\n")
        (d / "jobs.json").write_text(json.dumps({"items": jobs}))
        (d / "pods.json").write_text(json.dumps({"items": pods}))

    def test_wait_turnaround_and_unfinished(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            jobs = [job("a", T0, T0 + 100), job("b", T0 + 30, T0 + 200), job("c", T0 + 60)]
            pods = [pod("a", T0 + 10), pod("a", T0 + 50), pod("b", T0 + 90)]      # c never started
            self.write(d, jobs, pods, T0 + 300)
            g = LR.job_stream(d)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, mean (s)"], (10 + 60 + 240) / 3)
        self.assertAlmostEqual(g["queue: job wait, submitted to its first pod running, 95th percentile (s)"], 240)
        self.assertAlmostEqual(g["queue: job turnaround, submitted to done, mean (s)"], (100 + 170 + 240) / 3)
        self.assertEqual(g["queue: jobs unfinished at the window's end"], 1.0)

    def test_absent_without_the_stream(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(LR.job_stream(Path(t)), {})

    def test_every_queue_gauge_reads_lower(self):
        for k in LR.QUEUE:
            self.assertIn(k, LR.KEYS)
            self.assertNotIn(k, LR.NEUTRAL)


class Template(unittest.TestCase):
    def render(self, label, sched):
        text = (ROOT / "deploy" / "kind" / "batch-stream-job.yaml").read_text()
        for a, b in (("JOB_NAME", "omni-batch-001"), ("BATCH_COMPLETIONS", "10"), ("BATCH_PARALLELISM", "5"), ("BATCH_MB", "3000"),
                     ("QUEUE_LABEL", label), ("SCHEDULER_LINE", sched)):
            text = text.replace(a, b)
        return yaml.safe_load(text)

    def test_kueue_and_volcano(self):
        k = self.render("kueue.x-k8s.io/queue-name: omni-queue", "terminationGracePeriodSeconds: 30")
        self.assertEqual(k["metadata"]["labels"]["kueue.x-k8s.io/queue-name"], "omni-queue")
        self.assertNotIn("schedulerName", k["spec"]["template"]["spec"])
        v = self.render('omni-stream: "1"', "schedulerName: volcano")
        self.assertEqual(v["spec"]["template"]["spec"]["schedulerName"], "volcano")
        for j in (k, v):
            self.assertEqual((j["spec"]["completions"], j["spec"]["parallelism"]), (10, 5))
            self.assertEqual(j["spec"]["template"]["metadata"]["labels"]["app"], "omni-batch-stream")

    def test_the_script_parses(self):
        r = subprocess.run(["bash", "-n", str(ROOT / "scripts" / "kind_batch_queue.sh")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
