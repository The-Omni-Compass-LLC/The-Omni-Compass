# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Quota accounting and cleanup must not let sequential Azure arms overlap."""
import unittest
from unittest.mock import patch
from scripts import azure_capacity as cap


def usage(**values):
    return [{'name': {'value': k}, 'currentValue': v[0], 'limit': v[1]} for k, v in values.items()]


class AzureCapacity(unittest.TestCase):
    def test_shared_family_pools_and_system_are_added_once(self):
        specs = {'system': ('family', 2), 'work-a': ('family', 2), 'work-b': ('family', 4)}
        self.assertEqual(cap.demand('system', 'work-a:2,work-b:2', specs), {'family': 14})

    def test_standalone_vm_counts_one_machine_without_worker_pools(self):
        self.assertEqual(cap.demand('vm', '', {'vm': ('f', 8)}), {'f': 8})

    def test_pool_with_different_size_but_same_family_includes_system(self):
        self.assertEqual(cap.demand('system', 'workers:4', {'system': ('f', 2), 'workers': ('f', 2)}), {'f': 10})

    def test_occupied_family_waits_and_regional_limit_also_binds(self):
        self.assertFalse(cap.has_capacity({'f': 10}, usage(f=(8, 10), cores=(8, 200))))
        self.assertFalse(cap.has_capacity({'f': 10}, usage(f=(0, 10), cores=(195, 200))))
        self.assertTrue(cap.has_capacity({'f': 10}, usage(f=(0, 10), cores=(0, 200))))

    def test_unknown_or_permanently_insufficient_quota_is_not_treated_as_free(self):
        for rows in (usage(cores=(0, 200)), usage(f=(0, 8), cores=(0, 200))):
            with self.subTest(rows=rows), self.assertRaises(RuntimeError):
                cap.has_capacity({'f': 10}, rows)

    def test_capacity_wait_retries_without_allocating(self):
        sku = [{'name': 'worker', 'family': 'f', 'capabilities': [{'name': 'vCPUs', 'value': '2'}]}]
        with patch.object(cap, 'az', side_effect=[sku, usage(f=(8, 10), cores=(8, 200)),
                                                usage(f=(0, 10), cores=(0, 200))]) as az, patch.object(cap.time, 'sleep') as sleep:
            cap.wait_capacity('eastus', 'worker', 'worker:4')
            sleep.assert_called_once()
            self.assertEqual([c.args[:2] for c in az.call_args_list],
                             [('vm', 'list-skus'), ('vm', 'list-usage'), ('vm', 'list-usage')])

    def test_cleanup_timeout_is_reported_as_a_failure(self):
        with patch.object(cap, 'az', side_effect=[True, None, True]), patch.object(cap.time, 'monotonic', side_effect=[0, 2]):
            with self.assertRaises(RuntimeError):
                cap.cleanup('omni-compass-full-123-1', timeout=1)

    def test_paid_suites_share_a_region_queue_and_wait_for_cleanup(self):
        from pathlib import Path
        import yaml
        root = Path(__file__).resolve().parents[1]
        groups = []
        for name in ('aks-metered.yml', 'aks-metered-full.yml', 'big-organism.yml'):
            text = (root / '.github/workflows' / name).read_text()
            workflow = yaml.safe_load(text)
            groups.append(workflow['concurrency']['group'])
            self.assertFalse(workflow['concurrency']['cancel-in-progress'])
            self.assertNotIn('az group delete -n', text)
            self.assertIn('azure_capacity.py cleanup', text)
        self.assertEqual(len(set(groups)), 1)

    def test_cleanup_waits_for_resource_disappearance(self):
        with patch.object(cap, 'az', side_effect=[True, None, True, False]) as az, patch.object(cap.time, 'sleep') as sleep:
            cap.cleanup('omni-compass-full-123-1')
            self.assertEqual(az.call_count, 4)
            sleep.assert_called_once()

    def test_cleanup_missing_group_is_a_noop_and_failures_are_not_swallowed(self):
        with patch.object(cap, 'az', return_value=False) as az:
            cap.cleanup('omni-big-123-0')
            az.assert_called_once()
        with patch.object(cap, 'az', side_effect=RuntimeError('permission denied')), self.assertRaises(RuntimeError):
            cap.cleanup('omni-big-123-0')
        with self.assertRaises(ValueError):
            cap.cleanup('unrelated-production-group')

    def test_cluster_cleanup_deletes_only_the_named_existing_cluster(self):
        with patch.object(cap, 'az', side_effect=[[{'name': 'omni-native-1'}], None]) as az:
            cap.cleanup_cluster('omni-compass-full-123-1', 'omni-native-1')
            self.assertEqual(az.call_count, 2)
            self.assertNotIn('--no-wait', az.call_args.args)
        with patch.object(cap, 'az', return_value=[]) as az:
            cap.cleanup_cluster('omni-compass-full-123-1', 'absent')
            az.assert_called_once()


if __name__ == '__main__':
    unittest.main()
