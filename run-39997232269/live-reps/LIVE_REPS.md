# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 518.3 | 517.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518.3 | 517.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 299 | 158.3 |
| response time (ms), 95th percentile | 830.7 | 326.2 |
| response time (ms), 99th percentile | 2917 | 1535 |
| time over the response line (% of samples) | 20.28 | 12.16 |
| failed requests (%) | 10.73 | 9.837 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.3 | 22 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2167 |
| utilisation (used / allocatable) | 0.1042 | 0.1029 |
| CPU used (cores), mean | 2.5 | 2.469 |
| Omni's own CPU (cores), mean | 0 | 0.00913 |
| CPU used with Omni's own (cores), mean | 2.5 | 2.478 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 289.1 | 293.6 |
| HPA replicas, mean | 9.438 | 9.975 |
| pods started | 5.4 | 7.6 |
| pod start wait, total (s) | 8.2 | 12.2 |
| pod start wait, mean (s) | 1.508 | 1.602 |
| host CPU busy, the real machine under kind (%) | 70.24 | 69.68 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.146e-15 to +9.679e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.511 | -0.0% | -0.004519 to +0.002519 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 518.3 | 517.4 | -0.2% | -1.916 to +0.1593 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518.3 | 517.4 | -0.2% | -1.916 to +0.1593 | no |
| response time (ms), mean | 299 | 158.3 | -47.1% | -177.1 to -104.4 | yes: GAIN |
| response time (ms), 95th percentile | 830.7 | 326.2 | -60.7% | -652.3 to -356.8 | yes: GAIN |
| response time (ms), 99th percentile | 2917 | 1535 | -47.4% | -2226 to -537.6 | yes: GAIN |
| time over the response line (% of samples) | 20.28 | 12.16 | -40.1% | -10.79 to -5.463 | yes: GAIN |
| failed requests (%) | 10.73 | 9.837 | -8.3% | -1.726 to -0.06523 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.3 | 22 | -24.9% | -9.588 to -5.012 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.1 | +43.1 (native is 0) | +32.38 to +53.82 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2167 | +16.1% | -0.08053 to +0.1405 | no |
| utilisation (used / allocatable) | 0.1042 | 0.1029 | -1.3% | -0.002375 to -0.0002506 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.5 | 2.469 | -1.3% | -0.057 to -0.006014 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00913 | +0.00913 (native is 0) | +0.007909 to +0.01035 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.5 | 2.478 | -0.9% | -0.04809 to +0.003327 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 289.1 | 293.6 | +1.6% | +0.7253 to +8.276 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.438 | 9.975 | +5.7% | +0.06442 to +1.01 | yes: power given |
| pods started | 5.4 | 7.6 | +40.7% | -0.3857 to +4.786 | no |
| pod start wait, total (s) | 8.2 | 12.2 | +48.8% | -1.406 to +9.406 | no |
| pod start wait, mean (s) | 1.508 | 1.602 | +6.3% | -0.226 to +0.4145 | no |
| host CPU busy, the real machine under kind (%) | 70.24 | 69.68 | -0.8% | -1.202 to +0.0924 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.2 |  |  | 10 |
| compass | 28.2 | +46.9% | +6.0 to +12.0 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*