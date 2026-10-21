# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.399 | 5.997 |
| node-hours | 2.513 | 2.516 | 2.263 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.5 | 272.2 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 272.5 | 253.3 | 272 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 317 | 140.1 | 282.4 | 105.6 |
| response time (ms), 95th percentile | 1085 | 247.3 | 1101 | 233.2 |
| response time (ms), 99th percentile | 1527 | 346.9 | 1556 | 340.5 |
| time over the response line (% of samples) | 15.57 | 0.2624 | 16.04 | 0.2088 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 0 | 9.2 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.8 | 11.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.555 | 1099 | 9.623 | 1132 |
| utilisation (used / allocatable) | 0.05846 | 0.06039 | 0.06695 | 0.05898 |
| CPU used (cores), mean | 1.403 | 1.449 | 1.416 | 1.415 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01549 | 0.01183 |
| CPU used with Omni's own (cores), mean | 1.403 | 1.449 | 1.431 | 1.427 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471 | 448.9 | 428.3 | 458.9 |
| HPA replicas, mean | 1.925 | 2.011 | 2.236 | 1.916 |
| pods started | 0 | 0.1 | 0.3 | 0.1 |
| pod start wait, total (s) | 0 | 0.3 | 0.4 | 0.1 |
| pod start wait, mean (s) | 0 | 0.3 | 0.4 | 0.1 |
| host CPU busy, the real machine under kind (%) | 40.3 | 45.2 | 41.06 | 44.52 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 762.8 | 1428 | 763 | 1455 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.025 | 5.9 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 139.6 | 0.04583 | 168.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 694.2 | 0.3 | 838.5 |
| queue: job turnaround, submitted to done, mean (s) | 69.7 | 813.4 | 70 | 851.2 |
| queue: jobs unfinished at the window's end | 0 | 10.1 | 0 | 11.1 |

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
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.01058 to +0.004093 | no |
| node-hours | 2.516 | 2.516 | -0.0% | -0.00876 to +0.008371 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.1 | -0.1% | -1.163 to +0.3482 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272 | -0.2% | -1.268 to +0.2492 | no |
| response time (ms), mean | 140.1 | 105.6 | -24.6% | -44.28 to -24.71 | yes: GAIN |
| response time (ms), 95th percentile | 247.3 | 233.2 | -5.7% | -30.32 to +2.169 | no |
| response time (ms), 99th percentile | 346.9 | 340.5 | -1.8% | -26.25 to +13.47 | no |
| time over the response line (% of samples) | 0.2624 | 0.2088 | -20.4% | -0.1339 to +0.02687 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 | +11.9 (native is 0) | +11.11 to +12.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1099 | 1132 | +3.1% | -48.47 to +115.6 | no |
| utilisation (used / allocatable) | 0.06039 | 0.05898 | -2.3% | -0.002546 to -0.0002826 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.449 | 1.415 | -2.4% | -0.06218 to -0.007226 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01183 | +0.0118 (native is 0) | +0.0106 to +0.01306 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.449 | 1.427 | -1.6% | -0.05072 to +0.004972 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.9 | 458.9 | +2.2% | +1.964 to +17.89 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.011 | 1.916 | -4.7% | -0.2772 to +0.08736 | no |
| pods started | 0.1 | 0.1 | +0.0% | +0 to +0 | no |
| pod start wait, total (s) | 0.3 | 0.1 | -66.7% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | -66.7% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 45.2 | 44.52 | -1.5% | -1.722 to +0.343 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1428 | 1455 | +1.9% | -30.2 to +84 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.9 | -1.7% | -1.371 to +1.171 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 139.6 | 168.8 | +20.9% | -28.3 to +86.65 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 694.2 | 838.5 | +20.8% | -76.67 to +365.3 | no |
| queue: job turnaround, submitted to done, mean (s) | 813.4 | 851.2 | +4.7% | -22.9 to +98.65 | no |
| queue: jobs unfinished at the window's end | 10.1 | 11.1 | +9.9% | -0.4698 to +2.47 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.789e-15 to -4.083e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.516 | +0.1% | -0.005364 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.5 | +0.3% | -1.032 to +2.646 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 272.5 | +0.3% | -1.032 to +2.646 | no |
| response time (ms), mean | 317 | 140.1 | -55.8% | -297.2 to -56.51 | yes: GAIN |
| response time (ms), 95th percentile | 1085 | 247.3 | -77.2% | -1414 to -261.4 | yes: GAIN |
| response time (ms), 99th percentile | 1527 | 346.9 | -77.3% | -1994 to -365.8 | yes: GAIN |
| time over the response line (% of samples) | 15.57 | 0.2624 | -98.3% | -24.41 to -6.209 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 0 | -100.0% | -13.41 to -4.991 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.555 | 1099 | +11400.2% | +820.7 to +1358 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05846 | 0.06039 | +3.3% | -0.003854 to +0.007712 | no |
| CPU used (cores), mean | 1.403 | 1.449 | +3.3% | -0.09249 to +0.1851 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.403 | 1.449 | +3.3% | -0.09249 to +0.1851 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471 | 448.9 | -4.7% | -65.26 to +21.16 | no |
| HPA replicas, mean | 1.925 | 2.011 | +4.4% | -0.07285 to +0.2436 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 40.3 | 45.2 | +12.2% | +2.167 to +7.643 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.8 | 1428 | +87.2% | +577.4 to +753 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 139.6 | +239228.6% | +105.3 to +173.8 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 694.2 | +138740.0% | +542.2 to +845.2 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 69.7 | 813.4 | +1067.0% | +603.7 to +883.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.1 | +10.1 (native is 0) | +4.083 to +16.12 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.399 | -10.0% | -1.349 to +0.1477 | no |
| node-hours | 2.513 | 2.263 | -10.0% | -0.5622 to +0.06178 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.2 | +0.2% | -0.1919 to +1.165 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 253.3 | -6.8% | -41.76 to +4.975 | no |
| response time (ms), mean | 317 | 282.4 | -10.9% | -53.35 to -15.78 | yes: GAIN |
| response time (ms), 95th percentile | 1085 | 1101 | +1.5% | -61.93 to +93.92 | no |
| response time (ms), 99th percentile | 1527 | 1556 | +1.9% | -96.6 to +154.2 | no |
| time over the response line (% of samples) | 15.57 | 16.04 | +3.0% | -0.301 to +1.242 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.2 | +0.0% | -0.584 to +0.584 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.8 (native is 0) | +20.99 to +62.61 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.555 | 9.623 | +0.7% | -2.104 to +2.24 | no |
| utilisation (used / allocatable) | 0.05846 | 0.06695 | +14.5% | -0.001714 to +0.01869 | no |
| CPU used (cores), mean | 1.403 | 1.416 | +0.9% | -0.009092 to +0.03452 | no |
| Omni's own CPU (cores), mean | 0 | 0.01549 | +0.0155 (native is 0) | +0.01416 to +0.01682 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.403 | 1.431 | +2.0% | +0.006658 to +0.04975 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471 | 428.3 | -9.1% | -91.27 to +5.856 | no |
| HPA replicas, mean | 1.925 | 2.236 | +16.1% | +0.04398 to +0.5762 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 40.3 | 41.06 | +1.9% | +0.1838 to +1.346 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.8 | 763 | +0.0% | -7.093 to +7.493 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.025 | -16.2% | -2.133 to +0.1832 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.04583 | -21.4% | -0.06326 to +0.03826 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 69.7 | 70 | +0.4% | -6.018 to +6.626 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.399 | -10.0% | -1.349 to +0.1477 | no |
| node-hours | 2.516 | 2.263 | -10.1% | -0.565 to +0.05922 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.2 | -0.1% | -1.968 to +1.327 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 253.3 | -7.0% | -43.64 to +5.243 | no |
| response time (ms), mean | 140.1 | 282.4 | +101.6% | +36.5 to +248.1 | yes: LOSS |
| response time (ms), 95th percentile | 247.3 | 1101 | +345.2% | +330.2 to +1377 | yes: LOSS |
| response time (ms), 99th percentile | 346.9 | 1556 | +348.4% | +460.7 to +1957 | yes: LOSS |
| time over the response line (% of samples) | 0.2624 | 16.04 | +6013.9% | +6.696 to +24.86 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 9.2 | +9.2 (native is 0) | +5.045 to +13.35 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.8 | +41.8 (native is 0) | +20.99 to +62.61 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1099 | 9.623 | -99.1% | -1358 to -820.9 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06039 | 0.06695 | +10.9% | -0.001323 to +0.01444 | no |
| CPU used (cores), mean | 1.449 | 1.416 | -2.3% | -0.169 to +0.1019 | no |
| Omni's own CPU (cores), mean | 0 | 0.01549 | +0.0155 (native is 0) | +0.01416 to +0.01682 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.449 | 1.431 | -1.2% | -0.1534 to +0.1172 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.9 | 428.3 | -4.6% | -54.01 to +12.69 | no |
| HPA replicas, mean | 2.011 | 2.236 | +11.2% | -0.02602 to +0.4754 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | -0.6113 to +0.8113 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | -0.6113 to +0.8113 | no |
| host CPU busy, the real machine under kind (%) | 45.2 | 41.06 | -9.2% | -6.636 to -1.644 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1428 | 763 | -46.6% | -751.6 to -578.4 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.34 | -44.3% | -8.382 to +3.063 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 139.6 | 0.04583 | -100.0% | -173.9 to -105.2 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 694.2 | 0.3 | -100.0% | -845.6 to -542.2 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 813.4 | 70 | -91.4% | -883.6 to -603.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.1 | 0 | -100.0% | -16.12 to -4.083 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.01058 to +0.004093 | no |
| node-hours | 2.513 | 2.516 | +0.1% | -0.003111 to +0.008055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.1 | +0.1% | -1.697 to +2.496 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 272 | +0.1% | -1.717 to +2.312 | no |
| response time (ms), mean | 317 | 105.6 | -66.7% | -336.5 to -86.27 | yes: GAIN |
| response time (ms), 95th percentile | 1085 | 233.2 | -78.5% | -1432 to -271.8 | yes: GAIN |
| response time (ms), 99th percentile | 1527 | 340.5 | -77.7% | -1997 to -375.4 | yes: GAIN |
| time over the response line (% of samples) | 15.57 | 0.2088 | -98.7% | -24.47 to -6.253 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 0.1 | -98.9% | -13.26 to -4.937 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 | +11.9 (native is 0) | +11.11 to +12.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.555 | 1132 | +11751.7% | +885 to +1361 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05846 | 0.05898 | +0.9% | -0.004767 to +0.005797 | no |
| CPU used (cores), mean | 1.403 | 1.415 | +0.8% | -0.1145 to +0.1376 | no |
| Omni's own CPU (cores), mean | 0 | 0.01183 | +0.0118 (native is 0) | +0.0106 to +0.01306 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.403 | 1.427 | +1.7% | -0.1016 to +0.1484 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471 | 458.9 | -2.6% | -51.77 to +27.53 | no |
| HPA replicas, mean | 1.925 | 1.916 | -0.5% | -0.1399 to +0.1208 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 40.3 | 44.52 | +10.5% | +1.34 to +7.09 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.8 | 1455 | +90.7% | +612.9 to +771.3 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.9 | -1.7% | -1.371 to +1.171 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 168.8 | +289242.9% | +117 to +220.5 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 838.5 | +167600.0% | +613.6 to +1062 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 69.7 | 851.2 | +1121.4% | +641.8 to +921.3 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.1 | +11.1 (native is 0) | +5.092 to +17.11 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*