# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.519 | 1.51 | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.3 | 159.2 | 160.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.3 | 159.2 | 160.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 132.1 | 136.3 | 132 | 135.3 |
| response time (ms), 95th percentile | 271 | 274.2 | 266 | 273.8 |
| response time (ms), 99th percentile | 367.2 | 391.8 | 379.8 | 383.9 |
| time over the response line (% of samples) | 0.3344 | 0.3483 | 0.2449 | 0.3479 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 1.2 | 3.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.1083 | 0.375 | 0.5817 |
| utilisation (used / allocatable) | 0.03778 | 0.04194 | 0.03783 | 0.04292 |
| CPU used (cores), mean | 0.9068 | 1.006 | 0.908 | 1.03 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00568 | 0.00995 |
| CPU used with Omni's own (cores), mean | 0.9068 | 1.006 | 0.9137 | 1.04 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.3 | 631.7 | 696.5 | 619 |
| HPA replicas, mean | 8.92 | 8.852 | 9.721 | 10.48 |
| pods started | 4.9 | 4.9 | 6.6 | 8.2 |
| pod start wait, total (s) | 8 | 6.6 | 10.3 | 13.5 |
| pod start wait, mean (s) | 1.643 | 1.325 | 1.547 | 1.607 |
| host CPU busy, the real machine under kind (%) | 26.76 | 30.54 | 27.26 | 31.85 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 3 of 10 repetitions (repetitions 5, 6, 8): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.517 | +0.5% | +1.461e-06 to +0.01467 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 160.3 | +0.6% | +0.2435 to +1.775 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 160.3 | +0.6% | +0.2435 to +1.775 | yes: power given |
| response time (ms), mean | 136.3 | 135.3 | -0.7% | -3.402 to +1.426 | no |
| response time (ms), 95th percentile | 274.2 | 273.8 | -0.1% | -9.88 to +9.17 | no |
| response time (ms), 99th percentile | 391.8 | 383.9 | -2.0% | -25.6 to +9.917 | no |
| time over the response line (% of samples) | 0.3483 | 0.3479 | -0.1% | -0.1376 to +0.1368 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 3.2 | +3.2 (native is 0) | +1.1 to +5.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.5817 | +436.9% | +0.02513 to +0.9215 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04194 | 0.04292 | +2.3% | +0.0002736 to +0.001696 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.006 | 1.03 | +2.3% | +0.006566 to +0.0407 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00995 | +0.00995 (native is 0) | +0.007923 to +0.01198 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 1.04 | +3.3% | +0.01529 to +0.05187 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.7 | 619 | -2.0% | -21.9 to -3.471 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.852 | 10.48 | +18.4% | +0.7115 to +2.549 | yes: power given |
| pods started | 4.9 | 8.2 | +67.3% | +1.391 to +5.209 | yes: power given |
| pod start wait, total (s) | 6.6 | 13.5 | +104.5% | +3.093 to +10.71 | yes: LOSS |
| pod start wait, mean (s) | 1.325 | 1.607 | +21.3% | +0.01857 to +0.5462 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.54 | 31.85 | +4.3% | +0.74 to +1.887 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.13e-17 to +1.295e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.51 | -0.7% | -0.01686 to -0.00314 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.3 | -0.1% | -0.926 to +0.6807 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.3 | -0.1% | -0.926 to +0.6807 | no |
| response time (ms), mean | 132.1 | 136.3 | +3.2% | +0.6509 to +7.759 | yes: LOSS |
| response time (ms), 95th percentile | 271 | 274.2 | +1.2% | -5.84 to +12.21 | no |
| response time (ms), 99th percentile | 367.2 | 391.8 | +6.7% | +0.9586 to +48.14 | yes: LOSS |
| time over the response line (% of samples) | 0.3344 | 0.3483 | +4.2% | -0.09697 to +0.1248 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.1083 | -42.5% | -0.3188 to +0.1588 | no |
| utilisation (used / allocatable) | 0.03778 | 0.04194 | +11.0% | +0.003542 to +0.004764 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9068 | 1.006 | +11.0% | +0.085 to +0.1143 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.9068 | 1.006 | +11.0% | +0.085 to +0.1143 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.3 | 631.7 | -9.3% | -71.02 to -58.28 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.92 | 8.852 | -0.8% | -0.1668 to +0.02985 | no |
| pods started | 4.9 | 4.9 | +0.0% | -0.584 to +0.584 | no |
| pod start wait, total (s) | 8 | 6.6 | -17.5% | -4.059 to +1.259 | no |
| pod start wait, mean (s) | 1.643 | 1.325 | -19.4% | -0.7849 to +0.1483 | no |
| host CPU busy, the real machine under kind (%) | 26.76 | 30.54 | +14.1% | +3.268 to +4.28 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.439e-17 to +1.367e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.516 | -0.2% | -0.01133 to +0.005332 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.2 | -0.2% | -1.165 to +0.5847 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.2 | -0.2% | -1.165 to +0.5847 | no |
| response time (ms), mean | 132.1 | 132 | -0.0% | -3.735 to +3.619 | no |
| response time (ms), 95th percentile | 271 | 266 | -1.8% | -18.42 to +8.531 | no |
| response time (ms), 99th percentile | 367.2 | 379.8 | +3.4% | +1.166 to +24 | yes: LOSS |
| time over the response line (% of samples) | 0.3344 | 0.2449 | -26.8% | -0.2468 to +0.06783 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.2 | +1.2 (native is 0) | +0.2583 to +2.142 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.375 | +99.1% | -0.09667 to +0.47 | no |
| utilisation (used / allocatable) | 0.03778 | 0.03783 | +0.1% | -0.000563 to +0.0006617 | no |
| CPU used (cores), mean | 0.9068 | 0.908 | +0.1% | -0.01351 to +0.01588 | no |
| Omni's own CPU (cores), mean | 0 | 0.00568 | +0.00568 (native is 0) | +0.004916 to +0.006444 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9068 | 0.9137 | +0.8% | -0.008311 to +0.02204 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.3 | 696.5 | +0.0% | -10.89 to +11.23 | no |
| HPA replicas, mean | 8.92 | 9.721 | +9.0% | +0.1683 to +1.434 | yes: power given |
| pods started | 4.9 | 6.6 | +34.7% | -0.5124 to +3.912 | no |
| pod start wait, total (s) | 8 | 10.3 | +28.8% | -1.803 to +6.403 | no |
| pod start wait, mean (s) | 1.643 | 1.547 | -5.9% | -0.3568 to +0.1643 | no |
| host CPU busy, the real machine under kind (%) | 26.76 | 27.26 | +1.9% | +0.02614 to +0.9668 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.516 | +0.5% | -0.002876 to +0.01688 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.2 | -0.1% | -1.228 to +0.8923 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.2 | -0.1% | -1.228 to +0.8923 | no |
| response time (ms), mean | 136.3 | 132 | -3.1% | -7.75 to -0.7774 | yes: GAIN |
| response time (ms), 95th percentile | 274.2 | 266 | -3.0% | -15.5 to -0.7496 | yes: GAIN |
| response time (ms), 99th percentile | 391.8 | 379.8 | -3.1% | -36.83 to +12.89 | no |
| time over the response line (% of samples) | 0.3483 | 0.2449 | -29.7% | -0.2534 to +0.04659 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.2 | +1.2 (native is 0) | +0.2583 to +2.142 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.375 | +246.2% | +0.04749 to +0.4858 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04194 | 0.03783 | -9.8% | -0.004915 to -0.003293 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.006 | 0.908 | -9.8% | -0.118 to -0.07902 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00568 | +0.00568 (native is 0) | +0.004916 to +0.006444 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.006 | 0.9137 | -9.2% | -0.1122 to -0.07339 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 631.7 | 696.5 | +10.3% | +51.68 to +77.97 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.852 | 9.721 | +9.8% | +0.2244 to +1.515 | yes: power given |
| pods started | 4.9 | 6.6 | +34.7% | -0.2385 to +3.639 | no |
| pod start wait, total (s) | 6.6 | 10.3 | +56.1% | +0.0363 to +7.364 | yes: LOSS |
| pod start wait, mean (s) | 1.325 | 1.547 | +16.8% | -0.1486 to +0.5928 | no |
| host CPU busy, the real machine under kind (%) | 30.54 | 27.26 | -10.7% | -3.751 to -2.803 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.27e-16 to +1.648e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.517 | -0.2% | -0.008725 to +0.003391 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 160.3 | +0.6% | +0.1422 to +1.631 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 160.3 | +0.6% | +0.1422 to +1.631 | yes: power given |
| response time (ms), mean | 132.1 | 135.3 | +2.4% | -0.3254 to +6.76 | no |
| response time (ms), 95th percentile | 271 | 273.8 | +1.0% | -8.15 to +13.81 | no |
| response time (ms), 99th percentile | 367.2 | 383.9 | +4.6% | -7.388 to +40.8 | no |
| time over the response line (% of samples) | 0.3344 | 0.3479 | +4.0% | -0.1047 to +0.1316 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 3.2 | +3.2 (native is 0) | +1.1 to +5.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.5817 | +208.8% | -0.1005 to +0.8871 | no |
| utilisation (used / allocatable) | 0.03778 | 0.04292 | +13.6% | +0.004152 to +0.006123 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9068 | 1.03 | +13.6% | +0.09965 to +0.147 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00995 | +0.00995 (native is 0) | +0.007923 to +0.01198 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9068 | 1.04 | +14.7% | +0.1078 to +0.1587 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 696.3 | 619 | -11.1% | -87.35 to -67.33 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.92 | 10.48 | +17.5% | +0.6506 to +2.473 | yes: power given |
| pods started | 4.9 | 8.2 | +67.3% | +1.193 to +5.407 | yes: power given |
| pod start wait, total (s) | 8 | 13.5 | +68.8% | +1.023 to +9.977 | yes: LOSS |
| pod start wait, mean (s) | 1.643 | 1.607 | -2.2% | -0.4054 to +0.3335 | no |
| host CPU busy, the real machine under kind (%) | 26.76 | 31.85 | +19.0% | +4.085 to +6.09 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*