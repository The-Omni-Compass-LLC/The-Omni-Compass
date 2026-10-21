# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.517 | 1.519 | 1.516 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 159.8 | 160 | 159.6 | 159.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 159.8 | 160 | 159.6 | 159.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 165.7 | 162.2 | 158.4 | 160 | 83.7 |
| response time (ms), 95th percentile | 375.4 | 359.2 | 361.9 | 363.7 | 127.7 |
| response time (ms), 99th percentile | 648 | 595 | 578.2 | 599.8 | 171.7 |
| time over the response line (% of samples) | 3.024 | 2.345 | 2.676 | 2.516 | 0.0241 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 2.8 | 2.6 | 2.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 17.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.08167 | 0.08 | 0 | 0.5217 |
| utilisation (used / allocatable) | 0.0403 | 0.04055 | 0.04042 | 0.04027 | 0.03824 |
| CPU used (cores), mean | 0.9671 | 0.9732 | 0.9702 | 0.9665 | 0.9177 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00848 |
| CPU used with Omni's own (cores), mean | 0.9671 | 0.9732 | 0.9702 | 0.9665 | 0.9261 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.7 | 699 | 703.4 | 703.6 | 731.5 |
| HPA replicas, mean | 8.536 | 9.014 | 9.554 | 9.898 | 8.457 |
| pods started | 4.7 | 4.2 | 2.6 | 0.6 | 3.4 |
| pod start wait, total (s) | 7.3 | 6.5 | 3.7 | 0.7 | 5.5 |
| pod start wait, mean (s) | 1.51 | 1.59 | 1.43 | 0.225 | 1.38 |
| host CPU busy, the real machine under kind (%) | 29.11 | 29.24 | 29.04 | 28.96 | 28.08 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.615e-16 to +4.062e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.52 | +0.2% | -0.002276 to +0.009609 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 159.7 | -0.0% | -0.6791 to +0.5451 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 159.7 | -0.0% | -0.6791 to +0.5451 | no |
| response time (ms), mean | 165.7 | 83.7 | -49.5% | -105.9 to -58.1 | yes: GAIN |
| response time (ms), 95th percentile | 375.4 | 127.7 | -66.0% | -317.3 to -177.9 | yes: GAIN |
| response time (ms), 99th percentile | 648 | 171.7 | -73.5% | -608.9 to -343.6 | yes: GAIN |
| time over the response line (% of samples) | 3.024 | 0.0241 | -99.2% | -4.247 to -1.753 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 0 | -100.0% | -4.772 to -1.828 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.1 (native is 0) | +15.54 to +18.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.5217 | +552.1% | +0.07818 to +0.8052 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0403 | 0.03824 | -5.1% | -0.002987 to -0.001131 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9671 | 0.9177 | -5.1% | -0.07169 to -0.02716 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00848 | +0.00848 (native is 0) | +0.007194 to +0.009766 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9671 | 0.9261 | -4.2% | -0.06204 to -0.01985 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.7 | 731.5 | +3.8% | +12.19 to +41.4 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.536 | 8.457 | -0.9% | -0.3817 to +0.2227 | no |
| pods started | 4.7 | 3.4 | -27.7% | -2.369 to -0.231 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 5.5 | -24.7% | -4.227 to +0.6269 | no |
| pod start wait, mean (s) | 1.51 | 1.38 | -8.6% | -0.5532 to +0.2932 | no |
| host CPU busy, the real machine under kind (%) | 29.11 | 28.08 | -3.5% | -1.553 to -0.5019 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 375.4 | 648 | 8.536 | 0.9671 | 6 |
| Native tuned, HPA target 40 | 359.2 | 595 | 9.014 | 0.9732 | 6 |
| Native tuned, HPA target 30 | 361.9 | 578.2 | 9.554 | 0.9702 | 6 |
| Native tuned, HPA target 20 | 363.7 | 599.8 | 9.898 | 0.9665 | 6 |
| omni | 127.7 | 171.7 | 8.457 | 0.9261 | 6 |

- omni (p95 127.7 ms): no native setting tried reached it; the lowest native p95 is 359.2 ms (Native tuned, HPA target 40).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*