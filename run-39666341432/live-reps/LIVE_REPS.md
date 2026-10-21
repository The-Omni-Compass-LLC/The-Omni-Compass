# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.914 | 5.019 |
| node-hours | 2.512 | 2.508 | 2.059 | 2.104 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.3 | 271.9 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.3 | 237.8 | 241.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 373.2 | 337.3 | 324.7 | 338 |
| response time (ms), 95th percentile | 1375 | 1378 | 1343 | 1566 |
| response time (ms), 99th percentile | 1939 | 1953 | 1817 | 2181 |
| time over the response line (% of samples) | 16.65 | 11.61 | 14.83 | 12.7 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.1 | 7.5 | 8.111 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 45 | 34.89 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 66.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.92 | 14.95 | 15.87 | 20.5 |
| utilisation (used / allocatable) | 0.05971 | 0.05863 | 0.07078 | 0.07145 |
| CPU used (cores), mean | 1.433 | 1.407 | 1.398 | 1.422 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01701 | 0.01607 |
| CPU used with Omni's own (cores), mean | 1.433 | 1.407 | 1.415 | 1.438 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 478.4 | 413.8 | 411 |
| HPA replicas, mean | 1.947 | 2.034 | 2.063 | 2.203 |
| pods started | 0 | 0.1 | 0.4 | 0.3333 |
| pod start wait, total (s) | 0 | 0.2 | 0.9 | 0.3333 |
| pod start wait, mean (s) | 0 | 0.2 | 0.9 | 0.3333 |
| host CPU busy, the real machine under kind (%) | 40.57 | 40.01 | 41.18 | 41.57 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 788 | 783.8 | 787.2 | 797.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.974 | 4.409 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.162 | 0.3625 | 0.3375 | 0.4583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2.3 | 2.1 | 2.333 |
| queue: job turnaround, submitted to done, mean (s) | 93.38 | 90.66 | 91.44 | 104.8 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.019 | -16.4% | -1.893 to -0.06933 | yes: GAIN |
| node-hours | 2.508 | 2.104 | -16.1% | -0.7847 to -0.02217 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.4 | +0.3% | -0.03801 to +1.806 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 241.6 | -11.0% | -58.7 to -1.215 | yes: GAIN |
| response time (ms), mean | 359.5 | 338 | -6.0% | -36.33 to -6.763 | yes: GAIN |
| response time (ms), 95th percentile | 1498 | 1566 | +4.5% | -18.77 to +154.3 | no |
| response time (ms), 99th percentile | 2123 | 2181 | +2.7% | -223.9 to +340.3 | no |
| time over the response line (% of samples) | 12.85 | 12.7 | -1.1% | -1.18 to +0.8919 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.889 | 8.111 | +2.8% | -0.1167 to +0.5612 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.89 | +34.9 (native is 0) | +21.4 to +48.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.86 | 20.5 | +29.3% | -2.111 to +11.4 | no |
| utilisation (used / allocatable) | 0.05938 | 0.07145 | +20.3% | +0.0007588 to +0.02338 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.425 | 1.422 | -0.2% | -0.02759 to +0.02146 | no |
| Omni's own CPU (cores), mean | 0 | 0.01607 | +0.0161 (native is 0) | +0.01419 to +0.01795 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.425 | 1.438 | +0.9% | -0.01171 to +0.03772 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 411 | -13.3% | -122.9 to -3.274 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.019 | 2.203 | +9.1% | -0.1493 to +0.5173 | no |
| pods started | 0.1111 | 0.3333 | +200.0% | -0.1167 to +0.5612 | no |
| pod start wait, total (s) | 0.2222 | 0.3333 | +50.0% | -0.3508 to +0.573 | no |
| pod start wait, mean (s) | 0.2222 | 0.3333 | +50.0% | -0.3508 to +0.573 | no |
| host CPU busy, the real machine under kind (%) | 40.5 | 41.57 | +2.6% | +0.5274 to +1.603 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790.6 | 797.4 | +0.9% | -1.921 to +15.7 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.409 | -26.5% | -3.026 to -0.1557 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3981 | 0.4583 | +15.1% | -0.1719 to +0.2923 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.556 | 2.333 | -8.7% | -2.354 to +1.91 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.42 | 104.8 | +7.5% | -3.178 to +17.87 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.262e-15 to +6.694e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.508 | -0.2% | -0.01028 to +0.00102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.5 | -0.2% | -1.394 to +0.2612 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.5 | -0.2% | -1.394 to +0.2612 | no |
| response time (ms), mean | 373.2 | 359.5 | -3.7% | -33.47 to +6.16 | no |
| response time (ms), 95th percentile | 1375 | 1498 | +8.9% | -59.04 to +305 | no |
| response time (ms), 99th percentile | 1939 | 2123 | +9.5% | -80.71 to +448.7 | no |
| time over the response line (% of samples) | 16.65 | 12.85 | -22.8% | -6.692 to -0.9134 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.889 | -1.4% | -0.3673 to +0.1451 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.92 | 15.86 | +13.9% | -2.536 to +6.402 | no |
| utilisation (used / allocatable) | 0.05971 | 0.05938 | -0.6% | -0.001158 to +0.0004938 | no |
| CPU used (cores), mean | 1.433 | 1.425 | -0.6% | -0.02779 to +0.01185 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.433 | 1.425 | -0.6% | -0.02779 to +0.01185 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 474.1 | +0.9% | -1.1 to +9.602 | no |
| HPA replicas, mean | 1.947 | 2.019 | +3.7% | -0.06559 to +0.2106 | no |
| pods started | 0 | 0.1111 | +0.111 (native is 0) | -0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0 | 0.2222 | +0.222 (native is 0) | -0.2902 to +0.7347 | no |
| pod start wait, mean (s) | 0 | 0.2222 | +0.222 (native is 0) | -0.2902 to +0.7347 | no |
| host CPU busy, the real machine under kind (%) | 40.57 | 40.5 | -0.2% | -0.679 to +0.5357 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 788 | 790.6 | +0.3% | -7.921 to +13.03 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.162 | 0.3981 | +145.7% | -0.2241 to +0.6964 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2.556 | +155.6% | -2.674 to +5.785 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.38 | 97.42 | +4.3% | -6.015 to +14.11 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.937 | -17.7% | -1.742 to -0.3831 | yes: GAIN |
| node-hours | 2.512 | 2.069 | -17.7% | -0.7261 to -0.1608 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.2 | +0.1% | -0.7875 to +1.065 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 238.8 | -12.2% | -54.59 to -11.9 | yes: GAIN |
| response time (ms), mean | 373.2 | 347.6 | -6.9% | -41.18 to -9.991 | yes: GAIN |
| response time (ms), 95th percentile | 1375 | 1452 | +5.6% | -56.82 to +211.1 | no |
| response time (ms), 99th percentile | 1939 | 1961 | +1.2% | -91.84 to +136.5 | no |
| time over the response line (% of samples) | 16.65 | 16.32 | -2.0% | -0.8174 to +0.1499 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.33 | +41.3 (native is 0) | +22.04 to +60.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.92 | 16.86 | +21.1% | -3.213 to +9.098 | no |
| utilisation (used / allocatable) | 0.05971 | 0.07142 | +19.6% | +0.003912 to +0.0195 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.433 | 1.418 | -1.1% | -0.04777 to +0.01754 | no |
| Omni's own CPU (cores), mean | 0 | 0.01631 | +0.0163 (native is 0) | +0.01459 to +0.01803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.433 | 1.434 | +0.1% | -0.0323 to +0.03469 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 410.2 | -12.7% | -104.2 to -15.24 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.947 | 2.075 | +6.6% | -0.04925 to +0.3067 | no |
| pods started | 0 | 0.4444 | +0.444 (native is 0) | +0.03932 to +0.8496 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | -0.01685 to +2.017 | no |
| pod start wait, mean (s) | 0 | 1 | +1 (native is 0) | -0.01685 to +2.017 | no |
| host CPU busy, the real machine under kind (%) | 40.57 | 41.6 | +2.5% | +0.5735 to +1.476 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 788 | 794.3 | +0.8% | -1.534 to +14.2 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.014 | -33.1% | -3.162 to -0.8106 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.162 | 0.375 | +131.4% | -0.2341 to +0.66 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2.333 | +133.3% | -1.517 to +4.184 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.38 | 98.34 | +5.3% | -2.804 to +12.74 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.914 | -18.1% | -1.685 to -0.4877 | yes: GAIN |
| node-hours | 2.508 | 2.059 | -17.9% | -0.6995 to -0.1987 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.9 | +0.2% | -0.06216 to +1.264 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 237.8 | -12.4% | -52.47 to -14.56 | yes: GAIN |
| response time (ms), mean | 337.3 | 324.7 | -3.7% | -25.05 to -0.1772 | yes: GAIN |
| response time (ms), 95th percentile | 1378 | 1343 | -2.5% | -116.1 to +46.76 | no |
| response time (ms), 99th percentile | 1953 | 1817 | -7.0% | -350.7 to +78.43 | no |
| time over the response line (% of samples) | 11.61 | 14.83 | +27.7% | +0.8402 to +5.595 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.5 | +5.6% | -0.2911 to +1.091 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45 | +45 (native is 0) | +26.15 to +63.85 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.95 | 15.87 | +6.2% | -2.184 to +4.03 | no |
| utilisation (used / allocatable) | 0.05863 | 0.07078 | +20.7% | +0.005046 to +0.01924 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.407 | 1.398 | -0.6% | -0.0322 to +0.01476 | no |
| Omni's own CPU (cores), mean | 0 | 0.01701 | +0.017 (native is 0) | +0.01483 to +0.01919 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.415 | +0.6% | -0.0157 to +0.03227 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.4 | 413.8 | -13.5% | -105.7 to -23.58 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.034 | 2.063 | +1.4% | -0.1531 to +0.2116 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | -0.3144 to +1.714 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | -0.3144 to +1.714 | no |
| host CPU busy, the real machine under kind (%) | 40.01 | 41.18 | +2.9% | +0.7273 to +1.605 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 783.8 | 787.2 | +0.4% | -0.621 to +7.421 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.974 | -33.8% | -3.062 to -0.9905 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3625 | 0.3375 | -6.9% | -0.06762 to +0.01762 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.1 | -8.7% | -1.774 to +1.374 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.66 | 91.44 | +0.9% | -3.442 to +5 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.019 | -16.4% | -1.893 to -0.06933 | yes: GAIN |
| node-hours | 2.512 | 2.104 | -16.2% | -0.7872 to -0.02892 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.4 | +0.1% | -0.5184 to +1.154 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 241.6 | -11.2% | -59.02 to -2.034 | yes: GAIN |
| response time (ms), mean | 373.2 | 338 | -9.4% | -55.74 to -14.67 | yes: GAIN |
| response time (ms), 95th percentile | 1375 | 1566 | +13.9% | -24.67 to +406.1 | no |
| response time (ms), 99th percentile | 1939 | 2181 | +12.5% | +17.49 to +466.9 | yes: LOSS |
| time over the response line (% of samples) | 16.65 | 12.7 | -23.7% | -6.767 to -1.126 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.111 | +1.4% | -0.3508 to +0.573 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.89 | +34.9 (native is 0) | +21.4 to +48.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.92 | 20.5 | +47.3% | -2.958 to +16.12 | no |
| utilisation (used / allocatable) | 0.05971 | 0.07145 | +19.7% | +0.0006658 to +0.02281 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.433 | 1.422 | -0.8% | -0.04921 to +0.02714 | no |
| Omni's own CPU (cores), mean | 0 | 0.01607 | +0.0161 (native is 0) | +0.01419 to +0.01795 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.433 | 1.438 | +0.4% | -0.03375 to +0.04381 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 411 | -12.5% | -115.9 to -1.82 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.947 | 2.203 | +13.2% | +0.03997 to +0.473 | yes: power given |
| pods started | 0 | 0.3333 | +0.333 (native is 0) | -0.051 to +0.7177 | no |
| pod start wait, total (s) | 0 | 0.3333 | +0.333 (native is 0) | -0.051 to +0.7177 | no |
| pod start wait, mean (s) | 0 | 0.3333 | +0.333 (native is 0) | -0.051 to +0.7177 | no |
| host CPU busy, the real machine under kind (%) | 40.57 | 41.57 | +2.4% | -0.02019 to +2.007 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 788 | 797.4 | +1.2% | -8.377 to +27.27 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.409 | -26.5% | -3.026 to -0.1557 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.162 | 0.4583 | +182.9% | -0.1797 to +0.7723 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2.333 | +133.3% | -1.329 to +3.996 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.38 | 104.8 | +12.2% | -7.651 to +30.44 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*