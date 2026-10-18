# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 520.6 | 520.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 520.6 | 520.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 291.1 | 167.3 |
| response time (ms), 95th percentile | 762.5 | 337.5 |
| response time (ms), 99th percentile | 2533 | 1578 |
| time over the response line (% of samples) | 21.74 | 14.15 |
| failed requests (%) | 12.83 | 11.64 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.9 | 24.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3817 | 0.3467 |
| utilisation (used / allocatable) | 0.1076 | 0.1066 |
| CPU used (cores), mean | 2.581 | 2.559 |
| Omni's own CPU (cores), mean | 0 | 0.00895 |
| CPU used with Omni's own (cores), mean | 2.581 | 2.568 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.1 | 287.4 |
| HPA replicas, mean | 9.559 | 9.68 |
| pods started | 4 | 5.7 |
| pod start wait, total (s) | 12.8 | 13.8 |
| pod start wait, mean (s) | 2.678 | 2.054 |
| host CPU busy, the real machine under kind (%) | 72.57 | 72.26 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.449e-15 to +5.604e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.511 | -0.0% | -0.007676 to +0.006676 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 520.6 | 520.1 | -0.1% | -2.01 to +1.016 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 520.6 | 520.1 | -0.1% | -2.01 to +1.016 | no |
| response time (ms), mean | 291.1 | 167.3 | -42.5% | -157.3 to -90.33 | yes: GAIN |
| response time (ms), 95th percentile | 762.5 | 337.5 | -55.7% | -536.7 to -313.4 | yes: GAIN |
| response time (ms), 99th percentile | 2533 | 1578 | -37.7% | -1868 to -42.82 | yes: GAIN |
| time over the response line (% of samples) | 21.74 | 14.15 | -34.9% | -10.41 to -4.77 | yes: GAIN |
| failed requests (%) | 12.83 | 11.64 | -9.3% | -2.09 to -0.2961 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.9 | 24.4 | -18.4% | -6.727 to -4.273 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.5 | +34.5 (native is 0) | +25.84 to +43.16 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3817 | 0.3467 | -9.2% | -0.2518 to +0.1818 | no |
| utilisation (used / allocatable) | 0.1076 | 0.1066 | -0.9% | -0.002212 to +0.0003682 | no |
| CPU used (cores), mean | 2.581 | 2.559 | -0.9% | -0.05309 to +0.008836 | no |
| Omni's own CPU (cores), mean | 0 | 0.00895 | +0.00895 (native is 0) | +0.00767 to +0.01023 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.581 | 2.568 | -0.5% | -0.04368 to +0.01732 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.1 | 287.4 | +0.5% | -2.261 to +4.898 | no |
| HPA replicas, mean | 9.559 | 9.68 | +1.3% | -0.416 to +0.6587 | no |
| pods started | 4 | 5.7 | +42.5% | -0.5633 to +3.963 | no |
| pod start wait, total (s) | 12.8 | 13.8 | +7.8% | -6.418 to +8.418 | no |
| pod start wait, mean (s) | 2.678 | 2.054 | -23.3% | -1.26 to +0.01147 | no |
| host CPU busy, the real machine under kind (%) | 72.57 | 72.26 | -0.4% | -1.061 to +0.4391 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 18.0 |  |  | 10 |
| compass | 27.6 | +53.3% | +7.4 to +11.8 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*