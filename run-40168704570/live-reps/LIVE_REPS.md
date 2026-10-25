# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.94 | 11.07 |
| node-hours | 5.026 | 5.032 | 4.593 | 4.645 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 527.7 | 526.8 | 527.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 527.7 | 493.4 | 498.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 598.2 | 801.8 | 570 | 887.9 |
| response time (ms), 95th percentile | 2391 | 4050 | 2502 | 4599 |
| response time (ms), 99th percentile | 3497 | 5741 | 3630 | 6354 |
| time over the response line (% of samples) | 26.32 | 25.87 | 25.66 | 27.36 |
| failed requests (%) | 0 | 0.01367 | 0.005602 | 0.1097 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 14.1 | 12.3 | 15 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 55.4 | 47.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.81 | 18.15 | 14.24 | 34.96 |
| utilisation (used / allocatable) | 0.03452 | 0.03686 | 0.0382 | 0.03882 |
| CPU used (cores), mean | 1.657 | 1.769 | 1.655 | 1.719 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01224 | 0.01001 |
| CPU used with Omni's own (cores), mean | 1.657 | 1.769 | 1.667 | 1.729 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.3 | 733.2 | 713.2 | 701.6 |
| HPA replicas, mean | 4.193 | 4.192 | 4.699 | 4.75 |
| pods started | 0 | 0.2 | 1.7 | 1.5 |
| pod start wait, total (s) | 0 | 0.4 | 2.5 | 2.9 |
| pod start wait, mean (s) | 0 | 0.4 | 1.2 | 1.7 |
| host CPU busy, the real machine under kind (%) | 50.05 | 57.06 | 51.62 | 60.45 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 861.5 | 985.2 | 874.7 | 1039 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.41 | 10.54 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.4208 | 0.05833 | 2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.1 | 0.6 | 2.3 |
| queue: job turnaround, submitted to done, mean (s) | 174.4 | 283.4 | 182.8 | 337.7 |
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
| worker nodes in service, mean | 12 | 11.07 | −7.7% | −2.3388 to +0.4804 | no |
| node-hours | 5.032 | 4.645 | −7.7% | −0.9810 to +0.2074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.7 | 527.3 | −0.1% | −2.0875 to +1.4155 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.7 | 498.1 | −5.6% | −74.2894 to +15.2424 | no |
| response time (ms), mean | 801.8 | 887.9 | +10.7% | +17.0003 to +155.2350 | yes: LOSS |
| response time (ms), 95th percentile | 4050 | 4599 | +13.5% | +205.8969 to +891.2601 | yes: LOSS |
| response time (ms), 99th percentile | 5741 | 6354 | +10.7% | +261.8555 to +962.7917 | yes: LOSS |
| time over the response line (% of samples) | 25.87 | 27.36 | +5.8% | +0.1217 to +2.8540 | yes: LOSS |
| failed requests (%) | 0.01367 | 0.1097 | +702.7% | +0.0069 to +0.1853 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 15 | +6.4% | +0.4940 to +1.3060 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 | +47.400 (native is 0) | +30.7771 to +64.0229 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.15 | 34.96 | +92.7% | +4.3181 to +29.3052 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03686 | 0.03882 | +5.3% | −0.0026 to +0.0066 | no |
| CPU used (cores), mean | 1.769 | 1.719 | −2.9% | −0.1254 to +0.0239 | no |
| Omni's own CPU (cores), mean | 0 | 0.01001 | +0.010 (native is 0) | +0.0089 to +0.0111 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.769 | 1.729 | −2.3% | −0.1158 to +0.0342 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.2 | 701.6 | −4.3% | −108.7683 to +45.6592 | no |
| HPA replicas, mean | 4.192 | 4.75 | +13.3% | +0.1642 to +0.9525 | yes: power given |
| pods started | 0.2 | 1.5 | +650.0% | +0.8172 to +1.7828 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.9 | +625.0% | +1.5315 to +3.4685 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.7 | +325.0% | +0.7111 to +1.8889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.06 | 60.45 | +6.0% | +2.5701 to +4.2229 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 985.2 | 1039 | +5.5% | +29.4450 to +77.9550 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.54 | −12.1% | −3.6536 to +0.7424 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4208 | 2 | +375.2% | −1.4589 to +4.6172 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 2.3 | +109.1% | −0.5456 to +2.9456 | no |
| queue: job turnaround, submitted to done, mean (s) | 283.4 | 337.7 | +19.1% | +31.4942 to +76.9808 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.026 | 5.032 | +0.1% | −0.0097 to +0.0217 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 527.7 | +0.5% | +0.6850 to +4.0707 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 527.7 | +0.5% | +0.6850 to +4.0707 | yes: power given |
| response time (ms), mean | 598.2 | 801.8 | +34.0% | +117.0971 to +290.2189 | yes: LOSS |
| response time (ms), 95th percentile | 2391 | 4050 | +69.4% | +1022.6502 to +2296.3498 | yes: LOSS |
| response time (ms), 99th percentile | 3497 | 5741 | +64.2% | +1369.6021 to +3119.8585 | yes: LOSS |
| time over the response line (% of samples) | 26.32 | 25.87 | −1.7% | −1.3935 to +0.4868 | no |
| failed requests (%) | 0 | 0.01367 | +0.014 (native is 0) | −0.0070 to +0.0343 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 14.1 | +16.5% | +1.1740 to +2.8260 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.81 | 18.14 | +31.3% | +1.9289 to +6.7311 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03452 | 0.03686 | +6.8% | +0.0016 to +0.0031 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.657 | 1.769 | +6.8% | +0.0760 to +0.1488 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.657 | 1.769 | +6.8% | +0.0760 to +0.1488 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.3 | 733.2 | −5.6% | −53.8521 to −32.3169 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.193 | 4.192 | −0.0% | −0.3625 to +0.3606 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 50.05 | 57.06 | +14.0% | +5.4147 to +8.5976 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 861.5 | 985.2 | +14.4% | +76.7711 to +170.6289 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.4208 | +405.0% | +0.2147 to +0.4603 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.1 | +83.3% | +0.1230 to +0.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 174.4 | 283.4 | +62.5% | +66.6331 to +151.5002 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.94 | −8.8% | −2.6590 to +0.5390 | no |
| node-hours | 5.026 | 4.593 | −8.6% | −1.1061 to +0.2409 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 526.8 | +0.3% | +0.4143 to +2.5595 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 493.4 | −6.1% | −82.4906 to +18.7686 | no |
| response time (ms), mean | 598.2 | 570 | −4.7% | −48.1129 to −8.1453 | yes: GAIN |
| response time (ms), 95th percentile | 2391 | 2502 | +4.7% | +21.1692 to +201.3538 | yes: LOSS |
| response time (ms), 99th percentile | 3497 | 3630 | +3.8% | −83.9617 to +350.2435 | no |
| time over the response line (% of samples) | 26.32 | 25.66 | −2.5% | −1.2334 to −0.0816 | yes: GAIN |
| failed requests (%) | 0 | 0.005602 | +0.006 (native is 0) | −0.0071 to +0.0183 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 12.3 | +1.7% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.4 | +55.400 (native is 0) | +32.5022 to +78.2978 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.81 | 14.24 | +3.1% | −3.6713 to +4.5246 | no |
| utilisation (used / allocatable) | 0.03452 | 0.0382 | +10.7% | −0.0015 to +0.0089 | no |
| CPU used (cores), mean | 1.657 | 1.655 | −0.1% | −0.0257 to +0.0221 | no |
| Omni's own CPU (cores), mean | 0 | 0.01224 | +0.012 (native is 0) | +0.0115 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.657 | 1.667 | +0.6% | −0.0137 to +0.0345 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.3 | 713.2 | −8.1% | −151.7172 to +25.6024 | no |
| HPA replicas, mean | 4.193 | 4.699 | +12.1% | +0.0062 to +1.0070 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.9422 to +2.4578 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | +1.1832 to +3.8168 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.6358 to +1.7642 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.05 | 51.62 | +3.1% | +1.1289 to +2.0086 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 861.5 | 874.7 | +1.5% | +5.1934 to +21.2066 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.41 | −13.3% | −3.9975 to +0.8097 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.05833 | −30.0% | −0.0600 to +0.0100 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 174.4 | 182.8 | +4.8% | +2.0279 to +14.7471 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.94 | −8.8% | −2.6590 to +0.5390 | no |
| node-hours | 5.032 | 4.593 | −8.7% | −1.1125 to +0.2352 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.7 | 526.8 | −0.2% | −2.4832 to +0.7013 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.7 | 493.4 | −6.5% | −84.5598 to +16.0821 | no |
| response time (ms), mean | 801.8 | 570 | −28.9% | −318.3259 to −145.2483 | yes: GAIN |
| response time (ms), 95th percentile | 4050 | 2502 | −38.2% | −2156.9739 to −939.5031 | yes: GAIN |
| response time (ms), 99th percentile | 5741 | 3630 | −36.8% | −2953.6738 to −1269.5050 | yes: GAIN |
| time over the response line (% of samples) | 25.87 | 25.66 | −0.8% | −0.9358 to +0.5275 | no |
| failed requests (%) | 0.01367 | 0.005602 | −59.0% | −0.0340 to +0.0179 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 12.3 | −12.8% | −2.5388 to −1.0612 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.4 | +55.400 (native is 0) | +32.5022 to +78.2978 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.15 | 14.24 | −21.5% | −6.5496 to −1.2571 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03686 | 0.0382 | +3.6% | −0.0045 to +0.0071 | no |
| CPU used (cores), mean | 1.769 | 1.655 | −6.5% | −0.1417 to −0.0868 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01224 | +0.012 (native is 0) | +0.0115 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.769 | 1.667 | −5.8% | −0.1297 to −0.0742 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733.2 | 713.2 | −2.7% | −113.7356 to +73.7899 | no |
| HPA replicas, mean | 4.192 | 4.699 | +12.1% | +0.1338 to +0.8813 | yes: power given |
| pods started | 0.2 | 1.7 | +750.0% | +0.8048 to +2.1952 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.5 | +525.0% | +0.8182 to +3.3818 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.2 | +200.0% | +0.0612 to +1.5388 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.06 | 51.62 | −9.5% | −6.8411 to −4.0336 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 985.2 | 874.7 | −11.2% | −152.3918 to −68.6082 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.41 | −13.3% | −3.9975 to +0.8097 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4208 | 0.05833 | −86.1% | −0.4732 to −0.2518 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.6 | −45.5% | −0.8770 to −0.1230 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 283.4 | 182.8 | −35.5% | −139.3701 to −61.9883 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.07 | −7.7% | −2.3388 to +0.4804 | no |
| node-hours | 5.026 | 4.645 | −7.6% | −0.9745 to +0.2128 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 527.3 | +0.4% | +0.7635 to +3.3202 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 498.1 | −5.2% | −72.1626 to +17.8712 | no |
| response time (ms), mean | 598.2 | 887.9 | +48.4% | +153.6415 to +425.9097 | yes: LOSS |
| response time (ms), 95th percentile | 2391 | 4599 | +92.4% | +1344.9197 to +3071.2373 | yes: LOSS |
| response time (ms), 99th percentile | 3497 | 6354 | +81.7% | +1743.6264 to +3970.4814 | yes: LOSS |
| time over the response line (% of samples) | 26.32 | 27.36 | +3.9% | −0.7985 to +2.8674 | no |
| failed requests (%) | 0 | 0.1097 | +0.110 (native is 0) | +0.0117 to +0.2078 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 15 | +24.0% | +1.9198 to +3.8802 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.4 | +47.400 (native is 0) | +30.7771 to +64.0229 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.81 | 34.96 | +153.0% | +7.6941 to +34.5893 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03452 | 0.03882 | +12.5% | +0.0002 to +0.0084 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.657 | 1.719 | +3.7% | −0.0320 to +0.1552 | no |
| Omni's own CPU (cores), mean | 0 | 0.01001 | +0.010 (native is 0) | +0.0089 to +0.0111 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.657 | 1.729 | +4.3% | −0.0226 to +0.1658 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 776.3 | 701.6 | −9.6% | −147.3952 to −1.8829 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.193 | 4.75 | +13.3% | +0.1188 to +0.9960 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.9942 to +2.0058 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.900 (native is 0) | +1.6182 to +4.1818 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.7 | +1.700 (native is 0) | +1.1111 to +2.2889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.05 | 60.45 | +20.8% | +8.1984 to +12.6068 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 861.5 | 1039 | +20.6% | +109.9777 to +244.8223 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.54 | −12.1% | −3.6536 to +0.7424 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 2 | +2300.0% | −1.1861 to +5.0195 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 2.3 | +283.3% | +0.0463 to +3.3537 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 174.4 | 337.7 | +93.7% | +101.1153 to +225.4931 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*