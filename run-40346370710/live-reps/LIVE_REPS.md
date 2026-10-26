# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.401 | 4.363 |
| node-hours | 2.516 | 2.513 | 1.847 | 1.827 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.5 | 269.3 | 268.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 269.5 | 219 | 217.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 221 | 171.3 | 198.6 | 140.8 |
| response time (ms), 95th percentile | 692.4 | 412.7 | 730.6 | 401.4 |
| response time (ms), 99th percentile | 1026 | 641.1 | 1082 | 670.9 |
| time over the response line (% of samples) | 10.92 | 5.258 | 11.06 | 5.592 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 5.2 | 5.3 | 5.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.3 | 29.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.867 | 12.37 | 9.647 | 12.84 |
| utilisation (used / allocatable) | 0.05167 | 0.05265 | 0.06869 | 0.0687 |
| CPU used (cores), mean | 1.24 | 1.264 | 1.202 | 1.192 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.015 | 0.01489 |
| CPU used with Omni's own (cores), mean | 1.24 | 1.264 | 1.217 | 1.207 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.1 | 528.9 | 440.6 | 443.3 |
| HPA replicas, mean | 1.925 | 1.953 | 1.939 | 2.019 |
| pods started | 0 | 0.1 | 0.1 | 0 |
| pod start wait, total (s) | 0 | 0.1 | 0.1 | 0 |
| pod start wait, mean (s) | 0 | 0.1 | 0.1 | 0 |
| host CPU busy, the real machine under kind (%) | 35.17 | 36.23 | 36.02 | 36.9 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 744 | 753.2 | 747.1 | 755.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.437 | 3.448 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.6292 | 0.05417 | 0.65 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1 | 0.4 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 50.97 | 63.49 | 53.3 | 66.05 |
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
| worker nodes in service, mean | 6 | 4.363 | −27.3% | −2.5415 to −0.7316 | yes: GAIN |
| node-hours | 2.513 | 1.827 | −27.3% | −1.0677 to −0.3047 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 268.6 | −0.4% | −2.6464 to +0.7020 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 217.2 | −19.4% | −81.5690 to −23.1338 | yes: GAIN |
| response time (ms), mean | 171.3 | 140.8 | −17.8% | −40.2643 to −20.7819 | yes: GAIN |
| response time (ms), 95th percentile | 412.7 | 401.4 | −2.7% | −56.5658 to +34.0828 | no |
| response time (ms), 99th percentile | 641.1 | 670.9 | +4.6% | −60.7743 to +120.3443 | no |
| time over the response line (% of samples) | 5.258 | 5.592 | +6.4% | −0.6103 to +1.2789 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.1 | −1.9% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 | +29.100 (native is 0) | +21.2682 to +36.9318 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.37 | 12.84 | +3.8% | −0.4609 to +1.4009 | no |
| utilisation (used / allocatable) | 0.05265 | 0.0687 | +30.5% | +0.0071 to +0.0250 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.264 | 1.192 | −5.6% | −0.1259 to −0.0167 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01489 | +0.015 (native is 0) | +0.0125 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.264 | 1.207 | −4.5% | −0.1130 to +0.0002 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 528.9 | 443.3 | −16.2% | −136.6381 to −34.5810 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.953 | 2.019 | +3.4% | −0.0369 to +0.1688 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 36.23 | 36.9 | +1.8% | +0.1990 to +1.1281 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 753.2 | 755.9 | +0.4% | −1.1895 to +6.5895 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.448 | −42.5% | −3.9027 to −1.2021 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6292 | 0.65 | +3.3% | −0.0525 to +0.0942 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.1 | +10.0% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.49 | 66.05 | +4.0% | −3.5435 to +8.6769 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.513 | −0.1% | −0.0109 to +0.0049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.5 | +0.0% | −0.7687 to +0.9116 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 269.5 | +0.0% | −0.7687 to +0.9116 | no |
| response time (ms), mean | 221 | 171.3 | −22.5% | −91.9986 to −7.4105 | yes: GAIN |
| response time (ms), 95th percentile | 692.4 | 412.7 | −40.4% | −488.3556 to −71.1814 | yes: GAIN |
| response time (ms), 99th percentile | 1026 | 641.1 | −37.5% | −667.3097 to −103.2027 | yes: GAIN |
| time over the response line (% of samples) | 10.92 | 5.258 | −51.9% | −11.0373 to −0.2909 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 5.2 | −1.9% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.867 | 12.37 | +39.5% | +1.2164 to +5.7903 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05167 | 0.05265 | +1.9% | +0.0002 to +0.0017 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.24 | 1.264 | +1.9% | +0.0055 to +0.0412 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.24 | 1.264 | +1.9% | +0.0055 to +0.0412 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.1 | 528.9 | −2.1% | −22.1891 to −0.3305 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 1.953 | +1.5% | −0.1273 to +0.1833 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 35.17 | 36.23 | +3.0% | +0.5571 to +1.5686 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744 | 753.2 | +1.2% | +0.6975 to +17.7025 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.6292 | +1410.0% | +0.5209 to +0.6541 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1 | +233.3% | +0.3545 to +1.0455 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 50.97 | 63.49 | +24.6% | +1.5325 to +23.5091 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.401 | −26.6% | −2.4426 to −0.7545 | yes: GAIN |
| node-hours | 2.516 | 1.847 | −26.6% | −1.0250 to −0.3134 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.3 | −0.1% | −1.1092 to +0.7762 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 219 | −18.7% | −77.3476 to −23.5896 | yes: GAIN |
| response time (ms), mean | 221 | 198.6 | −10.2% | −35.8474 to −9.1404 | yes: GAIN |
| response time (ms), 95th percentile | 692.4 | 730.6 | +5.5% | −22.4903 to +98.8433 | no |
| response time (ms), 99th percentile | 1026 | 1082 | +5.4% | +4.1211 to +106.4673 | yes: LOSS |
| time over the response line (% of samples) | 10.92 | 11.06 | +1.3% | −0.8022 to +1.0847 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 5.3 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.3 | +49.300 (native is 0) | +28.2418 to +70.3582 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.867 | 9.647 | +8.8% | −1.5034 to +3.0634 | no |
| utilisation (used / allocatable) | 0.05167 | 0.06869 | +32.9% | +0.0080 to +0.0261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.24 | 1.202 | −3.1% | −0.0723 to −0.0038 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.015 | +0.015 (native is 0) | +0.0133 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.24 | 1.217 | −1.9% | −0.0580 to +0.0119 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.1 | 440.6 | −18.4% | −158.1082 to −41.0392 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 1.939 | +0.8% | −0.1221 to +0.1513 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 35.17 | 36.02 | +2.4% | +0.3776 to +1.3326 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744 | 747.1 | +0.4% | −1.2504 to +7.4504 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.437 | −42.7% | −3.8382 to −1.2876 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05417 | +30.0% | −0.0221 to +0.0471 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 50.97 | 53.3 | +4.6% | −1.6208 to +6.2792 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.401 | −26.6% | −2.4426 to −0.7545 | yes: GAIN |
| node-hours | 2.513 | 1.847 | −26.5% | −1.0231 to −0.3093 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.3 | −0.1% | −1.3353 to +0.8593 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 219 | −18.8% | −77.6536 to −23.4266 | yes: GAIN |
| response time (ms), mean | 171.3 | 198.6 | +15.9% | −4.2007 to +58.6220 | no |
| response time (ms), 95th percentile | 412.7 | 730.6 | +77.0% | +130.7236 to +505.1664 | yes: LOSS |
| response time (ms), 99th percentile | 641.1 | 1082 | +68.7% | +186.9465 to +694.1543 | yes: LOSS |
| time over the response line (% of samples) | 5.258 | 11.06 | +110.4% | +0.8234 to +10.7872 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.3 | +1.9% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.3 | +49.300 (native is 0) | +28.2418 to +70.3582 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.37 | 9.647 | −22.0% | −4.3108 to −1.1358 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05265 | 0.06869 | +30.5% | +0.0072 to +0.0249 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.264 | 1.202 | −4.9% | −0.0947 to −0.0281 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.015 | +0.015 (native is 0) | +0.0133 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.264 | 1.217 | −3.7% | −0.0808 to −0.0120 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 528.9 | 440.6 | −16.7% | −140.7318 to −35.8961 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.953 | 1.939 | −0.7% | −0.1719 to +0.1451 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, mean (s) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| host CPU busy, the real machine under kind (%) | 36.23 | 36.02 | −0.6% | −0.5391 to +0.1236 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 753.2 | 747.1 | −0.8% | −12.1550 to −0.0450 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.437 | −42.7% | −3.8382 to −1.2876 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6292 | 0.05417 | −91.4% | −0.6308 to −0.5192 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.4 | −60.0% | −0.9694 to −0.2306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 63.49 | 53.3 | −16.1% | −18.3942 to −1.9891 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.363 | −27.3% | −2.5415 to −0.7316 | yes: GAIN |
| node-hours | 2.516 | 1.827 | −27.4% | −1.0701 to −0.3084 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 268.6 | −0.3% | −2.4967 to +0.6952 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 217.2 | −19.4% | −81.3096 to −23.2503 | yes: GAIN |
| response time (ms), mean | 221 | 140.8 | −36.3% | −124.2230 to −36.2322 | yes: GAIN |
| response time (ms), 95th percentile | 692.4 | 401.4 | −42.0% | −492.0135 to −90.0065 | yes: GAIN |
| response time (ms), 99th percentile | 1026 | 670.9 | −34.6% | −605.5619 to −105.3805 | yes: GAIN |
| time over the response line (% of samples) | 10.92 | 5.592 | −48.8% | −10.5061 to −0.1534 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 5.1 | −3.8% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 | +29.100 (native is 0) | +21.2682 to +36.9318 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.867 | 12.84 | +44.8% | +1.9573 to +5.9894 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05167 | 0.0687 | +32.9% | +0.0079 to +0.0261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.24 | 1.192 | −3.9% | −0.1042 to +0.0084 | no |
| Omni's own CPU (cores), mean | 0 | 0.01489 | +0.015 (native is 0) | +0.0125 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.24 | 1.207 | −2.7% | −0.0911 to +0.0251 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.1 | 443.3 | −17.9% | −153.9064 to −39.8322 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.925 | 2.019 | +4.9% | −0.0438 to +0.2317 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 35.17 | 36.9 | +4.9% | +1.3819 to +2.0709 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744 | 755.9 | +1.6% | +2.1244 to +21.6756 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.448 | −42.5% | −3.9027 to −1.2021 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.65 | +1460.0% | +0.5299 to +0.6868 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | +266.7% | +0.3476 to +1.2524 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 50.97 | 66.05 | +29.6% | +2.6583 to +27.5167 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*