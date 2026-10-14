# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""In the cloud the governor moves the machines alone (the founder's orders of 14 October, night: the same work for a bill
never bigger). It moves no pod autoscaler, conveys no processor and caps no power, so the pods are exactly native's and
Azure's autoscaler alone makes machines; the governor only parks machines that exist and wakes them again."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tests.test_compass_controller import cluster, probe, controller, target_now  # noqa: E402


class MachinesOnly(unittest.TestCase):
    def test_a_breach_moves_no_pod_target_when_the_governor_senses_no_service(self):
        with tempfile.TemporaryDirectory() as t:
            st = cluster(t)
            lat = probe(t, 600.0)                       # past the wall: elsewhere the pod target would fail up to 30
            c, marker = controller(t, lat, "--sensed", "none/none")
            for _ in range(3):
                c.step()
            self.assertEqual(target_now(st), 50)        # the operator's own target, untouched
            writes = (Path(t) / "writes.log").read_text() if (Path(t) / "writes.log").exists() else ""
            self.assertNotIn('"hpa"', writes)           # no HPA patched or annotated at all

    def test_the_cloud_sets_the_governor_to_machines_only(self):
        y = (ROOT / ".github" / "workflows" / "aks-metered.yml").read_text()
        self.assertRegex(y, r"OMNI_MACHINES_ONLY: '1'")
        s = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertIn('if [ -n "${OMNI_MACHINES_ONLY:-}" ]; then OMNI_SENSED="none/none"; OMNI_POWER_CMD=""; CAP_ARGS=""; fi', s)
        self.assertIn('--sensed "$OMNI_SENSED"', s)
        self.assertIn('${OMNI_POWER_CMD:+--power-cmd "$OMNI_POWER_CMD"}', s)
        # elsewhere nothing changes: the sensed service, the power command and conveyance as before
        self.assertIn('OMNI_SENSED="default/php-apache"; OMNI_POWER_CMD="bash scripts/kind_power.sh"', s)
        self.assertIn('CAP_ARGS="--cap-deployments default/php-apache"', s)

    def test_the_machine_lever_only_parks_and_wakes_machines_that_exist(self):
        s = (ROOT / "scripts" / "kind_nodepool.sh").read_text()
        self.assertIn("(( want > total )) && want=$total", s)   # never asks for a machine the cluster does not have
        self.assertNotRegex(s, r"az aks (nodepool )?scale")      # it never tells Azure to make one


if __name__ == "__main__":
    unittest.main()
