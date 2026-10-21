# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.1 | 11.15 |
| node-hours | 5.021 | 5.029 | 4.237 | 4.668 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 522.9 | 526.2 | 527.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 522.9 | 466.5 | 500.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 630.1 | 729.1 | 590.6 | 1000 |
| response time (ms), 95th percentile | 2493 | 2738 | 2538 | 3866 |
| response time (ms), 99th percentile | 3409 | 3776 | 3512 | 5213 |
| time over the response line (% of samples) | 21.13 | 24.85 | 21.63 | 37.09 |
| failed requests (%) | 0.03597 | 0.01653 | 0 | 0.05082 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 12.1 | 11.2 | 17.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 63.9 | 43.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 83.33 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.34 | 46.13 | 21.57 | 41.96 |
| utilisation (used / allocatable) | 0.03472 | 0.03075 | 0.04111 | 0.0397 |
| CPU used (cores), mean | 1.667 | 1.476 | 1.64 | 1.773 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01275 | 0.01188 |
| CPU used with Omni's own (cores), mean | 1.667 | 1.476 | 1.652 | 1.785 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 772.2 | 1066 | 682 | 682.5 |
| HPA replicas, mean | 4.111 | 4.106 | 4.268 | 4.257 |
| pods started | 0.3 | 0 | 1 | 1.5 |
| pod start wait, total (s) | 0.6 | 0 | 1.3 | 5 |
| pod start wait, mean (s) | 0.4 | 0 | 0.8 | 2.467 |
| host CPU busy, the real machine under kind (%) | 51.16 | 52.85 | 52.55 | 61.47 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 881.5 | 1023 | 890.5 | 1050 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.836 | 10.12 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 3.13 | 0.08333 | 13.05 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 6.333 | 0.4 | 85.4 |
| queue: job turnaround, submitted to done, mean (s) | 190.6 | 258.9 | 195 | 337.1 |
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
| worker nodes in service, mean | 12 | 11.15 | -7.1% | -1.648 to -0.06051 | yes: GAIN |
| node-hours | 5.029 | 4.668 | -7.2% | -0.6966 to -0.02482 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.9 | 527.3 | +0.8% | +0.2076 to +8.68 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.9 | 500.5 | -4.3% | -49.16 to +4.294 | no |
| response time (ms), mean | 729.1 | 1000 | +37.2% | +2.452 to +539.4 | yes: LOSS |
| response time (ms), 95th percentile | 2738 | 3866 | +41.2% | +43.74 to +2211 | yes: LOSS |
| response time (ms), 99th percentile | 3776 | 5213 | +38.0% | +4.813 to +2868 | yes: LOSS |
| time over the response line (% of samples) | 24.85 | 37.09 | +49.2% | +0.03421 to +24.44 | yes: LOSS |
| failed requests (%) | 0.01653 | 0.05082 | +207.5% | -0.04309 to +0.1117 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 17.6 | +45.5% | +0.6927 to +10.31 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 | +43.8 (native is 0) | +33.04 to +54.56 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 46.13 | 41.96 | -9.0% | -66.73 to +58.39 | no |
| utilisation (used / allocatable) | 0.03075 | 0.0397 | +29.1% | +0.004222 to +0.01368 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.476 | 1.773 | +20.1% | +0.05942 to +0.534 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01188 | +0.0119 (native is 0) | +0.01116 to +0.0126 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.476 | 1.785 | +20.9% | +0.07109 to +0.5461 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 1066 | 682.5 | -36.0% | -946.6 to +179.3 | no |
| HPA replicas, mean | 4.106 | 4.257 | +3.7% | -0.05868 to +0.3599 | no |
| pods started | 0 | 1.5 | +1.5 (native is 0) | +0.657 to +2.343 | yes: power given |
| pod start wait, total (s) | 0 | 5 | +5 (native is 0) | -0.4892 to +10.49 | no |
| pod start wait, mean (s) | 0 | 2.467 | +2.47 (native is 0) | -0.2772 to +5.211 | no |
| host CPU busy, the real machine under kind (%) | 52.85 | 61.47 | +16.3% | -2.452 to +19.7 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1023 | 1050 | +2.6% | -44.61 to +97.41 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.915 | -17.4% | -3.99 to -0.1795 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 3.13 | 14.34 | +358.1% | -0.6347 to +23.05 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.333 | 94.33 | +1389.5% | -7.562 to +183.6 | no |
| queue: job turnaround, submitted to done, mean (s) | 258.9 | 309.6 | +19.6% | +21 to +80.39 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | -2.532e-15 to +2.177e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.021 | 5.029 | +0.1% | -0.007612 to +0.02228 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 522.9 | -0.4% | -8.439 to +4.072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 522.9 | -0.4% | -8.439 to +4.072 | no |
| response time (ms), mean | 630.1 | 729.1 | +15.7% | -202.5 to +400.4 | no |
| response time (ms), 95th percentile | 2493 | 2738 | +9.8% | -1068 to +1558 | no |
| response time (ms), 99th percentile | 3409 | 3776 | +10.8% | -1383 to +2117 | no |
| time over the response line (% of samples) | 21.13 | 24.85 | +17.6% | -7.299 to +14.74 | no |
| failed requests (%) | 0.03597 | 0.01653 | -54.0% | -0.1127 to +0.0738 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 12.1 | +19.8% | -3.458 to +7.458 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.34 | 46.12 | +138.4% | -15.78 to +69.34 | no |
| utilisation (used / allocatable) | 0.03472 | 0.03075 | -11.4% | -0.01153 to +0.00358 | no |
| CPU used (cores), mean | 1.667 | 1.476 | -11.4% | -0.5533 to +0.1719 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.667 | 1.476 | -11.4% | -0.5533 to +0.1719 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 772.2 | 1066 | +38.1% | -330.1 to +918.2 | no |
| HPA replicas, mean | 4.111 | 4.106 | -0.1% | -0.1397 to +0.1308 | no |
| pods started | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| pod start wait, mean (s) | 0.4 | 0 | -100.0% | -1.003 to +0.2032 | no |
| host CPU busy, the real machine under kind (%) | 51.16 | 52.85 | +3.3% | -9.546 to +12.92 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 881.5 | 1023 | +16.1% | +41.25 to +241.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 3.135 | +4080.2% | -1.757 to +7.877 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 6.389 | +1177.8% | -4.305 to +16.08 | no |
| queue: job turnaround, submitted to done, mean (s) | 190.6 | 278.3 | +46.0% | +35.66 to +139.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.1 | -15.9% | -3.601 to -0.2035 | yes: GAIN |
| node-hours | 5.021 | 4.237 | -15.6% | -1.508 to -0.06129 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 526.2 | +0.2% | -0.7569 to +3.057 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 466.5 | -11.1% | -113.3 to -3.775 | yes: GAIN |
| response time (ms), mean | 630.1 | 590.6 | -6.3% | -69.84 to -9.164 | yes: GAIN |
| response time (ms), 95th percentile | 2493 | 2538 | +1.8% | -200.2 to +288.3 | no |
| response time (ms), 99th percentile | 3409 | 3512 | +3.0% | -159 to +365.5 | no |
| time over the response line (% of samples) | 21.13 | 21.63 | +2.4% | -0.1751 to +1.175 | no |
| failed requests (%) | 0.03597 | 0 | -100.0% | -0.1173 to +0.0454 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 11.2 | +10.9% | -0.08979 to +2.29 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.9 | +63.9 (native is 0) | +38.85 to +88.95 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.34 | 21.57 | +11.5% | -10.97 to +15.43 | no |
| utilisation (used / allocatable) | 0.03472 | 0.04111 | +18.4% | +0.0004701 to +0.01231 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.667 | 1.64 | -1.6% | -0.1078 to +0.05389 | no |
| Omni's own CPU (cores), mean | 0 | 0.01275 | +0.0128 (native is 0) | +0.01191 to +0.01359 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.667 | 1.652 | -0.9% | -0.09524 to +0.06678 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 772.2 | 682 | -11.7% | -175.2 to -5.125 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.111 | 4.268 | +3.8% | -0.1666 to +0.4819 | no |
| pods started | 0.3 | 1 | +233.3% | -0.05776 to +1.458 | no |
| pod start wait, total (s) | 0.6 | 1.3 | +116.7% | -0.4209 to +1.821 | no |
| pod start wait, mean (s) | 0.4 | 0.8 | +100.0% | -0.1792 to +0.9792 | no |
| host CPU busy, the real machine under kind (%) | 51.16 | 52.55 | +2.7% | +0.6675 to +2.123 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 881.5 | 890.5 | +1.0% | -2.734 to +20.73 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 8.836 | -26.4% | -5.926 to -0.4023 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.08333 | +11.1% | -0.03784 to +0.05451 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 190.6 | 195 | +2.3% | -5.517 to +14.3 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.1 | -15.9% | -3.601 to -0.2035 | yes: GAIN |
| node-hours | 5.029 | 4.237 | -15.8% | -1.518 to -0.06646 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.9 | 526.2 | +0.6% | -3.6 to +10.27 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.9 | 466.5 | -10.8% | -113.7 to +0.9894 | no |
| response time (ms), mean | 729.1 | 590.6 | -19.0% | -440.2 to +163.3 | no |
| response time (ms), 95th percentile | 2738 | 2538 | -7.3% | -1496 to +1095 | no |
| response time (ms), 99th percentile | 3776 | 3512 | -7.0% | -2087 to +1559 | no |
| time over the response line (% of samples) | 24.85 | 21.63 | -13.0% | -14.25 to +7.802 | no |
| failed requests (%) | 0.01653 | 0 | -100.0% | -0.05392 to +0.02086 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 11.2 | -7.4% | -6.052 to +4.252 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.9 | +63.9 (native is 0) | +38.85 to +88.95 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 46.13 | 21.58 | -53.2% | -61.93 to +12.83 | no |
| utilisation (used / allocatable) | 0.03075 | 0.04111 | +33.7% | +0.002148 to +0.01858 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.476 | 1.64 | +11.1% | -0.2394 to +0.5669 | no |
| Omni's own CPU (cores), mean | 0 | 0.01275 | +0.0128 (native is 0) | +0.01191 to +0.01359 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.476 | 1.652 | +12.0% | -0.2266 to +0.5796 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 1066 | 682 | -36.0% | -998.9 to +230.5 | no |
| HPA replicas, mean | 4.106 | 4.268 | +3.9% | -0.08843 to +0.4126 | no |
| pods started | 0 | 1 | +1 (native is 0) | +0.3256 to +1.674 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.3 (native is 0) | +0.4047 to +2.195 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.2615 to +1.338 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.85 | 52.55 | -0.6% | -11.53 to +10.95 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1023 | 890.5 | -13.0% | -226.5 to -38.69 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.484 | -29.3% | -6.53 to -0.5011 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 3.13 | 0.06019 | -98.1% | -7.875 to +1.736 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.333 | 0.3333 | -94.7% | -16.45 to +4.448 | no |
| queue: job turnaround, submitted to done, mean (s) | 258.9 | 177.1 | -31.6% | -131.2 to -32.44 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.15 | -7.1% | -1.648 to -0.06051 | yes: GAIN |
| node-hours | 5.021 | 4.668 | -7.0% | -0.6863 to -0.02044 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 527.3 | +0.4% | -0.1346 to +4.655 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 500.5 | -4.7% | -48.94 to -0.2916 | yes: GAIN |
| response time (ms), mean | 630.1 | 1000 | +58.7% | +233.6 to +506.1 | yes: LOSS |
| response time (ms), 95th percentile | 2493 | 3866 | +55.0% | +722.7 to +2022 | yes: LOSS |
| response time (ms), 99th percentile | 3409 | 5213 | +52.9% | +1031 to +2576 | yes: LOSS |
| time over the response line (% of samples) | 21.13 | 37.09 | +75.5% | +11.31 to +20.61 | yes: LOSS |
| failed requests (%) | 0.03597 | 0.05082 | +41.3% | -0.07884 to +0.1085 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 17.6 | +74.3% | +4.057 to +10.94 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 | +43.8 (native is 0) | +33.04 to +54.56 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.34 | 41.95 | +116.9% | -8.58 to +53.8 | no |
| utilisation (used / allocatable) | 0.03472 | 0.0397 | +14.3% | +0.0005215 to +0.009429 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.667 | 1.773 | +6.4% | -0.03508 to +0.247 | no |
| Omni's own CPU (cores), mean | 0 | 0.01188 | +0.0119 (native is 0) | +0.01116 to +0.0126 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.667 | 1.785 | +7.1% | -0.02284 to +0.2586 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 772.2 | 682.5 | -11.6% | -177.3 to -1.983 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.111 | 4.257 | +3.6% | -0.08446 to +0.3768 | no |
| pods started | 0.3 | 1.5 | +400.0% | +0.3207 to +2.079 | yes: power given |
| pod start wait, total (s) | 0.6 | 5 | +733.3% | -0.2382 to +9.038 | no |
| pod start wait, mean (s) | 0.4 | 2.467 | +516.7% | -0.2764 to +4.41 | no |
| host CPU busy, the real machine under kind (%) | 51.16 | 61.47 | +20.2% | +8.843 to +11.78 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 881.5 | 1050 | +19.1% | +115.8 to +220.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.12 | -15.6% | -3.613 to -0.1394 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 13.05 | +17305.6% | +0.2619 to +25.7 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 85.4 | +16980.0% | +0.8505 to +168.9 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 190.6 | 337.1 | +76.8% | +105.8 to +187.1 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*