# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.75 | 10.89 |
| node-hours | 5.021 | 5.031 | 4.5 | 4.564 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 526.1 | 524.8 | 525.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 526.1 | 485.6 | 491 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 561.7 | 757.8 | 542 | 711.9 |
| response time (ms), 95th percentile | 2181 | 3385 | 2339 | 3429 |
| response time (ms), 99th percentile | 3053 | 4740 | 3333 | 4870 |
| time over the response line (% of samples) | 20.8 | 23.11 | 21.31 | 24.17 |
| failed requests (%) | 0 | 0.08573 | 0 | 0.1344 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 13.6 | 11.7 | 14.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 96.3 | 48.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.94 | 21.9 | 14.24 | 30.23 |
| utilisation (used / allocatable) | 0.03388 | 0.03475 | 0.03802 | 0.03824 |
| CPU used (cores), mean | 1.626 | 1.668 | 1.629 | 1.668 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01211 | 0.00956 |
| CPU used with Omni's own (cores), mean | 1.626 | 1.668 | 1.641 | 1.677 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.2 | 785.8 | 723.5 | 716.6 |
| HPA replicas, mean | 3.913 | 4.027 | 4.66 | 4.759 |
| pods started | 0 | 0.3 | 1.5 | 1.3 |
| pod start wait, total (s) | 0 | 0.7 | 2.5 | 2.7 |
| pod start wait, mean (s) | 0 | 0.4 | 1.3 | 1.283 |
| host CPU busy, the real machine under kind (%) | 49.35 | 55.63 | 51.02 | 57.68 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 855.2 | 957.1 | 868.4 | 980.1 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.914 | 10.14 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 3.138 | 0.05 | 7.138 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.2 | 0.3 | 33.4 |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 259.5 | 174.2 | 279.7 |
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
| worker nodes in service, mean | 12 | 10.89 | -9.2% | -2.473 to +0.2543 | no |
| node-hours | 5.031 | 4.564 | -9.3% | -1.035 to +0.09988 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 525.9 | -0.0% | -2.294 to +1.837 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 491 | -6.7% | -77.63 to +7.482 | no |
| response time (ms), mean | 757.8 | 711.9 | -6.1% | -132.6 to +40.72 | no |
| response time (ms), 95th percentile | 3385 | 3429 | +1.3% | -453.9 to +542 | no |
| response time (ms), 99th percentile | 4740 | 4870 | +2.7% | -177.2 to +436 | no |
| time over the response line (% of samples) | 23.11 | 24.17 | +4.6% | -0.7245 to +2.851 | no |
| failed requests (%) | 0.08573 | 0.1344 | +56.8% | -0.0824 to +0.1797 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.6 | 14.1 | +3.7% | -0.005799 to +1.006 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.1 | +48.1 (native is 0) | +30.88 to +65.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.9 | 30.23 | +38.0% | -6.226 to +22.88 | no |
| utilisation (used / allocatable) | 0.03475 | 0.03824 | +10.1% | -0.001126 to +0.008113 | no |
| CPU used (cores), mean | 1.668 | 1.668 | -0.0% | -0.09131 to +0.09104 | no |
| Omni's own CPU (cores), mean | 0 | 0.00956 | +0.00956 (native is 0) | +0.00852 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.668 | 1.677 | +0.6% | -0.08173 to +0.1006 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.8 | 716.6 | -8.8% | -156.2 to +17.89 | no |
| HPA replicas, mean | 4.027 | 4.759 | +18.2% | +0.3534 to +1.111 | yes: power given |
| pods started | 0.3 | 1.3 | +333.3% | -0.06632 to +2.066 | no |
| pod start wait, total (s) | 0.7 | 2.7 | +285.7% | -0.9202 to +4.92 | no |
| pod start wait, mean (s) | 0.4 | 1.283 | +220.8% | -0.5418 to +2.308 | no |
| host CPU busy, the real machine under kind (%) | 55.63 | 57.68 | +3.7% | +1.001 to +3.103 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 957.1 | 980.1 | +2.4% | +0.6378 to +45.36 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.14 | -15.5% | -4.06 to +0.3484 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 3.138 | 7.138 | +127.5% | -2.442 to +10.44 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 33.4 | +2683.3% | -39.63 to +104 | no |
| queue: job turnaround, submitted to done, mean (s) | 259.5 | 279.7 | +7.8% | -2.933 to +43.18 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -6.856e-15 to +1.882e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.021 | 5.031 | +0.2% | +0.000689 to +0.02064 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 526.1 | +0.3% | +0.1285 to +3.532 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 526.1 | +0.3% | +0.1285 to +3.532 | yes: power given |
| response time (ms), mean | 561.7 | 757.8 | +34.9% | +75.43 to +316.8 | yes: LOSS |
| response time (ms), 95th percentile | 2181 | 3385 | +55.2% | +530.5 to +1877 | yes: LOSS |
| response time (ms), 99th percentile | 3053 | 4740 | +55.3% | +721.4 to +2654 | yes: LOSS |
| time over the response line (% of samples) | 20.8 | 23.11 | +11.1% | -0.6369 to +5.246 | no |
| failed requests (%) | 0 | 0.08573 | +0.0857 (native is 0) | +0.001645 to +0.1698 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 13.6 | +29.5% | +1.209 to +4.991 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.94 | 21.9 | +57.1% | -1.23 to +17.15 | no |
| utilisation (used / allocatable) | 0.03388 | 0.03475 | +2.6% | -0.00091 to +0.00264 | no |
| CPU used (cores), mean | 1.626 | 1.668 | +2.6% | -0.04368 to +0.1267 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.626 | 1.668 | +2.6% | -0.04368 to +0.1267 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.2 | 785.8 | -1.2% | -42.9 to +24.04 | no |
| HPA replicas, mean | 3.913 | 4.027 | +2.9% | +0.0007012 to +0.2268 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.6509 to +2.051 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2911 to +1.091 | no |
| host CPU busy, the real machine under kind (%) | 49.35 | 55.63 | +12.7% | +4.503 to +8.049 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 855.2 | 957.1 | +11.9% | +43.12 to +160.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 3.138 | +3322.7% | -1.133 to +7.224 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1.2 | +50.0% | -0.1001 to +0.9001 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 259.5 | +57.9% | +41.89 to +148.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.75 | -10.4% | -2.704 to +0.2046 | no |
| node-hours | 5.021 | 4.5 | -10.4% | -1.128 to +0.08706 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 524.8 | +0.1% | -0.2213 to +1.215 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 485.6 | -7.4% | -84.36 to +7.048 | no |
| response time (ms), mean | 561.7 | 542 | -3.5% | -33.07 to -6.472 | yes: GAIN |
| response time (ms), 95th percentile | 2181 | 2339 | +7.3% | +82.44 to +233.9 | yes: LOSS |
| response time (ms), 99th percentile | 3053 | 3333 | +9.2% | +101.2 to +460.5 | yes: LOSS |
| time over the response line (% of samples) | 20.8 | 21.31 | +2.5% | -0.7089 to +1.728 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 11.7 | +11.4% | -0.09723 to +2.497 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.3 | +96.3 (native is 0) | +46.04 to +146.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.94 | 14.24 | +2.2% | -2.712 to +3.312 | no |
| utilisation (used / allocatable) | 0.03388 | 0.03802 | +12.2% | -0.0003055 to +0.008579 | no |
| CPU used (cores), mean | 1.626 | 1.629 | +0.2% | -0.03683 to +0.04261 | no |
| Omni's own CPU (cores), mean | 0 | 0.01211 | +0.0121 (native is 0) | +0.0114 to +0.01282 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.626 | 1.641 | +0.9% | -0.02447 to +0.05447 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.2 | 723.5 | -9.0% | -148.6 to +5.21 | no |
| HPA replicas, mean | 3.913 | 4.66 | +19.1% | +0.4798 to +1.014 | yes: power given |
| pods started | 0 | 1.5 | +1.5 (native is 0) | +0.8048 to +2.195 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.5 (native is 0) | +1.1 to +3.9 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.3 (native is 0) | +0.7111 to +1.889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.35 | 51.02 | +3.4% | +1.13 to +2.219 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 855.2 | 868.4 | +1.5% | +0.233 to +26.17 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.914 | -17.4% | -4.415 to +0.2435 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.05 | -45.5% | -0.08141 to -0.001927 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.3 | -62.5% | -0.877 to -0.123 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 174.2 | +6.0% | +1.602 to +18.08 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.75 | -10.4% | -2.704 to +0.2046 | no |
| node-hours | 5.031 | 4.5 | -10.6% | -1.136 to +0.0743 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 524.8 | -0.3% | -3.08 to +0.4121 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 485.6 | -7.7% | -85.54 to +4.566 | no |
| response time (ms), mean | 757.8 | 542 | -28.5% | -335.5 to -96.23 | yes: GAIN |
| response time (ms), 95th percentile | 3385 | 2339 | -30.9% | -1661 to -429.5 | yes: GAIN |
| response time (ms), 99th percentile | 4740 | 3333 | -29.7% | -2291 to -523.1 | yes: GAIN |
| time over the response line (% of samples) | 23.11 | 21.31 | -7.8% | -4.055 to +0.4654 | no |
| failed requests (%) | 0.08573 | 0 | -100.0% | -0.1698 to -0.001645 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.6 | 11.7 | -14.0% | -2.756 to -1.044 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.3 | +96.3 (native is 0) | +46.04 to +146.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.9 | 14.24 | -35.0% | -16.18 to +0.8613 | no |
| utilisation (used / allocatable) | 0.03475 | 0.03802 | +9.4% | -0.002187 to +0.00873 | no |
| CPU used (cores), mean | 1.668 | 1.629 | -2.3% | -0.1223 to +0.04501 | no |
| Omni's own CPU (cores), mean | 0 | 0.01211 | +0.0121 (native is 0) | +0.0114 to +0.01282 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.668 | 1.641 | -1.6% | -0.1102 to +0.05719 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.8 | 723.5 | -7.9% | -161.8 to +37.3 | no |
| HPA replicas, mean | 4.027 | 4.66 | +15.7% | +0.3267 to +0.9392 | yes: power given |
| pods started | 0.3 | 1.5 | +400.0% | +0.3207 to +2.079 | yes: power given |
| pod start wait, total (s) | 0.7 | 2.5 | +257.1% | -0.3801 to +3.98 | no |
| pod start wait, mean (s) | 0.4 | 1.3 | +225.0% | -0.05076 to +1.851 | no |
| host CPU busy, the real machine under kind (%) | 55.63 | 51.02 | -8.3% | -6.155 to -3.049 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 957.1 | 868.4 | -9.3% | -138.4 to -39.02 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.914 | -17.4% | -4.415 to +0.2435 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 3.138 | 0.05 | -98.4% | -7.259 to +1.084 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.3 | -75.0% | -1.428 to -0.3722 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 259.5 | 174.2 | -32.9% | -133 to -37.64 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | -9.2% | -2.473 to +0.2543 | no |
| node-hours | 5.021 | 4.564 | -9.1% | -1.026 to +0.1122 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 525.9 | +0.3% | -0.5801 to +3.784 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 491 | -6.3% | -76.39 to +9.911 | no |
| response time (ms), mean | 561.7 | 711.9 | +26.7% | +51.84 to +248.4 | yes: LOSS |
| response time (ms), 95th percentile | 2181 | 3429 | +57.2% | +486.5 to +2009 | yes: LOSS |
| response time (ms), 99th percentile | 3053 | 4870 | +59.5% | +740.5 to +2894 | yes: LOSS |
| time over the response line (% of samples) | 20.8 | 24.17 | +16.2% | +0.3768 to +6.359 | yes: LOSS |
| failed requests (%) | 0 | 0.1344 | +0.134 (native is 0) | -0.02714 to +0.2959 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 14.1 | +34.3% | +1.778 to +5.422 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.1 | +48.1 (native is 0) | +30.88 to +65.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.94 | 30.23 | +116.8% | +1.104 to +31.47 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03388 | 0.03824 | +12.9% | +0.0006572 to +0.00806 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.626 | 1.668 | +2.5% | -0.0315 to +0.1143 | no |
| Omni's own CPU (cores), mean | 0 | 0.00956 | +0.00956 (native is 0) | +0.00852 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.626 | 1.677 | +3.1% | -0.02212 to +0.124 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 795.2 | 716.6 | -9.9% | -145.4 to -11.79 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.913 | 4.759 | +21.6% | +0.4608 to +1.231 | yes: power given |
| pods started | 0 | 1.3 | +1.3 (native is 0) | +0.4706 to +2.129 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.7 (native is 0) | +0.4367 to +4.963 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.283 | +1.28 (native is 0) | +0.1635 to +2.403 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.35 | 57.68 | +16.9% | +6.127 to +10.53 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 855.2 | 980.1 | +14.6% | +53.81 to +196 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.14 | -15.5% | -4.06 to +0.3484 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 7.138 | +7686.4% | -2.386 to +16.48 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 33.4 | +4075.0% | -39.63 to +104.8 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 279.7 | +70.1% | +52.2 to +178.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*