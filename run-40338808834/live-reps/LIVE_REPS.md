# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.894 | 4.708 |
| node-hours | 2.517 | 2.517 | 2.05 | 1.968 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.4 | 270.6 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.4 | 235.8 | 230 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 260.7 | 300.4 | 238.1 | 273 |
| response time (ms), 95th percentile | 814.6 | 1180 | 868.8 | 1249 |
| response time (ms), 99th percentile | 1162 | 1869 | 1261 | 1961 |
| time over the response line (% of samples) | 13.59 | 11.06 | 13.67 | 11.04 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.9 | 7 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.7 | 38.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.4 | 14.52 | 9.992 | 14.15 |
| utilisation (used / allocatable) | 0.05655 | 0.05635 | 0.06892 | 0.07258 |
| CPU used (cores), mean | 1.357 | 1.352 | 1.328 | 1.337 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01593 | 0.01853 |
| CPU used with Omni's own (cores), mean | 1.357 | 1.352 | 1.344 | 1.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.6 | 487 | 428.4 | 411.8 |
| HPA replicas, mean | 1.923 | 2.021 | 2.032 | 2.023 |
| pods started | 0.1 | 0.3 | 0 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.8 | 0 | 0.1 |
| pod start wait, mean (s) | 0.2 | 0.6 | 0 | 0.1 |
| host CPU busy, the real machine under kind (%) | 38.32 | 40.55 | 39.51 | 41.76 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 750.8 | 775.2 | 755.1 | 781.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.139 | 3.877 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.7167 | 0.04167 | 0.7708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.3 | 0.3 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 58.41 | 84.99 | 62.15 | 89.81 |
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
| worker nodes in service, mean | 6 | 4.708 | −21.5% | −2.1445 to −0.4404 | yes: GAIN |
| node-hours | 2.517 | 1.968 | −21.8% | −0.9048 to −0.1927 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.6 | −0.3% | −1.8232 to +0.1577 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 230 | −15.2% | −68.2696 to −14.4584 | yes: GAIN |
| response time (ms), mean | 300.4 | 273 | −9.1% | −45.7236 to −9.0669 | yes: GAIN |
| response time (ms), 95th percentile | 1180 | 1249 | +5.8% | −53.3543 to +190.4573 | no |
| response time (ms), 99th percentile | 1869 | 1961 | +5.0% | −120.8967 to +305.9195 | no |
| time over the response line (% of samples) | 11.06 | 11.04 | −0.1% | −0.7878 to +0.7576 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.3 | +5.8% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 | +38.500 (native is 0) | +25.1465 to +51.8535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.52 | 14.15 | −2.5% | −1.9972 to +1.2639 | no |
| utilisation (used / allocatable) | 0.05635 | 0.07258 | +28.8% | +0.0054 to +0.0270 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.352 | 1.337 | −1.2% | −0.0501 to +0.0189 | no |
| Omni's own CPU (cores), mean | 0 | 0.01853 | +0.019 (native is 0) | +0.0162 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.352 | 1.355 | +0.2% | −0.0326 to +0.0385 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487 | 411.8 | −15.4% | −124.3419 to −25.8775 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.021 | 2.023 | +0.1% | −0.1058 to +0.1097 | no |
| pods started | 0.3 | 0.1 | −66.7% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.8 | 0.1 | −87.5% | −1.7690 to +0.3690 | no |
| pod start wait, mean (s) | 0.6 | 0.1 | −83.3% | −1.4079 to +0.4079 | no |
| host CPU busy, the real machine under kind (%) | 40.55 | 41.76 | +3.0% | +0.8831 to +1.5341 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.2 | 781.4 | +0.8% | +1.0220 to +11.3780 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.877 | −35.4% | −3.3937 to −0.8531 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7167 | 0.7708 | +7.6% | −0.0347 to +0.1431 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.5 | +15.4% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.99 | 89.81 | +5.7% | −1.7897 to +11.4230 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.517 | +0.0% | −0.0059 to +0.0062 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.4 | −0.0% | −0.5530 to +0.5217 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.4 | −0.0% | −0.5530 to +0.5217 | no |
| response time (ms), mean | 260.7 | 300.4 | +15.2% | +6.7257 to +72.5331 | yes: LOSS |
| response time (ms), 95th percentile | 814.6 | 1180 | +44.9% | +77.8419 to +653.0061 | yes: LOSS |
| response time (ms), 99th percentile | 1162 | 1869 | +60.8% | +134.3707 to +1279.5337 | yes: LOSS |
| time over the response line (% of samples) | 13.59 | 11.06 | −18.6% | −4.5175 to −0.5424 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.9 | ±0.0% | −0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.4 | 14.52 | +39.6% | +2.1094 to +6.1306 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05655 | 0.05635 | −0.4% | −0.0009 to +0.0005 | no |
| CPU used (cores), mean | 1.357 | 1.352 | −0.4% | −0.0226 to +0.0131 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.357 | 1.352 | −0.4% | −0.0226 to +0.0131 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.6 | 487 | +0.5% | −4.8247 to +9.5300 | no |
| HPA replicas, mean | 1.923 | 2.021 | +5.1% | +0.0049 to +0.1918 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.7572 to +1.9572 | no |
| pod start wait, mean (s) | 0.2 | 0.6 | +200.0% | −0.7285 to +1.5285 | no |
| host CPU busy, the real machine under kind (%) | 38.32 | 40.55 | +5.8% | +1.7446 to +2.7054 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.8 | 775.2 | +3.2% | +7.7566 to +41.0434 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.7167 | +1811.1% | +0.5788 to +0.7796 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.3 | +333.3% | +0.5231 to +1.4769 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.41 | 84.99 | +45.5% | +8.5529 to +44.6054 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.894 | −18.4% | −1.9256 to −0.2857 | yes: GAIN |
| node-hours | 2.517 | 2.05 | −18.6% | −0.8061 to −0.1284 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.6 | −0.3% | −1.7353 to +0.1057 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 235.8 | −13.1% | −61.2520 to −9.9109 | yes: GAIN |
| response time (ms), mean | 260.7 | 238.1 | −8.7% | −38.9029 to −6.3575 | yes: GAIN |
| response time (ms), 95th percentile | 814.6 | 868.8 | +6.7% | −24.8508 to +133.2918 | no |
| response time (ms), 99th percentile | 1162 | 1261 | +8.6% | −47.6163 to +246.6719 | no |
| time over the response line (% of samples) | 13.59 | 13.67 | +0.6% | −0.4940 to +0.6558 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7 | +1.4% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.700 (native is 0) | +21.1667 to +62.2333 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.4 | 9.992 | −3.9% | −1.9730 to +1.1597 | no |
| utilisation (used / allocatable) | 0.05655 | 0.06892 | +21.9% | +0.0023 to +0.0224 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.357 | 1.328 | −2.1% | −0.1016 to +0.0437 | no |
| Omni's own CPU (cores), mean | 0 | 0.01593 | +0.016 (native is 0) | +0.0146 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.357 | 1.344 | −1.0% | −0.0859 to +0.0598 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.6 | 428.4 | −11.6% | −104.3875 to −8.0712 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.923 | 2.032 | +5.7% | +0.0434 to +0.1752 | yes: power given |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 38.32 | 39.51 | +3.1% | +0.6840 to +1.6944 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.8 | 755.1 | +0.6% | −0.3363 to +8.9363 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.139 | −31.0% | −3.1780 to −0.5432 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.04167 | +11.1% | −0.0286 to +0.0370 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.41 | 62.15 | +6.4% | −0.5065 to +7.9898 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.894 | −18.4% | −1.9256 to −0.2857 | yes: GAIN |
| node-hours | 2.517 | 2.05 | −18.6% | −0.8087 to −0.1261 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.6 | −0.3% | −1.5348 to −0.0634 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 235.8 | −13.1% | −61.4699 to −9.6617 | yes: GAIN |
| response time (ms), mean | 300.4 | 238.1 | −20.7% | −98.5862 to −25.9330 | yes: GAIN |
| response time (ms), 95th percentile | 1180 | 868.8 | −26.4% | −606.7422 to −15.6648 | yes: GAIN |
| response time (ms), 99th percentile | 1869 | 1261 | −32.5% | −1135.5319 to −79.3169 | yes: GAIN |
| time over the response line (% of samples) | 11.06 | 13.67 | +23.6% | +0.5447 to +4.6770 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7 | +1.4% | −0.6113 to +0.8113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.700 (native is 0) | +21.1667 to +62.2333 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.52 | 9.992 | −31.2% | −6.0172 to −3.0361 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05635 | 0.06892 | +22.3% | +0.0024 to +0.0227 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.352 | 1.328 | −1.8% | −0.0893 to +0.0409 | no |
| Omni's own CPU (cores), mean | 0 | 0.01593 | +0.016 (native is 0) | +0.0146 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.352 | 1.344 | −0.6% | −0.0735 to +0.0570 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487 | 428.4 | −12.0% | −107.6363 to −9.5276 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.021 | 2.032 | +0.5% | −0.0777 to +0.0995 | no |
| pods started | 0.3 | 0 | −100.0% | −0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.8 | 0 | −100.0% | −2.0064 to +0.4064 | no |
| pod start wait, mean (s) | 0.6 | 0 | −100.0% | −1.5656 to +0.3656 | no |
| host CPU busy, the real machine under kind (%) | 40.55 | 39.51 | −2.6% | −1.6834 to −0.3882 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.2 | 755.1 | −2.6% | −33.9804 to −6.2196 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.139 | −31.0% | −3.1780 to −0.5432 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7167 | 0.04167 | −94.2% | −0.7669 to −0.5831 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.3 | −76.9% | −1.3372 to −0.6628 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 84.99 | 62.15 | −26.9% | −38.6957 to −6.9793 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.708 | −21.5% | −2.1445 to −0.4404 | yes: GAIN |
| node-hours | 2.517 | 1.968 | −21.8% | −0.9027 to −0.1944 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.6 | −0.3% | −1.7063 to +0.0094 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 230 | −15.2% | −68.0993 to −14.6600 | yes: GAIN |
| response time (ms), mean | 260.7 | 273 | +4.7% | −24.4345 to +48.9028 | no |
| response time (ms), 95th percentile | 814.6 | 1249 | +53.3% | +71.7786 to +796.1724 | yes: LOSS |
| response time (ms), 99th percentile | 1162 | 1961 | +68.8% | +116.3437 to +1482.5835 | yes: LOSS |
| time over the response line (% of samples) | 13.59 | 11.04 | −18.7% | −4.4461 to −0.6441 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.3 | +5.8% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 | +38.500 (native is 0) | +25.1465 to +51.8535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.4 | 14.15 | +36.1% | +2.7614 to +4.7453 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05655 | 0.07258 | +28.4% | +0.0053 to +0.0267 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.357 | 1.337 | −1.5% | −0.0653 to +0.0245 | no |
| Omni's own CPU (cores), mean | 0 | 0.01853 | +0.019 (native is 0) | +0.0162 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.357 | 1.355 | −0.1% | −0.0480 to +0.0443 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.6 | 411.8 | −15.0% | −120.6818 to −24.8324 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.923 | 2.023 | +5.2% | −0.0254 to +0.2260 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 38.32 | 41.76 | +9.0% | +2.7814 to +4.0858 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.8 | 781.4 | +4.1% | +10.0635 to +51.1365 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.877 | −35.4% | −3.3937 to −0.8531 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.7708 | +1955.6% | +0.6476 to +0.8190 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.5 | +400.0% | +0.8984 to +1.5016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 58.41 | 89.81 | +53.7% | +9.4990 to +53.2927 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*