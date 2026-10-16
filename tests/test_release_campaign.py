# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The approved campaign's dispatch boundaries and the v6 capacity regressions."""
import inspect
import json
from pathlib import Path
import tempfile
import unittest
import yaml
from scripts import dispatch_grid as grid
from tests import test_kind_capacity as capacity

ROOT = Path(__file__).resolve().parents[1]


class ReleaseCampaign(unittest.TestCase):
    def test_capacity_regressions(self):
        for name, fn in vars(capacity).items():
            if name.startswith('test_') and callable(fn):
                with self.subTest(test=name), tempfile.TemporaryDirectory() as tmp:
                    fn(**({'tmp_path': Path(tmp)} if inspect.signature(fn).parameters else {}))

    def test_queue_is_complete_and_excluded_providers_cannot_dispatch(self):
        queue = grid.rerun_queue()
        self.assertEqual(len(queue), 99)
        self.assertEqual({row[0] for row in queue}, set('ABC'))
        workflows = {row[2] for row in queue}
        self.assertTrue({'capacity.yml', 'pandapower.yml', 'swarm.yml', 'cpu-power.yml',
                         'realms-v5.yml', 'kind-cruisekube.yml', 'aks-metered-full.yml'} <= workflows)
        self.assertFalse({'gke-metered.yml', 'eks-metered.yml', 'cloud-organism.yml',
                          'gpu-bench.yml', 'lambda-gpu.yml'} & workflows)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'reruns.txt'
            p.write_text('unapproved|gke-metered.yml|\n')
            old = grid.RERUNS
            try:
                grid.RERUNS = p
                with self.assertRaises(ValueError):
                    grid.rerun_queue()
            finally:
                grid.RERUNS = old

    def test_started_work_is_not_queued_again(self):
        queue = grid.rerun_queue()
        counts = {}
        for _, _, wf, _ in queue:
            counts[wf] = counts.get(wf, 0) + 1
        self.assertEqual(grid.reruns_to_start(queue, counts), [])

    def test_six_stage_burst_is_the_workflow_and_queue_default(self):
        text = (ROOT / '.github/workflows/aks-metered-full.yml').read_text()
        w = yaml.safe_load(text)
        trigger = w.get('on', w.get(True))
        self.assertEqual(trigger['workflow_dispatch']['inputs']['load_steps']['default'], '1 4 1 6 1 9')
        azure = [r[3] for r in grid.rerun_queue() if r[2] == 'aks-metered-full.yml']
        self.assertTrue(all(r['load_steps'] == '1 4 1 6 1 9' for r in azure))

    def test_gpu_profiles_do_not_launch_or_claim_extra_physical_devices(self):
        d = json.loads((ROOT / 'scripts/gpu_campaign_profiles.json').read_text())
        self.assertFalse(d['launch'])
        self.assertEqual(d['profiles']['one-card']['physical_gpus'], 1)
        self.assertEqual(d['profiles']['eight-card']['physical_gpus'], 8)
        self.assertEqual(len(d['organisms']), 7)
        self.assertEqual(d['reported_run_prefixes'], [1, 10, 100])
        self.assertEqual(grid.SIZES, (1, 10, 100, 1000))
        self.assertEqual(grid.RUNS, 1000)
        for p in d['profiles'].values():
            self.assertEqual(p['environment']['HIL_SCALES'], '1,10,100')
            self.assertEqual(p['environment']['HIL_REPS_BY_SCALE'], '100,100,100')

    def test_gpu_prefixes_keep_missing_early_pairs_missing(self):
        from unittest.mock import patch
        from tools import run_hil
        with tempfile.TemporaryDirectory() as tmp:
            value = {part: {"primary": 0.0, "work": 0.0, "energy": 0.0, "viol_pp": 0.0, "p95": 0.0}
                     for part in ("sim", "card", "all")}
            with patch.object(run_hil, "contrast", return_value=value):
                run_hil.write_prefixes(tmp, {(1, "tower"): {1: {"native": {}, "omni": {}}}})
            rows = json.loads((Path(tmp) / "HIL_PREFIXES.json").read_text())
            self.assertTrue(all(r['paired_runs'] == 0 for r in rows if r['prefix'] == 1))
            self.assertTrue(all(r['paired_runs'] == 1 for r in rows if r['prefix'] in (10, 100)))
            self.assertFalse(any(r['complete'] for r in rows))

    def test_gpu_rejects_paid_oversize_before_hardware_access(self):
        from unittest.mock import patch
        from tools import run_hil
        with patch.object(run_hil, "limit", side_effect=AssertionError("hardware accessed")):
            for args in (["--scales", "1000"], ["--reps", "1000"]):
                with self.subTest(args=args), self.assertRaises(SystemExit) as cm:
                    run_hil.main(["--out", "/tmp/omni-paid-rejected", *args])
                self.assertEqual(cm.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
