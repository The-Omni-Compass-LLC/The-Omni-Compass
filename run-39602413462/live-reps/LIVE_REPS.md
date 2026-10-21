# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 523.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 523.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 338.1 | 180.5 |
| response time (ms), 95th percentile | 930.4 | 374.3 |
| response time (ms), 99th percentile | 3460 | 1776 |
| time over the response line (% of samples) | 22.96 | 13.59 |
| failed requests (%) | 12.19 | 10.92 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 33.3 | 25.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 1.035 |
| utilisation (used / allocatable) | 0.1123 | 0.1109 |
| CPU used (cores), mean | 2.696 | 2.66 |
| Omni's own CPU (cores), mean | 0 | 0.00959 |
| CPU used with Omni's own (cores), mean | 2.696 | 2.67 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 261 | 263.9 |
| HPA replicas, mean | 9.589 | 10.09 |
| pods started | 5 | 7.2 |
| pod start wait, total (s) | 8.4 | 14.4 |
| pod start wait, mean (s) | 1.64 | 1.804 |
| host CPU busy, the real machine under kind (%) | 75.37 | 74.75 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.33e-15 to +9.745e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.516 | +0.1% | -0.003301 to +0.009635 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 523.4 | -0.1% | -1.026 to -0.006786 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 523.4 | -0.1% | -1.026 to -0.006786 | yes: GAIN |
| response time (ms), mean | 338.1 | 180.5 | -46.6% | -179.5 to -135.7 | yes: GAIN |
| response time (ms), 95th percentile | 930.4 | 374.3 | -59.8% | -628.3 to -483.7 | yes: GAIN |
| response time (ms), 99th percentile | 3460 | 1776 | -48.7% | -2401 to -966.5 | yes: GAIN |
| time over the response line (% of samples) | 22.96 | 13.59 | -40.8% | -10.77 to -7.982 | yes: GAIN |
| failed requests (%) | 12.19 | 10.92 | -10.4% | -1.91 to -0.626 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 33.3 | 25.9 | -22.2% | -8.366 to -6.434 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 | +47.7 (native is 0) | +40.38 to +55.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 1.035 | +195.7% | -0.1794 to +1.549 | no |
| utilisation (used / allocatable) | 0.1123 | 0.1109 | -1.3% | -0.002237 to -0.0007129 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.696 | 2.66 | -1.3% | -0.05368 to -0.01711 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00959 | +0.00959 (native is 0) | +0.008696 to +0.01048 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.696 | 2.67 | -1.0% | -0.04371 to -0.0079 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 261 | 263.9 | +1.1% | +1.623 to +4.202 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.589 | 10.09 | +5.3% | +0.2483 to +0.7623 | yes: power given |
| pods started | 5 | 7.2 | +44.0% | -0.1313 to +4.531 | no |
| pod start wait, total (s) | 8.4 | 14.4 | +71.4% | -1.033 to +13.03 | no |
| pod start wait, mean (s) | 1.64 | 1.804 | +10.0% | -0.3876 to +0.7151 | no |
| host CPU busy, the real machine under kind (%) | 75.37 | 74.75 | -0.8% | -0.9852 to -0.2596 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 14.4 |  |  | 10 |
| compass | 26.4 | +83.3% | +9.1 to +14.9 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*