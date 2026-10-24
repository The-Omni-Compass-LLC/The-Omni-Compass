# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.4 | 516.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.4 | 516.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 286.7 | 170.7 |
| response time (ms), 95th percentile | 767.9 | 350.1 |
| response time (ms), 99th percentile | 2760 | 2089 |
| time over the response line (% of samples) | 19.16 | 12.63 |
| failed requests (%) | 10.33 | 10.01 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 22.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.4367 |
| utilisation (used / allocatable) | 0.1028 | 0.102 |
| CPU used (cores), mean | 2.467 | 2.448 |
| Omni's own CPU (cores), mean | 0 | 0.00836 |
| CPU used with Omni's own (cores), mean | 2.467 | 2.456 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 297.8 | 302.8 |
| HPA replicas, mean | 9.453 | 10.11 |
| pods started | 5.5 | 7.1 |
| pod start wait, total (s) | 7.6 | 11 |
| pod start wait, mean (s) | 1.374 | 1.565 |
| host CPU busy, the real machine under kind (%) | 69.12 | 68.98 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.407e-15 to -3.694e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.509 | -0.1% | -0.009681 to +0.004681 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.4 | 516.7 | -0.1% | -1.984 to +0.5378 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.4 | 516.7 | -0.1% | -1.984 to +0.5378 | no |
| response time (ms), mean | 286.7 | 170.7 | -40.5% | -152.2 to -79.94 | yes: GAIN |
| response time (ms), 95th percentile | 767.9 | 350.1 | -54.4% | -543.1 to -292.5 | yes: GAIN |
| response time (ms), 99th percentile | 2760 | 2089 | -24.3% | -1952 to +609.1 | no |
| time over the response line (% of samples) | 19.16 | 12.63 | -34.1% | -8.837 to -4.237 | yes: GAIN |
| failed requests (%) | 10.33 | 10.01 | -3.1% | -1.155 to +0.5209 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 22.3 | -20.6% | -8.677 to -2.923 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.6 | +35.6 (native is 0) | +26.19 to +45.01 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.4367 | -9.7% | -0.5549 to +0.4615 | no |
| utilisation (used / allocatable) | 0.1028 | 0.102 | -0.8% | -0.002771 to +0.001135 | no |
| CPU used (cores), mean | 2.467 | 2.448 | -0.8% | -0.06651 to +0.02724 | no |
| Omni's own CPU (cores), mean | 0 | 0.00836 | +0.00836 (native is 0) | +0.007103 to +0.009617 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.467 | 2.456 | -0.5% | -0.059 to +0.03645 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 297.8 | 302.8 | +1.7% | -3.009 to +13.05 | no |
| HPA replicas, mean | 9.453 | 10.11 | +6.9% | -0.1351 to +1.442 | no |
| pods started | 5.5 | 7.1 | +29.1% | -0.4006 to +3.601 | no |
| pod start wait, total (s) | 7.6 | 11 | +44.7% | -0.2035 to +7.003 | no |
| pod start wait, mean (s) | 1.374 | 1.565 | +13.9% | +0.03285 to +0.3491 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 69.12 | 68.98 | -0.2% | -1.469 to +1.184 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.2 |  |  | 10 |
| compass | 29.4 | +53.1% | +6.1 to +14.3 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*