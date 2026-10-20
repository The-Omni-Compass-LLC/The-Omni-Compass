# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 519.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 519.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 313.5 | 161.3 |
| response time (ms), 95th percentile | 855.1 | 324.6 |
| response time (ms), 99th percentile | 3299 | 1636 |
| time over the response line (% of samples) | 22.85 | 13.43 |
| failed requests (%) | 12.85 | 11.13 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.1 | 23.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5733 | 0.4317 |
| utilisation (used / allocatable) | 0.1083 | 0.105 |
| CPU used (cores), mean | 2.598 | 2.521 |
| Omni's own CPU (cores), mean | 0 | 0.00915 |
| CPU used with Omni's own (cores), mean | 2.598 | 2.53 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 283.9 | 294.3 |
| HPA replicas, mean | 9.508 | 9.588 |
| pods started | 5.2 | 7 |
| pod start wait, total (s) | 7.9 | 11.1 |
| pod start wait, mean (s) | 1.526 | 1.528 |
| host CPU busy, the real machine under kind (%) | 72.82 | 71.16 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | no |
| node-hours | 4.514 | 4.515 | +0.0% | -0.005881 to +0.008548 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 519.4 | -0.4% | -3.119 to -0.536 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 519.4 | -0.4% | -3.119 to -0.536 | yes: GAIN |
| response time (ms), mean | 313.5 | 161.3 | -48.6% | -199.4 to -105 | yes: GAIN |
| response time (ms), 95th percentile | 855.1 | 324.6 | -62.0% | -669.9 to -391.1 | yes: GAIN |
| response time (ms), 99th percentile | 3299 | 1636 | -50.4% | -3043 to -281.9 | yes: GAIN |
| time over the response line (% of samples) | 22.85 | 13.43 | -41.2% | -12.2 to -6.625 | yes: GAIN |
| failed requests (%) | 12.85 | 11.13 | -13.4% | -2.658 to -0.7757 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.1 | 23.9 | -23.2% | -8.978 to -5.422 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36 | +36 (native is 0) | +25.87 to +46.13 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5733 | 0.4317 | -24.7% | -0.6243 to +0.341 | no |
| utilisation (used / allocatable) | 0.1083 | 0.105 | -3.0% | -0.004429 to -0.002014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.598 | 2.521 | -3.0% | -0.1063 to -0.04834 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00915 | +0.00915 (native is 0) | +0.007774 to +0.01053 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.598 | 2.53 | -2.6% | -0.09773 to -0.0386 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 283.9 | 294.3 | +3.7% | +0.9075 to +19.9 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.508 | 9.588 | +0.8% | -0.2146 to +0.3746 | no |
| pods started | 5.2 | 7 | +34.6% | -0.0096 to +3.61 | no |
| pod start wait, total (s) | 7.9 | 11.1 | +40.5% | +0.004605 to +6.395 | yes: LOSS |
| pod start wait, mean (s) | 1.526 | 1.528 | +0.1% | -0.3007 to +0.3045 | no |
| host CPU busy, the real machine under kind (%) | 72.82 | 71.16 | -2.3% | -2.414 to -0.8913 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 17.4 |  |  | 10 |
| compass | 27.0 | +55.2% | +6.6 to +12.6 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*