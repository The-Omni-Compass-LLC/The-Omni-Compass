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
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 523.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 523.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 324.8 | 184.1 |
| response time (ms), 95th percentile | 883.5 | 395.1 |
| response time (ms), 99th percentile | 2970 | 2311 |
| time over the response line (% of samples) | 22.94 | 14.85 |
| failed requests (%) | 12.76 | 11.59 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.6 | 27.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.4433 |
| utilisation (used / allocatable) | 0.1129 | 0.1116 |
| CPU used (cores), mean | 2.71 | 2.679 |
| Omni's own CPU (cores), mean | 0 | 0.00915 |
| CPU used with Omni's own (cores), mean | 2.71 | 2.688 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 259.8 | 262.7 |
| HPA replicas, mean | 9.624 | 10.42 |
| pods started | 4.4 | 7.7 |
| pod start wait, total (s) | 14.3 | 19.5 |
| pod start wait, mean (s) | 2.887 | 2.319 |
| host CPU busy, the real machine under kind (%) | 75.82 | 75.42 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.066e-16 to +9.395e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.512 | +0.0% | -0.008388 to +0.009054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.2 | 523.5 | -0.1% | -1.999 to +0.7046 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.2 | 523.5 | -0.1% | -1.999 to +0.7046 | no |
| response time (ms), mean | 324.8 | 184.1 | -43.3% | -164.8 to -116.7 | yes: GAIN |
| response time (ms), 95th percentile | 883.5 | 395.1 | -55.3% | -560.7 to -416.1 | yes: GAIN |
| response time (ms), 99th percentile | 2970 | 2311 | -22.2% | -1693 to +375.7 | no |
| time over the response line (% of samples) | 22.94 | 14.85 | -35.2% | -9.421 to -6.751 | yes: GAIN |
| failed requests (%) | 12.76 | 11.59 | -9.1% | -1.938 to -0.3894 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 32.6 | 27.1 | -16.9% | -7.502 to -3.498 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.2 | +43.2 (native is 0) | +34.75 to +51.65 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.4433 | +64.2% | -0.2009 to +0.5476 | no |
| utilisation (used / allocatable) | 0.1129 | 0.1116 | -1.1% | -0.002382 to -0.0001703 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.71 | 2.679 | -1.1% | -0.05718 to -0.004086 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00915 | +0.00915 (native is 0) | +0.00823 to +0.01007 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.71 | 2.688 | -0.8% | -0.04858 to +0.005614 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 259.8 | 262.7 | +1.1% | +0.8092 to +4.954 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.624 | 10.42 | +8.3% | -0.2389 to +1.832 | no |
| pods started | 4.4 | 7.7 | +75.0% | +0.8907 to +5.709 | yes: power given |
| pod start wait, total (s) | 14.3 | 19.5 | +36.4% | -1.684 to +12.08 | no |
| pod start wait, mean (s) | 2.887 | 2.319 | -19.7% | -1.22 to +0.084 | no |
| host CPU busy, the real machine under kind (%) | 75.82 | 75.42 | -0.5% | -1.213 to +0.4095 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 15.6 |  |  | 10 |
| compass | 25.2 | +61.5% | +6.6 to +12.6 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*