# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Tests for the kind shared-host replica ceiling."""
from omni_controller.capacity import HostCpuSampler, kind_replica_ceiling


def test_host_saturation_blocks_scale_out():
    assert kind_replica_ceiling(4000, 0, 100, 40, 0.90) == 40


def test_measured_headroom_caps_scale_out_at_reserve():
    # 4 cores, 70% busy and 10% reserved leaves 800m: eight 100m replicas.
    assert kind_replica_ceiling(4000, 0, 100, 40, 0.70) == 48


def test_request_capacity_remains_the_outer_ceiling():
    assert kind_replica_ceiling(4000, 2500, 100, 5, 0.20) == 14


def test_missing_or_invalid_host_sample_fails_closed():
    assert kind_replica_ceiling(4000, 0, 100, 40, None) == 40
    assert kind_replica_ceiling(4000, 0, 100, 40, 1.1) == 40


def test_sampler_uses_busy_delta_and_idle_plus_iowait(tmp_path):
    stat = tmp_path / "stat"
    stat.write_text("cpu 100 0 100 700 100 0 0 0 0 0\n")
    sampler = HostCpuSampler(stat)
    assert sampler.sample() is None
    stat.write_text("cpu 120 0 120 740 120 0 0 0 0 0\n")
    assert sampler.sample() == 0.6


def test_sampler_resets_after_unreadable_sample(tmp_path):
    stat = tmp_path / "stat"
    sampler = HostCpuSampler(stat)
    assert sampler.sample() is None
    stat.write_text("cpu 100 0 100 700 100 0 0 0 0 0\n")
    assert sampler.sample() is None
