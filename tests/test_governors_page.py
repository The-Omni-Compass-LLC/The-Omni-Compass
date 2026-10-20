# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governors and orchestrators page (tools/governors_page.py): every one the founder named stands on it; a line reads
only from its own three-run table, every row counted by the one key, losses included; without a table it says where its
runs stand and writes no number."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.governors_page as G

FOUNDERS_LIST = ("Kueue", "Volcano", "Crane", "Open Cluster Management", "CruiseKube", "Gödel", "Armada", "Karmada",
                 "Kubernetes scheduler", "KAI", "Nephio", "KubeEdge", "KubeRay", "Koordinator")


class GovernorsPage(unittest.TestCase):
    def test_every_one_named_stands_on_the_page(self):
        text = G.render(runs={})
        for name in FOUNDERS_LIST:
            self.assertIn(name, text)
        self.assertIn("www.omni-compass.com", text.splitlines()[2])          # the notice under the title
        self.assertIn("www.omni-compass.com", text.rstrip().splitlines()[-1])  # and at the end

    def test_a_line_reads_only_from_its_table(self):
        table = {"runs": ["1", "2", "3"], "engines": ["omni-v12"] * 3, "rows": {
            "queue: job wait, submitted to its first pod running, mean (s)": {"reading": "GAIN in all three of our runs"},
            "queue: jobs unfinished at the window's end": {"reading": "LOSS in all three of our runs"},
            "machines in service, mean": {"reading": "power given in all three of our runs"},
            "energy (kWh)": {"reading": "EVEN, no difference beyond the noise (all three runs)"},
            "pods started": {"reading": "shown, not judged"}}}
        with tempfile.TemporaryDirectory() as t:
            live = Path(t) / "results" / "live"; live.mkdir(parents=True)
            (live / "V12_KAI.json").write_text(json.dumps(table))
            with mock.patch.object(G, "ROOT", Path(t)):
                text = G.render(runs={"koordinator": {"A": "9"}})
        kai = next(l for l in text.splitlines() if l.startswith("| KAI scheduler"))
        self.assertIn("1 GAIN, 1 LOSS, 1 power given, 1 EVEN, 0 where the runs disagree", kai)
        koord = next(l for l in text.splitlines() if l.startswith("| Koordinator"))
        self.assertIn("runs not yet finished", koord)
        self.assertIn("LOSS in all three of our runs", text)                  # every row counted and shown, losses included

    def test_no_number_before_the_runs(self):
        text = G.render(runs={})
        crane = next(l for l in text.splitlines() if l.startswith("| Crane"))
        self.assertTrue(crane.endswith("| not yet run |"))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
