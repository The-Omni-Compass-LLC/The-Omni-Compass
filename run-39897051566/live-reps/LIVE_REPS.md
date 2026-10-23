# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.234 | 6 |
| node-hours | 2.512 | 2.514 | 2.19 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 286.7 | 271.1 | 286.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 286.7 | 247.1 | 286.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 299.3 | 673.5 | 279.9 | 658.6 |
| response time (ms), 95th percentile | 954 | 1430 | 1062 | 1407 |
| response time (ms), 99th percentile | 1366 | 1891 | 1565 | 1874 |
| time over the response line (% of samples) | 16.21 | 58.57 | 16.8 | 58.12 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 24.7 | 8.8 | 24.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 130.3 | 22.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 80 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.02 | 2.188 | 9.858 | 2.148 |
| utilisation (used / allocatable) | 0.05764 | 0.09825 | 0.06609 | 0.09827 |
| CPU used (cores), mean | 1.383 | 2.358 | 1.38 | 2.359 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0494 | 0.02829 |
| CPU used with Omni's own (cores), mean | 1.383 | 2.358 | 1.429 | 2.387 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.1 | 290.2 | 433.4 | 290.2 |
| HPA replicas, mean | 2.008 | 2.032 | 2.675 | 2.936 |
| pods started | 0 | 0 | 1.9 | 1.8 |
| pod start wait, total (s) | 0 | 0 | 4.6 | 4.6 |
| pod start wait, mean (s) | 0 | 0 | 1.34 | 2.158 |
| host CPU busy, the real machine under kind (%) | 39.69 | 75.8 | 41.91 | 76.91 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 759.3 | 1491 | 765.2 | 1492 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.706 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 690.5 | 0.04583 | 684 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1210 | 0.3 | 1270 |
| queue: job turnaround, submitted to done, mean (s) | 67.43 | 997.7 | 74.3 | 987.2 |
| queue: jobs unfinished at the window's end | 0 | 15.5 | 0 | 15.2 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.623e-16 to +1.25e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.51 | -0.2% | -0.01232 to +0.003658 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.7 | 286.2 | -0.2% | -1.391 to +0.5129 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.7 | 286.2 | -0.2% | -1.391 to +0.5129 | no |
| response time (ms), mean | 673.5 | 658.6 | -2.2% | -27.33 to -2.615 | yes: GAIN |
| response time (ms), 95th percentile | 1430 | 1407 | -1.6% | -73.3 to +27.19 | no |
| response time (ms), 99th percentile | 1891 | 1874 | -0.9% | -68.31 to +33.04 | no |
| time over the response line (% of samples) | 58.57 | 58.12 | -0.8% | -1.787 to +0.8896 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.7 | 24.8 | +0.4% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.4 | +22.4 (native is 0) | +17.31 to +27.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.188 | 2.148 | -1.8% | -0.2414 to +0.1614 | no |
| utilisation (used / allocatable) | 0.09825 | 0.09827 | +0.0% | -0.0006348 to +0.0006856 | no |
| CPU used (cores), mean | 2.358 | 2.359 | +0.0% | -0.01524 to +0.01646 | no |
| Omni's own CPU (cores), mean | 0 | 0.02829 | +0.0283 (native is 0) | +0.02496 to +0.03162 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.358 | 2.387 | +1.2% | +0.01497 to +0.04283 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.2 | 290.2 | +0.0% | -1.693 to +1.701 | no |
| HPA replicas, mean | 2.032 | 2.936 | +44.5% | +0.5421 to +1.267 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.5028 to +3.097 | yes: power given |
| pod start wait, total (s) | 0 | 4.6 | +4.6 (native is 0) | +0.827 to +8.373 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.158 | +2.16 (native is 0) | +1.443 to +2.874 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 75.8 | 76.91 | +1.5% | +0.6718 to +1.558 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1491 | 1492 | +0.1% | -8.636 to +11.04 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 690.5 | 684 | -0.9% | -68.68 to +55.73 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1210 | 1270 | +4.9% | -23.91 to +143.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 997.7 | 987.2 | -1.1% | -42.75 to +21.76 | no |
| queue: jobs unfinished at the window's end | 15.5 | 15.2 | -1.9% | -1.421 to +0.8209 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.444e-15 to -8.193e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.514 | +0.1% | -0.007586 to +0.01359 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 286.7 | +5.7% | +12.25 to +18.79 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 286.7 | +5.7% | +12.25 to +18.79 | yes: power given |
| response time (ms), mean | 299.3 | 673.5 | +125.1% | +327.4 to +421.1 | yes: LOSS |
| response time (ms), 95th percentile | 954 | 1430 | +49.9% | +199.6 to +753.1 | yes: LOSS |
| response time (ms), 99th percentile | 1366 | 1891 | +38.5% | +142.7 to +907.8 | yes: LOSS |
| time over the response line (% of samples) | 16.21 | 58.57 | +261.3% | +36.4 to +48.32 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 24.7 | +183.9% | +12.13 to +19.87 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.02 | 2.188 | -78.2% | -10.11 to -5.561 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05764 | 0.09825 | +70.5% | +0.03303 to +0.0482 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 2.358 | +70.5% | +0.7928 to +1.157 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.383 | 2.358 | +70.5% | +0.7928 to +1.157 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.1 | 290.2 | -39.9% | -262.4 to -123.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.008 | 2.032 | +1.2% | -0.07001 to +0.1184 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 39.69 | 75.8 | +91.0% | +33.22 to +39.01 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.3 | 1491 | +96.4% | +693.2 to +770.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 690.5 | +828508.4% | +458.3 to +922.6 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1210 | +172753.3% | +909.3 to +1509 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.43 | 997.7 | +1379.7% | +821.2 to +1039 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.5 | +15.5 (native is 0) | +10.59 to +20.41 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.234 | -12.8% | -1.533 to +0.0005377 | no |
| node-hours | 2.512 | 2.19 | -12.8% | -0.6411 to -0.0009153 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.1 | -0.0% | -1.007 to +0.8951 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 247.1 | -8.9% | -48.52 to +0.3306 | no |
| response time (ms), mean | 299.3 | 279.9 | -6.5% | -32.73 to -5.967 | yes: GAIN |
| response time (ms), 95th percentile | 954 | 1062 | +11.3% | +28.94 to +187 | yes: LOSS |
| response time (ms), 99th percentile | 1366 | 1565 | +14.6% | +18.7 to +380.2 | yes: LOSS |
| time over the response line (% of samples) | 16.21 | 16.8 | +3.6% | -0.2616 to +1.433 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.8 | +1.1% | -0.8204 to +1.02 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.3 | +130 (native is 0) | +51 to +209.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.02 | 9.858 | -1.6% | -1.387 to +1.06 | no |
| utilisation (used / allocatable) | 0.05764 | 0.06609 | +14.7% | +0.001123 to +0.01579 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 1.38 | -0.2% | -0.03957 to +0.0331 | no |
| Omni's own CPU (cores), mean | 0 | 0.0494 | +0.0494 (native is 0) | +0.04362 to +0.05518 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.383 | 1.429 | +3.3% | +0.009894 to +0.08244 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.1 | 433.4 | -10.3% | -95.66 to -3.839 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.008 | 2.675 | +33.3% | +0.3199 to +1.015 | yes: power given |
| pods started | 0 | 1.9 | +1.9 (native is 0) | +0.4129 to +3.387 | yes: power given |
| pod start wait, total (s) | 0 | 4.6 | +4.6 (native is 0) | +0.6937 to +8.506 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.34 | +1.34 (native is 0) | +0.4433 to +2.237 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.69 | 41.91 | +5.6% | +1.857 to +2.579 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.3 | 765.2 | +0.8% | +0.8821 to +10.92 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.706 | -21.6% | -2.524 to -0.06433 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.04583 | -45.0% | -0.0703 to -0.0047 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.3 | -57.1% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 67.43 | 74.3 | +10.2% | +1.231 to +12.53 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.234 | -12.8% | -1.533 to +0.0005377 | no |
| node-hours | 2.514 | 2.19 | -12.9% | -0.6478 to -0.0002536 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 286.7 | 271.1 | -5.4% | -19 to -12.16 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.7 | 247.1 | -13.8% | -66.9 to -12.33 | yes: GAIN |
| response time (ms), mean | 673.5 | 279.9 | -58.4% | -438.9 to -348.3 | yes: GAIN |
| response time (ms), 95th percentile | 1430 | 1062 | -25.8% | -677 to -59.8 | yes: GAIN |
| response time (ms), 99th percentile | 1891 | 1565 | -17.2% | -801.7 to +150.1 | no |
| time over the response line (% of samples) | 58.57 | 16.8 | -71.3% | -47.53 to -36.02 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.7 | 8.8 | -64.4% | -19.88 to -11.92 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.3 | +130 (native is 0) | +51 to +209.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.188 | 9.858 | +350.5% | +5.434 to +9.906 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09825 | 0.06609 | -32.7% | -0.03573 to -0.02858 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.358 | 1.38 | -41.5% | -1.184 to -0.7721 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0494 | +0.0494 (native is 0) | +0.04362 to +0.05518 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.358 | 1.429 | -39.4% | -1.137 to -0.7198 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.2 | 433.4 | +49.3% | +115.8 to +170.6 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.032 | 2.675 | +31.7% | +0.2777 to +1.009 | yes: power given |
| pods started | 0 | 1.9 | +1.9 (native is 0) | +0.4129 to +3.387 | yes: power given |
| pod start wait, total (s) | 0 | 4.6 | +4.6 (native is 0) | +0.6937 to +8.506 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.34 | +1.34 (native is 0) | +0.4433 to +2.237 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 75.8 | 41.91 | -44.7% | -37.05 to -30.74 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1491 | 765.2 | -48.7% | -765.5 to -686.5 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | -66.7% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 690.5 | 0.04583 | -100.0% | -922.7 to -458.3 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1210 | 0.3 | -100.0% | -1510 to -909.6 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 997.7 | 74.3 | -92.6% | -1031 to -816 | yes: GAIN |
| queue: jobs unfinished at the window's end | 15.5 | 0 | -100.0% | -20.41 to -10.59 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.448e-15 to -9.269e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.51 | -0.1% | -0.01014 to +0.007478 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 286.2 | +5.6% | +11.79 to +18.37 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 286.2 | +5.6% | +11.79 to +18.37 | yes: power given |
| response time (ms), mean | 299.3 | 658.6 | +120.1% | +314.4 to +404.2 | yes: LOSS |
| response time (ms), 95th percentile | 954 | 1407 | +47.5% | +172 to +734.7 | yes: LOSS |
| response time (ms), 99th percentile | 1366 | 1874 | +37.2% | +124.6 to +890.7 | yes: LOSS |
| time over the response line (% of samples) | 16.21 | 58.12 | +258.5% | +36.5 to +47.33 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 24.8 | +185.1% | +12.13 to +20.07 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.4 | +22.4 (native is 0) | +17.31 to +27.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.02 | 2.148 | -78.6% | -10.1 to -5.651 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05764 | 0.09827 | +70.5% | +0.03257 to +0.04871 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 2.359 | +70.5% | +0.7817 to +1.169 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02829 | +0.0283 (native is 0) | +0.02496 to +0.03162 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.383 | 2.387 | +72.6% | +0.8132 to +1.194 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.1 | 290.2 | -39.9% | -263.6 to -122.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.008 | 2.936 | +46.2% | +0.5681 to +1.289 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.5028 to +3.097 | yes: power given |
| pod start wait, total (s) | 0 | 4.6 | +4.6 (native is 0) | +0.827 to +8.373 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.158 | +2.16 (native is 0) | +1.443 to +2.874 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.69 | 76.91 | +93.8% | +34.14 to +40.31 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.3 | 1492 | +96.5% | +700.6 to +765.6 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 684 | +820736.5% | +483.6 to +884.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1270 | +181298.3% | +1007 to +1531 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.43 | 987.2 | +1364.1% | +826.7 to +1013 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.2 | +15.2 (native is 0) | +10.63 to +19.77 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*