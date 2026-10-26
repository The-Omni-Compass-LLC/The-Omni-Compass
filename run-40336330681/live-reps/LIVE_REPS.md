# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.115 | 5.214 |
| node-hours | 2.508 | 2.514 | 2.141 | 2.183 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.8 | 271.8 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.8 | 244 | 246.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 307.9 | 279 | 282.9 | 255.3 |
| response time (ms), 95th percentile | 1014 | 1016 | 1078 | 1120 |
| response time (ms), 99th percentile | 1431 | 1682 | 1564 | 1709 |
| time over the response line (% of samples) | 17.87 | 12.06 | 17.61 | 12.6 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 8.9 | 9.5 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 28.8 | 31.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.04 | 11.94 | 10.33 | 11.11 |
| utilisation (used / allocatable) | 0.0589 | 0.05829 | 0.06935 | 0.06835 |
| CPU used (cores), mean | 1.414 | 1.399 | 1.405 | 1.4 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01647 | 0.01592 |
| CPU used with Omni's own (cores), mean | 1.414 | 1.399 | 1.421 | 1.416 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 473.5 | 415.9 | 421.1 |
| HPA replicas, mean | 2.119 | 2.06 | 1.925 | 2.145 |
| pods started | 0 | 0 | 0 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 0 | 0.9 |
| pod start wait, mean (s) | 0 | 0 | 0 | 0.7 |
| host CPU busy, the real machine under kind (%) | 40.37 | 40.31 | 41.38 | 40.89 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 763.4 | 761.3 | 765.9 | 761 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.467 | 4.723 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.06667 | 0.04583 | 0.04583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | 0.5 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 71.26 | 70.06 | 73 | 70.66 |
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
| worker nodes in service, mean | 6 | 5.214 | −13.1% | −1.6141 to +0.0425 | no |
| node-hours | 2.514 | 2.183 | −13.2% | −0.6747 to +0.0115 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.6 | −0.1% | −0.8927 to +0.6200 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 246.9 | −9.1% | −50.3740 to +0.7096 | no |
| response time (ms), mean | 279 | 255.3 | −8.5% | −31.4139 to −16.0686 | yes: GAIN |
| response time (ms), 95th percentile | 1016 | 1120 | +10.2% | +18.1529 to +189.3001 | yes: LOSS |
| response time (ms), 99th percentile | 1682 | 1709 | +1.6% | −71.9391 to +125.8631 | no |
| time over the response line (% of samples) | 12.06 | 12.6 | +4.5% | −0.4932 to +1.5763 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.2 | +3.4% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.6 | +31.600 (native is 0) | +21.6358 to +41.5642 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.94 | 11.11 | −7.0% | −3.2103 to +1.5469 | no |
| utilisation (used / allocatable) | 0.05829 | 0.06835 | +17.3% | −0.0004 to +0.0205 | no |
| CPU used (cores), mean | 1.399 | 1.4 | +0.1% | −0.0168 to +0.0187 | no |
| Omni's own CPU (cores), mean | 0 | 0.01592 | +0.016 (native is 0) | +0.0140 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.416 | +1.2% | −0.0012 to +0.0349 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.5 | 421.1 | −11.1% | −108.0541 to +3.2946 | no |
| HPA replicas, mean | 2.06 | 2.145 | +4.1% | −0.0904 to +0.2587 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.0204 to +1.8204 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.31 | 40.89 | +1.4% | +0.1239 to +1.0193 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 761.3 | 761 | −0.0% | −2.5633 to +1.9633 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.723 | −21.3% | −2.5825 to +0.0282 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.04583 | −31.2% | −0.0530 to +0.0114 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 70.06 | 70.66 | +0.9% | −1.7142 to +2.9142 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.508 | 2.514 | +0.3% | −0.0009 to +0.0135 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.8 | +0.1% | −0.3253 to +1.0849 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.8 | +0.1% | −0.3253 to +1.0849 | no |
| response time (ms), mean | 307.9 | 279 | −9.4% | −57.7883 to +0.0661 | no |
| response time (ms), 95th percentile | 1014 | 1016 | +0.2% | −115.2620 to +120.3260 | no |
| response time (ms), 99th percentile | 1431 | 1682 | +17.5% | +35.8220 to +466.0142 | yes: LOSS |
| time over the response line (% of samples) | 17.87 | 12.06 | −32.5% | −10.2671 to −1.3464 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 8.9 | −3.3% | −0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.04 | 11.95 | +8.2% | −0.3381 to +2.1547 | no |
| utilisation (used / allocatable) | 0.0589 | 0.05829 | −1.0% | −0.0016 to +0.0004 | no |
| CPU used (cores), mean | 1.414 | 1.399 | −1.0% | −0.0389 to +0.0095 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.414 | 1.399 | −1.0% | −0.0389 to +0.0095 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 473.5 | +1.0% | −2.5029 to +11.4324 | no |
| HPA replicas, mean | 2.119 | 2.06 | −2.8% | −0.2120 to +0.0953 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.37 | 40.31 | −0.1% | −0.5471 to +0.4403 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.4 | 761.3 | −0.3% | −8.3673 to +4.1673 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.06667 | +60.0% | −0.0220 to +0.0720 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 71.26 | 70.06 | −1.7% | −6.9020 to +4.4937 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.115 | −14.8% | −1.6142 to −0.1568 | yes: GAIN |
| node-hours | 2.508 | 2.141 | −14.6% | −0.6709 to −0.0625 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.8 | +0.1% | −0.9886 to +1.7145 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 244 | −10.1% | −50.2461 to −4.6280 | yes: GAIN |
| response time (ms), mean | 307.9 | 282.9 | −8.1% | −39.1233 to −10.8821 | yes: GAIN |
| response time (ms), 95th percentile | 1014 | 1078 | +6.3% | −15.1616 to +142.7586 | no |
| response time (ms), 99th percentile | 1431 | 1564 | +9.3% | +7.5632 to +259.9782 | yes: LOSS |
| time over the response line (% of samples) | 17.87 | 17.61 | −1.4% | −1.1258 to +0.6173 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.5 | +3.3% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 | +28.800 (native is 0) | +13.8609 to +43.7391 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.04 | 10.33 | −6.4% | −1.6832 to +0.2632 | no |
| utilisation (used / allocatable) | 0.0589 | 0.06935 | +17.8% | +0.0015 to +0.0194 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.405 | −0.6% | −0.0294 to +0.0112 | no |
| Omni's own CPU (cores), mean | 0 | 0.01647 | +0.016 (native is 0) | +0.0148 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.421 | +0.5% | −0.0126 to +0.0274 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 415.9 | −11.3% | −101.9727 to −4.2759 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.119 | 1.925 | −9.1% | −0.3293 to −0.0575 | yes: GAIN |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.37 | 41.38 | +2.5% | +0.6422 to +1.3760 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.4 | 765.9 | +0.3% | −2.7699 to +7.7699 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.467 | −25.5% | −2.6710 to −0.3950 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.04583 | +10.0% | −0.0255 to +0.0338 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 71.26 | 73 | +2.4% | −2.0329 to +5.4995 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.115 | −14.8% | −1.6142 to −0.1568 | yes: GAIN |
| node-hours | 2.514 | 2.141 | −14.8% | −0.6760 to −0.0700 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.8 | −0.0% | −1.1435 to +1.1098 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 244 | −10.2% | −50.5627 to −5.0709 | yes: GAIN |
| response time (ms), mean | 279 | 282.9 | +1.4% | −14.7068 to +22.4236 | no |
| response time (ms), 95th percentile | 1016 | 1078 | +6.0% | +0.7432 to +121.7898 | yes: LOSS |
| response time (ms), 99th percentile | 1682 | 1564 | −7.0% | −253.7494 to +19.4546 | no |
| time over the response line (% of samples) | 12.06 | 17.61 | +46.0% | +1.7952 to +9.3098 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.5 | +6.7% | −0.3656 to +1.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 | +28.800 (native is 0) | +13.8609 to +43.7391 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.94 | 10.33 | −13.5% | −2.9779 to −0.2588 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05829 | 0.06935 | +19.0% | +0.0022 to +0.0200 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.399 | 1.405 | +0.4% | −0.0279 to +0.0392 | no |
| Omni's own CPU (cores), mean | 0 | 0.01647 | +0.016 (native is 0) | +0.0148 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.421 | +1.6% | −0.0109 to +0.0552 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.5 | 415.9 | −12.2% | −107.6968 to −7.4814 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.06 | 1.925 | −6.6% | −0.2308 to −0.0392 | yes: GAIN |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.31 | 41.38 | +2.6% | +0.6455 to +1.4795 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 761.3 | 765.9 | +0.6% | −0.2888 to +9.4888 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.467 | −25.5% | −2.6710 to −0.3950 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.04583 | −31.3% | −0.0757 to +0.0340 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 70.06 | 73 | +4.2% | −1.6380 to +7.5130 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.214 | −13.1% | −1.6141 to +0.0425 | no |
| node-hours | 2.508 | 2.183 | −13.0% | −0.6690 to +0.0185 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.6 | +0.1% | −0.5025 to +0.9893 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 246.9 | −9.0% | −50.0632 to +1.1584 | no |
| response time (ms), mean | 307.9 | 255.3 | −17.1% | −78.7039 to −26.5009 | yes: GAIN |
| response time (ms), 95th percentile | 1014 | 1120 | +10.5% | −10.3852 to +222.9022 | no |
| response time (ms), 99th percentile | 1431 | 1709 | +19.4% | +42.8121 to +512.9481 | yes: LOSS |
| time over the response line (% of samples) | 17.87 | 12.6 | −29.5% | −8.9915 to −1.5390 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.2 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.6 | +31.600 (native is 0) | +21.6358 to +41.5642 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.04 | 11.11 | +0.7% | −1.8633 to +2.0166 | no |
| utilisation (used / allocatable) | 0.0589 | 0.06835 | +16.1% | −0.0010 to +0.0199 | no |
| CPU used (cores), mean | 1.414 | 1.4 | −1.0% | −0.0430 to +0.0155 | no |
| Omni's own CPU (cores), mean | 0 | 0.01592 | +0.016 (native is 0) | +0.0140 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.416 | +0.2% | −0.0272 to +0.0315 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 421.1 | −10.2% | −102.2707 to +6.4407 | no |
| HPA replicas, mean | 2.119 | 2.145 | +1.2% | −0.2012 to +0.2528 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.0204 to +1.8204 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.37 | 40.89 | +1.3% | −0.0636 to +1.0999 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.4 | 761 | −0.3% | −8.6103 to +3.8103 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.723 | −21.3% | −2.5825 to +0.0282 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.04583 | +10.0% | −0.0315 to +0.0398 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 71.26 | 70.66 | −0.8% | −6.8301 to +5.6218 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*