# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.512 | 1.512 | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.8 | 158.8 | 158.9 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.8 | 158.8 | 158.9 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 151.5 | 149.3 | 147.4 | 147.6 | 78.39 |
| response time (ms), 95th percentile | 340.6 | 345 | 322.4 | 327.8 | 116.2 |
| response time (ms), 99th percentile | 550.7 | 532.2 | 537.6 | 527.2 | 158.4 |
| time over the response line (% of samples) | 2.253 | 2.238 | 1.867 | 1.906 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 2.4 | 1.8 | 2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 18.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.205 | 0.05333 | 0.08167 | 0.07833 | 0.2917 |
| utilisation (used / allocatable) | 0.03856 | 0.03813 | 0.03826 | 0.03843 | 0.0366 |
| CPU used (cores), mean | 0.9253 | 0.9152 | 0.9181 | 0.9224 | 0.8783 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00811 |
| CPU used with Omni's own (cores), mean | 0.9253 | 0.9152 | 0.9181 | 0.9224 | 0.8864 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 719.6 | 724.2 | 720.9 | 719.8 | 746.6 |
| HPA replicas, mean | 8.516 | 8.932 | 9.564 | 9.91 | 8.27 |
| pods started | 5.2 | 4.8 | 2.7 | 0.4 | 4.6 |
| pod start wait, total (s) | 8.8 | 6.9 | 3.7 | 0.6 | 6.9 |
| pod start wait, mean (s) | 1.686 | 1.453 | 1.207 | 0.2667 | 1.565 |
| host CPU busy, the real machine under kind (%) | 27.84 | 27.74 | 27.83 | 27.89 | 26.97 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.146e-15 to +9.679e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.513 | +0.1% | -1.933e-05 to +0.003353 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.5 | -0.1% | -0.5363 to +0.07528 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.5 | -0.1% | -0.5363 to +0.07528 | no |
| response time (ms), mean | 151.5 | 78.39 | -48.3% | -96.56 to -49.72 | yes: GAIN |
| response time (ms), 95th percentile | 340.6 | 116.2 | -65.9% | -292 to -156.8 | yes: GAIN |
| response time (ms), 99th percentile | 550.7 | 158.4 | -71.2% | -523.3 to -261.3 | yes: GAIN |
| time over the response line (% of samples) | 2.253 | 0 | -100.0% | -3.723 to -0.784 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | -100.0% | -3.348 to -0.4516 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.7 (native is 0) | +16.82 to +20.58 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.205 | 0.2917 | +42.3% | -0.1931 to +0.3664 | no |
| utilisation (used / allocatable) | 0.03856 | 0.0366 | -5.1% | -0.002965 to -0.0009567 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9253 | 0.8783 | -5.1% | -0.07116 to -0.02296 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00811 | +0.00811 (native is 0) | +0.007008 to +0.009212 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9253 | 0.8864 | -4.2% | -0.06209 to -0.01581 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 719.6 | 746.6 | +3.8% | +11.77 to +42.25 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.516 | 8.27 | -2.9% | -0.5624 to +0.07094 | no |
| pods started | 5.2 | 4.6 | -11.5% | -1.778 to +0.5778 | no |
| pod start wait, total (s) | 8.8 | 6.9 | -21.6% | -4.173 to +0.3733 | no |
| pod start wait, mean (s) | 1.686 | 1.565 | -7.1% | -0.5056 to +0.2647 | no |
| host CPU busy, the real machine under kind (%) | 27.84 | 26.97 | -3.1% | -1.548 to -0.2019 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 340.6 | 550.7 | 8.516 | 0.9253 | 6 |
| Native tuned, HPA target 40 | 345 | 532.2 | 8.932 | 0.9152 | 6 |
| Native tuned, HPA target 30 | 322.4 | 537.6 | 9.564 | 0.9181 | 6 |
| Native tuned, HPA target 20 | 327.8 | 527.2 | 9.91 | 0.9224 | 6 |
| omni | 116.2 | 158.4 | 8.27 | 0.8864 | 6 |

- omni (p95 116.2 ms): no native setting tried reached it; the lowest native p95 is 322.4 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*