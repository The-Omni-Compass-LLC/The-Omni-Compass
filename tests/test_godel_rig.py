# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Gödel scheduler on the batch rig (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 8): the pinned commit, node image and
metrics-server named the same in the scripts, the workflow and the preregistration; the image built from that commit and
checked before it is loaded; the stream's pods sent to Gödel with its guide's three annotations while every other system's
job file stays as it was; and the bench takes Gödel, its namespace and its metrics-server line."""
import re
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
QUEUE = (ROOT / "scripts" / "kind_batch_queue.sh").read_text()
BENCH = (ROOT / "scripts" / "kind_bench.sh").read_text()
BUILD = (ROOT / "scripts" / "kind_godel_build.sh").read_text()
PREREG = (ROOT / "docs" / "BATCH_QUEUE_PREREGISTRATION.md").read_text()
WF = yaml.safe_load((ROOT / ".github" / "workflows" / "kind-godel.yml").read_text())
COMMIT = re.search(r'GODEL_COMMIT="\$\{GODEL_COMMIT:-([0-9a-f]{40})\}"', QUEUE).group(1)


def job(queue_vars: str) -> dict:
    """The stream's job file as the submit phase writes it, for the given queue variables (the script's own sed line)."""
    sed = QUEUE[QUEUE.index('    sed -e "s/JOB_NAME/omni-batch-'):QUEUE.index('deploy/kind/batch-stream-job.yaml > "$OUT_DIR/job.yaml"')]
    script = (f'COMPLETIONS=10 PARALLELISM=5 MB=3000 i=1; label=""; podlabel=""; sched=""; podann=""; {queue_vars}\n'
              + sed.replace("\\\n", " ") + " deploy/kind/batch-stream-job.yaml")
    out = subprocess.run(["bash", "-c", script], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return yaml.safe_load(out)


class GodelRig(unittest.TestCase):
    def test_the_pins_are_the_preregistered_ones(self):
        self.assertIn(COMMIT, PREREG)
        env = next(s for s in WF["jobs"]["run"]["steps"] if "kind_paired.sh" in str(s.get("run", "")))["env"]
        self.assertEqual(env["BATCH_QUEUE"], "godel")
        for k in ("KIND_NODE_IMAGE", "METRICS_SERVER_SHA256"):
            self.assertIn(env[k].split("@")[-1].replace("sha256:", ""), PREREG)
        self.assertTrue(env["KIND_NODE_IMAGE"].startswith("kindest/node:v1.24."))
        self.assertEqual(env["METRICS_SERVER_VERSION"], "v0.5.2")
        kind = next(s for s in WF["jobs"]["run"]["steps"] if str(s.get("uses", "")).startswith("helm/kind-action"))
        self.assertEqual((kind["with"]["version"], kind["with"]["kubectl_version"]), ("v0.22.0", "v1.24.17"))

    def test_the_image_is_built_from_the_pinned_commit_and_checked_before_it_is_loaded(self):
        steps = [str(s.get("run", "")) for s in WF["jobs"]["run"]["steps"]]
        self.assertLess(steps.index("bash scripts/kind_godel_build.sh"), next(i for i, s in enumerate(steps) if "kind_paired.sh" in s))
        got = subprocess.run(["bash", "-c", BUILD[BUILD.index('GODEL_COMMIT="'):BUILD.index("\n", BUILD.index('GODEL_COMMIT="'))]
                              + '\necho "$GODEL_COMMIT"'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        self.assertEqual(got, COMMIT)                                           # one pin, read from the queue script
        self.assertIn('docker build -q -t godel-local:latest -f docker/godel-local.Dockerfile .', BUILD)
        self.assertIn('IMAGE_ID', BUILD)
        install = QUEUE[QUEUE.index('elif [ "$Q" = godel ]; then'):]
        self.assertLess(install.index('rev-parse HEAD'), install.index('kind load docker-image godel-local:latest'))
        self.assertLess(install.index('IMAGE_ID'), install.index('kind load docker-image godel-local:latest'))
        self.assertIn('kubectl apply --server-side -k "$GODEL_SRC/manifests/base"', install)

    def test_the_stream_goes_to_godel_with_its_annotations_and_no_other_job_changes(self):
        g = job('sched="schedulerName: godel-scheduler"; podann=", annotations: {godel.bytedance.com/pod-state: pending, '
                'godel.bytedance.com/pod-resource-type: guaranteed, godel.bytedance.com/pod-launcher: kubelet}"')
        pod = g["spec"]["template"]
        self.assertEqual(pod["spec"]["schedulerName"], "godel-scheduler")
        self.assertEqual(pod["metadata"]["annotations"], {"godel.bytedance.com/pod-state": "pending",
                                                          "godel.bytedance.com/pod-resource-type": "guaranteed",
                                                          "godel.bytedance.com/pod-launcher": "kubelet"})
        self.assertIn('[ "$Q" = godel ] && { sched="schedulerName: godel-scheduler"', QUEUE)
        k = job('label="kai.scheduler/queue: default-queue"; podlabel="$label"; sched="schedulerName: kai-scheduler"')
        self.assertNotIn("annotations", k["spec"]["template"]["metadata"])     # every other system's pods as before
        self.assertEqual(k["spec"]["template"]["metadata"]["labels"]["kai.scheduler/queue"], "default-queue")

    def test_the_bench_takes_godel_its_namespace_and_its_metrics_server(self):
        self.assertIn("|kuberay|godel|vanilla|binpack)", BENCH)
        self.assertIn('[ "$BATCH_QUEUE" = godel ] && qns=godel-system', BENCH)
        self.assertIn("v0.5.*) ms_floor=8 ;;", BENCH)
        self.assertIn("godel) NS=godel-system ;;", QUEUE)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
