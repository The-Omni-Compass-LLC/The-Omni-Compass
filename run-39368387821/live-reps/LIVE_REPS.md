# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.128 | 5.323 |
| node-hours | 2.518 | 2.512 | 2.151 | 2.228 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.7 | 272.2 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.7 | 244.7 | 250.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 307 | 329.3 | 271.9 | 280.9 |
| response time (ms), 95th percentile | 1006 | 1134 | 1044 | 1101 |
| response time (ms), 99th percentile | 1451 | 1643 | 1597 | 1605 |
| time over the response line (% of samples) | 14.95 | 15.73 | 14.03 | 14.59 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.8 | 7.7 | 8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 46.1 | 42 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 66.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.413 | 9.37 | 10.85 | 9.505 |
| utilisation (used / allocatable) | 0.0588 | 0.05914 | 0.0686 | 0.06654 |
| CPU used (cores), mean | 1.411 | 1.419 | 1.401 | 1.404 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01696 | 0.01752 |
| CPU used with Omni's own (cores), mean | 1.411 | 1.419 | 1.418 | 1.422 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.6 | 466.4 | 419.4 | 430.3 |
| HPA replicas, mean | 1.972 | 1.984 | 1.988 | 2.04 |
| pods started | 0 | 0.1 | 0.1 | 0.1 |
| pod start wait, total (s) | 0 | 0.4 | 0 | 0.1 |
| pod start wait, mean (s) | 0 | 0.4 | 0 | 0.1 |
| host CPU busy, the real machine under kind (%) | 40.1 | 41.07 | 41.1 | 41.77 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 768.1 | 775.1 | 771.6 | 775.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.38 | 4.717 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.1625 | 0.04167 | 0.1667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1 | 0.3 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 73.89 | 82.38 | 79.93 | 83.16 |
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
| worker nodes in service, mean | 6 | 5.323 | -11.3% | -1.292 to -0.06233 | yes: GAIN |
| node-hours | 2.512 | 2.228 | -11.3% | -0.5422 to -0.02478 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 | -0.0% | -1.128 to +1.029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 250.4 | -7.8% | -40.87 to -1.782 | yes: GAIN |
| response time (ms), mean | 329.3 | 280.9 | -14.7% | -66.54 to -30.26 | yes: GAIN |
| response time (ms), 95th percentile | 1134 | 1101 | -2.9% | -106.8 to +40.55 | no |
| response time (ms), 99th percentile | 1643 | 1605 | -2.3% | -107.9 to +32.54 | no |
| time over the response line (% of samples) | 15.73 | 14.59 | -7.2% | -2.105 to -0.1585 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8 | +2.6% | -0.6793 to +1.079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 | +42 (native is 0) | +34.37 to +49.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.37 | 9.505 | +1.4% | -0.7357 to +1.006 | no |
| utilisation (used / allocatable) | 0.05914 | 0.06654 | +12.5% | +0.0001801 to +0.01462 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.404 | -1.1% | -0.03328 to +0.003455 | no |
| Omni's own CPU (cores), mean | 0 | 0.01752 | +0.0175 (native is 0) | +0.01459 to +0.02045 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.422 | +0.2% | -0.01577 to +0.02099 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.4 | 430.3 | -7.7% | -73.43 to +1.211 | no |
| HPA replicas, mean | 1.984 | 2.04 | +2.8% | -0.05829 to +0.1705 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.4 | 0.1 | -75.0% | -1.257 to +0.6567 | no |
| pod start wait, mean (s) | 0.4 | 0.1 | -75.0% | -1.257 to +0.6567 | no |
| host CPU busy, the real machine under kind (%) | 41.07 | 41.77 | +1.7% | +0.3586 to +1.028 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.1 | 775.8 | +0.1% | -4.392 to +5.792 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.717 | -21.4% | -2.402 to -0.1642 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.1667 | +2.6% | -0.1219 to +0.1302 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.6 | -40.0% | -0.9001 to +0.1001 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.38 | 83.16 | +0.9% | -4.457 to +6.007 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.512 | -0.2% | -0.01487 to +0.002872 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.7 | -0.3% | -1.633 to +0.2462 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.7 | -0.3% | -1.633 to +0.2462 | no |
| response time (ms), mean | 307 | 329.3 | +7.3% | +0.04828 to +44.56 | yes: LOSS |
| response time (ms), 95th percentile | 1006 | 1134 | +12.8% | +3.334 to +253.7 | yes: LOSS |
| response time (ms), 99th percentile | 1451 | 1643 | +13.2% | -18.15 to +402.4 | no |
| time over the response line (% of samples) | 14.95 | 15.73 | +5.2% | -0.0272 to +1.575 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.8 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.413 | 9.37 | -0.5% | -1.36 to +1.274 | no |
| utilisation (used / allocatable) | 0.0588 | 0.05914 | +0.6% | -0.0008242 to +0.001507 | no |
| CPU used (cores), mean | 1.411 | 1.419 | +0.6% | -0.01978 to +0.03617 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.411 | 1.419 | +0.6% | -0.01978 to +0.03617 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.6 | 466.4 | -0.3% | -12.37 to +9.918 | no |
| HPA replicas, mean | 1.972 | 1.984 | +0.6% | -0.08626 to +0.1094 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| host CPU busy, the real machine under kind (%) | 40.1 | 41.07 | +2.4% | +0.4535 to +1.492 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768.1 | 775.1 | +0.9% | -0.8648 to +14.86 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.1625 | +178.6% | +0.04415 to +0.1642 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1 | +233.3% | +0.3545 to +1.046 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 73.89 | 82.38 | +11.5% | +0.1891 to +16.79 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.128 | -14.5% | -1.512 to -0.2324 | yes: GAIN |
| node-hours | 2.518 | 2.151 | -14.6% | -0.6319 to -0.1018 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.2 | -0.1% | -0.9246 to +0.4848 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 244.7 | -10.2% | -47.66 to -7.659 | yes: GAIN |
| response time (ms), mean | 307 | 271.9 | -11.4% | -44.99 to -25.26 | yes: GAIN |
| response time (ms), 95th percentile | 1006 | 1044 | +3.8% | -21.66 to +98.55 | no |
| response time (ms), 99th percentile | 1451 | 1597 | +10.1% | -24.81 to +318.6 | no |
| time over the response line (% of samples) | 14.95 | 14.03 | -6.1% | -1.925 to +0.08936 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.7 | -1.3% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.1 | +46.1 (native is 0) | +34.95 to +57.25 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.413 | 10.85 | +15.3% | -0.5107 to +3.384 | no |
| utilisation (used / allocatable) | 0.0588 | 0.0686 | +16.7% | +0.002843 to +0.01675 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.401 | -0.7% | -0.03799 to +0.01692 | no |
| Omni's own CPU (cores), mean | 0 | 0.01696 | +0.017 (native is 0) | +0.01582 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.418 | +0.5% | -0.0212 to +0.03405 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.6 | 419.4 | -10.3% | -81.17 to -15.25 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.972 | 1.988 | +0.8% | -0.1343 to +0.1652 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 40.1 | 41.1 | +2.5% | +0.5561 to +1.448 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768.1 | 771.6 | +0.5% | -0.4934 to +7.493 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.38 | -27.0% | -2.768 to -0.4723 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.04167 | -28.6% | -0.05928 to +0.02595 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.89 | 79.93 | +8.2% | +0.1596 to +11.92 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.128 | -14.5% | -1.512 to -0.2324 | yes: GAIN |
| node-hours | 2.512 | 2.151 | -14.4% | -0.6336 to -0.0881 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.2 | +0.2% | -0.4842 to +1.431 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 244.7 | -9.9% | -47.67 to -6.254 | yes: GAIN |
| response time (ms), mean | 329.3 | 271.9 | -17.4% | -86.19 to -28.67 | yes: GAIN |
| response time (ms), 95th percentile | 1134 | 1044 | -7.9% | -230.1 to +49.95 | no |
| response time (ms), 99th percentile | 1643 | 1597 | -2.8% | -210.7 to +120.2 | no |
| time over the response line (% of samples) | 15.73 | 14.03 | -10.8% | -3.147 to -0.2367 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.7 | -1.3% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.1 | +46.1 (native is 0) | +34.95 to +57.25 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.37 | 10.85 | +15.8% | +0.03899 to +2.921 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05914 | 0.0686 | +16.0% | +0.002185 to +0.01672 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.401 | -1.3% | -0.05121 to +0.01375 | no |
| Omni's own CPU (cores), mean | 0 | 0.01696 | +0.017 (native is 0) | +0.01582 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.418 | -0.1% | -0.03383 to +0.03028 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.4 | 419.4 | -10.1% | -83.4 to -10.57 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.984 | 1.988 | +0.2% | -0.1314 to +0.1392 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.4 | 0 | -100.0% | -1.305 to +0.5048 | no |
| pod start wait, mean (s) | 0.4 | 0 | -100.0% | -1.305 to +0.5048 | no |
| host CPU busy, the real machine under kind (%) | 41.07 | 41.1 | +0.1% | -0.3824 to +0.4407 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.1 | 771.6 | -0.5% | -10.07 to +3.067 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.38 | -27.0% | -2.768 to -0.4723 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.04167 | -74.4% | -0.1617 to -0.07999 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.3 | -70.0% | -1.046 to -0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 82.38 | 79.93 | -3.0% | -9.773 to +4.865 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.323 | -11.3% | -1.292 to -0.06233 | yes: GAIN |
| node-hours | 2.518 | 2.228 | -11.5% | -0.5425 to -0.03645 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.6 | -0.3% | -1.445 to -0.04082 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 250.4 | -8.1% | -41.11 to -2.927 | yes: GAIN |
| response time (ms), mean | 307 | 280.9 | -8.5% | -33.46 to -18.72 | yes: GAIN |
| response time (ms), 95th percentile | 1006 | 1101 | +9.5% | +19.12 to +171.6 | yes: LOSS |
| response time (ms), 99th percentile | 1451 | 1605 | +10.6% | -9.966 to +318.9 | no |
| time over the response line (% of samples) | 14.95 | 14.59 | -2.4% | -0.9737 to +0.2588 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8 | +2.6% | -0.4573 to +0.8573 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 | +42 (native is 0) | +34.37 to +49.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.413 | 9.505 | +1.0% | -1.433 to +1.616 | no |
| utilisation (used / allocatable) | 0.0588 | 0.06654 | +13.2% | +0.001103 to +0.01438 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.404 | -0.5% | -0.03498 to +0.02155 | no |
| Omni's own CPU (cores), mean | 0 | 0.01752 | +0.0175 (native is 0) | +0.01459 to +0.02045 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.422 | +0.8% | -0.01761 to +0.03921 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.6 | 430.3 | -8.0% | -69.35 to -5.319 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.972 | 2.04 | +3.4% | -0.07064 to +0.206 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 40.1 | 41.77 | +4.2% | +1.248 to +2.084 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768.1 | 775.8 | +1.0% | +2.541 to +12.86 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.717 | -21.4% | -2.402 to -0.1642 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.1667 | +185.7% | -0.02803 to +0.2447 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.89 | 83.16 | +12.5% | +2.4 to +16.13 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*