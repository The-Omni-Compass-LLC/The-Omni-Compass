# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.428 | 5.373 |
| node-hours | 2.515 | 2.513 | 2.274 | 2.252 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.4 | 272.1 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.4 | 254.2 | 252.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 321.2 | 373.7 | 285 | 339.8 |
| response time (ms), 95th percentile | 1035 | 1566 | 1083 | 1591 |
| response time (ms), 99th percentile | 1506 | 2532 | 1588 | 2490 |
| time over the response line (% of samples) | 17.27 | 14.23 | 17.14 | 13.95 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.6 | 9.3 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 31.8 | 46.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.533 | 16.54 | 10.42 | 16.32 |
| utilisation (used / allocatable) | 0.05941 | 0.06026 | 0.06643 | 0.06725 |
| CPU used (cores), mean | 1.426 | 1.446 | 1.436 | 1.435 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01583 | 0.01887 |
| CPU used with Omni's own (cores), mean | 1.426 | 1.446 | 1.452 | 1.454 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 455.6 | 424.7 | 421.5 |
| HPA replicas, mean | 2.056 | 2.055 | 2.051 | 2.23 |
| pods started | 0 | 0.1 | 0.3 | 0.5 |
| pod start wait, total (s) | 0 | 0.2 | 0.7 | 0.9 |
| pod start wait, mean (s) | 0 | 0.2 | 0.4 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.71 | 43.53 | 41.66 | 44.22 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 765.5 | 798.6 | 767.6 | 800.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.945 | 4.872 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.9042 | 0.0625 | 0.8875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.8 | 0.6 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 73.28 | 109.4 | 75.35 | 111.1 |
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
| worker nodes in service, mean | 6 | 5.373 | −10.5% | −1.2414 to −0.0128 | yes: GAIN |
| node-hours | 2.513 | 2.252 | −10.4% | −0.5147 to −0.0074 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 | +0.0% | −0.4701 to +0.6012 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 252.7 | −7.2% | −38.6502 to −0.6478 | yes: GAIN |
| response time (ms), mean | 373.7 | 339.8 | −9.1% | −57.1802 to −10.6070 | yes: GAIN |
| response time (ms), 95th percentile | 1566 | 1591 | +1.5% | −170.4297 to +218.6447 | no |
| response time (ms), 99th percentile | 2532 | 2490 | −1.6% | −237.6240 to +155.0114 | no |
| time over the response line (% of samples) | 14.23 | 13.95 | −2.0% | −1.0944 to +0.5382 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 | −4.2% | −1.6251 to +0.8251 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.5 | +46.500 (native is 0) | +29.0038 to +63.9962 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.54 | 16.32 | −1.3% | −1.9358 to +1.5091 | no |
| utilisation (used / allocatable) | 0.06026 | 0.06725 | +11.6% | −0.0001 to +0.0141 | no |
| CPU used (cores), mean | 1.446 | 1.435 | −0.7% | −0.0404 to +0.0189 | no |
| Omni's own CPU (cores), mean | 0 | 0.01887 | +0.019 (native is 0) | +0.0170 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.454 | +0.6% | −0.0215 to +0.0377 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.6 | 421.5 | −7.5% | −66.9421 to −1.2261 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.23 | +8.5% | +0.0415 to +0.3085 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.3690 to +1.7690 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | −0.3690 to +1.7690 | no |
| host CPU busy, the real machine under kind (%) | 43.53 | 44.22 | +1.6% | +0.1729 to +1.2074 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 798.6 | 800.7 | +0.3% | −3.4964 to +7.6964 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.872 | −18.8% | −2.1684 to −0.0869 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9042 | 0.8875 | −1.8% | −0.0814 to +0.0480 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 1.6 | −11.1% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 109.4 | 111.1 | +1.5% | −3.1779 to +6.5029 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.513 | −0.1% | −0.0108 to +0.0065 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.4 | +0.1% | −0.8180 to +1.1984 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.4 | +0.1% | −0.8180 to +1.1984 | no |
| response time (ms), mean | 321.2 | 373.7 | +16.3% | +11.1831 to +93.6438 | yes: LOSS |
| response time (ms), 95th percentile | 1035 | 1566 | +51.3% | +149.5690 to +913.1800 | yes: LOSS |
| response time (ms), 99th percentile | 1506 | 2532 | +68.1% | +379.0548 to +1672.0916 | yes: LOSS |
| time over the response line (% of samples) | 17.27 | 14.23 | −17.6% | −5.3431 to −0.7305 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.6 | +4.3% | −0.6769 to +1.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.533 | 16.54 | +73.5% | +4.9865 to +9.0201 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05941 | 0.06026 | +1.4% | −0.0003 to +0.0020 | no |
| CPU used (cores), mean | 1.426 | 1.446 | +1.4% | −0.0079 to +0.0488 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.426 | 1.446 | +1.4% | −0.0079 to +0.0488 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 455.6 | −1.4% | −15.3017 to +2.5168 | no |
| HPA replicas, mean | 2.056 | 2.055 | −0.1% | −0.2100 to +0.2064 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.71 | 43.53 | +6.9% | +2.2533 to +3.3834 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.5 | 798.6 | +4.3% | +14.9430 to +51.2570 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.9042 | +1450.0% | +0.7474 to +0.9442 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.8 | +350.0% | +1.0306 to +1.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 73.28 | 109.4 | +49.3% | +16.4384 to +55.7866 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.428 | −9.5% | −1.1716 to +0.0285 | no |
| node-hours | 2.515 | 2.274 | −9.6% | −0.4889 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.1 | −0.0% | −1.1009 to +0.9249 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 254.2 | −6.6% | −36.6315 to +0.5847 | no |
| response time (ms), mean | 321.2 | 285 | −11.3% | −50.9823 to −21.5207 | yes: GAIN |
| response time (ms), 95th percentile | 1035 | 1083 | +4.6% | −37.6927 to +133.1087 | no |
| response time (ms), 99th percentile | 1506 | 1588 | +5.5% | −10.4889 to +175.4421 | no |
| time over the response line (% of samples) | 17.27 | 17.14 | −0.7% | −1.1808 to +0.9241 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.3 | +1.1% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.8 | +31.800 (native is 0) | +15.5766 to +48.0234 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.533 | 10.42 | +9.2% | −0.5092 to +2.2725 | no |
| utilisation (used / allocatable) | 0.05941 | 0.06643 | +11.8% | +0.0005 to +0.0135 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.426 | 1.436 | +0.7% | −0.0146 to +0.0352 | no |
| Omni's own CPU (cores), mean | 0 | 0.01583 | +0.016 (native is 0) | +0.0150 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.426 | 1.452 | +1.8% | +0.0012 to +0.0511 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 424.7 | −8.1% | −69.8630 to −4.8364 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.056 | 2.051 | −0.3% | −0.2104 to +0.1995 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.6509 to +2.0509 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 40.71 | 41.66 | +2.3% | +0.7144 to +1.1690 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.5 | 767.6 | +0.3% | −0.4558 to +4.6558 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.945 | −17.6% | −2.1441 to +0.0350 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.0625 | +7.1% | −0.0342 to +0.0425 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.28 | 75.35 | +2.8% | −0.1773 to +4.3273 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.428 | −9.5% | −1.1716 to +0.0285 | no |
| node-hours | 2.513 | 2.274 | −9.5% | −0.4873 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.1 | −0.1% | −1.4757 to +0.9193 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 254.2 | −6.7% | −37.0784 to +0.6512 | no |
| response time (ms), mean | 373.7 | 285 | −23.7% | −127.5575 to −49.7723 | yes: GAIN |
| response time (ms), 95th percentile | 1566 | 1083 | −30.9% | −828.0715 to −139.2615 | yes: GAIN |
| response time (ms), 99th percentile | 2532 | 1588 | −37.3% | −1546.4751 to −339.7181 | yes: GAIN |
| time over the response line (% of samples) | 14.23 | 17.14 | +20.4% | +0.8910 to +4.9259 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.3 | −3.1% | −1.5181 to +0.9181 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.8 | +31.800 (native is 0) | +15.5766 to +48.0234 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.54 | 10.42 | −37.0% | −7.9611 to −4.2823 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06026 | 0.06643 | +10.2% | −0.0001 to +0.0124 | no |
| CPU used (cores), mean | 1.446 | 1.436 | −0.7% | −0.0412 to +0.0209 | no |
| Omni's own CPU (cores), mean | 0 | 0.01583 | +0.016 (native is 0) | +0.0150 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.452 | +0.4% | −0.0252 to +0.0366 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.6 | 424.7 | −6.8% | −60.2640 to −1.6505 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.051 | −0.2% | −0.1328 to +0.1255 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | −0.4079 to +1.4079 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 43.53 | 41.66 | −4.3% | −2.3039 to −1.4494 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 798.6 | 767.6 | −3.9% | −47.3776 to −14.6224 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.945 | −17.6% | −2.1441 to +0.0350 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9042 | 0.0625 | −93.1% | −0.9245 to −0.7588 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 0.6 | −66.7% | −1.5016 to −0.8984 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 109.4 | 75.35 | −31.1% | −52.2975 to −15.7775 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.373 | −10.5% | −1.2414 to −0.0128 | yes: GAIN |
| node-hours | 2.515 | 2.252 | −10.5% | −0.5149 to −0.0114 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.4 | +0.1% | −0.9684 to +1.4800 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 252.7 | −7.1% | −38.0621 to −0.8555 | yes: GAIN |
| response time (ms), mean | 321.2 | 339.8 | +5.8% | −23.4318 to +60.4715 | no |
| response time (ms), 95th percentile | 1035 | 1591 | +53.7% | +175.3102 to +935.6538 | yes: LOSS |
| response time (ms), 99th percentile | 1506 | 2490 | +65.4% | +336.7132 to +1631.8206 | yes: LOSS |
| time over the response line (% of samples) | 17.27 | 13.95 | −19.2% | −5.4522 to −1.1776 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.2 | ±0.0% | −1.4306 to +1.4306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.5 | +46.500 (native is 0) | +29.0038 to +63.9962 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.533 | 16.32 | +71.2% | +3.8579 to +9.7221 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05941 | 0.06725 | +13.2% | +0.0005 to +0.0152 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.426 | 1.435 | +0.7% | −0.0186 to +0.0380 | no |
| Omni's own CPU (cores), mean | 0 | 0.01887 | +0.019 (native is 0) | +0.0170 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.426 | 1.454 | +2.0% | −0.0010 to +0.0581 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 421.5 | −8.8% | −76.8991 to −4.0541 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.056 | 2.23 | +8.4% | −0.0435 to +0.3898 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.71 | 44.22 | +8.6% | +2.9214 to +4.0957 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.5 | 800.7 | +4.6% | +15.6227 to +54.7773 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.872 | −18.8% | −2.1684 to −0.0869 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.8875 | +1421.4% | +0.7432 to +0.9151 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.6 | +300.0% | +0.7476 to +1.6524 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 73.28 | 111.1 | +51.5% | +16.8115 to +58.7385 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*