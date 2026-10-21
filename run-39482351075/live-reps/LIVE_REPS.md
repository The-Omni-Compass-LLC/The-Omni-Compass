# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.26 | 7.16 |
| node-hours | 5.033 | 5.018 | 4.709 | 2.997 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 503.9 | 525.4 | 504.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 503.9 | 502.2 | 352.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 684 | 137.3 | 669.1 | 80 |
| response time (ms), 95th percentile | 2697 | 186.5 | 2871 | 104.3 |
| response time (ms), 99th percentile | 3778 | 207.1 | 4014 | 151.1 |
| time over the response line (% of samples) | 27.28 | 0 | 27.76 | 0.003597 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 0 | 14 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.2 | 25.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 0 | 26.96 | 0.05333 |
| utilisation (used / allocatable) | 0.03591 | 0.006467 | 0.03779 | 0.00942 |
| CPU used (cores), mean | 1.724 | 0.3104 | 1.696 | 0.2704 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01249 | 0.00954 |
| CPU used with Omni's own (cores), mean | 1.724 | 0.3104 | 1.709 | 0.2799 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.4 | 3912 | 711.6 | 3150 |
| HPA replicas, mean | 4.068 | 4.056 | 4.374 | 4.34 |
| pods started | 0.1 | 0 | 1.2 | 1.4 |
| pod start wait, total (s) | 0.3 | 0 | 2.3 | 2.3 |
| pod start wait, mean (s) | 0.3 | 0 | 1.083 | 1.4 |
| host CPU busy, the real machine under kind (%) | 52.66 | 15.13 | 54.8 | 16.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 892.4 | 1503 | 912.5 | 1505 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.71 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1157 | 0.1167 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1473 | 0.9 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 203.2 | 1157 | 221.3 | 1158 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 7.16 | -40.3% | -5.184 to -4.496 | yes: GAIN |
| node-hours | 5.018 | 2.997 | -40.3% | -2.17 to -1.872 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 503.9 | 504.6 | +0.1% | -0.2676 to +1.567 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.9 | 352.6 | -30.0% | -162.7 to -140 | yes: GAIN |
| response time (ms), mean | 137.3 | 80 | -41.7% | -62.85 to -51.82 | yes: GAIN |
| response time (ms), 95th percentile | 186.5 | 104.3 | -44.1% | -89.44 to -74.94 | yes: GAIN |
| response time (ms), 99th percentile | 207.1 | 151.1 | -27.1% | -70.06 to -42 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.003597 | +0.0036 (native is 0) | -0.00454 to +0.01173 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.5 | +25.5 (native is 0) | +23.98 to +27.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05333 | +0.0533 (native is 0) | -0.06731 to +0.174 | no |
| utilisation (used / allocatable) | 0.006467 | 0.00942 | +45.7% | +0.002706 to +0.003201 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3104 | 0.2704 | -12.9% | -0.04691 to -0.03314 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00954 | +0.00954 (native is 0) | +0.008604 to +0.01048 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3104 | 0.2799 | -9.8% | -0.03778 to -0.02319 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3912 | 3150 | -19.5% | -833.7 to -689.2 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.056 | 4.34 | +7.0% | +0.04501 to +0.5224 | yes: power given |
| pods started | 0 | 1.4 | +1.4 (native is 0) | +0.7968 to +2.003 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.3 (native is 0) | +1.036 to +3.564 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.4 | +1.4 (native is 0) | +0.9291 to +1.871 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.13 | 16.38 | +8.2% | +0.8441 to +1.651 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 1505 | +0.1% | -1.439 to +4.639 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1157 | 1158 | +0.1% | -1.676 to +4.485 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1473 | 1474 | +0.1% | -1.632 to +4.632 | no |
| queue: job turnaround, submitted to done, mean (s) | 1157 | 1158 | +0.1% | -1.676 to +4.485 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -6.362e-15 to -7.432e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.033 | 5.018 | -0.3% | -0.03034 to +0.0003396 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 503.9 | -4.4% | -26.32 to -20.15 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 503.9 | -4.4% | -26.32 to -20.15 | yes: GAIN |
| response time (ms), mean | 684 | 137.3 | -79.9% | -799.3 to -294.1 | yes: GAIN |
| response time (ms), 95th percentile | 2697 | 186.5 | -93.1% | -3650 to -1371 | yes: GAIN |
| response time (ms), 99th percentile | 3778 | 207.1 | -94.5% | -5111 to -2029 | yes: GAIN |
| time over the response line (% of samples) | 27.28 | 0 | -100.0% | -37.5 to -17.07 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 0 | -100.0% | -17.37 to -8.629 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 0 | -100.0% | -20.17 to -10.05 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03591 | 0.006467 | -82.0% | -0.03289 to -0.02599 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.724 | 0.3104 | -82.0% | -1.579 to -1.247 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.724 | 0.3104 | -82.0% | -1.579 to -1.247 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.4 | 3912 | +425.5% | +2977 to +3358 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.068 | 4.056 | -0.3% | -0.1278 to +0.104 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 52.66 | 15.13 | -71.3% | -42.05 to -33.01 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 892.4 | 1503 | +68.4% | +520.3 to +701.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1157 | +1632935.3% | +1154 to +1159 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1473 | +245383.3% | +1470 to +1475 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 203.2 | 1157 | +469.3% | +864.5 to +1043 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.26 | -6.2% | -1.874 to +0.3915 | no |
| node-hours | 5.033 | 4.709 | -6.4% | -0.8018 to +0.1541 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 525.4 | -0.3% | -4.201 to +0.6736 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 502.2 | -4.7% | -61.01 to +11.05 | no |
| response time (ms), mean | 684 | 669.1 | -2.2% | -47.48 to +17.56 | no |
| response time (ms), 95th percentile | 2697 | 2871 | +6.5% | -101.3 to +449.3 | no |
| response time (ms), 99th percentile | 3778 | 4014 | +6.3% | -220.5 to +692.8 | no |
| time over the response line (% of samples) | 27.28 | 27.76 | +1.7% | -0.722 to +1.671 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 14 | +7.7% | -0.306 to +2.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.2 | +49.2 (native is 0) | +25.32 to +73.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 26.96 | +78.5% | -3.198 to +26.9 | no |
| utilisation (used / allocatable) | 0.03591 | 0.03779 | +5.2% | -0.002294 to +0.006062 | no |
| CPU used (cores), mean | 1.724 | 1.696 | -1.6% | -0.1183 to +0.06389 | no |
| Omni's own CPU (cores), mean | 0 | 0.01249 | +0.0125 (native is 0) | +0.01167 to +0.01331 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.724 | 1.709 | -0.9% | -0.1055 to +0.07613 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.4 | 711.6 | -4.4% | -98.64 to +33.01 | no |
| HPA replicas, mean | 4.068 | 4.374 | +7.5% | +0.1067 to +0.5052 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.3128 to +1.887 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.3 | +666.7% | +0.4548 to +3.545 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.083 | +261.1% | +0.1574 to +1.409 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.66 | 54.8 | +4.1% | +1.653 to +2.631 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 892.4 | 912.5 | +2.3% | +8.623 to +31.58 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.71 | -10.7% | -3.136 to +0.5622 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.1167 | +64.7% | +0.01303 to +0.07863 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 203.2 | 221.3 | +8.9% | +9.876 to +26.28 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.26 | -6.2% | -1.874 to +0.3915 | no |
| node-hours | 5.018 | 4.709 | -6.2% | -0.7882 to +0.1705 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 503.9 | 525.4 | +4.3% | +18.61 to +24.33 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.9 | 502.2 | -0.3% | -39.77 to +36.28 | no |
| response time (ms), mean | 137.3 | 669.1 | +387.2% | +290.6 to +772.9 | yes: LOSS |
| response time (ms), 95th percentile | 186.5 | 2871 | +1439.3% | +1580 to +3789 | yes: LOSS |
| response time (ms), 99th percentile | 207.1 | 4014 | +1837.8% | +2326 to +5287 | yes: LOSS |
| time over the response line (% of samples) | 0 | 27.76 | +27.8 (native is 0) | +17.87 to +37.65 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14 | +14 (native is 0) | +10.07 to +17.93 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.2 | +49.2 (native is 0) | +25.32 to +73.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 26.96 | +27 (native is 0) | +7.469 to +46.45 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006467 | 0.03779 | +484.4% | +0.02964 to +0.03301 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3104 | 1.696 | +446.5% | +1.237 to +1.535 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01249 | +0.0125 (native is 0) | +0.01167 to +0.01331 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3104 | 1.709 | +450.6% | +1.25 to +1.547 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3912 | 711.6 | -81.8% | -3442 to -2958 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.056 | 4.374 | +7.8% | +0.09083 to +0.5449 | yes: power given |
| pods started | 0 | 1.2 | +1.2 (native is 0) | +0.3207 to +2.079 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.3 (native is 0) | +0.2475 to +4.352 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.083 | +1.08 (native is 0) | +0.3184 to +1.848 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.13 | 54.8 | +262.2% | +35.13 to +44.22 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1503 | 912.5 | -39.3% | -685.8 to -495.6 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1157 | 0.1167 | -100.0% | -1159 to -1154 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1473 | 0.9 | -99.9% | -1474 to -1470 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1157 | 221.3 | -80.9% | -1030 to -841.2 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.16 | -40.3% | -5.184 to -4.496 | yes: GAIN |
| node-hours | 5.033 | 2.997 | -40.5% | -2.182 to -1.891 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 504.6 | -4.3% | -25.25 to -19.92 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 352.6 | -33.1% | -184.4 to -164.7 | yes: GAIN |
| response time (ms), mean | 684 | 80 | -88.3% | -861.5 to -346.6 | yes: GAIN |
| response time (ms), 95th percentile | 2697 | 104.3 | -96.1% | -3733 to -1453 | yes: GAIN |
| response time (ms), 99th percentile | 3778 | 151.1 | -96.0% | -5162 to -2091 | yes: GAIN |
| time over the response line (% of samples) | 27.28 | 0.003597 | -100.0% | -37.5 to -17.07 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 0 | -100.0% | -17.37 to -8.629 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.5 | +25.5 (native is 0) | +23.98 to +27.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.11 | 0.05333 | -99.6% | -20.1 to -10.01 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03591 | 0.00942 | -73.8% | -0.02981 to -0.02317 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.724 | 0.2704 | -84.3% | -1.616 to -1.291 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00954 | +0.00954 (native is 0) | +0.008604 to +0.01048 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.724 | 0.2799 | -83.8% | -1.605 to -1.282 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.4 | 3150 | +323.2% | +2249 to +2563 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.068 | 4.34 | +6.7% | +0.1039 to +0.4396 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.6214 to +1.979 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.3 | +666.7% | +0.5302 to +3.47 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.4 | +366.7% | +0.4089 to +1.791 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.66 | 16.38 | -68.9% | -40.5 to -32.06 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 892.4 | 1505 | +68.6% | +523.2 to +701.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1158 | +1634917.6% | +1155 to +1161 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1474 | +245633.3% | +1470 to +1477 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 203.2 | 1158 | +469.9% | +867.4 to +1043 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*