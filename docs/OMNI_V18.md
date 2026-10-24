# Omni v18: Omni-Compass by itself, a pod muscle of its own

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v18 (`OMNI_V18.json`, digest `22486290b19349eb`, 55 files) lands on 24 October, 01:30 UTC, under the founder's order of
23 October that every organism is shown three ways: native; Omni-Compass and native; and Omni-Compass by itself, "running direct
muscles" with native's own controller of that muscle switched off ("there's native, there's Omni and native, and then there's Omni
by itself"). It is omni-v17 (`docs/OMNI_V17.md`) with one muscle added, in `omni_controller/controller.py`, and the models' arm
that runs it, in `realms/harness.py` and `realms/plants.py` (52 of its 55 files are omni-v17's bytes). Nothing moves unless the
operator names a workload to the muscle: with no workload named the engine is omni-v17, decision for decision (the toy gate below).
Preregistered before any run (`docs/SOLO_PREREGISTRATION.md`). Read in the toy gate against omni-v17 on the same seeds
(`results/toy_gate/V18_VS_V17.md`) and by itself beside native and beside Omni-Compass and native
(`results/toy_gate/SOLO_V18.md`) before it was pushed. The readings are our own models (evidence class S), never a benchmark result.
Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## The pod muscle of its own

On every engine before it, the Kubernetes governor moved a workload's pods only through the pod autoscaler's own object (its range
and its target): with the pod autoscaler switched off it had no pod muscle, so "by itself" held every workload at the operator's
count. omni-v18 gives it one (`--own-replicas`, `_own_pods`). For each workload the operator names and no autoscaler governs, the
governor sets the replica count itself, through the workload's own scale, by strict C's rule: replicas = ⌈current × measured busy
share / target⌉, up at once, down only to the highest recommendation of the last 300 s, inside a tolerance of a tenth. The target is
the one the compass moves for an autoscaler: the operator's own (the workload's target annotation, else `--own-target`), down to
60% of it, the most pods the cover allows past the wall. Never below the operator's own count at the max, never above the range's
top, never below one pod; the count it shipped is recorded once on the workload and handed back by the reset. A workload an
autoscaler governs keeps its autoscaler: the muscle writes nothing there. The muscle keeps the pace of the controller it stands in
for: a reconciliation every 15 s on the fast checks (`--own-every-s`, the pod autoscaler's sync), at the target the last decision
set; the compass moves the target only in a decision.

## The fault the gate found before it landed

Rebuilt on omni-v17, whose main engine decides every 60 s, the first candidate moved its pods only at a decision, once a minute.
By itself in the toy it then read the minutes over the response line **LOSS** against native (26.4 to 34.8 minutes a day), the 95th
percentile still a GAIN. The pod autoscaler it stands in for syncs every 15 s. The muscle now reconciles every 15 s between
decisions; its window of fewer pods counts those reconciliations (the strict window's 300 s at any beat). Two unit tests hold it
(`tests/test_own_replicas.py`, 11 in all).

## By itself, in our own model (`results/toy_gate/SOLO_V18.md`, 8 seeds of a day, class S)

| Gauge | native | Omni-Compass and native | Omni-Compass by itself |
|---|---:|---:|---:|
| machine-hours | 288.0 | 288.0 | 288.0 |
| pods waiting for a place (pod-minutes an hour) | 0.0 | 0.0 | 0.0 |
| 95th percentile response (ms) | 80.0 | 76.8 | 64.4 |
| minutes over the response line (a day) | 26.4 | 22.0 | 9.3 |

By the one key, Omni-Compass by itself against native: the 95th percentile **+19.4% GAIN** (+12.2% to +26.6%), the minutes over the
line **+64.9% GAIN** (+32.4% to +97.5%), machine-hours, energy per core-hour and pods waiting EVEN (identical machines). Against
Omni-Compass and native: the 95th percentile **+16.0% GAIN**, the minutes over the line **+58.0% GAIN**, the rest EVEN.
Omni-Compass and native against native: the 95th percentile **+4.0% GAIN**, the minutes over the line **+16.6% GAIN**.

## The toy gate against omni-v17 (`results/toy_gate/V18_VS_V17.md`)

Every toy, 8 seeds: the cluster in the cloud's setting at 60 and 15 s, the blink, the shipped default, the four conveyance toys, the
card and the card near its voltage floor, and the verdict. Every gauge of every toy reads **identical** to omni-v17, because no toy
names a workload to the muscle. No LOSS against the engine that stands.

## The rows against native that read LOSS (the engine's, as on omni-v17)

The same toys read against native carry the rows omni-v17 carries, unchanged, each on the next version's list with its cause:
pods waiting at a 15 s decision in the cloud's setting (−121.6% LOSS) and its 95th percentile (−0.36% LOSS); alert minutes with
the machines blinking out of the reading (−2.35% LOSS); the start wait in the conveyance toy (−9.0% LOSS, its 95th percentile
−10.0% LOSS) beside +64.2% GAIN in requests served and +53.1% GAIN in the 95th percentile; in the batch toy the requests served
(−2.11% LOSS), the alert minutes (−9.82% LOSS) and the batch turnaround (−0.05% LOSS); the card's 95th percentile (−2.38% LOSS;
near its voltage floor −5.78% LOSS) beside its energy (+4.72% GAIN; +1.30% GAIN). Every row is shown.

## Where it runs

On Kubernetes, the kind rig's `ARM=solo` (`scripts/kind_bench.sh`): the pod autoscaler removed, the operator's target and range
written on the workload, Omni-Compass the only controller of its pods; Kubernetes' own scheduler and kubelet stay. The three-run
tables read it against native (`solo`) and against Omni-Compass and native (`solo|compass`) (`tools/confirm_abc.py`,
`tools/live_reps.py`). In our models, the organisms runner's third arm (`tools/run_realms_v5.py`): every pool whose own autoscaler
can be switched off. Where native is a setting, or its own loop is the actuator, the two Omni-Compass arms are one. No cloud runs
by itself without the founder's word (the order of 14 October: nothing in a cloud adds a machine).

## Beside it: Omni-Compass direct

Omni-Compass's own orchestrator (`omni_orchestrator/`, `docs/OMNI_ORCHESTRATOR.md`) runs the organism with no Kubernetes at all,
its own walls, hands, front, room rule, brain and control plane. It is its own files beside the engine, not in the fingerprint; it
uses the engine's compass law and verdict, and its showings on GitHub play back on the live engine (section 5g).

## The real runs

Every benchmark runs again on omni-v18 (`scripts/reruns.txt`; the conductor's campaign from the moment it stands on main), and
`ARM=solo` joins the kind sets beside native and Omni-Compass and native, three runs, read by the one key.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
