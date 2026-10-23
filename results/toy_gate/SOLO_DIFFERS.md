# Omni-Compass by itself on the toy cluster (differs)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Our own model (evidence class S), never a benchmark result. The founder's order of 23 October: beside native and Omni-Compass and native, a third arm, Omni-Compass by itself, with native's controllers switched off (`docs/SOLO_PREREGISTRATION.md`). This page reads what the engine that stands does by itself on the toy cluster: 8 seeds of a day, the same seeds in every arm, read by the toy gate's own rule (`tools/toy_gate.py`: the mean change over the seeds, its 95% interval by Student t, the word by the gauge's aim; a resource that rose is power given).

Engine: differs from omni-v16: omni_controller/controller.py. Written by `python3 tools/solo_study.py`; every seed's reading of every arm is in its JSON twin (`per_seed`).

| Arm | What governs |
|---|---|
| native | the pod autoscaler (its target 70%) and the Cluster Autoscaler, as Kubernetes ships them |
| Omni-Compass and native | the shipped governor on top of both, the compass law at the max (as ARM=compass runs it) |
| Omni-Compass by itself | both native controllers switched off: every workload's pods at the operator's own count, the pool at its starting size (12 machines); the shipped governor the only controller, the compass law at the max |

## The means over the seeds

| Gauge | native | Omni-Compass and native | Omni-Compass by itself |
|---|---:|---:|---:|
| machine-hours | 288.000 | 288.000 | 288.000 |
| energy per used core-hour (kWh) | 0.063 | 0.063 | 0.063 |
| pods waiting for a place (pod-minutes an hour) | 0.000 | 0.000 | 0.000 |
| the pod autoscaler's shortfall (minutes an hour) | 3.585 | 3.596 | 0.000 |
| 95th percentile response (ms) | 79.955 | 76.612 | 65.545 |
| minutes over the response line | 26.375 | 18.250 | 8.125 |

## Omni-Compass by itself against native

| Gauge | Change | 95% interval | Reading |
|---|---:|---:|---|
| machine-hours | =0.0% | ±0.0% to ±0.0% | **EVEN (identical)** |
| energy per used core-hour (kWh) | =0.0% | −0.0% to +0.0% | **EVEN** |
| pods waiting for a place (pod-minutes an hour) | — | — | **EVEN (identical)** |
| the pod autoscaler's shortfall (minutes an hour) | +100.0% | +91.7% to +108.3% | **GAIN** |
| 95th percentile response (ms) | +18.0% | +11.3% to +24.7% | **GAIN** |
| minutes over the response line | +69.2% | +37.4% to +101.0% | **GAIN** |

## Omni-Compass by itself against Omni-Compass and native

| Gauge | Change | 95% interval | Reading |
|---|---:|---:|---|
| machine-hours | =0.0% | ±0.0% to ±0.0% | **EVEN (identical)** |
| energy per used core-hour (kWh) | =0.0% | −0.0% to +0.0% | **EVEN** |
| pods waiting for a place (pod-minutes an hour) | — | — | **EVEN (identical)** |
| the pod autoscaler's shortfall (minutes an hour) | +100.0% | +89.1% to +110.9% | **GAIN** |
| 95th percentile response (ms) | +14.4% | +8.9% to +20.0% | **GAIN** |
| minutes over the response line | +55.5% | +28.9% to +82.0% | **GAIN** |

## Omni-Compass and native against native

| Gauge | Change | 95% interval | Reading |
|---|---:|---:|---|
| machine-hours | =0.0% | ±0.0% to ±0.0% | **EVEN (identical)** |
| energy per used core-hour (kWh) | =0.0% | −0.0% to +0.0% | **EVEN** |
| pods waiting for a place (pod-minutes an hour) | — | — | **EVEN (identical)** |
| the pod autoscaler's shortfall (minutes an hour) | =0.3% | −3.6% to +4.2% | **EVEN** |
| 95th percentile response (ms) | +4.2% | +2.5% to +5.9% | **GAIN** |
| minutes over the response line | +30.8% | +14.7% to +46.9% | **GAIN** |

## The candidate (differs) against the engine that stands (omni-v16), arm by arm

| Gauge | native | Omni-Compass and native | Omni-Compass by itself |
|---|---|---|---|
| machine-hours | EVEN (identical) | EVEN (identical) | EVEN (identical) |
| energy per used core-hour (kWh) | EVEN (identical) | EVEN (identical) | GAIN +4.2% |
| pods waiting for a place (pod-minutes an hour) | EVEN (identical) | EVEN (identical) | EVEN (identical) |
| the pod autoscaler's shortfall (minutes an hour) | EVEN (identical) | EVEN (identical) | EVEN (identical) |
| 95th percentile response (ms) | EVEN (identical) | EVEN (identical) | GAIN +100.0% |
| minutes over the response line | EVEN (identical) | EVEN (identical) | GAIN +99.4% |

## What it says

On the engine that stands the governor moves a workload's pods only through the pod autoscaler's own object (its range and its target); with the pod autoscaler switched off it has no pod muscle of its own, so by itself it holds every workload at the operator's count and moves the machines alone. The table above is that engine by itself, read as it is; the pod muscle of its own is the next engine version's work (`docs/SOLO_PREREGISTRATION.md`), read first in this same toy, against this page, before any real run.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
