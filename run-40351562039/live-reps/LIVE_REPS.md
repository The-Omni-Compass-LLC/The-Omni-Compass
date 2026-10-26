# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.669 | 6 |
| node-hours | 2.517 | 2.517 | 2.377 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 286.8 | 273.6 | 286.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 286.8 | 263.2 | 286.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 353.6 | 756.3 | 313.1 | 720.2 |
| response time (ms), 95th percentile | 1132 | 1540 | 1165 | 1482 |
| response time (ms), 99th percentile | 1644 | 2069 | 1707 | 1983 |
| time over the response line (% of samples) | 22.15 | 67.76 | 21.55 | 65.35 |
| failed requests (%) | 0 | 0 | 0 | 0.01149 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 25 | 11.9 | 25 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 26.3 | 17.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 2.4 | 12.09 | 2.455 |
| utilisation (used / allocatable) | 0.06192 | 0.09802 | 0.06635 | 0.09799 |
| CPU used (cores), mean | 1.486 | 2.352 | 1.501 | 2.352 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01641 | 0.00986 |
| CPU used with Omni's own (cores), mean | 1.486 | 2.352 | 1.518 | 2.362 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.3 | 290.7 | 418.5 | 290.9 |
| HPA replicas, mean | 2.048 | 2.094 | 2.059 | 2.854 |
| pods started | 0 | 0.4 | 0.4 | 0.1 |
| pod start wait, total (s) | 0 | 0.5 | 0.9 | 0.2 |
| pod start wait, mean (s) | 0 | 0.35 | 0.45 | 0.2 |
| host CPU busy, the real machine under kind (%) | 42.32 | 76.82 | 43.28 | 77.19 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 767.6 | 1510 | 772.3 | 1510 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 5.333 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 838.8 | 0.0625 | 842.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1416 | 0.4 | 1391 |
| queue: job turnaround, submitted to done, mean (s) | 75.74 | 1056 | 81.15 | 1064 |
| queue: jobs unfinished at the window's end | 0 | 18.3 | 0 | 18.5 |

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
| node-hours | 2.517 | 2.516 | −0.0% | −0.0102 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.8 | 286.7 | −0.0% | −1.0587 to +0.9109 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.8 | 286.7 | −0.0% | −1.0587 to +0.9109 | no |
| response time (ms), mean | 756.3 | 720.2 | −4.8% | −97.5236 to +25.2185 | no |
| response time (ms), 95th percentile | 1540 | 1482 | −3.7% | −183.7934 to +69.2504 | no |
| response time (ms), 99th percentile | 2069 | 1983 | −4.2% | −266.5714 to +93.4224 | no |
| time over the response line (% of samples) | 67.76 | 65.35 | −3.6% | −6.6532 to +1.8291 | no |
| failed requests (%) | 0 | 0.01149 | +0.011 (native is 0) | −0.0145 to +0.0375 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 25 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 | +17.200 (native is 0) | +15.0199 to +19.3801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.4 | 2.455 | +2.3% | −0.0265 to +0.1365 | no |
| utilisation (used / allocatable) | 0.09802 | 0.09799 | −0.0% | −0.0007 to +0.0006 | no |
| CPU used (cores), mean | 2.352 | 2.352 | −0.0% | −0.0162 to +0.0151 | no |
| Omni's own CPU (cores), mean | 0 | 0.00986 | +0.010 (native is 0) | +0.0093 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.352 | 2.362 | +0.4% | −0.0060 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.7 | 290.9 | +0.1% | −1.5493 to +1.8522 | no |
| HPA replicas, mean | 2.094 | 2.854 | +36.3% | +0.6088 to +0.9109 | yes: power given |
| pods started | 0.4 | 0.1 | −75.0% | −0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.5 | 0.2 | −60.0% | −1.0578 to +0.4578 | no |
| pod start wait, mean (s) | 0.35 | 0.2 | −42.9% | −0.6284 to +0.3284 | no |
| host CPU busy, the real machine under kind (%) | 76.82 | 77.19 | +0.5% | +0.2951 to +0.4553 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 1510 | ±0.0% | −5.1911 to +5.1911 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 838.8 | 842.1 | +0.4% | −60.5727 to +67.1612 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1416 | 1391 | −1.7% | −61.0145 to +12.0145 | no |
| queue: job turnaround, submitted to done, mean (s) | 1056 | 1064 | +0.8% | −36.4808 to +52.4225 | no |
| queue: jobs unfinished at the window's end | 18.3 | 18.5 | +1.1% | −1.1403 to +1.5403 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.517 | −0.0% | −0.0091 to +0.0081 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 286.8 | +4.9% | +12.0240 to +14.7558 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 286.8 | +4.9% | +12.0240 to +14.7558 | yes: power given |
| response time (ms), mean | 353.6 | 756.3 | +113.9% | +337.1554 to +468.1894 | yes: LOSS |
| response time (ms), 95th percentile | 1132 | 1540 | +36.0% | +189.6650 to +626.0250 | yes: LOSS |
| response time (ms), 99th percentile | 1644 | 2069 | +25.9% | +128.9713 to +721.2765 | yes: LOSS |
| time over the response line (% of samples) | 22.15 | 67.76 | +205.9% | +40.6421 to +50.5769 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 25 | +110.1% | +10.8519 to +15.3481 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 2.4 | −77.3% | −9.7032 to −6.6835 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06192 | 0.09802 | +58.3% | +0.0321 to +0.0401 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 2.352 | +58.3% | +0.7699 to +0.9630 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.486 | 2.352 | +58.3% | +0.7699 to +0.9630 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.3 | 290.7 | −34.0% | −173.9135 to −125.2832 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.048 | 2.094 | +2.3% | −0.0893 to +0.1821 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1952 to +1.1952 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.350 (native is 0) | −0.0647 to +0.7647 | no |
| host CPU busy, the real machine under kind (%) | 42.32 | 76.82 | +81.5% | +32.7711 to +36.2257 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.6 | 1510 | +96.7% | +727.4975 to +757.3025 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 838.8 | +1184086.0% | +720.0990 to +957.3562 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1416 | +235850.0% | +1376.4580 to +1453.7420 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 75.74 | 1056 | +1294.3% | +937.4086 to +1023.1998 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 18.3 | +18.300 (native is 0) | +16.2475 to +20.3525 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.669 | −5.5% | −0.6813 to +0.0191 | no |
| node-hours | 2.517 | 2.377 | −5.6% | −0.2897 to +0.0096 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.6 | +0.1% | −0.6366 to +0.9494 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 263.2 | −3.7% | −21.5674 to +1.0718 | no |
| response time (ms), mean | 353.6 | 313.1 | −11.5% | −53.3742 to −27.6592 | yes: GAIN |
| response time (ms), 95th percentile | 1132 | 1165 | +2.9% | −41.8536 to +108.0106 | no |
| response time (ms), 99th percentile | 1644 | 1707 | +3.8% | −52.9509 to +178.5361 | no |
| time over the response line (% of samples) | 22.15 | 21.55 | −2.7% | −1.8242 to +0.6059 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 11.9 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 | +26.300 (native is 0) | +9.9605 to +42.6395 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 12.09 | +14.1% | −0.2458 to +3.2324 | no |
| utilisation (used / allocatable) | 0.06192 | 0.06635 | +7.2% | +0.0005 to +0.0083 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 1.501 | +1.0% | +0.0024 to +0.0279 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01641 | +0.016 (native is 0) | +0.0148 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.486 | 1.518 | +2.1% | +0.0180 to +0.0451 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.3 | 418.5 | −5.0% | −41.3272 to −2.3589 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.048 | 2.059 | +0.6% | −0.1289 to +0.1521 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.5484 to +2.3484 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | −0.2742 to +1.1742 | no |
| host CPU busy, the real machine under kind (%) | 42.32 | 43.28 | +2.3% | +0.6538 to +1.2621 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.6 | 772.3 | +0.6% | +0.3028 to +9.0972 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.333 | −11.1% | −1.3633 to +0.0292 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0625 | −11.8% | −0.0566 to +0.0399 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.8573 to +0.4573 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.74 | 81.15 | +7.1% | +0.8181 to +10.0069 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.669 | −5.5% | −0.6813 to +0.0191 | no |
| node-hours | 2.517 | 2.377 | −5.5% | −0.2872 to +0.0081 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.8 | 273.6 | −4.6% | −14.7413 to −11.7258 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.8 | 263.2 | −8.2% | −35.8859 to −11.3895 | yes: GAIN |
| response time (ms), mean | 756.3 | 313.1 | −58.6% | −512.7035 to −373.6747 | yes: GAIN |
| response time (ms), 95th percentile | 1540 | 1165 | −24.3% | −611.4242 to −138.1088 | yes: GAIN |
| response time (ms), 99th percentile | 2069 | 1707 | −17.5% | −695.2383 to −29.4243 | yes: GAIN |
| time over the response line (% of samples) | 67.76 | 21.55 | −68.2% | −51.1053 to −41.3321 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 11.9 | −52.4% | −15.3481 to −10.8519 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 | +26.300 (native is 0) | +9.9605 to +42.6395 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.4 | 12.09 | +403.6% | +7.7132 to +11.6601 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09802 | 0.06635 | −32.3% | −0.0343 to −0.0291 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.352 | 1.501 | −36.2% | −0.9520 to −0.7506 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01641 | +0.016 (native is 0) | +0.0148 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.352 | 1.518 | −35.5% | −0.9357 to −0.7341 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.7 | 418.5 | +43.9% | +115.7886 to +139.7221 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.094 | 2.059 | −1.7% | −0.1730 to +0.1033 | no |
| pods started | 0.4 | 0.4 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.5 | 0.9 | +80.0% | −1.0385 to +1.8385 | no |
| pod start wait, mean (s) | 0.35 | 0.45 | +28.6% | −0.6872 to +0.8872 | no |
| host CPU busy, the real machine under kind (%) | 76.82 | 43.28 | −43.7% | −35.2337 to −31.8471 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 772.3 | −48.9% | −751.8866 to −723.5134 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 838.8 | 0.0625 | −100.0% | −957.3699 to −720.1019 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1416 | 0.4 | −100.0% | −1454.2404 to −1376.3596 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1056 | 81.15 | −92.3% | −1017.3767 to −932.4067 | yes: GAIN |
| queue: jobs unfinished at the window's end | 18.3 | 0 | −100.0% | −20.3525 to −16.2475 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.516 | −0.1% | −0.0088 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 286.7 | +4.9% | +11.9191 to +14.7130 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 286.7 | +4.9% | +11.9191 to +14.7130 | yes: power given |
| response time (ms), mean | 353.6 | 720.2 | +103.6% | +319.5254 to +413.5143 | yes: LOSS |
| response time (ms), 95th percentile | 1132 | 1482 | +31.0% | +137.2377 to +563.9093 | yes: LOSS |
| response time (ms), 99th percentile | 1644 | 1983 | +20.6% | +14.7557 to +662.3431 | yes: LOSS |
| time over the response line (% of samples) | 22.15 | 65.35 | +195.0% | +38.2983 to +48.0966 | yes: LOSS |
| failed requests (%) | 0 | 0.01149 | +0.011 (native is 0) | −0.0145 to +0.0375 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 25 | +110.1% | +10.8519 to +15.3481 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 | +17.200 (native is 0) | +15.0199 to +19.3801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 2.455 | −76.8% | −9.6338 to −6.6429 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06192 | 0.09799 | +58.3% | +0.0319 to +0.0403 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 2.352 | +58.3% | +0.7650 to +0.9667 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00986 | +0.010 (native is 0) | +0.0093 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.486 | 2.362 | +58.9% | +0.7754 to +0.9760 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.3 | 290.9 | −33.9% | −174.1643 to −124.7295 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.048 | 2.854 | +39.4% | +0.6704 to +0.9421 | yes: power given |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 42.32 | 77.19 | +82.4% | +33.1924 to +36.5548 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.6 | 1510 | +96.7% | +727.3683 to +757.4317 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 842.1 | +1188736.8% | +730.4453 to +953.5985 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1391 | +231766.7% | +1324.9109 to +1456.2891 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 75.74 | 1064 | +1304.8% | +942.7310 to +1033.8190 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 18.5 | +18.500 (native is 0) | +15.9936 to +21.0064 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*