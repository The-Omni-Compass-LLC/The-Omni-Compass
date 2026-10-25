# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.401 | 5.4 |
| node-hours | 2.515 | 2.516 | 2.267 | 2.264 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | 272.5 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.1 | 253.6 | 253.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 335.6 | 306.1 | 293.8 | 266.7 |
| response time (ms), 95th percentile | 1079 | 1153 | 1106 | 1131 |
| response time (ms), 99th percentile | 1649 | 1823 | 1637 | 1728 |
| time over the response line (% of samples) | 19.42 | 13.58 | 18.75 | 14.05 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.3 | 9.9 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 33.6 | 41.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.22 | 10.35 | 10.4 | 11.4 |
| utilisation (used / allocatable) | 0.0596 | 0.05852 | 0.06514 | 0.06507 |
| CPU used (cores), mean | 1.43 | 1.404 | 1.409 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01533 | 0.01677 |
| CPU used with Omni's own (cores), mean | 1.43 | 1.404 | 1.425 | 1.415 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 470.7 | 434.5 | 435.2 |
| HPA replicas, mean | 2.097 | 2.055 | 2.423 | 2.304 |
| pods started | 0 | 0.2 | 0.4 | 0.4 |
| pod start wait, total (s) | 0 | 0.4 | 1 | 0.6 |
| pod start wait, mean (s) | 0 | 0.4 | 0.6667 | 0.45 |
| host CPU busy, the real machine under kind (%) | 40.58 | 40.18 | 41.19 | 40.87 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 767.5 | 761 | 766.6 | 761.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.94 | 4.924 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.04583 | 0.05833 | 0.0625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | 0.3 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 75.2 | 72.75 | 74.72 | 71.21 |
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
| worker nodes in service, mean | 6 | 5.4 | −10.0% | −1.2043 to +0.0048 | no |
| node-hours | 2.516 | 2.264 | −10.0% | −0.5091 to +0.0041 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272 | −0.1% | −1.2790 to +0.9932 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 253.2 | −7.0% | −38.4427 to +0.4861 | no |
| response time (ms), mean | 306.1 | 266.7 | −12.9% | −70.3364 to −8.4945 | yes: GAIN |
| response time (ms), 95th percentile | 1153 | 1131 | −1.9% | −201.4701 to +157.3771 | no |
| response time (ms), 99th percentile | 1823 | 1728 | −5.2% | −360.5217 to +170.9725 | no |
| time over the response line (% of samples) | 13.58 | 14.05 | +3.5% | −1.5636 to +2.5032 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.1 | −2.2% | −0.7642 to +0.3642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.800 (native is 0) | +29.6805 to +53.9195 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 11.41 | +10.2% | −0.2989 to +2.4089 | no |
| utilisation (used / allocatable) | 0.05852 | 0.06507 | +11.2% | +0.0000 to +0.0131 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.404 | 1.398 | −0.5% | −0.0272 to +0.0139 | no |
| Omni's own CPU (cores), mean | 0 | 0.01677 | +0.017 (native is 0) | +0.0149 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.404 | 1.415 | +0.7% | −0.0116 to +0.0318 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 435.2 | −7.5% | −74.9278 to +3.9775 | no |
| HPA replicas, mean | 2.055 | 2.304 | +12.1% | −0.0050 to +0.5030 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | −0.9081 to +1.3081 | no |
| pod start wait, mean (s) | 0.4 | 0.45 | +12.5% | −0.8804 to +0.9804 | no |
| host CPU busy, the real machine under kind (%) | 40.18 | 40.87 | +1.7% | +0.3156 to +1.0647 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 761 | 761.5 | +0.1% | −7.4457 to +8.4457 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.924 | −17.9% | −2.0550 to −0.0979 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.0625 | +36.4% | −0.0210 to +0.0544 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.75 | 71.21 | −2.1% | −7.7319 to +4.6486 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.516 | +0.0% | −0.0073 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −1.3937 to +1.0390 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.1 | −0.1% | −1.3937 to +1.0390 | no |
| response time (ms), mean | 335.6 | 306.1 | −8.8% | −62.9852 to +4.0071 | no |
| response time (ms), 95th percentile | 1079 | 1153 | +6.9% | −113.1459 to +261.4379 | no |
| response time (ms), 99th percentile | 1649 | 1823 | +10.5% | −108.7569 to +456.0491 | no |
| time over the response line (% of samples) | 19.42 | 13.58 | −30.1% | −9.4109 to −2.2636 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.3 | −6.1% | −1.5048 to +0.3048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.22 | 10.35 | +1.3% | −1.2799 to +1.5466 | no |
| utilisation (used / allocatable) | 0.0596 | 0.05852 | −1.8% | −0.0019 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.43 | 1.404 | −1.8% | −0.0453 to −0.0065 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.43 | 1.404 | −1.8% | −0.0453 to −0.0065 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 470.7 | +1.3% | −1.4372 to +13.3232 | no |
| HPA replicas, mean | 2.097 | 2.055 | −2.0% | −0.1853 to +0.1011 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 40.58 | 40.18 | −1.0% | −0.6326 to −0.1677 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.5 | 761 | −0.8% | −12.7108 to −0.2892 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.04583 | −21.4% | −0.0524 to +0.0274 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.2 | 72.75 | −3.3% | −8.5570 to +3.6570 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.401 | −10.0% | −1.2614 to +0.0628 | no |
| node-hours | 2.515 | 2.267 | −9.8% | −0.5260 to +0.0308 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.5 | +0.1% | −0.8818 to +1.2156 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 253.6 | −6.9% | −39.8463 to +2.5176 | no |
| response time (ms), mean | 335.6 | 293.8 | −12.4% | −56.6325 to −26.9085 | yes: GAIN |
| response time (ms), 95th percentile | 1079 | 1106 | +2.5% | −57.5893 to +110.7923 | no |
| response time (ms), 99th percentile | 1649 | 1637 | −0.8% | −152.5063 to +127.7009 | no |
| time over the response line (% of samples) | 19.42 | 18.75 | −3.4% | −1.5453 to +0.2097 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.9 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.6 | +33.600 (native is 0) | +19.2020 to +47.9980 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.22 | 10.4 | +1.8% | −1.0264 to +1.3931 | no |
| utilisation (used / allocatable) | 0.0596 | 0.06514 | +9.3% | −0.0004 to +0.0115 | no |
| CPU used (cores), mean | 1.43 | 1.409 | −1.5% | −0.0561 to +0.0138 | no |
| Omni's own CPU (cores), mean | 0 | 0.01533 | +0.015 (native is 0) | +0.0140 to +0.0166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.425 | −0.4% | −0.0418 to +0.0301 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 434.5 | −6.5% | −63.7778 to +3.2936 | no |
| HPA replicas, mean | 2.097 | 2.423 | +15.6% | −0.0236 to +0.6761 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −0.5080 to +2.5080 | no |
| pod start wait, mean (s) | 0 | 0.6667 | +0.667 (native is 0) | −0.4851 to +1.8184 | no |
| host CPU busy, the real machine under kind (%) | 40.58 | 41.19 | +1.5% | +0.3443 to +0.8632 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.5 | 766.6 | −0.1% | −6.1505 to +4.3505 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.94 | −17.7% | −2.1688 to +0.0487 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.05833 | =0.0% | −0.0421 to +0.0421 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.2 | 74.72 | −0.6% | −5.8085 to +4.8335 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.401 | −10.0% | −1.2614 to +0.0628 | no |
| node-hours | 2.516 | 2.267 | −9.9% | −0.5310 to +0.0338 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.5 | +0.1% | −1.1217 to +1.8103 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 253.6 | −6.8% | −40.4315 to +3.4576 | no |
| response time (ms), mean | 306.1 | 293.8 | −4.0% | −37.1879 to +12.6251 | no |
| response time (ms), 95th percentile | 1153 | 1106 | −4.1% | −210.6750 to +115.5860 | no |
| response time (ms), 99th percentile | 1823 | 1637 | −10.2% | −443.4804 to +71.3828 | no |
| time over the response line (% of samples) | 13.58 | 18.75 | +38.1% | +2.2465 to +8.0925 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.9 | +6.5% | −0.1689 to +1.3689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.6 | +33.600 (native is 0) | +19.2020 to +47.9980 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 10.4 | +0.5% | −1.0156 to +1.1156 | no |
| utilisation (used / allocatable) | 0.05852 | 0.06514 | +11.3% | +0.0013 to +0.0119 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.404 | 1.409 | +0.3% | −0.0470 to +0.0565 | no |
| Omni's own CPU (cores), mean | 0 | 0.01533 | +0.015 (native is 0) | +0.0140 to +0.0166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.404 | 1.425 | +1.4% | −0.0326 to +0.0728 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 434.5 | −7.7% | −64.6247 to −7.7456 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.423 | +17.9% | +0.0019 to +0.7349 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 0.4 | 1 | +150.0% | −0.6251 to +1.8251 | no |
| pod start wait, mean (s) | 0.4 | 0.6667 | +66.7% | −0.3672 to +0.9005 | no |
| host CPU busy, the real machine under kind (%) | 40.18 | 41.19 | +2.5% | +0.7848 to +1.2230 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 761 | 766.6 | +0.7% | +2.1087 to +9.0913 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.94 | −17.7% | −2.1688 to +0.0487 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05833 | +27.3% | −0.0298 to +0.0548 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.75 | 74.72 | +2.7% | −0.4459 to +4.3709 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.4 | −10.0% | −1.2043 to +0.0048 | no |
| node-hours | 2.515 | 2.264 | −10.0% | −0.5037 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272 | −0.1% | −0.9321 to +0.2916 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 253.2 | −7.0% | −37.9008 to −0.4105 | yes: GAIN |
| response time (ms), mean | 335.6 | 266.7 | −20.5% | −90.1688 to −47.6403 | yes: GAIN |
| response time (ms), 95th percentile | 1079 | 1131 | +4.8% | −2.8752 to +107.0742 | no |
| response time (ms), 99th percentile | 1649 | 1728 | +4.8% | −40.7004 to +198.4434 | no |
| time over the response line (% of samples) | 19.42 | 14.05 | −27.6% | −7.9308 to −2.8043 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 9.1 | −8.1% | −1.6793 to +0.0793 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.800 (native is 0) | +29.6805 to +53.9195 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.22 | 11.4 | +11.6% | −0.8929 to +3.2696 | no |
| utilisation (used / allocatable) | 0.0596 | 0.06507 | +9.2% | −0.0016 to +0.0125 | no |
| CPU used (cores), mean | 1.43 | 1.398 | −2.3% | −0.0484 to −0.0167 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01677 | +0.017 (native is 0) | +0.0149 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.415 | −1.1% | −0.0310 to −0.0006 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 435.2 | −6.4% | −74.9072 to +15.8429 | no |
| HPA replicas, mean | 2.097 | 2.304 | +9.9% | −0.0898 to +0.5035 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | −0.0950 to +0.9950 | no |
| host CPU busy, the real machine under kind (%) | 40.58 | 40.87 | +0.7% | −0.1384 to +0.7184 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.5 | 761.5 | −0.8% | −14.1138 to +2.1138 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.924 | −17.9% | −2.0550 to −0.0979 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.0625 | +7.1% | −0.0434 to +0.0517 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.2 | 71.21 | −5.3% | −9.3041 to +1.3207 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*