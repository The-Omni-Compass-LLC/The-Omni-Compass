# Preregistration: the decision pace of the Kubernetes governor (the omni-v16 candidate)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written and committed before the runs, on the founder's word of 22 October ("Go"). The runs' commit is the one that
carries this file; nothing in the engine, the harness or this rule changes after the first run starts.

## The question

How often should the Kubernetes governor take its full decision? Every engine through omni-v15 decided every 60 s: the
period was written into the first harness on 26 September, with no reason recorded, and never measured against another.
Native's pod autoscaler checks every 15 s (the controller manager's `--horizontal-pod-autoscaler-sync-period`), the
metrics it reads refresh every 15 s, the Cluster Autoscaler scans every 10 s and KEDA every 30 s. The founder asked for
15, 10 and 5 s on 14 October; until now the period was not a clean setting, because rules counted in decisions changed
their meaning with it.

The omni-v16 candidate (branch `v16-candidate`) counts every clock of the governor in seconds, so the period changes only
how often it looks: the brain's own minute (its blending of each reading, its inner time, its dwell and waits, its
machines added or removed a minute), the compass's damping and smoothing, the edge's window and rates, the coast per
raise, the additions past the scheduling floor (a step a minute), a command's minute to land, the host's busy share
over a minute, the heat law's minute, one batch job a minute, the conveyance every 15 s whichever check falls due, and
the loop that keeps its own schedule (`tests/test_pace_clocks.py`, `tests/test_loop_schedule.py`). At 60 s it makes
exactly omni-v15's decisions (the toy cluster, 4,578 records, none different); the conveyance's 15 s and the loop's
schedule are the only changes a run at 60 s can see.

## What was read first, in our own models (class S)

The toy gate, before any run (`results/toy_gate/V16_VS_V15.md`, `results/toy_gate/V16_PACE.md`): the candidate against
omni-v15 on every toy, and the candidate alone at 60, 15, 10 and 5 s on a plant that moves every 5 s, in the cloud's
setting and in this benchmark's. A pace that reads a LOSS there is not run here.

## What is run

Workflow `benchmark-reps` on branch `v16-candidate`, three runs (A, B and C) of 10 repetitions each, on GitHub's own
machines (no cost). Each repetition runs five arms back to back on the same runner, each on a fresh kind cluster, in an
order rotated by repetition (`scripts/kind_paired.sh`):

| Arm | What governs |
|---|---|
| native | Kubernetes alone (the HPA at its target, the scheduler); Omni-Compass not started |
| compass | Omni-Compass on top of native, the compass law at the max, a full decision every 60 s |
| compass15 | the same, a full decision every 15 s |
| compass10 | the same, a full decision every 10 s |
| compass5 | the same, a full decision every 5 s |

The fast checks (the scheduling floor, the pod reflex, and the conveyance every 15 s) run every 5 s in every Omni arm.
The load is the reruns' steady scenario: 900 measured seconds an arm, a fixed rate (`loadgen=open`), the same work in
every arm; the line 500 ms at the 95th percentile. Each Omni arm ends with the reset, which must return every setting to
native with no record left (`scripts/kind_bench.sh`).

## How each pace is read

By the one key (`tools/readings.py`), from the three runs' receipts (`tools/live_reps.py`, `tools/confirm_abc.py`): each
pace against native, and each faster pace against the 60 s arm, paired within the repetition. A row reads GAIN or LOSS
only when all three runs agree in sign with every 95% interval clear of zero; EVEN when an interval includes zero; and
"the runs disagree" when clear runs point different ways. A resource that rises (pods, machines, energy, the settings
commands, the governor's own processor) is power given, never a LOSS; it is shown and named.

## The rule that picks the default (frozen now)

The default becomes the fastest pace that meets all four:

1. In the toy gate, no LOSS at that pace.
2. Against native: no row reads LOSS.
3. Against the 60 s arm: no row of work done, time waited, missed or failed reads LOSS or "the runs disagree".
4. Omni-Compass's own processor at that pace (the receipt's "Omni's own CPU (cores)", from the overhead record every
   Omni arm writes) stays under 0.1 of one core, a fortieth of the runner's four.

If no faster pace meets all four, the default stays 60 s and omni-v16 lands with every clock in seconds at 60. Whatever
lands is the next version under the standing rule (tested in the toy first, told, not asked) and every benchmark runs
again on it.

## What does not change

Native's own clocks, the harness, the scenario and every other rule. The cloud sets (Azure, Google, Amazon) are not part
of this choice, because they cost money; they run at whatever default lands.

## Threats to validity

- One scenario (steady, fixed-rate load) on kind: one runner whose nodes are containers on one host. A pace chosen here
  is the default everywhere until a scenario reads a LOSS at it, and then it is root-caused like any other.
- Below 15 s the processor numbers the governor reads repeat (metrics-server refreshes every 15 s): part of what is
  measured, not corrected for.
- The runs share GitHub's runners with the campaign; each repetition pairs its five arms on one runner at one time, so
  the queue changes no comparison.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
