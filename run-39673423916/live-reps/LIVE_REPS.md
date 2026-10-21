# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.28 | 5.344 |
| node-hours | 2.517 | 2.512 | 2.212 | 2.239 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273 | 273 | 273.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273 | 250.4 | 252.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 386.6 | 321.3 | 355.7 | 272.7 |
| response time (ms), 95th percentile | 1356 | 1168 | 1429 | 1054 |
| response time (ms), 99th percentile | 2013 | 1945 | 2097 | 1726 |
| time over the response line (% of samples) | 20.62 | 13.33 | 20.42 | 12.64 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.7 | 10 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 40.8 | 43.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 83.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.06 | 16.89 | 11.91 | 17.51 |
| utilisation (used / allocatable) | 0.06184 | 0.06264 | 0.07049 | 0.06974 |
| CPU used (cores), mean | 1.484 | 1.503 | 1.477 | 1.493 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01702 | 0.01743 |
| CPU used with Omni's own (cores), mean | 1.484 | 1.503 | 1.494 | 1.51 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 444.7 | 406.7 | 408 |
| HPA replicas, mean | 1.957 | 1.983 | 2.192 | 2.236 |
| pods started | 0 | 0 | 0.5 | 0.5 |
| pod start wait, total (s) | 0 | 0 | 1 | 2.2 |
| pod start wait, mean (s) | 0 | 0 | 1 | 2.2 |
| host CPU busy, the real machine under kind (%) | 42.11 | 43.76 | 43.11 | 44.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 793.4 | 811.6 | 794.4 | 809 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.708 | 4.772 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7917 | 0.04167 | 0.8083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.7 | 0.3 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 100.9 | 124.6 | 101.8 | 122 |
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
| worker nodes in service, mean | 6 | 5.344 | -10.9% | -1.289 to -0.02188 | yes: GAIN |
| node-hours | 2.512 | 2.239 | -10.9% | -0.5369 to -0.009635 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.2 | +0.1% | -0.4626 to +0.8293 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 252.6 | -7.5% | -40.21 to -0.6324 | yes: GAIN |
| response time (ms), mean | 321.3 | 272.7 | -15.1% | -85.01 to -12.21 | yes: GAIN |
| response time (ms), 95th percentile | 1168 | 1054 | -9.7% | -303.6 to +76.46 | no |
| response time (ms), 99th percentile | 1945 | 1726 | -11.3% | -573.9 to +135.7 | no |
| time over the response line (% of samples) | 13.33 | 12.64 | -5.2% | -3.137 to +1.751 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.9 | +2.1% | -0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 | +43.7 (native is 0) | +20.99 to +66.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.89 | 17.51 | +3.7% | -1.429 to +2.679 | no |
| utilisation (used / allocatable) | 0.06264 | 0.06974 | +11.3% | +0.0004215 to +0.01379 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.503 | 1.493 | -0.7% | -0.03634 to +0.01474 | no |
| Omni's own CPU (cores), mean | 0 | 0.01743 | +0.0174 (native is 0) | +0.01618 to +0.01868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.503 | 1.51 | +0.4% | -0.01888 to +0.03214 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.7 | 408 | -8.3% | -73 to -0.534 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.236 | +12.7% | +0.1285 to +0.3773 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 2.2 | +2.2 (native is 0) | +0.2688 to +4.131 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.2 | +2.2 (native is 0) | +0.2688 to +4.131 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.76 | 44.38 | +1.4% | +0.05733 to +1.186 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 811.6 | 809 | -0.3% | -11.32 to +6.116 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.772 | -20.5% | -2.351 to -0.1051 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7917 | 0.8083 | +2.1% | -0.09052 to +0.1239 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1.6 | -5.9% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 124.6 | 122 | -2.1% | -11.42 to +6.154 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.206e-16 to +5.43e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.512 | -0.2% | -0.01043 to +0.002098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273 | -0.1% | -1.002 to +0.4161 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273 | -0.1% | -1.002 to +0.4161 | no |
| response time (ms), mean | 386.6 | 321.3 | -16.9% | -99.91 to -30.64 | yes: GAIN |
| response time (ms), 95th percentile | 1356 | 1168 | -13.9% | -381.5 to +5.498 | no |
| response time (ms), 99th percentile | 2013 | 1945 | -3.4% | -533 to +397.7 | no |
| time over the response line (% of samples) | 20.62 | 13.33 | -35.3% | -11.88 to -2.691 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.7 | -1.0% | -0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.06 | 16.89 | +52.7% | +3.303 to +8.357 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06184 | 0.06264 | +1.3% | -0.000365 to +0.001955 | no |
| CPU used (cores), mean | 1.484 | 1.503 | +1.3% | -0.008759 to +0.04691 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.484 | 1.503 | +1.3% | -0.008759 to +0.04691 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 444.7 | -0.8% | -13.46 to +6.037 | no |
| HPA replicas, mean | 1.957 | 1.983 | +1.3% | -0.1179 to +0.17 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 42.11 | 43.76 | +3.9% | +1.144 to +2.154 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 793.4 | 811.6 | +2.3% | +6.756 to +29.64 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7917 | +1627.3% | +0.5929 to +0.8987 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.7 | +466.7% | +0.7968 to +2.003 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 100.9 | 124.6 | +23.5% | +10.49 to +36.91 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.28 | -12.0% | -1.451 to +0.01173 | no |
| node-hours | 2.517 | 2.212 | -12.1% | -0.613 to +0.003184 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273 | -0.1% | -1.338 to +0.7606 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 250.4 | -8.4% | -46.1 to +0.34 | no |
| response time (ms), mean | 386.6 | 355.7 | -8.0% | -42.83 to -18.95 | yes: GAIN |
| response time (ms), 95th percentile | 1356 | 1429 | +5.4% | +41.57 to +105.4 | yes: LOSS |
| response time (ms), 99th percentile | 2013 | 2097 | +4.2% | -81.41 to +250.2 | no |
| time over the response line (% of samples) | 20.62 | 20.42 | -1.0% | -0.9707 to +0.5724 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 10 | +2.0% | -0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.8 | +40.8 (native is 0) | +20.1 to +61.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.06 | 11.91 | +7.7% | -0.4211 to +2.121 | no |
| utilisation (used / allocatable) | 0.06184 | 0.07049 | +14.0% | +0.0001408 to +0.01714 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.484 | 1.477 | -0.5% | -0.02967 to +0.01608 | no |
| Omni's own CPU (cores), mean | 0 | 0.01702 | +0.017 (native is 0) | +0.015 to +0.01904 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.484 | 1.494 | +0.7% | -0.01185 to +0.0323 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 406.7 | -9.3% | -83.28 to -0.1357 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.192 | +12.0% | +0.09324 to +0.3764 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | +0.174 to +1.826 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1 (native is 0) | +0.174 to +1.826 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.11 | 43.11 | +2.4% | +0.5395 to +1.475 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 793.4 | 794.4 | +0.1% | -3.745 to +5.745 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.708 | -21.5% | -2.57 to -0.01437 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04167 | -9.1% | -0.04252 to +0.03418 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.9 | 101.8 | +0.9% | -3.722 to +5.506 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.28 | -12.0% | -1.451 to +0.01173 | no |
| node-hours | 2.512 | 2.212 | -12.0% | -0.6065 to +0.004957 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273 | +0.0% | -0.7674 to +0.7764 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 250.4 | -8.3% | -45.32 to +0.1377 | no |
| response time (ms), mean | 321.3 | 355.7 | +10.7% | +5.023 to +63.75 | yes: LOSS |
| response time (ms), 95th percentile | 1168 | 1429 | +22.4% | +64.33 to +458.7 | yes: LOSS |
| response time (ms), 99th percentile | 1945 | 2097 | +7.8% | -245.9 to +550 | no |
| time over the response line (% of samples) | 13.33 | 20.42 | +53.1% | +2.675 to +11.5 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10 | +3.1% | -0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.8 | +40.8 (native is 0) | +20.1 to +61.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.89 | 11.91 | -29.5% | -7.311 to -2.649 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06264 | 0.07049 | +12.5% | -0.001228 to +0.01692 | no |
| CPU used (cores), mean | 1.503 | 1.477 | -1.7% | -0.05744 to +0.005698 | no |
| Omni's own CPU (cores), mean | 0 | 0.01702 | +0.017 (native is 0) | +0.015 to +0.01904 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.503 | 1.494 | -0.6% | -0.04057 to +0.02286 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.7 | 406.7 | -8.5% | -84.44 to +8.446 | no |
| HPA replicas, mean | 1.983 | 2.192 | +10.5% | +0.09944 to +0.318 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | +0.174 to +1.826 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1 (native is 0) | +0.174 to +1.826 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.76 | 43.11 | -1.5% | -1.081 to -0.2029 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 811.6 | 794.4 | -2.1% | -27.82 to -6.581 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.708 | -21.5% | -2.57 to -0.01437 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7917 | 0.04167 | -94.7% | -0.9052 to -0.5948 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 0.3 | -82.4% | -2.24 to -0.5604 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 124.6 | 101.8 | -18.3% | -35.77 to -9.846 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.344 | -10.9% | -1.289 to -0.02188 | yes: GAIN |
| node-hours | 2.517 | 2.239 | -11.0% | -0.5433 to -0.01158 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.2 | -0.0% | -0.9958 to +0.7762 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 252.6 | -7.6% | -41.03 to -0.4007 | yes: GAIN |
| response time (ms), mean | 386.6 | 272.7 | -29.5% | -155.6 to -72.21 | yes: GAIN |
| response time (ms), 95th percentile | 1356 | 1054 | -22.2% | -462.1 to -141 | yes: GAIN |
| response time (ms), 99th percentile | 2013 | 1726 | -14.2% | -479 to -94.54 | yes: GAIN |
| time over the response line (% of samples) | 20.62 | 12.64 | -38.7% | -12.42 to -3.536 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.9 | +1.0% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 | +43.7 (native is 0) | +20.99 to +66.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.06 | 17.51 | +58.4% | +4.377 to +8.533 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06184 | 0.06974 | +12.8% | +0.001852 to +0.01395 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.484 | 1.493 | +0.6% | -0.03446 to +0.05101 | no |
| Omni's own CPU (cores), mean | 0 | 0.01743 | +0.0174 (native is 0) | +0.01618 to +0.01868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.484 | 1.51 | +1.7% | -0.01705 to +0.06846 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.5 | 408 | -9.0% | -71.99 to -8.963 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.236 | +14.3% | +0.06745 to +0.4905 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 2.2 | +2.2 (native is 0) | +0.2688 to +4.131 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.2 | +2.2 (native is 0) | +0.2688 to +4.131 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.11 | 44.38 | +5.4% | +1.849 to +2.693 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 793.4 | 809 | +2.0% | +7.142 to +24.06 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.772 | -20.5% | -2.351 to -0.1051 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.8083 | +1663.6% | +0.6277 to +0.8973 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.6 | +433.3% | +0.8172 to +1.783 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 100.9 | 122 | +20.9% | +10.03 to +32.11 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*