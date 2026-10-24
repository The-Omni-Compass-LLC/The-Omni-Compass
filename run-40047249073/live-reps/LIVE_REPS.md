# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.514 | 1.518 | 1.515 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.8 | 159.1 | 158.8 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.8 | 159.1 | 158.8 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 148.4 | 143.6 | 142 | 139.4 | 76.57 |
| response time (ms), 95th percentile | 340.8 | 315.8 | 304.9 | 301.5 | 113.9 |
| response time (ms), 99th percentile | 536.4 | 507.6 | 498 | 477.6 | 153.7 |
| time over the response line (% of samples) | 2.273 | 1.851 | 1.663 | 1.687 | 0.02424 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 1.8 | 1.8 | 2.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 16.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.05167 | 0.08 | 0.02667 | 0.16 |
| utilisation (used / allocatable) | 0.03707 | 0.03722 | 0.03721 | 0.0371 | 0.03557 |
| CPU used (cores), mean | 0.8896 | 0.8933 | 0.8931 | 0.8904 | 0.8538 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00788 |
| CPU used with Omni's own (cores), mean | 0.8896 | 0.8933 | 0.8931 | 0.8904 | 0.8616 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757.4 | 755.2 | 755.1 | 758.4 | 780.4 |
| HPA replicas, mean | 8.392 | 8.958 | 9.56 | 9.843 | 7.805 |
| pods started | 5.2 | 4.3 | 2.6 | 1 | 4.4 |
| pod start wait, total (s) | 6.5 | 5.7 | 3.6 | 0.9 | 6.3 |
| pod start wait, mean (s) | 1.267 | 1.244 | 1.117 | 0.275 | 1.448 |
| host CPU busy, the real machine under kind (%) | 26.85 | 26.82 | 26.91 | 26.81 | 25.94 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.063e-16 to +7.286e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.519 | +0.3% | -0.003698 to +0.01236 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.9 | +0.1% | -0.7527 to +1.011 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.9 | +0.1% | -0.7527 to +1.011 | no |
| response time (ms), mean | 148.4 | 76.57 | -48.4% | -97.71 to -45.86 | yes: GAIN |
| response time (ms), 95th percentile | 340.8 | 113.9 | -66.6% | -308.2 to -145.6 | yes: GAIN |
| response time (ms), 99th percentile | 536.4 | 153.7 | -71.3% | -522.1 to -243.3 | yes: GAIN |
| time over the response line (% of samples) | 2.273 | 0.02424 | -98.9% | -3.766 to -0.7318 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | -100.0% | -4.054 to -0.5462 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.8 | +16.8 (native is 0) | +14.28 to +19.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.16 | +200.0% | -0.07761 to +0.2909 | no |
| utilisation (used / allocatable) | 0.03707 | 0.03557 | -4.0% | -0.002457 to -0.0005298 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8896 | 0.8538 | -4.0% | -0.05897 to -0.01272 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00788 | +0.00788 (native is 0) | +0.006596 to +0.009164 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8896 | 0.8616 | -3.1% | -0.05014 to -0.005791 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 757.4 | 780.4 | +3.0% | +6.684 to +39.29 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.392 | 7.805 | -7.0% | -1.199 to +0.02556 | no |
| pods started | 5.2 | 4.4 | -15.4% | -1.742 to +0.1417 | no |
| pod start wait, total (s) | 6.5 | 6.3 | -3.1% | -2.914 to +2.514 | no |
| pod start wait, mean (s) | 1.267 | 1.448 | +14.3% | -0.3481 to +0.7105 | no |
| host CPU busy, the real machine under kind (%) | 26.85 | 25.94 | -3.4% | -1.55 to -0.2858 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 340.8 | 536.4 | 8.392 | 0.8896 | 6 |
| Native tuned, HPA target 40 | 315.8 | 507.6 | 8.958 | 0.8933 | 6 |
| Native tuned, HPA target 30 | 304.9 | 498 | 9.56 | 0.8931 | 6 |
| Native tuned, HPA target 20 | 301.5 | 477.6 | 9.843 | 0.8904 | 6 |
| omni | 113.9 | 153.7 | 7.805 | 0.8616 | 6 |

- omni (p95 113.9 ms): no native setting tried reached it; the lowest native p95 is 301.5 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*