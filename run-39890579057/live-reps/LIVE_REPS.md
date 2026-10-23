# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.926 | 4.821 |
| node-hours | 2.513 | 2.512 | 2.063 | 2.019 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.7 | 269.9 | 269.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 269.7 | 236.1 | 232.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 209.3 | 203.7 | 198.3 | 182.7 |
| response time (ms), 95th percentile | 605.6 | 658.8 | 728.8 | 744.3 |
| response time (ms), 99th percentile | 831.9 | 1004 | 1048 | 1147 |
| time over the response line (% of samples) | 9.149 | 6.786 | 9.708 | 7.014 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5 | 5.9 | 5.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 161.5 | 123.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 80 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.082 | 8.863 | 8.145 | 10.04 |
| utilisation (used / allocatable) | 0.05291 | 0.05299 | 0.0648 | 0.06685 |
| CPU used (cores), mean | 1.27 | 1.272 | 1.275 | 1.266 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04758 | 0.04531 |
| CPU used with Omni's own (cores), mean | 1.27 | 1.272 | 1.323 | 1.311 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518.1 | 517.2 | 445.6 | 442.1 |
| HPA replicas, mean | 1.967 | 1.978 | 2.477 | 2.521 |
| pods started | 0.1 | 0 | 0.9 | 1.3 |
| pod start wait, total (s) | 0.2 | 0 | 2.2 | 2.1 |
| pod start wait, mean (s) | 0.2 | 0 | 0.925 | 0.75 |
| host CPU busy, the real machine under kind (%) | 36.23 | 36.49 | 38.5 | 38.37 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 739.2 | 740.7 | 745.3 | 745.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.95 | 3.957 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.02917 | 0.025 | 0.05 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | 0.1 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 44.98 | 49.56 | 51.93 | 52.51 |
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
| worker nodes in service, mean | 6 | 4.821 | -19.6% | -1.945 to -0.4132 | yes: GAIN |
| node-hours | 2.512 | 2.019 | -19.6% | -0.8175 to -0.1666 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.7 | +0.0% | -1.062 to +1.164 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 232.7 | -13.7% | -61.69 to -12.21 | yes: GAIN |
| response time (ms), mean | 203.7 | 182.7 | -10.3% | -38.39 to -3.76 | yes: GAIN |
| response time (ms), 95th percentile | 658.8 | 744.3 | +13.0% | -53.09 to +224 | no |
| response time (ms), 99th percentile | 1004 | 1147 | +14.3% | -88.54 to +374.9 | no |
| time over the response line (% of samples) | 6.786 | 7.014 | +3.4% | -0.9831 to +1.44 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 5.1 | +2.0% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123.7 | +124 (native is 0) | +92.36 to +155 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.863 | 10.04 | +13.2% | -1.252 to +3.599 | no |
| utilisation (used / allocatable) | 0.05299 | 0.06685 | +26.1% | +0.004193 to +0.02352 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.272 | 1.266 | -0.4% | -0.04059 to +0.0292 | no |
| Omni's own CPU (cores), mean | 0 | 0.04531 | +0.0453 (native is 0) | +0.03925 to +0.05137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.272 | 1.311 | +3.1% | +0.002751 to +0.07647 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 517.2 | 442.1 | -14.5% | -119.9 to -30.24 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.521 | +27.5% | +0.2716 to +0.8151 | yes: power given |
| pods started | 0 | 1.3 | +1.3 (native is 0) | +0.1295 to +2.471 | yes: power given |
| pod start wait, total (s) | 0 | 2.1 | +2.1 (native is 0) | +0.009094 to +4.191 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.75 | +0.75 (native is 0) | +0.1363 to +1.364 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.49 | 38.37 | +5.1% | +1.288 to +2.464 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 740.7 | 745.3 | +0.6% | -0.6152 to +9.815 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.957 | -34.1% | -3.308 to -0.7784 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.05 | +71.4% | -0.01429 to +0.05596 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 | +300.0% | -0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 49.56 | 52.51 | +5.9% | -0.5331 to +6.425 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.235e-16 to +6.788e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.512 | -0.1% | -0.01147 to +0.008466 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.7 | +0.0% | -1.028 to +1.036 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 269.7 | +0.0% | -1.028 to +1.036 | no |
| response time (ms), mean | 209.3 | 203.7 | -2.7% | -38.74 to +27.59 | no |
| response time (ms), 95th percentile | 605.6 | 658.8 | +8.8% | -116.4 to +222.7 | no |
| response time (ms), 99th percentile | 831.9 | 1004 | +20.6% | -156.8 to +500.3 | no |
| time over the response line (% of samples) | 9.149 | 6.786 | -25.8% | -6.221 to +1.494 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5 | -7.4% | -1.003 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.082 | 8.863 | +25.2% | -0.7587 to +4.322 | no |
| utilisation (used / allocatable) | 0.05291 | 0.05299 | +0.2% | -0.001007 to +0.001174 | no |
| CPU used (cores), mean | 1.27 | 1.272 | +0.2% | -0.02417 to +0.02818 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.27 | 1.272 | +0.2% | -0.02417 to +0.02818 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518.1 | 517.2 | -0.2% | -13.23 to +11.33 | no |
| HPA replicas, mean | 1.967 | 1.978 | +0.5% | -0.1459 to +0.1674 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 36.23 | 36.49 | +0.7% | -0.2733 to +0.8005 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.2 | 740.7 | +0.2% | -2.479 to +5.479 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.02917 | +0.0% | -0.01987 to +0.01987 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 44.98 | 49.56 | +10.2% | -0.04642 to +9.205 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.926 | -17.9% | -1.697 to -0.4503 | yes: GAIN |
| node-hours | 2.513 | 2.063 | -17.9% | -0.7096 to -0.1905 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.9 | +0.1% | -0.8752 to +1.28 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 236.1 | -12.4% | -53.02 to -14.01 | yes: GAIN |
| response time (ms), mean | 209.3 | 198.3 | -5.2% | -27.52 to +5.58 | no |
| response time (ms), 95th percentile | 605.6 | 728.8 | +20.3% | +7.115 to +239.3 | yes: LOSS |
| response time (ms), 99th percentile | 831.9 | 1048 | +26.0% | -1.17 to +433.2 | no |
| time over the response line (% of samples) | 9.149 | 9.708 | +6.1% | -0.4288 to +1.546 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5.9 | +9.3% | -0.4685 to +1.469 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161.5 | +162 (native is 0) | +112 to +211 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.082 | 8.145 | +15.0% | -0.3319 to +2.459 | no |
| utilisation (used / allocatable) | 0.05291 | 0.0648 | +22.5% | +0.00556 to +0.01822 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.27 | 1.275 | +0.4% | -0.02417 to +0.03446 | no |
| Omni's own CPU (cores), mean | 0 | 0.04758 | +0.0476 (native is 0) | +0.04067 to +0.05449 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.27 | 1.323 | +4.2% | +0.0196 to +0.08585 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518.1 | 445.6 | -14.0% | -112.8 to -32.35 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.967 | 2.477 | +25.9% | +0.1321 to +0.8866 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | -0.1417 to +1.742 | no |
| pod start wait, total (s) | 0.2 | 2.2 | +1000.0% | -0.5458 to +4.546 | no |
| pod start wait, mean (s) | 0.2 | 0.925 | +362.5% | -0.1199 to +1.57 | no |
| host CPU busy, the real machine under kind (%) | 36.23 | 38.5 | +6.3% | +1.704 to +2.844 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.2 | 745.3 | +0.8% | +0.1491 to +12.05 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.95 | -34.2% | -3.237 to -0.8624 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.025 | -14.3% | -0.03985 to +0.03152 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 44.98 | 51.93 | +15.5% | +0.07769 to +13.82 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.926 | -17.9% | -1.697 to -0.4503 | yes: GAIN |
| node-hours | 2.512 | 2.063 | -17.9% | -0.7143 to -0.1828 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.9 | +0.1% | -0.9231 to +1.32 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 236.1 | -12.4% | -53.73 to -13.31 | yes: GAIN |
| response time (ms), mean | 203.7 | 198.3 | -2.6% | -33.24 to +22.44 | no |
| response time (ms), 95th percentile | 658.8 | 728.8 | +10.6% | -75.1 to +215.2 | no |
| response time (ms), 99th percentile | 1004 | 1048 | +4.4% | -124.8 to +213.4 | no |
| time over the response line (% of samples) | 6.786 | 9.708 | +43.1% | -0.5543 to +6.399 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 5.9 | +18.0% | -0.4254 to +2.225 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161.5 | +162 (native is 0) | +112 to +211 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.863 | 8.145 | -8.1% | -2.743 to +1.306 | no |
| utilisation (used / allocatable) | 0.05299 | 0.0648 | +22.3% | +0.005672 to +0.01794 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.272 | 1.275 | +0.2% | -0.02302 to +0.0293 | no |
| Omni's own CPU (cores), mean | 0 | 0.04758 | +0.0476 (native is 0) | +0.04067 to +0.05449 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.272 | 1.323 | +4.0% | +0.02343 to +0.07802 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 517.2 | 445.6 | -13.8% | -109.8 to -33.44 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.477 | +25.2% | +0.2146 to +0.7825 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | -0.0802 to +1.88 | no |
| pod start wait, total (s) | 0 | 2.2 | +2.2 (native is 0) | -0.3857 to +4.786 | no |
| pod start wait, mean (s) | 0 | 0.925 | +0.925 (native is 0) | +0.05688 to +1.793 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.49 | 38.5 | +5.5% | +1.588 to +2.433 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 740.7 | 745.3 | +0.6% | -1.764 to +10.96 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.95 | -34.2% | -3.237 to -0.8624 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.025 | -14.3% | -0.03381 to +0.02547 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 49.56 | 51.93 | +4.8% | -2.268 to +7.01 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.821 | -19.6% | -1.945 to -0.4132 | yes: GAIN |
| node-hours | 2.513 | 2.019 | -19.6% | -0.8138 to -0.1733 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.7 | +0.0% | -1.055 to +1.165 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 232.7 | -13.7% | -61.11 to -12.79 | yes: GAIN |
| response time (ms), mean | 209.3 | 182.7 | -12.7% | -43.93 to -9.357 | yes: GAIN |
| response time (ms), 95th percentile | 605.6 | 744.3 | +22.9% | -15.42 to +292.7 | no |
| response time (ms), 99th percentile | 831.9 | 1147 | +37.9% | -53.96 to +683.8 | no |
| time over the response line (% of samples) | 9.149 | 7.014 | -23.3% | -5.247 to +0.9758 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5.1 | -5.6% | -0.6455 to +0.04553 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123.7 | +124 (native is 0) | +92.36 to +155 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.082 | 10.04 | +41.7% | +1.204 to +4.706 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05291 | 0.06685 | +26.3% | +0.00415 to +0.02373 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.27 | 1.266 | -0.3% | -0.04222 to +0.03483 | no |
| Omni's own CPU (cores), mean | 0 | 0.04531 | +0.0453 (native is 0) | +0.03925 to +0.05137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.27 | 1.311 | +3.3% | +0.000713 to +0.08252 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518.1 | 442.1 | -14.7% | -122.5 to -29.56 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.967 | 2.521 | +28.2% | +0.234 to +0.8742 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.1444 to +2.256 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.1 | +950.0% | +0.1014 to +3.699 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | +0.004977 to +1.095 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.23 | 38.37 | +5.9% | +1.252 to +3.027 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.2 | 745.3 | +0.8% | +1.583 to +10.62 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.957 | -34.1% | -3.308 to -0.7784 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.05 | +71.4% | -0.01136 to +0.05303 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 | +300.0% | -0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 44.98 | 52.51 | +16.7% | +1.334 to +13.72 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*