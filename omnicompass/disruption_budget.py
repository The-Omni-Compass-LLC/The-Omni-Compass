# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Karpenter-shaped voluntary node-down budget.

Not Karpenter. Caps how many nodes Omni may remove in a window.
allowed ≈ ceil(n0 * pct/100), then optional absolute ceiling.
"""
from __future__ import annotations
import math


def allowed_downs(n0: int, pct: float, abs_cap: int = 0) -> int:
    n0 = max(0, int(n0))
    raw = int(math.ceil(n0 * max(0.0, float(pct)) / 100.0)) if pct else n0
    if abs_cap and abs_cap > 0:
        raw = min(raw, int(abs_cap))
    return max(0, raw)


def apply_node_delta(delta: int, used: int, allow: int) -> tuple[int, int, bool]:
    """Return (delta, used, blocked). Only clips negative (voluntary shrink)."""
    if delta >= 0:
        return int(delta), int(used), False
    room = max(0, int(allow) - int(used))
    if room <= 0:
        return 0, int(used), True
    take = max(delta, -room)  # delta is negative
    return int(take), int(used) - int(take), False
