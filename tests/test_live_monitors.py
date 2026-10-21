# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every monitor of the live engine is registered, on the wall, knobbed and in the Grafana dashboard (the founder's order of 20
October: every monitor numbered, on the wall, with its own knobs and its open-source feed)."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
REG = ROOT / "docs" / "engine" / "monitors.json"


class LiveMonitors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        page = PAGE.read_text(encoding="utf-8")
        cls.body = re.sub(r'<script type="application/json" id="[^"]+">.*?</script>', "", page, flags=re.S)
        cls.canvases = [c for c in re.findall(r'<canvas id="([A-Za-z0-9_-]+)"', cls.body) if c != "wallCv"]
        cls.reg = json.loads(REG.read_text(encoding="utf-8"))

    def test_every_canvas_is_a_registered_monitor(self):
        ids = {m["id"] for m in self.reg["monitors"]}
        self.assertEqual(sorted(set(self.canvases) - ids), [], "a canvas on the page with no entry in docs/engine/monitors.json")
        self.assertEqual(sorted(ids - set(self.canvases)), [], "a registered monitor with no canvas on the page")

    def test_every_monitor_is_on_the_wall(self):
        wall = re.search(r"const WALL = \{.*?reg: \[(.*?)\]\]\};", self.body, re.S)
        self.assertIsNotNone(wall)
        on = set(re.findall(r'\["([A-Za-z0-9_-]+)",', wall.group(1)))
        self.assertEqual(sorted(set(self.canvases) - on), [], "a monitor missing from the wall")

    def test_every_knob_is_in_the_catalog(self):
        cat = set(self.reg["knobs"])
        for m in self.reg["monitors"]:
            self.assertTrue(set(m["knobs"]) <= cat, (m["id"], set(m["knobs"]) - cat))
            self.assertIn(m["layer"], self.reg["layers"], m["id"])

    def test_the_grafana_wall_has_a_panel_a_monitor(self):
        d = json.loads((ROOT / "deploy" / "grafana" / "omni-compass-wall.json").read_text(encoding="utf-8"))
        self.assertEqual(len(d["panels"]), len(self.reg["monitors"]))
        for p in d["panels"]:
            if p["type"] != "text":
                self.assertTrue(p["targets"] and all(t["expr"] for t in p["targets"]), p["title"])

    def test_the_kill_switch_words(self):
        self.assertIn('class="onword">ON</span>', self.body)
        self.assertIn('class="offword">OFF</span>', self.body)
        self.assertIn("Engine table of contents", self.body)


if __name__ == "__main__":
    unittest.main()
