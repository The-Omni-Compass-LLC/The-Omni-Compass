# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.01 | 10.16 |
| node-hours | 5.012 | 5.02 | 4.197 | 4.259 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 525.6 | 525.9 | 525.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 525.6 | 463.4 | 467.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 694 | 844.3 | 669.8 | 867.4 |
| response time (ms), 95th percentile | 2707 | 3666 | 2815 | 3759 |
| response time (ms), 99th percentile | 3712 | 4876 | 3925 | 5069 |
| time over the response line (% of samples) | 22.87 | 25.85 | 23.44 | 28 |
| failed requests (%) | 0.01501 | 0.06374 | 0.02144 | 0.1831 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 13.7 | 10.9 | 13.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 74.1 | 48.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.6 | 36.86 | 25.97 | 52.16 |
| utilisation (used / allocatable) | 0.03566 | 0.03546 | 0.04111 | 0.04053 |
| CPU used (cores), mean | 1.711 | 1.702 | 1.628 | 1.633 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01268 | 0.0097 |
| CPU used with Omni's own (cores), mean | 1.711 | 1.702 | 1.641 | 1.643 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 763.5 | 761.5 | 686.5 | 691.6 |
| HPA replicas, mean | 3.95 | 4.039 | 4.171 | 4.645 |
| pods started | 0 | 0.4 | 0.8 | 1 |
| pod start wait, total (s) | 0 | 1.1 | 1.9 | 2.2 |
| pod start wait, mean (s) | 0 | 0.85 | 1.25 | 1.225 |
| host CPU busy, the real machine under kind (%) | 51.82 | 58.53 | 53.68 | 59.97 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 909.9 | 1010 | 928.2 | 1040 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.86 | 8.966 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 9.812 | 0.1 | 16.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 64.4 | 0.5 | 122.3 |
| queue: job turnaround, submitted to done, mean (s) | 216.2 | 311.6 | 228.7 | 341.4 |
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
| worker nodes in service, mean | 12 | 10.16 | -15.3% | -3.543 to -0.1358 | yes: GAIN |
| node-hours | 5.02 | 4.259 | -15.2% | -1.487 to -0.03547 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 525.7 | +0.0% | -1.963 to +2.194 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 467.9 | -11.0% | -112.6 to -2.72 | yes: GAIN |
| response time (ms), mean | 844.3 | 867.4 | +2.7% | -70.89 to +117.1 | no |
| response time (ms), 95th percentile | 3666 | 3759 | +2.5% | -227.2 to +413.2 | no |
| response time (ms), 99th percentile | 4876 | 5069 | +4.0% | -206.8 to +593 | no |
| time over the response line (% of samples) | 25.85 | 28 | +8.3% | -1.983 to +6.281 | no |
| failed requests (%) | 0.06374 | 0.1831 | +187.3% | -0.04479 to +0.2835 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 13.6 | -0.7% | -3.707 to +3.507 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.2 | +48.2 (native is 0) | +35.57 to +60.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 36.86 | 52.16 | +41.5% | -5.901 to +36.49 | no |
| utilisation (used / allocatable) | 0.03546 | 0.04053 | +14.3% | -0.0009121 to +0.01105 | no |
| CPU used (cores), mean | 1.702 | 1.633 | -4.1% | -0.1719 to +0.03348 | no |
| Omni's own CPU (cores), mean | 0 | 0.0097 | +0.0097 (native is 0) | +0.008547 to +0.01085 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.702 | 1.643 | -3.5% | -0.1625 to +0.04352 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 691.6 | -9.2% | -161.8 to +22.04 | no |
| HPA replicas, mean | 4.039 | 4.645 | +15.0% | +0.1267 to +1.086 | yes: power given |
| pods started | 0.4 | 1 | +150.0% | -0.4769 to +1.677 | no |
| pod start wait, total (s) | 1.1 | 2.2 | +100.0% | -1.81 to +4.01 | no |
| pod start wait, mean (s) | 0.85 | 1.225 | +44.1% | -1.117 to +1.867 | no |
| host CPU busy, the real machine under kind (%) | 58.53 | 59.97 | +2.5% | -1.21 to +4.098 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1010 | 1040 | +3.0% | -3.226 to +64.43 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 8.966 | -25.3% | -5.84 to -0.228 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 9.812 | 16.2 | +65.1% | -0.04353 to +12.83 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 64.4 | 122.3 | +89.9% | -38.69 to +154.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 311.6 | 341.4 | +9.6% | -5.409 to +64.97 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -4.527e-15 to +6.189e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.012 | 5.02 | +0.2% | -0.005398 to +0.02206 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 525.6 | +0.2% | -1.552 to +3.197 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 525.6 | +0.2% | -1.552 to +3.197 | no |
| response time (ms), mean | 694 | 844.3 | +21.6% | +54.95 to +245.5 | yes: LOSS |
| response time (ms), 95th percentile | 2707 | 3666 | +35.4% | +376.8 to +1540 | yes: LOSS |
| response time (ms), 99th percentile | 3712 | 4876 | +31.3% | +485.3 to +1842 | yes: LOSS |
| time over the response line (% of samples) | 22.87 | 25.85 | +13.0% | +0.9799 to +4.987 | yes: LOSS |
| failed requests (%) | 0.01501 | 0.06374 | +324.7% | -0.0422 to +0.1397 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 13.7 | +31.7% | +0.844 to +5.756 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.6 | 36.86 | +122.0% | -0.9206 to +41.44 | no |
| utilisation (used / allocatable) | 0.03566 | 0.03546 | -0.5% | -0.002533 to +0.00215 | no |
| CPU used (cores), mean | 1.711 | 1.702 | -0.5% | -0.1216 to +0.1032 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.711 | 1.702 | -0.5% | -0.1216 to +0.1032 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 763.5 | 761.5 | -0.3% | -45.92 to +41.96 | no |
| HPA replicas, mean | 3.95 | 4.039 | +2.2% | -0.1734 to +0.3507 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | -0.2254 to +2.425 | no |
| pod start wait, mean (s) | 0 | 0.85 | +0.85 (native is 0) | -0.1338 to +1.834 | no |
| host CPU busy, the real machine under kind (%) | 51.82 | 58.53 | +12.9% | +4.878 to +8.531 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 909.9 | 1010 | +11.0% | +45.74 to +153.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 9.812 | +11114.3% | -0.327 to +19.78 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 64.4 | +12780.0% | -30.3 to +158.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 216.2 | 311.6 | +44.2% | +44.66 to +146.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.01 | -16.6% | -3.819 to -0.1625 | yes: GAIN |
| node-hours | 5.012 | 4.197 | -16.3% | -1.585 to -0.0448 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 525.9 | +0.2% | -0.361 to +2.583 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 463.4 | -11.7% | -119.2 to -3.569 | yes: GAIN |
| response time (ms), mean | 694 | 669.8 | -3.5% | -53.19 to +4.745 | no |
| response time (ms), 95th percentile | 2707 | 2815 | +4.0% | -54.98 to +271.7 | no |
| response time (ms), 99th percentile | 3712 | 3925 | +5.7% | -196.3 to +622.4 | no |
| time over the response line (% of samples) | 22.87 | 23.44 | +2.5% | -0.3764 to +1.528 | no |
| failed requests (%) | 0.01501 | 0.02144 | +42.8% | -0.02302 to +0.03588 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.9 | +4.8% | +0.123 to +0.877 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.1 | +74.1 (native is 0) | +40.94 to +107.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.6 | 25.97 | +56.4% | -2.574 to +21.3 | no |
| utilisation (used / allocatable) | 0.03566 | 0.04111 | +15.3% | -0.001271 to +0.01217 | no |
| CPU used (cores), mean | 1.711 | 1.628 | -4.8% | -0.173 to +0.007112 | no |
| Omni's own CPU (cores), mean | 0 | 0.01268 | +0.0127 (native is 0) | +0.01201 to +0.01335 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.711 | 1.641 | -4.1% | -0.1605 to +0.01989 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 763.5 | 686.5 | -10.1% | -175.9 to +21.83 | no |
| HPA replicas, mean | 3.95 | 4.171 | +5.6% | -0.02801 to +0.4696 | no |
| pods started | 0 | 0.8 | +0.8 (native is 0) | +0.2358 to +1.364 | yes: power given |
| pod start wait, total (s) | 0 | 1.9 | +1.9 (native is 0) | -0.1077 to +3.908 | no |
| pod start wait, mean (s) | 0 | 1.25 | +1.25 (native is 0) | +0.221 to +2.279 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.82 | 53.68 | +3.6% | +1.094 to +2.61 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 909.9 | 928.2 | +2.0% | +6.397 to +30.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.86 | -26.2% | -5.978 to -0.3023 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.1 | +14.3% | -0.03826 to +0.06326 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 216.2 | 228.7 | +5.8% | +2.749 to +22.41 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.01 | -16.6% | -3.819 to -0.1625 | yes: GAIN |
| node-hours | 5.02 | 4.197 | -16.4% | -1.601 to -0.04501 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 525.9 | +0.1% | -2.561 to +3.138 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 463.4 | -11.8% | -121.4 to -3.034 | yes: GAIN |
| response time (ms), mean | 844.3 | 669.8 | -20.7% | -283.6 to -65.32 | yes: GAIN |
| response time (ms), 95th percentile | 3666 | 2815 | -23.2% | -1445 to -255.9 | yes: GAIN |
| response time (ms), 99th percentile | 4876 | 3925 | -19.5% | -1645 to -256.4 | yes: GAIN |
| time over the response line (% of samples) | 25.85 | 23.44 | -9.3% | -4.215 to -0.6005 | yes: GAIN |
| failed requests (%) | 0.06374 | 0.02144 | -66.4% | -0.133 to +0.04842 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 10.9 | -20.4% | -5.273 to -0.3267 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.1 | +74.1 (native is 0) | +40.94 to +107.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 36.86 | 25.97 | -29.6% | -27.93 to +6.148 | no |
| utilisation (used / allocatable) | 0.03546 | 0.04111 | +15.9% | -0.0007826 to +0.01207 | no |
| CPU used (cores), mean | 1.702 | 1.628 | -4.3% | -0.2174 to +0.06987 | no |
| Omni's own CPU (cores), mean | 0 | 0.01268 | +0.0127 (native is 0) | +0.01201 to +0.01335 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.702 | 1.641 | -3.6% | -0.2048 to +0.08261 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 761.5 | 686.5 | -9.9% | -166 to +15.87 | no |
| HPA replicas, mean | 4.039 | 4.171 | +3.3% | -0.2286 to +0.4929 | no |
| pods started | 0.4 | 0.8 | +100.0% | -0.2032 to +1.003 | no |
| pod start wait, total (s) | 1.1 | 1.9 | +72.7% | -1.16 to +2.76 | no |
| pod start wait, mean (s) | 0.85 | 1.25 | +47.1% | -0.4564 to +1.256 | no |
| host CPU busy, the real machine under kind (%) | 58.53 | 53.68 | -8.3% | -6.44 to -3.265 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1010 | 928.2 | -8.1% | -124.8 to -38.05 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.86 | -26.2% | -5.978 to -0.3023 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 9.812 | 0.1 | -99.0% | -19.77 to +0.3487 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 64.4 | 0.5 | -99.2% | -158.1 to +30.3 | no |
| queue: job turnaround, submitted to done, mean (s) | 311.6 | 228.7 | -26.6% | -127.8 to -37.92 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.16 | -15.3% | -3.543 to -0.1358 | yes: GAIN |
| node-hours | 5.012 | 4.259 | -15.0% | -1.47 to -0.03566 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.8 | 525.7 | +0.2% | -0.5868 to +2.463 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.8 | 467.9 | -10.8% | -110.4 to -3.25 | yes: GAIN |
| response time (ms), mean | 694 | 867.4 | +25.0% | +52.58 to +294.2 | yes: LOSS |
| response time (ms), 95th percentile | 2707 | 3759 | +38.8% | +373.3 to +1730 | yes: LOSS |
| response time (ms), 99th percentile | 3712 | 5069 | +36.5% | +509.4 to +2204 | yes: LOSS |
| time over the response line (% of samples) | 22.87 | 28 | +22.4% | +1.622 to +8.643 | yes: LOSS |
| failed requests (%) | 0.01501 | 0.1831 | +1119.8% | -0.03108 to +0.3673 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 13.6 | +30.8% | +1.903 to +4.497 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.2 | +48.2 (native is 0) | +35.57 to +60.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.6 | 52.16 | +214.1% | +6.018 to +65.09 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03566 | 0.04053 | +13.7% | -0.001781 to +0.01153 | no |
| CPU used (cores), mean | 1.711 | 1.633 | -4.6% | -0.1884 to +0.03163 | no |
| Omni's own CPU (cores), mean | 0 | 0.0097 | +0.0097 (native is 0) | +0.008547 to +0.01085 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.711 | 1.643 | -4.0% | -0.1786 to +0.04123 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 763.5 | 691.6 | -9.4% | -175.6 to +31.83 | no |
| HPA replicas, mean | 3.95 | 4.645 | +17.6% | +0.3297 to +1.06 | yes: power given |
| pods started | 0 | 1 | +1 (native is 0) | +0.1079 to +1.892 | yes: power given |
| pod start wait, total (s) | 0 | 2.2 | +2.2 (native is 0) | -0.08202 to +4.482 | no |
| pod start wait, mean (s) | 0 | 1.225 | +1.23 (native is 0) | +0.2048 to +2.245 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.82 | 59.97 | +15.7% | +5.743 to +10.55 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 909.9 | 1040 | +14.3% | +52.29 to +208.3 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.966 | -25.3% | -5.84 to -0.228 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 16.2 | +18419.0% | +2.892 to +29.34 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 122.3 | +24360.0% | +9.466 to +234.1 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 216.2 | 341.4 | +57.9% | +52.07 to +198.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*