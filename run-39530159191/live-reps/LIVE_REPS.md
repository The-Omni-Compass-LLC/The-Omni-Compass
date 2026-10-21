# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.302 | 5.446 |
| node-hours | 2.512 | 2.518 | 2.222 | 2.279 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.7 | 272.5 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.7 | 250.5 | 254.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 382.2 | 385.2 | 388.3 | 377.9 |
| response time (ms), 95th percentile | 1428 | 1504 | 1467 | 1494 |
| response time (ms), 99th percentile | 2066 | 2163 | 2143 | 2239 |
| time over the response line (% of samples) | 15.45 | 14.44 | 15.96 | 14.79 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.3 | 9.1 | 8.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 10.9 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.11 | 15.43 | 15.34 | 16.36 |
| utilisation (used / allocatable) | 0.06138 | 0.0609 | 0.0685 | 0.0648 |
| CPU used (cores), mean | 1.473 | 1.462 | 1.444 | 1.425 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01193 | 0.01376 |
| CPU used with Omni's own (cores), mean | 1.473 | 1.462 | 1.456 | 1.439 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.4 | 461.3 | 422.4 | 439.1 |
| HPA replicas, mean | 2.065 | 2.035 | 2.355 | 2.267 |
| pods started | 0 | 0 | 0.5 | 0.4 |
| pod start wait, total (s) | 0 | 0 | 1.2 | 0.7 |
| pod start wait, mean (s) | 0 | 0 | 1.2 | 0.7 |
| host CPU busy, the real machine under kind (%) | 41.93 | 42.78 | 42.64 | 43.34 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 801.2 | 809 | 807.4 | 808.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.81 | 4.972 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3958 | 0.9917 | 0.3083 | 0.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2 | 2 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 109.4 | 117.4 | 113.1 | 115.8 |
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
| worker nodes in service, mean | 6 | 5.446 | -9.2% | -1.057 to -0.05226 | yes: GAIN |
| node-hours | 2.518 | 2.279 | -9.5% | -0.4512 to -0.02661 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 271.6 | -0.4% | -1.872 to -0.2999 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 254.2 | -6.8% | -34.74 to -2.193 | yes: GAIN |
| response time (ms), mean | 385.2 | 377.9 | -1.9% | -27.85 to +13.25 | no |
| response time (ms), 95th percentile | 1504 | 1494 | -0.6% | -209.7 to +190.8 | no |
| response time (ms), 99th percentile | 2163 | 2239 | +3.5% | -133.8 to +285.7 | no |
| time over the response line (% of samples) | 14.44 | 14.79 | +2.5% | -0.4573 to +1.168 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.6 | +3.6% | -0.4578 to +1.058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.7 (native is 0) | +8.327 to +15.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.43 | 16.36 | +6.0% | -2.842 to +4.699 | no |
| utilisation (used / allocatable) | 0.0609 | 0.0648 | +6.4% | -7.713e-05 to +0.007871 | no |
| CPU used (cores), mean | 1.462 | 1.425 | -2.5% | -0.07093 to -0.002751 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01376 | +0.0138 (native is 0) | +0.01188 to +0.01564 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.462 | 1.439 | -1.6% | -0.05673 to +0.01056 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.3 | 439.1 | -4.8% | -46.73 to +2.265 | no |
| HPA replicas, mean | 2.035 | 2.267 | +11.4% | +0.01191 to +0.4517 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | +0.0214 to +1.379 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | +0.0214 to +1.379 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.78 | 43.34 | +1.3% | +0.2176 to +0.9036 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 809 | 808.1 | -0.1% | -3.999 to +2.199 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.972 | -17.1% | -1.955 to -0.101 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9917 | 0.5 | -49.6% | -2.135 to +1.152 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 0.8 | -60.0% | -3.457 to +1.057 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.4 | 115.8 | -1.3% | -7.016 to +3.866 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.216e-15 to +6.83e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.518 | +0.3% | -0.0006364 to +0.0133 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.7 | +0.2% | -0.4557 to +1.289 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.7 | +0.2% | -0.4557 to +1.289 | no |
| response time (ms), mean | 382.2 | 385.2 | +0.8% | -16.2 to +22.06 | no |
| response time (ms), 95th percentile | 1428 | 1504 | +5.3% | -43.59 to +194.7 | no |
| response time (ms), 99th percentile | 2066 | 2163 | +4.7% | -73.53 to +266 | no |
| time over the response line (% of samples) | 15.45 | 14.44 | -6.5% | -1.836 to -0.1798 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.3 | -2.4% | -1.079 to +0.6793 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.11 | 15.43 | +17.8% | -1.68 to +6.337 | no |
| utilisation (used / allocatable) | 0.06138 | 0.0609 | -0.8% | -0.002115 to +0.001166 | no |
| CPU used (cores), mean | 1.473 | 1.462 | -0.8% | -0.05076 to +0.02797 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.473 | 1.462 | -0.8% | -0.05076 to +0.02797 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.4 | 461.3 | +1.1% | -13.04 to +22.94 | no |
| HPA replicas, mean | 2.065 | 2.035 | -1.4% | -0.2278 to +0.1681 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 41.93 | 42.78 | +2.0% | +0.5194 to +1.179 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 801.2 | 809 | +1.0% | +1.493 to +14.11 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3958 | 0.9917 | +150.5% | -0.8974 to +2.089 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2 | +53.8% | -2.182 to +3.582 | no |
| queue: job turnaround, submitted to done, mean (s) | 109.4 | 117.4 | +7.3% | -1.003 to +17.05 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.302 | -11.6% | -1.403 to +0.008008 | no |
| node-hours | 2.512 | 2.222 | -11.5% | -0.589 to +0.01046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.5 | +0.1% | -0.5961 to +0.9689 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 250.5 | -8.0% | -44.57 to +1.076 | no |
| response time (ms), mean | 382.2 | 388.3 | +1.6% | -5.763 to +17.89 | no |
| response time (ms), 95th percentile | 1428 | 1467 | +2.7% | -9.649 to +86.65 | no |
| response time (ms), 99th percentile | 2066 | 2143 | +3.7% | -75.07 to +227.5 | no |
| time over the response line (% of samples) | 15.45 | 15.96 | +3.4% | -0.0408 to +1.077 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 9.1 | +7.1% | -0.8385 to +2.039 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.9 | +10.9 (native is 0) | +8.322 to +13.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.11 | 15.34 | +17.0% | -1.754 to +6.217 | no |
| utilisation (used / allocatable) | 0.06138 | 0.0685 | +11.6% | -0.001172 to +0.01543 | no |
| CPU used (cores), mean | 1.473 | 1.444 | -1.9% | -0.05468 to -0.002744 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01193 | +0.0119 (native is 0) | +0.01116 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.473 | 1.456 | -1.1% | -0.04272 to +0.009152 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.4 | 422.4 | -7.4% | -71.04 to +3.164 | no |
| HPA replicas, mean | 2.065 | 2.355 | +14.1% | +0.132 to +0.4483 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | +0.1997 to +2.2 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | +0.1997 to +2.2 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.93 | 42.64 | +1.7% | +0.3866 to +1.03 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 801.2 | 807.4 | +0.8% | -0.3888 to +12.79 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.81 | -19.8% | -2.327 to -0.05205 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3958 | 0.3083 | -22.1% | -0.2985 to +0.1235 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2 | +53.8% | -0.1953 to +1.595 | no |
| queue: job turnaround, submitted to done, mean (s) | 109.4 | 113.1 | +3.4% | -1.794 to +9.185 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.302 | -11.6% | -1.403 to +0.008008 | no |
| node-hours | 2.518 | 2.222 | -11.7% | -0.5921 to +0.0009051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.5 | -0.1% | -0.9419 to +0.4813 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 250.5 | -8.1% | -44.41 to +0.08378 | no |
| response time (ms), mean | 385.2 | 388.3 | +0.8% | -18.07 to +24.34 | no |
| response time (ms), 95th percentile | 1504 | 1467 | -2.5% | -169.6 to +95.48 | no |
| response time (ms), 99th percentile | 2163 | 2143 | -0.9% | -167.3 to +127.3 | no |
| time over the response line (% of samples) | 14.44 | 15.96 | +10.6% | +0.4942 to +2.558 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 9.1 | +9.6% | -0.4064 to +2.006 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.9 | +10.9 (native is 0) | +8.322 to +13.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.43 | 15.34 | -0.6% | -4.047 to +3.853 | no |
| utilisation (used / allocatable) | 0.0609 | 0.0685 | +12.5% | -0.001246 to +0.01645 | no |
| CPU used (cores), mean | 1.462 | 1.444 | -1.2% | -0.05104 to +0.0164 | no |
| Omni's own CPU (cores), mean | 0 | 0.01193 | +0.0119 (native is 0) | +0.01116 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.462 | 1.456 | -0.4% | -0.03921 to +0.02843 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.3 | 422.4 | -8.4% | -84.09 to +6.31 | no |
| HPA replicas, mean | 2.035 | 2.355 | +15.7% | +0.03211 to +0.6079 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | +0.1997 to +2.2 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | +0.1997 to +2.2 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.78 | 42.64 | -0.3% | -0.4567 to +0.1741 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 809 | 807.4 | -0.2% | -7.838 to +4.638 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.81 | -19.8% | -2.327 to -0.05205 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9917 | 0.3083 | -68.9% | -2.2 to +0.8328 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 2 | +0.0% | -3.035 to +3.035 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.4 | 113.1 | -3.7% | -11.81 to +3.153 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.446 | -9.2% | -1.057 to -0.05226 | yes: GAIN |
| node-hours | 2.512 | 2.279 | -9.3% | -0.4477 to -0.01751 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.6 | -0.2% | -1.85 to +0.5111 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 254.2 | -6.6% | -34.9 to -1.202 | yes: GAIN |
| response time (ms), mean | 382.2 | 377.9 | -1.1% | -21.52 to +12.79 | no |
| response time (ms), 95th percentile | 1428 | 1494 | +4.6% | -80.86 to +213 | no |
| response time (ms), 99th percentile | 2066 | 2239 | +8.3% | -50.72 to +395 | no |
| time over the response line (% of samples) | 15.45 | 14.79 | -4.2% | -1.724 to +0.4183 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.6 | +1.2% | -0.6113 to +0.8113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.7 (native is 0) | +8.327 to +15.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.11 | 16.36 | +24.9% | -0.3338 to +6.847 | no |
| utilisation (used / allocatable) | 0.06138 | 0.0648 | +5.6% | +2.577e-05 to +0.006819 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.473 | 1.425 | -3.3% | -0.09244 to -0.004035 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01376 | +0.0138 (native is 0) | +0.01188 to +0.01564 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.473 | 1.439 | -2.3% | -0.0778 to +0.00885 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.4 | 439.1 | -3.8% | -34.54 to -0.02186 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.065 | 2.267 | +9.8% | -0.02704 to +0.4309 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | +0.0214 to +1.379 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | +0.0214 to +1.379 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.93 | 43.34 | +3.4% | +1.15 to +1.67 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 801.2 | 808.1 | +0.9% | +2.296 to +11.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.972 | -17.1% | -1.955 to -0.101 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3958 | 0.5 | +26.3% | -0.259 to +0.4674 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.8 | -38.5% | -2.194 to +1.194 | no |
| queue: job turnaround, submitted to done, mean (s) | 109.4 | 115.8 | +5.9% | +0.1625 to +12.74 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*