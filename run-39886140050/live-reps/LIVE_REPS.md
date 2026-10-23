# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.383 | 5.983 |
| node-hours | 2.512 | 2.519 | 2.256 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 272.8 | 271.9 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 272.8 | 252.5 | 270.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 304.3 | 140.6 | 276.8 | 111.7 |
| response time (ms), 95th percentile | 1008 | 249.5 | 1060 | 244.5 |
| response time (ms), 99th percentile | 1386 | 356.1 | 1520 | 363.7 |
| time over the response line (% of samples) | 17.58 | 0.1699 | 17.76 | 0.3745 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 0 | 10.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 124.1 | 30.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.09 | 1125 | 11.08 | 1254 |
| utilisation (used / allocatable) | 0.05798 | 0.06014 | 0.0652 | 0.05764 |
| CPU used (cores), mean | 1.391 | 1.443 | 1.398 | 1.379 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04989 | 0.04672 |
| CPU used with Omni's own (cores), mean | 1.391 | 1.443 | 1.448 | 1.426 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.5 | 450.6 | 432.9 | 468.6 |
| HPA replicas, mean | 1.994 | 2.016 | 2.639 | 2.009 |
| pods started | 0 | 0 | 0.9 | 0.1 |
| pod start wait, total (s) | 0 | 0 | 1.6 | 0.2 |
| pod start wait, mean (s) | 0 | 0 | 0.725 | 0.2 |
| host CPU busy, the real machine under kind (%) | 40.06 | 44.95 | 42.22 | 45.4 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 751.9 | 1460 | 757.5 | 1478 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.791 | 5.529 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 164.5 | 0.0375 | 160.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 723.9 | 0.2 | 802.8 |
| queue: job turnaround, submitted to done, mean (s) | 62.1 | 839.3 | 65.99 | 884.6 |
| queue: jobs unfinished at the window's end | 0 | 10.7 | 0 | 13.9 |

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
| worker nodes in service, mean | 6 | 5.983 | -0.3% | -0.05563 to +0.02152 | no |
| node-hours | 2.519 | 2.508 | -0.4% | -0.03035 to +0.007736 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 271.4 | -0.5% | -2.637 to -0.1637 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 270.9 | -0.7% | -3.675 to -0.1969 | yes: GAIN |
| response time (ms), mean | 140.6 | 111.7 | -20.6% | -38.15 to -19.67 | yes: GAIN |
| response time (ms), 95th percentile | 249.5 | 244.5 | -2.0% | -13.25 to +3.212 | no |
| response time (ms), 99th percentile | 356.1 | 363.7 | +2.1% | -13.62 to +28.83 | no |
| time over the response line (% of samples) | 0.1699 | 0.3745 | +120.5% | +0.02611 to +0.3832 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.5 (native is 0) | +20.14 to +40.86 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1125 | 1254 | +11.4% | +57.5 to +198.9 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06014 | 0.05764 | -4.2% | -0.003964 to -0.001034 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.379 | -4.4% | -0.09662 to -0.03093 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04672 | +0.0467 (native is 0) | +0.04186 to +0.05158 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.426 | -1.2% | -0.04944 to +0.01533 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.6 | 468.6 | +4.0% | +8.102 to +27.91 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.009 | -0.4% | -0.0969 to +0.08252 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.95 | 45.4 | +1.0% | -0.2388 to +1.154 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1460 | 1478 | +1.3% | -22.02 to +59.22 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.529 | -7.8% | -6.45 to +5.509 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 164.5 | 160.8 | -2.2% | -33.09 to +25.71 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 723.9 | 802.8 | +10.9% | -57.98 to +215.8 | no |
| queue: job turnaround, submitted to done, mean (s) | 839.3 | 884.6 | +5.4% | -12.34 to +102.9 | no |
| queue: jobs unfinished at the window's end | 10.7 | 13.9 | +29.9% | +0.169 to +6.231 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.057e-15 to +8.793e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.519 | +0.3% | -0.001975 to +0.01698 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 272.8 | +0.5% | -0.04428 to +2.841 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 272.8 | +0.5% | -0.04428 to +2.841 | no |
| response time (ms), mean | 304.3 | 140.6 | -53.8% | -236 to -91.34 | yes: GAIN |
| response time (ms), 95th percentile | 1008 | 249.5 | -75.2% | -1101 to -415.3 | yes: GAIN |
| response time (ms), 99th percentile | 1386 | 356.1 | -74.3% | -1495 to -564.9 | yes: GAIN |
| time over the response line (% of samples) | 17.58 | 0.1699 | -99.0% | -25.77 to -9.046 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 0 | -100.0% | -13.73 to -5.667 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.09 | 1125 | +11050.6% | +884.3 to +1346 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05798 | 0.06014 | +3.7% | -0.002462 to +0.006775 | no |
| CPU used (cores), mean | 1.391 | 1.443 | +3.7% | -0.05908 to +0.1626 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.391 | 1.443 | +3.7% | -0.05908 to +0.1626 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.5 | 450.6 | -4.8% | -63.1 to +17.26 | no |
| HPA replicas, mean | 1.994 | 2.016 | +1.1% | -0.08027 to +0.1245 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 40.06 | 44.95 | +12.2% | +2.851 to +6.927 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 751.9 | 1460 | +94.1% | +637.1 to +778.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 164.5 | +246700.0% | +129.3 to +199.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 723.9 | +144680.0% | +568.5 to +878.3 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 62.1 | 839.3 | +1251.5% | +642.6 to +911.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.7 | +10.7 (native is 0) | +5.252 to +16.15 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.383 | -10.3% | -1.217 to -0.01707 | yes: GAIN |
| node-hours | 2.512 | 2.256 | -10.2% | -0.5073 to -0.004851 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.9 | +0.2% | -0.2886 to +1.195 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 252.5 | -7.0% | -37.83 to -0.04251 | yes: GAIN |
| response time (ms), mean | 304.3 | 276.8 | -9.0% | -50.37 to -4.558 | yes: GAIN |
| response time (ms), 95th percentile | 1008 | 1060 | +5.2% | -62.77 to +167.7 | no |
| response time (ms), 99th percentile | 1386 | 1520 | +9.7% | -23.56 to +291.1 | no |
| time over the response line (% of samples) | 17.58 | 17.76 | +1.0% | -1.148 to +1.503 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.1 | +4.1% | -0.2911 to +1.091 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.1 | +124 (native is 0) | +62.44 to +185.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.09 | 11.08 | +9.7% | -0.7872 to +2.754 | no |
| utilisation (used / allocatable) | 0.05798 | 0.0652 | +12.5% | +0.0006146 to +0.01384 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.391 | 1.398 | +0.5% | -0.00625 to +0.01923 | no |
| Omni's own CPU (cores), mean | 0 | 0.04989 | +0.0499 (native is 0) | +0.04411 to +0.05567 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.391 | 1.448 | +4.1% | +0.03951 to +0.07326 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.5 | 432.9 | -8.6% | -78.41 to -2.77 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.994 | 2.639 | +32.3% | +0.3073 to +0.982 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | -0.02037 to +1.82 | no |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | -0.4566 to +3.657 | no |
| pod start wait, mean (s) | 0 | 0.725 | +0.725 (native is 0) | +0.103 to +1.347 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.06 | 42.22 | +5.4% | +1.725 to +2.598 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 751.9 | 757.5 | +0.7% | -0.1145 to +11.31 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.791 | -20.2% | -2.372 to -0.04644 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.0375 | -43.7% | -0.05744 to -0.0008917 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | -60.0% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.1 | 65.99 | +6.3% | -2.785 to +10.57 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.383 | -10.3% | -1.217 to -0.01707 | yes: GAIN |
| node-hours | 2.519 | 2.256 | -10.5% | -0.5098 to -0.0173 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 271.9 | -0.3% | -2.28 to +0.3898 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 252.5 | -7.5% | -40.08 to -0.591 | yes: GAIN |
| response time (ms), mean | 140.6 | 276.8 | +96.9% | +72.01 to +200.4 | yes: LOSS |
| response time (ms), 95th percentile | 249.5 | 1060 | +324.9% | +480.6 to +1141 | yes: LOSS |
| response time (ms), 99th percentile | 356.1 | 1520 | +326.8% | +686.5 to +1641 | yes: LOSS |
| time over the response line (% of samples) | 0.1699 | 17.76 | +10353.2% | +9.485 to +25.69 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.1 | +10.1 (native is 0) | +6.399 to +13.8 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.1 | +124 (native is 0) | +62.44 to +185.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1125 | 11.08 | -99.0% | -1345 to -884.1 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06014 | 0.0652 | +8.4% | +0.002266 to +0.007872 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.398 | -3.1% | -0.163 to +0.07251 | no |
| Omni's own CPU (cores), mean | 0 | 0.04989 | +0.0499 (native is 0) | +0.04411 to +0.05567 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.448 | +0.3% | -0.1167 to +0.126 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.6 | 432.9 | -3.9% | -28.74 to -6.609 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.639 | +30.9% | +0.327 to +0.9179 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | -0.02037 to +1.82 | no |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | -0.4566 to +3.657 | no |
| pod start wait, mean (s) | 0 | 0.725 | +0.725 (native is 0) | +0.103 to +1.347 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.95 | 42.22 | -6.1% | -4.799 to -0.6551 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1460 | 757.5 | -48.1% | -771.5 to -633.1 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.612 | -56.5% | -4.944 to -1.832 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 164.5 | 0.0375 | -100.0% | -199.7 to -129.3 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 723.9 | 0.2 | -100.0% | -878.7 to -568.7 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 839.3 | 65.99 | -92.1% | -905.7 to -640.9 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.7 | 0 | -100.0% | -16.15 to -5.252 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.983 | -0.3% | -0.05563 to +0.02152 | no |
| node-hours | 2.512 | 2.508 | -0.2% | -0.02134 to +0.01373 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.4 | -0.0% | -1.894 to +1.89 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 270.9 | -0.2% | -2.357 to +1.282 | no |
| response time (ms), mean | 304.3 | 111.7 | -63.3% | -272.2 to -113 | yes: GAIN |
| response time (ms), 95th percentile | 1008 | 244.5 | -75.7% | -1106 to -420.7 | yes: GAIN |
| response time (ms), 99th percentile | 1386 | 363.7 | -73.8% | -1482 to -563.2 | yes: GAIN |
| time over the response line (% of samples) | 17.58 | 0.3745 | -97.9% | -25.48 to -8.923 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 0.1 | -99.0% | -13.59 to -5.607 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.5 (native is 0) | +20.14 to +40.86 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.09 | 1254 | +12320.8% | +1017 to +1470 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05798 | 0.05764 | -0.6% | -0.00573 to +0.005045 | no |
| CPU used (cores), mean | 1.391 | 1.379 | -0.9% | -0.1371 to +0.1131 | no |
| Omni's own CPU (cores), mean | 0 | 0.04672 | +0.0467 (native is 0) | +0.04186 to +0.05158 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.391 | 1.426 | +2.5% | -0.08693 to +0.1563 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.5 | 468.6 | -1.0% | -50.15 to +40.33 | no |
| HPA replicas, mean | 1.994 | 2.009 | +0.7% | -0.08383 to +0.1137 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.06 | 45.4 | +13.3% | +3.161 to +7.531 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 751.9 | 1478 | +96.6% | +667.2 to +785.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.529 | -7.8% | -6.45 to +5.509 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 160.8 | +241162.5% | +124 to +197.5 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 802.8 | +160460.0% | +631.6 to +973 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 62.1 | 884.6 | +1324.4% | +701.2 to +943.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.9 | +13.9 (native is 0) | +8.416 to +19.38 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*