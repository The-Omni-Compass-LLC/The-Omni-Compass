# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.171 | 5.337 |
| node-hours | 2.511 | 2.512 | 2.161 | 2.232 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.2 | 272.6 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273.2 | 246.7 | 252.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 371.1 | 404 | 333.4 | 356.3 |
| response time (ms), 95th percentile | 1278 | 1409 | 1334 | 1474 |
| response time (ms), 99th percentile | 1825 | 2029 | 1886 | 2040 |
| time over the response line (% of samples) | 21.68 | 23.23 | 20.71 | 21.66 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.11 | 11 | 11.33 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.89 | 33.11 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.83 | 11.43 | 10.84 | 12.05 |
| utilisation (used / allocatable) | 0.06286 | 0.06291 | 0.07272 | 0.0711 |
| CPU used (cores), mean | 1.509 | 1.51 | 1.496 | 1.507 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01814 | 0.01838 |
| CPU used with Omni's own (cores), mean | 1.509 | 1.51 | 1.514 | 1.525 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.8 | 436.9 | 395.2 | 400.5 |
| HPA replicas, mean | 2.052 | 2.108 | 2.01 | 2.083 |
| pods started | 0 | 0.1111 | 0 | 0.5556 |
| pod start wait, total (s) | 0 | 0.3333 | 0 | 1.222 |
| pod start wait, mean (s) | 0 | 0.3333 | 0 | 0.7222 |
| host CPU busy, the real machine under kind (%) | 42.82 | 43.31 | 43.46 | 44.54 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 779.2 | 790.4 | 784.2 | 794.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.43 | 4.724 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 0.2361 | 0.02778 | 0.2361 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 0.8889 | 0 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 87.61 | 98.69 | 92.22 | 102.1 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.337 | -11.0% | -1.283 to -0.04248 | yes: GAIN |
| node-hours | 2.512 | 2.232 | -11.1% | -0.5413 to -0.01873 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273 | -0.1% | -0.8515 to +0.2988 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 252.2 | -7.7% | -40.76 to -1.383 | yes: GAIN |
| response time (ms), mean | 404 | 356.3 | -11.8% | -70.49 to -24.92 | yes: GAIN |
| response time (ms), 95th percentile | 1409 | 1474 | +4.7% | -35.72 to +166.9 | no |
| response time (ms), 99th percentile | 2029 | 2040 | +0.6% | -136.6 to +160.2 | no |
| time over the response line (% of samples) | 23.23 | 21.66 | -6.7% | -2.69 to -0.4328 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.11 | 11.33 | +2.0% | -0.1167 to +0.5612 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.11 | +33.1 (native is 0) | +21.77 to +44.46 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.43 | 12.05 | +5.4% | -1.448 to +2.681 | no |
| utilisation (used / allocatable) | 0.06291 | 0.0711 | +13.0% | +0.0001106 to +0.01628 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.51 | 1.507 | -0.2% | -0.02458 to +0.01846 | no |
| Omni's own CPU (cores), mean | 0 | 0.01838 | +0.0184 (native is 0) | +0.0172 to +0.01956 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.51 | 1.525 | +1.0% | -0.00669 to +0.03732 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.9 | 400.5 | -8.3% | -74.4 to +1.576 | no |
| HPA replicas, mean | 2.108 | 2.083 | -1.2% | -0.2833 to +0.2329 | no |
| pods started | 0.1111 | 0.5556 | +400.0% | -0.3348 to +1.224 | no |
| pod start wait, total (s) | 0.3333 | 1.222 | +266.7% | -1.05 to +2.828 | no |
| pod start wait, mean (s) | 0.3333 | 0.7222 | +116.7% | -0.9113 to +1.689 | no |
| host CPU busy, the real machine under kind (%) | 43.31 | 44.54 | +2.8% | +0.5204 to +1.935 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790.4 | 794.2 | +0.5% | -0.4109 to +7.966 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.724 | -21.3% | -2.377 to -0.1759 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2361 | 0.2361 | +0.0% | -0.04237 to +0.04237 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8889 | 1 | +12.5% | -0.1451 to +0.3673 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.69 | 102.1 | +3.5% | -2.663 to +9.496 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.005e-15 to +1.202e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.511 | 2.512 | +0.1% | -0.005415 to +0.008008 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.2 | +0.1% | -0.4171 to +0.7407 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273.2 | +0.1% | -0.4171 to +0.7407 | no |
| response time (ms), mean | 371.1 | 404 | +8.9% | +13.7 to +52.24 | yes: LOSS |
| response time (ms), 95th percentile | 1278 | 1409 | +10.2% | +37.2 to +224.2 | yes: LOSS |
| response time (ms), 99th percentile | 1825 | 2029 | +11.1% | +90.91 to +315.9 | yes: LOSS |
| time over the response line (% of samples) | 21.68 | 23.23 | +7.2% | +0.6291 to +2.473 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.11 | +1.0% | -0.1451 to +0.3673 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.83 | 11.43 | +5.5% | -1.443 to +2.639 | no |
| utilisation (used / allocatable) | 0.06286 | 0.06291 | +0.1% | -0.001074 to +0.001179 | no |
| CPU used (cores), mean | 1.509 | 1.51 | +0.1% | -0.02577 to +0.0283 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.509 | 1.51 | +0.1% | -0.02577 to +0.0283 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.8 | 436.9 | +0.2% | -8.285 to +10.42 | no |
| HPA replicas, mean | 2.052 | 2.108 | +2.7% | -0.05993 to +0.1719 | no |
| pods started | 0 | 0.1111 | +0.111 (native is 0) | -0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0 | 0.3333 | +0.333 (native is 0) | -0.4353 to +1.102 | no |
| pod start wait, mean (s) | 0 | 0.3333 | +0.333 (native is 0) | -0.4353 to +1.102 | no |
| host CPU busy, the real machine under kind (%) | 42.82 | 43.31 | +1.1% | -0.4592 to +1.439 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 779.2 | 790.4 | +1.4% | +4.436 to +18.01 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 0.2361 | +537.5% | +0.1162 to +0.2819 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 0.8889 | +700.0% | +0.4388 to +1.117 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 87.61 | 98.69 | +12.7% | +4.737 to +17.44 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.171 | -13.8% | -1.422 to -0.2353 | yes: GAIN |
| node-hours | 2.511 | 2.161 | -13.9% | -0.5962 to -0.104 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.6 | -0.2% | -1.136 to +0.2673 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 246.7 | -9.7% | -45.18 to -7.682 | yes: GAIN |
| response time (ms), mean | 371.1 | 333.4 | -10.1% | -59.4 to -15.9 | yes: GAIN |
| response time (ms), 95th percentile | 1278 | 1334 | +4.4% | -65.51 to +176.8 | no |
| response time (ms), 99th percentile | 1825 | 1886 | +3.3% | -88.82 to +210.1 | no |
| time over the response line (% of samples) | 21.68 | 20.71 | -4.5% | -2.16 to +0.2287 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11 | +0.0% | -0.3843 to +0.3843 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.89 | +41.9 (native is 0) | +29.46 to +54.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.83 | 10.84 | +0.1% | -2.536 to +2.551 | no |
| utilisation (used / allocatable) | 0.06286 | 0.07272 | +15.7% | +0.003309 to +0.01642 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.509 | 1.496 | -0.8% | -0.05802 to +0.03325 | no |
| Omni's own CPU (cores), mean | 0 | 0.01814 | +0.0181 (native is 0) | +0.01706 to +0.01923 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 1.514 | +0.4% | -0.04063 to +0.05215 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.8 | 395.2 | -9.3% | -67.47 to -13.84 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.052 | 2.01 | -2.0% | -0.2115 to +0.1283 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 42.82 | 43.46 | +1.5% | -0.279 to +1.565 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 779.2 | 784.2 | +0.6% | -2.744 to +12.74 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.43 | -26.2% | -2.507 to -0.6327 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 0.02778 | -25.0% | -0.03595 to +0.01743 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 0 | -100.0% | -0.3673 to +0.1451 | no |
| queue: job turnaround, submitted to done, mean (s) | 87.61 | 92.22 | +5.3% | -2.012 to +11.24 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.171 | -13.8% | -1.422 to -0.2353 | yes: GAIN |
| node-hours | 2.512 | 2.161 | -14.0% | -0.6007 to -0.1021 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.6 | -0.2% | -1.126 to -0.06572 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 246.7 | -9.7% | -45.4 to -7.78 | yes: GAIN |
| response time (ms), mean | 404 | 333.4 | -17.5% | -96.72 to -44.52 | yes: GAIN |
| response time (ms), 95th percentile | 1409 | 1334 | -5.3% | -207.9 to +57.83 | no |
| response time (ms), 99th percentile | 2029 | 1886 | -7.0% | -279.2 to -6.285 | yes: GAIN |
| time over the response line (% of samples) | 23.23 | 20.71 | -10.8% | -3.935 to -1.098 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.11 | 11 | -1.0% | -0.573 to +0.3508 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.89 | +41.9 (native is 0) | +29.46 to +54.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.43 | 10.84 | -5.2% | -2.787 to +1.605 | no |
| utilisation (used / allocatable) | 0.06291 | 0.07272 | +15.6% | +0.002471 to +0.01715 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.51 | 1.496 | -0.9% | -0.03493 to +0.007632 | no |
| Omni's own CPU (cores), mean | 0 | 0.01814 | +0.0181 (native is 0) | +0.01706 to +0.01923 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.51 | 1.514 | +0.3% | -0.01739 to +0.02638 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.9 | 395.2 | -9.5% | -75.02 to -8.425 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.108 | 2.01 | -4.6% | -0.267 to +0.07189 | no |
| pods started | 0.1111 | 0 | -100.0% | -0.3673 to +0.1451 | no |
| pod start wait, total (s) | 0.3333 | 0 | -100.0% | -1.102 to +0.4353 | no |
| pod start wait, mean (s) | 0.3333 | 0 | -100.0% | -1.102 to +0.4353 | no |
| host CPU busy, the real machine under kind (%) | 43.31 | 43.46 | +0.4% | -0.18 to +0.4863 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 790.4 | 784.2 | -0.8% | -13.06 to +0.6182 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.43 | -26.2% | -2.507 to -0.6327 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2361 | 0.02778 | -88.2% | -0.3003 to -0.1163 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8889 | 0 | -100.0% | -1.145 to -0.6327 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 98.69 | 92.22 | -6.6% | -12.47 to -0.4747 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.337 | -11.0% | -1.283 to -0.04248 | yes: GAIN |
| node-hours | 2.511 | 2.232 | -11.1% | -0.5366 to -0.02091 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273 | -0.0% | -0.7168 to +0.4878 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 252.2 | -7.7% | -40.49 to -1.323 | yes: GAIN |
| response time (ms), mean | 371.1 | 356.3 | -4.0% | -29.7 to +0.2395 | no |
| response time (ms), 95th percentile | 1278 | 1474 | +15.4% | +99.54 to +293 | yes: LOSS |
| response time (ms), 99th percentile | 1825 | 2040 | +11.8% | +68.22 to +362.3 | yes: LOSS |
| time over the response line (% of samples) | 21.68 | 21.66 | -0.0% | -0.7367 to +0.7162 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.33 | +3.0% | -0.051 to +0.7177 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.11 | +33.1 (native is 0) | +21.77 to +44.46 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.83 | 12.05 | +11.2% | -1.438 to +3.868 | no |
| utilisation (used / allocatable) | 0.06286 | 0.0711 | +13.1% | +0.001117 to +0.01538 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.509 | 1.507 | -0.1% | -0.02943 to +0.02584 | no |
| Omni's own CPU (cores), mean | 0 | 0.01838 | +0.0184 (native is 0) | +0.0172 to +0.01956 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 1.525 | +1.1% | -0.01145 to +0.04461 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.8 | 400.5 | -8.1% | -65.36 to -5.322 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.052 | 2.083 | +1.5% | -0.1851 to +0.2468 | no |
| pods started | 0 | 0.5556 | +0.556 (native is 0) | -0.1223 to +1.233 | no |
| pod start wait, total (s) | 0 | 1.222 | +1.22 (native is 0) | -0.3983 to +2.843 | no |
| pod start wait, mean (s) | 0 | 0.7222 | +0.722 (native is 0) | -0.1607 to +1.605 | no |
| host CPU busy, the real machine under kind (%) | 42.82 | 44.54 | +4.0% | +1.261 to +2.174 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 779.2 | 794.2 | +1.9% | +8.455 to +21.54 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.724 | -21.3% | -2.377 to -0.1759 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 0.2361 | +537.5% | +0.1335 to +0.2647 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 1 | +800.0% | +0.6327 to +1.145 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 87.61 | 102.1 | +16.6% | +7.572 to +21.44 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*