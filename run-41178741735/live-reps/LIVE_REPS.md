# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.51 | 1.51 | 1.51 | 1.51 | 1.51 | 1.512 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.6 | 158.6 | 158.6 | 158.5 | 158.6 | 158.8 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.6 | 158.6 | 158.6 | 158.5 | 158.6 | 158.8 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 165.3 | 82.16 | 81.75 | 82.11 | 81.43 | 82.58 | 82.84 | 83.75 |
| response time (ms), 95th percentile | 376 | 123.1 | 123.3 | 122.4 | 122.6 | 123.7 | 123.4 | 127.5 |
| response time (ms), 99th percentile | 680.5 | 171.7 | 163.8 | 159 | 167 | 168 | 172.9 | 178.2 |
| time over the response line (% of samples) | 2.627 | 0.02424 | 0 | 0.03636 | 0.02424 | 0.03644 | 0.04848 | 0.02432 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.5 | 15.5 | 18.3 | 18.4 | 19.3 | 21.3 | 21 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 80 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.4833 | 0.215 | 0.24 | 0.1317 | 0.215 | 0.3783 | 0.1917 |
| utilisation (used / allocatable) | 0.04079 | 0.03827 | 0.03809 | 0.0384 | 0.03804 | 0.03846 | 0.03831 | 0.03891 |
| CPU used (cores), mean | 0.9789 | 0.9184 | 0.9141 | 0.9217 | 0.9129 | 0.9229 | 0.9194 | 0.9338 |
| Omni's own CPU (cores), mean | 0 | 0.00947 | 0.00646 | 0.00732 | 0.00822 | 0.01519 | 0.02707 | 0.07346 |
| CPU used with Omni's own (cores), mean | 0.9789 | 0.9279 | 0.9206 | 0.929 | 0.9211 | 0.9381 | 0.9465 | 1.007 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 713.8 | 716.4 | 711 | 720.1 | 714.7 | 715 | 704.5 |
| HPA replicas, mean | 8.674 | 8.241 | 8.68 | 8.679 | 7.895 | 7.792 | 8.67 | 8.779 |
| pods started | 5 | 3.6 | 3.5 | 4 | 3.3 | 3.7 | 4.4 | 3.4 |
| pod start wait, total (s) | 9.3 | 5.4 | 5.1 | 5.7 | 5.4 | 5.5 | 6.3 | 5.2 |
| pod start wait, mean (s) | 1.867 | 1.517 | 1.41 | 1.462 | 1.607 | 1.463 | 1.43 | 1.638 |
| host CPU busy, the real machine under kind (%) | 29.67 | 28.44 | 28.28 | 28.43 | 28.19 | 28.67 | 29.18 | 31.03 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.51 | −0.0% | −0.0021 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.6 | −0.4% | −1.0454 to −0.2190 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.6 | −0.4% | −1.0454 to −0.2190 | yes: GAIN |
| response time (ms), mean | 165.3 | 82.16 | −50.3% | −105.6047 to −60.6567 | yes: GAIN |
| response time (ms), 95th percentile | 376 | 123.1 | −67.3% | −318.5866 to −187.2104 | yes: GAIN |
| response time (ms), 99th percentile | 680.5 | 171.7 | −74.8% | −744.9815 to −272.6629 | yes: GAIN |
| time over the response line (% of samples) | 2.627 | 0.02424 | −99.1% | −3.8282 to −1.3783 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.4617 to −1.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.5 | +18.500 (native is 0) | +16.2824 to +20.7176 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.4833 | +63.8% | −0.0816 to +0.4583 | no |
| utilisation (used / allocatable) | 0.04079 | 0.03827 | −6.2% | −0.0040 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9789 | 0.9184 | −6.2% | −0.0955 to −0.0255 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00947 | +0.009 (native is 0) | +0.0083 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9789 | 0.9279 | −5.2% | −0.0857 to −0.0163 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 713.8 | +5.1% | +9.7782 to +58.8506 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.674 | 8.241 | −5.0% | −1.0949 to +0.2288 | no |
| pods started | 5 | 3.6 | −28.0% | −2.4769 to −0.3231 | yes: GAIN |
| pod start wait, total (s) | 9.3 | 5.4 | −41.9% | −6.2471 to −1.5529 | yes: GAIN |
| pod start wait, mean (s) | 1.867 | 1.517 | −18.8% | −0.7868 to +0.0868 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 28.44 | −4.1% | −2.0070 to −0.4516 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.51 | −0.0% | −0.0018 to +0.0011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.6 | −0.4% | −1.0563 to −0.2739 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.6 | −0.4% | −1.0563 to −0.2739 | yes: GAIN |
| response time (ms), mean | 165.3 | 81.75 | −50.5% | −106.3077 to −60.7730 | yes: GAIN |
| response time (ms), 95th percentile | 376 | 123.3 | −67.2% | −318.8712 to −186.5098 | yes: GAIN |
| response time (ms), 99th percentile | 680.5 | 163.8 | −75.9% | −755.0841 to −278.4077 | yes: GAIN |
| time over the response line (% of samples) | 2.627 | 0 | −100.0% | −3.8550 to −1.4000 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.4617 to −1.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.5 | +15.500 (native is 0) | +14.4744 to +16.5256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.215 | −27.1% | −0.3906 to +0.2306 | no |
| utilisation (used / allocatable) | 0.04079 | 0.03809 | −6.6% | −0.0041 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9789 | 0.9141 | −6.6% | −0.0988 to −0.0308 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00646 | +0.006 (native is 0) | +0.0057 to +0.0072 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9789 | 0.9206 | −6.0% | −0.0921 to −0.0246 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 716.4 | +5.4% | +14.1562 to +59.7674 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.674 | 8.68 | +0.1% | −0.3761 to +0.3883 | no |
| pods started | 5 | 3.5 | −30.0% | −2.9405 to −0.0595 | yes: GAIN |
| pod start wait, total (s) | 9.3 | 5.1 | −45.2% | −6.7413 to −1.6587 | yes: GAIN |
| pod start wait, mean (s) | 1.867 | 1.41 | −24.5% | −0.9423 to +0.0290 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 28.28 | −4.7% | −2.1068 to −0.6837 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.51 | −0.0% | −0.0021 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.6 | −0.4% | −1.0084 to −0.2810 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.6 | −0.4% | −1.0084 to −0.2810 | yes: GAIN |
| response time (ms), mean | 165.3 | 82.11 | −50.3% | −105.8170 to −60.5465 | yes: GAIN |
| response time (ms), 95th percentile | 376 | 122.4 | −67.5% | −318.7617 to −188.5173 | yes: GAIN |
| response time (ms), 99th percentile | 680.5 | 159 | −76.6% | −755.9549 to −287.1053 | yes: GAIN |
| time over the response line (% of samples) | 2.627 | 0.03636 | −98.6% | −3.8102 to −1.3721 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.4617 to −1.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | +18.300 (native is 0) | +17.0361 to +19.5639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.24 | −18.6% | −0.3637 to +0.2537 | no |
| utilisation (used / allocatable) | 0.04079 | 0.0384 | −5.8% | −0.0037 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9789 | 0.9217 | −5.8% | −0.0897 to −0.0247 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00732 | +0.007 (native is 0) | +0.0065 to +0.0081 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9789 | 0.929 | −5.1% | −0.0821 to −0.0177 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 711 | +4.7% | +8.5509 to +54.6426 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.674 | 8.679 | +0.1% | −0.3224 to +0.3333 | no |
| pods started | 5 | 4 | −20.0% | −2.5080 to +0.5080 | no |
| pod start wait, total (s) | 9.3 | 5.7 | −38.7% | −6.2379 to −0.9621 | yes: GAIN |
| pod start wait, mean (s) | 1.867 | 1.462 | −21.7% | −0.8280 to +0.0184 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 28.43 | −4.2% | −2.0391 to −0.4486 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.509 | −0.1% | −0.0030 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.5 | −0.5% | −1.0779 to −0.4127 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.5 | −0.5% | −1.0779 to −0.4127 | yes: GAIN |
| response time (ms), mean | 165.3 | 81.43 | −50.7% | −106.5571 to −61.1696 | yes: GAIN |
| response time (ms), 95th percentile | 376 | 122.6 | −67.4% | −318.4357 to −188.4333 | yes: GAIN |
| response time (ms), 99th percentile | 680.5 | 167 | −75.5% | −748.6535 to −278.4025 | yes: GAIN |
| time over the response line (% of samples) | 2.627 | 0.02424 | −99.1% | −3.8213 to −1.3852 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.4617 to −1.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +15.3991 to +21.4009 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.1317 | −55.4% | −0.4217 to +0.0950 | no |
| utilisation (used / allocatable) | 0.04079 | 0.03804 | −6.7% | −0.0041 to −0.0014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9789 | 0.9129 | −6.7% | −0.0979 to −0.0341 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00822 | +0.008 (native is 0) | +0.0070 to +0.0095 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9789 | 0.9211 | −5.9% | −0.0893 to −0.0262 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 720.1 | +6.0% | +20.8250 to +60.5639 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.674 | 7.895 | −9.0% | −1.4793 to −0.0786 | yes: GAIN |
| pods started | 5 | 3.3 | −34.0% | −2.7690 to −0.6310 | yes: GAIN |
| pod start wait, total (s) | 9.3 | 5.4 | −41.9% | −6.9987 to −0.8013 | yes: GAIN |
| pod start wait, mean (s) | 1.867 | 1.607 | −13.9% | −0.8260 to +0.3060 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 28.19 | −5.0% | −2.1861 to −0.7779 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.51 | −0.0% | −0.0024 to +0.0010 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.6 | −0.4% | −0.9654 to −0.3028 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.6 | −0.4% | −0.9654 to −0.3028 | yes: GAIN |
| response time (ms), mean | 165.3 | 82.58 | −50.0% | −105.0055 to −60.4159 | yes: GAIN |
| response time (ms), 95th percentile | 376 | 123.7 | −67.1% | −317.1474 to −187.4286 | yes: GAIN |
| response time (ms), 99th percentile | 680.5 | 168 | −75.3% | −748.2646 to −276.7614 | yes: GAIN |
| time over the response line (% of samples) | 2.627 | 0.03644 | −98.6% | −3.8008 to −1.3813 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.4617 to −1.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +15.9272 to +22.6728 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.215 | −27.1% | −0.4507 to +0.2907 | no |
| utilisation (used / allocatable) | 0.04079 | 0.03846 | −5.7% | −0.0037 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9789 | 0.9229 | −5.7% | −0.0899 to −0.0221 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01519 | +0.015 (native is 0) | +0.0132 to +0.0172 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9789 | 0.9381 | −4.2% | −0.0746 to −0.0069 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 714.7 | +5.2% | +11.7889 to +58.7363 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.674 | 7.792 | −10.2% | −1.5195 to −0.2446 | yes: GAIN |
| pods started | 5 | 3.7 | −26.0% | −2.5639 to −0.0361 | yes: GAIN |
| pod start wait, total (s) | 9.3 | 5.5 | −40.9% | −6.6968 to −0.9032 | yes: GAIN |
| pod start wait, mean (s) | 1.867 | 1.463 | −21.6% | −0.9422 to +0.1355 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 28.67 | −3.4% | −1.6999 to −0.3006 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0011 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.8 | −0.3% | −0.8940 to −0.0673 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.8 | −0.3% | −0.8940 to −0.0673 | yes: GAIN |
| response time (ms), mean | 165.3 | 82.84 | −49.9% | −104.8938 to −60.0102 | yes: GAIN |
| response time (ms), 95th percentile | 376 | 123.4 | −67.2% | −318.0632 to −187.1128 | yes: GAIN |
| response time (ms), 99th percentile | 680.5 | 172.9 | −74.6% | −744.5664 to −270.7992 | yes: GAIN |
| time over the response line (% of samples) | 2.627 | 0.04848 | −98.2% | −3.7882 to −1.3698 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.4617 to −1.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.3 | +21.300 (native is 0) | +20.1295 to +22.4705 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.3783 | +28.2% | −0.2143 to +0.3810 | no |
| utilisation (used / allocatable) | 0.04079 | 0.03831 | −6.1% | −0.0039 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9789 | 0.9194 | −6.1% | −0.0945 to −0.0245 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02707 | +0.027 (native is 0) | +0.0238 to +0.0304 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9789 | 0.9465 | −3.3% | −0.0669 to +0.0020 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 715 | +5.2% | +12.0873 to +58.9289 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.674 | 8.67 | −0.0% | −0.3457 to +0.3373 | no |
| pods started | 5 | 4.4 | −12.0% | −1.8251 to +0.6251 | no |
| pod start wait, total (s) | 9.3 | 6.3 | −32.3% | −5.5901 to −0.4099 | yes: GAIN |
| pod start wait, mean (s) | 1.867 | 1.43 | −23.4% | −0.8149 to −0.0585 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 29.67 | 29.18 | −1.6% | −1.2230 to +0.2478 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.512 | +0.1% | −0.0006 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.9 | −0.2% | −0.6592 to +0.0588 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.9 | −0.2% | −0.6592 to +0.0588 | no |
| response time (ms), mean | 165.3 | 83.75 | −49.3% | −103.4665 to −59.6130 | yes: GAIN |
| response time (ms), 95th percentile | 376 | 127.5 | −66.1% | −312.3102 to −184.6958 | yes: GAIN |
| response time (ms), 99th percentile | 680.5 | 178.2 | −73.8% | −740.8622 to −263.7798 | yes: GAIN |
| time over the response line (% of samples) | 2.627 | 0.02432 | −99.1% | −3.8212 to −1.3852 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.9 | 0 | −100.0% | −4.4617 to −1.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21 | +21.000 (native is 0) | +19.2806 to +22.7194 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.1917 | −35.0% | −0.4231 to +0.2165 | no |
| utilisation (used / allocatable) | 0.04079 | 0.03891 | −4.6% | −0.0033 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9789 | 0.9338 | −4.6% | −0.0787 to −0.0116 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07346 | +0.073 (native is 0) | +0.0644 to +0.0825 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9789 | 1.007 | +2.9% | −0.0060 to +0.0626 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 679.5 | 704.5 | +3.7% | +0.5817 to +49.4724 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.674 | 8.779 | +1.2% | −0.4108 to +0.6202 | no |
| pods started | 5 | 3.4 | −32.0% | −2.9985 to −0.2015 | yes: GAIN |
| pod start wait, total (s) | 9.3 | 5.2 | −44.1% | −6.4228 to −1.7772 | yes: GAIN |
| pod start wait, mean (s) | 1.867 | 1.638 | −12.2% | −0.5732 to +0.1165 | no |
| host CPU busy, the real machine under kind (%) | 29.67 | 31.03 | +4.6% | +0.5699 to +2.1356 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.51 | −0.0% | −0.0020 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.6 | −0.0% | −0.2242 to +0.1584 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.6 | −0.0% | −0.2242 to +0.1584 | no |
| response time (ms), mean | 82.16 | 81.75 | −0.5% | −1.6526 to +0.8332 | no |
| response time (ms), 95th percentile | 123.1 | 123.3 | +0.2% | −1.3437 to +1.7597 | no |
| response time (ms), 99th percentile | 171.7 | 163.8 | −4.6% | −24.8199 to +8.9725 | no |
| time over the response line (% of samples) | 0.02424 | 0 | −100.0% | −0.0608 to +0.0123 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 15.5 | −16.2% | −5.8612 to −0.1388 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.215 | −55.5% | −0.5362 to −0.0004 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03827 | 0.03809 | −0.5% | −0.0007 to +0.0003 | no |
| CPU used (cores), mean | 0.9184 | 0.9141 | −0.5% | −0.0156 to +0.0070 | no |
| Omni's own CPU (cores), mean | 0.00947 | 0.00646 | −31.8% | −0.0036 to −0.0025 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9279 | 0.9206 | −0.8% | −0.0187 to +0.0041 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.8 | 716.4 | +0.4% | −3.9981 to +9.2930 | no |
| HPA replicas, mean | 8.241 | 8.68 | +5.3% | −0.0895 to +0.9678 | no |
| pods started | 3.6 | 3.5 | −2.8% | −1.4254 to +1.2254 | no |
| pod start wait, total (s) | 5.4 | 5.1 | −5.6% | −2.8469 to +2.2469 | no |
| pod start wait, mean (s) | 1.517 | 1.41 | −7.0% | −0.4088 to +0.1955 | no |
| host CPU busy, the real machine under kind (%) | 28.44 | 28.28 | −0.6% | −0.4641 to +0.1323 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.51 | −0.0% | −0.0021 to +0.0011 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.6 | −0.0% | −0.2318 to +0.2068 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.6 | −0.0% | −0.2318 to +0.2068 | no |
| response time (ms), mean | 82.16 | 82.11 | −0.1% | −1.0016 to +0.8995 | no |
| response time (ms), 95th percentile | 123.1 | 122.4 | −0.6% | −2.3403 to +0.8583 | no |
| response time (ms), 99th percentile | 171.7 | 159 | −7.4% | −23.9399 to −1.4759 | yes: GAIN |
| time over the response line (% of samples) | 0.02424 | 0.03636 | +50.0% | −0.0371 to +0.0613 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 18.3 | −1.1% | −3.2868 to +2.8868 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.24 | −50.3% | −0.5741 to +0.0874 | no |
| utilisation (used / allocatable) | 0.03827 | 0.0384 | +0.4% | −0.0004 to +0.0006 | no |
| CPU used (cores), mean | 0.9184 | 0.9217 | +0.4% | −0.0086 to +0.0151 | no |
| Omni's own CPU (cores), mean | 0.00947 | 0.00732 | −22.7% | −0.0026 to −0.0017 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9279 | 0.929 | +0.1% | −0.0108 to +0.0130 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.8 | 711 | −0.4% | −12.7452 to +7.3099 | no |
| HPA replicas, mean | 8.241 | 8.679 | +5.3% | −0.0620 to +0.9390 | no |
| pods started | 3.6 | 4 | +11.1% | −0.9146 to +1.7146 | no |
| pod start wait, total (s) | 5.4 | 5.7 | +5.6% | −2.5020 to +3.1020 | no |
| pod start wait, mean (s) | 1.517 | 1.462 | −3.6% | −0.5215 to +0.4120 | no |
| host CPU busy, the real machine under kind (%) | 28.44 | 28.43 | −0.1% | −0.3426 to +0.3136 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.509 | −0.1% | −0.0029 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −0.2975 to +0.0713 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −0.2975 to +0.0713 | no |
| response time (ms), mean | 82.16 | 81.43 | −0.9% | −1.5364 to +0.0710 | no |
| response time (ms), 95th percentile | 123.1 | 122.6 | −0.4% | −2.3109 to +1.2389 | no |
| response time (ms), 99th percentile | 171.7 | 167 | −2.7% | −12.7448 to +3.3332 | no |
| time over the response line (% of samples) | 0.02424 | 0.02424 | ±0.0% | −0.0578 to +0.0578 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 18.4 | −0.5% | −3.5130 to +3.3130 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.1317 | −72.8% | −0.6888 to −0.0145 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03827 | 0.03804 | −0.6% | −0.0005 to +0.0000 | no |
| CPU used (cores), mean | 0.9184 | 0.9129 | −0.6% | −0.0121 to +0.0010 | no |
| Omni's own CPU (cores), mean | 0.00947 | 0.00822 | −13.2% | −0.0015 to −0.0010 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9279 | 0.9211 | −0.7% | −0.0136 to +0.0000 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.8 | 720.1 | +0.9% | −1.8937 to +14.6538 | no |
| HPA replicas, mean | 8.241 | 7.895 | −4.2% | −0.8971 to +0.2053 | no |
| pods started | 3.6 | 3.3 | −8.3% | −1.4209 to +0.8209 | no |
| pod start wait, total (s) | 5.4 | 5.4 | ±0.0% | −2.1853 to +2.1853 | no |
| pod start wait, mean (s) | 1.517 | 1.607 | +5.9% | −0.3164 to +0.4964 | no |
| host CPU busy, the real machine under kind (%) | 28.44 | 28.19 | −0.9% | −0.4898 to −0.0155 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.51 | −0.0% | −0.0016 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.6 | −0.0% | −0.2524 to +0.2485 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.6 | −0.0% | −0.2524 to +0.2485 | no |
| response time (ms), mean | 82.16 | 82.58 | +0.5% | −1.6852 to +2.5251 | no |
| response time (ms), 95th percentile | 123.1 | 123.7 | +0.5% | −3.2471 to +4.4681 | no |
| response time (ms), 99th percentile | 171.7 | 168 | −2.1% | −21.9203 to +14.5387 | no |
| time over the response line (% of samples) | 0.02424 | 0.03644 | +50.3% | −0.0519 to +0.0762 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 19.3 | +4.3% | −3.1150 to +4.7150 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.215 | −55.5% | −0.7106 to +0.1739 | no |
| utilisation (used / allocatable) | 0.03827 | 0.03846 | +0.5% | −0.0005 to +0.0009 | no |
| CPU used (cores), mean | 0.9184 | 0.9229 | +0.5% | −0.0115 to +0.0205 | no |
| Omni's own CPU (cores), mean | 0.00947 | 0.01519 | +60.4% | +0.0049 to +0.0066 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9279 | 0.9381 | +1.1% | −0.0063 to +0.0268 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.8 | 714.7 | +0.1% | −12.8566 to +14.7530 | no |
| HPA replicas, mean | 8.241 | 7.792 | −5.4% | −1.1918 to +0.2938 | no |
| pods started | 3.6 | 3.7 | +2.8% | −1.4249 to +1.6249 | no |
| pod start wait, total (s) | 5.4 | 5.5 | +1.9% | −2.8483 to +3.0483 | no |
| pod start wait, mean (s) | 1.517 | 1.463 | −3.5% | −0.4848 to +0.3781 | no |
| host CPU busy, the real machine under kind (%) | 28.44 | 28.67 | +0.8% | −0.1972 to +0.6554 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.511 | +0.1% | −0.0004 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.8 | +0.1% | −0.0024 to +0.3055 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.8 | +0.1% | −0.0024 to +0.3055 | no |
| response time (ms), mean | 82.16 | 82.84 | +0.8% | −0.3383 to +1.6957 | no |
| response time (ms), 95th percentile | 123.1 | 123.4 | +0.3% | −1.4246 to +2.0456 | no |
| response time (ms), 99th percentile | 171.7 | 172.9 | +0.7% | −13.3469 to +15.6257 | no |
| time over the response line (% of samples) | 0.02424 | 0.04848 | +100.0% | −0.0442 to +0.0926 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 21.3 | +15.1% | +1.0221 to +4.5779 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.3783 | −21.7% | −0.4337 to +0.2237 | no |
| utilisation (used / allocatable) | 0.03827 | 0.03831 | +0.1% | −0.0005 to +0.0006 | no |
| CPU used (cores), mean | 0.9184 | 0.9194 | +0.1% | −0.0126 to +0.0146 | no |
| Omni's own CPU (cores), mean | 0.00947 | 0.02707 | +185.9% | +0.0155 to +0.0197 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9279 | 0.9465 | +2.0% | +0.0047 to +0.0325 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.8 | 715 | +0.2% | −7.7026 to +10.0901 | no |
| HPA replicas, mean | 8.241 | 8.67 | +5.2% | −0.1276 to +0.9852 | no |
| pods started | 3.6 | 4.4 | +22.2% | −0.5821 to +2.1821 | no |
| pod start wait, total (s) | 5.4 | 6.3 | +16.7% | −1.6109 to +3.4109 | no |
| pod start wait, mean (s) | 1.517 | 1.43 | −5.7% | −0.4837 to +0.3104 | no |
| host CPU busy, the real machine under kind (%) | 28.44 | 29.18 | +2.6% | +0.3493 to +1.1342 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.51 | 1.512 | +0.1% | +0.0004 to +0.0029 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.9 | +0.2% | +0.1412 to +0.5229 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.9 | +0.2% | +0.1412 to +0.5229 | yes: power given |
| response time (ms), mean | 82.16 | 83.75 | +1.9% | +0.5175 to +2.6644 | yes: LOSS |
| response time (ms), 95th percentile | 123.1 | 127.5 | +3.6% | +1.3247 to +7.4663 | yes: LOSS |
| response time (ms), 99th percentile | 171.7 | 178.2 | +3.8% | −2.5559 to +15.5583 | no |
| time over the response line (% of samples) | 0.02424 | 0.02432 | +0.3% | −0.0409 to +0.0411 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.5 | 21 | +13.5% | −0.3262 to +5.3262 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.1917 | −60.3% | −0.5183 to −0.0650 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03827 | 0.03891 | +1.7% | +0.0001 to +0.0012 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9184 | 0.9338 | +1.7% | +0.0014 to +0.0292 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00947 | 0.07346 | +675.7% | +0.0561 to +0.0718 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9279 | 1.007 | +8.5% | +0.0610 to +0.0976 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.8 | 704.5 | −1.3% | −16.9813 to −1.5934 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.241 | 8.779 | +6.5% | +0.1330 to +0.9424 | yes: power given |
| pods started | 3.6 | 3.4 | −5.6% | −1.1417 to +0.7417 | no |
| pod start wait, total (s) | 5.4 | 5.2 | −3.7% | −1.5403 to +1.1403 | no |
| pod start wait, mean (s) | 1.517 | 1.638 | +8.0% | −0.1760 to +0.4194 | no |
| host CPU busy, the real machine under kind (%) | 28.44 | 31.03 | +9.1% | +2.1143 to +3.0499 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*