# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.509 | 1.509 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 171 | 85.46 | 89.79 |
| response time (ms), 95th percentile | 397.8 | 129.8 | 128.5 |
| response time (ms), 99th percentile | 612.2 | 180.2 | 177.6 |
| time over the response line (% of samples) | 2.891 | 0.04863 | 0.2922 |
| failed requests (%) | 0 | 0 | 0.1238 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | 16.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.22 | 0.2433 | 0.5417 |
| utilisation (used / allocatable) | 0.04189 | 0.03944 | 0.0401 |
| CPU used (cores), mean | 1.005 | 0.9467 | 0.9623 |
| Omni's own CPU (cores), mean | 0 | 0.00949 | 0.00923 |
| CPU used with Omni's own (cores), mean | 1.005 | 0.9561 | 0.9715 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 658 | 689.4 | 680.6 |
| HPA replicas, mean | 8.639 | 8.543 | 9.736 |
| pods started | 5.1 | 3.1 | 9 |
| pod start wait, total (s) | 8.5 | 4.6 | 17.5 |
| pod start wait, mean (s) | 1.675 | 1.295 | 1.944 |
| host CPU busy, the real machine under kind (%) | 30.26 | 29.18 | 29.88 |
| host cores (the real machine under kind) | 4 | 4 | 4 |

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
| node-hours | 1.509 | 1.51 | +0.0% | −0.0011 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | −0.3% | −0.7992 to −0.2502 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | −0.3% | −0.7992 to −0.2502 | yes: GAIN |
| response time (ms), mean | 171 | 85.46 | −50.0% | −107.1410 to −63.8473 | yes: GAIN |
| response time (ms), 95th percentile | 397.8 | 129.8 | −67.4% | −334.4865 to −201.4935 | yes: GAIN |
| response time (ms), 99th percentile | 612.2 | 180.2 | −70.6% | −538.3124 to −325.7372 | yes: GAIN |
| time over the response line (% of samples) | 2.891 | 0.04863 | −98.3% | −4.2878 to −1.3977 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 0 | −100.0% | −4.3379 to −1.2621 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | +18.600 (native is 0) | +15.5991 to +21.6009 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.22 | 0.2433 | +10.6% | −0.3541 to +0.4008 | no |
| utilisation (used / allocatable) | 0.04189 | 0.03944 | −5.8% | −0.0034 to −0.0015 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.005 | 0.9467 | −5.8% | −0.0822 to −0.0351 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00949 | +0.009 (native is 0) | +0.0083 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.005 | 0.9561 | −4.9% | −0.0718 to −0.0265 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 658 | 689.4 | +4.8% | +18.7630 to +44.0044 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.639 | 8.543 | −1.1% | −0.6759 to +0.4838 | no |
| pods started | 5.1 | 3.1 | −39.2% | −3.1681 to −0.8319 | yes: GAIN |
| pod start wait, total (s) | 8.5 | 4.6 | −45.9% | −7.4916 to −0.3084 | yes: GAIN |
| pod start wait, mean (s) | 1.675 | 1.295 | −22.7% | −0.9849 to +0.2249 | no |
| host CPU busy, the real machine under kind (%) | 30.26 | 29.18 | −3.6% | −1.7103 to −0.4533 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.509 | 1.514 | +0.3% | −0.0018 to +0.0112 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.4 | +0.1% | −0.5058 to +0.7219 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.4 | +0.1% | −0.5058 to +0.7219 | no |
| response time (ms), mean | 171 | 89.79 | −47.5% | −101.9008 to −60.4201 | yes: GAIN |
| response time (ms), 95th percentile | 397.8 | 128.5 | −67.7% | −336.0506 to −202.4154 | yes: GAIN |
| response time (ms), 99th percentile | 612.2 | 177.6 | −71.0% | −547.3406 to −321.8672 | yes: GAIN |
| time over the response line (% of samples) | 2.891 | 0.2922 | −89.9% | −4.0951 to −1.1034 | yes: GAIN |
| failed requests (%) | 0 | 0.1238 | +0.124 (native is 0) | +0.0514 to +0.1962 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 0.3 | −89.3% | −4.1944 to −0.8056 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 | +16.600 (native is 0) | +14.2834 to +18.9166 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.22 | 0.5417 | +146.2% | −0.1066 to +0.7500 | no |
| utilisation (used / allocatable) | 0.04189 | 0.0401 | −4.3% | −0.0026 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.005 | 0.9623 | −4.3% | −0.0623 to −0.0237 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00923 | +0.009 (native is 0) | +0.0084 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.005 | 0.9715 | −3.4% | −0.0524 to −0.0151 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 658 | 680.6 | +3.4% | +10.8101 to +34.2199 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.639 | 9.736 | +12.7% | +0.6956 to +1.4978 | yes: power given |
| pods started | 5.1 | 9 | +76.5% | +3.4940 to +4.3060 | yes: power given |
| pod start wait, total (s) | 8.5 | 17.5 | +105.9% | +5.8189 to +12.1811 | yes: LOSS |
| pod start wait, mean (s) | 1.675 | 1.944 | +16.1% | −0.0726 to +0.6115 | no |
| host CPU busy, the real machine under kind (%) | 30.26 | 29.88 | −1.3% | −0.8640 to +0.0876 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.509 | 1.514 | +0.3% | −0.0024 to +0.0111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.4 | +0.4% | −0.1171 to +1.3825 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.4 | +0.4% | −0.1171 to +1.3825 | no |
| response time (ms), mean | 85.46 | 89.79 | +5.1% | +0.4994 to +8.1680 | yes: LOSS |
| response time (ms), 95th percentile | 129.8 | 128.5 | −1.0% | −3.5503 to +1.0643 | no |
| response time (ms), 99th percentile | 180.2 | 177.6 | −1.4% | −28.6817 to +23.5235 | no |
| time over the response line (% of samples) | 0.04863 | 0.2922 | +500.7% | +0.1455 to +0.3416 | yes: LOSS |
| failed requests (%) | 0 | 0.1238 | +0.124 (native is 0) | +0.0514 to +0.1962 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 18.6 | 16.6 | −10.8% | −6.0182 to +2.0182 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2433 | 0.5417 | +122.6% | −0.1352 to +0.7319 | no |
| utilisation (used / allocatable) | 0.03944 | 0.0401 | +1.7% | +0.0002 to +0.0011 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9467 | 0.9623 | +1.7% | +0.0055 to +0.0258 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00949 | 0.00923 | −2.7% | −0.0008 to +0.0003 | no |
| CPU used with Omni's own (cores), mean | 0.9561 | 0.9715 | +1.6% | +0.0053 to +0.0254 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 689.4 | 680.6 | −1.3% | −15.0873 to −2.6501 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.543 | 9.736 | +14.0% | +0.5336 to +1.8518 | yes: power given |
| pods started | 3.1 | 9 | +190.3% | +4.6633 to +7.1367 | yes: power given |
| pod start wait, total (s) | 4.6 | 17.5 | +280.4% | +7.9048 to +17.8952 | yes: LOSS |
| pod start wait, mean (s) | 1.295 | 1.944 | +50.2% | +0.0080 to +1.2909 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 29.18 | 29.88 | +2.4% | +0.2219 to +1.1652 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*