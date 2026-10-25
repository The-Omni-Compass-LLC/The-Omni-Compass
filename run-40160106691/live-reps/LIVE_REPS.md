# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.021 | 5.974 |
| node-hours | 2.522 | 2.512 | 2.102 | 2.507 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 286.1 | 271.5 | 286.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 286.1 | 240.8 | 285.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 291.8 | 608.5 | 261.7 | 640.7 |
| response time (ms), 95th percentile | 923 | 1276 | 972.7 | 1357 |
| response time (ms), 99th percentile | 1391 | 1775 | 1469 | 1855 |
| time over the response line (% of samples) | 16.17 | 52.87 | 15.74 | 56.38 |
| failed requests (%) | 0 | 0.01156 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 24.3 | 8.6 | 24.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 38 | 18.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.648 | 2.312 | 11.64 | 2.3 |
| utilisation (used / allocatable) | 0.05713 | 0.09739 | 0.07015 | 0.0969 |
| CPU used (cores), mean | 1.371 | 2.337 | 1.391 | 2.317 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01647 | 0.00928 |
| CPU used with Omni's own (cores), mean | 1.371 | 2.337 | 1.408 | 2.326 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 293.5 | 413.8 | 294.7 |
| HPA replicas, mean | 2.051 | 2.107 | 2.385 | 2.642 |
| pods started | 0 | 0 | 0.3 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 0.7 | 0.4 |
| pod start wait, mean (s) | 0 | 0 | 0.7 | 0.4 |
| host CPU busy, the real machine under kind (%) | 39.28 | 74.82 | 40.41 | 75.13 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 758.1 | 1469 | 761.7 | 1470 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.308 | 5 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 685.8 | 0.05 | 732.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1254 | 0.3 | 1271 |
| queue: job turnaround, submitted to done, mean (s) | 65.5 | 958.4 | 68.22 | 983.8 |
| queue: jobs unfinished at the window's end | 0 | 15 | 0 | 16.2 |

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
| worker nodes in service, mean | 6 | 5.974 | −0.4% | −0.0864 to +0.0334 | no |
| node-hours | 2.512 | 2.507 | −0.2% | −0.0309 to +0.0210 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.1 | 286.5 | +0.1% | −0.2982 to +1.1224 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.1 | 285.7 | −0.1% | −2.3731 to +1.5265 | no |
| response time (ms), mean | 608.5 | 640.7 | +5.3% | +2.1628 to +62.3675 | yes: LOSS |
| response time (ms), 95th percentile | 1276 | 1357 | +6.3% | +5.8178 to +155.0892 | yes: LOSS |
| response time (ms), 99th percentile | 1775 | 1855 | +4.5% | −33.1003 to +192.8903 | no |
| time over the response line (% of samples) | 52.87 | 56.38 | +6.6% | +0.7414 to +6.2698 | yes: LOSS |
| failed requests (%) | 0.01156 | 0 | −100.0% | −0.0377 to +0.0146 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.3 | 24.3 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +15.2332 to +21.5668 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.312 | 2.3 | −0.5% | −0.4201 to +0.3968 | no |
| utilisation (used / allocatable) | 0.09739 | 0.0969 | −0.5% | −0.0017 to +0.0007 | no |
| CPU used (cores), mean | 2.337 | 2.317 | −0.9% | −0.0398 to −0.0015 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00928 | +0.009 (native is 0) | +0.0083 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.337 | 2.326 | −0.5% | −0.0310 to +0.0082 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.5 | 294.7 | +0.4% | −1.7203 to +4.1299 | no |
| HPA replicas, mean | 2.107 | 2.642 | +25.4% | +0.3335 to +0.7353 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 74.82 | 75.13 | +0.4% | +0.1543 to +0.4628 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1469 | 1470 | +0.1% | −2.8945 to +5.6945 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5 | −16.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 685.8 | 732.7 | +6.8% | −7.3682 to +101.1395 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1254 | 1271 | +1.4% | −19.3093 to +54.2327 | no |
| queue: job turnaround, submitted to done, mean (s) | 958.4 | 983.8 | +2.6% | −25.4524 to +76.1940 | no |
| queue: jobs unfinished at the window's end | 15 | 16.2 | +8.0% | −0.4101 to +2.8101 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.522 | 2.512 | −0.4% | −0.0162 to −0.0024 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 286.1 | +5.1% | +10.7934 to +17.2122 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 286.1 | +5.1% | +10.7934 to +17.2122 | yes: power given |
| response time (ms), mean | 291.8 | 608.5 | +108.5% | +266.7681 to +366.6312 | yes: LOSS |
| response time (ms), 95th percentile | 923 | 1276 | +38.3% | +148.3194 to +557.8686 | yes: LOSS |
| response time (ms), 99th percentile | 1391 | 1775 | +27.6% | +22.5760 to +745.3836 | yes: LOSS |
| time over the response line (% of samples) | 16.17 | 52.87 | +227.0% | +29.7177 to +43.6901 | yes: LOSS |
| failed requests (%) | 0 | 0.01156 | +0.012 (native is 0) | −0.0146 to +0.0377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 24.3 | +196.3% | +12.1038 to +20.0962 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.648 | 2.312 | −76.0% | −9.3107 to −5.3626 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05713 | 0.09739 | +70.5% | +0.0327 to +0.0479 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.371 | 2.337 | +70.5% | +0.7839 to +1.1487 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.371 | 2.337 | +70.5% | +0.7839 to +1.1487 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 293.5 | −39.4% | −247.5825 to −134.1402 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.051 | 2.107 | +2.7% | −0.1022 to +0.2139 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 39.28 | 74.82 | +90.5% | +31.6654 to +39.4142 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.1 | 1469 | +93.7% | +628.2329 to +793.1671 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 685.8 | +1371575.6% | +466.4205 to +905.1551 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1254 | +417876.7% | +956.8291 to +1550.4312 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.5 | 958.4 | +1363.4% | +754.9629 to +1030.9371 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15 | +15.000 (native is 0) | +10.1720 to +19.8280 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.021 | −16.3% | −1.7328 to −0.2247 | yes: GAIN |
| node-hours | 2.522 | 2.102 | −16.6% | −0.7340 to −0.1047 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.5 | −0.2% | −1.6941 to +0.5700 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 240.8 | −11.5% | −54.6449 to −7.9333 | yes: GAIN |
| response time (ms), mean | 291.8 | 261.7 | −10.3% | −47.7938 to −12.3553 | yes: GAIN |
| response time (ms), 95th percentile | 923 | 972.7 | +5.4% | −71.2043 to +170.6123 | no |
| response time (ms), 99th percentile | 1391 | 1469 | +5.6% | −126.1127 to +282.5995 | no |
| time over the response line (% of samples) | 16.17 | 15.74 | −2.7% | −1.3516 to +0.4873 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.6 | +4.9% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 | +38.000 (native is 0) | +20.6514 to +55.3486 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.648 | 11.64 | +20.6% | −0.0704 to +4.0471 | no |
| utilisation (used / allocatable) | 0.05713 | 0.07015 | +22.8% | +0.0030 to +0.0230 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.371 | 1.391 | +1.5% | −0.0008 to +0.0407 | no |
| Omni's own CPU (cores), mean | 0 | 0.01647 | +0.016 (native is 0) | +0.0151 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.371 | 1.408 | +2.7% | +0.0168 to +0.0560 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 413.8 | −14.6% | −128.8926 to −12.2529 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.051 | 2.385 | +16.3% | +0.0193 to +0.6483 | yes: power given |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| host CPU busy, the real machine under kind (%) | 39.28 | 40.41 | +2.9% | +0.7419 to +1.5247 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.1 | 761.7 | +0.5% | −2.4339 to +9.6339 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.308 | −28.2% | −2.9275 to −0.4575 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05 | ±0.0% | −0.0466 to +0.0466 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.5 | 68.22 | +4.2% | −3.0642 to +8.5142 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.021 | −16.3% | −1.7328 to −0.2247 | yes: GAIN |
| node-hours | 2.512 | 2.102 | −16.3% | −0.7264 to −0.0937 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 286.1 | 271.5 | −5.1% | −17.1777 to −11.9520 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.1 | 240.8 | −15.8% | −71.1148 to −19.4691 | yes: GAIN |
| response time (ms), mean | 608.5 | 261.7 | −57.0% | −401.0712 to −292.4772 | yes: GAIN |
| response time (ms), 95th percentile | 1276 | 972.7 | −23.8% | −512.5412 to −94.2388 | yes: GAIN |
| response time (ms), 99th percentile | 1775 | 1469 | −17.2% | −703.9780 to +92.5052 | no |
| time over the response line (% of samples) | 52.87 | 15.74 | −70.2% | −44.3387 to −29.9334 | yes: GAIN |
| failed requests (%) | 0.01156 | 0 | −100.0% | −0.0377 to +0.0146 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.3 | 8.6 | −64.6% | −19.5008 to −11.8992 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 | +38.000 (native is 0) | +20.6514 to +55.3486 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.312 | 11.64 | +403.4% | +6.2092 to +12.4408 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09739 | 0.07015 | −28.0% | −0.0342 to −0.0203 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.337 | 1.391 | −40.5% | −1.1300 to −0.7627 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01647 | +0.016 (native is 0) | +0.0151 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.337 | 1.408 | −39.8% | −1.1134 to −0.7464 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.5 | 413.8 | +41.0% | +101.9153 to +138.6619 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.107 | 2.385 | +13.2% | −0.0454 to +0.6013 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| host CPU busy, the real machine under kind (%) | 74.82 | 40.41 | −46.0% | −38.1709 to −30.6421 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1469 | 761.7 | −48.1% | −789.1575 to −625.0425 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 685.8 | 0.05 | −100.0% | −905.1523 to −466.4233 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1254 | 0.3 | −100.0% | −1550.4362 to −956.8241 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 958.4 | 68.22 | −92.9% | −1027.0264 to −753.4236 | yes: GAIN |
| queue: jobs unfinished at the window's end | 15 | 0 | −100.0% | −19.8280 to −10.1720 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.974 | −0.4% | −0.0864 to +0.0334 | no |
| node-hours | 2.522 | 2.507 | −0.6% | −0.0405 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 286.5 | +5.3% | +11.1898 to +17.6399 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 285.7 | +5.0% | +9.8041 to +17.3548 | yes: power given |
| response time (ms), mean | 291.8 | 640.7 | +119.6% | +296.6185 to +401.3112 | yes: LOSS |
| response time (ms), 95th percentile | 923 | 1357 | +47.0% | +219.6864 to +647.4086 | yes: LOSS |
| response time (ms), 99th percentile | 1391 | 1855 | +33.4% | +94.1152 to +833.6344 | yes: LOSS |
| time over the response line (% of samples) | 16.17 | 56.38 | +248.7% | +33.2423 to +47.1767 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 24.3 | +196.3% | +12.1038 to +20.0962 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +15.2332 to +21.5668 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.648 | 2.3 | −76.2% | −9.2222 to −5.4745 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05713 | 0.0969 | +69.6% | +0.0327 to +0.0468 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.371 | 2.317 | +69.0% | +0.7763 to +1.1150 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00928 | +0.009 (native is 0) | +0.0083 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.371 | 2.326 | +69.6% | +0.7862 to +1.1236 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 294.7 | −39.2% | −246.1601 to −133.1530 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.051 | 2.642 | +28.8% | +0.4150 to +0.7655 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 39.28 | 75.13 | +91.3% | +31.9613 to +39.7354 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.1 | 1470 | +93.9% | +626.9558 to +797.2442 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5 | −16.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 732.7 | +1465346.9% | +526.5189 to +938.8280 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1271 | +423697.3% | +1000.8664 to +1541.3174 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.5 | 983.8 | +1402.1% | +777.7602 to +1058.8815 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 16.2 | +16.200 (native is 0) | +11.6285 to +20.7715 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*