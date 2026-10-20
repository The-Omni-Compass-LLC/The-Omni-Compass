# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.849 | 4.95 |
| node-hours | 2.514 | 2.513 | 2.034 | 2.074 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.2 | 272.1 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.2 | 235.9 | 239.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 328.6 | 260.4 | 290.2 | 232.1 |
| response time (ms), 95th percentile | 1133 | 884.6 | 1167 | 1003 |
| response time (ms), 99th percentile | 1627 | 1478 | 1620 | 1567 |
| time over the response line (% of samples) | 13.94 | 8.862 | 13.31 | 7.955 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 7.1 | 7.9 | 6.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 55.7 | 32.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.818 | 16.41 | 10.79 | 16.62 |
| utilisation (used / allocatable) | 0.05963 | 0.05984 | 0.07309 | 0.07212 |
| CPU used (cores), mean | 1.431 | 1.436 | 1.398 | 1.408 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01773 | 0.01657 |
| CPU used with Omni's own (cores), mean | 1.431 | 1.436 | 1.415 | 1.425 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 463.8 | 408.2 | 409.5 |
| HPA replicas, mean | 1.987 | 1.976 | 2.093 | 2.068 |
| pods started | 0.2 | 0.1 | 0.2 | 0.4 |
| pod start wait, total (s) | 0.3 | 0.1 | 0.3 | 1.4 |
| pod start wait, mean (s) | 0.15 | 0.1 | 0.15 | 0.7 |
| host CPU busy, the real machine under kind (%) | 40.49 | 41.73 | 41.33 | 42.51 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 780.2 | 791.2 | 781.9 | 793.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.972 | 4.228 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.725 | 0.06667 | 0.8917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | 0.5 | 2.2 |
| queue: job turnaround, submitted to done, mean (s) | 85.9 | 101 | 87.21 | 102.8 |
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
| worker nodes in service, mean | 6 | 4.95 | -17.5% | -1.862 to -0.2384 | yes: GAIN |
| node-hours | 2.513 | 2.074 | -17.5% | -0.7753 to -0.1024 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.1 | -0.0% | -0.6337 to +0.6018 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 239.1 | -12.1% | -58.49 to -7.6 | yes: GAIN |
| response time (ms), mean | 260.4 | 232.1 | -10.9% | -53.86 to -2.824 | yes: GAIN |
| response time (ms), 95th percentile | 884.6 | 1003 | +13.4% | -74.36 to +310.8 | no |
| response time (ms), 99th percentile | 1478 | 1567 | +6.0% | -71.83 to +249.8 | no |
| time over the response line (% of samples) | 8.862 | 7.955 | -10.2% | -2.699 to +0.8845 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 6.2 | -12.7% | -1.88 to +0.0802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.1 (native is 0) | +26.23 to +37.97 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.41 | 16.62 | +1.3% | -1.627 to +2.061 | no |
| utilisation (used / allocatable) | 0.05984 | 0.07212 | +20.5% | +0.002804 to +0.02175 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 1.408 | -2.0% | -0.06093 to +0.004876 | no |
| Omni's own CPU (cores), mean | 0 | 0.01657 | +0.0166 (native is 0) | +0.01502 to +0.01812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.425 | -0.8% | -0.04466 to +0.02174 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.8 | 409.5 | -11.7% | -96.03 to -12.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.068 | +4.7% | -0.1135 to +0.2979 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.3786 to +0.9786 | no |
| pod start wait, total (s) | 0.1 | 1.4 | +1300.0% | -1.086 to +3.686 | no |
| pod start wait, mean (s) | 0.1 | 0.7 | +600.0% | -0.6251 to +1.825 | no |
| host CPU busy, the real machine under kind (%) | 41.73 | 42.51 | +1.9% | +0.3605 to +1.212 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 791.2 | 793.3 | +0.3% | -3.052 to +7.252 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.228 | -29.5% | -3.099 to -0.4444 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.8917 | +23.0% | -0.05769 to +0.391 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 2.2 | +46.7% | -0.4209 to +1.821 | no |
| queue: job turnaround, submitted to done, mean (s) | 101 | 102.8 | +1.8% | -4.569 to +8.219 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.358e-15 to +6.47e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.513 | -0.0% | -0.008684 to +0.007684 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.2 | -0.0% | -0.9415 to +0.8265 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.2 | -0.0% | -0.9415 to +0.8265 | no |
| response time (ms), mean | 328.6 | 260.4 | -20.8% | -123.5 to -12.93 | yes: GAIN |
| response time (ms), 95th percentile | 1133 | 884.6 | -22.0% | -444.9 to -52.78 | yes: GAIN |
| response time (ms), 99th percentile | 1627 | 1478 | -9.1% | -461.1 to +164.2 | no |
| time over the response line (% of samples) | 13.94 | 8.862 | -36.4% | -9.834 to -0.33 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 7.1 | -10.1% | -1.679 to +0.07931 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.818 | 16.41 | +67.1% | +3.353 to +9.82 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05963 | 0.05984 | +0.3% | -0.0007597 to +0.001173 | no |
| CPU used (cores), mean | 1.431 | 1.436 | +0.3% | -0.01823 to +0.02815 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.431 | 1.436 | +0.3% | -0.01823 to +0.02815 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 463.8 | -0.3% | -9.543 to +7.181 | no |
| HPA replicas, mean | 1.987 | 1.976 | -0.6% | -0.169 to +0.1471 | no |
| pods started | 0.2 | 0.1 | -50.0% | -0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.3 | 0.1 | -66.7% | -0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.15 | 0.1 | -33.3% | -0.4782 to +0.3782 | no |
| host CPU busy, the real machine under kind (%) | 40.49 | 41.73 | +3.0% | +0.9838 to +1.477 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 780.2 | 791.2 | +1.4% | +2.872 to +19.13 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.725 | +866.7% | +0.4985 to +0.8015 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.5 | +275.0% | +0.3128 to +1.887 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 85.9 | 101 | +17.6% | +4.845 to +25.35 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.849 | -19.2% | -1.857 to -0.4453 | yes: GAIN |
| node-hours | 2.514 | 2.034 | -19.1% | -0.7791 to -0.18 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.1 | -0.0% | -1.026 to +0.8386 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 235.9 | -13.3% | -59.15 to -13.37 | yes: GAIN |
| response time (ms), mean | 328.6 | 290.2 | -11.7% | -56.82 to -20.01 | yes: GAIN |
| response time (ms), 95th percentile | 1133 | 1167 | +2.9% | -32.85 to +99.2 | no |
| response time (ms), 99th percentile | 1627 | 1620 | -0.4% | -172.5 to +158.1 | no |
| time over the response line (% of samples) | 13.94 | 13.31 | -4.5% | -1.892 to +0.6287 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 7.9 | +0.0% | -0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.7 | +55.7 (native is 0) | +35.95 to +75.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.818 | 10.79 | +9.8% | -1.195 to +3.129 | no |
| utilisation (used / allocatable) | 0.05963 | 0.07309 | +22.6% | +0.004312 to +0.02261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.398 | -2.3% | -0.05842 to -0.008828 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01773 | +0.0177 (native is 0) | +0.01636 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.415 | -1.1% | -0.0416 to +0.009811 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 408.2 | -12.2% | -96.54 to -17.01 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.987 | 2.093 | +5.4% | -0.133 to +0.3463 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.3 | 0.3 | +0.0% | -1.012 to +1.012 | no |
| pod start wait, mean (s) | 0.15 | 0.15 | +0.0% | -0.5058 to +0.5058 | no |
| host CPU busy, the real machine under kind (%) | 40.49 | 41.33 | +2.1% | +0.6214 to +1.043 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 780.2 | 781.9 | +0.2% | -1.518 to +4.918 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.972 | -33.8% | -3.086 to -0.9699 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.06667 | -11.1% | -0.04757 to +0.03091 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.9 | 87.21 | +1.5% | -1.522 to +4.13 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.849 | -19.2% | -1.857 to -0.4453 | yes: GAIN |
| node-hours | 2.513 | 2.034 | -19.1% | -0.7755 to -0.1827 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.1 | -0.0% | -0.9933 to +0.9204 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 235.9 | -13.3% | -58.6 to -13.81 | yes: GAIN |
| response time (ms), mean | 260.4 | 290.2 | +11.4% | -16.31 to +75.92 | no |
| response time (ms), 95th percentile | 884.6 | 1167 | +31.9% | +95.25 to +468.8 | yes: LOSS |
| response time (ms), 99th percentile | 1478 | 1620 | +9.6% | -122.8 to +405.3 | no |
| time over the response line (% of samples) | 8.862 | 13.31 | +50.2% | +0.5045 to +8.397 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.9 | +11.3% | -0.2556 to +1.856 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.7 | +55.7 (native is 0) | +35.95 to +75.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.41 | 10.79 | -34.3% | -8.391 to -2.849 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05984 | 0.07309 | +22.1% | +0.0038 to +0.02271 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.436 | 1.398 | -2.7% | -0.07217 to -0.00499 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01773 | +0.0177 (native is 0) | +0.01636 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.415 | -1.5% | -0.05498 to +0.01328 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.8 | 408.2 | -12.0% | -98.37 to -12.82 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.093 | +6.0% | -0.1136 to +0.3488 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.1 | 0.3 | +200.0% | -0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.1 | 0.15 | +50.0% | -0.3782 to +0.4782 | no |
| host CPU busy, the real machine under kind (%) | 41.73 | 41.33 | -1.0% | -0.637 to -0.1591 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 791.2 | 781.9 | -1.2% | -17.46 to -1.137 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.972 | -33.8% | -3.086 to -0.9699 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.06667 | -90.8% | -0.8022 to -0.5145 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.5 | -66.7% | -1.826 to -0.174 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 101 | 87.21 | -13.7% | -23.89 to -3.694 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.95 | -17.5% | -1.862 to -0.2384 | yes: GAIN |
| node-hours | 2.514 | 2.074 | -17.5% | -0.7808 to -0.098 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.1 | -0.0% | -0.8589 to +0.712 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 239.1 | -12.2% | -59.17 to -7.035 | yes: GAIN |
| response time (ms), mean | 328.6 | 232.1 | -29.4% | -144.5 to -48.64 | yes: GAIN |
| response time (ms), 95th percentile | 1133 | 1003 | -11.5% | -376.5 to +115.2 | no |
| response time (ms), 99th percentile | 1627 | 1567 | -3.7% | -402.9 to +284 | no |
| time over the response line (% of samples) | 13.94 | 7.955 | -43.0% | -11.1 to -0.8817 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 6.2 | -21.5% | -3.051 to -0.3491 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.1 (native is 0) | +26.23 to +37.97 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.818 | 16.62 | +69.3% | +3.114 to +10.49 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05963 | 0.07212 | +20.9% | +0.002994 to +0.02198 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.408 | -1.6% | -0.06064 to +0.0145 | no |
| Omni's own CPU (cores), mean | 0 | 0.01657 | +0.0166 (native is 0) | +0.01502 to +0.01812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.425 | -0.5% | -0.04433 to +0.03133 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 409.5 | -11.9% | -97.06 to -13.93 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.987 | 2.068 | +4.1% | -0.1447 to +0.3072 | no |
| pods started | 0.2 | 0.4 | +100.0% | -0.6121 to +1.012 | no |
| pod start wait, total (s) | 0.3 | 1.4 | +366.7% | -1.433 to +3.633 | no |
| pod start wait, mean (s) | 0.15 | 0.7 | +366.7% | -0.7167 to +1.817 | no |
| host CPU busy, the real machine under kind (%) | 40.49 | 42.51 | +5.0% | +1.629 to +2.405 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 780.2 | 793.3 | +1.7% | +3.489 to +22.71 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.228 | -29.5% | -3.099 to -0.4444 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.8917 | +1088.9% | +0.5176 to +1.116 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 2.2 | +450.0% | +0.155 to +3.445 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 85.9 | 102.8 | +19.7% | +4.717 to +29.12 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*