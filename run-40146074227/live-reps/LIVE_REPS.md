# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.44 | 5.989 |
| node-hours | 2.511 | 2.516 | 2.279 | 2.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272.3 | 272 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 272.3 | 254.3 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 289.5 | 145.9 | 264.1 | 107.9 |
| response time (ms), 95th percentile | 908.8 | 248.2 | 969 | 238.1 |
| response time (ms), 99th percentile | 1299 | 366.1 | 1408 | 360.4 |
| time over the response line (% of samples) | 17.01 | 0.2311 | 17.83 | 0.253 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 0 | 11.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 29.1 | 12.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 1221 | 10.72 | 1228 |
| utilisation (used / allocatable) | 0.05901 | 0.05952 | 0.06549 | 0.05944 |
| CPU used (cores), mean | 1.416 | 1.429 | 1.415 | 1.424 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01683 | 0.01274 |
| CPU used with Omni's own (cores), mean | 1.416 | 1.429 | 1.432 | 1.437 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 455.3 | 429.6 | 455.6 |
| HPA replicas, mean | 1.949 | 1.998 | 2.4 | 2.006 |
| pods started | 0.1 | 0 | 0.4 | 0.1 |
| pod start wait, total (s) | 0.2 | 0 | 0.9 | 0.1 |
| pod start wait, mean (s) | 0.2 | 0 | 0.9 | 0.1 |
| host CPU busy, the real machine under kind (%) | 40.55 | 44.93 | 41.4 | 45.03 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 746.5 | 1482 | 750.1 | 1480 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.942 | 5.444 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 162.1 | 0.02917 | 160.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 751.4 | 0.1 | 739.1 |
| queue: job turnaround, submitted to done, mean (s) | 55.3 | 912.3 | 58.32 | 889.7 |
| queue: jobs unfinished at the window's end | 0 | 14.5 | 0 | 12.5 |

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
| worker nodes in service, mean | 6 | 5.989 | −0.2% | −0.0348 to +0.0135 | no |
| node-hours | 2.516 | 2.511 | −0.2% | −0.0241 to +0.0136 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −1.7964 to +1.2697 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.7 | −0.2% | −2.5614 to +1.3680 | no |
| response time (ms), mean | 145.9 | 107.9 | −26.0% | −42.6513 to −33.2569 | yes: GAIN |
| response time (ms), 95th percentile | 248.2 | 238.1 | −4.1% | −20.4537 to +0.3337 | no |
| response time (ms), 99th percentile | 366.1 | 360.4 | −1.5% | −36.9830 to +25.6682 | no |
| time over the response line (% of samples) | 0.2311 | 0.253 | +9.5% | −0.1647 to +0.2085 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.600 (native is 0) | +10.2834 to +14.9166 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1221 | 1228 | +0.6% | −72.0135 to +86.1135 | no |
| utilisation (used / allocatable) | 0.05952 | 0.05944 | −0.1% | −0.0019 to +0.0017 | no |
| CPU used (cores), mean | 1.429 | 1.424 | −0.3% | −0.0462 to +0.0375 | no |
| Omni's own CPU (cores), mean | 0 | 0.01274 | +0.013 (native is 0) | +0.0119 to +0.0136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.437 | +0.6% | −0.0336 to +0.0504 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 455.6 | +0.1% | −11.8507 to +12.5591 | no |
| HPA replicas, mean | 1.998 | 2.006 | +0.4% | −0.0927 to +0.1084 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 44.93 | 45.03 | +0.2% | −0.9759 to +1.1882 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1482 | 1480 | −0.2% | −12.8977 to +8.0977 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.444 | −9.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 162.1 | 160.7 | −0.8% | −54.4914 to +51.7998 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 751.4 | 739.1 | −1.6% | −227.3426 to +202.7426 | no |
| queue: job turnaround, submitted to done, mean (s) | 912.3 | 889.7 | −2.5% | −81.3680 to +36.0346 | no |
| queue: jobs unfinished at the window's end | 14.5 | 12.5 | −13.8% | −4.6976 to +0.6976 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.511 | 2.516 | +0.2% | +0.0002 to +0.0098 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272.3 | +0.3% | −0.5349 to +1.9128 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 272.3 | +0.3% | −0.5349 to +1.9128 | no |
| response time (ms), mean | 289.5 | 145.9 | −49.6% | −187.2977 to −99.9890 | yes: GAIN |
| response time (ms), 95th percentile | 908.8 | 248.2 | −72.7% | −861.4292 to −459.7668 | yes: GAIN |
| response time (ms), 99th percentile | 1299 | 366.1 | −71.8% | −1209.9236 to −656.9374 | yes: GAIN |
| time over the response line (% of samples) | 17.01 | 0.2311 | −98.6% | −22.8579 to −10.6985 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 0 | −100.0% | −14.1347 to −7.4653 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 1221 | +13303.5% | +1041.9206 to +1381.0927 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05901 | 0.05952 | +0.9% | −0.0032 to +0.0042 | no |
| CPU used (cores), mean | 1.416 | 1.429 | +0.9% | −0.0774 to +0.1018 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.416 | 1.429 | +0.9% | −0.0774 to +0.1018 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 455.3 | −1.7% | −39.6097 to +23.8201 | no |
| HPA replicas, mean | 1.949 | 1.998 | +2.5% | −0.1049 to +0.2031 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 40.55 | 44.93 | +10.8% | +2.7841 to +5.9615 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 746.5 | 1482 | +98.5% | +679.5862 to +791.6138 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 162.1 | +324058.3% | +130.8588 to +193.1995 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 751.4 | +187750.0% | +647.1712 to +854.8288 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.3 | 912.3 | +1549.9% | +753.4993 to +960.5923 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.5 | +14.500 (native is 0) | +9.5990 to +19.4010 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.44 | −9.3% | −1.1286 to +0.0088 | no |
| node-hours | 2.511 | 2.279 | −9.2% | −0.4713 to +0.0068 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272 | +0.1% | −0.2832 to +0.8987 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 254.3 | −6.4% | −35.3463 to +0.7493 | no |
| response time (ms), mean | 289.5 | 264.1 | −8.8% | −36.9772 to −13.8372 | yes: GAIN |
| response time (ms), 95th percentile | 908.8 | 969 | +6.6% | +4.6486 to +115.7184 | yes: LOSS |
| response time (ms), 99th percentile | 1299 | 1408 | +8.3% | +10.6258 to +206.1986 | yes: LOSS |
| time over the response line (% of samples) | 17.01 | 17.83 | +4.8% | −0.5016 to +2.1455 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11.1 | +2.8% | −0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 | +29.100 (native is 0) | +19.4827 to +38.7173 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 10.72 | +17.7% | −0.6519 to +3.8752 | no |
| utilisation (used / allocatable) | 0.05901 | 0.06549 | +11.0% | +0.0001 to +0.0129 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.416 | 1.415 | −0.1% | −0.0215 to +0.0187 | no |
| Omni's own CPU (cores), mean | 0 | 0.01683 | +0.017 (native is 0) | +0.0156 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.416 | 1.432 | +1.1% | −0.0043 to +0.0352 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 429.6 | −7.3% | −68.4598 to +1.2628 | no |
| HPA replicas, mean | 1.949 | 2.4 | +23.1% | +0.2215 to +0.6806 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.5181 to +1.9181 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | −0.5181 to +1.9181 | no |
| host CPU busy, the real machine under kind (%) | 40.55 | 41.4 | +2.1% | +0.5490 to +1.1390 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 746.5 | 750.1 | +0.5% | +0.7748 to +6.4252 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.942 | −17.6% | −2.1047 to −0.0117 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.02917 | −41.7% | −0.0498 to +0.0081 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.1 | −75.0% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.3 | 58.32 | +5.5% | +0.2488 to +5.8012 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.44 | −9.3% | −1.1286 to +0.0088 | no |
| node-hours | 2.516 | 2.279 | −9.4% | −0.4759 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272 | −0.1% | −1.8833 to +1.1210 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 254.3 | −6.6% | −37.2167 to +1.2419 | no |
| response time (ms), mean | 145.9 | 264.1 | +81.0% | +75.6573 to +160.8149 | yes: LOSS |
| response time (ms), 95th percentile | 248.2 | 969 | +290.4% | +510.7139 to +930.8491 | yes: LOSS |
| response time (ms), 99th percentile | 366.1 | 1408 | +284.6% | +736.9259 to +1346.7595 | yes: LOSS |
| time over the response line (% of samples) | 0.2311 | 17.83 | +7615.0% | +11.4362 to +23.7641 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.1 | +11.100 (native is 0) | +8.2298 to +13.9702 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 | +29.100 (native is 0) | +19.4827 to +38.7173 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1221 | 10.72 | −99.1% | −1379.3621 to −1040.4279 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05952 | 0.06549 | +10.0% | +0.0025 to +0.0095 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.429 | 1.415 | −1.0% | −0.1077 to +0.0805 | no |
| Omni's own CPU (cores), mean | 0 | 0.01683 | +0.017 (native is 0) | +0.0156 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.432 | +0.2% | −0.0908 to +0.0973 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 429.6 | −5.6% | −37.5807 to −13.8267 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.4 | +20.1% | +0.1800 to +0.6238 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.1366 to +1.9366 | no |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | −0.1366 to +1.9366 | no |
| host CPU busy, the real machine under kind (%) | 44.93 | 41.4 | −7.9% | −5.1803 to −1.8774 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1482 | 750.1 | −49.4% | −787.4874 to −676.5126 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.755 | −54.1% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 162.1 | 0.02917 | −100.0% | −193.2292 to −130.8708 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 751.4 | 0.1 | −100.0% | −855.2449 to −647.3551 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 912.3 | 58.32 | −93.6% | −956.3404 to −751.7013 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.5 | 0 | −100.0% | −19.4010 to −9.5990 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.989 | −0.2% | −0.0348 to +0.0135 | no |
| node-hours | 2.511 | 2.511 | −0.0% | −0.0183 to +0.0177 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272.1 | +0.2% | −1.0382 to +1.8893 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 271.7 | +0.0% | −1.5389 to +1.7233 | no |
| response time (ms), mean | 289.5 | 107.9 | −62.7% | −229.2769 to −133.9179 | yes: GAIN |
| response time (ms), 95th percentile | 908.8 | 238.1 | −73.8% | −869.0804 to −472.2356 | yes: GAIN |
| response time (ms), 99th percentile | 1299 | 360.4 | −72.3% | −1213.5556 to −664.6202 | yes: GAIN |
| time over the response line (% of samples) | 17.01 | 0.253 | −98.5% | −22.8299 to −10.6828 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 0.1 | −99.1% | −14.0047 to −7.3953 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.600 (native is 0) | +10.2834 to +14.9166 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 1228 | +13380.9% | +1032.2634 to +1404.8500 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05901 | 0.05944 | +0.7% | −0.0033 to +0.0042 | no |
| CPU used (cores), mean | 1.416 | 1.424 | +0.6% | −0.0782 to +0.0939 | no |
| Omni's own CPU (cores), mean | 0 | 0.01274 | +0.013 (native is 0) | +0.0119 to +0.0136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.416 | 1.437 | +1.5% | −0.0649 to +0.1061 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 455.6 | −1.6% | −39.5188 to +24.4377 | no |
| HPA replicas, mean | 1.949 | 2.006 | +2.9% | −0.0556 to +0.1696 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 40.55 | 45.03 | +11.0% | +3.0481 to +5.9099 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 746.5 | 1480 | +98.2% | +668.2178 to +798.1822 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.444 | −9.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 160.7 | +321366.7% | +115.0954 to +206.2713 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 739.1 | +184675.0% | +532.9265 to +944.4735 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.3 | 889.7 | +1508.9% | +721.7884 to +946.9700 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.5 | +12.500 (native is 0) | +8.1392 to +16.8608 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*