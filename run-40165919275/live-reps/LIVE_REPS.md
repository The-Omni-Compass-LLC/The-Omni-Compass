# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.29 | 10.87 |
| node-hours | 5.023 | 5.029 | 4.315 | 4.547 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 524.4 | 523.3 | 524.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 524.4 | 469.6 | 488.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 381.7 | 596.3 | 365.8 | 641.9 |
| response time (ms), 95th percentile | 1442 | 2410 | 1562 | 2671 |
| response time (ms), 99th percentile | 2044 | 3310 | 2217 | 3794 |
| time over the response line (% of samples) | 13.97 | 19.25 | 14.93 | 22.32 |
| failed requests (%) | 0 | 0.007663 | 0 | 0.08713 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 10.9 | 9.4 | 11.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 113.2 | 91.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.19 | 14.19 | 9.318 | 15.42 |
| utilisation (used / allocatable) | 0.03078 | 0.03283 | 0.03674 | 0.03739 |
| CPU used (cores), mean | 1.477 | 1.576 | 1.483 | 1.628 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01231 | 0.01284 |
| CPU used with Omni's own (cores), mean | 1.477 | 1.576 | 1.495 | 1.641 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 872.5 | 828.3 | 762.1 | 736.4 |
| HPA replicas, mean | 3.956 | 4.093 | 4.719 | 4.693 |
| pods started | 0.1 | 0 | 0.9 | 1.5 |
| pod start wait, total (s) | 0.2 | 0 | 1.3 | 2.5 |
| pod start wait, mean (s) | 0.2 | 0 | 0.95 | 1.317 |
| host CPU busy, the real machine under kind (%) | 45.37 | 51.58 | 46.91 | 54.17 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 796.6 | 879.3 | 802.7 | 924.1 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.349 | 10.19 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 2.854 | 0.0625 | 8.579 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 28.3 | 0.4 | 59.1 |
| queue: job turnaround, submitted to done, mean (s) | 107.3 | 170.3 | 111.9 | 199.1 |
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
| worker nodes in service, mean | 12 | 10.87 | −9.5% | −2.4705 to +0.2016 | no |
| node-hours | 5.029 | 4.547 | −9.6% | −1.0446 to +0.0796 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 524.5 | +0.0% | −1.5517 to +1.9372 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 488.9 | −6.8% | −77.9179 to +7.0784 | no |
| response time (ms), mean | 596.3 | 641.9 | +7.6% | −6.3503 to +97.4985 | no |
| response time (ms), 95th percentile | 2410 | 2671 | +10.8% | +44.5861 to +475.6829 | yes: LOSS |
| response time (ms), 99th percentile | 3310 | 3794 | +14.6% | +109.5972 to +858.4808 | yes: LOSS |
| time over the response line (% of samples) | 19.25 | 22.32 | +15.9% | +0.0873 to +6.0469 | yes: LOSS |
| failed requests (%) | 0.007663 | 0.08713 | +1037.0% | −0.0533 to +0.2123 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.6 | +6.4% | −0.0578 to +1.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.6 | +91.600 (native is 0) | +56.1120 to +127.0880 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.19 | 15.42 | +8.6% | −0.1408 to +2.5941 | no |
| utilisation (used / allocatable) | 0.03283 | 0.03739 | +13.9% | +0.0008 to +0.0083 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.576 | 1.628 | +3.3% | +0.0003 to +0.1042 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01284 | +0.013 (native is 0) | +0.0118 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.576 | 1.641 | +4.1% | +0.0134 to +0.1169 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.3 | 736.4 | −11.1% | −170.7769 to −13.0544 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.093 | 4.693 | +14.7% | +0.1253 to +1.0745 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.8048 to +2.1952 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | +1.2726 to +3.7274 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.317 | +1.317 (native is 0) | +0.7734 to +1.8599 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.58 | 54.17 | +5.0% | +1.5576 to +3.6069 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 879.3 | 924.1 | +5.1% | +10.1278 to +79.4722 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.19 | −15.0% | −3.9100 to +0.2984 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 2.854 | 8.579 | +200.6% | −2.1736 to +13.6236 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 28.3 | 59.1 | +108.8% | −45.2874 to +106.8874 | no |
| queue: job turnaround, submitted to done, mean (s) | 170.3 | 199.1 | +16.9% | +7.9568 to +49.6849 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.023 | 5.029 | +0.1% | −0.0060 to +0.0180 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 524.4 | +0.4% | +0.2686 to +3.6098 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 524.4 | +0.4% | +0.2686 to +3.6098 | yes: power given |
| response time (ms), mean | 381.7 | 596.3 | +56.2% | +44.0302 to +385.2544 | yes: LOSS |
| response time (ms), 95th percentile | 1442 | 2410 | +67.2% | +197.6582 to +1740.0258 | yes: LOSS |
| response time (ms), 99th percentile | 2044 | 3310 | +61.9% | +229.9145 to +2301.8085 | yes: LOSS |
| time over the response line (% of samples) | 13.97 | 19.25 | +37.8% | +2.5661 to +7.9908 | yes: LOSS |
| failed requests (%) | 0 | 0.007663 | +0.008 (native is 0) | −0.0097 to +0.0250 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 10.9 | +39.7% | +1.4327 to +4.7673 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.19 | 14.19 | +39.2% | −0.3325 to +8.3258 | no |
| utilisation (used / allocatable) | 0.03078 | 0.03283 | +6.7% | +0.0008 to +0.0033 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.477 | 1.576 | +6.7% | +0.0364 to +0.1602 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.477 | 1.576 | +6.7% | +0.0364 to +0.1602 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 872.5 | 828.3 | −5.1% | −66.4214 to −21.9566 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.956 | 4.093 | +3.5% | −0.0837 to +0.3583 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 45.37 | 51.58 | +13.7% | +4.0092 to +8.4170 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.6 | 879.3 | +10.4% | +18.0861 to +147.3139 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 2.854 | +4792.9% | −2.9654 to +8.5571 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 28.3 | +6975.0% | −32.9487 to +88.7487 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.3 | 170.3 | +58.7% | +14.0426 to +111.9158 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.29 | −14.2% | −3.4653 to +0.0550 | no |
| node-hours | 5.023 | 4.315 | −14.1% | −1.4416 to +0.0240 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 523.3 | +0.2% | −0.9484 to +2.6776 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 469.6 | −10.1% | −107.6813 to +2.0897 | no |
| response time (ms), mean | 381.7 | 365.8 | −4.2% | −41.5408 to +9.7005 | no |
| response time (ms), 95th percentile | 1442 | 1562 | +8.4% | −19.4476 to +260.4916 | no |
| response time (ms), 99th percentile | 2044 | 2217 | +8.4% | −35.5217 to +380.5431 | no |
| time over the response line (% of samples) | 13.97 | 14.93 | +6.9% | −0.5610 to +2.4755 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 9.4 | +20.5% | −0.0927 to +3.2927 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.2 | +113.200 (native is 0) | +64.7725 to +161.6275 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.19 | 9.318 | −8.6% | −3.2025 to +1.4525 | no |
| utilisation (used / allocatable) | 0.03078 | 0.03674 | +19.4% | +0.0000 to +0.0119 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.477 | 1.483 | +0.4% | −0.0164 to +0.0277 | no |
| Omni's own CPU (cores), mean | 0 | 0.01231 | +0.012 (native is 0) | +0.0114 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.477 | 1.495 | +1.2% | −0.0043 to +0.0401 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 872.5 | 762.1 | −12.7% | −217.6101 to −3.1392 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.956 | 4.719 | +19.3% | +0.3664 to +1.1606 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | +0.2358 to +1.3642 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | +0.1796 to +2.0204 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.95 | +375.0% | −0.0972 to +1.5972 | no |
| host CPU busy, the real machine under kind (%) | 45.37 | 46.91 | +3.4% | +0.8795 to +2.1964 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.6 | 802.7 | +0.8% | −3.8827 to +16.0827 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.349 | −22.1% | −5.3160 to +0.0147 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.0625 | +7.1% | −0.0390 to +0.0474 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.3 | 111.9 | +4.3% | −2.4458 to +11.7041 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.29 | −14.2% | −3.4653 to +0.0550 | no |
| node-hours | 5.029 | 4.315 | −14.2% | −1.4511 to +0.0215 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 523.3 | −0.2% | −3.2715 to +1.1224 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 469.6 | −10.4% | −109.5435 to +0.0735 | no |
| response time (ms), mean | 596.3 | 365.8 | −38.7% | −399.5354 to −61.5896 | yes: GAIN |
| response time (ms), 95th percentile | 2410 | 1562 | −35.2% | −1584.2080 to −112.4320 | yes: GAIN |
| response time (ms), 99th percentile | 3310 | 2217 | −33.0% | −2077.3188 to −109.3828 | yes: GAIN |
| time over the response line (% of samples) | 19.25 | 14.93 | −22.4% | −6.6955 to −1.9469 | yes: GAIN |
| failed requests (%) | 0.007663 | 0 | −100.0% | −0.0250 to +0.0097 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 9.4 | −13.8% | −2.4079 to −0.5921 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.2 | +113.200 (native is 0) | +64.7725 to +161.6275 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.19 | 9.318 | −34.3% | −9.7543 to +0.0110 | no |
| utilisation (used / allocatable) | 0.03283 | 0.03674 | +11.9% | −0.0027 to +0.0105 | no |
| CPU used (cores), mean | 1.576 | 1.483 | −5.9% | −0.1451 to −0.0402 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01231 | +0.012 (native is 0) | +0.0114 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.576 | 1.495 | −5.1% | −0.1326 to −0.0281 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 828.3 | 762.1 | −8.0% | −177.1522 to +44.7808 | no |
| HPA replicas, mean | 4.093 | 4.719 | +15.3% | +0.2066 to +1.0457 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | +0.2737 to +1.5263 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | +0.4047 to +2.1953 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.95 | +0.950 (native is 0) | +0.2258 to +1.6742 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.58 | 46.91 | −9.1% | −6.6485 to −2.7018 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 879.3 | 802.7 | −8.7% | −136.2873 to −16.9127 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.349 | −22.1% | −5.3160 to +0.0147 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 2.854 | 0.0625 | −97.8% | −8.5331 to +2.9497 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 28.3 | 0.4 | −98.6% | −88.7487 to +32.9487 | no |
| queue: job turnaround, submitted to done, mean (s) | 170.3 | 111.9 | −34.3% | −105.6489 to −11.0511 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.87 | −9.5% | −2.4705 to +0.2016 | no |
| node-hours | 5.023 | 4.547 | −9.5% | −1.0333 to +0.0803 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.4 | 524.5 | +0.4% | +0.4422 to +3.8217 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.4 | 488.9 | −6.4% | −75.8457 to +8.8847 | no |
| response time (ms), mean | 381.7 | 641.9 | +68.2% | +60.2184 to +460.2144 | yes: LOSS |
| response time (ms), 95th percentile | 1442 | 2671 | +85.3% | +390.0733 to +2067.8797 | yes: LOSS |
| response time (ms), 99th percentile | 2044 | 3794 | +85.6% | +499.8350 to +2999.9660 | yes: LOSS |
| time over the response line (% of samples) | 13.97 | 22.32 | +59.7% | +3.4837 to +13.2073 | yes: LOSS |
| failed requests (%) | 0 | 0.08713 | +0.087 (native is 0) | −0.0442 to +0.2184 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 11.6 | +48.7% | +1.7268 to +5.8732 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.6 | +91.600 (native is 0) | +56.1120 to +127.0880 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.19 | 15.42 | +51.2% | +1.3118 to +9.1349 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03078 | 0.03739 | +21.5% | +0.0034 to +0.0098 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.477 | 1.628 | +10.2% | +0.0796 to +0.2216 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01284 | +0.013 (native is 0) | +0.0118 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.477 | 1.641 | +11.1% | +0.0924 to +0.2345 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 872.5 | 736.4 | −15.6% | −209.6095 to −62.5998 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.956 | 4.693 | +18.6% | +0.3387 to +1.1356 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.7089 to +2.0911 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.5 | +1150.0% | +1.1295 to +3.4705 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.317 | +558.3% | +0.5298 to +1.7035 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.37 | 54.17 | +19.4% | +6.1821 to +11.4086 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.6 | 924.1 | +16.0% | +33.9686 to +221.0314 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.19 | −15.0% | −3.9100 to +0.2984 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 8.579 | +14607.1% | −1.2611 to +18.3028 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 59.1 | +14675.0% | −9.8270 to +127.2270 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.3 | 199.1 | +85.5% | +27.8873 to +155.7127 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*