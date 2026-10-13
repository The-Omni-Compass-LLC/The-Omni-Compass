# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The CruiseKube test's wiring (docs/CRUISEKUBE_PREREGISTRATION.md): every download pinned, CruiseKube's usage reports off,
the set beside KEDA's HTTP add-on alone, the CPU limit left to CruiseKube, and a run without an applied change invalid."""
import re
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ADDON = ROOT / "scripts/kind_addons_cruisekube.sh"
BENCH = ROOT / "scripts/kind_bench.sh"


class Wiring(unittest.TestCase):
    def test_scripts_parse(self):
        for f in (ADDON, BENCH):
            subprocess.run(["bash", "-n", str(f)], check=True)

    def test_every_download_is_pinned(self):
        s = ADDON.read_text()
        fetched = re.findall(r'^\s*fetch "[^"]+" "[^"]+" "\$(\w+)"', s, re.M)
        self.assertEqual(len(fetched), 5)                          # kube-state-metrics' five standard files
        for var in fetched:
            self.assertRegex(s, rf'(?m)^{var}="[0-9a-f]{{64}}"$')
        # the chart: a counted run needs its SHA-256; only a shakedown run may record one instead
        self.assertIn('CK_VERSION="${CK_VERSION:-0.3.4}"', s)
        self.assertIn('elif [ "${CRUISEKUBE_SHAKEDOWN:-}" != 1 ]; then', s)
        self.assertIn('[ "$got" = "$CK_CHART_SHA256" ] || {', s)

    def test_images_pinned_to_a_release(self):
        docs = [d for d in yaml.safe_load_all((ROOT / "deploy/kind/cruisekube-metrics.yaml").read_text()) if d]
        images = [c["image"] for d in docs if d.get("kind") in ("Deployment", "DaemonSet")
                  for c in d["spec"]["template"]["spec"]["containers"]]
        self.assertEqual(sorted(images), ["quay.io/prometheus/node-exporter:v1.12.0", "quay.io/prometheus/prometheus:v3.10.0"])
        prom = next(d for d in docs if d.get("kind") == "Deployment" and d["metadata"]["name"] == "prometheus")
        self.assertEqual(prom["spec"]["template"]["spec"]["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})

    def test_values_as_shipped_but_for_the_run(self):
        v = yaml.safe_load((ROOT / "deploy/kind/cruisekube-values.yaml").read_text())
        c = v["cruisekubeController"]
        self.assertIs(c["usageTelemetry"]["enabled"], False)       # no usage reports to its maker
        self.assertIs(c["admin"]["enabled"], False)
        self.assertIs(c["serviceMonitor"]["enabled"], False)
        self.assertIs(v["cruisekubeWebhook"]["serviceMonitor"]["enabled"], False)
        self.assertIs(v["cruisekubeFrontend"]["enabled"], False)
        self.assertEqual(c["env"], {"CRUISEKUBE_DEPENDENCIES_INCLUSTER_PROMETHEUSURL": "http://prometheus.cruisekube-metrics.svc:9090"})
        self.assertEqual(v["postgresql"]["primary"]["nodeSelector"], {"node-role.kubernetes.io/control-plane": ""})

    def test_beside_keda_http_alone_and_the_limit_left_to_cruisekube(self):
        s = BENCH.read_text()
        self.assertIn('[ -z "$CRUISEKUBE" ] || { [ "$ADDONS" = keda ] && [ "${ADDONS_PROFILE:-both}" = http ]; }', s)
        self.assertIn('CAP_ARGS="--cap-deployments default/php-apache"; [ -z "$CRUISEKUBE" ] || CAP_ARGS=""', s)
        self.assertNotIn("--cap-deployments default/php-apache --", s.replace('CAP_ARGS="--cap-deployments default/php-apache"', ""))
        self.assertIn("{.spec.template.spec.containers[0].resources.limits.cpu}", s)
        for phase in ("install", "learn", "end"):
            self.assertIn(f"PHASE={phase} ", s[s.index('if [ -n "$CRUISEKUBE" ]'):])

    def test_no_change_applied_is_invalid(self):
        s = ADDON.read_text()
        self.assertIn('[ -n "$applied" ] || { echo "INVALID RUN: CruiseKube made no change', s)
        self.assertIn('test("RECOMMENDATION_APPLIED|WEBHOOK_MUTATION")', s)
        self.assertIn('LEARN="${CRUISEKUBE_LEARN:-4500}"', s)          # longer than CruiseKube's hour
        self.assertIn(">> \"$OUT_DIR/addons.txt\"", s)                  # KEDA's lines kept

    def test_workflow(self):
        w = yaml.safe_load((ROOT / ".github/workflows/kind-cruisekube.yml").read_text())
        step = next(s for s in w["jobs"]["run"]["steps"] if s.get("run") == "bash scripts/kind_paired.sh")
        env = step["env"]
        self.assertEqual((env["ADDONS"], env["ADDONS_PROFILE"], env["CRUISEKUBE"], env["ARMS"]),
                         ("keda", "http", "1", "native compass"))
        commit = next(s for s in w["jobs"]["aggregate"]["steps"] if "committed back" in s.get("name", ""))
        self.assertIn("github.event.inputs.shakedown != 'yes'", commit["if"])   # a shakedown run is never counted


if __name__ == "__main__":
    unittest.main()
