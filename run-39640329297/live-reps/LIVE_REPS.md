# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.518 | 1.517 | 1.515 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 158 | 157.8 | 157.6 | 157.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 158 | 157.8 | 157.6 | 157.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 117.5 | 114.4 | 111 | 110.6 | 64.96 |
| response time (ms), 95th percentile | 266.9 | 247.9 | 240.7 | 241.6 | 96.66 |
| response time (ms), 99th percentile | 432.8 | 408.8 | 397.2 | 377.6 | 133.1 |
| time over the response line (% of samples) | 1.494 | 1.413 | 1.313 | 1.334 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 1.6 | 1.2 | 1.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 16.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.2317 | 0 | 0.05333 | 0.3533 |
| utilisation (used / allocatable) | 0.03192 | 0.03217 | 0.03196 | 0.03191 | 0.03078 |
| CPU used (cores), mean | 0.7661 | 0.772 | 0.7671 | 0.7658 | 0.7386 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.0075 |
| CPU used with Omni's own (cores), mean | 0.7661 | 0.772 | 0.7671 | 0.7658 | 0.7461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 916.2 | 896.5 | 901.1 | 910.2 | 926.1 |
| HPA replicas, mean | 7.455 | 8.48 | 9.251 | 9.644 | 7.332 |
| pods started | 4.9 | 5.3 | 3.7 | 2 | 4.4 |
| pod start wait, total (s) | 7.6 | 8.7 | 4.9 | 3.3 | 5.8 |
| pod start wait, mean (s) | 1.552 | 1.658 | 1.28 | 1.017 | 1.293 |
| host CPU busy, the real machine under kind (%) | 23.41 | 23.82 | 23.61 | 23.5 | 23.11 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.513 | -0.2% | -0.0106 to +0.005265 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.3 | -0.3% | -1.439 to +0.3534 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.3 | -0.3% | -1.439 to +0.3534 | no |
| response time (ms), mean | 117.5 | 64.96 | -44.7% | -82.23 to -22.77 | yes: GAIN |
| response time (ms), 95th percentile | 266.9 | 96.66 | -63.8% | -250.7 to -89.83 | yes: GAIN |
| response time (ms), 99th percentile | 432.8 | 133.1 | -69.2% | -443.9 to -155.5 | yes: GAIN |
| time over the response line (% of samples) | 1.494 | 0 | -100.0% | -2.863 to -0.1245 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0 | -100.0% | -3.354 to -0.04635 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 | +16.3 (native is 0) | +14.58 to +18.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.3533 | +11.6% | -0.4108 to +0.4842 | no |
| utilisation (used / allocatable) | 0.03192 | 0.03078 | -3.6% | -0.002545 to +0.000254 | no |
| CPU used (cores), mean | 0.7661 | 0.7386 | -3.6% | -0.06109 to +0.006095 | no |
| Omni's own CPU (cores), mean | 0 | 0.0075 | +0.0075 (native is 0) | +0.00607 to +0.00893 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7661 | 0.7461 | -2.6% | -0.05239 to +0.01239 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 916.2 | 926.1 | +1.1% | -22.04 to +41.95 | no |
| HPA replicas, mean | 7.455 | 7.332 | -1.7% | -0.3957 to +0.1496 | no |
| pods started | 4.9 | 4.4 | -10.2% | -1.773 to +0.7729 | no |
| pod start wait, total (s) | 7.6 | 5.8 | -23.7% | -4.812 to +1.212 | no |
| pod start wait, mean (s) | 1.552 | 1.293 | -16.6% | -0.6622 to +0.1455 | no |
| host CPU busy, the real machine under kind (%) | 23.41 | 23.11 | -1.3% | -1.24 to +0.6352 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 266.9 | 432.8 | 7.455 | 0.7661 | 6 |
| Native tuned, HPA target 40 | 247.9 | 408.8 | 8.48 | 0.772 | 6 |
| Native tuned, HPA target 30 | 240.7 | 397.2 | 9.251 | 0.7671 | 6 |
| Native tuned, HPA target 20 | 241.6 | 377.6 | 9.644 | 0.7658 | 6 |
| omni | 96.66 | 133.1 | 7.332 | 0.7461 | 6 |

- omni (p95 96.66 ms): no native setting tried reached it; the lowest native p95 is 240.7 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*