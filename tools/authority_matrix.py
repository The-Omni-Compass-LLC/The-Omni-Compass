#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1]))
import json
from omnicompass.authority_contract import catalogue
print(json.dumps({'schema':'omnicompass.authority_catalogue.v1','contracts':catalogue()},indent=2,sort_keys=True))
