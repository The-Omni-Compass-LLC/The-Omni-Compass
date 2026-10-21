# Omni v14: a knob for every muscle, no raise on the reading that opens another workload's run, commands without a shell (the engine that stands since 21 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v14 has been the engine on main since 21 October. The founder's orders behind it: knobs on every monitor, "to turn off and
on such a mechanism, a muscle, or tweak and turn any muscle" (20 October, evening), and, the next night, "tune the engine". It is
omni-v13 (`docs/OMNI_V13.md`) with three changes, each written before it was built and each read in the toy gate against omni-v13
on the same seeds before it landed: a knob that leaves any one muscle native, the conveyance's last raise on a shared host taken
away where its reading could not see the other workload's load, and the operator's own commands run without a shell. Every
setting, gain, preset and muscle is omni-v13's, and so is every other rule.

Its fingerprint is `OMNI_V14.json` (digest DIGEST, 47 files). Forty-five files are omni-v13's bytes; two differ, the Kubernetes
governor (`omni_controller/controller.py`) and its muscles (`omni_controller/muscles.py`). Every benchmark runs again on
omni-v14, A, B and C. Every earlier table stands as its own engine's result until its three runs on v14 land, and results from
two versions are never pooled. The readings from the toy gate are our own models (evidence class S), never a benchmark result.
Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

| # | Change | Where | Why |
|---|---|---|---|
| 1 | `--native MUSCLE[,...]` leaves each named muscle where native runs it: never written, the rest running as before; a name that is not a muscle is refused at the start | the governor and its muscles; the control panel's muscle button | the founder's order of 20 October: a knob for every muscle; and his rule that a muscle Omni-Compass would hurt stays native |
| 2 | On a shared host beside another workload with room of its own, no limit is raised on the reading that opens that workload's run: no pod of it with room was running at the previous reading, and now one runs or is starting, so it ran for none or part of the interval and the reading does not hold its load. The next reading decides as omni-v13 does. Lowering and omni-v13's hand-back are never held | the conveyance (`omni_controller/muscles.py`) | omni-v13 still raised the web's limits once, on the reading that opened the batch queue, and handed them back 15 s later; in the toy set from KubeRay's rig the job turnaround read +0.03% against native, a LOSS by the key (`results/toy_gate/V13_VS_V12.md`). The same raise is the mechanism behind the two LOSS rows of the omni-v12 group runs (`docs/GROUP_PREREGISTRATION.md`, amendment 3) |
| 3 | The operator's own commands (the site power reading, a muscle's read command, a wall meter's `cmd:`) run without a shell unless they hold a pipe, a redirect or a variable | `run_operator_cmd` (`omni_controller/muscles.py`), `tools/wall_meter.py` | the static scan's three high findings (`docs/SECURITY_SCAN.md`); the governor's site power reading no longer reaches a shell at all |

## 1. The knob

`--native MUSCLE[,MUSCLE...]` (or `OMNI_NATIVE`) names the muscles the governor leaves native. A muscle named there is never
written: it stays where native runs it, and every other muscle runs as before. The governor still reads the whole body and
decides with all of it in view; only the write of a muscle left native is withheld, and the audit says so (`"held"`, and
`"native_muscles"` at the start). A name that is not a muscle is refused at the start, never ignored, so a misspelling can
never leave a muscle driven that the operator meant to leave native.

| Muscle | What is left native |
|---|---|
| `machines` | the node pool's size (the operator's node-scale command) |
| `replicas` | the pod autoscaler's target, the pod reflex's replica floor and the replica cap |
| `cpu` | the serving pods' CPU limits (the conveyance and the pod power cap) |
| `clock` | the processors' frequency ceiling |
| `gpu` | the GPU's power limit |
| `rollout` | the rollout guard (pause and undo) |
| `batch` | the batch admission and pacing |
| `rightsize`, `coldstart`, `contain`, `cooling` | the pods' rightsizing, the cold-start reserve, the namespaces' containment, the cooling setpoint |

## 2. The button

The control panel (`tools/omni_control.py`) carries it as one more button, `POST /v1/muscle {"muscle": NAME, "on": true|false}`,
role operator, every press audited with its holder and reason, and as a row of On and Native buttons on the console. Like a
dial press it passes through native: the governor's own kill file is set, its exit awaited (every setting it wrote restored
and read back), and it starts again with the new list. Nothing is changed under a running governor. The monitor wall
(`docs/MONITOR_WALL.md`) points every row at these buttons; the wall itself never presses one.

## 3. The conveyance's reading and the other workload's run

The governor reads the host's busy share as the change in the host's processor counters since its previous reading (every
15 s, on its fast check). A batch pod that started between two readings ran for part of the interval; one still starting
(Pending) ran for none of it. So on the reading that opens a batch's run, the busy share is the host before most of its load,
and on a host whose batch is about to fill it, omni-v13 could read room that was no longer there: it raised the web pods' limits
on that reading and handed them back on the next, once the busy share showed the host at its top. omni-v14 keeps, for each
serving deployment, the other workloads' pods with room that were running at the previous reading. When none was, and now one
runs or is starting, nothing is raised on this reading, and the audit says why (`"reading_opens_another_workload": true` on the
`"convey": "held"` record). The next reading, which holds that workload's load, decides as omni-v13 does. A new pod of a workload
already running holds nothing, nothing is lowered later for it, and nothing about a host with no other workload's room changes.
Tests: `tests/test_convey_shared_host.py`, `ReadingThatOpensAnotherWorkload`; omni-v13's hand-back tests carry the one line that
says their batch pod ran through the previous reading.

A broader rule was written and tried first: no raise on any reading older than that workload's newest running pod, so every
reading after any new batch pod started. The toy gate refused it: in the batch toy the web's 95th percentile read 6.4% higher
than omni-v13's, a LOSS, because a stream of jobs starts a pod every few seconds and the web lost the raises it had earned
between the queue's openings. It is not in omni-v14. The gate also found the toy listing a batch pod as Running from the moment
it was made; a cluster lists it as Pending until its container runs (the rig's own pod start, about 3 s). The toy now lists it as
the cluster does, the same for both engines, and both were read on it (section 5).

## 4. The operator's commands without a shell

A command the operator configured (`--power-cmd`, a muscle's read command in the wiring file, a wall meter's `cmd:`) is split
into its words as a shell would split them and run directly when it holds nothing only a shell reads: no pipe, list, redirect,
subshell, variable, substitution, glob, home directory, comment or `NAME=value` before the command. One that does runs through
the shell as before, so no operator's wiring changes. Tests: `tests/test_operator_cmd.py`. The static scan reads two high
findings where it read three (`docs/SECURITY_SCAN.md`): the governor's own call to a shell is gone, and the two that remain are
the fallback for a command that needs one.

## 5. The toy gate against omni-v13

GATE

## 6. What stays omni-v13's

Every other engine file; every rule, gain and guard but the two above, the conveyance's hand-back of omni-v13 among them; the verdict byte for
byte. The next version's list (`docs/CHANGE_CONTROL.md`) carries what is still to fix. The GPU governors
(`omni_controller/gpu_governor.py`, `gpu_compass.py`) keep their own two levers, the power limit and the clock, and take the
per-muscle knob with the version that next changes them.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
