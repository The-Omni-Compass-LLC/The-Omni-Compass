# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 523.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 523.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 326.3 | 185 |
| response time (ms), 95th percentile | 882.8 | 369.9 |
| response time (ms), 99th percentile | 3036 | 2349 |
| time over the response line (% of samples) | 23.62 | 14.46 |
| failed requests (%) | 13.31 | 11.39 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 34 | 27 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.2467 |
| utilisation (used / allocatable) | 0.1133 | 0.111 |
| CPU used (cores), mean | 2.718 | 2.665 |
| Omni's own CPU (cores), mean | 0 | 0.00929 |
| CPU used with Omni's own (cores), mean | 2.718 | 2.674 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 260.1 | 264.8 |
| HPA replicas, mean | 9.537 | 9.855 |
| pods started | 5.4 | 6.7 |
| pod start wait, total (s) | 9.7 | 11.8 |
| pod start wait, mean (s) | 1.807 | 1.609 |
| host CPU busy, the real machine under kind (%) | 76.11 | 75.08 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.513 | -0.0% | -0.005976 to +0.005309 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.6 | 523.2 | -0.3% | -1.952 to -0.7577 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.6 | 523.2 | -0.3% | -1.952 to -0.7577 | yes: GAIN |
| response time (ms), mean | 326.3 | 185 | -43.3% | -162.8 to -119.8 | yes: GAIN |
| response time (ms), 95th percentile | 882.8 | 369.9 | -58.1% | -600.9 to -424.8 | yes: GAIN |
| response time (ms), 99th percentile | 3036 | 2349 | -22.6% | -1307 to -66.79 | yes: GAIN |
| time over the response line (% of samples) | 23.62 | 14.46 | -38.8% | -10.53 to -7.783 | yes: GAIN |
| failed requests (%) | 13.31 | 11.39 | -14.5% | -2.686 to -1.164 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 34 | 27 | -20.6% | -8.066 to -5.934 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.2 | +38.2 (native is 0) | +31.19 to +45.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.2467 | -46.6% | -0.6985 to +0.2685 | no |
| utilisation (used / allocatable) | 0.1133 | 0.111 | -2.0% | -0.002888 to -0.001583 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.718 | 2.665 | -2.0% | -0.06932 to -0.038 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00929 | +0.00929 (native is 0) | +0.008451 to +0.01013 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.718 | 2.674 | -1.6% | -0.05975 to -0.02899 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 260.1 | 264.8 | +1.8% | +3.194 to +6.162 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.537 | 9.855 | +3.3% | +0.08277 to +0.5543 | yes: power given |
| pods started | 5.4 | 6.7 | +24.1% | -1.42 to +4.02 | no |
| pod start wait, total (s) | 9.7 | 11.8 | +21.6% | -4.773 to +8.973 | no |
| pod start wait, mean (s) | 1.807 | 1.609 | -10.9% | -0.7245 to +0.3291 | no |
| host CPU busy, the real machine under kind (%) | 76.11 | 75.08 | -1.4% | -1.351 to -0.7129 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 14.4 |  |  | 10 |
| compass | 24.6 | +70.8% | +8.1 to +12.3 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*