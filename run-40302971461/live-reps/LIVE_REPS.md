# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.52 | 1.517 | 1.518 | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.9 | 158.9 | 158.6 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.9 | 158.9 | 158.6 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 139.5 | 135.9 | 132.3 | 131.9 | 73.3 |
| response time (ms), 95th percentile | 317.5 | 304.5 | 284.2 | 298.4 | 112.5 |
| response time (ms), 99th percentile | 506 | 490.2 | 474.2 | 478.9 | 148.1 |
| time over the response line (% of samples) | 1.931 | 2.025 | 1.519 | 1.65 | 0.03622 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 2 | 1.6 | 1.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 15.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.02667 | 0.05167 | 0.05333 | 0.245 |
| utilisation (used / allocatable) | 0.03589 | 0.03596 | 0.036 | 0.03581 | 0.03432 |
| CPU used (cores), mean | 0.8613 | 0.8631 | 0.8641 | 0.8593 | 0.8237 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00796 |
| CPU used with Omni's own (cores), mean | 0.8613 | 0.8631 | 0.8641 | 0.8593 | 0.8317 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.1 | 796.6 | 792.4 | 800.9 | 816.7 |
| HPA replicas, mean | 7.93 | 8.818 | 9.442 | 9.745 | 7.598 |
| pods started | 5.1 | 4.4 | 2.9 | 1.5 | 3.5 |
| pod start wait, total (s) | 7.9 | 5.8 | 3.5 | 2.4 | 5 |
| pod start wait, mean (s) | 1.567 | 1.342 | 0.9217 | 0.625 | 1.438 |
| host CPU busy, the real machine under kind (%) | 25.99 | 26.1 | 26.15 | 26.03 | 25.28 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.517 | −0.2% | −0.0129 to +0.0069 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.5 | −0.4% | −1.7429 to +0.4429 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.5 | −0.4% | −1.7429 to +0.4429 | no |
| response time (ms), mean | 139.5 | 73.3 | −47.4% | −93.9385 to −38.4029 | yes: GAIN |
| response time (ms), 95th percentile | 317.5 | 112.5 | −64.6% | −276.8025 to −133.2275 | yes: GAIN |
| response time (ms), 99th percentile | 506 | 148.1 | −70.7% | −485.5951 to −230.1499 | yes: GAIN |
| time over the response line (% of samples) | 1.931 | 0.03622 | −98.1% | −3.1248 to −0.6655 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.3488 to −0.6512 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 | +15.900 (native is 0) | +12.6056 to +19.1944 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.245 | +206.2% | −0.0872 to +0.4172 | no |
| utilisation (used / allocatable) | 0.03589 | 0.03432 | −4.4% | −0.0032 to +0.0000 | no |
| CPU used (cores), mean | 0.8613 | 0.8237 | −4.4% | −0.0757 to +0.0005 | no |
| Omni's own CPU (cores), mean | 0 | 0.00796 | +0.008 (native is 0) | +0.0066 to +0.0093 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8613 | 0.8317 | −3.4% | −0.0665 to +0.0073 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.1 | 816.7 | +1.4% | −20.5978 to +43.8564 | no |
| HPA replicas, mean | 7.93 | 7.598 | −4.2% | −0.9545 to +0.2902 | no |
| pods started | 5.1 | 3.5 | −31.4% | −2.4396 to −0.7604 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 5 | −36.7% | −5.2228 to −0.5772 | yes: GAIN |
| pod start wait, mean (s) | 1.567 | 1.438 | −8.2% | −0.4751 to +0.2185 | no |
| host CPU busy, the real machine under kind (%) | 25.99 | 25.28 | −2.7% | −1.5578 to +0.1424 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 317.5 | 506 | 7.93 | 0.8613 | 6 |
| Native tuned, HPA target 40 | 304.5 | 490.2 | 8.818 | 0.8631 | 6 |
| Native tuned, HPA target 30 | 284.2 | 474.2 | 9.442 | 0.8641 | 6 |
| Native tuned, HPA target 20 | 298.4 | 478.9 | 9.745 | 0.8593 | 6 |
| omni | 112.5 | 148.1 | 7.598 | 0.8317 | 6 |

- omni (p95 112.5 ms): no native setting tried reached it; the lowest native p95 is 284.2 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*