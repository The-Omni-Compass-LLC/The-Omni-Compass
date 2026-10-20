# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.209 | 5.639 |
| node-hours | 2.516 | 2.514 | 2.185 | 2.363 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273 | 273.3 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273 | 248.5 | 262 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 347.3 | 410.9 | 296.1 | 371.1 |
| response time (ms), 95th percentile | 1135 | 1712 | 1150 | 1788 |
| response time (ms), 99th percentile | 1712 | 2761 | 1697 | 2775 |
| time over the response line (% of samples) | 20.59 | 17.63 | 19.09 | 17.46 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.6 | 11 | 11.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 43.6 | 30.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.97 | 17.31 | 10.18 | 17.2 |
| utilisation (used / allocatable) | 0.06162 | 0.06178 | 0.07138 | 0.06637 |
| CPU used (cores), mean | 1.479 | 1.483 | 1.47 | 1.493 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01791 | 0.0184 |
| CPU used with Omni's own (cores), mean | 1.479 | 1.483 | 1.488 | 1.512 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 443.4 | 403.6 | 420.1 |
| HPA replicas, mean | 2.089 | 1.98 | 2.013 | 2.209 |
| pods started | 0 | 0.3 | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.6 | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.4 | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 42.16 | 44.52 | 42.92 | 45.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 772.7 | 807.9 | 773.3 | 812.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.545 | 5.303 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.8458 | 0.07083 | 0.8042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.4 | 0.5 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 82.27 | 119.4 | 82.29 | 125.4 |
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
| worker nodes in service, mean | 6 | 5.639 | -6.0% | -0.7319 to +0.01046 | no |
| node-hours | 2.514 | 2.363 | -6.0% | -0.3105 to +0.009121 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.3 | +0.1% | -0.8252 to +1.378 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 262 | -4.0% | -23.11 to +1.034 | no |
| response time (ms), mean | 410.9 | 371.1 | -9.7% | -68.37 to -11.15 | yes: GAIN |
| response time (ms), 95th percentile | 1712 | 1788 | +4.4% | -122.1 to +273.1 | no |
| response time (ms), 99th percentile | 2761 | 2775 | +0.5% | -254.3 to +281.5 | no |
| time over the response line (% of samples) | 17.63 | 17.46 | -1.0% | -2.405 to +2.062 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.5 | -0.9% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.8 | +30.8 (native is 0) | +25.73 to +35.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.31 | 17.2 | -0.6% | -2.006 to +1.786 | no |
| utilisation (used / allocatable) | 0.06178 | 0.06637 | +7.4% | +0.0002799 to +0.008889 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.483 | 1.493 | +0.7% | -0.01018 to +0.03114 | no |
| Omni's own CPU (cores), mean | 0 | 0.0184 | +0.0184 (native is 0) | +0.01509 to +0.02171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.483 | 1.512 | +1.9% | +0.009397 to +0.04836 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.4 | 420.1 | -5.3% | -45.35 to -1.225 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.98 | 2.209 | +11.6% | +0.03224 to +0.4261 | yes: power given |
| pods started | 0.3 | 0.4 | +33.3% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.6 | 0.5 | -16.7% | -1.137 to +0.9366 | no |
| pod start wait, mean (s) | 0.4 | 0.5 | +25.0% | -0.6872 to +0.8872 | no |
| host CPU busy, the real machine under kind (%) | 44.52 | 45.58 | +2.4% | +0.5775 to +1.552 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 807.9 | 812.4 | +0.6% | -2.136 to +11.14 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.303 | -11.6% | -1.348 to -0.04576 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8458 | 0.8042 | -4.9% | -0.109 to +0.02571 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.6 | +14.3% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 119.4 | 125.4 | +5.0% | +0.1921 to +11.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.057e-15 to +8.793e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.514 | -0.1% | -0.01143 to +0.007761 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273 | -0.0% | -1.096 to +0.8924 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273 | -0.0% | -1.096 to +0.8924 | no |
| response time (ms), mean | 347.3 | 410.9 | +18.3% | +25.98 to +101.2 | yes: LOSS |
| response time (ms), 95th percentile | 1135 | 1712 | +50.8% | +256.7 to +897 | yes: LOSS |
| response time (ms), 99th percentile | 1712 | 2761 | +61.3% | +527.6 to +1571 | yes: LOSS |
| time over the response line (% of samples) | 20.59 | 17.63 | -14.4% | -5.384 to -0.5269 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.6 | +6.4% | +0.2172 to +1.183 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.97 | 17.31 | +57.8% | +4.25 to +8.423 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06162 | 0.06178 | +0.3% | -0.0009662 to +0.001281 | no |
| CPU used (cores), mean | 1.479 | 1.483 | +0.3% | -0.02319 to +0.03075 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.479 | 1.483 | +0.3% | -0.02319 to +0.03075 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 443.4 | -0.0% | -8.429 to +8.185 | no |
| HPA replicas, mean | 2.089 | 1.98 | -5.2% | -0.3544 to +0.1356 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.3656 to +1.566 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 42.16 | 44.52 | +5.6% | +1.92 to +2.805 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.7 | 807.9 | +4.6% | +20.81 to +49.59 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.8458 | +968.4% | +0.6559 to +0.8775 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.4 | +100.0% | +0.2172 to +1.183 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.27 | 119.4 | +45.2% | +22.06 to +52.29 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.209 | -13.2% | -1.356 to -0.2261 | yes: GAIN |
| node-hours | 2.516 | 2.185 | -13.1% | -0.5662 to -0.09517 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.3 | +0.1% | -0.3278 to +0.7591 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 248.5 | -9.0% | -42.4 to -6.918 | yes: GAIN |
| response time (ms), mean | 347.3 | 296.1 | -14.7% | -76.74 to -25.53 | yes: GAIN |
| response time (ms), 95th percentile | 1135 | 1150 | +1.3% | -97.72 to +127.7 | no |
| response time (ms), 99th percentile | 1712 | 1697 | -0.9% | -281.8 to +251.6 | no |
| time over the response line (% of samples) | 20.59 | 19.09 | -7.3% | -2.405 to -0.5977 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11 | +0.9% | -0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 | +43.6 (native is 0) | +31.77 to +55.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.97 | 10.18 | -7.2% | -2.692 to +1.108 | no |
| utilisation (used / allocatable) | 0.06162 | 0.07138 | +15.8% | +0.002119 to +0.01738 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.479 | 1.47 | -0.6% | -0.03741 to +0.01877 | no |
| Omni's own CPU (cores), mean | 0 | 0.01791 | +0.0179 (native is 0) | +0.01675 to +0.01907 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.488 | +0.6% | -0.0202 to +0.03738 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 403.6 | -9.0% | -68.54 to -11.32 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.089 | 2.013 | -3.6% | -0.3612 to +0.2091 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 42.16 | 42.92 | +1.8% | +0.2699 to +1.26 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.7 | 773.3 | +0.1% | -6.634 to +7.834 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.545 | -24.2% | -2.3 to -0.6094 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.07083 | -10.5% | -0.03912 to +0.02245 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.5 | -28.6% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.27 | 82.29 | +0.0% | -9.163 to +9.204 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.209 | -13.2% | -1.356 to -0.2261 | yes: GAIN |
| node-hours | 2.514 | 2.185 | -13.1% | -0.5677 to -0.08994 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.3 | +0.1% | -0.622 to +1.257 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 248.5 | -9.0% | -42.42 to -6.698 | yes: GAIN |
| response time (ms), mean | 410.9 | 296.1 | -27.9% | -164.3 to -65.18 | yes: GAIN |
| response time (ms), 95th percentile | 1712 | 1150 | -32.8% | -901.6 to -222.1 | yes: GAIN |
| response time (ms), 99th percentile | 2761 | 1697 | -38.5% | -1582 to -546.1 | yes: GAIN |
| time over the response line (% of samples) | 17.63 | 19.09 | +8.2% | -0.3534 to +3.262 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11 | -5.2% | -1.1 to -0.09985 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 | +43.6 (native is 0) | +31.77 to +55.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.31 | 10.18 | -41.2% | -8.785 to -5.471 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06178 | 0.07138 | +15.5% | +0.001439 to +0.01775 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.483 | 1.47 | -0.9% | -0.03028 to +0.004083 | no |
| Omni's own CPU (cores), mean | 0 | 0.01791 | +0.0179 (native is 0) | +0.01675 to +0.01907 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.483 | 1.488 | +0.3% | -0.01263 to +0.02225 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.4 | 403.6 | -9.0% | -73.19 to -6.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.98 | 2.013 | +1.7% | -0.07882 to +0.1455 | no |
| pods started | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| pod start wait, mean (s) | 0.4 | 0 | -100.0% | -1.003 to +0.2032 | no |
| host CPU busy, the real machine under kind (%) | 44.52 | 42.92 | -3.6% | -2.121 to -1.074 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 807.9 | 773.3 | -4.3% | -48.34 to -20.86 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.545 | -24.2% | -2.3 to -0.6094 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8458 | 0.07083 | -91.6% | -0.8884 to -0.6616 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.5 | -64.3% | -1.306 to -0.494 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 119.4 | 82.29 | -31.1% | -52.04 to -22.27 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.639 | -6.0% | -0.7319 to +0.01046 | no |
| node-hours | 2.516 | 2.363 | -6.1% | -0.3081 to +0.003113 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.3 | +0.1% | -0.5404 to +0.8887 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 262 | -4.1% | -22.83 to +0.551 | no |
| response time (ms), mean | 347.3 | 371.1 | +6.9% | -8.031 to +55.7 | no |
| response time (ms), 95th percentile | 1135 | 1788 | +57.5% | +365.7 to +939 | yes: LOSS |
| response time (ms), 99th percentile | 1712 | 2775 | +62.1% | +566.2 to +1559 | yes: LOSS |
| time over the response line (% of samples) | 20.59 | 17.46 | -15.2% | -7.156 to +0.9018 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.5 | +5.5% | +0.09985 to +1.1 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.8 | +30.8 (native is 0) | +25.73 to +35.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.97 | 17.2 | +56.8% | +3.925 to +8.529 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06162 | 0.06637 | +7.7% | +0.0005002 to +0.008984 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.479 | 1.493 | +1.0% | -0.009999 to +0.03852 | no |
| Omni's own CPU (cores), mean | 0 | 0.0184 | +0.0184 (native is 0) | +0.01509 to +0.02171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.512 | +2.2% | +0.007544 to +0.05778 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.5 | 420.1 | -5.3% | -43.56 to -3.25 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.089 | 2.209 | +5.7% | -0.1872 to +0.4267 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| host CPU busy, the real machine under kind (%) | 42.16 | 45.58 | +8.1% | +2.828 to +4.027 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772.7 | 812.4 | +5.1% | +23.02 to +56.38 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.303 | -11.6% | -1.348 to -0.04576 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.8042 | +915.8% | +0.6393 to +0.8107 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.6 | +128.6% | +0.494 to +1.306 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.27 | 125.4 | +52.5% | +25.54 to +60.81 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*