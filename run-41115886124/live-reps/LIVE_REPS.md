# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.51 | 1.51 | 1.508 | 1.509 | 1.509 | 1.51 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | 158.5 | 158.3 | 158.6 | 158.5 | 158.5 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | 158.5 | 158.3 | 158.6 | 158.5 | 158.5 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 159.1 | 80.92 | 81.01 | 80.87 | 81.49 | 81.82 | 81.17 | 82.17 |
| response time (ms), 95th percentile | 357.4 | 118 | 117.9 | 116.9 | 118.4 | 119.2 | 118 | 121.3 |
| response time (ms), 99th percentile | 557.1 | 155.5 | 154.4 | 156.7 | 153.4 | 160.2 | 162 | 163.7 |
| time over the response line (% of samples) | 2.488 | 0.01212 | 0 | 0.02432 | 0 | 0.01227 | 0.02439 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | 15.5 | 17.4 | 17.7 | 17.4 | 21.9 | 20.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 90 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.215 | 0.38 | 0.2733 | 0.02667 | 0.05333 | 0.3267 | 0.1933 |
| utilisation (used / allocatable) | 0.04004 | 0.03823 | 0.03799 | 0.03815 | 0.03854 | 0.03843 | 0.03802 | 0.03857 |
| CPU used (cores), mean | 0.961 | 0.9175 | 0.9117 | 0.9157 | 0.925 | 0.9223 | 0.9124 | 0.9257 |
| Omni's own CPU (cores), mean | 0 | 0.00897 | 0.0061 | 0.00694 | 0.00771 | 0.01414 | 0.02555 | 0.06966 |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9265 | 0.9178 | 0.9226 | 0.9328 | 0.9364 | 0.938 | 0.9954 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 731.9 | 731.9 | 730.5 | 721.1 | 734.1 | 737 | 724.9 |
| HPA replicas, mean | 8.578 | 8.374 | 8.42 | 8.405 | 8.035 | 7.985 | 9.03 | 8.954 |
| pods started | 4.5 | 4.1 | 3.7 | 3.8 | 3.1 | 2.9 | 4 | 3.3 |
| pod start wait, total (s) | 7.2 | 6.1 | 4.9 | 5.9 | 3.9 | 4.2 | 6.7 | 4.1 |
| pod start wait, mean (s) | 1.645 | 1.524 | 1.332 | 1.615 | 1.242 | 1.497 | 1.627 | 1.25 |
| host CPU busy, the real machine under kind (%) | 29.09 | 28.17 | 27.97 | 28.06 | 28.24 | 28.41 | 28.7 | 30.46 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.51 | −0.1% | −0.0025 to +0.0002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −0.6622 to −0.3620 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −0.6622 to −0.3620 | yes: GAIN |
| response time (ms), mean | 159.1 | 80.92 | −49.1% | −102.2450 to −54.1422 | yes: GAIN |
| response time (ms), 95th percentile | 357.4 | 118 | −67.0% | −304.2063 to −174.6237 | yes: GAIN |
| response time (ms), 99th percentile | 557.1 | 155.5 | −72.1% | −509.0967 to −294.0417 | yes: GAIN |
| time over the response line (% of samples) | 2.488 | 0.01212 | −99.5% | −3.8758 to −1.0754 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.7194 to −1.2806 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.7 | +18.700 (native is 0) | +15.3953 to +22.0047 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.215 | −34.5% | −0.4403 to +0.2136 | no |
| utilisation (used / allocatable) | 0.04004 | 0.03823 | −4.5% | −0.0026 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.9175 | −4.5% | −0.0630 to −0.0240 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00897 | +0.009 (native is 0) | +0.0076 to +0.0103 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9265 | −3.6% | −0.0530 to −0.0161 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 731.9 | +3.7% | +9.8516 to +42.8971 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.578 | 8.374 | −2.4% | −0.6854 to +0.2770 | no |
| pods started | 4.5 | 4.1 | −8.9% | −2.2835 to +1.4835 | no |
| pod start wait, total (s) | 7.2 | 6.1 | −15.3% | −4.3422 to +2.1422 | no |
| pod start wait, mean (s) | 1.645 | 1.524 | −7.3% | −0.3284 to +0.0869 | no |
| host CPU busy, the real machine under kind (%) | 29.09 | 28.17 | −3.2% | −1.4676 to −0.3861 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.51 | −0.0% | −0.0032 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −0.9224 to −0.0861 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −0.9224 to −0.0861 | yes: GAIN |
| response time (ms), mean | 159.1 | 81.01 | −49.1% | −102.2049 to −53.9876 | yes: GAIN |
| response time (ms), 95th percentile | 357.4 | 117.9 | −67.0% | −304.4360 to −174.6500 | yes: GAIN |
| response time (ms), 99th percentile | 557.1 | 154.4 | −72.3% | −510.8433 to −294.5689 | yes: GAIN |
| time over the response line (% of samples) | 2.488 | 0 | −100.0% | −3.8962 to −1.0792 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.7194 to −1.2806 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.5 | +15.500 (native is 0) | +14.3690 to +16.6310 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.38 | +15.7% | −0.3836 to +0.4870 | no |
| utilisation (used / allocatable) | 0.04004 | 0.03799 | −5.1% | −0.0031 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.9117 | −5.1% | −0.0750 to −0.0237 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0061 | +0.006 (native is 0) | +0.0053 to +0.0069 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9178 | −4.5% | −0.0681 to −0.0184 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 731.9 | +3.7% | +13.9329 to +38.8206 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.578 | 8.42 | −1.9% | −0.3668 to +0.0491 | no |
| pods started | 4.5 | 3.7 | −17.8% | −1.9583 to +0.3583 | no |
| pod start wait, total (s) | 7.2 | 4.9 | −31.9% | −4.5380 to −0.0620 | yes: GAIN |
| pod start wait, mean (s) | 1.645 | 1.332 | −19.0% | −0.5862 to −0.0404 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 29.09 | 27.97 | −3.9% | −1.8534 to −0.3983 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.508 | −0.2% | −0.0084 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.3 | −0.5% | −1.2057 to −0.2737 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.3 | −0.5% | −1.2057 to −0.2737 | yes: GAIN |
| response time (ms), mean | 159.1 | 80.87 | −49.2% | −102.3763 to −54.1124 | yes: GAIN |
| response time (ms), 95th percentile | 357.4 | 116.9 | −67.3% | −305.6100 to −175.4850 | yes: GAIN |
| response time (ms), 99th percentile | 557.1 | 156.7 | −71.9% | −506.3774 to −294.4164 | yes: GAIN |
| time over the response line (% of samples) | 2.488 | 0.02432 | −99.0% | −3.8656 to −1.0612 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.7194 to −1.2806 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.400 (native is 0) | +14.5547 to +20.2453 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.2733 | −16.8% | −0.4248 to +0.3148 | no |
| utilisation (used / allocatable) | 0.04004 | 0.03815 | −4.7% | −0.0028 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.9157 | −4.7% | −0.0670 to −0.0236 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00694 | +0.007 (native is 0) | +0.0059 to +0.0080 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9226 | −4.0% | −0.0592 to −0.0175 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 730.5 | +3.5% | +12.4406 to +37.4314 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.578 | 8.405 | −2.0% | −0.4170 to +0.0705 | no |
| pods started | 4.5 | 3.8 | −15.6% | −2.0509 to +0.6509 | no |
| pod start wait, total (s) | 7.2 | 5.9 | −18.1% | −3.8469 to +1.2469 | no |
| pod start wait, mean (s) | 1.645 | 1.615 | −1.8% | −0.3428 to +0.2828 | no |
| host CPU busy, the real machine under kind (%) | 29.09 | 28.06 | −3.6% | −1.7493 to −0.3223 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.509 | −0.1% | −0.0037 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | −0.3% | −0.8955 to −0.0590 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | −0.3% | −0.8955 to −0.0590 | yes: GAIN |
| response time (ms), mean | 159.1 | 81.49 | −48.8% | −102.6038 to −52.6379 | yes: GAIN |
| response time (ms), 95th percentile | 357.4 | 118.4 | −66.9% | −306.0344 to −172.0406 | yes: GAIN |
| response time (ms), 99th percentile | 557.1 | 153.4 | −72.5% | −517.0517 to −290.2965 | yes: GAIN |
| time over the response line (% of samples) | 2.488 | 0 | −100.0% | −3.8962 to −1.0792 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.7194 to −1.2806 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | +17.700 (native is 0) | +14.3104 to +21.0896 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.02667 | −91.9% | −0.6054 to +0.0020 | no |
| utilisation (used / allocatable) | 0.04004 | 0.03854 | −3.7% | −0.0028 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.925 | −3.7% | −0.0675 to −0.0045 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00771 | +0.008 (native is 0) | +0.0065 to +0.0090 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9328 | −2.9% | −0.0589 to +0.0024 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 721.1 | +2.2% | −19.9896 to +51.1185 | no |
| HPA replicas, mean | 8.578 | 8.035 | −6.3% | −1.0361 to −0.0516 | yes: GAIN |
| pods started | 4.5 | 3.1 | −31.1% | −2.8775 to +0.0775 | no |
| pod start wait, total (s) | 7.2 | 3.9 | −45.8% | −5.8691 to −0.7309 | yes: GAIN |
| pod start wait, mean (s) | 1.645 | 1.242 | −24.5% | −0.7199 to −0.0868 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 29.09 | 28.24 | −2.9% | −1.7738 to +0.0667 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.509 | −0.1% | −0.0027 to −0.0003 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −0.6698 to −0.3206 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −0.6698 to −0.3206 | yes: GAIN |
| response time (ms), mean | 159.1 | 81.82 | −48.6% | −100.6479 to −53.9377 | yes: GAIN |
| response time (ms), 95th percentile | 357.4 | 119.2 | −66.6% | −301.6923 to −174.7597 | yes: GAIN |
| response time (ms), 99th percentile | 557.1 | 160.2 | −71.2% | −500.2835 to −293.4705 | yes: GAIN |
| time over the response line (% of samples) | 2.488 | 0.01227 | −99.5% | −3.8755 to −1.0754 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.7194 to −1.2806 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.400 (native is 0) | +13.9911 to +20.8089 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.05333 | −83.8% | −0.6483 to +0.0983 | no |
| utilisation (used / allocatable) | 0.04004 | 0.03843 | −4.0% | −0.0023 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.9223 | −4.0% | −0.0547 to −0.0227 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01414 | +0.014 (native is 0) | +0.0120 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9364 | −2.6% | −0.0396 to −0.0095 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 734.1 | +4.0% | +16.1222 to +40.9342 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.578 | 7.985 | −6.9% | −1.2519 to +0.0657 | no |
| pods started | 4.5 | 2.9 | −35.6% | −3.0385 to −0.1615 | yes: GAIN |
| pod start wait, total (s) | 7.2 | 4.2 | −41.7% | −5.6764 to −0.3236 | yes: GAIN |
| pod start wait, mean (s) | 1.645 | 1.497 | −9.0% | −0.4986 to +0.2019 | no |
| host CPU busy, the real machine under kind (%) | 29.09 | 28.41 | −2.4% | −1.1979 to −0.1755 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.51 | −0.1% | −0.0023 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −0.7803 to −0.2371 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −0.7803 to −0.2371 | yes: GAIN |
| response time (ms), mean | 159.1 | 81.17 | −49.0% | −101.3140 to −54.5613 | yes: GAIN |
| response time (ms), 95th percentile | 357.4 | 118 | −67.0% | −303.5323 to −175.3517 | yes: GAIN |
| response time (ms), 99th percentile | 557.1 | 162 | −70.9% | −496.8929 to −293.3917 | yes: GAIN |
| time over the response line (% of samples) | 2.488 | 0.02439 | −99.0% | −3.8646 to −1.0621 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.7194 to −1.2806 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.9 | +21.900 (native is 0) | +16.2129 to +27.5871 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.3267 | −0.5% | −0.4877 to +0.4843 | no |
| utilisation (used / allocatable) | 0.04004 | 0.03802 | −5.1% | −0.0030 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.9124 | −5.1% | −0.0717 to −0.0255 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02555 | +0.026 (native is 0) | +0.0218 to +0.0293 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.938 | −2.4% | −0.0435 to −0.0026 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 737 | +4.5% | +11.1443 to +51.8059 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.578 | 9.03 | +5.3% | −0.2931 to +1.1956 | no |
| pods started | 4.5 | 4 | −11.1% | −2.6918 to +1.6918 | no |
| pod start wait, total (s) | 7.2 | 6.7 | −6.9% | −4.7952 to +3.7952 | no |
| pod start wait, mean (s) | 1.645 | 1.627 | −1.1% | −0.4317 to +0.3950 | no |
| host CPU busy, the real machine under kind (%) | 29.09 | 28.7 | −1.4% | −1.0866 to +0.2910 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.512 | +0.1% | +0.0007 to +0.0026 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.9 | −0.1% | −0.3605 to +0.1286 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.9 | −0.1% | −0.3605 to +0.1286 | no |
| response time (ms), mean | 159.1 | 82.17 | −48.4% | −100.4191 to −53.4564 | yes: GAIN |
| response time (ms), 95th percentile | 357.4 | 121.3 | −66.1% | −299.4335 to −172.9235 | yes: GAIN |
| response time (ms), 99th percentile | 557.1 | 163.7 | −70.6% | −495.5245 to −291.3015 | yes: GAIN |
| time over the response line (% of samples) | 2.488 | 0.01212 | −99.5% | −3.8817 to −1.0694 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | −100.0% | −4.7194 to −1.2806 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.2 | +20.200 (native is 0) | +17.5278 to +22.8722 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3283 | 0.1933 | −41.1% | −0.3745 to +0.1045 | no |
| utilisation (used / allocatable) | 0.04004 | 0.03857 | −3.7% | −0.0024 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.961 | 0.9257 | −3.7% | −0.0582 to −0.0124 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06966 | +0.070 (native is 0) | +0.0602 to +0.0791 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.961 | 0.9954 | +3.6% | +0.0173 to +0.0514 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.6 | 724.9 | +2.7% | +0.6451 to +37.9600 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.578 | 8.954 | +4.4% | +0.0587 to +0.6919 | yes: power given |
| pods started | 4.5 | 3.3 | −26.7% | −3.1604 to +0.7604 | no |
| pod start wait, total (s) | 7.2 | 4.1 | −43.1% | −5.5652 to −0.6348 | yes: GAIN |
| pod start wait, mean (s) | 1.645 | 1.25 | −24.0% | −0.7069 to −0.0831 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 29.09 | 30.46 | +4.7% | +1.0006 to +1.7280 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.51 | +0.0% | −0.0018 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.5 | +0.0% | −0.3315 to +0.3472 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.5 | +0.0% | −0.3315 to +0.3472 | no |
| response time (ms), mean | 80.92 | 81.01 | +0.1% | −0.8585 to +1.0532 | no |
| response time (ms), 95th percentile | 118 | 117.9 | −0.1% | −2.9515 to +2.6955 | no |
| response time (ms), 99th percentile | 155.5 | 154.4 | −0.7% | −9.2128 to +6.9390 | no |
| time over the response line (% of samples) | 0.01212 | 0 | −100.0% | −0.0395 to +0.0153 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 15.5 | −17.1% | −6.5347 to +0.1347 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.38 | +76.7% | −0.1582 to +0.4882 | no |
| utilisation (used / allocatable) | 0.03823 | 0.03799 | −0.6% | −0.0007 to +0.0002 | no |
| CPU used (cores), mean | 0.9175 | 0.9117 | −0.6% | −0.0174 to +0.0058 | no |
| Omni's own CPU (cores), mean | 0.00897 | 0.0061 | −32.0% | −0.0035 to −0.0023 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9265 | 0.9178 | −0.9% | −0.0208 to +0.0034 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 731.9 | +0.0% | −16.1738 to +16.1786 | no |
| HPA replicas, mean | 8.374 | 8.42 | +0.5% | −0.3845 to +0.4753 | no |
| pods started | 4.1 | 3.7 | −9.8% | −1.6251 to +0.8251 | no |
| pod start wait, total (s) | 6.1 | 4.9 | −19.7% | −3.1604 to +0.7604 | no |
| pod start wait, mean (s) | 1.524 | 1.332 | −12.6% | −0.4072 to +0.0219 | no |
| host CPU busy, the real machine under kind (%) | 28.17 | 27.97 | −0.7% | −0.5114 to +0.1135 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.508 | −0.1% | −0.0071 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.3 | −0.1% | −0.6728 to +0.2177 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.3 | −0.1% | −0.6728 to +0.2177 | no |
| response time (ms), mean | 80.92 | 80.87 | −0.1% | −1.0332 to +0.9317 | no |
| response time (ms), 95th percentile | 118 | 116.9 | −1.0% | −2.9583 to +0.6933 | no |
| response time (ms), 99th percentile | 155.5 | 156.7 | +0.8% | −6.3668 to +8.7114 | no |
| time over the response line (% of samples) | 0.01212 | 0.02432 | +100.6% | −0.0371 to +0.0615 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 17.4 | −7.0% | −5.1895 to +2.5895 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.2733 | +27.1% | −0.2462 to +0.3629 | no |
| utilisation (used / allocatable) | 0.03823 | 0.03815 | −0.2% | −0.0007 to +0.0005 | no |
| CPU used (cores), mean | 0.9175 | 0.9157 | −0.2% | −0.0158 to +0.0122 | no |
| Omni's own CPU (cores), mean | 0.00897 | 0.00694 | −22.6% | −0.0025 to −0.0015 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9265 | 0.9226 | −0.4% | −0.0181 to +0.0104 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 730.5 | −0.2% | −25.6973 to +22.8206 | no |
| HPA replicas, mean | 8.374 | 8.405 | +0.4% | −0.4024 to +0.4644 | no |
| pods started | 4.1 | 3.8 | −7.3% | −1.6509 to +1.0509 | no |
| pod start wait, total (s) | 6.1 | 5.9 | −3.3% | −2.9969 to +2.5969 | no |
| pod start wait, mean (s) | 1.524 | 1.615 | +6.0% | −0.3628 to +0.5443 | no |
| host CPU busy, the real machine under kind (%) | 28.17 | 28.06 | −0.4% | −0.5036 to +0.2858 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.509 | −0.0% | −0.0027 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.6 | +0.0% | −0.2943 to +0.3641 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.6 | +0.0% | −0.2943 to +0.3641 | no |
| response time (ms), mean | 80.92 | 81.49 | +0.7% | −1.1224 to +2.2679 | no |
| response time (ms), 95th percentile | 118 | 118.4 | +0.3% | −3.3502 to +4.1052 | no |
| response time (ms), 99th percentile | 155.5 | 153.4 | −1.4% | −11.0551 to +6.8453 | no |
| time over the response line (% of samples) | 0.01212 | 0 | −100.0% | −0.0395 to +0.0153 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 17.7 | −5.3% | −4.7092 to +2.7092 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.02667 | −87.6% | −0.4122 to +0.0355 | no |
| utilisation (used / allocatable) | 0.03823 | 0.03854 | +0.8% | −0.0005 to +0.0011 | no |
| CPU used (cores), mean | 0.9175 | 0.925 | +0.8% | −0.0108 to +0.0259 | no |
| Omni's own CPU (cores), mean | 0.00897 | 0.00771 | −14.0% | −0.0016 to −0.0009 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9265 | 0.9328 | +0.7% | −0.0121 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 721.1 | −1.5% | −32.7530 to +11.1332 | no |
| HPA replicas, mean | 8.374 | 8.035 | −4.1% | −0.7730 to +0.0937 | no |
| pods started | 4.1 | 3.1 | −24.4% | −2.1681 to +0.1681 | no |
| pod start wait, total (s) | 6.1 | 3.9 | −36.1% | −4.5313 to +0.1313 | no |
| pod start wait, mean (s) | 1.524 | 1.242 | −18.5% | −0.7135 to +0.1483 | no |
| host CPU busy, the real machine under kind (%) | 28.17 | 28.24 | +0.3% | −0.4163 to +0.5628 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.509 | −0.0% | −0.0020 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.5 | +0.0% | −0.1841 to +0.2180 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.5 | +0.0% | −0.1841 to +0.2180 | no |
| response time (ms), mean | 80.92 | 81.82 | +1.1% | −1.3988 to +3.2005 | no |
| response time (ms), 95th percentile | 118 | 119.2 | +1.0% | −3.0895 to +5.4675 | no |
| response time (ms), 99th percentile | 155.5 | 160.2 | +3.0% | −8.9223 to +18.3067 | no |
| time over the response line (% of samples) | 0.01212 | 0.01227 | +1.2% | −0.0002 to +0.0005 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 17.4 | −7.0% | −4.7725 to +2.1725 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.05333 | −75.2% | −0.3685 to +0.0451 | no |
| utilisation (used / allocatable) | 0.03823 | 0.03843 | +0.5% | −0.0006 to +0.0010 | no |
| CPU used (cores), mean | 0.9175 | 0.9223 | +0.5% | −0.0148 to +0.0244 | no |
| Omni's own CPU (cores), mean | 0.00897 | 0.01414 | +57.6% | +0.0043 to +0.0061 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9265 | 0.9364 | +1.1% | −0.0100 to +0.0300 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 734.1 | +0.3% | −15.3731 to +19.6808 | no |
| HPA replicas, mean | 8.374 | 7.985 | −4.6% | −0.8987 to +0.1210 | no |
| pods started | 4.1 | 2.9 | −29.3% | −2.2556 to −0.1444 | yes: GAIN |
| pod start wait, total (s) | 6.1 | 4.2 | −31.1% | −3.9909 to +0.1909 | no |
| pod start wait, mean (s) | 1.524 | 1.497 | −1.8% | −0.3632 to +0.3080 | no |
| host CPU busy, the real machine under kind (%) | 28.17 | 28.41 | +0.9% | −0.2345 to +0.7148 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.51 | +0.0% | −0.0010 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.5 | +0.0% | −0.1825 to +0.1893 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.5 | +0.0% | −0.1825 to +0.1893 | no |
| response time (ms), mean | 80.92 | 81.17 | +0.3% | −0.7553 to +1.2672 | no |
| response time (ms), 95th percentile | 118 | 118 | −0.0% | −2.1901 to +2.1361 | no |
| response time (ms), 99th percentile | 155.5 | 162 | +4.1% | −1.2765 to +14.1303 | no |
| time over the response line (% of samples) | 0.01212 | 0.02439 | +101.2% | −0.0520 to +0.0765 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 21.9 | +17.1% | −3.4830 to +9.8830 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.3267 | +51.9% | −0.1348 to +0.3582 | no |
| utilisation (used / allocatable) | 0.03823 | 0.03802 | −0.6% | −0.0005 to +0.0001 | no |
| CPU used (cores), mean | 0.9175 | 0.9124 | −0.6% | −0.0131 to +0.0029 | no |
| Omni's own CPU (cores), mean | 0.00897 | 0.02555 | +184.8% | +0.0141 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9265 | 0.938 | +1.2% | +0.0031 to +0.0199 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 737 | +0.7% | −2.0752 to +12.2767 | no |
| HPA replicas, mean | 8.374 | 9.03 | +7.8% | −0.1248 to +1.4357 | no |
| pods started | 4.1 | 4 | −2.4% | −1.8342 to +1.6342 | no |
| pod start wait, total (s) | 6.1 | 6.7 | +9.8% | −2.9558 to +4.1558 | no |
| pod start wait, mean (s) | 1.524 | 1.627 | +6.7% | −0.3607 to +0.5654 | no |
| host CPU busy, the real machine under kind (%) | 28.17 | 28.7 | +1.9% | +0.1451 to +0.9130 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.512 | +0.2% | +0.0015 to +0.0042 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.9 | +0.2% | +0.2289 to +0.5635 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.9 | +0.2% | +0.2289 to +0.5635 | yes: power given |
| response time (ms), mean | 80.92 | 82.17 | +1.6% | +0.4295 to +2.0821 | yes: LOSS |
| response time (ms), 95th percentile | 118 | 121.3 | +2.7% | +1.3005 to +5.1725 | yes: LOSS |
| response time (ms), 99th percentile | 155.5 | 163.7 | +5.2% | +0.2945 to +16.0179 | yes: LOSS |
| time over the response line (% of samples) | 0.01212 | 0.01212 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.7 | 20.2 | +8.0% | −3.1265 to +6.1265 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.1933 | −10.1% | −0.2406 to +0.1972 | no |
| utilisation (used / allocatable) | 0.03823 | 0.03857 | +0.9% | −0.0001 to +0.0008 | no |
| CPU used (cores), mean | 0.9175 | 0.9257 | +0.9% | −0.0032 to +0.0196 | no |
| Omni's own CPU (cores), mean | 0.00897 | 0.06966 | +676.6% | +0.0526 to +0.0688 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9265 | 0.9954 | +7.4% | +0.0551 to +0.0827 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 724.9 | −1.0% | −13.8383 to −0.3052 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.374 | 8.954 | +6.9% | +0.1152 to +1.0439 | yes: power given |
| pods started | 4.1 | 3.3 | −19.5% | −2.2621 to +0.6621 | no |
| pod start wait, total (s) | 6.1 | 4.1 | −32.8% | −3.9662 to −0.0338 | yes: GAIN |
| pod start wait, mean (s) | 1.524 | 1.25 | −18.0% | −0.6025 to +0.0539 | no |
| host CPU busy, the real machine under kind (%) | 28.17 | 30.46 | +8.1% | +1.8931 to +2.6893 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*