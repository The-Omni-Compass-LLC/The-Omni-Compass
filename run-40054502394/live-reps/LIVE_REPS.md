# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.596 | 5.739 |
| node-hours | 2.517 | 2.518 | 2.346 | 2.4 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.4 | 273.2 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.4 | 260.4 | 264.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 357.3 | 422.3 | 327.9 | 361.6 |
| response time (ms), 95th percentile | 1172 | 1790 | 1261 | 1667 |
| response time (ms), 99th percentile | 1694 | 2818 | 1838 | 2781 |
| time over the response line (% of samples) | 21.8 | 17.53 | 22.04 | 16.92 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.3 | 11.6 | 11.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 34.8 | 43.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.11 | 17.07 | 11.19 | 17.86 |
| utilisation (used / allocatable) | 0.06167 | 0.06163 | 0.06645 | 0.0651 |
| CPU used (cores), mean | 1.48 | 1.479 | 1.485 | 1.494 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01708 | 0.01821 |
| CPU used with Omni's own (cores), mean | 1.48 | 1.479 | 1.502 | 1.513 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.8 | 444.7 | 419.7 | 424.8 |
| HPA replicas, mean | 1.995 | 2.076 | 2.451 | 2.386 |
| pods started | 0 | 0.2 | 0.4 | 0.8 |
| pod start wait, total (s) | 0 | 0.4 | 1.2 | 1.2 |
| pod start wait, mean (s) | 0 | 0.4 | 1.2 | 0.8667 |
| host CPU busy, the real machine under kind (%) | 42.11 | 44.79 | 43.28 | 45.59 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 771 | 812.6 | 779.3 | 811.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.235 | 5.519 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.9125 | 0.06667 | 0.9167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.6 | 0.6 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 80.57 | 125.3 | 86.62 | 121.7 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.739 | -4.3% | -0.6082 to +0.08686 | no |
| node-hours | 2.518 | 2.4 | -4.7% | -0.2595 to +0.02279 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 272.8 | -0.2% | -1.732 to +0.4912 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 264.6 | -3.2% | -19.01 to +1.343 | no |
| response time (ms), mean | 422.3 | 361.6 | -14.4% | -101.5 to -19.98 | yes: GAIN |
| response time (ms), 95th percentile | 1790 | 1667 | -6.9% | -363.2 to +117.5 | no |
| response time (ms), 99th percentile | 2818 | 2781 | -1.3% | -356.2 to +283.2 | no |
| time over the response line (% of samples) | 17.53 | 16.92 | -3.5% | -2.075 to +0.8554 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.4 | +0.9% | -0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.4 | +43.4 (native is 0) | +26.09 to +60.71 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.07 | 17.86 | +4.6% | -0.827 to +2.414 | no |
| utilisation (used / allocatable) | 0.06163 | 0.0651 | +5.6% | -0.0005951 to +0.007523 | no |
| CPU used (cores), mean | 1.479 | 1.494 | +1.0% | -0.01424 to +0.04464 | no |
| Omni's own CPU (cores), mean | 0 | 0.01821 | +0.0182 (native is 0) | +0.01724 to +0.01918 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.513 | +2.3% | +0.003786 to +0.06304 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.7 | 424.8 | -4.5% | -43.14 to +3.293 | no |
| HPA replicas, mean | 2.076 | 2.386 | +14.9% | +0.1489 to +0.4713 | yes: power given |
| pods started | 0.2 | 0.8 | +300.0% | -0.2396 to +1.44 | no |
| pod start wait, total (s) | 0.4 | 1.2 | +200.0% | -0.6621 to +2.262 | no |
| pod start wait, mean (s) | 0.4 | 0.8667 | +116.7% | -0.5889 to +1.522 | no |
| host CPU busy, the real machine under kind (%) | 44.79 | 45.59 | +1.8% | +0.147 to +1.454 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 812.6 | 811.2 | -0.2% | -12.41 to +9.605 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.519 | -8.0% | -1.078 to +0.1155 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9125 | 0.9167 | +0.5% | -0.07336 to +0.0817 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.7 | +6.3% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.3 | 121.7 | -2.8% | -15.75 to +8.646 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.813e-15 to +2.141e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.518 | +0.0% | -0.004846 to +0.006179 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.4 | +0.0% | -0.5462 to +0.6146 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.4 | +0.0% | -0.5462 to +0.6146 | no |
| response time (ms), mean | 357.3 | 422.3 | +18.2% | +12.47 to +117.6 | yes: LOSS |
| response time (ms), 95th percentile | 1172 | 1790 | +52.7% | +261.6 to +973.3 | yes: LOSS |
| response time (ms), 99th percentile | 1694 | 2818 | +66.4% | +577 to +1672 | yes: LOSS |
| time over the response line (% of samples) | 21.8 | 17.53 | -19.6% | -6.179 to -2.356 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.3 | +0.0% | -1.39 to +1.39 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.11 | 17.06 | +53.6% | +4.594 to +7.316 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06167 | 0.06163 | -0.1% | -0.001231 to +0.001146 | no |
| CPU used (cores), mean | 1.48 | 1.479 | -0.1% | -0.02956 to +0.0275 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.48 | 1.479 | -0.1% | -0.02956 to +0.0275 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.8 | 444.7 | +0.2% | -6.312 to +8.137 | no |
| HPA replicas, mean | 1.995 | 2.076 | +4.1% | -0.07301 to +0.2349 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 42.11 | 44.79 | +6.4% | +2.104 to +3.246 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771 | 812.6 | +5.4% | +25.36 to +57.84 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.9125 | +1052.6% | +0.7564 to +0.9103 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.6 | +220.0% | +0.4737 to +1.726 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.57 | 125.3 | +55.5% | +25.08 to +64.34 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.596 | -6.7% | -0.8583 to +0.04993 | no |
| node-hours | 2.517 | 2.346 | -6.8% | -0.3606 to +0.01841 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.2 | -0.1% | -0.968 to +0.5422 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 260.4 | -4.7% | -27.37 to +1.458 | no |
| response time (ms), mean | 357.3 | 327.9 | -8.2% | -50.59 to -8.149 | yes: GAIN |
| response time (ms), 95th percentile | 1172 | 1261 | +7.6% | -36.41 to +215 | no |
| response time (ms), 99th percentile | 1694 | 1838 | +8.6% | -3.281 to +292.9 | no |
| time over the response line (% of samples) | 21.8 | 22.04 | +1.1% | -0.9771 to +1.465 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.6 | +2.7% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.8 | +34.8 (native is 0) | +19.98 to +49.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.11 | 11.19 | +0.7% | -1.881 to +2.044 | no |
| utilisation (used / allocatable) | 0.06167 | 0.06645 | +7.7% | +0.0002841 to +0.009257 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.48 | 1.485 | +0.3% | -0.01914 to +0.02814 | no |
| Omni's own CPU (cores), mean | 0 | 0.01708 | +0.0171 (native is 0) | +0.01617 to +0.01799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.48 | 1.502 | +1.5% | -0.001888 to +0.04505 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.8 | 419.7 | -5.4% | -46.11 to -2.053 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.451 | +22.8% | +0.2775 to +0.6333 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | -0.05264 to +2.453 | no |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | -0.05264 to +2.453 | no |
| host CPU busy, the real machine under kind (%) | 42.11 | 43.28 | +2.8% | +0.7238 to +1.624 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771 | 779.3 | +1.1% | +2.479 to +14.12 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.235 | -12.7% | -1.594 to +0.06473 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.06667 | -15.8% | -0.05704 to +0.03204 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 | +20.0% | -0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 80.57 | 86.62 | +7.5% | -0.04047 to +12.14 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.596 | -6.7% | -0.8583 to +0.04993 | no |
| node-hours | 2.518 | 2.346 | -6.8% | -0.3608 to +0.01731 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.2 | -0.1% | -0.8552 to +0.3611 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 260.4 | -4.8% | -27.24 to +1.258 | no |
| response time (ms), mean | 422.3 | 327.9 | -22.3% | -141.1 to -47.72 | yes: GAIN |
| response time (ms), 95th percentile | 1790 | 1261 | -29.5% | -827.3 to -228.9 | yes: GAIN |
| response time (ms), 99th percentile | 2818 | 1838 | -34.8% | -1469 to -489.9 | yes: GAIN |
| time over the response line (% of samples) | 17.53 | 22.04 | +25.7% | +2.516 to +6.507 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.6 | +2.7% | -1.319 to +1.919 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.8 | +34.8 (native is 0) | +19.98 to +49.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.07 | 11.19 | -34.4% | -8.212 to -3.535 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06163 | 0.06645 | +7.8% | -0.0001513 to +0.009778 | no |
| CPU used (cores), mean | 1.479 | 1.485 | +0.4% | -0.02482 to +0.03587 | no |
| Omni's own CPU (cores), mean | 0 | 0.01708 | +0.0171 (native is 0) | +0.01617 to +0.01799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.502 | +1.5% | -0.007496 to +0.05271 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.7 | 419.7 | -5.6% | -50.38 to +0.3953 | no |
| HPA replicas, mean | 2.076 | 2.451 | +18.0% | +0.2031 to +0.5458 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.4 | 1.2 | +200.0% | -0.6226 to +2.223 | no |
| pod start wait, mean (s) | 0.4 | 1.2 | +200.0% | -0.6226 to +2.223 | no |
| host CPU busy, the real machine under kind (%) | 44.79 | 43.28 | -3.4% | -2.01 to -0.9916 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 812.6 | 779.3 | -4.1% | -47.79 to -18.81 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.235 | -12.7% | -1.594 to +0.06473 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9125 | 0.06667 | -92.7% | -0.9038 to -0.7878 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.6 | -62.5% | -1.584 to -0.416 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 125.3 | 86.62 | -30.9% | -55.82 to -21.5 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.739 | -4.3% | -0.6082 to +0.08686 | no |
| node-hours | 2.517 | 2.4 | -4.7% | -0.2609 to +0.02553 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 272.8 | -0.2% | -1.513 to +0.341 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 264.6 | -3.2% | -19.3 to +1.703 | no |
| response time (ms), mean | 357.3 | 361.6 | +1.2% | -30.35 to +38.94 | no |
| response time (ms), 95th percentile | 1172 | 1667 | +42.2% | +226.7 to +762.3 | yes: LOSS |
| response time (ms), 99th percentile | 1694 | 2781 | +64.2% | +626.6 to +1549 | yes: LOSS |
| time over the response line (% of samples) | 21.8 | 16.92 | -22.4% | -7.144 to -2.611 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.4 | +0.9% | -1.137 to +1.337 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.4 | +43.4 (native is 0) | +26.09 to +60.71 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.11 | 17.86 | +60.7% | +5.343 to +8.153 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06167 | 0.0651 | +5.5% | -0.0001147 to +0.006957 | no |
| CPU used (cores), mean | 1.48 | 1.494 | +1.0% | -0.002799 to +0.03115 | no |
| Omni's own CPU (cores), mean | 0 | 0.01821 | +0.0182 (native is 0) | +0.01724 to +0.01918 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.48 | 1.513 | +2.2% | +0.01536 to +0.04941 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.8 | 424.8 | -4.3% | -38.43 to +0.4067 | no |
| HPA replicas, mean | 1.995 | 2.386 | +19.6% | +0.2055 to +0.5766 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | +0.1427 to +1.457 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | +0.09185 to +2.308 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8667 | +0.867 (native is 0) | +0.2698 to +1.464 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.11 | 45.59 | +8.3% | +3.145 to +3.806 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771 | 811.2 | +5.2% | +27.3 to +53.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.519 | -8.0% | -1.078 to +0.1155 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.9167 | +1057.9% | +0.7417 to +0.9333 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.7 | +240.0% | +0.6358 to +1.764 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.57 | 121.7 | +51.1% | +27.27 to +55.04 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*