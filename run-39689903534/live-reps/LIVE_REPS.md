# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.31 | 10.74 |
| node-hours | 5.018 | 5.031 | 4.32 | 4.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 526.1 | 525.1 | 526.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 526.1 | 471.9 | 486.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 512.2 | 755 | 512.2 | 834.3 |
| response time (ms), 95th percentile | 1996 | 2853 | 2199 | 3295 |
| response time (ms), 99th percentile | 2697 | 3859 | 2965 | 4267 |
| time over the response line (% of samples) | 17.92 | 24.79 | 18.73 | 28.86 |
| failed requests (%) | 0 | 0.05367 | 0.02166 | 0.07992 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 12.1 | 10.6 | 13.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 81.1 | 71.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 19.14 | 15.06 | 33.77 |
| utilisation (used / allocatable) | 0.03376 | 0.03483 | 0.03894 | 0.03879 |
| CPU used (cores), mean | 1.62 | 1.672 | 1.601 | 1.665 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0119 | 0.01236 |
| CPU used with Omni's own (cores), mean | 1.62 | 1.672 | 1.613 | 1.677 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 799.4 | 778.3 | 715.8 | 706.1 |
| HPA replicas, mean | 4.026 | 3.987 | 4.444 | 4.317 |
| pods started | 0.3 | 0 | 1.2 | 1.4 |
| pod start wait, total (s) | 0.6 | 0 | 2.3 | 3.8 |
| pod start wait, mean (s) | 0.4 | 0 | 1.367 | 1.883 |
| host CPU busy, the real machine under kind (%) | 48.6 | 55.09 | 50.7 | 57.61 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 844.6 | 946.9 | 860.7 | 983.2 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.043 | 9.875 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 10.73 | 0.08333 | 12.04 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 88.6 | 0.5 | 95.1 |
| queue: job turnaround, submitted to done, mean (s) | 153.4 | 226.3 | 165.6 | 274.3 |
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
| worker nodes in service, mean | 12 | 10.74 | -10.5% | -2.648 to +0.127 | no |
| node-hours | 5.031 | 4.503 | -10.5% | -1.115 to +0.05951 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 526.3 | +0.0% | -2.016 to +2.381 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 486.7 | -7.5% | -83.76 to +4.903 | no |
| response time (ms), mean | 755 | 834.3 | +10.5% | -6.155 to +164.6 | no |
| response time (ms), 95th percentile | 2853 | 3295 | +15.5% | +115.8 to +768.8 | yes: LOSS |
| response time (ms), 99th percentile | 3859 | 4267 | +10.6% | -119.1 to +934.3 | no |
| time over the response line (% of samples) | 24.79 | 28.86 | +16.4% | -0.2108 to +8.363 | no |
| failed requests (%) | 0.05367 | 0.07992 | +48.9% | -0.1199 to +0.1724 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 13.3 | +9.9% | +0.1997 to +2.2 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.4 | +71.4 (native is 0) | +35.3 to +107.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.14 | 33.77 | +76.5% | -6.306 to +35.57 | no |
| utilisation (used / allocatable) | 0.03483 | 0.03879 | +11.4% | -0.0009048 to +0.008824 | no |
| CPU used (cores), mean | 1.672 | 1.665 | -0.4% | -0.1212 to +0.1069 | no |
| Omni's own CPU (cores), mean | 0 | 0.01236 | +0.0124 (native is 0) | +0.01135 to +0.01337 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.672 | 1.677 | +0.3% | -0.1084 to +0.1189 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.3 | 706.1 | -9.3% | -154.9 to +10.61 | no |
| HPA replicas, mean | 3.987 | 4.317 | +8.3% | +0.02243 to +0.6372 | yes: power given |
| pods started | 0 | 1.4 | +1.4 (native is 0) | +0.6311 to +2.169 | yes: power given |
| pod start wait, total (s) | 0 | 3.8 | +3.8 (native is 0) | +0.5517 to +7.048 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.883 | +1.88 (native is 0) | +0.3157 to +3.451 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.09 | 57.61 | +4.6% | +0.8152 to +4.214 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 946.9 | 983.2 | +3.8% | +1.418 to +71.18 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.875 | -17.7% | -4.423 to +0.1721 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 10.73 | 12.04 | +12.3% | -5.658 to +8.292 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 88.6 | 95.1 | +7.3% | -33.81 to +46.81 | no |
| queue: job turnaround, submitted to done, mean (s) | 226.3 | 274.3 | +21.2% | +11.84 to +84.16 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -4.636e-15 to +1.793e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.018 | 5.031 | +0.3% | +0.004407 to +0.02159 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 526.1 | +0.4% | +1.053 to +3.128 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 526.1 | +0.4% | +1.053 to +3.128 | yes: power given |
| response time (ms), mean | 512.2 | 755 | +47.4% | +69.79 to +415.8 | yes: LOSS |
| response time (ms), 95th percentile | 1996 | 2853 | +42.9% | +314.2 to +1400 | yes: LOSS |
| response time (ms), 99th percentile | 2697 | 3859 | +43.1% | +462.3 to +1862 | yes: LOSS |
| time over the response line (% of samples) | 17.92 | 24.79 | +38.3% | +2.562 to +11.16 | yes: LOSS |
| failed requests (%) | 0 | 0.05367 | +0.0537 (native is 0) | -0.0345 to +0.1418 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 12.1 | +31.5% | +0.1102 to +5.69 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 19.14 | +33.6% | -1.666 to +11.29 | no |
| utilisation (used / allocatable) | 0.03376 | 0.03483 | +3.2% | +0.0002224 to +0.001933 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.62 | 1.672 | +3.2% | +0.01067 to +0.0928 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.62 | 1.672 | +3.2% | +0.01067 to +0.0928 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 799.4 | 778.3 | -2.6% | -39.88 to -2.368 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.026 | 3.987 | -1.0% | -0.1744 to +0.09599 | no |
| pods started | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| pod start wait, mean (s) | 0.4 | 0 | -100.0% | -1.003 to +0.2032 | no |
| host CPU busy, the real machine under kind (%) | 48.6 | 55.09 | +13.4% | +5.001 to +7.987 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 844.6 | 946.9 | +12.1% | +40.02 to +164.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 10.73 | +12770.0% | -0.8524 to +22.14 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 88.6 | +14666.7% | -24.53 to +200.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 153.4 | 226.3 | +47.5% | +29.76 to +116 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.31 | -14.1% | -3.211 to -0.1695 | yes: GAIN |
| node-hours | 5.018 | 4.32 | -13.9% | -1.333 to -0.06309 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 525.1 | +0.2% | +0.08422 to +2.037 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 471.9 | -9.9% | -99.83 to -4.295 | yes: GAIN |
| response time (ms), mean | 512.2 | 512.2 | -0.0% | -28.87 to +28.78 | no |
| response time (ms), 95th percentile | 1996 | 2199 | +10.2% | +38.56 to +367.8 | yes: LOSS |
| response time (ms), 99th percentile | 2697 | 2965 | +9.9% | +9.65 to +526.3 | yes: LOSS |
| time over the response line (% of samples) | 17.92 | 18.73 | +4.5% | -0.2533 to +1.861 | no |
| failed requests (%) | 0 | 0.02166 | +0.0217 (native is 0) | -0.01308 to +0.0564 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 10.6 | +15.2% | -0.7905 to +3.59 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.1 | +81.1 (native is 0) | +44.41 to +117.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 15.05 | +5.1% | -2.496 to +3.96 | no |
| utilisation (used / allocatable) | 0.03376 | 0.03894 | +15.3% | +0.0005929 to +0.009768 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.62 | 1.601 | -1.2% | -0.05673 to +0.01753 | no |
| Omni's own CPU (cores), mean | 0 | 0.0119 | +0.0119 (native is 0) | +0.0111 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.62 | 1.613 | -0.5% | -0.04498 to +0.02958 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 799.4 | 715.8 | -10.5% | -156.9 to -10.32 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.026 | 4.444 | +10.4% | +0.04299 to +0.7921 | yes: power given |
| pods started | 0.3 | 1.2 | +300.0% | -0.19 to +1.99 | no |
| pod start wait, total (s) | 0.6 | 2.3 | +283.3% | -0.7327 to +4.133 | no |
| pod start wait, mean (s) | 0.4 | 1.367 | +241.7% | -0.4223 to +2.356 | no |
| host CPU busy, the real machine under kind (%) | 48.6 | 50.7 | +4.3% | +1.573 to +2.638 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 844.6 | 860.7 | +1.9% | +3.926 to +28.27 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.043 | -24.6% | -5.511 to -0.404 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.08333 | +0.0% | -0.0466 to +0.0466 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | -16.7% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 153.4 | 165.6 | +7.9% | +3.655 to +20.67 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.31 | -14.1% | -3.211 to -0.1695 | yes: GAIN |
| node-hours | 5.031 | 4.32 | -14.1% | -1.352 to -0.07001 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 525.1 | -0.2% | -2.523 to +0.4625 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 471.9 | -10.3% | -102.3 to -6.05 | yes: GAIN |
| response time (ms), mean | 755 | 512.2 | -32.2% | -400 to -85.66 | yes: GAIN |
| response time (ms), 95th percentile | 2853 | 2199 | -22.9% | -1118 to -189.5 | yes: GAIN |
| response time (ms), 99th percentile | 3859 | 2965 | -23.2% | -1470 to -318.1 | yes: GAIN |
| time over the response line (% of samples) | 24.79 | 18.73 | -24.4% | -9.938 to -2.176 | yes: GAIN |
| failed requests (%) | 0.05367 | 0.02166 | -59.6% | -0.09924 to +0.03522 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 10.6 | -12.4% | -2.408 to -0.5921 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.1 | +81.1 (native is 0) | +44.41 to +117.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.14 | 15.05 | -21.3% | -10.25 to +2.087 | no |
| utilisation (used / allocatable) | 0.03483 | 0.03894 | +11.8% | -0.001037 to +0.009242 | no |
| CPU used (cores), mean | 1.672 | 1.601 | -4.3% | -0.1049 to -0.03776 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0119 | +0.0119 (native is 0) | +0.0111 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.672 | 1.613 | -3.6% | -0.09349 to -0.02538 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 778.3 | 715.8 | -8.0% | -145.3 to +20.27 | no |
| HPA replicas, mean | 3.987 | 4.444 | +11.5% | +0.01346 to +0.9 | yes: power given |
| pods started | 0 | 1.2 | +1.2 (native is 0) | +0.4612 to +1.939 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.3 (native is 0) | +0.4515 to +4.148 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.367 | +1.37 (native is 0) | +0.3952 to +2.338 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.09 | 50.7 | -8.0% | -5.904 to -2.873 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 946.9 | 860.7 | -9.1% | -138.5 to -33.92 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.043 | -24.6% | -5.511 to -0.404 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 10.73 | 0.08333 | -99.2% | -22.13 to +0.8486 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 88.6 | 0.5 | -99.4% | -200.6 to +24.39 | no |
| queue: job turnaround, submitted to done, mean (s) | 226.3 | 165.6 | -26.8% | -97.8 to -23.6 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.74 | -10.5% | -2.648 to +0.127 | no |
| node-hours | 5.018 | 4.503 | -10.3% | -1.096 to +0.06609 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 526.3 | +0.4% | +0.5257 to +4.021 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 486.7 | -7.1% | -81.27 to +6.596 | no |
| response time (ms), mean | 512.2 | 834.3 | +62.9% | +134.1 to +509.9 | yes: LOSS |
| response time (ms), 95th percentile | 1996 | 3295 | +65.1% | +638.2 to +1960 | yes: LOSS |
| response time (ms), 99th percentile | 2697 | 4267 | +58.2% | +804.7 to +2334 | yes: LOSS |
| time over the response line (% of samples) | 17.92 | 28.86 | +61.0% | +4.898 to +16.98 | yes: LOSS |
| failed requests (%) | 0 | 0.07992 | +0.0799 (native is 0) | -0.03177 to +0.1916 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 13.3 | +44.6% | +1.113 to +7.087 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.4 | +71.4 (native is 0) | +35.3 to +107.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 33.77 | +135.8% | -1.524 to +40.42 | no |
| utilisation (used / allocatable) | 0.03376 | 0.03879 | +14.9% | +0.0006218 to +0.009453 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.62 | 1.665 | +2.8% | -0.06933 to +0.1585 | no |
| Omni's own CPU (cores), mean | 0 | 0.01236 | +0.0124 (native is 0) | +0.01135 to +0.01337 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.62 | 1.677 | +3.5% | -0.05657 to +0.1705 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 799.4 | 706.1 | -11.7% | -171.4 to -15.15 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.026 | 4.317 | +7.2% | -0.006422 to +0.5877 | no |
| pods started | 0.3 | 1.4 | +366.7% | +0.06342 to +2.137 | yes: power given |
| pod start wait, total (s) | 0.6 | 3.8 | +533.3% | -0.4286 to +6.829 | no |
| pod start wait, mean (s) | 0.4 | 1.883 | +370.8% | -0.3119 to +3.279 | no |
| host CPU busy, the real machine under kind (%) | 48.6 | 57.61 | +18.5% | +6.774 to +11.24 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 844.6 | 983.2 | +16.4% | +68.71 to +208.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.875 | -17.7% | -4.423 to +0.1721 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 12.04 | +14350.0% | -2.78 to +26.7 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 95.1 | +15750.0% | -23.99 to +213 | no |
| queue: job turnaround, submitted to done, mean (s) | 153.4 | 274.3 | +78.8% | +58.84 to +182.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*