# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.176 | 5.987 |
| node-hours | 2.513 | 2.513 | 2.17 | 2.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.6 | 270.8 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.6 | 244.9 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 240.5 | 133.8 | 204.7 | 97.92 |
| response time (ms), 95th percentile | 696.5 | 227.8 | 722.1 | 209.5 |
| response time (ms), 99th percentile | 1042 | 323.1 | 994.3 | 320.5 |
| time over the response line (% of samples) | 12.02 | 0.1842 | 11.65 | 0.2002 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 0 | 8.5 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 44.1 | 12.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.188 | 1030 | 7.633 | 1049 |
| utilisation (used / allocatable) | 0.05625 | 0.05959 | 0.06532 | 0.05926 |
| CPU used (cores), mean | 1.35 | 1.43 | 1.327 | 1.42 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01605 | 0.0121 |
| CPU used with Omni's own (cores), mean | 1.35 | 1.43 | 1.343 | 1.432 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 454.6 | 439.7 | 456.8 |
| HPA replicas, mean | 2.081 | 2.015 | 2.413 | 1.971 |
| pods started | 0 | 0.3 | 0.1 | 0 |
| pod start wait, total (s) | 0 | 0.6 | 0.1 | 0 |
| pod start wait, mean (s) | 0 | 0.4 | 0.1 | 0 |
| host CPU busy, the real machine under kind (%) | 38.35 | 43.67 | 39 | 44.24 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 737.1 | 1438 | 738.1 | 1429 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.608 | 5.857 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 144.5 | 0.03333 | 144.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 664.2 | 0.1 | 718 |
| queue: job turnaround, submitted to done, mean (s) | 45.09 | 789.6 | 45.49 | 785.1 |
| queue: jobs unfinished at the window's end | 0 | 9.4 | 0 | 8.5 |

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
| worker nodes in service, mean | 6 | 5.987 | -0.2% | -0.04167 to +0.01612 | no |
| node-hours | 2.513 | 2.511 | -0.1% | -0.01536 to +0.01198 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.9 | +0.1% | -0.351 to +0.9206 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 271.5 | -0.0% | -1.253 to +1.018 | no |
| response time (ms), mean | 133.8 | 97.92 | -26.8% | -43.82 to -27.93 | yes: GAIN |
| response time (ms), 95th percentile | 227.8 | 209.5 | -8.0% | -29.58 to -6.955 | yes: GAIN |
| response time (ms), 99th percentile | 323.1 | 320.5 | -0.8% | -28.49 to +23.45 | no |
| time over the response line (% of samples) | 0.1842 | 0.2002 | +8.7% | -0.1068 to +0.1388 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.9 | +12.9 (native is 0) | +10.68 to +15.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1030 | 1049 | +1.8% | -57.98 to +95.63 | no |
| utilisation (used / allocatable) | 0.05959 | 0.05926 | -0.5% | -0.00223 to +0.001585 | no |
| CPU used (cores), mean | 1.43 | 1.42 | -0.7% | -0.05624 to +0.03518 | no |
| Omni's own CPU (cores), mean | 0 | 0.0121 | +0.0121 (native is 0) | +0.01108 to +0.01312 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.432 | +0.1% | -0.04366 to +0.0468 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.6 | 456.8 | +0.5% | -11.79 to +16.22 | no |
| HPA replicas, mean | 2.015 | 1.971 | -2.2% | -0.2133 to +0.1262 | no |
| pods started | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| pod start wait, mean (s) | 0.4 | 0 | -100.0% | -1.003 to +0.2032 | no |
| host CPU busy, the real machine under kind (%) | 43.67 | 44.24 | +1.3% | -0.2851 to +1.431 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1438 | 1429 | -0.6% | -63.1 to +46.1 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.857 | -2.4% | -0.5974 to +0.3117 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 144.5 | 144.4 | -0.1% | -19.26 to +18.95 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 664.2 | 718 | +8.1% | -68.1 to +175.7 | no |
| queue: job turnaround, submitted to done, mean (s) | 789.6 | 785.1 | -0.6% | -76.62 to +67.7 | no |
| queue: jobs unfinished at the window's end | 9.4 | 8.5 | -9.6% | -2.387 to +0.5871 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.547e-15 to +1.259e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.513 | +0.0% | -0.007348 to +0.008014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.6 | +0.3% | -0.2147 to +1.962 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.6 | +0.3% | -0.2147 to +1.962 | no |
| response time (ms), mean | 240.5 | 133.8 | -44.4% | -155.7 to -57.65 | yes: GAIN |
| response time (ms), 95th percentile | 696.5 | 227.8 | -67.3% | -689 to -248.5 | yes: GAIN |
| response time (ms), 99th percentile | 1042 | 323.1 | -69.0% | -1035 to -402 | yes: GAIN |
| time over the response line (% of samples) | 12.02 | 0.1842 | -98.5% | -19.19 to -4.487 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 0 | -100.0% | -12.7 to -4.9 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.188 | 1030 | +12480.2% | +791.3 to +1252 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05625 | 0.05959 | +5.9% | +2.704e-05 to +0.006649 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.35 | 1.43 | +5.9% | +0.0006489 to +0.1596 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.35 | 1.43 | +5.9% | +0.0006489 to +0.1596 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 454.6 | -6.1% | -57.61 to -1.874 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.081 | 2.015 | -3.2% | -0.2895 to +0.1575 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.3656 to +1.566 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 38.35 | 43.67 | +13.9% | +3.712 to +6.921 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 737.1 | 1438 | +95.0% | +610 to +791 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 144.5 | +385277.8% | +109.1 to +179.9 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 664.2 | +221300.0% | +523.1 to +804.7 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 45.09 | 789.6 | +1651.1% | +603.4 to +885.6 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.4 | +9.4 (native is 0) | +3.461 to +15.34 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.176 | -13.7% | -1.622 to -0.02534 | yes: GAIN |
| node-hours | 2.513 | 2.17 | -13.6% | -0.6748 to -0.0107 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.8 | +0.0% | -0.5413 to +0.6708 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 244.9 | -9.6% | -51.01 to -0.7482 | yes: GAIN |
| response time (ms), mean | 240.5 | 204.7 | -14.9% | -48.14 to -23.35 | yes: GAIN |
| response time (ms), 95th percentile | 696.5 | 722.1 | +3.7% | -24.48 to +75.76 | no |
| response time (ms), 99th percentile | 1042 | 994.3 | -4.5% | -134.7 to +40.18 | no |
| time over the response line (% of samples) | 12.02 | 11.65 | -3.1% | -1.598 to +0.8492 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.5 | -3.4% | -1.058 to +0.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.1 | +44.1 (native is 0) | +28.69 to +59.51 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.188 | 7.633 | -6.8% | -1.697 to +0.5874 | no |
| utilisation (used / allocatable) | 0.05625 | 0.06532 | +16.1% | +0.0002544 to +0.01788 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.35 | 1.327 | -1.7% | -0.05467 to +0.008353 | no |
| Omni's own CPU (cores), mean | 0 | 0.01605 | +0.016 (native is 0) | +0.01495 to +0.01715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.35 | 1.343 | -0.5% | -0.03904 to +0.02482 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 439.7 | -9.2% | -86.67 to -2.656 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.081 | 2.413 | +16.0% | -0.05944 to +0.7241 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 38.35 | 39 | +1.7% | +0.3206 to +0.9675 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 737.1 | 738.1 | +0.1% | -0.7194 to +2.719 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.608 | -23.2% | -2.717 to -0.0671 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.03333 | -11.1% | -0.03026 to +0.02193 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.1 | -66.7% | -0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 45.09 | 45.49 | +0.9% | -1.779 to +2.579 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.176 | -13.7% | -1.622 to -0.02534 | yes: GAIN |
| node-hours | 2.513 | 2.17 | -13.7% | -0.6748 to -0.01134 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.8 | -0.3% | -1.976 to +0.3581 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 244.9 | -9.8% | -52.73 to -0.7729 | yes: GAIN |
| response time (ms), mean | 133.8 | 204.7 | +53.0% | +28.08 to +113.8 | yes: LOSS |
| response time (ms), 95th percentile | 227.8 | 722.1 | +217.1% | +277.2 to +711.5 | yes: LOSS |
| response time (ms), 99th percentile | 323.1 | 994.3 | +207.8% | +391.6 to +950.9 | yes: LOSS |
| time over the response line (% of samples) | 0.1842 | 11.65 | +6222.2% | +4.285 to +18.64 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.5 | +8.5 (native is 0) | +4.535 to +12.46 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.1 | +44.1 (native is 0) | +28.69 to +59.51 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1030 | 7.633 | -99.3% | -1253 to -792.4 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05959 | 0.06532 | +9.6% | -0.001054 to +0.01251 | no |
| CPU used (cores), mean | 1.43 | 1.327 | -7.2% | -0.2021 to -0.004402 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01605 | +0.016 (native is 0) | +0.01495 to +0.01715 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.343 | -6.1% | -0.1861 to +0.01166 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.6 | 439.7 | -3.3% | -39.32 to +9.47 | no |
| HPA replicas, mean | 2.015 | 2.413 | +19.8% | +0.07951 to +0.7172 | yes: power given |
| pods started | 0.3 | 0.1 | -66.7% | -0.7642 to +0.3642 | no |
| pod start wait, total (s) | 0.6 | 0.1 | -83.3% | -1.526 to +0.5256 | no |
| pod start wait, mean (s) | 0.4 | 0.1 | -75.0% | -0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 43.67 | 39 | -10.7% | -6.3 to -3.045 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1438 | 738.1 | -48.7% | -789.6 to -609.4 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.536 | -57.7% | -4.848 to -2.08 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 144.5 | 0.03333 | -100.0% | -179.9 to -109.1 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 664.2 | 0.1 | -100.0% | -804.9 to -523.3 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 789.6 | 45.49 | -94.2% | -885.1 to -603.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.4 | 0 | -100.0% | -15.34 to -3.461 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.987 | -0.2% | -0.04167 to +0.01612 | no |
| node-hours | 2.513 | 2.511 | -0.1% | -0.01545 to +0.01273 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.9 | +0.4% | -0.1791 to +2.496 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.5 | +0.3% | -0.702 to +2.215 | no |
| response time (ms), mean | 240.5 | 97.92 | -59.3% | -197.3 to -87.78 | yes: GAIN |
| response time (ms), 95th percentile | 696.5 | 209.5 | -69.9% | -709.5 to -264.5 | yes: GAIN |
| response time (ms), 99th percentile | 1042 | 320.5 | -69.2% | -1038 to -403.6 | yes: GAIN |
| time over the response line (% of samples) | 12.02 | 0.2002 | -98.3% | -19.15 to -4.486 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 0.2 | -97.7% | -12.4 to -4.797 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.9 | +12.9 (native is 0) | +10.68 to +15.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.188 | 1049 | +12710.1% | +813 to +1268 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05625 | 0.05926 | +5.4% | -0.0009646 to +0.006996 | no |
| CPU used (cores), mean | 1.35 | 1.42 | +5.2% | -0.02444 to +0.1636 | no |
| Omni's own CPU (cores), mean | 0 | 0.0121 | +0.0121 (native is 0) | +0.01108 to +0.01312 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.35 | 1.432 | +6.1% | -0.01137 to +0.1747 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.4 | 456.8 | -5.7% | -60.36 to +5.307 | no |
| HPA replicas, mean | 2.081 | 1.971 | -5.3% | -0.2395 to +0.0205 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 38.35 | 44.24 | +15.4% | +4.113 to +7.666 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 737.1 | 1429 | +93.9% | +605.6 to +778.4 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.857 | -2.4% | -0.5974 to +0.3117 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 144.4 | +384866.7% | +107.7 to +181 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 718 | +239233.3% | +536.8 to +898.6 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 45.09 | 785.1 | +1641.2% | +605.1 to +875 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.5 | +8.5 (native is 0) | +3.123 to +13.88 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*