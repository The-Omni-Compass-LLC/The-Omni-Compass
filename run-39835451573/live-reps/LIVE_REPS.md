# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 513.7 | 512.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 513.7 | 512.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 251.3 | 156.8 |
| response time (ms), 95th percentile | 694.1 | 336.3 |
| response time (ms), 99th percentile | 2041 | 1945 |
| time over the response line (% of samples) | 18.08 | 12.7 |
| failed requests (%) | 10.75 | 10.12 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 20.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3783 | 0.485 |
| utilisation (used / allocatable) | 0.09716 | 0.09596 |
| CPU used (cores), mean | 2.332 | 2.303 |
| Omni's own CPU (cores), mean | 0 | 0.0276 |
| CPU used with Omni's own (cores), mean | 2.332 | 2.331 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 326.1 | 332.3 |
| HPA replicas, mean | 9.343 | 9.267 |
| pods started | 5.8 | 7.7 |
| pod start wait, total (s) | 7.9 | 11.3 |
| pod start wait, mean (s) | 1.374 | 1.441 |
| host CPU busy, the real machine under kind (%) | 65.94 | 66.1 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.788e-16 to +3.235e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.509 | -0.1% | -0.01017 to +0.002501 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 513.7 | 512.6 | -0.2% | -2.463 to +0.3711 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 513.7 | 512.6 | -0.2% | -2.463 to +0.3711 | no |
| response time (ms), mean | 251.3 | 156.8 | -37.6% | -123 to -66.12 | yes: GAIN |
| response time (ms), 95th percentile | 694.1 | 336.3 | -51.5% | -466.8 to -248.7 | yes: GAIN |
| response time (ms), 99th percentile | 2041 | 1945 | -4.7% | -818.2 to +626.3 | no |
| time over the response line (% of samples) | 18.08 | 12.7 | -29.8% | -7.994 to -2.772 | yes: GAIN |
| failed requests (%) | 10.75 | 10.12 | -5.9% | -1.435 to +0.1607 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 20.6 | -16.9% | -5.406 to -2.994 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.2 | +42.2 (native is 0) | +32.66 to +51.74 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3783 | 0.485 | +28.2% | -0.1946 to +0.408 | no |
| utilisation (used / allocatable) | 0.09716 | 0.09596 | -1.2% | -0.002323 to -7.628e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.332 | 2.303 | -1.2% | -0.05575 to -0.001831 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0276 | +0.0276 (native is 0) | +0.02241 to +0.03279 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.331 | -0.1% | -0.03065 to +0.02827 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 326.1 | 332.3 | +1.9% | +0.4763 to +11.92 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.343 | 9.267 | -0.8% | -0.8654 to +0.7124 | no |
| pods started | 5.8 | 7.7 | +32.8% | -0.1358 to +3.936 | no |
| pod start wait, total (s) | 7.9 | 11.3 | +43.0% | -0.5926 to +7.393 | no |
| pod start wait, mean (s) | 1.374 | 1.441 | +4.9% | -0.204 to +0.3383 | no |
| host CPU busy, the real machine under kind (%) | 65.94 | 66.1 | +0.2% | -0.6806 to +1.008 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 22.8 |  |  | 10 |
| compass | 30.6 | +34.2% | +5.7 to +9.9 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*