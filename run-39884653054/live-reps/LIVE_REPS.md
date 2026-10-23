# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.709 | 4.5 |
| node-hours | 2.514 | 2.514 | 1.973 | 1.886 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.9 | 269.6 | 270 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 269.9 | 229.1 | 222.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 220.5 | 249.3 | 198.7 | 211.6 |
| response time (ms), 95th percentile | 649.6 | 961.7 | 727.9 | 911 |
| response time (ms), 99th percentile | 959.6 | 1447 | 1089 | 1406 |
| time over the response line (% of samples) | 8.691 | 7.199 | 9.201 | 6.783 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 4.4 | 5.8 | 4.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 168.1 | 110 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | 83.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 14.11 | 8.612 | 13.64 |
| utilisation (used / allocatable) | 0.05301 | 0.0532 | 0.06672 | 0.07162 |
| CPU used (cores), mean | 1.272 | 1.277 | 1.253 | 1.266 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04412 | 0.04963 |
| CPU used with Omni's own (cores), mean | 1.272 | 1.277 | 1.297 | 1.316 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 517 | 518.8 | 441.4 | 422.6 |
| HPA replicas, mean | 2.107 | 2.045 | 2.316 | 2.384 |
| pods started | 0.1 | 0 | 0.4 | 1.1 |
| pod start wait, total (s) | 0.1 | 0 | 0.8 | 1.9 |
| pod start wait, mean (s) | 0.1 | 0 | 0.6 | 0.7167 |
| host CPU busy, the real machine under kind (%) | 36.29 | 38.37 | 38.1 | 40.42 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 739.8 | 757.3 | 744.3 | 760.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.667 | 3.415 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7792 | 0.05 | 0.6625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | 0.3 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 46.84 | 66.52 | 51.84 | 67.76 |
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
| worker nodes in service, mean | 6 | 4.5 | -25.0% | -2.223 to -0.7764 | yes: GAIN |
| node-hours | 2.514 | 1.886 | -25.0% | -0.9353 to -0.3209 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 270 | +0.0% | -0.723 to +0.8578 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 222.9 | -17.4% | -70.29 to -23.74 | yes: GAIN |
| response time (ms), mean | 249.3 | 211.6 | -15.1% | -62.36 to -13.15 | yes: GAIN |
| response time (ms), 95th percentile | 961.7 | 911 | -5.3% | -185.2 to +83.77 | no |
| response time (ms), 99th percentile | 1447 | 1406 | -2.8% | -111.9 to +31.07 | no |
| time over the response line (% of samples) | 7.199 | 6.783 | -5.8% | -1.378 to +0.5455 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 4.6 | +4.5% | -0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110 | +110 (native is 0) | +84.63 to +135.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 13.64 | -3.3% | -1.703 to +0.7635 | no |
| utilisation (used / allocatable) | 0.0532 | 0.07162 | +34.6% | +0.009044 to +0.02779 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.277 | 1.266 | -0.8% | -0.05751 to +0.036 | no |
| Omni's own CPU (cores), mean | 0 | 0.04963 | +0.0496 (native is 0) | +0.04281 to +0.05645 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.277 | 1.316 | +3.0% | -0.007087 to +0.08484 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518.8 | 422.6 | -18.5% | -145.6 to -46.78 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.045 | 2.384 | +16.6% | -0.02239 to +0.7011 | no |
| pods started | 0 | 1.1 | +1.1 (native is 0) | -0.04101 to +2.241 | no |
| pod start wait, total (s) | 0 | 1.9 | +1.9 (native is 0) | -0.02085 to +3.821 | no |
| pod start wait, mean (s) | 0 | 0.7167 | +0.717 (native is 0) | +0.04685 to +1.386 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.37 | 40.42 | +5.4% | +1.485 to +2.627 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.3 | 760.9 | +0.5% | -0.3784 to +7.578 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.415 | -43.1% | -3.776 to -1.395 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.6625 | -15.0% | -0.1983 to -0.03498 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.2 | -7.7% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 66.52 | 67.76 | +1.9% | -4.106 to +6.589 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.599e-15 to +1.779e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.514 | +0.0% | -0.00684 to +0.007174 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.9 | +0.1% | -0.5088 to +0.9448 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 269.9 | +0.1% | -0.5088 to +0.9448 | no |
| response time (ms), mean | 220.5 | 249.3 | +13.1% | -13.5 to +71.2 | no |
| response time (ms), 95th percentile | 649.6 | 961.7 | +48.1% | -55.76 to +680.1 | no |
| response time (ms), 99th percentile | 959.6 | 1447 | +50.8% | -123.3 to +1098 | no |
| time over the response line (% of samples) | 8.691 | 7.199 | -17.2% | -3.003 to +0.02095 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 4.4 | -17.0% | -2.268 to +0.4676 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 14.11 | +55.4% | +3.071 to +6.996 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05301 | 0.0532 | +0.4% | -0.001023 to +0.001398 | no |
| CPU used (cores), mean | 1.272 | 1.277 | +0.4% | -0.02455 to +0.03356 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.272 | 1.277 | +0.4% | -0.02455 to +0.03356 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 517 | 518.8 | +0.3% | -11.76 to +15.37 | no |
| HPA replicas, mean | 2.107 | 2.045 | -2.9% | -0.2197 to +0.0957 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 36.29 | 38.37 | +5.7% | +1.355 to +2.802 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.8 | 757.3 | +2.4% | +0.6257 to +34.37 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.7792 | +1458.3% | +0.6183 to +0.84 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | +225.0% | +0.494 to +1.306 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 46.84 | 66.52 | +42.0% | +0.3621 to +39 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.709 | -21.5% | -1.983 to -0.5991 | yes: GAIN |
| node-hours | 2.514 | 1.973 | -21.5% | -0.8309 to -0.2514 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.6 | -0.0% | -0.9117 to +0.7613 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 229.1 | -15.1% | -62.77 to -18.46 | yes: GAIN |
| response time (ms), mean | 220.5 | 198.7 | -9.9% | -35.09 to -8.518 | yes: GAIN |
| response time (ms), 95th percentile | 649.6 | 727.9 | +12.1% | -13.37 to +170 | no |
| response time (ms), 99th percentile | 959.6 | 1089 | +13.5% | -67.75 to +327.2 | no |
| time over the response line (% of samples) | 8.691 | 9.201 | +5.9% | -0.07047 to +1.092 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 5.8 | +9.4% | -0.343 to +1.343 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 168.1 | +168 (native is 0) | +112.6 to +223.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 8.612 | -5.2% | -2.304 to +1.367 | no |
| utilisation (used / allocatable) | 0.05301 | 0.06672 | +25.9% | +0.006808 to +0.0206 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.272 | 1.253 | -1.5% | -0.05647 to +0.01726 | no |
| Omni's own CPU (cores), mean | 0 | 0.04412 | +0.0441 (native is 0) | +0.0382 to +0.05004 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.272 | 1.297 | +1.9% | -0.01635 to +0.06538 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 517 | 441.4 | -14.6% | -113.7 to -37.53 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.107 | 2.316 | +9.9% | -0.1062 to +0.5252 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.1 | 0.8 | +700.0% | -0.4209 to +1.821 | no |
| pod start wait, mean (s) | 0.1 | 0.6 | +500.0% | -0.343 to +1.343 | no |
| host CPU busy, the real machine under kind (%) | 36.29 | 38.1 | +5.0% | +1.28 to +2.348 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.8 | 744.3 | +0.6% | -1.478 to +10.48 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.667 | -38.9% | -3.506 to -1.161 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05 | +0.0% | -0.04443 to +0.04443 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | -25.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 46.84 | 51.84 | +10.7% | -1.851 to +11.85 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.709 | -21.5% | -1.983 to -0.5991 | yes: GAIN |
| node-hours | 2.514 | 1.973 | -21.5% | -0.8325 to -0.2501 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 269.6 | -0.1% | -1.43 to +0.8433 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 229.1 | -15.1% | -63.06 to -18.6 | yes: GAIN |
| response time (ms), mean | 249.3 | 198.7 | -20.3% | -85.31 to -16 | yes: GAIN |
| response time (ms), 95th percentile | 961.7 | 727.9 | -24.3% | -546.8 to +79.1 | no |
| response time (ms), 99th percentile | 1447 | 1089 | -24.7% | -841.1 to +126.2 | no |
| time over the response line (% of samples) | 7.199 | 9.201 | +27.8% | +0.4277 to +3.576 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 5.8 | +31.8% | -0.326 to +3.126 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 168.1 | +168 (native is 0) | +112.6 to +223.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 8.612 | -39.0% | -7.459 to -3.544 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0532 | 0.06672 | +25.4% | +0.006226 to +0.02081 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.277 | 1.253 | -1.9% | -0.06002 to +0.01179 | no |
| Omni's own CPU (cores), mean | 0 | 0.04412 | +0.0441 (native is 0) | +0.0382 to +0.05004 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.277 | 1.297 | +1.6% | -0.01642 to +0.05643 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518.8 | 441.4 | -14.9% | -121.4 to -33.51 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.045 | 2.316 | +13.3% | -0.05706 to +0.6 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | -0.2556 to +1.856 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 38.37 | 38.1 | -0.7% | -0.6916 to +0.1619 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.3 | 744.3 | -1.7% | -25.53 to -0.4736 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.667 | -38.9% | -3.506 to -1.161 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.05 | -93.6% | -0.8226 to -0.6357 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.3 | -76.9% | -1.337 to -0.6628 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 66.52 | 51.84 | -22.1% | -28.28 to -1.079 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.5 | -25.0% | -2.223 to -0.7764 | yes: GAIN |
| node-hours | 2.514 | 1.886 | -25.0% | -0.9325 to -0.3233 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 270 | +0.1% | -0.437 to +1.008 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 222.9 | -17.4% | -69.88 to -23.71 | yes: GAIN |
| response time (ms), mean | 220.5 | 211.6 | -4.0% | -41.36 to +23.56 | no |
| response time (ms), 95th percentile | 649.6 | 911 | +40.3% | -59.89 to +582.8 | no |
| response time (ms), 99th percentile | 959.6 | 1406 | +46.6% | -128.9 to +1022 | no |
| time over the response line (% of samples) | 8.691 | 6.783 | -22.0% | -3.702 to -0.113 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 4.6 | -13.2% | -2.133 to +0.7326 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110 | +110 (native is 0) | +84.63 to +135.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.08 | 13.64 | +50.3% | +2.935 to +6.192 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05301 | 0.07162 | +35.1% | +0.009552 to +0.02765 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.272 | 1.266 | -0.5% | -0.03827 to +0.02577 | no |
| Omni's own CPU (cores), mean | 0 | 0.04963 | +0.0496 (native is 0) | +0.04281 to +0.05645 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.272 | 1.316 | +3.4% | +0.008953 to +0.07781 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 517 | 422.6 | -18.3% | -136.8 to -51.95 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.107 | 2.384 | +13.2% | -0.07127 to +0.626 | no |
| pods started | 0.1 | 1.1 | +1000.0% | -0.2158 to +2.216 | no |
| pod start wait, total (s) | 0.1 | 1.9 | +1800.0% | -0.1892 to +3.789 | no |
| pod start wait, mean (s) | 0.1 | 0.7167 | +616.7% | -0.1458 to +1.379 | no |
| host CPU busy, the real machine under kind (%) | 36.29 | 40.42 | +11.4% | +3.361 to +4.908 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.8 | 760.9 | +2.9% | +0.6071 to +41.59 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.415 | -43.1% | -3.776 to -1.395 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.6625 | +1225.0% | +0.5225 to +0.7025 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.2 | +200.0% | +0.4984 to +1.102 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 46.84 | 67.76 | +44.7% | +0.2399 to +41.6 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*