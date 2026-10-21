# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.517 | 1.517 | 1.516 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.3 | 158.3 | 158.2 | 158.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.3 | 158.3 | 158.2 | 158.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 127.4 | 124 | 123.5 | 120.3 | 69.64 |
| response time (ms), 95th percentile | 275.1 | 260.2 | 261.8 | 251.7 | 100.8 |
| response time (ms), 99th percentile | 422.8 | 423.7 | 430.1 | 401.2 | 138.3 |
| time over the response line (% of samples) | 1.018 | 0.8786 | 1.039 | 0.9759 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0.8 | 1 | 0.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 18.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1283 | 0.07833 | 0 | 0.3483 |
| utilisation (used / allocatable) | 0.03405 | 0.03403 | 0.03385 | 0.03369 | 0.03294 |
| CPU used (cores), mean | 0.8171 | 0.8168 | 0.8125 | 0.8085 | 0.7907 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00829 |
| CPU used with Omni's own (cores), mean | 0.8171 | 0.8168 | 0.8125 | 0.8085 | 0.799 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.1 | 805.4 | 811.4 | 814.4 | 823.8 |
| HPA replicas, mean | 8.189 | 8.831 | 9.365 | 9.854 | 7.874 |
| pods started | 5.7 | 5 | 3.2 | 1.4 | 5.3 |
| pod start wait, total (s) | 8 | 7.3 | 5.4 | 2 | 8.7 |
| pod start wait, mean (s) | 1.413 | 1.425 | 1.513 | 0.675 | 1.648 |
| host CPU busy, the real machine under kind (%) | 25.56 | 25.33 | 25.26 | 25.18 | 25.05 |
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
| node-hours | 1.517 | 1.519 | +0.1% | +0.0005345 to +0.003466 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.3 | +0.0% | -0.3332 to +0.351 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.3 | +0.0% | -0.3332 to +0.351 | no |
| response time (ms), mean | 127.4 | 69.64 | -45.3% | -78.87 to -36.64 | yes: GAIN |
| response time (ms), 95th percentile | 275.1 | 100.8 | -63.3% | -228.9 to -119.6 | yes: GAIN |
| response time (ms), 99th percentile | 422.8 | 138.3 | -67.3% | -375.5 to -193.5 | yes: GAIN |
| time over the response line (% of samples) | 1.018 | 0 | -100.0% | -1.998 to -0.03697 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0 | -100.0% | -1.99 to +0.19 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.7 (native is 0) | +17.08 to +20.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.3483 | +226.6% | -0.002867 to +0.4862 | no |
| utilisation (used / allocatable) | 0.03405 | 0.03294 | -3.2% | -0.002259 to +5.285e-05 | no |
| CPU used (cores), mean | 0.8171 | 0.7907 | -3.2% | -0.05422 to +0.001268 | no |
| Omni's own CPU (cores), mean | 0 | 0.00829 | +0.00829 (native is 0) | +0.007332 to +0.009248 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8171 | 0.799 | -2.2% | -0.04534 to +0.008969 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.1 | 823.8 | +1.9% | -2.56 to +33.9 | no |
| HPA replicas, mean | 8.189 | 7.874 | -3.8% | -0.5393 to -0.09106 | yes: GAIN |
| pods started | 5.7 | 5.3 | -7.0% | -1.003 to +0.2032 | no |
| pod start wait, total (s) | 8 | 8.7 | +8.7% | -1.662 to +3.062 | no |
| pod start wait, mean (s) | 1.413 | 1.648 | +16.6% | -0.1587 to +0.6287 | no |
| host CPU busy, the real machine under kind (%) | 25.56 | 25.05 | -2.0% | -1.126 to +0.1179 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 275.1 | 422.8 | 8.189 | 0.8171 | 6 |
| Native tuned, HPA target 40 | 260.2 | 423.7 | 8.831 | 0.8168 | 6 |
| Native tuned, HPA target 30 | 261.8 | 430.1 | 9.365 | 0.8125 | 6 |
| Native tuned, HPA target 20 | 251.7 | 401.2 | 9.854 | 0.8085 | 6 |
| omni | 100.8 | 138.3 | 7.874 | 0.799 | 6 |

- omni (p95 100.8 ms): no native setting tried reached it; the lowest native p95 is 251.7 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*