# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.498 | 5.485 |
| node-hours | 2.516 | 2.516 | 2.304 | 2.3 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.5 | 273.7 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 274.5 | 258 | 258.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 494.9 | 505 | 501.3 | 500.8 |
| response time (ms), 95th percentile | 1956 | 2118 | 1968 | 2082 |
| response time (ms), 99th percentile | 2903 | 3170 | 2924 | 3154 |
| time over the response line (% of samples) | 24.35 | 23.25 | 25 | 23.11 |
| failed requests (%) | 0 | 0 | 0.0122 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.7 | 11.7 | 11.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 8.3 | 8.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.91 | 20.34 | 17.92 | 19.45 |
| utilisation (used / allocatable) | 0.0661 | 0.06613 | 0.0726 | 0.07118 |
| CPU used (cores), mean | 1.586 | 1.587 | 1.579 | 1.562 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01172 | 0.01261 |
| CPU used with Omni's own (cores), mean | 1.586 | 1.587 | 1.591 | 1.574 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.9 | 421.8 | 391.8 | 399 |
| HPA replicas, mean | 2.003 | 2.121 | 2.307 | 2.309 |
| pods started | 0.1 | 0 | 0.6 | 0.5 |
| pod start wait, total (s) | 0.3 | 0 | 1 | 0.8 |
| pod start wait, mean (s) | 0.3 | 0 | 1 | 0.8 |
| host CPU busy, the real machine under kind (%) | 45.25 | 45.97 | 46.14 | 46.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 830.6 | 837.8 | 832.9 | 840.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.199 | 5.081 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3917 | 0.25 | 0.5625 | 0.3125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1 | 1.9 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 138.8 | 148.6 | 140.9 | 153 |
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
| worker nodes in service, mean | 6 | 5.485 | -8.6% | -1.2 to +0.1692 | no |
| node-hours | 2.516 | 2.3 | -8.6% | -0.5023 to +0.06978 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.4 | -0.0% | -0.9315 to +0.7427 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 258.2 | -6.0% | -38.04 to +5.357 | no |
| response time (ms), mean | 505 | 500.8 | -0.8% | -23.31 to +14.89 | no |
| response time (ms), 95th percentile | 2118 | 2082 | -1.7% | -151.4 to +79.32 | no |
| response time (ms), 99th percentile | 3170 | 3154 | -0.5% | -252.2 to +220.8 | no |
| time over the response line (% of samples) | 23.25 | 23.11 | -0.6% | -1.015 to +0.7393 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11.8 | +0.9% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.6 | +8.6 (native is 0) | +6.006 to +11.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.34 | 19.45 | -4.3% | -4.388 to +2.625 | no |
| utilisation (used / allocatable) | 0.06613 | 0.07118 | +7.6% | -0.001551 to +0.01164 | no |
| CPU used (cores), mean | 1.587 | 1.562 | -1.6% | -0.07036 to +0.01922 | no |
| Omni's own CPU (cores), mean | 0 | 0.01261 | +0.0126 (native is 0) | +0.01194 to +0.01328 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.587 | 1.574 | -0.8% | -0.05829 to +0.03236 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.8 | 399 | -5.4% | -55.17 to +9.632 | no |
| HPA replicas, mean | 2.121 | 2.309 | +8.9% | -0.0005643 to +0.3762 | no |
| pods started | 0 | 0.5 | +0.5 (native is 0) | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | +0.1427 to +1.457 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.1427 to +1.457 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.97 | 46.58 | +1.3% | +0.4513 to +0.7613 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 837.8 | 840.6 | +0.3% | +0.6461 to +4.954 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.081 | -15.3% | -2.091 to +0.2532 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.3125 | +25.0% | -0.09348 to +0.2185 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.8 | -20.0% | -0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 148.6 | 153 | +3.0% | +0.7737 to +8.001 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.331e-15 to +3.774e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.516 | +0.0% | -0.008351 to +0.009018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.5 | +0.0% | -1.063 to +1.104 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 274.5 | +0.0% | -1.063 to +1.104 | no |
| response time (ms), mean | 494.9 | 505 | +2.0% | -12.33 to +32.59 | no |
| response time (ms), 95th percentile | 1956 | 2118 | +8.3% | -3.542 to +326.5 | no |
| response time (ms), 99th percentile | 2903 | 3170 | +9.2% | -1.847 to +536.4 | no |
| time over the response line (% of samples) | 24.35 | 23.25 | -4.5% | -2.105 to -0.09409 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.7 | +0.9% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.91 | 20.33 | +13.5% | -0.08132 to +4.921 | no |
| utilisation (used / allocatable) | 0.0661 | 0.06613 | +0.0% | -0.0007159 to +0.0007794 | no |
| CPU used (cores), mean | 1.586 | 1.587 | +0.0% | -0.01718 to +0.01871 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.586 | 1.587 | +0.0% | -0.01718 to +0.01871 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.9 | 421.8 | +0.2% | -5.917 to +7.692 | no |
| HPA replicas, mean | 2.003 | 2.121 | +5.9% | -0.001148 to +0.2381 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 45.25 | 45.97 | +1.6% | +0.5516 to +0.9047 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 830.6 | 837.8 | +0.9% | +3.344 to +11.06 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3917 | 0.25 | -36.2% | -0.5062 to +0.2229 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1 | -41.2% | -2.725 to +1.325 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.8 | 148.6 | +7.0% | +5.176 to +14.33 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.498 | -8.4% | -1.257 to +0.2531 | no |
| node-hours | 2.516 | 2.304 | -8.4% | -0.527 to +0.1031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 273.7 | -0.3% | -2.49 to +1.016 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 258 | -6.0% | -39.95 to +6.915 | no |
| response time (ms), mean | 494.9 | 501.3 | +1.3% | -9.254 to +22.01 | no |
| response time (ms), 95th percentile | 1956 | 1968 | +0.6% | -61.48 to +85.84 | no |
| response time (ms), 99th percentile | 2903 | 2924 | +0.7% | -136 to +178.4 | no |
| time over the response line (% of samples) | 24.35 | 25 | +2.7% | -0.3679 to +1.674 | no |
| failed requests (%) | 0 | 0.0122 | +0.0122 (native is 0) | -0.01539 to +0.03978 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.7 | +0.9% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.3 | +8.3 (native is 0) | +6.579 to +10.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.91 | 17.92 | +0.0% | -1.87 to +1.883 | no |
| utilisation (used / allocatable) | 0.0661 | 0.0726 | +9.8% | -0.003076 to +0.01607 | no |
| CPU used (cores), mean | 1.586 | 1.579 | -0.5% | -0.03988 to +0.02483 | no |
| Omni's own CPU (cores), mean | 0 | 0.01172 | +0.0117 (native is 0) | +0.011 to +0.01244 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.586 | 1.591 | +0.3% | -0.02809 to +0.03648 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.9 | 391.8 | -6.9% | -71.39 to +13.14 | no |
| HPA replicas, mean | 2.003 | 2.307 | +15.2% | +0.05869 to +0.5494 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0.3 | 1 | +233.3% | -0.4705 to +1.871 | no |
| pod start wait, mean (s) | 0.3 | 1 | +233.3% | -0.4705 to +1.871 | no |
| host CPU busy, the real machine under kind (%) | 45.25 | 46.14 | +2.0% | +0.1945 to +1.585 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 830.6 | 832.9 | +0.3% | -1.939 to +6.539 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.199 | -13.3% | -2.003 to +0.4015 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3917 | 0.5625 | +43.6% | -0.5624 to +0.9041 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1.9 | +11.8% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.8 | 140.9 | +1.5% | -1.493 to +5.609 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.498 | -8.4% | -1.257 to +0.2531 | no |
| node-hours | 2.516 | 2.304 | -8.4% | -0.5288 to +0.1043 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 273.7 | -0.3% | -2.642 to +1.127 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 258 | -6.0% | -39.99 to +6.916 | no |
| response time (ms), mean | 505 | 501.3 | -0.7% | -31.18 to +23.68 | no |
| response time (ms), 95th percentile | 2118 | 1968 | -7.0% | -312.2 to +13.63 | no |
| response time (ms), 99th percentile | 3170 | 2924 | -7.8% | -510.9 to +18.73 | no |
| time over the response line (% of samples) | 23.25 | 25 | +7.5% | +0.7776 to +2.727 | yes: LOSS |
| failed requests (%) | 0 | 0.0122 | +0.0122 (native is 0) | -0.01539 to +0.03978 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11.7 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.3 | +8.3 (native is 0) | +6.579 to +10.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.34 | 17.92 | -11.9% | -4.217 to -0.6093 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06613 | 0.0726 | +9.8% | -0.003587 to +0.01652 | no |
| CPU used (cores), mean | 1.587 | 1.579 | -0.5% | -0.04801 to +0.03144 | no |
| Omni's own CPU (cores), mean | 0 | 0.01172 | +0.0117 (native is 0) | +0.011 to +0.01244 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.587 | 1.591 | +0.2% | -0.03615 to +0.04302 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.8 | 391.8 | -7.1% | -77.47 to +17.45 | no |
| HPA replicas, mean | 2.121 | 2.307 | +8.7% | -0.07271 to +0.4438 | no |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1 (native is 0) | +0.246 to +1.754 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1 (native is 0) | +0.246 to +1.754 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.97 | 46.14 | +0.4% | -0.5621 to +0.885 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 837.8 | 832.9 | -0.6% | -11.16 to +1.358 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.199 | -13.3% | -2.003 to +0.4015 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.5625 | +125.0% | -0.6119 to +1.237 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.9 | +90.0% | -1.297 to +3.097 | no |
| queue: job turnaround, submitted to done, mean (s) | 148.6 | 140.9 | -5.2% | -14.02 to -1.371 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.485 | -8.6% | -1.2 to +0.1692 | no |
| node-hours | 2.516 | 2.3 | -8.6% | -0.5005 to +0.06864 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.4 | -0.0% | -0.8415 to +0.6939 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 258.2 | -5.9% | -38.01 to +5.367 | no |
| response time (ms), mean | 494.9 | 500.8 | +1.2% | -12.96 to +24.79 | no |
| response time (ms), 95th percentile | 1956 | 2082 | +6.4% | -51.46 to +302.3 | no |
| response time (ms), 99th percentile | 2903 | 3154 | +8.7% | -42.61 to +545.7 | no |
| time over the response line (% of samples) | 24.35 | 23.11 | -5.1% | -2.388 to -0.08678 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.8 | +1.7% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.6 | +8.6 (native is 0) | +6.006 to +11.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.91 | 19.45 | +8.6% | -1.117 to +4.194 | no |
| utilisation (used / allocatable) | 0.0661 | 0.07118 | +7.7% | -0.001079 to +0.01123 | no |
| CPU used (cores), mean | 1.586 | 1.562 | -1.6% | -0.07354 to +0.02392 | no |
| Omni's own CPU (cores), mean | 0 | 0.01261 | +0.0126 (native is 0) | +0.01194 to +0.01328 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.586 | 1.574 | -0.8% | -0.06138 to +0.03699 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.9 | 399 | -5.2% | -49.24 to +5.472 | no |
| HPA replicas, mean | 2.003 | 2.309 | +15.3% | +0.06321 to +0.5494 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.3 | 0.8 | +166.7% | -0.1952 to +1.195 | no |
| pod start wait, mean (s) | 0.3 | 0.8 | +166.7% | -0.1952 to +1.195 | no |
| host CPU busy, the real machine under kind (%) | 45.25 | 46.58 | +2.9% | +1.186 to +1.483 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 830.6 | 840.6 | +1.2% | +5.102 to +14.9 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.081 | -15.3% | -2.091 to +0.2532 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3917 | 0.3125 | -20.2% | -0.3925 to +0.2342 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 0.8 | -52.9% | -2.85 to +1.05 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.8 | 153 | +10.2% | +7.277 to +21.01 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*