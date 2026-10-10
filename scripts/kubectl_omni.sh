#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
# Run kubectl as the Omni-Compass service account (deploy/kind/rbac-omni.yaml), never as cluster admin.
set -euo pipefail
exec kubectl --as=system:serviceaccount:omni-compass:omni-compass "$@"
