# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 516.4 | 514.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.4 | 514.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 282.5 | 164.2 |
| response time (ms), 95th percentile | 768 | 344.9 |
| response time (ms), 99th percentile | 2648 | 2014 |
| time over the response line (% of samples) | 19.49 | 11.7 |
| failed requests (%) | 10.91 | 9.28 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.2 | 20.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.64 | 0.2917 |
| utilisation (used / allocatable) | 0.101 | 0.09832 |
| CPU used (cores), mean | 2.425 | 2.36 |
| Omni's own CPU (cores), mean | 0 | 0.00869 |
| CPU used with Omni's own (cores), mean | 2.425 | 2.368 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.1 | 319.1 |
| HPA replicas, mean | 9.382 | 9.276 |
| pods started | 5.6 | 5.4 |
| pod start wait, total (s) | 9.6 | 8.8 |
| pod start wait, mean (s) | 1.726 | 1.576 |
| host CPU busy, the real machine under kind (%) | 68.48 | 67.09 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.588e-16 to +1.014e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.513 | -0.0% | -0.004403 to +0.00307 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516.4 | 514.5 | -0.4% | -2.387 to -1.231 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.4 | 514.5 | -0.4% | -2.387 to -1.231 | yes: GAIN |
| response time (ms), mean | 282.5 | 164.2 | -41.9% | -152.4 to -84.24 | yes: GAIN |
| response time (ms), 95th percentile | 768 | 344.9 | -55.1% | -538.6 to -307.5 | yes: GAIN |
| response time (ms), 99th percentile | 2648 | 2014 | -23.9% | -1638 to +370.8 | no |
| time over the response line (% of samples) | 19.49 | 11.7 | -40.0% | -10.91 to -4.67 | yes: GAIN |
| failed requests (%) | 10.91 | 9.28 | -15.0% | -2.603 to -0.6634 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.2 | 20.3 | -25.4% | -8.699 to -5.101 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.5 (native is 0) | +21.57 to +39.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.64 | 0.2917 | -54.4% | -0.8526 to +0.1559 | no |
| utilisation (used / allocatable) | 0.101 | 0.09832 | -2.7% | -0.003116 to -0.002332 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.425 | 2.36 | -2.7% | -0.07479 to -0.05598 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00869 | +0.00869 (native is 0) | +0.007274 to +0.01011 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.425 | 2.368 | -2.3% | -0.06659 to -0.04679 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.1 | 319.1 | +3.2% | +3.738 to +16.17 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.382 | 9.276 | -1.1% | -0.5474 to +0.3352 | no |
| pods started | 5.6 | 5.4 | -3.6% | -2.354 to +1.954 | no |
| pod start wait, total (s) | 9.6 | 8.8 | -8.3% | -4.715 to +3.115 | no |
| pod start wait, mean (s) | 1.726 | 1.576 | -8.7% | -0.3915 to +0.09242 | no |
| host CPU busy, the real machine under kind (%) | 68.48 | 67.09 | -2.0% | -1.604 to -1.174 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 21.0 |  |  | 10 |
| compass | 31.8 | +51.4% | +8.1 to +13.5 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*