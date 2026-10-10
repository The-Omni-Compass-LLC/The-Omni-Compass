# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
"""Referee harness: metrics-server + HPA + Cluster Autoscaler / Karpenter-lite + Omni-Compass.

This is an algorithm replica of documented Kubernetes control-plane behaviour.
It is not kube-controller-manager, cluster-autoscaler, or Karpenter source.
"""
from .config import HarnessConfig
from .benchmark import ARMS, run, simulate
