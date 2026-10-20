# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.335 | 5.54 |
| node-hours | 2.515 | 2.518 | 2.234 | 2.321 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 274.1 | 273.5 | 273.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 274.1 | 252.6 | 259.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 396.8 | 459.4 | 360.3 | 425 |
| response time (ms), 95th percentile | 1366 | 1927 | 1450 | 1992 |
| response time (ms), 99th percentile | 1972 | 2841 | 2134 | 2937 |
| time over the response line (% of samples) | 20.42 | 18.89 | 19.84 | 18.32 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.4 | 11.6 | 12.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 47.1 | 31.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 21.9 | 11.25 | 23.4 |
| utilisation (used / allocatable) | 0.06297 | 0.0635 | 0.07092 | 0.06909 |
| CPU used (cores), mean | 1.511 | 1.524 | 1.517 | 1.53 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01824 | 0.01924 |
| CPU used with Omni's own (cores), mean | 1.511 | 1.524 | 1.535 | 1.55 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 435.5 | 400.3 | 409.1 |
| HPA replicas, mean | 1.954 | 2.055 | 2.058 | 2.112 |
| pods started | 0 | 0.2 | 0.2 | 0.3 |
| pod start wait, total (s) | 0 | 0.3 | 0.2 | 0.4 |
| pod start wait, mean (s) | 0 | 0.15 | 0.2 | 0.4 |
| host CPU busy, the real machine under kind (%) | 43.13 | 46.1 | 44.29 | 47.29 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 790 | 835 | 797.8 | 844.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.694 | 5.055 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1.071 | 0.075 | 1.079 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 2.6 | 0.4 | 3 |
| queue: job turnaround, submitted to done, mean (s) | 98.16 | 139.5 | 106.2 | 148.6 |
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
| worker nodes in service, mean | 6 | 5.54 | -7.7% | -0.8497 to -0.07003 | yes: GAIN |
| node-hours | 2.518 | 2.321 | -7.8% | -0.3627 to -0.03014 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.9 | -0.1% | -1.143 to +0.7176 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 259.5 | -5.3% | -27.13 to -2.153 | yes: GAIN |
| response time (ms), mean | 459.4 | 425 | -7.5% | -54.19 to -14.61 | yes: GAIN |
| response time (ms), 95th percentile | 1927 | 1992 | +3.4% | -45.55 to +175.8 | no |
| response time (ms), 99th percentile | 2841 | 2937 | +3.4% | -98.96 to +292.2 | no |
| time over the response line (% of samples) | 18.89 | 18.32 | -3.0% | -2.146 to +1.003 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 12.1 | -2.4% | -0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.7 | +31.7 (native is 0) | +28.19 to +35.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.9 | 23.4 | +6.8% | -3.199 to +6.193 | no |
| utilisation (used / allocatable) | 0.0635 | 0.06909 | +8.8% | +0.000863 to +0.01033 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.53 | +0.4% | -0.009858 to +0.02271 | no |
| Omni's own CPU (cores), mean | 0 | 0.01924 | +0.0192 (native is 0) | +0.01699 to +0.02149 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.55 | +1.7% | +0.008144 to +0.04318 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.5 | 409.1 | -6.0% | -51.31 to -1.364 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.112 | +2.8% | -0.133 to +0.2474 | no |
| pods started | 0.2 | 0.3 | +50.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | -0.306 to +0.506 | no |
| pod start wait, mean (s) | 0.15 | 0.4 | +166.7% | -0.05395 to +0.5539 | no |
| host CPU busy, the real machine under kind (%) | 46.1 | 47.29 | +2.6% | +0.8225 to +1.562 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 835 | 844.2 | +1.1% | +2.416 to +15.98 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.055 | -15.7% | -1.697 to -0.192 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.071 | 1.079 | +0.8% | -0.3406 to +0.3573 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.6 | 3 | +15.4% | -1.572 to +2.372 | no |
| queue: job turnaround, submitted to done, mean (s) | 139.5 | 148.6 | +6.5% | +1.093 to +17.07 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.15e-15 to -1.591e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.518 | +0.1% | -0.002942 to +0.008942 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 274.1 | +0.2% | -0.05004 to +1.17 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 274.1 | +0.2% | -0.05004 to +1.17 | no |
| response time (ms), mean | 396.8 | 459.4 | +15.8% | +32.01 to +93.18 | yes: LOSS |
| response time (ms), 95th percentile | 1366 | 1927 | +41.1% | +266.9 to +855.7 | yes: LOSS |
| response time (ms), 99th percentile | 1972 | 2841 | +44.0% | +457.9 to +1279 | yes: LOSS |
| time over the response line (% of samples) | 20.42 | 18.89 | -7.5% | -4.848 to +1.785 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.4 | +6.9% | +0.4984 to +1.102 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 21.9 | +89.9% | +4.475 to +16.26 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06297 | 0.0635 | +0.8% | -0.0004545 to +0.001509 | no |
| CPU used (cores), mean | 1.511 | 1.524 | +0.8% | -0.01091 to +0.03621 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.511 | 1.524 | +0.8% | -0.01091 to +0.03621 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 435.5 | -0.6% | -9.938 to +5.114 | no |
| HPA replicas, mean | 1.954 | 2.055 | +5.2% | -0.03189 to +0.2337 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.15 | +0.15 (native is 0) | -0.1893 to +0.4893 | no |
| host CPU busy, the real machine under kind (%) | 43.13 | 46.1 | +6.9% | +2.276 to +3.665 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790 | 835 | +5.7% | +22.44 to +67.56 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1.071 | +1613.3% | +0.7236 to +1.293 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 2.6 | +550.0% | +0.9028 to +3.497 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 98.16 | 139.5 | +42.1% | +23.67 to +58.94 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.335 | -11.1% | -1.079 to -0.2506 | yes: GAIN |
| node-hours | 2.515 | 2.234 | -11.1% | -0.4507 to -0.1096 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.5 | -0.0% | -0.7824 to +0.644 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 252.6 | -7.7% | -33.7 to -8.232 | yes: GAIN |
| response time (ms), mean | 396.8 | 360.3 | -9.2% | -54.16 to -18.82 | yes: GAIN |
| response time (ms), 95th percentile | 1366 | 1450 | +6.2% | -56.8 to +225.2 | no |
| response time (ms), 99th percentile | 1972 | 2134 | +8.2% | -41.01 to +364.2 | no |
| time over the response line (% of samples) | 20.42 | 19.84 | -2.9% | -1.452 to +0.2878 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.6 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 | +47.1 (native is 0) | +30.24 to +63.96 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 11.25 | -2.5% | -1.618 to +1.044 | no |
| utilisation (used / allocatable) | 0.06297 | 0.07092 | +12.6% | +0.00358 to +0.01232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.511 | 1.517 | +0.4% | -0.01377 to +0.02544 | no |
| Omni's own CPU (cores), mean | 0 | 0.01824 | +0.0182 (native is 0) | +0.01718 to +0.0193 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.511 | 1.535 | +1.6% | +0.004133 to +0.04402 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 400.3 | -8.6% | -59.56 to -15.51 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.954 | 2.058 | +5.4% | -0.03734 to +0.2465 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 43.13 | 44.29 | +2.7% | +0.8184 to +1.499 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790 | 797.8 | +1.0% | +1.667 to +13.93 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.694 | -21.8% | -2.088 to -0.5238 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.075 | +20.0% | -0.04551 to +0.07051 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.16 | 106.2 | +8.2% | +2.574 to +13.5 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.335 | -11.1% | -1.079 to -0.2506 | yes: GAIN |
| node-hours | 2.518 | 2.234 | -11.2% | -0.4569 to -0.1094 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.5 | -0.2% | -1.568 to +0.3091 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 252.6 | -7.9% | -34.48 to -8.577 | yes: GAIN |
| response time (ms), mean | 459.4 | 360.3 | -21.6% | -127.7 to -70.46 | yes: GAIN |
| response time (ms), 95th percentile | 1927 | 1450 | -24.8% | -748.7 to -205.4 | yes: GAIN |
| response time (ms), 99th percentile | 2841 | 2134 | -24.9% | -1045 to -369.1 | yes: GAIN |
| time over the response line (% of samples) | 18.89 | 19.84 | +5.0% | -2.306 to +4.205 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 11.6 | -6.5% | -1.364 to -0.2358 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 | +47.1 (native is 0) | +30.24 to +63.96 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.9 | 11.25 | -48.6% | -16.92 to -4.388 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0635 | 0.07092 | +11.7% | +0.00267 to +0.01217 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.517 | -0.4% | -0.02076 to +0.007129 | no |
| Omni's own CPU (cores), mean | 0 | 0.01824 | +0.0182 (native is 0) | +0.01718 to +0.0193 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.535 | +0.7% | -0.002888 to +0.02573 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.5 | 400.3 | -8.1% | -59.53 to -10.71 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.058 | +0.2% | -0.161 to +0.1683 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.584 to +0.584 | no |
| pod start wait, total (s) | 0.3 | 0.2 | -33.3% | -0.8872 to +0.6872 | no |
| pod start wait, mean (s) | 0.15 | 0.2 | +33.3% | -0.4401 to +0.5401 | no |
| host CPU busy, the real machine under kind (%) | 46.1 | 44.29 | -3.9% | -2.455 to -1.168 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 835 | 797.8 | -4.5% | -54.72 to -19.68 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.694 | -21.8% | -2.088 to -0.5238 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.071 | 0.075 | -93.0% | -1.302 to -0.6901 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.6 | 0.4 | -84.6% | -3.7 to -0.6996 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 139.5 | 106.2 | -23.9% | -46.96 to -19.59 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.54 | -7.7% | -0.8497 to -0.07003 | yes: GAIN |
| node-hours | 2.515 | 2.321 | -7.7% | -0.3567 to -0.03013 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.9 | +0.1% | -0.526 to +1.221 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 259.5 | -5.1% | -26.47 to -1.7 | yes: GAIN |
| response time (ms), mean | 396.8 | 425 | +7.1% | -11.65 to +68.04 | no |
| response time (ms), 95th percentile | 1366 | 1992 | +45.9% | +281.3 to +971.4 | yes: LOSS |
| response time (ms), 99th percentile | 1972 | 2937 | +48.9% | +441.8 to +1488 | yes: LOSS |
| time over the response line (% of samples) | 20.42 | 18.32 | -10.3% | -4.594 to +0.3876 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.1 | +4.3% | -0.343 to +1.343 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.7 | +31.7 (native is 0) | +28.19 to +35.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 23.4 | +102.9% | +2.308 to +21.42 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06297 | 0.06909 | +9.7% | +0.002085 to +0.01016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.511 | 1.53 | +1.3% | -0.004351 to +0.0425 | no |
| Omni's own CPU (cores), mean | 0 | 0.01924 | +0.0192 (native is 0) | +0.01699 to +0.02149 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.511 | 1.55 | +2.5% | +0.01505 to +0.06158 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.9 | 409.1 | -6.6% | -47.75 to -9.752 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.954 | 2.112 | +8.1% | -0.0124 to +0.3287 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 43.13 | 47.29 | +9.7% | +3.293 to +5.032 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790 | 844.2 | +6.9% | +27.15 to +81.25 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.055 | -15.7% | -1.697 to -0.192 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1.079 | +1626.7% | +0.5688 to +1.465 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 3 | +650.0% | +0.5159 to +4.684 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 98.16 | 148.6 | +51.3% | +27.49 to +73.29 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*