# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.042 | 5.369 |
| node-hours | 2.516 | 2.514 | 2.119 | 2.249 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.4 | 271.6 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 271.4 | 241.5 | 251.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 247.9 | 289.3 | 218.8 | 248.5 |
| response time (ms), 95th percentile | 769.9 | 1091 | 799.9 | 1071 |
| response time (ms), 99th percentile | 1061 | 1572 | 1158 | 1562 |
| time over the response line (% of samples) | 9.693 | 9.417 | 9.7 | 8.709 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 7.5 | 7 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 53 | 24.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 33.33 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.635 | 16.69 | 7.618 | 14.97 |
| utilisation (used / allocatable) | 0.05628 | 0.05693 | 0.0674 | 0.06472 |
| CPU used (cores), mean | 1.351 | 1.366 | 1.337 | 1.367 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01611 | 0.01524 |
| CPU used with Omni's own (cores), mean | 1.351 | 1.366 | 1.353 | 1.382 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.8 | 481.8 | 431.4 | 441.9 |
| HPA replicas, mean | 1.999 | 2.027 | 2.222 | 2.221 |
| pods started | 0.3 | 0.3 | 0.4 | 0.7 |
| pod start wait, total (s) | 0.6 | 0.6 | 0.7 | 1.5 |
| pod start wait, mean (s) | 0.4 | 0.6 | 0.7 | 1.3 |
| host CPU busy, the real machine under kind (%) | 38.56 | 41.21 | 39.53 | 41.84 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 750.6 | 773.9 | 751.4 | 772.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.375 | 4.909 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.7667 | 0.05 | 0.8625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.6 | 0.3 | 1.8 |
| queue: job turnaround, submitted to done, mean (s) | 57.12 | 81.21 | 57.79 | 79.8 |
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
| worker nodes in service, mean | 6 | 5.369 | -10.5% | -1.302 to +0.04023 | no |
| node-hours | 2.514 | 2.249 | -10.5% | -0.5405 to +0.01091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.5 | +0.0% | -0.7853 to +0.9849 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 251.6 | -7.3% | -40.35 to +0.8521 | no |
| response time (ms), mean | 289.3 | 248.5 | -14.1% | -55.44 to -26.19 | yes: GAIN |
| response time (ms), 95th percentile | 1091 | 1071 | -1.8% | -72.89 to +32.85 | no |
| response time (ms), 99th percentile | 1572 | 1562 | -0.6% | -88.72 to +68.77 | no |
| time over the response line (% of samples) | 9.417 | 8.709 | -7.5% | -1.501 to +0.08637 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.1 | -5.3% | -2.093 to +1.293 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.3 | +24.3 (native is 0) | +15.78 to +32.82 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.69 | 14.97 | -10.3% | -3.978 to +0.541 | no |
| utilisation (used / allocatable) | 0.05693 | 0.06472 | +13.7% | -0.0007964 to +0.01636 | no |
| CPU used (cores), mean | 1.366 | 1.367 | +0.0% | -0.03483 to +0.03615 | no |
| Omni's own CPU (cores), mean | 0 | 0.01524 | +0.0152 (native is 0) | +0.01381 to +0.01667 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.382 | +1.2% | -0.01948 to +0.05128 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.8 | 441.9 | -8.3% | -83.33 to +3.516 | no |
| HPA replicas, mean | 2.027 | 2.221 | +9.6% | -0.02175 to +0.4113 | no |
| pods started | 0.3 | 0.7 | +133.3% | -0.2032 to +1.003 | no |
| pod start wait, total (s) | 0.6 | 1.5 | +150.0% | -0.5086 to +2.309 | no |
| pod start wait, mean (s) | 0.6 | 1.3 | +116.7% | -0.5181 to +1.918 | no |
| host CPU busy, the real machine under kind (%) | 41.21 | 41.84 | +1.5% | +0.2014 to +1.069 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.9 | 772.6 | -0.2% | -5.233 to +2.633 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.909 | -18.2% | -2.236 to +0.05393 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7667 | 0.8625 | +12.5% | -0.03897 to +0.2306 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.8 | +12.5% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.21 | 79.8 | -1.7% | -4.287 to +1.453 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.776e-15 to +1.118e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.514 | -0.1% | -0.00956 to +0.005226 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.4 | +0.1% | -0.4615 to +0.8276 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 271.4 | +0.1% | -0.4615 to +0.8276 | no |
| response time (ms), mean | 247.9 | 289.3 | +16.7% | -4.951 to +87.83 | no |
| response time (ms), 95th percentile | 769.9 | 1091 | +41.8% | -12.63 to +655.6 | no |
| response time (ms), 99th percentile | 1061 | 1572 | +48.1% | +45.07 to +975.3 | yes: LOSS |
| time over the response line (% of samples) | 9.693 | 9.417 | -2.9% | -2.774 to +2.22 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 7.5 | +21.0% | -1.086 to +3.686 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.635 | 16.69 | +93.3% | +2.009 to +14.1 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05628 | 0.05693 | +1.2% | -0.0009781 to +0.002295 | no |
| CPU used (cores), mean | 1.351 | 1.366 | +1.2% | -0.02347 to +0.05507 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.351 | 1.366 | +1.2% | -0.02347 to +0.05507 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.8 | 481.8 | -0.8% | -17.88 to +9.935 | no |
| HPA replicas, mean | 1.999 | 2.027 | +1.4% | -0.1249 to +0.179 | no |
| pods started | 0.3 | 0.3 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.6 | 0.6 | +0.0% | -1.349 to +1.349 | no |
| pod start wait, mean (s) | 0.4 | 0.6 | +50.0% | -0.8556 to +1.256 | no |
| host CPU busy, the real machine under kind (%) | 38.56 | 41.21 | +6.9% | +1.902 to +3.398 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.6 | 773.9 | +3.1% | +0.06982 to +46.53 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.7667 | +2528.6% | +0.5028 to +0.9722 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.6 | +433.3% | +0.08188 to +2.518 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 57.12 | 81.21 | +42.2% | +4.523 to +43.65 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.042 | -16.0% | -1.671 to -0.2449 | yes: GAIN |
| node-hours | 2.516 | 2.119 | -15.8% | -0.6964 to -0.09738 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.6 | +0.2% | -0.5836 to +1.425 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 241.5 | -11.0% | -52.46 to -6.981 | yes: GAIN |
| response time (ms), mean | 247.9 | 218.8 | -11.8% | -40.81 to -17.48 | yes: GAIN |
| response time (ms), 95th percentile | 769.9 | 799.9 | +3.9% | -54.73 to +114.8 | no |
| response time (ms), 99th percentile | 1061 | 1158 | +9.1% | -38.29 to +232.4 | no |
| time over the response line (% of samples) | 9.693 | 9.7 | +0.1% | -0.7988 to +0.8114 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 7 | +12.9% | -0.01208 to +1.612 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53 | +53 (native is 0) | +34.32 to +71.68 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.635 | 7.618 | -11.8% | -1.997 to -0.03614 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05628 | 0.0674 | +19.8% | +0.002702 to +0.01954 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.351 | 1.337 | -1.0% | -0.04798 to +0.0207 | no |
| Omni's own CPU (cores), mean | 0 | 0.01611 | +0.0161 (native is 0) | +0.01457 to +0.01765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.351 | 1.353 | +0.2% | -0.03161 to +0.03655 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.8 | 431.4 | -11.2% | -92.39 to -16.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.222 | +11.1% | +0.03003 to +0.4157 | yes: power given |
| pods started | 0.3 | 0.4 | +33.3% | -0.6113 to +0.8113 | no |
| pod start wait, total (s) | 0.6 | 0.7 | +16.7% | -1.309 to +1.509 | no |
| pod start wait, mean (s) | 0.4 | 0.7 | +75.0% | -0.8209 to +1.421 | no |
| host CPU busy, the real machine under kind (%) | 38.56 | 39.53 | +2.5% | +0.512 to +1.439 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.6 | 751.4 | +0.1% | -3.042 to +4.642 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.375 | -27.1% | -2.746 to -0.5042 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.05 | +71.4% | -0.017 to +0.05866 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.12 | 57.79 | +1.2% | -1.657 to +2.99 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.042 | -16.0% | -1.671 to -0.2449 | yes: GAIN |
| node-hours | 2.514 | 2.119 | -15.7% | -0.693 to -0.09645 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.6 | +0.1% | -0.7632 to +1.239 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 241.5 | -11.0% | -52.43 to -7.376 | yes: GAIN |
| response time (ms), mean | 289.3 | 218.8 | -24.4% | -119.6 to -21.6 | yes: GAIN |
| response time (ms), 95th percentile | 1091 | 799.9 | -26.7% | -644.7 to +61.72 | no |
| response time (ms), 99th percentile | 1572 | 1158 | -26.3% | -817.9 to -8.38 | yes: GAIN |
| time over the response line (% of samples) | 9.417 | 9.7 | +3.0% | -1.623 to +2.189 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7 | -6.7% | -2.984 to +1.984 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53 | +53 (native is 0) | +34.32 to +71.68 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.69 | 7.618 | -54.3% | -14.94 to -3.2 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05693 | 0.0674 | +18.4% | +0.001542 to +0.01938 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.366 | 1.337 | -2.2% | -0.06376 to +0.004885 | no |
| Omni's own CPU (cores), mean | 0 | 0.01611 | +0.0161 (native is 0) | +0.01457 to +0.01765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.353 | -1.0% | -0.04744 to +0.02079 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.8 | 431.4 | -10.5% | -93.35 to -7.399 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.027 | 2.222 | +9.7% | -0.05032 to +0.4419 | no |
| pods started | 0.3 | 0.4 | +33.3% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.6 | 0.7 | +16.7% | -0.5263 to +0.7263 | no |
| pod start wait, mean (s) | 0.6 | 0.7 | +16.7% | -0.5263 to +0.7263 | no |
| host CPU busy, the real machine under kind (%) | 41.21 | 39.53 | -4.1% | -2.558 to -0.7901 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.9 | 751.4 | -2.9% | -43.2 to -1.798 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.375 | -27.1% | -2.746 to -0.5042 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7667 | 0.05 | -93.5% | -0.9231 to -0.5103 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.3 | -81.2% | -2.518 to -0.08188 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 81.21 | 57.79 | -28.8% | -42.08 to -4.758 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.369 | -10.5% | -1.302 to +0.04023 | no |
| node-hours | 2.516 | 2.249 | -10.6% | -0.5454 to +0.01148 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.5 | +0.1% | -0.5938 to +1.16 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 251.6 | -7.2% | -40.55 to +1.42 | no |
| response time (ms), mean | 247.9 | 248.5 | +0.3% | -34.6 to +35.86 | no |
| response time (ms), 95th percentile | 769.9 | 1071 | +39.2% | -24.65 to +627.6 | no |
| response time (ms), 99th percentile | 1061 | 1562 | +47.1% | -0.7189 to +1001 | no |
| time over the response line (% of samples) | 9.693 | 8.709 | -10.2% | -3.516 to +1.548 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 7.1 | +14.5% | -1.136 to +2.936 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.3 | +24.3 (native is 0) | +15.78 to +32.82 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.635 | 14.97 | +73.4% | +1.157 to +11.51 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05628 | 0.06472 | +15.0% | +0.0003008 to +0.01658 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.351 | 1.367 | +1.2% | -0.0188 to +0.05172 | no |
| Omni's own CPU (cores), mean | 0 | 0.01524 | +0.0152 (native is 0) | +0.01381 to +0.01667 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.351 | 1.382 | +2.3% | -0.003511 to +0.06691 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.8 | 441.9 | -9.0% | -82.14 to -5.621 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.221 | +11.1% | +0.0499 to +0.3938 | yes: power given |
| pods started | 0.3 | 0.7 | +133.3% | -0.2032 to +1.003 | no |
| pod start wait, total (s) | 0.6 | 1.5 | +150.0% | -0.3367 to +2.137 | no |
| pod start wait, mean (s) | 0.4 | 1.3 | +225.0% | +0.1128 to +1.687 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.56 | 41.84 | +8.5% | +2.714 to +3.856 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.6 | 772.6 | +2.9% | +1.02 to +42.98 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.909 | -18.2% | -2.236 to +0.05393 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.8625 | +2857.1% | +0.6788 to +0.9879 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.8 | +500.0% | +0.5315 to +2.469 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 57.12 | 79.8 | +39.7% | +4.576 to +40.77 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*