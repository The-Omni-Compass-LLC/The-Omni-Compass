# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Where a unit goes: the room rule.

A machine's room is its processor less the requests of the units on it; a unit goes only where its request fits, so no
machine is ever asked for more than it has. Only machines awake take new units (one booting, draining or parked takes
none). Two ways to choose among the machines that fit:

  pack    Omni's: the machine left fullest by the unit (the best fit), so whole machines empty out and can be parked;
          but a service of two or more units is never left on one machine alone, so one machine lost never takes the
          whole service with it
  spread  the yardstick's, as Kubernetes' own scheduler scores by default: the machine with the fewest units of the
          service, then the one with the most room left

`place` returns the machine's name, or None when no machine awake has the room (the brain then wakes one)."""
from __future__ import annotations


BUSY_TOP = 0.75     # the engine's own rule (omni_controller/capacity.py, omni-v7): no unit onto a machine this busy


def room(machine: dict, units: list[dict], rule: str = "requests") -> float:
    """The room on a machine: its processor less the requests on it; under the busy rule also less what its measured
    busy share leaves under 75% of its processor, so a machine at its top takes no unit whatever its requests say."""
    by_req = machine["cpu_m"] - sum(u["req_m"] for u in units if u["machine"] == machine["name"])
    if rule == "busy" and machine.get("busy_m") is not None:
        return min(by_req, BUSY_TOP * machine["cpu_m"] - machine["busy_m"])
    return by_req


def place(req_m: float, service: str, machines: dict[str, dict], units: list[dict], how: str = "pack",
          rule: str = "requests") -> str | None:
    awake = [m for m in machines.values() if m["state"] == "awake"]
    fits = [m for m in awake if room(m, units, rule) >= req_m]
    if not fits:
        return None
    mine = {m["name"]: sum(1 for u in units if u["machine"] == m["name"] and u.get("service") == service) for m in awake}
    if how == "spread":
        return min(fits, key=lambda m: (mine[m["name"]], -room(m, units, rule), m["name"]))["name"]
    on = {name for name, n in mine.items() if n > 0}
    if len(on) == 1:
        # the service stands on one machine: its next unit goes to another machine where there is one with the room
        others = [m for m in fits if m["name"] not in on]
        if others:
            fits = others
    return min(fits, key=lambda m: (room(m, units, rule) - req_m, m["name"]))["name"]

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
