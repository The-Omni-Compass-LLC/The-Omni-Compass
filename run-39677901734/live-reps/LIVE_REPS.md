# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.561 | 5.707 |
| node-hours | 2.513 | 2.513 | 2.328 | 2.39 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.9 | 275.1 | 275 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 274.9 | 261.3 | 265.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 552.1 | 543.3 | 551.5 | 561.7 |
| response time (ms), 95th percentile | 2224 | 2294 | 2202 | 2333 |
| response time (ms), 99th percentile | 3162 | 3297 | 3288 | 3285 |
| time over the response line (% of samples) | 24.21 | 22.66 | 24.56 | 23.61 |
| failed requests (%) | 0.01156 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12.1 | 12.5 | 12 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 9.6 | 8.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.51 | 23.67 | 19.22 | 23.47 |
| utilisation (used / allocatable) | 0.06814 | 0.0678 | 0.07407 | 0.0715 |
| CPU used (cores), mean | 1.635 | 1.627 | 1.638 | 1.641 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01167 | 0.01223 |
| CPU used with Omni's own (cores), mean | 1.635 | 1.627 | 1.65 | 1.653 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.6 | 415.6 | 385.2 | 394.1 |
| HPA replicas, mean | 2.079 | 2.008 | 2.283 | 2.211 |
| pods started | 0 | 0 | 0.7 | 0.5 |
| pod start wait, total (s) | 0 | 0 | 1.4 | 0.9 |
| pod start wait, mean (s) | 0 | 0 | 1.4 | 0.7 |
| host CPU busy, the real machine under kind (%) | 46.73 | 47.56 | 47.45 | 48.1 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 861.8 | 867.2 | 864.2 | 872.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.267 | 5.437 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4958 | 0.7 | 0.3625 | 0.4167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.1 | 2.1 | 1.4 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 168.1 | 176.3 | 170 | 181.9 |
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
| worker nodes in service, mean | 6 | 5.707 | -4.9% | -0.7174 to +0.1321 | no |
| node-hours | 2.513 | 2.39 | -4.9% | -0.3007 to +0.05523 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275 | +0.1% | -0.04618 to +0.3699 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 265.8 | -3.3% | -22.31 to +4.274 | no |
| response time (ms), mean | 543.3 | 561.7 | +3.4% | -11.48 to +48.45 | no |
| response time (ms), 95th percentile | 2294 | 2333 | +1.7% | -177.3 to +255.1 | no |
| response time (ms), 99th percentile | 3297 | 3285 | -0.4% | -272.3 to +248.6 | no |
| time over the response line (% of samples) | 22.66 | 23.61 | +4.2% | -0.02219 to +1.914 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 12 | -0.8% | -1.425 to +1.225 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.1 | +8.1 (native is 0) | +5.852 to +10.35 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.67 | 23.47 | -0.9% | -4.951 to +4.544 | no |
| utilisation (used / allocatable) | 0.0678 | 0.0715 | +5.4% | -0.0009345 to +0.008322 | no |
| CPU used (cores), mean | 1.627 | 1.641 | +0.8% | -0.001997 to +0.02869 | no |
| Omni's own CPU (cores), mean | 0 | 0.01223 | +0.0122 (native is 0) | +0.01133 to +0.01313 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.627 | 1.653 | +1.6% | +0.01006 to +0.04109 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.6 | 394.1 | -5.2% | -48.68 to +5.811 | no |
| HPA replicas, mean | 2.008 | 2.211 | +10.1% | +0.08514 to +0.3218 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | -0.0802 to +1.88 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | +0.0214 to +1.379 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.56 | 48.1 | +1.1% | -0.06609 to +1.136 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 867.2 | 872.2 | +0.6% | -6.47 to +16.47 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.437 | -9.4% | -1.377 to +0.2517 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7 | 0.4167 | -40.5% | -1.079 to +0.5123 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 1.9 | -9.5% | -3.466 to +3.066 | no |
| queue: job turnaround, submitted to done, mean (s) | 176.3 | 181.9 | +3.2% | -5.875 to +17.09 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.38e-15 to -8.177e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.513 | +0.0% | -0.00693 to +0.007263 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.9 | -0.0% | -0.8077 to +0.7289 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 274.9 | -0.0% | -0.8077 to +0.7289 | no |
| response time (ms), mean | 552.1 | 543.3 | -1.6% | -35.3 to +17.59 | no |
| response time (ms), 95th percentile | 2224 | 2294 | +3.2% | -40.88 to +181.1 | no |
| response time (ms), 99th percentile | 3162 | 3297 | +4.2% | -72.35 to +341.1 | no |
| time over the response line (% of samples) | 24.21 | 22.66 | -6.4% | -2.518 to -0.5872 | yes: GAIN |
| failed requests (%) | 0.01156 | 0 | -100.0% | -0.03771 to +0.01459 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12.1 | +1.7% | -0.7417 to +1.142 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.51 | 23.67 | +15.4% | -2.17 to +8.493 | no |
| utilisation (used / allocatable) | 0.06814 | 0.0678 | -0.5% | -0.001065 to +0.000396 | no |
| CPU used (cores), mean | 1.635 | 1.627 | -0.5% | -0.02556 to +0.009503 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.635 | 1.627 | -0.5% | -0.02556 to +0.009503 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.6 | 415.6 | +0.7% | -2.224 to +8.22 | no |
| HPA replicas, mean | 2.079 | 2.008 | -3.4% | -0.1964 to +0.05406 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 46.73 | 47.56 | +1.8% | +0.4362 to +1.225 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 861.8 | 867.2 | +0.6% | -1.602 to +12.4 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4958 | 0.7 | +41.2% | -0.5771 to +0.9855 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.1 | 2.1 | -32.3% | -4.455 to +2.455 | no |
| queue: job turnaround, submitted to done, mean (s) | 168.1 | 176.3 | +4.9% | +1.387 to +15.05 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.561 | -7.3% | -1.087 to +0.208 | no |
| node-hours | 2.513 | 2.328 | -7.4% | -0.4579 to +0.08841 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275.1 | +0.1% | -0.7106 to +1.177 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 261.3 | -4.9% | -34.04 to +6.847 | no |
| response time (ms), mean | 552.1 | 551.5 | -0.1% | -22.98 to +21.67 | no |
| response time (ms), 95th percentile | 2224 | 2202 | -1.0% | -134.5 to +89.56 | no |
| response time (ms), 99th percentile | 3162 | 3288 | +4.0% | -18.77 to +271 | no |
| time over the response line (% of samples) | 24.21 | 24.56 | +1.5% | -0.3967 to +1.101 | no |
| failed requests (%) | 0.01156 | 0 | -100.0% | -0.03771 to +0.01459 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12.5 | +5.0% | -0.3656 to +1.566 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.6 | +9.6 (native is 0) | +7.516 to +11.68 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.51 | 19.22 | -6.3% | -5.489 to +2.919 | no |
| utilisation (used / allocatable) | 0.06814 | 0.07407 | +8.7% | -0.002961 to +0.01483 | no |
| CPU used (cores), mean | 1.635 | 1.638 | +0.2% | -0.01732 to +0.0236 | no |
| Omni's own CPU (cores), mean | 0 | 0.01167 | +0.0117 (native is 0) | +0.01088 to +0.01246 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.635 | 1.65 | +0.9% | -0.005512 to +0.03513 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.6 | 385.2 | -6.6% | -64.67 to +10 | no |
| HPA replicas, mean | 2.079 | 2.283 | +9.8% | +0.04768 to +0.3599 | yes: power given |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.3545 to +1.046 | yes: power given |
| pod start wait, total (s) | 0 | 1.4 | +1.4 (native is 0) | +0.4344 to +2.366 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.4 | +1.4 (native is 0) | +0.4344 to +2.366 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.73 | 47.45 | +1.5% | +0.224 to +1.219 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 861.8 | 864.2 | +0.3% | -5.313 to +10.11 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.267 | -12.2% | -1.749 to +0.2824 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4958 | 0.3625 | -26.9% | -0.6401 to +0.3734 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.1 | 1.4 | -54.8% | -4.621 to +1.221 | no |
| queue: job turnaround, submitted to done, mean (s) | 168.1 | 170 | +1.2% | -4.175 to +8.092 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.561 | -7.3% | -1.087 to +0.208 | no |
| node-hours | 2.513 | 2.328 | -7.4% | -0.4541 to +0.0843 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275.1 | +0.1% | -0.5272 to +1.072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 261.3 | -4.9% | -33.51 to +6.395 | no |
| response time (ms), mean | 543.3 | 551.5 | +1.5% | -13.77 to +30.18 | no |
| response time (ms), 95th percentile | 2294 | 2202 | -4.0% | -230.8 to +45.6 | no |
| response time (ms), 99th percentile | 3297 | 3288 | -0.3% | -165 to +148.5 | no |
| time over the response line (% of samples) | 22.66 | 24.56 | +8.4% | +1.231 to +2.578 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 12.5 | +3.3% | -0.2032 to +1.003 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.6 | +9.6 (native is 0) | +7.516 to +11.68 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.67 | 19.22 | -18.8% | -8.273 to -0.6205 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0678 | 0.07407 | +9.2% | -0.002852 to +0.01539 | no |
| CPU used (cores), mean | 1.627 | 1.638 | +0.7% | -0.002055 to +0.02439 | no |
| Omni's own CPU (cores), mean | 0 | 0.01167 | +0.0117 (native is 0) | +0.01088 to +0.01246 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.627 | 1.65 | +1.4% | +0.009991 to +0.03568 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.6 | 385.2 | -7.3% | -70.9 to +10.24 | no |
| HPA replicas, mean | 2.008 | 2.283 | +13.7% | +0.1076 to +0.4423 | yes: power given |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.3545 to +1.046 | yes: power given |
| pod start wait, total (s) | 0 | 1.4 | +1.4 (native is 0) | +0.4344 to +2.366 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.4 | +1.4 (native is 0) | +0.4344 to +2.366 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.56 | 47.45 | -0.2% | -0.4102 to +0.1926 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 867.2 | 864.2 | -0.3% | -8.985 to +2.985 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.267 | -12.2% | -1.749 to +0.2824 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7 | 0.3625 | -48.2% | -0.7109 to +0.03594 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 1.4 | -33.3% | -2.21 to +0.8099 | no |
| queue: job turnaround, submitted to done, mean (s) | 176.3 | 170 | -3.6% | -11.97 to -0.5472 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.707 | -4.9% | -0.7174 to +0.1321 | no |
| node-hours | 2.513 | 2.39 | -4.9% | -0.3046 to +0.0595 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275 | +0.0% | -0.5965 to +0.8415 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 265.8 | -3.3% | -22.86 to +4.752 | no |
| response time (ms), mean | 552.1 | 561.7 | +1.7% | -19.53 to +38.78 | no |
| response time (ms), 95th percentile | 2224 | 2333 | +4.9% | -108 to +326 | no |
| response time (ms), 99th percentile | 3162 | 3285 | +3.9% | -42.95 to +288 | no |
| time over the response line (% of samples) | 24.21 | 23.61 | -2.5% | -1.068 to -0.1453 | yes: GAIN |
| failed requests (%) | 0.01156 | 0 | -100.0% | -0.03771 to +0.01459 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 12 | +0.8% | -0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.1 | +8.1 (native is 0) | +5.852 to +10.35 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.51 | 23.47 | +14.4% | +0.4016 to +5.515 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06814 | 0.0715 | +4.9% | -0.0009757 to +0.007694 | no |
| CPU used (cores), mean | 1.635 | 1.641 | +0.3% | -0.01128 to +0.02191 | no |
| Omni's own CPU (cores), mean | 0 | 0.01223 | +0.0122 (native is 0) | +0.01133 to +0.01313 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.635 | 1.653 | +1.1% | +0.0007968 to +0.03429 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.6 | 394.1 | -4.5% | -42.03 to +5.154 | no |
| HPA replicas, mean | 2.079 | 2.211 | +6.4% | -0.08377 to +0.3483 | no |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | -0.0802 to +1.88 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | +0.0214 to +1.379 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.73 | 48.1 | +2.9% | +0.8577 to +1.873 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 861.8 | 872.2 | +1.2% | -0.365 to +21.17 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.437 | -9.4% | -1.377 to +0.2517 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4958 | 0.4167 | -16.0% | -0.5442 to +0.3859 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.1 | 1.9 | -38.7% | -4.5 to +2.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 168.1 | 181.9 | +8.2% | +2.477 to +25.17 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*