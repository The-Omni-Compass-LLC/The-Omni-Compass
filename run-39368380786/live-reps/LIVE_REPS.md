# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.123 | 5.916 |
| node-hours | 2.514 | 2.516 | 2.15 | 2.478 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.7 | 271.7 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271.7 | 244.1 | 268.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 277.9 | 141.2 | 242 | 103.5 |
| response time (ms), 95th percentile | 863.2 | 236.9 | 913.5 | 221.2 |
| response time (ms), 99th percentile | 1252 | 336.7 | 1296 | 338.3 |
| time over the response line (% of samples) | 14.02 | 0.1697 | 13.87 | 0.2301 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0.1 | 9.6 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.2 | 11.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 999.1 | 9.008 | 1073 |
| utilisation (used / allocatable) | 0.05678 | 0.05869 | 0.06635 | 0.05924 |
| CPU used (cores), mean | 1.363 | 1.409 | 1.359 | 1.405 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01692 | 0.01196 |
| CPU used with Omni's own (cores), mean | 1.363 | 1.409 | 1.376 | 1.417 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 464.6 | 433.5 | 460.3 |
| HPA replicas, mean | 2 | 2.017 | 1.983 | 1.972 |
| pods started | 0.1 | 0 | 0.2 | 0.1 |
| pod start wait, total (s) | 0.2 | 0 | 0.6 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0 | 0.3 | 0.2 |
| host CPU busy, the real machine under kind (%) | 38.72 | 43.61 | 39.55 | 43.9 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 747.2 | 1396 | 750.6 | 1421 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.288 | 5.342 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 146.3 | 0.04167 | 142.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 698.5 | 0.3 | 684.4 |
| queue: job turnaround, submitted to done, mean (s) | 55.45 | 763.3 | 59.44 | 789 |
| queue: jobs unfinished at the window's end | 0 | 9.6 | 0 | 8.8 |

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
| worker nodes in service, mean | 6 | 5.916 | -1.4% | -0.2743 to +0.1061 | no |
| node-hours | 2.516 | 2.478 | -1.5% | -0.1122 to +0.03573 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.5 | -0.1% | -1.499 to +0.9982 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 268.8 | -1.1% | -8.302 to +2.493 | no |
| response time (ms), mean | 141.2 | 103.5 | -26.7% | -43.25 to -32.12 | yes: GAIN |
| response time (ms), 95th percentile | 236.9 | 221.2 | -6.6% | -22.5 to -8.892 | yes: GAIN |
| response time (ms), 99th percentile | 336.7 | 338.3 | +0.4% | -24.02 to +27.05 | no |
| time over the response line (% of samples) | 0.1697 | 0.2301 | +35.6% | -0.05788 to +0.1788 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 | +11.4 (native is 0) | +8.555 to +14.25 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 999.1 | 1073 | +7.4% | +30.73 to +117.5 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05869 | 0.05924 | +0.9% | -0.001358 to +0.002447 | no |
| CPU used (cores), mean | 1.409 | 1.405 | -0.2% | -0.03746 to +0.03087 | no |
| Omni's own CPU (cores), mean | 0 | 0.01196 | +0.012 (native is 0) | +0.01105 to +0.01287 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.417 | +0.6% | -0.0252 to +0.04254 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.6 | 460.3 | -0.9% | -18.45 to +9.953 | no |
| HPA replicas, mean | 2.017 | 1.972 | -2.2% | -0.215 to +0.1253 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 43.61 | 43.9 | +0.7% | -0.6605 to +1.235 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1396 | 1421 | +1.8% | -17.87 to +67.27 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.342 | -11.0% | -3.491 to +2.174 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 146.3 | 142.5 | -2.5% | -43.21 to +35.76 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 698.5 | 684.4 | -2.0% | -197.8 to +169.6 | no |
| queue: job turnaround, submitted to done, mean (s) | 763.3 | 789 | +3.4% | -8.589 to +59.9 | no |
| queue: jobs unfinished at the window's end | 9.6 | 8.8 | -8.3% | -2.702 to +1.102 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.628e-15 to -5.699e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.516 | +0.1% | -0.008981 to +0.01298 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.7 | +0.2% | -0.8481 to +2.021 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271.7 | +0.2% | -0.8481 to +2.021 | no |
| response time (ms), mean | 277.9 | 141.2 | -49.2% | -216.2 to -57.28 | yes: GAIN |
| response time (ms), 95th percentile | 863.2 | 236.9 | -72.6% | -999.5 to -253 | yes: GAIN |
| response time (ms), 99th percentile | 1252 | 336.7 | -73.1% | -1449 to -380.7 | yes: GAIN |
| time over the response line (% of samples) | 14.02 | 0.1697 | -98.8% | -21.74 to -5.958 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0.1 | -98.9% | -12.86 to -5.54 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 999.1 | +10871.5% | +713.8 to +1266 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05678 | 0.05869 | +3.4% | -0.0019 to +0.005732 | no |
| CPU used (cores), mean | 1.363 | 1.409 | +3.4% | -0.04559 to +0.1376 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.363 | 1.409 | +3.4% | -0.04559 to +0.1376 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 464.6 | -4.2% | -50.1 to +9.46 | no |
| HPA replicas, mean | 2 | 2.017 | +0.8% | -0.09154 to +0.1244 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 38.72 | 43.61 | +12.6% | +3.152 to +6.626 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.2 | 1396 | +86.9% | +511.2 to +787.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 146.3 | +233933.3% | +101.3 to +191.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 698.5 | +139600.0% | +508.7 to +887.3 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.45 | 763.3 | +1276.6% | +542.9 to +872.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.6 | +9.6 (native is 0) | +3.501 to +15.7 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.123 | -14.6% | -1.346 to -0.4088 | yes: GAIN |
| node-hours | 2.514 | 2.15 | -14.5% | -0.5667 to -0.1607 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.7 | +0.2% | -0.3353 to +1.457 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 244.1 | -10.0% | -42.42 to -11.64 | yes: GAIN |
| response time (ms), mean | 277.9 | 242 | -12.9% | -44.55 to -27.3 | yes: GAIN |
| response time (ms), 95th percentile | 863.2 | 913.5 | +5.8% | -10.07 to +110.8 | no |
| response time (ms), 99th percentile | 1252 | 1296 | +3.6% | -15.78 to +104.9 | no |
| time over the response line (% of samples) | 14.02 | 13.87 | -1.1% | -0.9908 to +0.6896 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.6 | +3.2% | -0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 | +41.2 (native is 0) | +29.17 to +53.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 9.008 | -1.1% | -2.754 to +2.557 | no |
| utilisation (used / allocatable) | 0.05678 | 0.06635 | +16.9% | +0.004506 to +0.01464 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.363 | 1.359 | -0.3% | -0.01906 to +0.01127 | no |
| Omni's own CPU (cores), mean | 0 | 0.01692 | +0.0169 (native is 0) | +0.01504 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.376 | +1.0% | -0.002962 to +0.02901 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 433.5 | -10.6% | -80.65 to -22.17 | yes, down (shown, not judged) |
| HPA replicas, mean | 2 | 1.983 | -0.9% | -0.1927 to +0.158 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | -1.078 to +1.878 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | -0.7564 to +0.9564 | no |
| host CPU busy, the real machine under kind (%) | 38.72 | 39.55 | +2.1% | +0.6842 to +0.9776 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.2 | 750.6 | +0.5% | +0.1099 to +6.69 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.288 | -28.5% | -2.594 to -0.83 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.04167 | -33.3% | -0.05303 to +0.01136 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.45 | 59.44 | +7.2% | +0.1282 to +7.847 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.123 | -14.6% | -1.346 to -0.4088 | yes: GAIN |
| node-hours | 2.516 | 2.15 | -14.5% | -0.5627 to -0.1687 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 | -0.0% | -1.611 to +1.56 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 244.1 | -10.2% | -43.47 to -11.76 | yes: GAIN |
| response time (ms), mean | 141.2 | 242 | +71.4% | +18.3 to +183.3 | yes: LOSS |
| response time (ms), 95th percentile | 236.9 | 913.5 | +285.6% | +252.1 to +1101 | yes: LOSS |
| response time (ms), 99th percentile | 336.7 | 1296 | +285.0% | +393.5 to +1526 | yes: LOSS |
| time over the response line (% of samples) | 0.1697 | 13.87 | +8073.6% | +5.94 to +21.46 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 9.6 | +9500.0% | +6.141 to +12.86 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 | +41.2 (native is 0) | +29.17 to +53.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 999.1 | 9.008 | -99.1% | -1265 to -714.9 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05869 | 0.06635 | +13.0% | +0.004448 to +0.01087 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.409 | 1.359 | -3.5% | -0.1484 to +0.04863 | no |
| Omni's own CPU (cores), mean | 0 | 0.01692 | +0.0169 (native is 0) | +0.01504 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.376 | -2.3% | -0.1326 to +0.06664 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.6 | 433.5 | -6.7% | -47.76 to -14.43 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.017 | 1.983 | -1.7% | -0.1942 to +0.1266 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.7572 to +1.957 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 43.61 | 39.55 | -9.3% | -5.894 to -2.222 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1396 | 750.6 | -46.2% | -782.8 to -508.8 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.046 | -49.2% | -3.868 to -2.041 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 146.3 | 0.04167 | -100.0% | -191.1 to -101.3 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 698.5 | 0.3 | -100.0% | -887.4 to -509 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 763.3 | 59.44 | -92.2% | -866.7 to -541.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.6 | 0 | -100.0% | -15.7 to -3.501 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.916 | -1.4% | -0.2743 to +0.1061 | no |
| node-hours | 2.514 | 2.478 | -1.4% | -0.1167 to +0.04428 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.5 | +0.1% | -1.118 to +1.791 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 268.8 | -0.9% | -8.502 to +3.866 | no |
| response time (ms), mean | 277.9 | 103.5 | -62.8% | -257.5 to -91.37 | yes: GAIN |
| response time (ms), 95th percentile | 863.2 | 221.2 | -74.4% | -1012 to -271.9 | yes: GAIN |
| response time (ms), 99th percentile | 1252 | 338.3 | -73.0% | -1435 to -392.1 | yes: GAIN |
| time over the response line (% of samples) | 14.02 | 0.2301 | -98.4% | -21.66 to -5.914 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0.1 | -98.9% | -12.84 to -5.556 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 | +11.4 (native is 0) | +8.555 to +14.25 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.107 | 1073 | +11685.6% | +772.5 to +1356 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05678 | 0.05924 | +4.3% | -0.002443 to +0.007364 | no |
| CPU used (cores), mean | 1.363 | 1.405 | +3.1% | -0.06925 to +0.1546 | no |
| Omni's own CPU (cores), mean | 0 | 0.01196 | +0.012 (native is 0) | +0.01105 to +0.01287 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.417 | +4.0% | -0.05651 to +0.1658 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.9 | 460.3 | -5.1% | -62.83 to +13.7 | no |
| HPA replicas, mean | 2 | 1.972 | -1.4% | -0.2335 to +0.1767 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 38.72 | 43.9 | +13.4% | +2.861 to +7.491 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.2 | 1421 | +90.2% | +537.1 to +810.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.342 | -11.0% | -3.491 to +2.174 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 142.5 | +227980.0% | +93.63 to +191.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 684.4 | +136780.0% | +430.2 to +937.6 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 55.45 | 789 | +1322.9% | +569.9 to +897.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.8 | +8.8 (native is 0) | +3.261 to +14.34 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*