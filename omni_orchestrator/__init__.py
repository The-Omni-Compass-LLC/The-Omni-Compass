# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass's own orchestrator: the organism run without Kubernetes (the founder's order of 23 October 2026).

Written from scratch on Python's standard library and Omni-Compass's own compass law (omnicompass/compass_law.py); no
code of Kubernetes, Docker Swarm, Nomad, Slurm or any other orchestrator is in it. The layers under it stay native: the
Linux kernel shares each machine's processor among its units and enforces the walls set here.

  cgroup.py     a machine's and a unit's walls: CPU and memory limits through the kernel's control groups
  agent.py      a machine's hand, one process per machine: starts, watches, restarts and stops the units on its
                machine, inside its walls, and answers the control plane over HTTP
  workload.py   the showing's organism: a service whose every answer can be checked, and batch tasks
  front.py      one address for a service: requests queued and handed to ready units one at a time each, retried on
                another unit when one dies; the response time it measures is the brain's sense
  scheduler.py  where a unit goes: the room on each machine, a service never on one machine alone, packed onto the
                fewest machines (Omni) or spread over all (the yardstick)
  brain.py      how many units and how many machines: the compass law on the response time, never below its native
                twin (the yardstick's rule computed on the same readings); the yardstick's rule itself beside it
  control.py    the control plane: the ledger of what is wanted and what runs, journaled and replayed after a crash;
                the checks every second; the brain on its beat; the kill switch; the routes; the audit
  load.py       closed-loop clients stepping by one, every answer checked against its known digest
"""

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
