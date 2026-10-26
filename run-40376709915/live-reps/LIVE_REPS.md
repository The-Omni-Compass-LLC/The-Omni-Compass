# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.2 | 10.59 |
| node-hours | 5.018 | 5.032 | 4.266 | 4.431 |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 525.3 | 523.2 | 525.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 525.3 | 466.8 | 481.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 435.3 | 695.7 | 421.1 | 781.6 |
| response time (ms), 95th percentile | 1648 | 2834 | 1809 | 3133 |
| response time (ms), 99th percentile | 2359 | 3777 | 2624 | 4477 |
| time over the response line (% of samples) | 16.66 | 22.82 | 17.14 | 25.78 |
| failed requests (%) | 0 | 0.01481 | 0 | 0.07262 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 11.6 | 9.4 | 13.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 95.5 | 62.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.32 | 25.5 | 11.56 | 16.05 |
| utilisation (used / allocatable) | 0.03224 | 0.03363 | 0.03814 | 0.04007 |
| CPU used (cores), mean | 1.547 | 1.614 | 1.538 | 1.7 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01268 | 0.01267 |
| CPU used with Omni's own (cores), mean | 1.547 | 1.614 | 1.551 | 1.712 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 829.3 | 804.7 | 731.1 | 691.2 |
| HPA replicas, mean | 4.018 | 4.131 | 4.2 | 4.092 |
| pods started | 0 | 0.8 | 0.6 | 0.9 |
| pod start wait, total (s) | 0 | 2.3 | 0.9 | 1.9 |
| pod start wait, mean (s) | 0 | 1.35 | 0.8 | 1.2 |
| host CPU busy, the real machine under kind (%) | 46.67 | 53.63 | 48.59 | 56.44 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 815.1 | 918.9 | 825.7 | 951.4 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.018 | 9.576 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 4.029 | 0.07083 | 8.342 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 17.8 | 0.5 | 61.6 |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 206.4 | 134 | 245.3 |
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
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.8711 to +0.0580 | no |
| node-hours | 5.032 | 4.431 | −11.9% | −1.2159 to +0.0137 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 525.5 | +0.0% | −1.7478 to +2.1862 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 481.4 | −8.4% | −90.6192 to +2.8409 | no |
| response time (ms), mean | 695.7 | 781.6 | +12.3% | +27.4477 to +144.3800 | yes: LOSS |
| response time (ms), 95th percentile | 2834 | 3133 | +10.5% | +89.1672 to +508.6718 | yes: LOSS |
| response time (ms), 99th percentile | 3777 | 4477 | +18.5% | +410.6906 to +988.4038 | yes: LOSS |
| time over the response line (% of samples) | 22.82 | 25.78 | +12.9% | −0.0790 to +5.9877 | no |
| failed requests (%) | 0.01481 | 0.07262 | +390.2% | −0.0090 to +0.1246 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 13.2 | +13.8% | +0.4222 to +2.7778 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.9 | +62.900 (native is 0) | +30.6936 to +95.1064 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.5 | 16.05 | −37.0% | −24.9848 to +6.0882 | no |
| utilisation (used / allocatable) | 0.03363 | 0.04007 | +19.2% | +0.0023 to +0.0106 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.614 | 1.7 | +5.3% | −0.0092 to +0.1802 | no |
| Omni's own CPU (cores), mean | 0 | 0.01267 | +0.013 (native is 0) | +0.0118 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.614 | 1.712 | +6.1% | +0.0039 to +0.1925 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.7 | 691.2 | −14.1% | −186.2193 to −40.7346 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.131 | 4.092 | −0.9% | −0.1990 to +0.1228 | no |
| pods started | 0.8 | 0.9 | +12.5% | −0.8802 to +1.0802 | no |
| pod start wait, total (s) | 2.3 | 1.9 | −17.4% | −3.3241 to +2.5241 | no |
| pod start wait, mean (s) | 1.35 | 1.2 | −11.1% | −1.3546 to +1.0546 | no |
| host CPU busy, the real machine under kind (%) | 53.63 | 56.44 | +5.2% | +2.0974 to +3.5098 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 918.9 | 951.4 | +3.5% | +14.4662 to +50.5338 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.576 | −20.2% | −4.8824 to +0.0336 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 4.029 | 8.342 | +107.0% | −1.4463 to +10.0713 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 17.8 | 61.6 | +246.1% | −8.4112 to +96.0112 | no |
| queue: job turnaround, submitted to done, mean (s) | 206.4 | 245.3 | +18.8% | +17.3409 to +60.3924 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.018 | 5.032 | +0.3% | +0.0011 to +0.0262 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 525.3 | +0.4% | +0.0478 to +4.4767 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 525.3 | +0.4% | +0.0478 to +4.4767 | yes: power given |
| response time (ms), mean | 435.3 | 695.7 | +59.8% | +85.3851 to +435.3801 | yes: LOSS |
| response time (ms), 95th percentile | 1648 | 2834 | +71.9% | +390.1095 to +1980.7415 | yes: LOSS |
| response time (ms), 99th percentile | 2359 | 3777 | +60.2% | +490.7525 to +2346.8681 | yes: LOSS |
| time over the response line (% of samples) | 16.66 | 22.82 | +37.0% | +2.8743 to +9.4530 | yes: LOSS |
| failed requests (%) | 0 | 0.01481 | +0.015 (native is 0) | −0.0187 to +0.0483 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 11.6 | +41.5% | +1.0109 to +5.7891 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.32 | 25.5 | +125.3% | −3.0610 to +31.4243 | no |
| utilisation (used / allocatable) | 0.03224 | 0.03363 | +4.3% | −0.0006 to +0.0033 | no |
| CPU used (cores), mean | 1.547 | 1.614 | +4.3% | −0.0270 to +0.1601 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.547 | 1.614 | +4.3% | −0.0270 to +0.1601 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 829.3 | 804.7 | −3.0% | −58.2622 to +9.0483 | no |
| HPA replicas, mean | 4.018 | 4.131 | +2.8% | −0.1441 to +0.3697 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.0612 to +1.5388 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | −0.0129 to +4.6129 | no |
| pod start wait, mean (s) | 0 | 1.35 | +1.350 (native is 0) | +0.2830 to +2.4170 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.67 | 53.63 | +14.9% | +4.5449 to +9.3910 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 815.1 | 918.9 | +12.7% | +32.5354 to +175.0646 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 4.029 | +8690.9% | −0.7839 to +8.7505 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 17.8 | +5833.3% | −7.8309 to +42.8309 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 206.4 | +65.0% | +27.2482 to +135.4684 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.2 | −15.0% | −3.4407 to −0.1568 | yes: GAIN |
| node-hours | 5.018 | 4.266 | −15.0% | −1.4408 to −0.0638 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 523.2 | +0.0% | −1.4452 to +1.8220 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 466.8 | −10.8% | −108.2244 to −4.2988 | yes: GAIN |
| response time (ms), mean | 435.3 | 421.1 | −3.3% | −28.2403 to −0.1766 | yes: GAIN |
| response time (ms), 95th percentile | 1648 | 1809 | +9.7% | +72.4205 to +247.6345 | yes: LOSS |
| response time (ms), 99th percentile | 2359 | 2624 | +11.2% | +19.4903 to +511.0857 | yes: LOSS |
| time over the response line (% of samples) | 16.66 | 17.14 | +2.9% | −0.7170 to +1.6732 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 9.4 | +14.6% | −0.4101 to +2.8101 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.5 | +95.500 (native is 0) | +44.3321 to +146.6679 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.32 | 11.56 | +2.1% | −2.4610 to +2.9344 | no |
| utilisation (used / allocatable) | 0.03224 | 0.03814 | +18.3% | +0.0007 to +0.0111 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.538 | −0.6% | −0.0509 to +0.0318 | no |
| Omni's own CPU (cores), mean | 0 | 0.01268 | +0.013 (native is 0) | +0.0119 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.551 | +0.2% | −0.0381 to +0.0444 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 829.3 | 731.1 | −11.8% | −181.2191 to −15.2805 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.018 | 4.2 | +4.5% | −0.0949 to +0.4600 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1128 to +1.6872 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.0612 to +1.5388 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.67 | 48.59 | +4.1% | +0.9884 to +2.8668 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 815.1 | 825.7 | +1.3% | +2.5128 to +18.6872 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.018 | −24.9% | −5.6132 to −0.3516 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.07083 | +54.5% | −0.0127 to +0.0627 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 134 | +7.1% | +4.7830 to +13.1003 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.2 | −15.0% | −3.4407 to −0.1568 | yes: GAIN |
| node-hours | 5.032 | 4.266 | −15.2% | −1.4524 to −0.0796 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 523.2 | −0.4% | −4.2226 to +0.0748 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 466.8 | −11.1% | −109.5924 to −7.4553 | yes: GAIN |
| response time (ms), mean | 695.7 | 421.1 | −39.5% | −454.1824 to −94.9996 | yes: GAIN |
| response time (ms), 95th percentile | 2834 | 1809 | −36.2% | −1777.6522 to −273.1438 | yes: GAIN |
| response time (ms), 99th percentile | 3777 | 2624 | −30.5% | −2046.7959 to −260.2487 | yes: GAIN |
| time over the response line (% of samples) | 22.82 | 17.14 | −24.9% | −8.9236 to −2.4476 | yes: GAIN |
| failed requests (%) | 0.01481 | 0 | −100.0% | −0.0483 to +0.0187 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 9.4 | −19.0% | −4.4570 to +0.0570 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.5 | +95.500 (native is 0) | +44.3321 to +146.6679 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.5 | 11.56 | −54.7% | −32.0965 to +4.2065 | no |
| utilisation (used / allocatable) | 0.03363 | 0.03814 | +13.4% | −0.0018 to +0.0108 | no |
| CPU used (cores), mean | 1.614 | 1.538 | −4.7% | −0.1705 to +0.0183 | no |
| Omni's own CPU (cores), mean | 0 | 0.01268 | +0.013 (native is 0) | +0.0119 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.614 | 1.551 | −3.9% | −0.1579 to +0.0310 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 804.7 | 731.1 | −9.2% | −175.0024 to +27.7167 | no |
| HPA replicas, mean | 4.131 | 4.2 | +1.7% | −0.2543 to +0.3938 | no |
| pods started | 0.8 | 0.6 | −25.0% | −1.0793 to +0.6793 | no |
| pod start wait, total (s) | 2.3 | 0.9 | −60.9% | −3.9945 to +1.1945 | no |
| pod start wait, mean (s) | 1.35 | 0.8 | −40.7% | −1.9449 to +0.8449 | no |
| host CPU busy, the real machine under kind (%) | 53.63 | 48.59 | −9.4% | −7.6626 to −2.4181 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 918.9 | 825.7 | −10.1% | −158.0508 to −28.3492 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.018 | −24.9% | −5.6132 to −0.3516 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.029 | 0.07083 | −98.2% | −8.7250 to +0.8084 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 17.8 | 0.5 | −97.2% | −42.7111 to +8.1111 | no |
| queue: job turnaround, submitted to done, mean (s) | 206.4 | 134 | −35.1% | −123.2684 to −21.5649 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.8711 to +0.0580 | no |
| node-hours | 5.018 | 4.431 | −11.7% | −1.2042 to +0.0293 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523 | 525.5 | +0.5% | +0.3869 to +4.5760 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523 | 481.4 | −8.0% | −89.1768 to +5.9231 | no |
| response time (ms), mean | 435.3 | 781.6 | +79.6% | +122.2186 to +570.3742 | yes: LOSS |
| response time (ms), 95th percentile | 1648 | 3133 | +90.0% | +642.2133 to +2326.4767 | yes: LOSS |
| response time (ms), 99th percentile | 2359 | 4477 | +89.8% | +931.1915 to +3305.5235 | yes: LOSS |
| time over the response line (% of samples) | 16.66 | 25.78 | +54.7% | +4.1214 to +14.1147 | yes: LOSS |
| failed requests (%) | 0 | 0.07262 | +0.073 (native is 0) | +0.0031 to +0.1421 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 13.2 | +61.0% | +2.6638 to +7.3362 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.9 | +62.900 (native is 0) | +30.6936 to +95.1064 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.32 | 16.05 | +41.8% | +0.6915 to +8.7752 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03224 | 0.04007 | +24.3% | +0.0046 to +0.0110 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.7 | +9.8% | +0.0594 to +0.2448 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01267 | +0.013 (native is 0) | +0.0118 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.712 | +10.6% | +0.0721 to +0.2574 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 829.3 | 691.2 | −16.7% | −194.2348 to −81.9330 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.018 | 4.092 | +1.9% | −0.1066 to +0.2560 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | +0.2737 to +1.5263 | yes: power given |
| pod start wait, total (s) | 0 | 1.9 | +1.900 (native is 0) | +0.4129 to +3.3871 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.4056 to +1.9944 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.67 | 56.44 | +20.9% | +7.2179 to +12.3253 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 815.1 | 951.4 | +16.7% | +53.9391 to +218.6609 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.576 | −20.2% | −4.8824 to +0.0336 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 8.342 | +18100.0% | −0.2299 to +16.8215 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 61.6 | +20433.3% | −2.3691 to +124.9691 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.1 | 245.3 | +96.1% | +49.1550 to +191.2950 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*