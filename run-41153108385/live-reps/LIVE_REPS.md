# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.513 | 1.512 | 1.512 | 1.511 | 1.512 | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | 157.7 | 157.7 | 157.6 | 157.7 | 157.8 | 158 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | 157.7 | 157.7 | 157.6 | 157.7 | 157.8 | 158 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 132.6 | 70.09 | 69.67 | 70.15 | 69.83 | 70.42 | 70.65 | 71.5 |
| response time (ms), 95th percentile | 297.7 | 105.6 | 104.9 | 106.1 | 104.4 | 106.2 | 107.2 | 109 |
| response time (ms), 99th percentile | 486 | 140.7 | 137.6 | 143.3 | 139.5 | 141 | 148.9 | 149.6 |
| time over the response line (% of samples) | 1.849 | 0 | 0.01212 | 0 | 0 | 0 | 0.01212 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | 13.5 | 17.3 | 15 | 14.6 | 20.2 | 19.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.315 | 0.185 | 0.3167 | 0.1783 | 0.2617 | 0.4883 | 0.1567 |
| utilisation (used / allocatable) | 0.03462 | 0.03327 | 0.03309 | 0.03318 | 0.03314 | 0.03339 | 0.03359 | 0.03396 |
| CPU used (cores), mean | 0.831 | 0.7984 | 0.7942 | 0.7963 | 0.7953 | 0.8014 | 0.8062 | 0.815 |
| Omni's own CPU (cores), mean | 0 | 0.00833 | 0.00561 | 0.00654 | 0.007 | 0.01311 | 0.02395 | 0.06592 |
| CPU used with Omni's own (cores), mean | 0.831 | 0.8067 | 0.7998 | 0.8028 | 0.8023 | 0.8145 | 0.8301 | 0.8809 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 857.3 | 868.6 | 863.1 | 872.1 | 860.5 | 855.7 | 846.6 |
| HPA replicas, mean | 7.857 | 7.811 | 7.478 | 7.914 | 6.811 | 6.968 | 7.914 | 8.09 |
| pods started | 5.2 | 3.9 | 3 | 4.3 | 3.6 | 3 | 4.1 | 3.6 |
| pod start wait, total (s) | 7.7 | 6.1 | 3.4 | 6.4 | 5.5 | 4.3 | 7.4 | 4.7 |
| pod start wait, mean (s) | 1.495 | 1.647 | 1.217 | 1.489 | 1.552 | 1.497 | 1.842 | 1.373 |
| host CPU busy, the real machine under kind (%) | 25.52 | 24.81 | 24.55 | 24.72 | 24.58 | 24.96 | 25.41 | 27.19 |
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
| node-hours | 1.511 | 1.513 | +0.1% | −0.0012 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.6515 to +0.2499 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.6515 to +0.2499 | no |
| response time (ms), mean | 132.6 | 70.09 | −47.1% | −92.5566 to −32.5044 | yes: GAIN |
| response time (ms), 95th percentile | 297.7 | 105.6 | −64.5% | −274.7002 to −109.6548 | yes: GAIN |
| response time (ms), 99th percentile | 486 | 140.7 | −71.1% | −481.8597 to −208.7539 | yes: GAIN |
| time over the response line (% of samples) | 1.849 | 0 | −100.0% | −3.1807 to −0.5172 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.1260 to −0.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | +16.900 (native is 0) | +14.8365 to +18.9635 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.315 | +68.7% | −0.2634 to +0.5200 | no |
| utilisation (used / allocatable) | 0.03462 | 0.03327 | −3.9% | −0.0028 to +0.0001 | no |
| CPU used (cores), mean | 0.831 | 0.7984 | −3.9% | −0.0668 to +0.0016 | no |
| Omni's own CPU (cores), mean | 0 | 0.00833 | +0.008 (native is 0) | +0.0068 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.831 | 0.8067 | −2.9% | −0.0572 to +0.0086 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 857.3 | +1.2% | −23.3593 to +44.3297 | no |
| HPA replicas, mean | 7.857 | 7.811 | −0.6% | −0.4250 to +0.3316 | no |
| pods started | 5.2 | 3.9 | −25.0% | −2.4209 to −0.1791 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 6.1 | −20.8% | −3.9410 to +0.7410 | no |
| pod start wait, mean (s) | 1.495 | 1.647 | +10.1% | −0.0880 to +0.3913 | no |
| host CPU busy, the real machine under kind (%) | 25.52 | 24.81 | −2.8% | −1.6070 to +0.1731 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0007 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.2% | −0.5591 to +0.0303 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.2% | −0.5591 to +0.0303 | no |
| response time (ms), mean | 132.6 | 69.67 | −47.5% | −92.5013 to −33.4091 | yes: GAIN |
| response time (ms), 95th percentile | 297.7 | 104.9 | −64.8% | −274.9874 to −110.6626 | yes: GAIN |
| response time (ms), 99th percentile | 486 | 137.6 | −71.7% | −485.7201 to −211.1267 | yes: GAIN |
| time over the response line (% of samples) | 1.849 | 0.01212 | −99.3% | −3.1573 to −0.5164 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.1260 to −0.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.5 | +13.500 (native is 0) | +11.7078 to +15.2922 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.185 | −0.9% | −0.3251 to +0.3218 | no |
| utilisation (used / allocatable) | 0.03462 | 0.03309 | −4.4% | −0.0027 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.831 | 0.7942 | −4.4% | −0.0641 to −0.0094 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00561 | +0.006 (native is 0) | +0.0046 to +0.0066 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.831 | 0.7998 | −3.7% | −0.0576 to −0.0046 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 868.6 | +2.6% | −1.1354 to +44.6799 | no |
| HPA replicas, mean | 7.857 | 7.478 | −4.8% | −1.2769 to +0.5189 | no |
| pods started | 5.2 | 3 | −42.3% | −3.4526 to −0.9474 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 3.4 | −55.8% | −6.6855 to −1.9145 | yes: GAIN |
| pod start wait, mean (s) | 1.495 | 1.217 | −18.6% | −0.6056 to +0.0489 | no |
| host CPU busy, the real machine under kind (%) | 25.52 | 24.55 | −3.8% | −1.7625 to −0.1852 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0012 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.6228 to +0.1503 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.6228 to +0.1503 | no |
| response time (ms), mean | 132.6 | 70.15 | −47.1% | −92.0978 to −32.8441 | yes: GAIN |
| response time (ms), 95th percentile | 297.7 | 106.1 | −64.4% | −273.2841 to −110.0679 | yes: GAIN |
| response time (ms), 99th percentile | 486 | 143.3 | −70.5% | −477.4900 to −207.8060 | yes: GAIN |
| time over the response line (% of samples) | 1.849 | 0 | −100.0% | −3.1807 to −0.5172 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.1260 to −0.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.3 | +17.300 (native is 0) | +15.7166 to +18.8834 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.3167 | +69.6% | −0.2640 to +0.5240 | no |
| utilisation (used / allocatable) | 0.03462 | 0.03318 | −4.2% | −0.0026 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.831 | 0.7963 | −4.2% | −0.0633 to −0.0062 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00654 | +0.007 (native is 0) | +0.0054 to +0.0077 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.831 | 0.8028 | −3.4% | −0.0558 to −0.0006 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 863.1 | +1.9% | −5.4185 to +37.9198 | no |
| HPA replicas, mean | 7.857 | 7.914 | +0.7% | −0.2517 to +0.3653 | no |
| pods started | 5.2 | 4.3 | −17.3% | −2.2676 to +0.4676 | no |
| pod start wait, total (s) | 7.7 | 6.4 | −16.9% | −3.7093 to +1.1093 | no |
| pod start wait, mean (s) | 1.495 | 1.489 | −0.4% | −0.3465 to +0.3336 | no |
| host CPU busy, the real machine under kind (%) | 25.52 | 24.72 | −3.1% | −1.6797 to +0.0832 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.511 | =0.0% | −0.0014 to +0.0014 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.6 | −0.2% | −0.5831 to −0.0175 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.6 | −0.2% | −0.5831 to −0.0175 | yes: GAIN |
| response time (ms), mean | 132.6 | 69.83 | −47.3% | −92.0546 to −33.5277 | yes: GAIN |
| response time (ms), 95th percentile | 297.7 | 104.4 | −64.9% | −274.7560 to −111.8490 | yes: GAIN |
| response time (ms), 99th percentile | 486 | 139.5 | −71.3% | −479.2735 to −213.7795 | yes: GAIN |
| time over the response line (% of samples) | 1.849 | 0 | −100.0% | −3.1807 to −0.5172 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.1260 to −0.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 | +15.000 (native is 0) | +11.5945 to +18.4055 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1783 | −4.5% | −0.3128 to +0.2961 | no |
| utilisation (used / allocatable) | 0.03462 | 0.03314 | −4.3% | −0.0024 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.831 | 0.7953 | −4.3% | −0.0575 to −0.0138 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.007 | +0.007 (native is 0) | +0.0055 to +0.0085 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.831 | 0.8023 | −3.4% | −0.0493 to −0.0081 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 872.1 | +3.0% | +11.9711 to +38.5354 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.857 | 6.811 | −13.3% | −1.6854 to −0.4075 | yes: GAIN |
| pods started | 5.2 | 3.6 | −30.8% | −2.6228 to −0.5772 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 5.5 | −28.6% | −4.4570 to +0.0570 | no |
| pod start wait, mean (s) | 1.495 | 1.552 | +3.8% | −0.2993 to +0.4126 | no |
| host CPU busy, the real machine under kind (%) | 25.52 | 24.58 | −3.7% | −1.5332 to −0.3524 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.512 | +0.0% | −0.0012 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.7 | −0.1% | −0.5448 to +0.1127 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.7 | −0.1% | −0.5448 to +0.1127 | no |
| response time (ms), mean | 132.6 | 70.42 | −46.9% | −91.5641 to −32.8374 | yes: GAIN |
| response time (ms), 95th percentile | 297.7 | 106.2 | −64.3% | −273.2028 to −109.8862 | yes: GAIN |
| response time (ms), 99th percentile | 486 | 141 | −71.0% | −478.3667 to −211.6533 | yes: GAIN |
| time over the response line (% of samples) | 1.849 | 0 | −100.0% | −3.1807 to −0.5172 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.1260 to −0.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.6 | +14.600 (native is 0) | +11.0925 to +18.1075 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2617 | +40.2% | −0.2101 to +0.3601 | no |
| utilisation (used / allocatable) | 0.03462 | 0.03339 | −3.6% | −0.0023 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.831 | 0.8014 | −3.6% | −0.0559 to −0.0033 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01311 | +0.013 (native is 0) | +0.0105 to +0.0157 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.831 | 0.8145 | −2.0% | −0.0406 to +0.0076 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 860.5 | +1.6% | −9.8373 to +37.2835 | no |
| HPA replicas, mean | 7.857 | 6.968 | −11.3% | −1.6011 to −0.1780 | yes: GAIN |
| pods started | 5.2 | 3 | −42.3% | −2.8573 to −1.5427 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 4.3 | −44.2% | −4.6707 to −2.1293 | yes: GAIN |
| pod start wait, mean (s) | 1.495 | 1.497 | +0.1% | −0.2765 to +0.2799 | no |
| host CPU busy, the real machine under kind (%) | 25.52 | 24.96 | −2.2% | −1.2245 to +0.1091 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.513 | +0.1% | −0.0010 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.8 | −0.1% | −0.4887 to +0.3119 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.8 | −0.1% | −0.4887 to +0.3119 | no |
| response time (ms), mean | 132.6 | 70.65 | −46.7% | −91.3302 to −32.6159 | yes: GAIN |
| response time (ms), 95th percentile | 297.7 | 107.2 | −64.0% | −271.7394 to −109.3116 | yes: GAIN |
| response time (ms), 99th percentile | 486 | 148.9 | −69.4% | −464.7797 to −209.3281 | yes: GAIN |
| time over the response line (% of samples) | 1.849 | 0.01212 | −99.3% | −3.1577 to −0.5160 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.1260 to −0.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.2 | +20.200 (native is 0) | +17.8687 to +22.5313 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.4883 | +161.6% | −0.1209 to +0.7243 | no |
| utilisation (used / allocatable) | 0.03462 | 0.03359 | −3.0% | −0.0021 to +0.0001 | no |
| CPU used (cores), mean | 0.831 | 0.8062 | −3.0% | −0.0511 to +0.0015 | no |
| Omni's own CPU (cores), mean | 0 | 0.02395 | +0.024 (native is 0) | +0.0195 to +0.0284 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.831 | 0.8301 | −0.1% | −0.0238 to +0.0220 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 855.7 | +1.1% | −11.6306 to +29.4640 | no |
| HPA replicas, mean | 7.857 | 7.914 | +0.7% | −0.1091 to +0.2220 | no |
| pods started | 5.2 | 4.1 | −21.2% | −1.8872 to −0.3128 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 7.4 | −3.9% | −2.0210 to +1.4210 | no |
| pod start wait, mean (s) | 1.495 | 1.842 | +23.2% | +0.0492 to +0.6441 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 25.52 | 25.41 | −0.4% | −0.8081 to +0.5871 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.514 | +0.2% | +0.0011 to +0.0043 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 158 | +0.1% | −0.1848 to +0.4004 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 158 | +0.1% | −0.1848 to +0.4004 | no |
| response time (ms), mean | 132.6 | 71.5 | −46.1% | −90.1382 to −32.1188 | yes: GAIN |
| response time (ms), 95th percentile | 297.7 | 109 | −63.4% | −268.6877 to −108.8523 | yes: GAIN |
| response time (ms), 99th percentile | 486 | 149.6 | −69.2% | −466.6307 to −206.1315 | yes: GAIN |
| time over the response line (% of samples) | 1.849 | 0 | −100.0% | −3.1807 to −0.5172 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.4 | 0 | −100.0% | −4.1260 to −0.6740 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +17.8283 to +20.7717 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1567 | −16.1% | −0.2583 to +0.1983 | no |
| utilisation (used / allocatable) | 0.03462 | 0.03396 | −1.9% | −0.0017 to +0.0004 | no |
| CPU used (cores), mean | 0.831 | 0.815 | −1.9% | −0.0415 to +0.0096 | no |
| Omni's own CPU (cores), mean | 0 | 0.06592 | +0.066 (native is 0) | +0.0539 to +0.0779 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.831 | 0.8809 | +6.0% | +0.0317 to +0.0683 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 846.8 | 846.6 | −0.0% | −28.6786 to +28.2204 | no |
| HPA replicas, mean | 7.857 | 8.09 | +3.0% | −0.0794 to +0.5445 | no |
| pods started | 5.2 | 3.6 | −30.8% | −2.8251 to −0.3749 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 4.7 | −39.0% | −4.6519 to −1.3481 | yes: GAIN |
| pod start wait, mean (s) | 1.495 | 1.373 | −8.1% | −0.3613 to +0.1180 | no |
| host CPU busy, the real machine under kind (%) | 25.52 | 27.19 | +6.5% | +1.1040 to +2.2346 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.512 | −0.0% | −0.0021 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.7 | −0.0% | −0.3165 to +0.1892 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.7 | −0.0% | −0.3165 to +0.1892 | no |
| response time (ms), mean | 70.09 | 69.67 | −0.6% | −1.2018 to +0.3523 | no |
| response time (ms), 95th percentile | 105.6 | 104.9 | −0.6% | −2.1832 to +0.8882 | no |
| response time (ms), 99th percentile | 140.7 | 137.6 | −2.2% | −13.9542 to +7.7210 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 13.5 | −20.1% | −5.2531 to −1.5469 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.185 | −41.3% | −0.4009 to +0.1409 | no |
| utilisation (used / allocatable) | 0.03327 | 0.03309 | −0.5% | −0.0007 to +0.0004 | no |
| CPU used (cores), mean | 0.7984 | 0.7942 | −0.5% | −0.0178 to +0.0095 | no |
| Omni's own CPU (cores), mean | 0.00833 | 0.00561 | −32.7% | −0.0033 to −0.0022 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8067 | 0.7998 | −0.8% | −0.0203 to +0.0066 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.3 | 868.6 | +1.3% | −4.0945 to +26.6685 | no |
| HPA replicas, mean | 7.811 | 7.478 | −4.3% | −1.0371 to +0.3726 | no |
| pods started | 3.9 | 3 | −23.1% | −2.0898 to +0.2898 | no |
| pod start wait, total (s) | 6.1 | 3.4 | −44.3% | −4.8072 to −0.5928 | yes: GAIN |
| pod start wait, mean (s) | 1.647 | 1.217 | −26.1% | −0.7633 to −0.0967 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 24.81 | 24.55 | −1.0% | −0.4811 to −0.0327 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.512 | −0.0% | −0.0014 to +0.0008 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.7 | −0.0% | −0.1784 to +0.1075 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.7 | −0.0% | −0.1784 to +0.1075 | no |
| response time (ms), mean | 70.09 | 70.15 | +0.1% | −0.7925 to +0.9115 | no |
| response time (ms), 95th percentile | 105.6 | 106.1 | +0.5% | −1.0891 to +2.0921 | no |
| response time (ms), 99th percentile | 140.7 | 143.3 | +1.9% | −8.9115 to +14.2291 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 17.3 | +2.4% | −2.1053 to +2.9053 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.3167 | +0.5% | −0.3060 to +0.3094 | no |
| utilisation (used / allocatable) | 0.03327 | 0.03318 | −0.3% | −0.0006 to +0.0004 | no |
| CPU used (cores), mean | 0.7984 | 0.7963 | −0.3% | −0.0139 to +0.0097 | no |
| Omni's own CPU (cores), mean | 0.00833 | 0.00654 | −21.5% | −0.0023 to −0.0013 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8067 | 0.8028 | −0.5% | −0.0155 to +0.0078 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.3 | 863.1 | +0.7% | −14.2819 to +25.8127 | no |
| HPA replicas, mean | 7.811 | 7.914 | +1.3% | −0.2842 to +0.4912 | no |
| pods started | 3.9 | 4.3 | +10.3% | −0.3689 to +1.1689 | no |
| pod start wait, total (s) | 6.1 | 6.4 | +4.9% | −1.8072 to +2.4072 | no |
| pod start wait, mean (s) | 1.647 | 1.489 | −9.6% | −0.4510 to +0.1348 | no |
| host CPU busy, the real machine under kind (%) | 24.81 | 24.72 | −0.3% | −0.3366 to +0.1739 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.511 | −0.1% | −0.0029 to +0.0005 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.6 | −0.1% | −0.3422 to +0.1431 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.6 | −0.1% | −0.3422 to +0.1431 | no |
| response time (ms), mean | 70.09 | 69.83 | −0.4% | −1.4489 to +0.9275 | no |
| response time (ms), 95th percentile | 105.6 | 104.4 | −1.1% | −2.8878 to +0.6378 | no |
| response time (ms), 99th percentile | 140.7 | 139.5 | −0.9% | −8.1059 to +5.6665 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 15 | −11.2% | −4.9618 to +1.1618 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.1783 | −43.4% | −0.4653 to +0.1919 | no |
| utilisation (used / allocatable) | 0.03327 | 0.03314 | −0.4% | −0.0009 to +0.0006 | no |
| CPU used (cores), mean | 0.7984 | 0.7953 | −0.4% | −0.0214 to +0.0153 | no |
| Omni's own CPU (cores), mean | 0.00833 | 0.007 | −16.0% | −0.0016 to −0.0011 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8067 | 0.8023 | −0.5% | −0.0227 to +0.0140 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.3 | 872.1 | +1.7% | −10.0217 to +39.5578 | no |
| HPA replicas, mean | 7.811 | 6.811 | −12.8% | −1.6039 to −0.3956 | yes: GAIN |
| pods started | 3.9 | 3.6 | −7.7% | −2.0210 to +1.4210 | no |
| pod start wait, total (s) | 6.1 | 5.5 | −9.8% | −3.1945 to +1.9945 | no |
| pod start wait, mean (s) | 1.647 | 1.552 | −5.8% | −0.4195 to +0.2295 | no |
| host CPU busy, the real machine under kind (%) | 24.81 | 24.58 | −0.9% | −0.6233 to +0.1716 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.512 | −0.0% | −0.0019 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.7 | −0.0% | −0.1809 to +0.1504 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.7 | −0.0% | −0.1809 to +0.1504 | no |
| response time (ms), mean | 70.09 | 70.42 | +0.5% | −0.7252 to +1.3846 | no |
| response time (ms), 95th percentile | 105.6 | 106.2 | +0.6% | −1.2324 to +2.4984 | no |
| response time (ms), 99th percentile | 140.7 | 141 | +0.2% | −7.4852 to +8.0788 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 14.6 | −13.6% | −5.3544 to +0.7544 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.2617 | −16.9% | −0.3306 to +0.2239 | no |
| utilisation (used / allocatable) | 0.03327 | 0.03339 | +0.4% | −0.0003 to +0.0006 | no |
| CPU used (cores), mean | 0.7984 | 0.8014 | +0.4% | −0.0082 to +0.0142 | no |
| Omni's own CPU (cores), mean | 0.00833 | 0.01311 | +57.4% | +0.0037 to +0.0058 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8067 | 0.8145 | +1.0% | −0.0042 to +0.0198 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.3 | 860.5 | +0.4% | −8.3026 to +14.7783 | no |
| HPA replicas, mean | 7.811 | 6.968 | −10.8% | −1.4183 to −0.2674 | yes: GAIN |
| pods started | 3.9 | 3 | −23.1% | −2.1818 to +0.3818 | no |
| pod start wait, total (s) | 6.1 | 4.3 | −29.5% | −3.7312 to +0.1312 | no |
| pod start wait, mean (s) | 1.647 | 1.497 | −9.1% | −0.4039 to +0.1039 | no |
| host CPU busy, the real machine under kind (%) | 24.81 | 24.96 | +0.6% | −0.1482 to +0.4666 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.513 | +0.0% | −0.0014 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.8 | +0.1% | −0.0925 to +0.3174 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.8 | +0.1% | −0.0925 to +0.3174 | no |
| response time (ms), mean | 70.09 | 70.65 | +0.8% | −0.4964 to +1.6111 | no |
| response time (ms), 95th percentile | 105.6 | 107.2 | +1.6% | −0.0926 to +3.3966 | no |
| response time (ms), 99th percentile | 140.7 | 148.9 | +5.9% | −3.3143 to +19.8201 | no |
| time over the response line (% of samples) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 20.2 | +19.5% | +1.3037 to +5.2963 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.4883 | +55.0% | −0.2869 to +0.6336 | no |
| utilisation (used / allocatable) | 0.03327 | 0.03359 | +1.0% | −0.0003 to +0.0009 | no |
| CPU used (cores), mean | 0.7984 | 0.8062 | +1.0% | −0.0060 to +0.0216 | no |
| Omni's own CPU (cores), mean | 0.00833 | 0.02395 | +187.5% | +0.0127 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8067 | 0.8301 | +2.9% | +0.0076 to +0.0392 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.3 | 855.7 | −0.2% | −19.9753 to +16.8382 | no |
| HPA replicas, mean | 7.811 | 7.914 | +1.3% | −0.2342 to +0.4405 | no |
| pods started | 3.9 | 4.1 | +5.1% | −0.6793 to +1.0793 | no |
| pod start wait, total (s) | 6.1 | 7.4 | +21.3% | −0.4859 to +3.0859 | no |
| pod start wait, mean (s) | 1.647 | 1.842 | +11.8% | −0.0308 to +0.4208 | no |
| host CPU busy, the real machine under kind (%) | 24.81 | 25.41 | +2.4% | +0.2114 to +1.0014 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0000 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 158 | +0.2% | +0.0932 to +0.5241 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 158 | +0.2% | +0.0932 to +0.5241 | yes: power given |
| response time (ms), mean | 70.09 | 71.5 | +2.0% | +0.2942 to +2.5097 | yes: LOSS |
| response time (ms), 95th percentile | 105.6 | 109 | +3.2% | +0.5345 to +6.2805 | yes: LOSS |
| response time (ms), 99th percentile | 140.7 | 149.6 | +6.3% | −3.9531 to +21.8045 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 19.3 | +14.2% | −0.0128 to +4.8128 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.1567 | −50.3% | −0.3775 to +0.0609 | no |
| utilisation (used / allocatable) | 0.03327 | 0.03396 | +2.1% | +0.0001 to +0.0013 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7984 | 0.815 | +2.1% | +0.0031 to +0.0303 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00833 | 0.06592 | +691.4% | +0.0471 to +0.0681 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8067 | 0.8809 | +9.2% | +0.0517 to +0.0968 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.3 | 846.6 | −1.2% | −22.6773 to +1.2488 | no |
| HPA replicas, mean | 7.811 | 8.09 | +3.6% | −0.1889 to +0.7474 | no |
| pods started | 3.9 | 3.6 | −7.7% | −1.1953 to +0.5953 | no |
| pod start wait, total (s) | 6.1 | 4.7 | −23.0% | −2.9888 to +0.1888 | no |
| pod start wait, mean (s) | 1.647 | 1.373 | −16.6% | −0.5705 to +0.0238 | no |
| host CPU busy, the real machine under kind (%) | 24.81 | 27.19 | +9.6% | +1.6749 to +3.0976 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*