# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.125 | 5.255 |
| node-hours | 2.515 | 2.514 | 2.15 | 2.201 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.9 | 272.3 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.9 | 244.8 | 248.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 302.1 | 222.2 | 266.7 | 178.2 |
| response time (ms), 95th percentile | 926.1 | 517.4 | 996.5 | 518.9 |
| response time (ms), 99th percentile | 1337 | 846.3 | 1467 | 825.4 |
| time over the response line (% of samples) | 16.62 | 7.226 | 16.19 | 6.84 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 7.6 | 9.9 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 40.2 | 35.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.998 | 13.61 | 10.46 | 14.53 |
| utilisation (used / allocatable) | 0.05883 | 0.05893 | 0.06903 | 0.06798 |
| CPU used (cores), mean | 1.412 | 1.414 | 1.409 | 1.405 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01732 | 0.01708 |
| CPU used with Omni's own (cores), mean | 1.412 | 1.414 | 1.426 | 1.422 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.4 | 464.5 | 417.8 | 422.8 |
| HPA replicas, mean | 2.014 | 2.053 | 2.008 | 2.004 |
| pods started | 0.2 | 0.1 | 0 | 0.2 |
| pod start wait, total (s) | 0.4 | 0.2 | 0 | 0.4 |
| pod start wait, mean (s) | 0.2 | 0.2 | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 40.33 | 41.33 | 41.29 | 42.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 758.7 | 767.6 | 762.1 | 772.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.258 | 4.683 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.7208 | 0.05417 | 0.7667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.4 | 0.3 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 65.63 | 81.51 | 70.4 | 86.72 |
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
| worker nodes in service, mean | 6 | 5.255 | -12.4% | -1.481 to -0.009579 | yes: GAIN |
| node-hours | 2.514 | 2.201 | -12.5% | -0.6248 to -0.001981 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 | -0.1% | -1.274 to +0.8162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 248.3 | -8.7% | -47.26 to +0.09363 | no |
| response time (ms), mean | 222.2 | 178.2 | -19.8% | -66.47 to -21.51 | yes: GAIN |
| response time (ms), 95th percentile | 517.4 | 518.9 | +0.3% | -112.5 to +115.5 | no |
| response time (ms), 99th percentile | 846.3 | 825.4 | -2.5% | -252.3 to +210.6 | no |
| time over the response line (% of samples) | 7.226 | 6.84 | -5.3% | -3.321 to +2.548 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.1 | -6.6% | -1.68 to +0.6802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.2 | +35.2 (native is 0) | +21.52 to +48.88 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.61 | 14.53 | +6.8% | -1.093 to +2.933 | no |
| utilisation (used / allocatable) | 0.05893 | 0.06798 | +15.4% | +0.0006079 to +0.01749 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.405 | -0.6% | -0.03857 to +0.02082 | no |
| Omni's own CPU (cores), mean | 0 | 0.01708 | +0.0171 (native is 0) | +0.01579 to +0.01837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.422 | +0.6% | -0.02122 to +0.03763 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.5 | 422.8 | -9.0% | -78.72 to -4.649 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.053 | 2.004 | -2.4% | -0.2154 to +0.116 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | -0.6121 to +1.012 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | -0.6121 to +1.012 | no |
| host CPU busy, the real machine under kind (%) | 41.33 | 42.27 | +2.3% | +0.7151 to +1.182 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 767.6 | 772.3 | +0.6% | +0.8398 to +8.56 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.683 | -22.0% | -2.58 to -0.05435 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7208 | 0.7667 | +6.4% | -0.0687 to +0.1604 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.3 | -7.1% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.51 | 86.72 | +6.4% | +0.5672 to +9.841 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.146e-15 to +9.679e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.514 | -0.0% | -0.009905 to +0.008571 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.9 | -0.0% | -1.031 to +0.8784 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.9 | -0.0% | -1.031 to +0.8784 | no |
| response time (ms), mean | 302.1 | 222.2 | -26.5% | -122.6 to -37.23 | yes: GAIN |
| response time (ms), 95th percentile | 926.1 | 517.4 | -44.1% | -628.5 to -188.7 | yes: GAIN |
| response time (ms), 99th percentile | 1337 | 846.3 | -36.7% | -783.4 to -198.6 | yes: GAIN |
| time over the response line (% of samples) | 16.62 | 7.226 | -56.5% | -15.08 to -3.706 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 7.6 | -12.6% | -1.811 to -0.3887 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.998 | 13.61 | +36.1% | +0.9071 to +6.316 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05883 | 0.05893 | +0.2% | -0.0004813 to +0.0006771 | no |
| CPU used (cores), mean | 1.412 | 1.414 | +0.2% | -0.01155 to +0.01625 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.412 | 1.414 | +0.2% | -0.01155 to +0.01625 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.4 | 464.5 | -0.2% | -5.443 to +3.737 | no |
| HPA replicas, mean | 2.014 | 2.053 | +1.9% | -0.1372 to +0.2153 | no |
| pods started | 0.2 | 0.1 | -50.0% | -0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.4 | 0.2 | -50.0% | -1.256 to +0.8556 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 40.33 | 41.33 | +2.5% | +0.751 to +1.24 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.7 | 767.6 | +1.2% | +4.222 to +13.58 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.7208 | +1053.3% | +0.5524 to +0.7642 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.4 | +366.7% | +0.694 to +1.506 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.63 | 81.51 | +24.2% | +7.126 to +24.63 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.125 | -14.6% | -1.294 to -0.4557 | yes: GAIN |
| node-hours | 2.515 | 2.15 | -14.5% | -0.5398 to -0.1909 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.3 | +0.1% | -0.4197 to +1.074 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 244.8 | -10.0% | -40.3 to -14.1 | yes: GAIN |
| response time (ms), mean | 302.1 | 266.7 | -11.7% | -45.46 to -25.46 | yes: GAIN |
| response time (ms), 95th percentile | 926.1 | 996.5 | +7.6% | +7.093 to +133.8 | yes: LOSS |
| response time (ms), 99th percentile | 1337 | 1467 | +9.7% | +24.89 to +233.9 | yes: LOSS |
| time over the response line (% of samples) | 16.62 | 16.19 | -2.6% | -1.338 to +0.4783 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.9 | +13.8% | -0.09723 to +2.497 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.2 | +40.2 (native is 0) | +31.7 to +48.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.998 | 10.46 | +4.6% | -1.203 to +2.123 | no |
| utilisation (used / allocatable) | 0.05883 | 0.06903 | +17.3% | +0.005534 to +0.01486 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.412 | 1.409 | -0.2% | -0.01755 to +0.01181 | no |
| Omni's own CPU (cores), mean | 0 | 0.01732 | +0.0173 (native is 0) | +0.01601 to +0.01863 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.412 | 1.426 | +1.0% | -0.0004629 to +0.02936 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.4 | 417.8 | -10.2% | -71.5 to -23.56 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.008 | -0.3% | -0.2004 to +0.1879 | no |
| pods started | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.4 | 0 | -100.0% | -1.305 to +0.5048 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 40.33 | 41.29 | +2.4% | +0.749 to +1.17 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.7 | 762.1 | +0.4% | -1.051 to +7.851 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.258 | -29.0% | -2.541 to -0.9417 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05417 | -13.3% | -0.05001 to +0.03335 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.63 | 70.4 | +7.3% | +0.7109 to +8.822 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.125 | -14.6% | -1.294 to -0.4557 | yes: GAIN |
| node-hours | 2.514 | 2.15 | -14.5% | -0.5414 to -0.1879 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.3 | +0.1% | -0.5403 to +1.348 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 244.8 | -10.0% | -40.36 to -13.88 | yes: GAIN |
| response time (ms), mean | 222.2 | 266.7 | +20.0% | +1.564 to +87.39 | yes: LOSS |
| response time (ms), 95th percentile | 517.4 | 996.5 | +92.6% | +241.4 to +716.7 | yes: LOSS |
| response time (ms), 99th percentile | 846.3 | 1467 | +73.3% | +266.9 to +974 | yes: LOSS |
| time over the response line (% of samples) | 7.226 | 16.19 | +124.1% | +3.715 to +14.21 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 9.9 | +30.3% | +0.5141 to +4.086 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.2 | +40.2 (native is 0) | +31.7 to +48.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.61 | 10.46 | -23.2% | -5.638 to -0.6649 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05893 | 0.06903 | +17.1% | +0.005066 to +0.01513 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.409 | -0.4% | -0.02068 to +0.01024 | no |
| Omni's own CPU (cores), mean | 0 | 0.01732 | +0.0173 (native is 0) | +0.01601 to +0.01863 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.426 | +0.9% | -0.003945 to +0.02815 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.5 | 417.8 | -10.0% | -73.17 to -20.18 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.053 | 2.008 | -2.2% | -0.25 to +0.1594 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 41.33 | 41.29 | -0.1% | -0.3042 to +0.2317 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 767.6 | 762.1 | -0.7% | -9.041 to -1.959 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.258 | -29.0% | -2.541 to -0.9417 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7208 | 0.05417 | -92.5% | -0.7609 to -0.5724 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.3 | -78.6% | -1.506 to -0.694 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 81.51 | 70.4 | -13.6% | -17.29 to -4.937 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.255 | -12.4% | -1.481 to -0.009579 | yes: GAIN |
| node-hours | 2.515 | 2.201 | -12.5% | -0.6257 to -0.002443 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | -0.1% | -1.281 to +0.67 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 248.3 | -8.7% | -47.35 to +0.0305 | no |
| response time (ms), mean | 302.1 | 178.2 | -41.0% | -165 to -82.88 | yes: GAIN |
| response time (ms), 95th percentile | 926.1 | 518.9 | -44.0% | -607.8 to -206.4 | yes: GAIN |
| response time (ms), 99th percentile | 1337 | 825.4 | -38.3% | -746.1 to -277.7 | yes: GAIN |
| time over the response line (% of samples) | 16.62 | 6.84 | -58.8% | -15.52 to -4.041 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 7.1 | -18.4% | -2.623 to -0.5772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.2 | +35.2 (native is 0) | +21.52 to +48.88 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.998 | 14.53 | +45.3% | +2.217 to +6.847 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05883 | 0.06798 | +15.5% | +0.0005813 to +0.01771 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.412 | 1.405 | -0.5% | -0.03433 to +0.02128 | no |
| Omni's own CPU (cores), mean | 0 | 0.01708 | +0.0171 (native is 0) | +0.01579 to +0.01837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.412 | 1.422 | +0.7% | -0.01694 to +0.03805 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.4 | 422.8 | -9.1% | -80.98 to -4.099 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.004 | -0.5% | -0.1703 to +0.1489 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.4 | 0.4 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.33 | 42.27 | +4.8% | +1.771 to +2.118 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.7 | 772.3 | +1.8% | +6.028 to +21.17 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.683 | -22.0% | -2.58 to -0.05435 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.7667 | +1126.7% | +0.6376 to +0.7707 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.3 | +333.3% | +0.5231 to +1.477 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.63 | 86.72 | +32.1% | +8.803 to +33.36 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*