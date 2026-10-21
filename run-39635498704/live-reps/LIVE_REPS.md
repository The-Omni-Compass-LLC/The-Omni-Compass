# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.512 | 1.52 | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 157.9 | 158.8 | 158.5 | 158.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 157.9 | 158.8 | 158.5 | 158.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 132.7 | 128.5 | 126 | 126 | 71.66 |
| response time (ms), 95th percentile | 303.5 | 286.1 | 280.2 | 285.2 | 108.5 |
| response time (ms), 99th percentile | 492.1 | 483.1 | 440.4 | 440.4 | 145.4 |
| time over the response line (% of samples) | 1.837 | 1.778 | 1.793 | 1.705 | 0.02439 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 2.1 | 1.6 | 1.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 16.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2617 | 0.1583 | 0.1317 | 0.08 | 0.3217 |
| utilisation (used / allocatable) | 0.03501 | 0.03431 | 0.03447 | 0.03489 | 0.03359 |
| CPU used (cores), mean | 0.8402 | 0.8234 | 0.8272 | 0.8373 | 0.8063 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.00782 |
| CPU used with Omni's own (cores), mean | 0.8402 | 0.8234 | 0.8272 | 0.8373 | 0.8141 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.9 | 845.2 | 836.1 | 832.3 | 858.4 |
| HPA replicas, mean | 8.004 | 8.608 | 9.271 | 9.697 | 7.779 |
| pods started | 5.3 | 5.2 | 3.5 | 1.6 | 4.6 |
| pod start wait, total (s) | 7.8 | 7.5 | 4.7 | 1.9 | 6.4 |
| pod start wait, mean (s) | 1.47 | 1.486 | 1.373 | 0.625 | 1.415 |
| host CPU busy, the real machine under kind (%) | 25.62 | 25.14 | 25.27 | 25.55 | 24.87 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.516 | +0.1% | -0.01147 to +0.01314 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | -0.1% | -1.38 to +1.008 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | -0.1% | -1.38 to +1.008 | no |
| response time (ms), mean | 132.7 | 71.66 | -46.0% | -88.31 to -33.68 | yes: GAIN |
| response time (ms), 95th percentile | 303.5 | 108.5 | -64.2% | -267.7 to -122.3 | yes: GAIN |
| response time (ms), 99th percentile | 492.1 | 145.4 | -70.5% | -489.2 to -204.3 | yes: GAIN |
| time over the response line (% of samples) | 1.837 | 0.02439 | -98.7% | -3.193 to -0.4314 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 0 | -100.0% | -3.801 to -0.3989 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.7 | +16.7 (native is 0) | +15.08 to +18.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2617 | 0.3217 | +22.9% | -0.3104 to +0.4304 | no |
| utilisation (used / allocatable) | 0.03501 | 0.03359 | -4.0% | -0.002358 to -0.0004689 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8402 | 0.8063 | -4.0% | -0.0566 to -0.01125 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00782 | +0.00782 (native is 0) | +0.006535 to +0.009105 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8402 | 0.8141 | -3.1% | -0.04834 to -0.003878 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825.9 | 858.4 | +3.9% | +11.41 to +53.74 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.004 | 7.779 | -2.8% | -0.6106 to +0.1608 | no |
| pods started | 5.3 | 4.6 | -13.2% | -1.821 to +0.4209 | no |
| pod start wait, total (s) | 7.8 | 6.4 | -17.9% | -4.245 to +1.445 | no |
| pod start wait, mean (s) | 1.47 | 1.415 | -3.7% | -0.4366 to +0.3275 | no |
| host CPU busy, the real machine under kind (%) | 25.62 | 24.87 | -2.9% | -1.401 to -0.0816 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 303.5 | 492.1 | 8.004 | 0.8402 | 6 |
| Native tuned, HPA target 40 | 286.1 | 483.1 | 8.608 | 0.8234 | 6 |
| Native tuned, HPA target 30 | 280.2 | 440.4 | 9.271 | 0.8272 | 6 |
| Native tuned, HPA target 20 | 285.2 | 440.4 | 9.697 | 0.8373 | 6 |
| omni | 108.5 | 145.4 | 7.779 | 0.8141 | 6 |

- omni (p95 108.5 ms): no native setting tried reached it; the lowest native p95 is 280.2 ms (Native tuned, HPA target 30).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*