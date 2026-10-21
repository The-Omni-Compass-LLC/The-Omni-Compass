# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.51 | 1.513 | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 157.9 | 158.1 | 158.3 | 158 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 157.9 | 158.1 | 158.3 | 158 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 132.8 | 131.1 | 130 | 129.9 | 72.05 |
| response time (ms), 95th percentile | 295.3 | 289.9 | 285.6 | 286.5 | 103.9 |
| response time (ms), 99th percentile | 450.6 | 447.6 | 456.1 | 450.9 | 138.4 |
| time over the response line (% of samples) | 1.382 | 1.61 | 1.708 | 1.635 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 1.6 | 1.4 | 1.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.16 | 0.05333 | 0 | 0.1333 |
| utilisation (used / allocatable) | 0.03511 | 0.03526 | 0.03502 | 0.03551 | 0.03401 |
| CPU used (cores), mean | 0.8427 | 0.8462 | 0.8405 | 0.8521 | 0.8164 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00784 |
| CPU used with Omni's own (cores), mean | 0.8427 | 0.8462 | 0.8405 | 0.8521 | 0.8242 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 810.4 | 807 | 809.3 | 803.8 | 818.4 |
| HPA replicas, mean | 8.118 | 8.82 | 9.386 | 9.803 | 8.07 |
| pods started | 5.2 | 4.4 | 3.3 | 1 | 4 |
| pod start wait, total (s) | 7.9 | 6.4 | 5.3 | 1.7 | 5 |
| pod start wait, mean (s) | 1.49 | 1.438 | 1.585 | 0.5 | 1.223 |
| host CPU busy, the real machine under kind (%) | 28.04 | 28.11 | 28.14 | 28.32 | 27.69 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.167e-15 to +6.345e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.514 | -0.1% | -0.006597 to +0.004597 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158 | -0.2% | -0.9649 to +0.2466 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158 | -0.2% | -0.9649 to +0.2466 | no |
| response time (ms), mean | 132.8 | 72.05 | -45.7% | -87.51 to -33.93 | yes: GAIN |
| response time (ms), 95th percentile | 295.3 | 103.9 | -64.8% | -259.6 to -123.2 | yes: GAIN |
| response time (ms), 99th percentile | 450.6 | 138.4 | -69.3% | -419.8 to -204.6 | yes: GAIN |
| time over the response line (% of samples) | 1.382 | 0.01212 | -99.1% | -2.504 to -0.2357 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.5 | 0 | -100.0% | -2.9 to -0.09951 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17 (native is 0) | +15.69 to +18.31 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.1333 | -43.7% | -0.4165 to +0.2099 | no |
| utilisation (used / allocatable) | 0.03511 | 0.03401 | -3.1% | -0.002259 to +5.997e-05 | no |
| CPU used (cores), mean | 0.8427 | 0.8164 | -3.1% | -0.05422 to +0.001439 | no |
| Omni's own CPU (cores), mean | 0 | 0.00784 | +0.00784 (native is 0) | +0.006953 to +0.008727 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8427 | 0.8242 | -2.2% | -0.04564 to +0.008539 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 810.4 | 818.4 | +1.0% | -20.03 to +35.94 | no |
| HPA replicas, mean | 8.118 | 8.07 | -0.6% | -0.2821 to +0.1849 | no |
| pods started | 5.2 | 4 | -23.1% | -2.012 to -0.3879 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 5 | -36.7% | -4.533 to -1.267 | yes: GAIN |
| pod start wait, mean (s) | 1.49 | 1.223 | -17.9% | -0.5146 to -0.01778 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.04 | 27.69 | -1.2% | -1.237 to +0.5478 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 295.3 | 450.6 | 8.118 | 0.8427 | 6 |
| Native tuned, HPA target 40 | 289.9 | 447.6 | 8.82 | 0.8462 | 6 |
| Native tuned, HPA target 30 | 285.6 | 456.1 | 9.386 | 0.8405 | 6 |
| Native tuned, HPA target 20 | 286.5 | 450.9 | 9.803 | 0.8521 | 6 |
| omni | 103.9 | 138.4 | 8.07 | 0.8242 | 6 |

- omni (p95 103.9 ms): no native setting tried reached it; the lowest native p95 is 285.6 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*