# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.802 | 5.046 |
| node-hours | 2.516 | 2.52 | 2.012 | 2.112 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.5 | 270.8 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 271.5 | 233.2 | 241 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 307.1 | 288.9 | 270.1 | 246 |
| response time (ms), 95th percentile | 1078 | 1156 | 1083 | 1210 |
| response time (ms), 99th percentile | 1531 | 1714 | 1544 | 1736 |
| time over the response line (% of samples) | 12.85 | 9.909 | 12.52 | 8.717 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.8 | 6.2 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 57.9 | 44.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.775 | 9.923 | 9.477 | 11.01 |
| utilisation (used / allocatable) | 0.05728 | 0.05567 | 0.06955 | 0.06639 |
| CPU used (cores), mean | 1.375 | 1.336 | 1.327 | 1.347 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01691 | 0.01699 |
| CPU used with Omni's own (cores), mean | 1.375 | 1.336 | 1.344 | 1.364 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.6 | 506.1 | 429.4 | 440.8 |
| HPA replicas, mean | 1.966 | 1.996 | 2.067 | 2.274 |
| pods started | 0.1 | 0.1 | 0.3 | 0.9 |
| pod start wait, total (s) | 0.4 | 0.1 | 0.4 | 1.7 |
| pod start wait, mean (s) | 0.4 | 0.1 | 0.4 | 0.5857 |
| host CPU busy, the real machine under kind (%) | 38.83 | 38.58 | 39.25 | 39.63 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 776.1 | 775.8 | 774.5 | 780.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.91 | 4.332 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.07083 | 0.0625 | 0.075 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | 0.3 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 82.15 | 83.64 | 80.5 | 87.6 |
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
| worker nodes in service, mean | 6 | 5.046 | -15.9% | -1.56 to -0.3481 | yes: GAIN |
| node-hours | 2.52 | 2.112 | -16.2% | -0.6567 to -0.1575 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271 | -0.2% | -1.713 to +0.7854 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 241 | -11.2% | -49.11 to -11.83 | yes: GAIN |
| response time (ms), mean | 288.9 | 246 | -14.9% | -67.58 to -18.24 | yes: GAIN |
| response time (ms), 95th percentile | 1156 | 1210 | +4.7% | -50.71 to +160.5 | no |
| response time (ms), 99th percentile | 1714 | 1736 | +1.3% | -61.8 to +104.9 | no |
| time over the response line (% of samples) | 9.909 | 8.717 | -12.0% | -2.786 to +0.4014 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 6.1 | +5.2% | -0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.5 | +44.5 (native is 0) | +33.59 to +55.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.923 | 11.01 | +11.0% | -1.284 to +3.457 | no |
| utilisation (used / allocatable) | 0.05567 | 0.06639 | +19.3% | +0.004343 to +0.01711 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.336 | 1.347 | +0.8% | -0.01146 to +0.03259 | no |
| Omni's own CPU (cores), mean | 0 | 0.01699 | +0.017 (native is 0) | +0.01547 to +0.01851 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.336 | 1.364 | +2.1% | +0.00487 to +0.05024 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 506.1 | 440.8 | -12.9% | -104.7 to -25.82 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.996 | 2.274 | +13.9% | -0.04382 to +0.5995 | no |
| pods started | 0.1 | 0.9 | +800.0% | -0.8101 to +2.41 | no |
| pod start wait, total (s) | 0.1 | 1.7 | +1600.0% | -1.343 to +4.543 | no |
| pod start wait, mean (s) | 0.1 | 0.5857 | +485.7% | -0.2717 to +1.243 | no |
| host CPU busy, the real machine under kind (%) | 38.58 | 39.63 | +2.7% | +0.3449 to +1.746 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.8 | 780.4 | +0.6% | -0.953 to +10.15 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.332 | -27.8% | -2.669 to -0.6675 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.075 | +5.9% | -0.03418 to +0.04252 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | -60.0% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.64 | 87.6 | +4.7% | -0.5256 to +8.451 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.057e-15 to +8.793e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.52 | +0.2% | -0.004415 to +0.01241 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.5 | -0.0% | -1.118 to +0.8921 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 271.5 | -0.0% | -1.118 to +0.8921 | no |
| response time (ms), mean | 307.1 | 288.9 | -5.9% | -31.25 to -5.21 | yes: GAIN |
| response time (ms), 95th percentile | 1078 | 1156 | +7.2% | -43.24 to +199.3 | no |
| response time (ms), 99th percentile | 1531 | 1714 | +11.9% | -45.2 to +411.1 | no |
| time over the response line (% of samples) | 12.85 | 9.909 | -22.9% | -5.587 to -0.3031 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.8 | -4.9% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.775 | 9.923 | +1.5% | -1.473 to +1.77 | no |
| utilisation (used / allocatable) | 0.05728 | 0.05567 | -2.8% | -0.002423 to -0.0007975 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.375 | 1.336 | -2.8% | -0.05814 to -0.01914 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.375 | 1.336 | -2.8% | -0.05814 to -0.01914 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.6 | 506.1 | +3.4% | +3.571 to +29.32 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.966 | 1.996 | +1.6% | -0.1179 to +0.179 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.4 | 0.1 | -75.0% | -1.257 to +0.6567 | no |
| pod start wait, mean (s) | 0.4 | 0.1 | -75.0% | -1.257 to +0.6567 | no |
| host CPU busy, the real machine under kind (%) | 38.83 | 38.58 | -0.6% | -0.9052 to +0.4076 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 776.1 | 775.8 | -0.0% | -4.579 to +3.979 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.07083 | +30.8% | -0.008467 to +0.0418 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | -16.7% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.15 | 83.64 | +1.8% | -1.62 to +4.587 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.802 | -20.0% | -2.033 to -0.3626 | yes: GAIN |
| node-hours | 2.516 | 2.012 | -20.0% | -0.8555 to -0.1523 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.8 | -0.3% | -1.677 to +0.1989 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 233.2 | -14.1% | -64.95 to -11.79 | yes: GAIN |
| response time (ms), mean | 307.1 | 270.1 | -12.1% | -52.75 to -21.28 | yes: GAIN |
| response time (ms), 95th percentile | 1078 | 1083 | +0.5% | -51.82 to +62.53 | no |
| response time (ms), 99th percentile | 1531 | 1544 | +0.8% | -53.78 to +79.01 | no |
| time over the response line (% of samples) | 12.85 | 12.52 | -2.6% | -1.069 to +0.4067 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 6.2 | +1.6% | -0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.9 | +57.9 (native is 0) | +35.49 to +80.31 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.775 | 9.477 | -3.1% | -2.295 to +1.698 | no |
| utilisation (used / allocatable) | 0.05728 | 0.06955 | +21.4% | +0.002864 to +0.02169 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.375 | 1.327 | -3.4% | -0.08114 to -0.01311 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01691 | +0.0169 (native is 0) | +0.01543 to +0.01839 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.375 | 1.344 | -2.2% | -0.06413 to +0.003698 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.6 | 429.4 | -12.3% | -106 to -14.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.067 | +5.2% | -0.1312 to +0.3347 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.4 | 0.4 | +0.0% | -1.118 to +1.118 | no |
| pod start wait, mean (s) | 0.4 | 0.4 | +0.0% | -1.118 to +1.118 | no |
| host CPU busy, the real machine under kind (%) | 38.83 | 39.25 | +1.1% | -0.1469 to +0.9843 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 776.1 | 774.5 | -0.2% | -5.373 to +2.173 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.91 | -34.8% | -3.514 to -0.6659 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0625 | +15.4% | -0.0255 to +0.04217 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.3 | -50.0% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.15 | 80.5 | -2.0% | -3.415 to +0.1148 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.802 | -20.0% | -2.033 to -0.3626 | yes: GAIN |
| node-hours | 2.52 | 2.012 | -20.2% | -0.8576 to -0.1582 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 270.8 | -0.2% | -1.409 to +0.1566 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 233.2 | -14.1% | -64.48 to -12.04 | yes: GAIN |
| response time (ms), mean | 288.9 | 270.1 | -6.5% | -29.44 to -8.131 | yes: GAIN |
| response time (ms), 95th percentile | 1156 | 1083 | -6.3% | -202.7 to +57.35 | no |
| response time (ms), 99th percentile | 1714 | 1544 | -9.9% | -416 to +75.32 | no |
| time over the response line (% of samples) | 9.909 | 12.52 | +26.4% | +0.4362 to +4.792 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 6.2 | +6.9% | -0.5656 to +1.366 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.9 | +57.9 (native is 0) | +35.49 to +80.31 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.923 | 9.477 | -4.5% | -2.79 to +1.896 | no |
| utilisation (used / allocatable) | 0.05567 | 0.06955 | +24.9% | +0.004351 to +0.02342 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.336 | 1.327 | -0.6% | -0.03476 to +0.01779 | no |
| Omni's own CPU (cores), mean | 0 | 0.01691 | +0.0169 (native is 0) | +0.01543 to +0.01839 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.336 | 1.344 | +0.6% | -0.01761 to +0.03446 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 506.1 | 429.4 | -15.2% | -129.8 to -23.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.996 | 2.067 | +3.6% | -0.0975 to +0.2399 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.1 | 0.4 | +300.0% | -0.2889 to +0.8889 | no |
| pod start wait, mean (s) | 0.1 | 0.4 | +300.0% | -0.2889 to +0.8889 | no |
| host CPU busy, the real machine under kind (%) | 38.58 | 39.25 | +1.7% | +0.3114 to +1.024 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.8 | 774.5 | -0.2% | -4.772 to +2.172 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.91 | -34.8% | -3.514 to -0.6659 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0625 | -11.8% | -0.04497 to +0.0283 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.64 | 80.5 | -3.7% | -6.642 to +0.3752 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.046 | -15.9% | -1.56 to -0.3481 | yes: GAIN |
| node-hours | 2.516 | 2.112 | -16.0% | -0.6546 to -0.1516 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271 | -0.2% | -1.748 to +0.5934 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 241 | -11.3% | -49.57 to -11.6 | yes: GAIN |
| response time (ms), mean | 307.1 | 246 | -19.9% | -97.56 to -24.72 | yes: GAIN |
| response time (ms), 95th percentile | 1078 | 1210 | +12.3% | -45.49 to +311.3 | no |
| response time (ms), 99th percentile | 1531 | 1736 | +13.4% | -59.92 to +469 | no |
| time over the response line (% of samples) | 12.85 | 8.717 | -32.2% | -8.12 to -0.1546 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 6.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.5 | +44.5 (native is 0) | +33.59 to +55.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.775 | 11.01 | +12.6% | -1.11 to +3.58 | no |
| utilisation (used / allocatable) | 0.05728 | 0.06639 | +15.9% | +0.002795 to +0.01544 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.375 | 1.347 | -2.0% | -0.06082 to +0.004661 | no |
| Omni's own CPU (cores), mean | 0 | 0.01699 | +0.017 (native is 0) | +0.01547 to +0.01851 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.375 | 1.364 | -0.8% | -0.04421 to +0.02204 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.6 | 440.8 | -10.0% | -82.13 to -15.48 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.274 | +15.7% | -0.1354 to +0.7522 | no |
| pods started | 0.1 | 0.9 | +800.0% | -0.8101 to +2.41 | no |
| pod start wait, total (s) | 0.4 | 1.7 | +325.0% | -1.864 to +4.464 | no |
| pod start wait, mean (s) | 0.4 | 0.5857 | +46.4% | -1.056 to +1.427 | no |
| host CPU busy, the real machine under kind (%) | 38.83 | 39.63 | +2.1% | +0.3367 to +1.256 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 776.1 | 780.4 | +0.6% | +0.142 to +8.458 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.332 | -27.8% | -2.669 to -0.6675 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.075 | +38.5% | -0.01952 to +0.06119 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.2 | -66.7% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 82.15 | 87.6 | +6.6% | +0.7964 to +10.1 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*