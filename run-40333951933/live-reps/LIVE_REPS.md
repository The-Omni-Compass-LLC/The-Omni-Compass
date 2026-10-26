# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.124 | 5.009 |
| node-hours | 2.52 | 2.511 | 2.144 | 2.102 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.6 | 271.4 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.6 | 243.9 | 240.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 316.1 | 232.9 | 289.5 | 203.6 |
| response time (ms), 95th percentile | 1042 | 605.5 | 1096 | 602.3 |
| response time (ms), 99th percentile | 1553 | 1022 | 1608 | 1062 |
| time over the response line (% of samples) | 18.91 | 9.406 | 19.04 | 10.02 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.1 | 9.4 | 8.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 30.2 | 32.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 14.18 | 11.36 | 15.4 |
| utilisation (used / allocatable) | 0.05808 | 0.05901 | 0.0686 | 0.06914 |
| CPU used (cores), mean | 1.394 | 1.416 | 1.39 | 1.38 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01547 | 0.01759 |
| CPU used with Omni's own (cores), mean | 1.394 | 1.416 | 1.406 | 1.397 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482 | 471.1 | 424 | 421.1 |
| HPA replicas, mean | 1.989 | 2.002 | 1.913 | 2.084 |
| pods started | 0 | 0.1 | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.1 | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.1 | 0 | 0.25 |
| host CPU busy, the real machine under kind (%) | 39.74 | 40.9 | 40.87 | 41.49 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 765.2 | 778.3 | 768.3 | 782.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.56 | 4.332 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.7458 | 0.04167 | 0.6958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 | 0.3 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 72.07 | 93.36 | 75.18 | 98.55 |
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
| worker nodes in service, mean | 6 | 5.009 | −16.5% | −1.7984 to −0.1843 | yes: GAIN |
| node-hours | 2.511 | 2.102 | −16.3% | −0.7435 to −0.0743 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272.1 | +0.2% | −0.4251 to +1.4249 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 240.9 | −11.3% | −56.2036 to −5.2800 | yes: GAIN |
| response time (ms), mean | 232.9 | 203.6 | −12.6% | −36.2801 to −22.3279 | yes: GAIN |
| response time (ms), 95th percentile | 605.5 | 602.3 | −0.5% | −51.7402 to +45.2642 | no |
| response time (ms), 99th percentile | 1022 | 1062 | +3.9% | −130.7109 to +211.0773 | no |
| time over the response line (% of samples) | 9.406 | 10.02 | +6.6% | −0.6919 to +1.9284 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.9 | −2.2% | −0.8573 to +0.4573 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.100 (native is 0) | +23.0053 to +41.1947 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.18 | 15.4 | +8.6% | −0.0090 to +2.4390 | no |
| utilisation (used / allocatable) | 0.05901 | 0.06914 | +17.2% | +0.0025 to +0.0178 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.416 | 1.38 | −2.6% | −0.0927 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0 | 0.01759 | +0.018 (native is 0) | +0.0149 to +0.0203 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.416 | 1.397 | −1.3% | −0.0769 to +0.0392 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.1 | 421.1 | −10.6% | −93.3160 to −6.7431 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.084 | +4.1% | −0.0216 to +0.1863 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.7778 to +1.5778 | no |
| pod start wait, mean (s) | 0.1 | 0.25 | +150.0% | −0.4820 to +0.7820 | no |
| host CPU busy, the real machine under kind (%) | 40.9 | 41.49 | +1.4% | +0.0118 to +1.1624 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.3 | 782.9 | +0.6% | +0.2660 to +8.9340 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.332 | −27.8% | −2.8845 to −0.4516 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7458 | 0.6958 | −6.7% | −0.1185 to +0.0185 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.1 | −21.4% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.36 | 98.55 | +5.6% | −2.4922 to +12.8672 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.52 | 2.511 | −0.3% | −0.0187 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.6 | −0.2% | −1.8115 to +0.4636 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.6 | −0.2% | −1.8115 to +0.4636 | no |
| response time (ms), mean | 316.1 | 232.9 | −26.3% | −124.1708 to −42.3649 | yes: GAIN |
| response time (ms), 95th percentile | 1042 | 605.5 | −41.9% | −649.1681 to −223.4329 | yes: GAIN |
| response time (ms), 99th percentile | 1553 | 1022 | −34.2% | −814.3803 to −249.1675 | yes: GAIN |
| time over the response line (% of samples) | 18.91 | 9.406 | −50.2% | −14.5857 to −4.4133 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.1 | ±0.0% | −0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 14.18 | +37.0% | +2.5725 to +5.0942 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05808 | 0.05901 | +1.6% | −0.0003 to +0.0021 | no |
| CPU used (cores), mean | 1.394 | 1.416 | +1.6% | −0.0071 to +0.0515 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.394 | 1.416 | +1.6% | −0.0071 to +0.0515 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482 | 471.1 | −2.3% | −28.9592 to +7.0275 | no |
| HPA replicas, mean | 1.989 | 2.002 | +0.6% | −0.0809 to +0.1061 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 39.74 | 40.9 | +2.9% | +0.8043 to +1.5182 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.2 | 778.3 | +1.7% | +3.9741 to +22.2259 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.7458 | +1093.3% | +0.6087 to +0.7579 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 | +250.0% | +0.5231 to +1.4769 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 72.07 | 93.36 | +29.5% | +9.8405 to +32.7345 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.124 | −14.6% | −1.7357 to −0.0156 | yes: GAIN |
| node-hours | 2.52 | 2.144 | −14.9% | −0.7364 to −0.0145 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.4 | −0.3% | −1.6677 to −0.1586 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 243.9 | −10.4% | −55.6201 to −1.2020 | yes: GAIN |
| response time (ms), mean | 316.1 | 289.5 | −8.4% | −40.9621 to −12.3599 | yes: GAIN |
| response time (ms), 95th percentile | 1042 | 1096 | +5.2% | −5.1370 to +113.1700 | no |
| response time (ms), 99th percentile | 1553 | 1608 | +3.5% | −83.3156 to +191.9664 | no |
| time over the response line (% of samples) | 18.91 | 19.04 | +0.7% | −0.8248 to +1.0844 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.4 | +3.3% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.2 | +30.200 (native is 0) | +12.2751 to +48.1249 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 11.36 | +9.8% | −1.0416 to +3.0649 | no |
| utilisation (used / allocatable) | 0.05808 | 0.0686 | +18.1% | +0.0010 to +0.0201 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.39 | −0.3% | −0.0356 to +0.0279 | no |
| Omni's own CPU (cores), mean | 0 | 0.01547 | +0.015 (native is 0) | +0.0141 to +0.0168 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.406 | +0.8% | −0.0207 to +0.0438 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482 | 424 | −12.0% | −113.9178 to −2.1477 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.989 | 1.913 | −3.8% | −0.1747 to +0.0221 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 39.74 | 40.87 | +2.8% | +0.8207 to +1.4367 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.2 | 768.3 | +0.4% | −1.7567 to +7.9567 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.56 | −24.0% | −2.8096 to −0.0695 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.04167 | −33.3% | −0.0419 to +0.0002 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.07 | 75.18 | +4.3% | −0.9717 to +7.1883 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.124 | −14.6% | −1.7357 to −0.0156 | yes: GAIN |
| node-hours | 2.511 | 2.144 | −14.6% | −0.7236 to −0.0107 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.4 | −0.1% | −1.5630 to +1.0846 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 243.9 | −10.2% | −54.6004 to −0.8738 | yes: GAIN |
| response time (ms), mean | 232.9 | 289.5 | +24.3% | +22.3906 to +90.8232 | yes: LOSS |
| response time (ms), 95th percentile | 605.5 | 1096 | +81.0% | +282.0684 to +698.5656 | yes: LOSS |
| response time (ms), 99th percentile | 1022 | 1608 | +57.4% | +292.0888 to +880.1098 | yes: LOSS |
| time over the response line (% of samples) | 9.406 | 19.04 | +102.4% | +4.8548 to +14.4038 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.4 | +3.3% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.2 | +30.200 (native is 0) | +12.2751 to +48.1249 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.18 | 11.36 | −19.9% | −4.6424 to −1.0009 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05901 | 0.0686 | +16.3% | +0.0002 to +0.0190 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.416 | 1.39 | −1.8% | −0.0658 to +0.0136 | no |
| Omni's own CPU (cores), mean | 0 | 0.01547 | +0.015 (native is 0) | +0.0141 to +0.0168 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.416 | 1.406 | −0.8% | −0.0511 to +0.0298 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.1 | 424 | −10.0% | −94.0412 to −0.0925 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 1.913 | −4.4% | −0.2150 to +0.0371 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 40.9 | 40.87 | −0.1% | −0.3165 to +0.2513 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.3 | 768.3 | −1.3% | −16.1348 to −3.8652 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.56 | −24.0% | −2.8096 to −0.0695 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7458 | 0.04167 | −94.4% | −0.7764 to −0.6319 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.3 | −78.6% | −1.5060 to −0.6940 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 93.36 | 75.18 | −19.5% | −27.5517 to −8.8066 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.009 | −16.5% | −1.7984 to −0.1843 | yes: GAIN |
| node-hours | 2.52 | 2.102 | −16.6% | −0.7557 to −0.0788 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −0.9296 to +0.5814 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 240.9 | −11.5% | −57.1668 to −5.6647 | yes: GAIN |
| response time (ms), mean | 316.1 | 203.6 | −35.6% | −152.6851 to −72.4586 | yes: GAIN |
| response time (ms), 95th percentile | 1042 | 602.3 | −42.2% | −633.6051 to −245.4719 | yes: GAIN |
| response time (ms), 99th percentile | 1553 | 1062 | −31.6% | −783.3014 to −199.8800 | yes: GAIN |
| time over the response line (% of samples) | 18.91 | 10.02 | −47.0% | −13.4480 to −4.3145 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.9 | −2.2% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.100 (native is 0) | +23.0053 to +41.1947 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.35 | 15.4 | +48.8% | +3.2493 to +6.8473 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05808 | 0.06914 | +19.0% | +0.0031 to +0.0190 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.38 | −1.0% | −0.0768 to +0.0483 | no |
| Omni's own CPU (cores), mean | 0 | 0.01759 | +0.018 (native is 0) | +0.0149 to +0.0203 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.397 | +0.2% | −0.0603 to +0.0670 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482 | 421.1 | −12.7% | −116.7873 to −5.2035 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.989 | 2.084 | +4.8% | +0.0223 to +0.1676 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.25 | +0.250 (native is 0) | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 39.74 | 41.49 | +4.4% | +0.9641 to +2.5326 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.2 | 782.9 | +2.3% | +6.7628 to +28.6372 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.332 | −27.8% | −2.8845 to −0.4516 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.6958 | +1013.3% | +0.5648 to +0.7019 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | +175.0% | +0.3545 to +1.0455 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 72.07 | 98.55 | +36.7% | +12.6971 to +40.2529 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*