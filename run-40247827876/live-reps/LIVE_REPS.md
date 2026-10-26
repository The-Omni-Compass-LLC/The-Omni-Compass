# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.52 | 1.511 | 1.514 | 1.518 | 1.518 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.9 | 159 | 159.2 | 159.6 | 159.6 | 159.3 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.9 | 159 | 159.2 | 159.6 | 159.6 | 159.3 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 174.1 | 84.86 | 85.81 | 85.56 | 85.04 | 85.49 | 85.98 | 86.88 |
| response time (ms), 95th percentile | 387.3 | 126.4 | 128.4 | 127.4 | 126.2 | 127.6 | 128.4 | 131.5 |
| response time (ms), 99th percentile | 646 | 166.9 | 183.7 | 175.2 | 173.5 | 179.9 | 177.3 | 181 |
| time over the response line (% of samples) | 2.746 | 0.02424 | 0.0122 | 0.03644 | 0 | 0.01212 | 0.02424 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | 15.3 | 17.5 | 18 | 18.1 | 20.4 | 21.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 90 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.185 | 0.2167 | 0.1833 | 0.1583 | 0.1067 | 0.2133 | 0.1867 |
| utilisation (used / allocatable) | 0.04136 | 0.03896 | 0.03962 | 0.03934 | 0.03917 | 0.03925 | 0.03962 | 0.04023 |
| CPU used (cores), mean | 0.9926 | 0.935 | 0.951 | 0.9441 | 0.9401 | 0.942 | 0.9508 | 0.9655 |
| Omni's own CPU (cores), mean | 0 | 0.00846 | 0.00602 | 0.00674 | 0.00747 | 0.01365 | 0.02472 | 0.06692 |
| CPU used with Omni's own (cores), mean | 0.9926 | 0.9434 | 0.957 | 0.9508 | 0.9476 | 0.9556 | 0.9755 | 1.032 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 706.1 | 686 | 694.3 | 695.2 | 691.9 | 691.8 | 681.2 |
| HPA replicas, mean | 8.671 | 8.252 | 8.516 | 8.561 | 8.049 | 8.226 | 9.003 | 8.833 |
| pods started | 4.8 | 3.6 | 3.4 | 4.1 | 3.5 | 3.8 | 4.7 | 4.3 |
| pod start wait, total (s) | 7.8 | 6.2 | 5.4 | 6.3 | 5.4 | 6.4 | 7 | 6.9 |
| pod start wait, mean (s) | 1.645 | 1.6 | 1.682 | 1.543 | 1.543 | 1.655 | 1.525 | 1.622 |
| host CPU busy, the real machine under kind (%) | 29.72 | 28.36 | 28.68 | 28.61 | 28.52 | 28.8 | 29.33 | 30.97 |
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
| node-hours | 1.515 | 1.52 | +0.3% | −0.0013 to +0.0109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.9 | −0.0% | −0.5277 to +0.4974 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.9 | −0.0% | −0.5277 to +0.4974 | no |
| response time (ms), mean | 174.1 | 84.86 | −51.2% | −109.6493 to −68.7384 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 126.4 | −67.4% | −313.2059 to −208.6851 | yes: GAIN |
| response time (ms), 99th percentile | 646 | 166.9 | −74.2% | −594.3993 to −363.7025 | yes: GAIN |
| time over the response line (% of samples) | 2.746 | 0.02424 | −99.1% | −3.9242 to −1.5187 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.9456 to −1.4544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.500 (native is 0) | +14.4419 to +20.5581 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.185 | +640.0% | −0.0216 to +0.3416 | no |
| utilisation (used / allocatable) | 0.04136 | 0.03896 | −5.8% | −0.0033 to −0.0015 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9926 | 0.935 | −5.8% | −0.0799 to −0.0354 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00846 | +0.008 (native is 0) | +0.0074 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9926 | 0.9434 | −5.0% | −0.0708 to −0.0276 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 706.1 | +6.0% | +18.0978 to +62.2696 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.671 | 8.252 | −4.8% | −1.1253 to +0.2877 | no |
| pods started | 4.8 | 3.6 | −25.0% | −2.7004 to +0.3004 | no |
| pod start wait, total (s) | 7.8 | 6.2 | −20.5% | −5.0421 to +1.8421 | no |
| pod start wait, mean (s) | 1.645 | 1.6 | −2.7% | −0.5211 to +0.4311 | no |
| host CPU busy, the real machine under kind (%) | 29.72 | 28.36 | −4.6% | −1.9241 to −0.7887 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.511 | −0.3% | −0.0127 to +0.0034 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159 | −0.6% | −1.7696 to −0.0352 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159 | −0.6% | −1.7696 to −0.0352 | yes: GAIN |
| response time (ms), mean | 174.1 | 85.81 | −50.7% | −109.1841 to −67.2907 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 128.4 | −66.8% | −311.5625 to −206.3145 | yes: GAIN |
| response time (ms), 99th percentile | 646 | 183.7 | −71.6% | −573.2226 to −351.3076 | yes: GAIN |
| time over the response line (% of samples) | 2.746 | 0.0122 | −99.6% | −3.9392 to −1.5278 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.9456 to −1.4544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.3 | +15.300 (native is 0) | +14.0819 to +16.5181 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.2167 | +766.7% | −0.0483 to +0.4316 | no |
| utilisation (used / allocatable) | 0.04136 | 0.03962 | −4.2% | −0.0028 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9926 | 0.951 | −4.2% | −0.0673 to −0.0160 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00602 | +0.006 (native is 0) | +0.0052 to +0.0068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9926 | 0.957 | −3.6% | −0.0607 to −0.0105 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 686 | +3.0% | +1.3284 to +38.7205 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.671 | 8.516 | −1.8% | −0.9421 to +0.6310 | no |
| pods started | 4.8 | 3.4 | −29.2% | −2.6251 to −0.1749 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5.4 | −30.8% | −3.9526 to −0.8474 | yes: GAIN |
| pod start wait, mean (s) | 1.645 | 1.682 | +2.2% | −0.3723 to +0.4456 | no |
| host CPU busy, the real machine under kind (%) | 29.72 | 28.68 | −3.5% | −1.6537 to −0.4118 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.513 | −0.1% | −0.0071 to +0.0035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.2 | −0.4% | −1.2437 to −0.0898 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.2 | −0.4% | −1.2437 to −0.0898 | yes: GAIN |
| response time (ms), mean | 174.1 | 85.56 | −50.8% | −109.3916 to −67.5991 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 127.4 | −67.1% | −312.4268 to −207.3852 | yes: GAIN |
| response time (ms), 99th percentile | 646 | 175.2 | −72.9% | −584.3341 to −357.1687 | yes: GAIN |
| time over the response line (% of samples) | 2.746 | 0.03644 | −98.7% | −3.9071 to −1.5114 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.9456 to −1.4544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.500 (native is 0) | +16.2726 to +18.7274 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.1833 | +633.3% | −0.0004 to +0.3171 | no |
| utilisation (used / allocatable) | 0.04136 | 0.03934 | −4.9% | −0.0029 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9926 | 0.9441 | −4.9% | −0.0686 to −0.0284 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00674 | +0.007 (native is 0) | +0.0060 to +0.0075 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9926 | 0.9508 | −4.2% | −0.0613 to −0.0223 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 694.3 | +4.3% | +19.0543 to +37.6533 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.671 | 8.561 | −1.3% | −0.3795 to +0.1602 | no |
| pods started | 4.8 | 4.1 | −14.6% | −1.7690 to +0.3690 | no |
| pod start wait, total (s) | 7.8 | 6.3 | −19.2% | −3.6393 to +0.6393 | no |
| pod start wait, mean (s) | 1.645 | 1.543 | −6.2% | −0.4675 to +0.2642 | no |
| host CPU busy, the real machine under kind (%) | 29.72 | 28.61 | −3.7% | −1.6587 to −0.5611 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.518 | +0.2% | −0.0032 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.6 | −0.2% | −0.8421 to +0.2874 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.6 | −0.2% | −0.8421 to +0.2874 | no |
| response time (ms), mean | 174.1 | 85.04 | −51.1% | −109.9141 to −68.1073 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 126.2 | −67.4% | −314.2554 to −208.1146 | yes: GAIN |
| response time (ms), 99th percentile | 646 | 173.5 | −73.1% | −581.1092 to −363.8492 | yes: GAIN |
| time over the response line (% of samples) | 2.746 | 0 | −100.0% | −3.9606 to −1.5308 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.9456 to −1.4544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +15.7888 to +20.2112 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.1583 | +533.3% | −0.0015 to +0.2682 | no |
| utilisation (used / allocatable) | 0.04136 | 0.03917 | −5.3% | −0.0033 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9926 | 0.9401 | −5.3% | −0.0796 to −0.0254 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00747 | +0.007 (native is 0) | +0.0065 to +0.0085 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9926 | 0.9476 | −4.5% | −0.0713 to −0.0187 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 695.2 | +4.4% | +15.2306 to +43.2495 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.671 | 8.049 | −7.2% | −1.2611 to +0.0164 | no |
| pods started | 4.8 | 3.5 | −27.1% | −2.0578 to −0.5422 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 5.4 | −30.8% | −3.9155 to −0.8845 | yes: GAIN |
| pod start wait, mean (s) | 1.645 | 1.543 | −6.2% | −0.3241 to +0.1208 | no |
| host CPU busy, the real machine under kind (%) | 29.72 | 28.52 | −4.0% | −1.7984 to −0.6003 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.518 | +0.2% | −0.0065 to +0.0115 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.6 | −0.1% | −1.1502 to +0.7036 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.6 | −0.1% | −1.1502 to +0.7036 | no |
| response time (ms), mean | 174.1 | 85.49 | −50.9% | −109.8425 to −67.2717 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 127.6 | −67.0% | −313.0247 to −206.3973 | yes: GAIN |
| response time (ms), 99th percentile | 646 | 179.9 | −72.1% | −576.6148 to −355.4090 | yes: GAIN |
| time over the response line (% of samples) | 2.746 | 0.01212 | −99.6% | −3.9455 to −1.5216 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.9456 to −1.4544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 | +18.100 (native is 0) | +15.6579 to +20.5421 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.1067 | +326.7% | −0.0733 to +0.2366 | no |
| utilisation (used / allocatable) | 0.04136 | 0.03925 | −5.1% | −0.0032 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9926 | 0.942 | −5.1% | −0.0777 to −0.0235 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01365 | +0.014 (native is 0) | +0.0120 to +0.0153 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9926 | 0.9556 | −3.7% | −0.0626 to −0.0113 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 691.9 | +3.9% | +9.1432 to +42.6886 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.671 | 8.226 | −5.1% | −0.8364 to −0.0543 | yes: GAIN |
| pods started | 4.8 | 3.8 | −20.8% | −2.1184 to +0.1184 | no |
| pod start wait, total (s) | 7.8 | 6.4 | −17.9% | −3.9053 to +1.1053 | no |
| pod start wait, mean (s) | 1.645 | 1.655 | +0.6% | −0.3395 to +0.3595 | no |
| host CPU busy, the real machine under kind (%) | 29.72 | 28.8 | −3.1% | −1.6662 to −0.1682 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0109 to +0.0082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.3 | −0.4% | −1.6019 to +0.4314 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.3 | −0.4% | −1.6019 to +0.4314 | no |
| response time (ms), mean | 174.1 | 85.98 | −50.6% | −108.6575 to −67.4817 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 128.4 | −66.9% | −311.6109 to −206.3321 | yes: GAIN |
| response time (ms), 99th percentile | 646 | 177.3 | −72.5% | −582.0758 to −355.1980 | yes: GAIN |
| time over the response line (% of samples) | 2.746 | 0.02424 | −99.1% | −3.9156 to −1.5273 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.9456 to −1.4544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.4 | +20.400 (native is 0) | +17.8721 to +22.9279 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.2133 | +753.3% | −0.0486 to +0.4253 | no |
| utilisation (used / allocatable) | 0.04136 | 0.03962 | −4.2% | −0.0027 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9926 | 0.9508 | −4.2% | −0.0644 to −0.0192 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02472 | +0.025 (native is 0) | +0.0219 to +0.0275 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9926 | 0.9755 | −1.7% | −0.0381 to +0.0040 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 691.8 | +3.9% | +11.8067 to +39.9346 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.671 | 9.003 | +3.8% | −0.0892 to +0.7522 | no |
| pods started | 4.8 | 4.7 | −2.1% | −1.3367 to +1.1367 | no |
| pod start wait, total (s) | 7.8 | 7 | −10.3% | −3.4934 to +1.8934 | no |
| pod start wait, mean (s) | 1.645 | 1.525 | −7.3% | −0.4605 to +0.2195 | no |
| host CPU busy, the real machine under kind (%) | 29.72 | 29.33 | −1.3% | −1.0250 to +0.2491 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0072 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.4 | −0.3% | −1.0772 to +0.2132 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.4 | −0.3% | −1.0772 to +0.2132 | no |
| response time (ms), mean | 174.1 | 86.88 | −50.1% | −107.3304 to −67.0116 | yes: GAIN |
| response time (ms), 95th percentile | 387.3 | 131.5 | −66.0% | −306.4434 to −205.2386 | yes: GAIN |
| response time (ms), 99th percentile | 646 | 181 | −72.0% | −569.6192 to −360.3394 | yes: GAIN |
| time over the response line (% of samples) | 2.746 | 0 | −100.0% | −3.9606 to −1.5308 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.9456 to −1.4544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.5 | +21.500 (native is 0) | +19.8056 to +23.1944 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.1867 | +646.7% | +0.0017 to +0.3216 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04136 | 0.04023 | −2.7% | −0.0019 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9926 | 0.9655 | −2.7% | −0.0451 to −0.0090 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06692 | +0.067 (native is 0) | +0.0585 to +0.0754 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9926 | 1.032 | +4.0% | +0.0256 to +0.0541 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.9 | 681.2 | +2.3% | +5.7905 to +24.7174 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.671 | 8.833 | +1.9% | −0.1915 to +0.5147 | no |
| pods started | 4.8 | 4.3 | −10.4% | −1.4079 to +0.4079 | no |
| pod start wait, total (s) | 7.8 | 6.9 | −11.5% | −2.9909 to +1.1909 | no |
| pod start wait, mean (s) | 1.645 | 1.622 | −1.4% | −0.4439 to +0.3973 | no |
| host CPU busy, the real machine under kind (%) | 29.72 | 30.97 | +4.2% | +0.9471 to +1.5676 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.511 | −0.6% | −0.0188 to −0.0002 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159 | −0.6% | −1.8186 to +0.0442 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159 | −0.6% | −1.8186 to +0.0442 | no |
| response time (ms), mean | 84.86 | 85.81 | +1.1% | −0.3578 to +2.2707 | no |
| response time (ms), 95th percentile | 126.4 | 128.4 | +1.6% | −0.2324 to +4.2464 | no |
| response time (ms), 99th percentile | 166.9 | 183.7 | +10.1% | +6.5204 to +27.0512 | yes: LOSS |
| time over the response line (% of samples) | 0.02424 | 0.0122 | −49.7% | −0.0614 to +0.0373 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 15.3 | −12.6% | −5.6848 to +1.2848 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.2167 | +17.1% | −0.2615 to +0.3248 | no |
| utilisation (used / allocatable) | 0.03896 | 0.03962 | +1.7% | −0.0004 to +0.0017 | no |
| CPU used (cores), mean | 0.935 | 0.951 | +1.7% | −0.0088 to +0.0408 | no |
| Omni's own CPU (cores), mean | 0.00846 | 0.00602 | −28.8% | −0.0030 to −0.0019 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9434 | 0.957 | +1.4% | −0.0115 to +0.0386 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.1 | 686 | −2.9% | −56.8045 to +16.4859 | no |
| HPA replicas, mean | 8.252 | 8.516 | +3.2% | −0.8107 to +1.3372 | no |
| pods started | 3.6 | 3.4 | −5.6% | −2.5313 to +2.1313 | no |
| pod start wait, total (s) | 6.2 | 5.4 | −12.9% | −4.7869 to +3.1869 | no |
| pod start wait, mean (s) | 1.6 | 1.682 | +5.1% | −0.3734 to +0.5367 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 28.68 | +1.1% | −0.2833 to +0.9307 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.52 | 1.514 | −0.4% | −0.0149 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.2 | −0.4% | −1.4273 to +0.1242 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.2 | −0.4% | −1.4273 to +0.1242 | no |
| response time (ms), mean | 84.86 | 85.56 | +0.8% | −0.1629 to +1.5600 | no |
| response time (ms), 95th percentile | 126.4 | 127.4 | +0.8% | −1.1350 to +3.2140 | no |
| response time (ms), 99th percentile | 166.9 | 175.2 | +5.0% | −4.8327 to +21.4317 | no |
| time over the response line (% of samples) | 0.02424 | 0.03644 | +50.3% | −0.0371 to +0.0615 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 17.5 | ±0.0% | −2.7601 to +2.7601 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.1833 | −0.9% | −0.2386 to +0.2353 | no |
| utilisation (used / allocatable) | 0.03896 | 0.03934 | +1.0% | −0.0004 to +0.0011 | no |
| CPU used (cores), mean | 0.935 | 0.9441 | +1.0% | −0.0089 to +0.0272 | no |
| Omni's own CPU (cores), mean | 0.00846 | 0.00674 | −20.3% | −0.0021 to −0.0013 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9434 | 0.9508 | +0.8% | −0.0108 to +0.0256 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.1 | 694.3 | −1.7% | −33.1543 to +9.4944 | no |
| HPA replicas, mean | 8.252 | 8.561 | +3.7% | −0.4437 to +1.0620 | no |
| pods started | 3.6 | 4.1 | +13.9% | −1.0906 to +2.0906 | no |
| pod start wait, total (s) | 6.2 | 6.3 | +1.6% | −2.3421 to +2.5421 | no |
| pod start wait, mean (s) | 1.6 | 1.543 | −3.5% | −0.2868 to +0.1734 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 28.61 | +0.9% | −0.2063 to +0.6993 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.518 | −0.2% | −0.0080 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.6 | −0.2% | −0.8839 to +0.3596 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.6 | −0.2% | −0.8839 to +0.3596 | no |
| response time (ms), mean | 84.86 | 85.04 | +0.2% | −0.7702 to +1.1366 | no |
| response time (ms), 95th percentile | 126.4 | 126.2 | −0.2% | −2.9136 to +2.4346 | no |
| response time (ms), 99th percentile | 166.9 | 173.5 | +3.9% | −8.5421 to +21.6855 | no |
| time over the response line (% of samples) | 0.02424 | 0 | −100.0% | −0.0608 to +0.0123 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 18 | +2.9% | −2.7387 to +3.7387 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.1583 | −14.4% | −0.2871 to +0.2338 | no |
| utilisation (used / allocatable) | 0.03896 | 0.03917 | +0.6% | −0.0004 to +0.0008 | no |
| CPU used (cores), mean | 0.935 | 0.9401 | +0.6% | −0.0095 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0.00846 | 0.00747 | −11.7% | −0.0014 to −0.0006 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9434 | 0.9476 | +0.4% | −0.0107 to +0.0191 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.1 | 695.2 | −1.5% | −33.4074 to +11.5201 | no |
| HPA replicas, mean | 8.252 | 8.049 | −2.5% | −1.1656 to +0.7584 | no |
| pods started | 3.6 | 3.5 | −2.8% | −1.9910 to +1.7910 | no |
| pod start wait, total (s) | 6.2 | 5.4 | −12.9% | −4.2684 to +2.6684 | no |
| pod start wait, mean (s) | 1.6 | 1.543 | −3.5% | −0.4130 to +0.2997 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 28.52 | +0.6% | −0.2151 to +0.5292 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.518 | −0.2% | −0.0083 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.6 | −0.1% | −0.8537 to +0.4375 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.6 | −0.1% | −0.8537 to +0.4375 | no |
| response time (ms), mean | 84.86 | 85.49 | +0.8% | −0.7580 to +2.0315 | no |
| response time (ms), 95th percentile | 126.4 | 127.6 | +1.0% | −1.2900 to +3.7590 | no |
| response time (ms), 99th percentile | 166.9 | 179.9 | +7.8% | +2.0957 to +23.9823 | yes: LOSS |
| time over the response line (% of samples) | 0.02424 | 0.01212 | −50.0% | −0.0613 to +0.0371 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 18.1 | +3.4% | −1.7166 to +2.9166 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.1067 | −42.3% | −0.3164 to +0.1597 | no |
| utilisation (used / allocatable) | 0.03896 | 0.03925 | +0.8% | −0.0004 to +0.0010 | no |
| CPU used (cores), mean | 0.935 | 0.942 | +0.8% | −0.0108 to +0.0248 | no |
| Omni's own CPU (cores), mean | 0.00846 | 0.01365 | +61.3% | +0.0046 to +0.0058 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9434 | 0.9556 | +1.3% | −0.0053 to +0.0297 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.1 | 691.9 | −2.0% | −46.0087 to +17.4731 | no |
| HPA replicas, mean | 8.252 | 8.226 | −0.3% | −0.6796 to +0.6264 | no |
| pods started | 3.6 | 3.8 | +5.6% | −1.5128 to +1.9128 | no |
| pod start wait, total (s) | 6.2 | 6.4 | +3.2% | −2.6573 to +3.0573 | no |
| pod start wait, mean (s) | 1.6 | 1.655 | +3.4% | −0.3589 to +0.4689 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 28.8 | +1.5% | −0.0579 to +0.9363 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.514 | −0.4% | −0.0150 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.3 | −0.4% | −1.5320 to +0.3919 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.3 | −0.4% | −1.5320 to +0.3919 | no |
| response time (ms), mean | 84.86 | 85.98 | +1.3% | +0.3981 to +1.8504 | yes: LOSS |
| response time (ms), 95th percentile | 126.4 | 128.4 | +1.6% | −0.6232 to +4.5712 | no |
| response time (ms), 99th percentile | 166.9 | 177.3 | +6.2% | −6.3563 to +27.1843 | no |
| time over the response line (% of samples) | 0.02424 | 0.02424 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 20.4 | +16.6% | +0.5772 to +5.2228 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.2133 | +15.3% | −0.1141 to +0.1707 | no |
| utilisation (used / allocatable) | 0.03896 | 0.03962 | +1.7% | +0.0004 to +0.0010 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.935 | 0.9508 | +1.7% | +0.0084 to +0.0233 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00846 | 0.02472 | +192.2% | +0.0145 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9434 | 0.9755 | +3.4% | +0.0247 to +0.0395 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.1 | 691.8 | −2.0% | −26.7040 to −1.9221 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.252 | 9.003 | +9.1% | +0.1552 to +1.3453 | yes: power given |
| pods started | 3.6 | 4.7 | +30.6% | −0.1367 to +2.3367 | no |
| pod start wait, total (s) | 6.2 | 7 | +12.9% | −1.3539 to +2.9539 | no |
| pod start wait, mean (s) | 1.6 | 1.525 | −4.7% | −0.4267 to +0.2758 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 29.33 | +3.4% | +0.7574 to +1.1794 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.514 | −0.4% | −0.0143 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.4 | −0.3% | −1.2145 to +0.3808 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.4 | −0.3% | −1.2145 to +0.3808 | no |
| response time (ms), mean | 84.86 | 86.88 | +2.4% | +1.0152 to +3.0305 | yes: LOSS |
| response time (ms), 95th percentile | 126.4 | 131.5 | +4.0% | +1.7065 to +8.5025 | yes: LOSS |
| response time (ms), 99th percentile | 166.9 | 181 | +8.4% | −1.9285 to +30.0717 | no |
| time over the response line (% of samples) | 0.02424 | 0 | −100.0% | −0.0608 to +0.0123 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 21.5 | +22.9% | +1.8942 to +6.1058 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.1867 | +0.9% | −0.1782 to +0.1815 | no |
| utilisation (used / allocatable) | 0.03896 | 0.04023 | +3.3% | +0.0006 to +0.0019 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.935 | 0.9655 | +3.3% | +0.0151 to +0.0461 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00846 | 0.06692 | +691.0% | +0.0511 to +0.0658 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9434 | 1.032 | +9.4% | +0.0711 to +0.1069 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.1 | 681.2 | −3.5% | −44.8984 to −4.9611 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.252 | 8.833 | +7.0% | −0.1240 to +1.2847 | no |
| pods started | 3.6 | 4.3 | +19.4% | −0.9537 to +2.3537 | no |
| pod start wait, total (s) | 6.2 | 6.9 | +11.3% | −2.4280 to +3.8280 | no |
| pod start wait, mean (s) | 1.6 | 1.622 | +1.4% | −0.4639 to +0.5072 | no |
| host CPU busy, the real machine under kind (%) | 28.36 | 30.97 | +9.2% | +2.1188 to +3.1088 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*