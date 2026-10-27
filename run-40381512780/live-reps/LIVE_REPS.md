# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.32 | 7.053 |
| node-hours | 5.024 | 5.024 | 4.75 | 2.954 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 504.4 | 526.5 | 504.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 504.4 | 505.2 | 349.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 587.5 | 133.3 | 571.1 | 76.28 |
| response time (ms), 95th percentile | 2379 | 182 | 2538 | 97.91 |
| response time (ms), 99th percentile | 3457 | 206.2 | 3707 | 133.8 |
| time over the response line (% of samples) | 23.09 | 0.003802 | 23.41 | 0.003597 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 0 | 13.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 67.5 | 27.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.57 | 0.02667 | 14.99 | 0.1317 |
| utilisation (used / allocatable) | 0.03459 | 0.006488 | 0.03699 | 0.009344 |
| CPU used (cores), mean | 1.66 | 0.3114 | 1.672 | 0.2641 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01356 | 0.00941 |
| CPU used with Omni's own (cores), mean | 1.66 | 0.3114 | 1.685 | 0.2735 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.3 | 3900 | 724.9 | 3187 |
| HPA replicas, mean | 4.04 | 4.292 | 4.205 | 4.603 |
| pods started | 0 | 0.2 | 0.3 | 2.4 |
| pod start wait, total (s) | 0 | 0.3 | 0.8 | 4 |
| pod start wait, mean (s) | 0 | 0.3 | 0.8 | 1.458 |
| host CPU busy, the real machine under kind (%) | 50.85 | 14.5 | 52.61 | 15.47 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 855.2 | 1505 | 867.4 | 1505 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.68 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1158 | 0.08333 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1474 | 0.6 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 168.2 | 1158 | 174.9 | 1158 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 7.053 | −41.2% | −5.1113 to −4.7820 | yes: GAIN |
| node-hours | 5.024 | 2.954 | −41.2% | −2.1388 to −2.0012 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 504.6 | +0.1% | −0.7112 to +1.2232 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 349.3 | −30.8% | −160.3027 to −149.9352 | yes: GAIN |
| response time (ms), mean | 133.3 | 76.28 | −42.8% | −63.1240 to −50.8867 | yes: GAIN |
| response time (ms), 95th percentile | 182 | 97.91 | −46.2% | −90.3640 to −77.9040 | yes: GAIN |
| response time (ms), 99th percentile | 206.2 | 133.8 | −35.1% | −86.5812 to −58.0968 | yes: GAIN |
| time over the response line (% of samples) | 0.003802 | 0.003597 | −5.4% | −0.0007 to +0.0003 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.1 | +27.100 (native is 0) | +25.5383 to +28.6617 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1317 | +393.7% | +0.0080 to +0.2020 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006488 | 0.009344 | +44.0% | +0.0027 to +0.0030 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3114 | 0.2641 | −15.2% | −0.0549 to −0.0398 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00941 | +0.009 (native is 0) | +0.0088 to +0.0100 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3114 | 0.2735 | −12.2% | −0.0454 to −0.0306 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3900 | 3187 | −18.3% | −799.4035 to −627.1564 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.292 | 4.603 | +7.2% | −0.0110 to +0.6327 | no |
| pods started | 0.2 | 2.4 | +1100.0% | +1.2583 to +3.1417 | yes: power given |
| pod start wait, total (s) | 0.3 | 4 | +1233.3% | +1.8515 to +5.5485 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.458 | +386.1% | +0.3968 to +1.9199 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.5 | 15.47 | +6.7% | +0.6319 to +1.3139 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 1505 | −0.0% | −3.1803 to +2.9803 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 1158 | −0.0% | −3.3791 to +2.9375 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 1474 | ±0.0% | −3.1088 to +3.1088 | no |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 1158 | −0.0% | −3.3791 to +2.9375 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.024 | 5.024 | −0.0% | −0.0152 to +0.0138 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 504.4 | −4.0% | −23.4696 to −18.0919 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 504.4 | −4.0% | −23.4696 to −18.0919 | yes: GAIN |
| response time (ms), mean | 587.5 | 133.3 | −77.3% | −660.0670 to −248.2917 | yes: GAIN |
| response time (ms), 95th percentile | 2379 | 182 | −92.3% | −3246.0340 to −1147.3800 | yes: GAIN |
| response time (ms), 99th percentile | 3457 | 206.2 | −94.0% | −4733.9849 to −1767.6001 | yes: GAIN |
| time over the response line (% of samples) | 23.09 | 0.003802 | −100.0% | −33.8018 to −12.3768 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 0 | −100.0% | −16.1981 to −7.8019 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.57 | 0.02667 | −99.8% | −19.6661 to −11.4272 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03459 | 0.006488 | −81.2% | −0.0307 to −0.0255 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.66 | 0.3114 | −81.2% | −1.4745 to −1.2233 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.66 | 0.3114 | −81.2% | −1.4745 to −1.2233 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.3 | 3900 | +408.9% | +2930.4026 to +3337.4322 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.04 | 4.292 | +6.3% | +0.0436 to +0.4618 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 50.85 | 14.5 | −71.5% | −40.2008 to −32.5083 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 855.2 | 1505 | +76.0% | +583.6606 to +715.7394 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1158 | +1323704.8% | +1154.5272 to +1161.9561 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1474 | +210542.9% | +1470.0939 to +1477.5061 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 168.2 | 1158 | +588.7% | +921.4352 to +1058.8481 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.32 | −5.6% | −1.5771 to +0.2227 | no |
| node-hours | 5.024 | 4.75 | −5.5% | −0.6500 to +0.1012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 526.5 | +0.3% | −0.1146 to +2.8801 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 505.2 | −3.8% | −47.9404 to +8.0976 | no |
| response time (ms), mean | 587.5 | 571.1 | −2.8% | −52.5932 to +19.9086 | no |
| response time (ms), 95th percentile | 2379 | 2538 | +6.7% | −28.8140 to +346.3440 | no |
| response time (ms), 99th percentile | 3457 | 3707 | +7.2% | +33.2548 to +467.0918 | yes: LOSS |
| time over the response line (% of samples) | 23.09 | 23.41 | +1.4% | −1.3444 to +1.9709 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 13.7 | +14.2% | −0.4340 to +3.8340 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.5 | +67.500 (native is 0) | +21.5737 to +113.4263 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.57 | 14.99 | −3.7% | −4.2443 to +3.0843 | no |
| utilisation (used / allocatable) | 0.03459 | 0.03699 | +6.9% | −0.0007 to +0.0055 | no |
| CPU used (cores), mean | 1.66 | 1.672 | +0.7% | −0.0087 to +0.0312 | no |
| Omni's own CPU (cores), mean | 0 | 0.01356 | +0.014 (native is 0) | +0.0122 to +0.0149 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.66 | 1.685 | +1.5% | +0.0050 to +0.0447 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.3 | 724.9 | −5.4% | −93.6383 to +10.8013 | no |
| HPA replicas, mean | 4.04 | 4.205 | +4.1% | −0.2066 to +0.5372 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.1417 to +1.7417 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | −0.1417 to +1.7417 | no |
| host CPU busy, the real machine under kind (%) | 50.85 | 52.61 | +3.5% | +1.1985 to +2.3211 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 855.2 | 867.4 | +1.4% | +0.0665 to +24.3335 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.68 | −11.0% | −2.9700 to +0.3325 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.08333 | −4.8% | −0.0557 to +0.0474 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 168.2 | 174.9 | +4.0% | −3.3800 to +16.8717 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.32 | −5.6% | −1.5771 to +0.2227 | no |
| node-hours | 5.024 | 4.75 | −5.4% | −0.6550 to +0.1076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 526.5 | +4.4% | +19.6894 to +24.6377 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 505.2 | +0.2% | −29.3367 to +31.0555 | no |
| response time (ms), mean | 133.3 | 571.1 | +328.5% | +230.8594 to +644.8147 | yes: LOSS |
| response time (ms), 95th percentile | 182 | 2538 | +1293.9% | +1270.6421 to +3440.3019 | yes: LOSS |
| response time (ms), 99th percentile | 206.2 | 3707 | +1698.0% | +1990.5424 to +5011.3892 | yes: LOSS |
| time over the response line (% of samples) | 0.003802 | 23.41 | +615486.2% | +14.0720 to +32.7331 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 13.7 | +13.700 (native is 0) | +11.0014 to +16.3986 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.5 | +67.500 (native is 0) | +21.5737 to +113.4263 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 14.99 | +56125.0% | +10.2554 to +19.6780 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006488 | 0.03699 | +470.1% | +0.0285 to +0.0325 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3114 | 1.672 | +436.7% | +1.2339 to +1.4865 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01356 | +0.014 (native is 0) | +0.0122 to +0.0149 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3114 | 1.685 | +441.1% | +1.2482 to +1.4993 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3900 | 724.9 | −81.4% | −3421.0701 to −2929.6017 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.292 | 4.205 | −2.0% | −0.3460 to +0.1713 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.3 | 0.8 | +166.7% | −0.3430 to +1.3430 | no |
| pod start wait, mean (s) | 0.3 | 0.8 | +166.7% | −0.3430 to +1.3430 | no |
| host CPU busy, the real machine under kind (%) | 14.5 | 52.61 | +262.9% | +34.1778 to +42.0509 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 867.4 | −42.4% | −709.7600 to −565.2400 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 0.08333 | −100.0% | −1161.9777 to −1154.5139 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 0.6 | −100.0% | −1477.7660 to −1470.0340 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 174.9 | −84.9% | −1052.9056 to −913.8861 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.053 | −41.2% | −5.1113 to −4.7820 | yes: GAIN |
| node-hours | 5.024 | 2.954 | −41.2% | −2.1396 to −2.0018 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 504.6 | −3.9% | −23.3004 to −17.7490 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 349.3 | −33.5% | −179.8985 to −171.9009 | yes: GAIN |
| response time (ms), mean | 587.5 | 76.28 | −87.0% | −722.2052 to −300.1642 | yes: GAIN |
| response time (ms), 95th percentile | 2379 | 97.91 | −95.9% | −3332.5788 to −1229.1032 | yes: GAIN |
| response time (ms), 99th percentile | 3457 | 133.8 | −96.1% | −4802.2952 to −1843.9678 | yes: GAIN |
| time over the response line (% of samples) | 23.09 | 0.003597 | −100.0% | −33.8021 to −12.3769 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 0 | −100.0% | −16.1981 to −7.8019 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.1 | +27.100 (native is 0) | +25.5383 to +28.6617 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.57 | 0.1317 | −99.2% | −19.5582 to −11.3251 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03459 | 0.009344 | −73.0% | −0.0278 to −0.0227 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.66 | 0.2641 | −84.1% | −1.5225 to −1.2701 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00941 | +0.009 (native is 0) | +0.0088 to +0.0100 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.66 | 0.2735 | −83.5% | −1.5126 to −1.2612 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.3 | 3187 | +315.9% | +2271.8443 to +2569.4306 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.04 | 4.603 | +14.0% | +0.3250 to +0.8021 | yes: power given |
| pods started | 0 | 2.4 | +2.400 (native is 0) | +1.4952 to +3.3048 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +2.2479 to +5.7521 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.458 | +1.458 (native is 0) | +0.9610 to +1.9557 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.85 | 15.47 | −69.6% | −39.0545 to −31.7088 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 855.2 | 1505 | +76.0% | +584.0703 to +715.1297 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1158 | +1323452.4% | +1155.1625 to +1160.8791 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1474 | +210542.9% | +1470.9828 to +1476.6172 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 168.2 | 1158 | +588.6% | +921.6546 to +1058.1870 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*