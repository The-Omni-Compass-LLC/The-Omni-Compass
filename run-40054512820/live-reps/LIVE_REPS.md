# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.939 | 4.698 |
| node-hours | 2.517 | 2.514 | 2.067 | 1.967 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.4 | 271.3 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.4 | 238 | 230.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 295.2 | 219.6 | 260.1 | 192.7 |
| response time (ms), 95th percentile | 959.4 | 529.7 | 978.7 | 613.7 |
| response time (ms), 99th percentile | 1413 | 914.9 | 1454 | 1163 |
| time over the response line (% of samples) | 14.71 | 8.117 | 14.59 | 7.84 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 6.6 | 7.6 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.4 | 48.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.25 | 14.04 | 10.63 | 13.73 |
| utilisation (used / allocatable) | 0.05776 | 0.05746 | 0.07064 | 0.07431 |
| CPU used (cores), mean | 1.386 | 1.379 | 1.38 | 1.366 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01596 | 0.01779 |
| CPU used with Omni's own (cores), mean | 1.386 | 1.379 | 1.396 | 1.384 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.7 | 481.2 | 413.1 | 402.9 |
| HPA replicas, mean | 2.001 | 2 | 2.161 | 2.227 |
| pods started | 0 | 0.1 | 0.4 | 0.2 |
| pod start wait, total (s) | 0 | 0.2 | 0.6 | 0.7 |
| pod start wait, mean (s) | 0 | 0.2 | 0.4 | 0.35 |
| host CPU busy, the real machine under kind (%) | 39.63 | 40.38 | 40.39 | 41.39 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 761.8 | 771.2 | 763.9 | 775 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.116 | 3.87 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.6958 | 0.0375 | 0.6667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.4 | 0.2 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 69.59 | 83.48 | 71.39 | 84.98 |
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
| worker nodes in service, mean | 6 | 4.698 | -21.7% | -2.165 to -0.4396 | yes: GAIN |
| node-hours | 2.514 | 1.967 | -21.8% | -0.9107 to -0.1839 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.1 | -0.1% | -1.104 to +0.5767 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 230.3 | -15.1% | -68.55 to -13.68 | yes: GAIN |
| response time (ms), mean | 219.6 | 192.7 | -12.3% | -36.17 to -17.63 | yes: GAIN |
| response time (ms), 95th percentile | 529.7 | 613.7 | +15.9% | +6.379 to +161.6 | yes: LOSS |
| response time (ms), 99th percentile | 914.9 | 1163 | +27.1% | -8.331 to +504.1 | no |
| time over the response line (% of samples) | 8.117 | 7.84 | -3.4% | -1.732 to +1.178 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.1 | +7.6% | -0.1079 to +1.108 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.9 | +48.9 (native is 0) | +28.07 to +69.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.04 | 13.73 | -2.2% | -2.458 to +1.835 | no |
| utilisation (used / allocatable) | 0.05746 | 0.07431 | +29.3% | +0.005179 to +0.02852 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.379 | 1.366 | -0.9% | -0.02931 to +0.003492 | no |
| Omni's own CPU (cores), mean | 0 | 0.01779 | +0.0178 (native is 0) | +0.01516 to +0.02042 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.379 | 1.384 | +0.4% | -0.01272 to +0.02249 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.2 | 402.9 | -16.3% | -133.7 to -22.92 | yes, down (shown, not judged) |
| HPA replicas, mean | 2 | 2.227 | +11.3% | +0.07126 to +0.3822 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | -1.194 to +2.194 | no |
| pod start wait, mean (s) | 0.2 | 0.35 | +75.0% | -0.8045 to +1.104 | no |
| host CPU busy, the real machine under kind (%) | 40.38 | 41.39 | +2.5% | +0.7328 to +1.29 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.2 | 775 | +0.5% | +1.149 to +6.451 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.87 | -35.5% | -3.432 to -0.8287 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.6667 | -4.2% | -0.1087 to +0.05037 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.2 | -14.3% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.48 | 84.98 | +1.8% | -1.189 to +4.189 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.101e-15 to +3.905e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.514 | -0.1% | -0.01199 to +0.005319 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.4 | -0.2% | -1.546 to +0.4416 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.4 | -0.2% | -1.546 to +0.4416 | no |
| response time (ms), mean | 295.2 | 219.6 | -25.6% | -118.9 to -32.32 | yes: GAIN |
| response time (ms), 95th percentile | 959.4 | 529.7 | -44.8% | -666.7 to -192.7 | yes: GAIN |
| response time (ms), 99th percentile | 1413 | 914.9 | -35.2% | -793.5 to -202.2 | yes: GAIN |
| time over the response line (% of samples) | 14.71 | 8.117 | -44.8% | -11.39 to -1.797 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 6.6 | -12.0% | -1.99 to +0.19 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.25 | 14.04 | +36.9% | +2.442 to +5.131 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05776 | 0.05746 | -0.5% | -0.001655 to +0.001037 | no |
| CPU used (cores), mean | 1.386 | 1.379 | -0.5% | -0.03973 to +0.0249 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.386 | 1.379 | -0.5% | -0.03973 to +0.0249 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.7 | 481.2 | +1.2% | -8.976 to +19.99 | no |
| HPA replicas, mean | 2.001 | 2 | -0.1% | -0.1173 to +0.1153 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 39.63 | 40.38 | +1.9% | +0.3269 to +1.165 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 761.8 | 771.2 | +1.2% | +3.329 to +15.47 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.6958 | +1291.7% | +0.5578 to +0.7339 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.4 | +366.7% | +0.5722 to +1.628 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 69.59 | 83.48 | +20.0% | +4.68 to +23.09 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.939 | -17.7% | -1.809 to -0.3129 | yes: GAIN |
| node-hours | 2.517 | 2.067 | -17.9% | -0.7645 to -0.1358 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.3 | -0.2% | -1.629 to +0.3627 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 238 | -12.5% | -57.78 to -10.05 | yes: GAIN |
| response time (ms), mean | 295.2 | 260.1 | -11.9% | -50.07 to -20 | yes: GAIN |
| response time (ms), 95th percentile | 959.4 | 978.7 | +2.0% | -48.11 to +86.82 | no |
| response time (ms), 99th percentile | 1413 | 1454 | +2.9% | -149.1 to +231.3 | no |
| time over the response line (% of samples) | 14.71 | 14.59 | -0.8% | -0.6804 to +0.4426 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.6 | +1.3% | -0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.4 | +41.4 (native is 0) | +26.35 to +56.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.25 | 10.63 | +3.7% | -1.323 to +2.076 | no |
| utilisation (used / allocatable) | 0.05776 | 0.07064 | +22.3% | +0.004149 to +0.02161 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.386 | 1.38 | -0.4% | -0.03196 to +0.01964 | no |
| Omni's own CPU (cores), mean | 0 | 0.01596 | +0.016 (native is 0) | +0.01412 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.386 | 1.396 | +0.7% | -0.01663 to +0.03622 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.7 | 413.1 | -13.2% | -104.8 to -20.51 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.001 | 2.161 | +8.0% | -0.05389 to +0.3746 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.3048 to +1.505 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 39.63 | 40.39 | +1.9% | +0.4647 to +1.042 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 761.8 | 763.9 | +0.3% | -1.523 to +5.723 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.116 | -31.4% | -3.132 to -0.6347 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0375 | -25.0% | -0.04981 to +0.02481 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | -33.3% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 69.59 | 71.39 | +2.6% | -2.362 to +5.962 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.939 | -17.7% | -1.809 to -0.3129 | yes: GAIN |
| node-hours | 2.514 | 2.067 | -17.8% | -0.7623 to -0.1313 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 | -0.0% | -1.007 to +0.8451 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 238 | -12.3% | -57.04 to -9.686 | yes: GAIN |
| response time (ms), mean | 219.6 | 260.1 | +18.5% | -0.1479 to +81.3 | no |
| response time (ms), 95th percentile | 529.7 | 978.7 | +84.8% | +196.9 to +701.1 | yes: LOSS |
| response time (ms), 99th percentile | 914.9 | 1454 | +58.9% | +248.8 to +829 | yes: LOSS |
| time over the response line (% of samples) | 8.117 | 14.59 | +79.8% | +1.726 to +11.22 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.6 | +15.2% | -0.06632 to +2.066 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.4 | +41.4 (native is 0) | +26.35 to +56.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.04 | 10.63 | -24.3% | -4.439 to -2.381 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05746 | 0.07064 | +23.0% | +0.003571 to +0.0228 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.379 | 1.38 | +0.1% | -0.01815 to +0.02066 | no |
| Omni's own CPU (cores), mean | 0 | 0.01596 | +0.016 (native is 0) | +0.01412 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.379 | 1.396 | +1.2% | -0.001558 to +0.03599 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.2 | 413.1 | -14.2% | -120.1 to -16.22 | yes, down (shown, not judged) |
| HPA replicas, mean | 2 | 2.161 | +8.1% | -0.05007 to +0.3728 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | -0.6769 to +1.477 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | -0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 40.38 | 40.39 | +0.0% | -0.3191 to +0.3336 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.2 | 763.9 | -0.9% | -11.85 to -2.75 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.116 | -31.4% | -3.132 to -0.6347 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.0375 | -94.6% | -0.7436 to -0.5731 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.2 | -85.7% | -1.652 to -0.7476 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 83.48 | 71.39 | -14.5% | -20.86 to -3.319 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.698 | -21.7% | -2.165 to -0.4396 | yes: GAIN |
| node-hours | 2.517 | 1.967 | -21.9% | -0.9146 to -0.1866 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.1 | -0.3% | -1.892 to +0.2603 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 230.3 | -15.3% | -69.46 to -13.87 | yes: GAIN |
| response time (ms), mean | 295.2 | 192.7 | -34.7% | -141.6 to -63.45 | yes: GAIN |
| response time (ms), 95th percentile | 959.4 | 613.7 | -36.0% | -520.1 to -171.2 | yes: GAIN |
| response time (ms), 99th percentile | 1413 | 1163 | -17.7% | -509.7 to +9.824 | no |
| time over the response line (% of samples) | 14.71 | 7.84 | -46.7% | -11.58 to -2.161 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.1 | -5.3% | -1.366 to +0.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.9 | +48.9 (native is 0) | +28.07 to +69.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.25 | 13.73 | +33.9% | +1.278 to +5.672 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05776 | 0.07431 | +28.6% | +0.005671 to +0.02741 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.386 | 1.366 | -1.5% | -0.057 to +0.01635 | no |
| Omni's own CPU (cores), mean | 0 | 0.01779 | +0.0178 (native is 0) | +0.01516 to +0.02042 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.386 | 1.384 | -0.2% | -0.04101 to +0.03594 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.7 | 402.9 | -15.3% | -119.5 to -26.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.001 | 2.227 | +11.3% | +0.06873 to +0.3827 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.8834 to +2.283 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.35 (native is 0) | -0.4417 to +1.142 | no |
| host CPU busy, the real machine under kind (%) | 39.63 | 41.39 | +4.4% | +1.183 to +2.331 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 761.8 | 775 | +1.7% | +5.387 to +21.01 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.87 | -35.5% | -3.432 to -0.8287 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.6667 | +1233.3% | +0.5258 to +0.7075 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.2 | +300.0% | +0.3722 to +1.428 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 69.59 | 84.98 | +22.1% | +4.873 to +25.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*