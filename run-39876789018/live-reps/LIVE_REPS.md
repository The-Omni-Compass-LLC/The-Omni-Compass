# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.519 | 1.513 | 1.515 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.8 | 158.3 | 158.3 | 158.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.8 | 158.3 | 158.3 | 158.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 134.4 | 133.9 | 132.6 | 129 | 71.71 |
| response time (ms), 95th percentile | 306.5 | 293 | 292.9 | 281.6 | 107.8 |
| response time (ms), 99th percentile | 483.7 | 478.3 | 480.6 | 485.9 | 135.8 |
| time over the response line (% of samples) | 1.711 | 1.785 | 1.761 | 1.683 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 1.8 | 1.7 | 1.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.07833 | 0.105 | 0.02667 | 0.1583 |
| utilisation (used / allocatable) | 0.03523 | 0.0349 | 0.03556 | 0.03499 | 0.03349 |
| CPU used (cores), mean | 0.8455 | 0.8377 | 0.8534 | 0.8398 | 0.8037 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.02164 |
| CPU used with Omni's own (cores), mean | 0.8455 | 0.8377 | 0.8534 | 0.8398 | 0.8253 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.8 | 833.4 | 819.8 | 832.6 | 851.2 |
| HPA replicas, mean | 8.075 | 8.689 | 9.311 | 9.776 | 8.206 |
| pods started | 5.5 | 4.8 | 3.4 | 1.1 | 4 |
| pod start wait, total (s) | 7.8 | 6.3 | 5.3 | 1.3 | 5.7 |
| pod start wait, mean (s) | 1.449 | 1.32 | 1.567 | 0.475 | 1.448 |
| host CPU busy, the real machine under kind (%) | 25.53 | 25.17 | 25.58 | 25.33 | 25.09 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.785e-16 to +8.338e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.1% | -0.003743 to +0.00741 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.3 | -0.1% | -0.8067 to +0.4182 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.3 | -0.1% | -0.8067 to +0.4182 | no |
| response time (ms), mean | 134.4 | 71.71 | -46.6% | -90.8 to -34.52 | yes: GAIN |
| response time (ms), 95th percentile | 306.5 | 107.8 | -64.8% | -275 to -122.5 | yes: GAIN |
| response time (ms), 99th percentile | 483.7 | 135.8 | -71.9% | -484.5 to -211.2 | yes: GAIN |
| time over the response line (% of samples) | 1.711 | 0 | -100.0% | -2.975 to -0.4476 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | -100.0% | -3.462 to -0.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | +17.9 (native is 0) | +16.57 to +19.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1583 | +18.7% | -0.1839 to +0.2339 | no |
| utilisation (used / allocatable) | 0.03523 | 0.03349 | -4.9% | -0.002928 to -0.0005586 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8455 | 0.8037 | -4.9% | -0.07026 to -0.01341 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02164 | +0.0216 (native is 0) | +0.01779 to +0.02549 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8455 | 0.8253 | -2.4% | -0.04523 to +0.004841 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.8 | 851.2 | +3.2% | +5.963 to +46.87 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.075 | 8.206 | +1.6% | -0.2987 to +0.5604 | no |
| pods started | 5.5 | 4 | -27.3% | -2.408 to -0.5921 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5.7 | -26.9% | -3.899 to -0.3014 | yes: GAIN |
| pod start wait, mean (s) | 1.449 | 1.448 | -0.1% | -0.2778 to +0.2759 | no |
| host CPU busy, the real machine under kind (%) | 25.53 | 25.09 | -1.7% | -1.11 to +0.2273 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 306.5 | 483.7 | 8.075 | 0.8455 | 6 |
| Native tuned, HPA target 40 | 293 | 478.3 | 8.689 | 0.8377 | 6 |
| Native tuned, HPA target 30 | 292.9 | 480.6 | 9.311 | 0.8534 | 6 |
| Native tuned, HPA target 20 | 281.6 | 485.9 | 9.776 | 0.8398 | 6 |
| omni | 107.8 | 135.8 | 8.206 | 0.8253 | 6 |

- omni (p95 107.8 ms): no native setting tried reached it; the lowest native p95 is 281.6 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*