# Preregistration: Omni-Compass by itself, the third arm

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written and committed before any run of the arm, on the founder's order of 23 October: "a whole other Omni-Compass by itself,
without any Kubernetes or any schedulers or any governors, running direct muscles ... there's native, there's Omni and native,
and then there's Omni by itself, which we're going to add. That means the one that said Omni before is going to have to add the
words 'and native' ... a whole new set of monitors for every gauge and dashboard and Grafana ... so that the metrics are
following with real benchmarks." Nothing in the rules below changes after the first run of the arm starts; a change is an
amendment, written and dated here before the run it governs.

## The three arms

| Arm | Its words on every page | Its key in the records | What governs every muscle |
|---|---|---|---|
| native | native | `native` | the organism's own controllers, as shipped |
| Omni-Compass and native | Omni-Compass and native | `omni` (unchanged, so every record already written reads as it did) | Omni-Compass on top of the native controllers: the arm every table has carried since 26 September |
| Omni-Compass by itself | Omni-Compass by itself | `solo` | each muscle's own native controller switched off; Omni-Compass the only controller that moves the knob |

**What "by itself" switches off.** The controller of each muscle's own knob: on Kubernetes the pod autoscaler and the Cluster
Autoscaler; in our models each plant's own loop (a pool's autoscaler, a room's PI loop and its staging, a battery's dispatch, an
axis's PID). What stays is the organism itself: on Kubernetes the API server, the scheduler and the kubelet place and run the
pods in every arm, because without them there are no pods; "without any Kubernetes" holds only in our models. Omni-Compass never
touches the output directly: it moves knobs, and the muscles make the output, in every arm.

**The knob's setting with native off** is the operator's own, as the system starts: a pool's starting size, a workload's
replica count as its manifest ships it, a service's configured setting. **Never below**, with no live native to stand on: never
below the operator's own setting and never below the floor (two machines a pool, one replica a workload). The max is still the
default brain; the dial's tune-down is the only arm that may give back below the operator's setting, and only above the floor.

## Where by itself is the same arm, and where it is not run

- **The same arm, native being a setting and not a controller**: Redis (the memory ceiling), MySQL (the buffer pool), MongoDB
  (the storage engine's cache), the PostgreSQL pooler (its pool size), Kafka (the consumer group's size), and in our models
  every power cap, admission limit, setpoint and speed scale. Each table says so in one line; no run is repeated for it.
- **Native's own loop is the actuator and cannot be switched off**: the GPU's firmware, the robot's servo, the drone's
  autopilot, the grid's tap changer, and in our models the batteries' dispatch and the cooling units' staging. Each is labelled
  "native's own loop is the actuator: the same arm".
- **Not run: the cloud.** By itself, Omni-Compass would have to make machines with the cloud's autoscaler off; the order of 14
  October is that in a cloud it never adds a machine and only parks one the cloud made (`--give-back-only`), and every set costs
  money. A cloud arm by itself waits for the founder's word.

## What the engine that stands does by itself (read first, our own model)

On omni-v16 the governor moves a workload's pods only through the pod autoscaler's own object (its range and its target); with the
autoscaler switched off it has no pod muscle of its own: by itself it holds every workload at the operator's count and moves the
machines alone. `tools/solo_study.py` reads it on the toy cluster (class S), on the machines as the kind rig has them (every worker
made at the start, no cluster autoscaler), eight seeds of a day, the three arms on the same seeds; its page is written with the
version it reads, in `results/toy_gate/`.

## The next engine version: a pod muscle of its own, and the arm in our models

1. **A pod muscle of its own** (`omni_controller/`): for a workload the operator names (`--own-replicas namespace/name`) and that
   no autoscaler governs, the governor sets the replica count itself through the workload's own scale, with the compass law on the
   pods' busy share inside the cover the pod autoscaler's target would have had (the operator's target, from the workload's
   annotation, down to 60% of it), more pods at once when the response line is crossed, fewer only after the workload's own
   window and never below the operator's count; restored to the snapshot at the end, every write audited and read back.
2. **The arm in our models** (`realms/`): a switch on each plant that holds its knob at the operator's setting with no native
   loop, and the arm `solo` in the harness beside `native` and `v5`, the bodies' twins static with it.
3. **The toy gate first** (the order of 15 October), against the engine that stands, on the same seeds: every existing toy must
   read identical (the new muscle acts only where the operator names a workload, the switch only in the arm `solo`), native and
   `v5` byte-identical on the development seeds of the realms (7100 and up), and the toy cluster read by itself against this page.
   A LOSS anywhere is root-caused and fixed in the model before anything is run.
4. **Landed** with `tools/land_engine.py` as the next version, and, by the standing rule, every benchmark run again on it.

## What is run once it lands

- **Real Kubernetes, on GitHub's own machines ($0)**: `ARM=solo` on the kind rig (`scripts/kind_bench.sh`): the pod autoscaler
  removed after the deploy, the workload at its manifest's count, the governor with its own pod muscle on it; in
  `benchmark-reps` beside native and Omni-Compass and native, the arms rotated by repetition, three runs (A, B and C) through a
  new block in `scripts/reruns.txt`.
- **Our models (class S)**: the realms (the seven organisms), the orchestra (the eighth), the grid with a third value in every
  square, and the whole stack's composition (the ninth body) with a third total.

## How it is read

Every comparison is paired within its repetition and read by the one key (`tools/readings.py`): Omni-Compass by itself against
native, Omni-Compass by itself against Omni-Compass and native, and Omni-Compass and native against native as before. GAIN, STEADY
or LOSS by the gauge's aim, power given for a resource spent that rose, the floor of half of one percent, the three-run rule.
Every row is reported, LOSS included; a LOSS is answered by finding where the mechanism or its wiring is wrong.

## Threats to validity

- The operator's own setting decides much of what by itself reads: a workload shipped at one replica starts far below its load.
  The setting is the one the rig's manifest and the toy's scenario already carry, frozen here; it is never tuned to a result.
- The muscle cards were found on top of native; by itself they run as they are, and a card found for by itself is its own
  version.
- Kind has no cluster autoscaler: on kind, native's machine count is static, so the machine muscle is the same in both
  Omni-Compass arms there; only the pods differ.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
