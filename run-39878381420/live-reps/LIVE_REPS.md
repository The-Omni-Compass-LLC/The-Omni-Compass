# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.518 | 1.518 | 1.518 | 1.521 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.3 | 160.4 | 160.3 | 160.4 | 160.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.3 | 160.4 | 160.3 | 160.4 | 160.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 179.3 | 172.4 | 170.2 | 173.7 | 88.49 |
| response time (ms), 95th percentile | 412.2 | 380.7 | 384.4 | 396 | 135.7 |
| response time (ms), 99th percentile | 666.3 | 672.7 | 644.1 | 640.5 | 182.6 |
| time over the response line (% of samples) | 3.371 | 2.642 | 2.637 | 3.065 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.6 | 2.8 | 2.7 | 3.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 18.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1583 | 0.07833 | 0.1067 | 0.2117 |
| utilisation (used / allocatable) | 0.0428 | 0.04243 | 0.0423 | 0.04268 | 0.04099 |
| CPU used (cores), mean | 1.027 | 1.018 | 1.015 | 1.024 | 0.9837 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.02539 |
| CPU used with Omni's own (cores), mean | 1.027 | 1.018 | 1.015 | 1.024 | 1.009 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 641.7 | 645.6 | 650.6 | 647.6 | 666.5 |
| HPA replicas, mean | 8.722 | 9.253 | 9.654 | 9.927 | 9.312 |
| pods started | 5 | 3.5 | 2 | 0.4 | 2.9 |
| pod start wait, total (s) | 6.9 | 5.2 | 2.8 | 0.7 | 3.5 |
| pod start wait, mean (s) | 1.387 | 1.345 | 1.25 | 0.175 | 1.367 |
| host CPU busy, the real machine under kind (%) | 30.49 | 30.22 | 30.21 | 30.4 | 29.94 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.599e-16 to +1.115e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.521 | +0.3% | -0.001658 to +0.01199 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.3 | 160.4 | +0.1% | -0.4797 to +0.7627 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.3 | 160.4 | +0.1% | -0.4797 to +0.7627 | no |
| response time (ms), mean | 179.3 | 88.49 | -50.6% | -110.6 to -71.02 | yes: GAIN |
| response time (ms), 95th percentile | 412.2 | 135.7 | -67.1% | -338.2 to -214.8 | yes: GAIN |
| response time (ms), 99th percentile | 666.3 | 182.6 | -72.6% | -593.5 to -373.8 | yes: GAIN |
| time over the response line (% of samples) | 3.371 | 0 | -100.0% | -4.558 to -2.185 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.6 | 0 | -100.0% | -5.153 to -2.047 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | +18.3 (native is 0) | +16.83 to +19.77 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.2117 | +693.8% | -0.01673 to +0.3867 | no |
| utilisation (used / allocatable) | 0.0428 | 0.04099 | -4.2% | -0.002894 to -0.0007187 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.027 | 0.9837 | -4.2% | -0.06945 to -0.01725 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02539 | +0.0254 (native is 0) | +0.02255 to +0.02823 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.027 | 1.009 | -1.7% | -0.04371 to +0.007795 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 641.7 | 666.5 | +3.9% | +11.92 to +37.59 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.722 | 9.312 | +6.8% | +0.1551 to +1.026 | yes: power given |
| pods started | 5 | 2.9 | -42.0% | -3.337 to -0.8633 | yes: GAIN |
| pod start wait, total (s) | 6.9 | 3.5 | -49.3% | -4.003 to -2.797 | yes: GAIN |
| pod start wait, mean (s) | 1.387 | 1.367 | -1.4% | -0.5007 to +0.4607 | no |
| host CPU busy, the real machine under kind (%) | 30.49 | 29.94 | -1.8% | -1.267 to +0.1761 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 412.2 | 666.3 | 8.722 | 1.027 | 6 |
| Native tuned, HPA target 40 | 380.7 | 672.7 | 9.253 | 1.018 | 6 |
| Native tuned, HPA target 30 | 384.4 | 644.1 | 9.654 | 1.015 | 6 |
| Native tuned, HPA target 20 | 396 | 640.5 | 9.927 | 1.024 | 6 |
| omni | 135.7 | 182.6 | 9.312 | 1.009 | 6 |

- omni (p95 135.7 ms): no native setting tried reached it; the lowest native p95 is 380.7 ms (Native tuned, HPA target 40).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*