# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.519 | 1.516 | 1.516 | 1.518 | 1.518 | 1.518 | 1.517 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.6 | 159.6 | 159.8 | 159.9 | 159.9 | 159.8 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.6 | 159.6 | 159.8 | 159.9 | 159.9 | 159.8 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 178.5 | 87.58 | 87.8 | 88.41 | 88.18 | 88.46 | 88.66 | 89.05 |
| response time (ms), 95th percentile | 410.5 | 134.1 | 134.5 | 135.5 | 135 | 136.2 | 135.6 | 138.7 |
| response time (ms), 99th percentile | 684.1 | 185.8 | 187.4 | 184.5 | 187.6 | 183.5 | 182.4 | 196.6 |
| time over the response line (% of samples) | 3.137 | 0.03629 | 0 | 0.08485 | 0.02424 | 0.02424 | 0.03636 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | 16.8 | 19.2 | 18.3 | 19.5 | 19.5 | 20.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 90 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1083 | 0.1633 | 0.05333 | 0.135 | 0.08 | 0.05333 | 0.08 |
| utilisation (used / allocatable) | 0.04235 | 0.04008 | 0.04002 | 0.03993 | 0.04014 | 0.0402 | 0.04036 | 0.04074 |
| CPU used (cores), mean | 1.016 | 0.962 | 0.9605 | 0.9583 | 0.9634 | 0.9647 | 0.9686 | 0.9778 |
| Omni's own CPU (cores), mean | 0 | 0.00886 | 0.00641 | 0.00723 | 0.00787 | 0.01459 | 0.02567 | 0.06991 |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9709 | 0.9669 | 0.9656 | 0.9713 | 0.9793 | 0.9943 | 1.048 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 666.6 | 667.1 | 669.1 | 665.7 | 663.8 | 661.4 | 655.5 |
| HPA replicas, mean | 8.819 | 8.613 | 8.56 | 8.652 | 8.123 | 8.487 | 9.235 | 9.013 |
| pods started | 5.1 | 2.4 | 3.9 | 3.7 | 3 | 3.5 | 3.1 | 3.1 |
| pod start wait, total (s) | 8.7 | 3.5 | 5.7 | 6.1 | 4.2 | 5.4 | 4.8 | 5.1 |
| pod start wait, mean (s) | 1.69 | 1.403 | 1.497 | 1.64 | 1.383 | 1.517 | 1.517 | 1.35 |
| host CPU busy, the real machine under kind (%) | 30.28 | 28.95 | 29.01 | 29.03 | 29.12 | 29.42 | 29.71 | 31.49 |
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
| node-hours | 1.519 | 1.516 | −0.2% | −0.0093 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.6 | −0.5% | −1.5083 to −0.1565 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.6 | −0.5% | −1.5083 to −0.1565 | yes: GAIN |
| response time (ms), mean | 178.5 | 87.58 | −50.9% | −108.3250 to −73.4407 | yes: GAIN |
| response time (ms), 95th percentile | 410.5 | 134.1 | −67.3% | −326.1698 to −226.7162 | yes: GAIN |
| response time (ms), 99th percentile | 684.1 | 185.8 | −72.8% | −611.7037 to −384.8549 | yes: GAIN |
| time over the response line (% of samples) | 3.137 | 0.03629 | −98.8% | −4.2026 to −1.9988 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.7572 to −2.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.9 | +16.900 (native is 0) | +14.6519 to +19.1481 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1083 | −17.7% | −0.1663 to +0.1196 | no |
| utilisation (used / allocatable) | 0.04235 | 0.04008 | −5.4% | −0.0031 to −0.0014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.962 | −5.4% | −0.0749 to −0.0339 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00886 | +0.009 (native is 0) | +0.0082 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9709 | −4.5% | −0.0655 to −0.0257 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 666.6 | +4.8% | +19.5129 to +41.2163 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.819 | 8.613 | −2.3% | −1.1120 to +0.7000 | no |
| pods started | 5.1 | 2.4 | −52.9% | −3.9181 to −1.4819 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 3.5 | −59.8% | −7.4060 to −2.9940 | yes: GAIN |
| pod start wait, mean (s) | 1.69 | 1.403 | −17.0% | −0.8070 to +0.2337 | no |
| host CPU busy, the real machine under kind (%) | 30.28 | 28.95 | −4.4% | −1.8081 to −0.8395 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.519 | 1.516 | −0.2% | −0.0090 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.6 | −0.5% | −1.5123 to −0.1706 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.6 | −0.5% | −1.5123 to −0.1706 | yes: GAIN |
| response time (ms), mean | 178.5 | 87.8 | −50.8% | −108.2208 to −73.1064 | yes: GAIN |
| response time (ms), 95th percentile | 410.5 | 134.5 | −67.2% | −327.2205 to −224.8745 | yes: GAIN |
| response time (ms), 99th percentile | 684.1 | 187.4 | −72.6% | −605.4030 to −387.9354 | yes: GAIN |
| time over the response line (% of samples) | 3.137 | 0 | −100.0% | −4.2512 to −2.0227 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.7572 to −2.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.8 | +16.800 (native is 0) | +15.6417 to +17.9583 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1633 | +24.1% | −0.2020 to +0.2653 | no |
| utilisation (used / allocatable) | 0.04235 | 0.04002 | −5.5% | −0.0032 to −0.0015 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9605 | −5.5% | −0.0762 to −0.0357 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00641 | +0.006 (native is 0) | +0.0059 to +0.0069 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9669 | −4.9% | −0.0695 to −0.0297 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 667.1 | +4.9% | +18.6842 to +43.0853 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.819 | 8.56 | −2.9% | −0.6281 to +0.1116 | no |
| pods started | 5.1 | 3.9 | −23.5% | −2.3583 to −0.0417 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 5.7 | −34.5% | −5.2620 to −0.7380 | yes: GAIN |
| pod start wait, mean (s) | 1.69 | 1.497 | −11.4% | −0.5455 to +0.1589 | no |
| host CPU busy, the real machine under kind (%) | 30.28 | 29.01 | −4.2% | −1.8907 to −0.6433 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.518 | −0.1% | −0.0024 to +0.0008 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.8 | −0.4% | −0.8265 to −0.4686 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.8 | −0.4% | −0.8265 to −0.4686 | yes: GAIN |
| response time (ms), mean | 178.5 | 88.41 | −50.5% | −107.0789 to −73.0266 | yes: GAIN |
| response time (ms), 95th percentile | 410.5 | 135.5 | −67.0% | −324.5785 to −225.4515 | yes: GAIN |
| response time (ms), 99th percentile | 684.1 | 184.5 | −73.0% | −609.4401 to −389.6213 | yes: GAIN |
| time over the response line (% of samples) | 3.137 | 0.08485 | −97.3% | −4.1362 to −1.9680 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.7572 to −2.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | +19.200 (native is 0) | +17.8597 to +20.5403 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.05333 | −59.5% | −0.1714 to +0.0147 | no |
| utilisation (used / allocatable) | 0.04235 | 0.03993 | −5.7% | −0.0033 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9583 | −5.7% | −0.0789 to −0.0374 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00723 | +0.007 (native is 0) | +0.0068 to +0.0077 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9656 | −5.0% | −0.0713 to −0.0305 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 669.1 | +5.2% | +22.8952 to +42.9210 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.819 | 8.652 | −1.9% | −0.5101 to +0.1775 | no |
| pods started | 5.1 | 3.7 | −27.5% | −2.4228 to −0.3772 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 6.1 | −29.9% | −5.3228 to +0.1228 | no |
| pod start wait, mean (s) | 1.69 | 1.64 | −2.9% | −0.5887 to +0.4896 | no |
| host CPU busy, the real machine under kind (%) | 30.28 | 29.03 | −4.1% | −1.7622 to −0.7385 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.518 | −0.0% | −0.0025 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.9 | −0.3% | −0.7879 to −0.2182 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.9 | −0.3% | −0.7879 to −0.2182 | yes: GAIN |
| response time (ms), mean | 178.5 | 88.18 | −50.6% | −107.7167 to −72.8428 | yes: GAIN |
| response time (ms), 95th percentile | 410.5 | 135 | −67.1% | −326.1306 to −224.8094 | yes: GAIN |
| response time (ms), 99th percentile | 684.1 | 187.6 | −72.6% | −608.1303 to −384.8905 | yes: GAIN |
| time over the response line (% of samples) | 3.137 | 0.02424 | −99.2% | −4.2239 to −2.0015 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.7572 to −2.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | +18.300 (native is 0) | +15.3210 to +21.2790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.135 | +2.5% | −0.1822 to +0.1889 | no |
| utilisation (used / allocatable) | 0.04235 | 0.04014 | −5.2% | −0.0030 to −0.0014 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9634 | −5.2% | −0.0720 to −0.0342 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00787 | +0.008 (native is 0) | +0.0071 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9713 | −4.4% | −0.0635 to −0.0269 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 665.7 | +4.6% | +19.3138 to +39.7569 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.819 | 8.123 | −7.9% | −1.5508 to +0.1596 | no |
| pods started | 5.1 | 3 | −41.2% | −3.0802 to −1.1198 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 4.2 | −51.7% | −6.6918 to −2.3082 | yes: GAIN |
| pod start wait, mean (s) | 1.69 | 1.383 | −18.1% | −0.6512 to +0.0379 | no |
| host CPU busy, the real machine under kind (%) | 30.28 | 29.12 | −3.8% | −1.6851 to −0.6173 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.518 | −0.0% | −0.0019 to +0.0012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.9 | −0.3% | −0.8226 to −0.2263 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.9 | −0.3% | −0.8226 to −0.2263 | yes: GAIN |
| response time (ms), mean | 178.5 | 88.46 | −50.4% | −107.4648 to −72.5359 | yes: GAIN |
| response time (ms), 95th percentile | 410.5 | 136.2 | −66.8% | −324.4024 to −224.1326 | yes: GAIN |
| response time (ms), 99th percentile | 684.1 | 183.5 | −73.2% | −612.5798 to −388.5520 | yes: GAIN |
| time over the response line (% of samples) | 3.137 | 0.02424 | −99.2% | −4.2205 to −2.0049 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.7572 to −2.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.500 (native is 0) | +18.4744 to +20.5256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.08 | −39.2% | −0.1707 to +0.0673 | no |
| utilisation (used / allocatable) | 0.04235 | 0.0402 | −5.1% | −0.0031 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9647 | −5.1% | −0.0744 to −0.0291 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01459 | +0.015 (native is 0) | +0.0136 to +0.0156 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9793 | −3.7% | −0.0590 to −0.0154 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 663.8 | +4.3% | +13.9852 to +41.1697 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.819 | 8.487 | −3.8% | −0.6449 to −0.0188 | yes: GAIN |
| pods started | 5.1 | 3.5 | −31.4% | −2.5656 to −0.6344 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 5.4 | −37.9% | −6.0611 to −0.5389 | yes: GAIN |
| pod start wait, mean (s) | 1.69 | 1.517 | −10.3% | −0.6579 to +0.3113 | no |
| host CPU busy, the real machine under kind (%) | 30.28 | 29.42 | −2.8% | −1.5098 to −0.1995 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.519 | 1.517 | −0.1% | −0.0074 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.8 | −0.4% | −1.2116 to −0.0912 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.8 | −0.4% | −1.2116 to −0.0912 | yes: GAIN |
| response time (ms), mean | 178.5 | 88.66 | −50.3% | −106.9607 to −72.6426 | yes: GAIN |
| response time (ms), 95th percentile | 410.5 | 135.6 | −67.0% | −324.5740 to −225.1830 | yes: GAIN |
| response time (ms), 99th percentile | 684.1 | 182.4 | −73.3% | −604.1133 to −399.1427 | yes: GAIN |
| time over the response line (% of samples) | 3.137 | 0.03636 | −98.8% | −4.2015 to −1.9997 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.7572 to −2.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.500 (native is 0) | +17.9826 to +21.0174 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.05333 | −59.5% | −0.2077 to +0.0511 | no |
| utilisation (used / allocatable) | 0.04235 | 0.04036 | −4.7% | −0.0030 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9686 | −4.7% | −0.0709 to −0.0249 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02567 | +0.026 (native is 0) | +0.0238 to +0.0275 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9943 | −2.2% | −0.0438 to −0.0006 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 661.4 | +4.0% | +11.3174 to +39.1108 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.819 | 9.235 | +4.7% | +0.0837 to +0.7493 | yes: power given |
| pods started | 5.1 | 3.1 | −39.2% | −3.3060 to −0.6940 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 4.8 | −44.8% | −7.0892 to −0.7108 | yes: GAIN |
| pod start wait, mean (s) | 1.69 | 1.517 | −10.3% | −0.6598 to +0.3131 | no |
| host CPU busy, the real machine under kind (%) | 30.28 | 29.71 | −1.9% | −1.1591 to +0.0296 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.512 | −0.4% | −0.0157 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 159.4 | −0.6% | −2.0471 to −0.0083 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 159.4 | −0.6% | −2.0471 to −0.0083 | yes: GAIN |
| response time (ms), mean | 178.5 | 89.05 | −50.1% | −106.9963 to −71.8223 | yes: GAIN |
| response time (ms), 95th percentile | 410.5 | 138.7 | −66.2% | −321.2326 to −222.4524 | yes: GAIN |
| response time (ms), 99th percentile | 684.1 | 196.6 | −71.3% | −591.4549 to −383.5165 | yes: GAIN |
| time over the response line (% of samples) | 3.137 | 0 | −100.0% | −4.2512 to −2.0227 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.4 | 0 | −100.0% | −4.7572 to −2.0428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.4 | +20.400 (native is 0) | +18.5165 to +22.2835 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.08 | −39.2% | −0.2258 to +0.1225 | no |
| utilisation (used / allocatable) | 0.04235 | 0.04074 | −3.8% | −0.0024 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9778 | −3.8% | −0.0586 to −0.0187 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06991 | +0.070 (native is 0) | +0.0651 to +0.0747 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 1.048 | +3.1% | +0.0143 to +0.0482 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 636.2 | 655.5 | +3.0% | +4.6896 to +33.8622 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.819 | 9.013 | +2.2% | −0.1744 to +0.5639 | no |
| pods started | 5.1 | 3.1 | −39.2% | −3.2158 to −0.7842 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 5.1 | −41.4% | −5.9410 to −1.2590 | yes: GAIN |
| pod start wait, mean (s) | 1.69 | 1.35 | −20.1% | −0.7359 to +0.0559 | no |
| host CPU busy, the real machine under kind (%) | 30.28 | 31.49 | +4.0% | +0.6310 to +1.7918 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | +0.0% | −0.0007 to +0.0010 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.6 | −0.0% | −0.2227 to +0.2046 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.6 | −0.0% | −0.2227 to +0.2046 | no |
| response time (ms), mean | 87.58 | 87.8 | +0.3% | −1.1801 to +1.6187 | no |
| response time (ms), 95th percentile | 134.1 | 134.5 | +0.3% | −3.6315 to +4.4225 | no |
| response time (ms), 99th percentile | 185.8 | 187.4 | +0.9% | −22.3373 to +25.5575 | no |
| time over the response line (% of samples) | 0.03629 | 0 | −100.0% | −0.0781 to +0.0055 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 16.8 | −0.6% | −2.4712 to +2.2712 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.1633 | +50.8% | −0.1825 to +0.2925 | no |
| utilisation (used / allocatable) | 0.04008 | 0.04002 | −0.2% | −0.0007 to +0.0006 | no |
| CPU used (cores), mean | 0.962 | 0.9605 | −0.2% | −0.0180 to +0.0149 | no |
| Omni's own CPU (cores), mean | 0.00886 | 0.00641 | −27.7% | −0.0028 to −0.0021 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9709 | 0.9669 | −0.4% | −0.0205 to +0.0126 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.6 | 667.1 | +0.1% | −10.6172 to +11.6576 | no |
| HPA replicas, mean | 8.613 | 8.56 | −0.6% | −0.9581 to +0.8536 | no |
| pods started | 2.4 | 3.9 | +62.5% | −0.0544 to +3.0544 | no |
| pod start wait, total (s) | 3.5 | 5.7 | +62.9% | +0.3286 to +4.0714 | yes: LOSS |
| pod start wait, mean (s) | 1.403 | 1.497 | +6.7% | −0.5317 to +0.7183 | no |
| host CPU busy, the real machine under kind (%) | 28.95 | 29.01 | +0.2% | −0.3468 to +0.4605 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.2% | −0.0040 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.8 | +0.1% | −0.4582 to +0.8279 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.8 | +0.1% | −0.4582 to +0.8279 | no |
| response time (ms), mean | 87.58 | 88.41 | +0.9% | −0.2630 to +1.9232 | no |
| response time (ms), 95th percentile | 134.1 | 135.5 | +1.1% | −0.4566 to +3.3126 | no |
| response time (ms), 99th percentile | 185.8 | 184.5 | −0.7% | −25.0282 to +22.5254 | no |
| time over the response line (% of samples) | 0.03629 | 0.08485 | +133.8% | −0.0532 to +0.1503 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 19.2 | +13.6% | −0.8280 to +5.4280 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.05333 | −50.8% | −0.1349 to +0.0249 | no |
| utilisation (used / allocatable) | 0.04008 | 0.03993 | −0.4% | −0.0007 to +0.0004 | no |
| CPU used (cores), mean | 0.962 | 0.9583 | −0.4% | −0.0168 to +0.0095 | no |
| Omni's own CPU (cores), mean | 0.00886 | 0.00723 | −18.4% | −0.0019 to −0.0013 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9709 | 0.9656 | −0.5% | −0.0185 to +0.0079 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.6 | 669.1 | +0.4% | −5.4417 to +10.5289 | no |
| HPA replicas, mean | 8.613 | 8.652 | +0.5% | −0.8889 to +0.9683 | no |
| pods started | 2.4 | 3.7 | +54.2% | −0.2834 to +2.8834 | no |
| pod start wait, total (s) | 3.5 | 6.1 | +74.3% | −0.2850 to +5.4850 | no |
| pod start wait, mean (s) | 1.403 | 1.64 | +16.9% | −0.0509 to +0.5252 | no |
| host CPU busy, the real machine under kind (%) | 28.95 | 29.03 | +0.3% | −0.1984 to +0.3453 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.2% | −0.0034 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.9 | +0.2% | −0.3290 to +0.9877 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.9 | +0.2% | −0.3290 to +0.9877 | no |
| response time (ms), mean | 87.58 | 88.18 | +0.7% | −0.8394 to +2.0456 | no |
| response time (ms), 95th percentile | 134.1 | 135 | +0.7% | −2.1062 to +4.0522 | no |
| response time (ms), 99th percentile | 185.8 | 187.6 | +1.0% | −24.3429 to +27.8807 | no |
| time over the response line (% of samples) | 0.03629 | 0.02424 | −33.2% | −0.0613 to +0.0372 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 18.3 | +8.3% | −1.4850 to +4.2850 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.135 | +24.6% | −0.1495 to +0.2028 | no |
| utilisation (used / allocatable) | 0.04008 | 0.04014 | +0.1% | −0.0005 to +0.0006 | no |
| CPU used (cores), mean | 0.962 | 0.9634 | +0.1% | −0.0113 to +0.0140 | no |
| Omni's own CPU (cores), mean | 0.00886 | 0.00787 | −11.2% | −0.0013 to −0.0007 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9709 | 0.9713 | +0.0% | −0.0124 to +0.0131 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.6 | 665.7 | −0.1% | −8.8294 to +7.1710 | no |
| HPA replicas, mean | 8.613 | 8.123 | −5.7% | −1.1620 to +0.1829 | no |
| pods started | 2.4 | 3 | +25.0% | −0.8775 to +2.0775 | no |
| pod start wait, total (s) | 3.5 | 4.2 | +20.0% | −1.8912 to +3.2912 | no |
| pod start wait, mean (s) | 1.403 | 1.383 | −1.4% | −0.6316 to +0.5916 | no |
| host CPU busy, the real machine under kind (%) | 28.95 | 29.12 | +0.6% | −0.1631 to +0.5084 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.2% | −0.0030 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.9 | +0.2% | −0.3179 to +0.9338 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.9 | +0.2% | −0.3179 to +0.9338 | no |
| response time (ms), mean | 87.58 | 88.46 | +1.0% | −0.7860 to +2.5510 | no |
| response time (ms), 95th percentile | 134.1 | 136.2 | +1.6% | −1.1195 to +5.4705 | no |
| response time (ms), 99th percentile | 185.8 | 183.5 | −1.2% | −21.6643 to +17.0911 | no |
| time over the response line (% of samples) | 0.03629 | 0.02424 | −33.2% | −0.0760 to +0.0519 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 19.5 | +15.4% | −0.0594 to +5.2594 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.08 | −26.2% | −0.2394 to +0.1827 | no |
| utilisation (used / allocatable) | 0.04008 | 0.0402 | +0.3% | −0.0004 to +0.0006 | no |
| CPU used (cores), mean | 0.962 | 0.9647 | +0.3% | −0.0095 to +0.0149 | no |
| Omni's own CPU (cores), mean | 0.00886 | 0.01459 | +64.7% | +0.0053 to +0.0062 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9709 | 0.9793 | +0.9% | −0.0039 to +0.0208 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.6 | 663.8 | −0.4% | −11.1002 to +5.5259 | no |
| HPA replicas, mean | 8.613 | 8.487 | −1.5% | −1.0934 to +0.8417 | no |
| pods started | 2.4 | 3.5 | +45.8% | −0.5673 to +2.7673 | no |
| pod start wait, total (s) | 3.5 | 5.4 | +54.3% | −1.3597 to +5.1597 | no |
| pod start wait, mean (s) | 1.403 | 1.517 | +8.1% | −0.5598 to +0.7864 | no |
| host CPU busy, the real machine under kind (%) | 28.95 | 29.42 | +1.6% | +0.1159 to +0.8225 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.517 | +0.1% | −0.0001 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.8 | +0.1% | −0.0662 to +0.4282 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.8 | +0.1% | −0.0662 to +0.4282 | no |
| response time (ms), mean | 87.58 | 88.66 | +1.2% | −0.3508 to +2.5132 | no |
| response time (ms), 95th percentile | 134.1 | 135.6 | +1.2% | −0.9308 to +4.0598 | no |
| response time (ms), 99th percentile | 185.8 | 182.4 | −1.8% | −29.8666 to +23.1692 | no |
| time over the response line (% of samples) | 0.03629 | 0.03636 | +0.2% | −0.0576 to +0.0578 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 19.5 | +15.4% | −0.4385 to +5.6385 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.05333 | −50.8% | −0.1774 to +0.0674 | no |
| utilisation (used / allocatable) | 0.04008 | 0.04036 | +0.7% | −0.0003 to +0.0009 | no |
| CPU used (cores), mean | 0.962 | 0.9686 | +0.7% | −0.0081 to +0.0213 | no |
| Omni's own CPU (cores), mean | 0.00886 | 0.02567 | +189.7% | +0.0155 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9709 | 0.9943 | +2.4% | +0.0086 to +0.0382 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.6 | 661.4 | −0.8% | −14.1878 to +3.8869 | no |
| HPA replicas, mean | 8.613 | 9.235 | +7.2% | −0.1729 to +1.4178 | no |
| pods started | 2.4 | 3.1 | +29.2% | −0.9537 to +2.3537 | no |
| pod start wait, total (s) | 3.5 | 4.8 | +37.1% | −1.2245 to +3.8245 | no |
| pod start wait, mean (s) | 1.403 | 1.517 | +8.1% | −0.4085 to +0.6351 | no |
| host CPU busy, the real machine under kind (%) | 28.95 | 29.71 | +2.6% | +0.4099 to +1.1083 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.512 | −0.2% | −0.0110 to +0.0044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.4 | −0.1% | −0.9999 to +0.6093 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.4 | −0.1% | −0.9999 to +0.6093 | no |
| response time (ms), mean | 87.58 | 89.05 | +1.7% | +0.2698 to +2.6773 | yes: LOSS |
| response time (ms), 95th percentile | 134.1 | 138.7 | +3.4% | +1.3386 to +7.8624 | yes: LOSS |
| response time (ms), 99th percentile | 185.8 | 196.6 | +5.8% | −13.8060 to +35.3932 | no |
| time over the response line (% of samples) | 0.03629 | 0 | −100.0% | −0.0781 to +0.0055 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.9 | 20.4 | +20.7% | +0.6738 to +6.3262 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.08 | −26.2% | −0.1968 to +0.1401 | no |
| utilisation (used / allocatable) | 0.04008 | 0.04074 | +1.6% | +0.0002 to +0.0011 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.962 | 0.9778 | +1.6% | +0.0047 to +0.0269 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00886 | 0.06991 | +689.1% | +0.0569 to +0.0652 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9709 | 1.048 | +7.9% | +0.0638 to +0.0899 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 666.6 | 655.5 | −1.7% | −20.4072 to −1.7701 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.613 | 9.013 | +4.7% | −0.4904 to +1.2920 | no |
| pods started | 2.4 | 3.1 | +29.2% | −0.9537 to +2.3537 | no |
| pod start wait, total (s) | 3.5 | 5.1 | +45.7% | −1.5488 to +4.7488 | no |
| pod start wait, mean (s) | 1.403 | 1.35 | −3.8% | −0.7871 to +0.6805 | no |
| host CPU busy, the real machine under kind (%) | 28.95 | 31.49 | +8.8% | +2.1767 to +2.8937 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*