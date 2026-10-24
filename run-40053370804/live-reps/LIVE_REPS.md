# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.173 | 5.299 |
| node-hours | 2.512 | 2.507 | 2.169 | 2.22 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.2 | 272.3 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271.2 | 246.3 | 249.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 293.2 | 354.7 | 268.9 | 308.2 |
| response time (ms), 95th percentile | 931.6 | 1467 | 1025 | 1395 |
| response time (ms), 99th percentile | 1313 | 2237 | 1458 | 2156 |
| time over the response line (% of samples) | 16.42 | 14.76 | 17.26 | 14.57 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | 9.8 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 35.3 | 35.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.782 | 15.53 | 10.3 | 15.12 |
| utilisation (used / allocatable) | 0.05892 | 0.05874 | 0.0687 | 0.06761 |
| CPU used (cores), mean | 1.414 | 1.41 | 1.408 | 1.406 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01624 | 0.01852 |
| CPU used with Omni's own (cores), mean | 1.414 | 1.41 | 1.424 | 1.425 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.9 | 470.3 | 418 | 425.3 |
| HPA replicas, mean | 1.909 | 2.04 | 2.27 | 2.36 |
| pods started | 0 | 0 | 0.5 | 0.4 |
| pod start wait, total (s) | 0 | 0 | 1.2 | 0.6 |
| pod start wait, mean (s) | 0 | 0 | 1.2 | 0.6 |
| host CPU busy, the real machine under kind (%) | 39.97 | 42.38 | 40.9 | 43.08 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 757.2 | 789.3 | 761.5 | 787.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.481 | 4.818 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.8083 | 0.05417 | 0.8125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.6 | 0.3 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 65.35 | 100.3 | 68.9 | 98.66 |
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
| worker nodes in service, mean | 6 | 5.299 | -11.7% | -1.424 to +0.02168 | no |
| node-hours | 2.507 | 2.22 | -11.5% | -0.5916 to +0.01649 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.9 | +0.2% | +0.2184 to +1.086 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 249.9 | -7.9% | -43.86 to +1.179 | no |
| response time (ms), mean | 354.7 | 308.2 | -13.1% | -77.1 to -15.94 | yes: GAIN |
| response time (ms), 95th percentile | 1467 | 1395 | -4.9% | -285.4 to +141 | no |
| response time (ms), 99th percentile | 2237 | 2156 | -3.6% | -305.3 to +143.4 | no |
| time over the response line (% of samples) | 14.76 | 14.57 | -1.2% | -1.068 to +0.7039 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.8 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 | +35.9 (native is 0) | +26.81 to +44.99 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.53 | 15.12 | -2.6% | -2.768 to +1.951 | no |
| utilisation (used / allocatable) | 0.05874 | 0.06761 | +15.1% | -0.001538 to +0.01929 | no |
| CPU used (cores), mean | 1.41 | 1.406 | -0.3% | -0.02609 to +0.01898 | no |
| Omni's own CPU (cores), mean | 0 | 0.01852 | +0.0185 (native is 0) | +0.01646 to +0.02058 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.425 | +1.1% | -0.007582 to +0.0375 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.3 | 425.3 | -9.6% | -99.69 to +9.831 | no |
| HPA replicas, mean | 2.04 | 2.36 | +15.7% | +0.09281 to +0.5473 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| host CPU busy, the real machine under kind (%) | 42.38 | 43.08 | +1.6% | +0.235 to +1.153 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 789.3 | 787.4 | -0.2% | -10.98 to +7.182 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.818 | -19.7% | -2.293 to -0.07033 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8083 | 0.8125 | +0.5% | -0.07336 to +0.0817 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.4 | -12.5% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.3 | 98.66 | -1.6% | -11.01 to +7.761 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.732e-16 to +1.306e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.507 | -0.2% | -0.01306 to +0.004061 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.2 | -0.2% | -1.396 to +0.405 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271.2 | -0.2% | -1.396 to +0.405 | no |
| response time (ms), mean | 293.2 | 354.7 | +21.0% | +19.18 to +103.7 | yes: LOSS |
| response time (ms), 95th percentile | 931.6 | 1467 | +57.5% | +194.5 to +876.8 | yes: LOSS |
| response time (ms), 99th percentile | 1313 | 2237 | +70.4% | +354 to +1494 | yes: LOSS |
| time over the response line (% of samples) | 16.42 | 14.76 | -10.2% | -5.008 to +1.672 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | +1.0% | -1.041 to +1.241 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.782 | 15.53 | +58.7% | +4.352 to +7.135 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05892 | 0.05874 | -0.3% | -0.001495 to +0.001124 | no |
| CPU used (cores), mean | 1.414 | 1.41 | -0.3% | -0.03588 to +0.02698 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.414 | 1.41 | -0.3% | -0.03588 to +0.02698 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.9 | 470.3 | +0.9% | -6.974 to +15.78 | no |
| HPA replicas, mean | 1.909 | 2.04 | +6.8% | -0.001058 to +0.2623 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 39.97 | 42.38 | +6.0% | +1.894 to +2.931 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.2 | 789.3 | +4.2% | +14.23 to +49.97 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.8083 | +1516.7% | +0.6612 to +0.8555 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.6 | +433.3% | +0.9545 to +1.646 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.35 | 100.3 | +53.5% | +16.64 to +53.23 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.173 | -13.8% | -1.518 to -0.1362 | yes: GAIN |
| node-hours | 2.512 | 2.169 | -13.6% | -0.6321 to -0.05303 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.3 | +0.2% | -0.3554 to +1.473 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 246.3 | -9.4% | -47.34 to -3.576 | yes: GAIN |
| response time (ms), mean | 293.2 | 268.9 | -8.3% | -43.62 to -4.976 | yes: GAIN |
| response time (ms), 95th percentile | 931.6 | 1025 | +10.0% | -5.591 to +192.3 | no |
| response time (ms), 99th percentile | 1313 | 1458 | +11.0% | -28.65 to +317.9 | no |
| time over the response line (% of samples) | 16.42 | 17.26 | +5.1% | -1.292 to +2.955 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | +1.0% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.3 | +35.3 (native is 0) | +24.34 to +46.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.782 | 10.3 | +5.3% | -0.6732 to +1.706 | no |
| utilisation (used / allocatable) | 0.05892 | 0.0687 | +16.6% | +0.00201 to +0.01754 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.408 | -0.5% | -0.03607 to +0.02313 | no |
| Omni's own CPU (cores), mean | 0 | 0.01624 | +0.0162 (native is 0) | +0.01499 to +0.01749 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.424 | +0.7% | -0.02011 to +0.03966 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.9 | 418 | -10.3% | -87.03 to -8.786 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.909 | 2.27 | +18.9% | +0.1185 to +0.6031 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | -0.0064 to +2.406 | no |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | -0.0064 to +2.406 | no |
| host CPU busy, the real machine under kind (%) | 39.97 | 40.9 | +2.3% | +0.4554 to +1.417 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.2 | 761.5 | +0.6% | -2.444 to +11.04 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.481 | -25.3% | -2.719 to -0.3182 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05417 | +8.3% | -0.04338 to +0.05171 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.35 | 68.9 | +5.4% | -3.285 to +10.39 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.173 | -13.8% | -1.518 to -0.1362 | yes: GAIN |
| node-hours | 2.507 | 2.169 | -13.5% | -0.6279 to -0.04825 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 272.3 | +0.4% | +0.1048 to +2.004 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 246.3 | -9.2% | -46.53 to -3.393 | yes: GAIN |
| response time (ms), mean | 354.7 | 268.9 | -24.2% | -135.4 to -36.03 | yes: GAIN |
| response time (ms), 95th percentile | 1467 | 1025 | -30.1% | -807.2 to -77.49 | yes: GAIN |
| response time (ms), 99th percentile | 2237 | 1458 | -34.8% | -1342 to -216.5 | yes: GAIN |
| time over the response line (% of samples) | 14.76 | 17.26 | +16.9% | +0.5364 to +4.463 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.8 | +0.0% | -1.216 to +1.216 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.3 | +35.3 (native is 0) | +24.34 to +46.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.53 | 10.3 | -33.7% | -7.257 to -3.196 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05874 | 0.0687 | +17.0% | +0.00114 to +0.01878 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.41 | 1.408 | -0.1% | -0.0281 to +0.02407 | no |
| Omni's own CPU (cores), mean | 0 | 0.01624 | +0.0162 (native is 0) | +0.01499 to +0.01749 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.424 | +1.0% | -0.01166 to +0.04011 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.3 | 418 | -11.1% | -101.6 to -3.029 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.04 | 2.27 | +11.3% | +0.05017 to +0.4101 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | -0.0064 to +2.406 | no |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | -0.0064 to +2.406 | no |
| host CPU busy, the real machine under kind (%) | 42.38 | 40.9 | -3.5% | -2.149 to -0.8031 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 789.3 | 761.5 | -3.5% | -46.89 to -8.714 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.481 | -25.3% | -2.719 to -0.3182 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8083 | 0.05417 | -93.3% | -0.8378 to -0.6705 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.3 | -81.2% | -1.783 to -0.8172 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 100.3 | 68.9 | -31.3% | -50.62 to -12.15 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.299 | -11.7% | -1.424 to +0.02168 | no |
| node-hours | 2.512 | 2.22 | -11.6% | -0.5968 to +0.01273 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.9 | +0.1% | -0.5574 to +0.87 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 249.9 | -8.0% | -44.75 to +1.081 | no |
| response time (ms), mean | 293.2 | 308.2 | +5.1% | -17.73 to +47.58 | no |
| response time (ms), 95th percentile | 931.6 | 1395 | +49.8% | +179.4 to +747.5 | yes: LOSS |
| response time (ms), 99th percentile | 1313 | 2156 | +64.2% | +335.4 to +1351 | yes: LOSS |
| time over the response line (% of samples) | 16.42 | 14.57 | -11.3% | -5.66 to +1.959 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | +1.0% | -1.041 to +1.241 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 | +35.9 (native is 0) | +26.81 to +44.99 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.782 | 15.12 | +54.5% | +2.871 to +7.799 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05892 | 0.06761 | +14.7% | -0.0008942 to +0.01827 | no |
| CPU used (cores), mean | 1.414 | 1.406 | -0.6% | -0.02994 to +0.01392 | no |
| Omni's own CPU (cores), mean | 0 | 0.01852 | +0.0185 (native is 0) | +0.01646 to +0.02058 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.425 | +0.7% | -0.0123 to +0.03331 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.9 | 425.3 | -8.7% | -86.46 to +5.408 | no |
| HPA replicas, mean | 1.909 | 2.36 | +23.6% | +0.2013 to +0.7001 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| host CPU busy, the real machine under kind (%) | 39.97 | 43.08 | +7.8% | +2.594 to +3.619 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.2 | 787.4 | +4.0% | +13.85 to +46.55 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.818 | -19.7% | -2.293 to -0.07033 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.8125 | +1525.0% | +0.6376 to +0.8874 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.4 | +366.7% | +0.694 to +1.506 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.35 | 98.66 | +51.0% | +16.46 to +50.16 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*