# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.514 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 160 | 159.1 | 160.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 160 | 159.1 | 160.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 146.9 | 150.6 | 143.8 | 150 |
| response time (ms), 95th percentile | 294.4 | 304.2 | 284.8 | 296.1 |
| response time (ms), 99th percentile | 421.4 | 405.4 | 405.5 | 408.1 |
| time over the response line (% of samples) | 0.5289 | 0.3876 | 0.4115 | 0.4139 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0.2 | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 2.6 | 2.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.1333 | 0.3667 | 0.3283 |
| utilisation (used / allocatable) | 0.03834 | 0.043 | 0.03869 | 0.04367 |
| CPU used (cores), mean | 0.9202 | 1.032 | 0.9285 | 1.048 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00617 | 0.01025 |
| CPU used with Omni's own (cores), mean | 0.9202 | 1.032 | 0.9347 | 1.058 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.1 | 616.6 | 681.7 | 608.1 |
| HPA replicas, mean | 9.031 | 8.898 | 10.46 | 10.16 |
| pods started | 4.1 | 4.6 | 7.3 | 7.6 |
| pod start wait, total (s) | 6.8 | 6.8 | 10.9 | 12.3 |
| pod start wait, mean (s) | 1.683 | 1.492 | 1.515 | 1.62 |
| host CPU busy, the real machine under kind (%) | 27.38 | 31.39 | 27.91 | 32.45 |
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

Omni-Compass stayed native in 2 of 10 repetitions (repetitions 5, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.514 | 1.514 | +0.0% | -0.008922 to +0.009922 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 160.2 | +0.1% | -0.7145 to +1.088 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 160.2 | +0.1% | -0.7145 to +1.088 | no |
| response time (ms), mean | 150.6 | 150 | -0.4% | -2.805 to +1.602 | no |
| response time (ms), 95th percentile | 304.2 | 296.1 | -2.7% | -15.84 to -0.4902 | yes: GAIN |
| response time (ms), 99th percentile | 405.4 | 408.1 | +0.7% | -15.45 to +20.84 | no |
| time over the response line (% of samples) | 0.3876 | 0.4139 | +6.8% | -0.1526 to +0.2052 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.5 | +2.5 (native is 0) | +1.183 to +3.817 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.3283 | +146.3% | -0.0668 to +0.4568 | no |
| utilisation (used / allocatable) | 0.043 | 0.04367 | +1.6% | -0.0001408 to +0.001483 | no |
| CPU used (cores), mean | 1.032 | 1.048 | +1.6% | -0.003378 to +0.03559 | no |
| Omni's own CPU (cores), mean | 0 | 0.01025 | +0.0103 (native is 0) | +0.008645 to +0.01186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.032 | 1.058 | +2.6% | +0.005949 to +0.04676 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 616.6 | 608.1 | -1.4% | -18.55 to +1.564 | no |
| HPA replicas, mean | 8.898 | 10.16 | +14.2% | +0.5406 to +1.983 | yes: power given |
| pods started | 4.6 | 7.6 | +65.2% | +1.348 to +4.652 | yes: power given |
| pod start wait, total (s) | 6.8 | 12.3 | +80.9% | +2.536 to +8.464 | yes: LOSS |
| pod start wait, mean (s) | 1.492 | 1.62 | +8.6% | -0.1424 to +0.3994 | no |
| host CPU busy, the real machine under kind (%) | 31.39 | 32.45 | +3.4% | +0.4482 to +1.675 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.895e-17 to +7.995e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.514 | -0.1% | -0.00938 to +0.007713 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 160 | +0.6% | +0.002614 to +1.891 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 160 | +0.6% | +0.002614 to +1.891 | yes: power given |
| response time (ms), mean | 146.9 | 150.6 | +2.6% | +1.049 to +6.487 | yes: LOSS |
| response time (ms), 95th percentile | 294.4 | 304.2 | +3.3% | +0.186 to +19.48 | yes: LOSS |
| response time (ms), 99th percentile | 421.4 | 405.4 | -3.8% | -37.15 to +5.261 | no |
| time over the response line (% of samples) | 0.5289 | 0.3876 | -26.7% | -0.3227 to +0.04021 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0.2 | -66.7% | -1.003 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.1333 | -59.6% | -0.5347 to +0.1413 | no |
| utilisation (used / allocatable) | 0.03834 | 0.043 | +12.1% | +0.003881 to +0.005428 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9202 | 1.032 | +12.1% | +0.09316 to +0.1303 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.9202 | 1.032 | +12.1% | +0.09316 to +0.1303 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.1 | 616.6 | -10.1% | -78.59 to -60.44 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.031 | 8.898 | -1.5% | -0.235 to -0.03236 | yes: GAIN |
| pods started | 4.1 | 4.6 | +12.2% | -0.343 to +1.343 | no |
| pod start wait, total (s) | 6.8 | 6.8 | +0.0% | -1.216 to +1.216 | no |
| pod start wait, mean (s) | 1.683 | 1.492 | -11.4% | -0.4806 to +0.09727 | no |
| host CPU busy, the real machine under kind (%) | 27.38 | 31.39 | +14.6% | +3.462 to +4.54 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.206e-16 to +5.43e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.514 | -0.0% | -0.006205 to +0.005205 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.1 | +0.0% | -0.5761 to +0.623 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.1 | +0.0% | -0.5761 to +0.623 | no |
| response time (ms), mean | 146.9 | 143.8 | -2.1% | -6.282 to +0.1072 | no |
| response time (ms), 95th percentile | 294.4 | 284.8 | -3.3% | -18.12 to -1.062 | yes: GAIN |
| response time (ms), 99th percentile | 421.4 | 405.5 | -3.8% | -39.11 to +7.373 | no |
| time over the response line (% of samples) | 0.5289 | 0.4115 | -22.2% | -0.3648 to +0.1301 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0.2 | -66.7% | -1.003 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.6 | +2.6 (native is 0) | +0.8414 to +4.359 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.3667 | +11.1% | -0.3262 to +0.3995 | no |
| utilisation (used / allocatable) | 0.03834 | 0.03869 | +0.9% | -0.0003373 to +0.001026 | no |
| CPU used (cores), mean | 0.9202 | 0.9285 | +0.9% | -0.008095 to +0.02463 | no |
| Omni's own CPU (cores), mean | 0 | 0.00617 | +0.00617 (native is 0) | +0.005381 to +0.006959 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9202 | 0.9347 | +1.6% | -0.002399 to +0.03127 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.1 | 681.7 | -0.6% | -17.21 to +8.465 | no |
| HPA replicas, mean | 9.031 | 10.46 | +15.8% | +0.721 to +2.137 | yes: power given |
| pods started | 4.1 | 7.3 | +78.0% | +1.422 to +4.978 | yes: power given |
| pod start wait, total (s) | 6.8 | 10.9 | +60.3% | +1.02 to +7.18 | yes: LOSS |
| pod start wait, mean (s) | 1.683 | 1.515 | -10.0% | -0.5908 to +0.2546 | no |
| host CPU busy, the real machine under kind (%) | 27.38 | 27.91 | +1.9% | -0.02134 to +1.079 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.933e-16 to +5.15e-18 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.514 | +0.0% | -0.009101 to +0.009768 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 159.1 | -0.6% | -1.995 to +0.1486 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 159.1 | -0.6% | -1.995 to +0.1486 | no |
| response time (ms), mean | 150.6 | 143.8 | -4.6% | -10.08 to -3.628 | yes: GAIN |
| response time (ms), 95th percentile | 304.2 | 284.8 | -6.4% | -30.21 to -8.639 | yes: GAIN |
| response time (ms), 99th percentile | 405.4 | 405.5 | +0.0% | -16.11 to +16.26 | no |
| time over the response line (% of samples) | 0.3876 | 0.4115 | +6.2% | -0.1598 to +0.2075 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.6 | +2.6 (native is 0) | +0.8414 to +4.359 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.3667 | +175.0% | -0.008848 to +0.4755 | no |
| utilisation (used / allocatable) | 0.043 | 0.03869 | -10.0% | -0.004958 to -0.003663 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.032 | 0.9285 | -10.0% | -0.119 to -0.0879 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00617 | +0.00617 (native is 0) | +0.005381 to +0.006959 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.032 | 0.9347 | -9.4% | -0.1129 to -0.0816 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 616.6 | 681.7 | +10.6% | +52.89 to +77.39 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.898 | 10.46 | +17.6% | +0.8418 to +2.283 | yes: power given |
| pods started | 4.6 | 7.3 | +58.7% | +0.979 to +4.421 | yes: power given |
| pod start wait, total (s) | 6.8 | 10.9 | +60.3% | +1.929 to +6.271 | yes: LOSS |
| pod start wait, mean (s) | 1.492 | 1.515 | +1.6% | -0.3261 to +0.3733 | no |
| host CPU busy, the real machine under kind (%) | 31.39 | 27.91 | -11.1% | -3.854 to -3.091 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.514 | -0.0% | -0.00728 to +0.006614 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 160.2 | +0.7% | +0.3123 to +1.954 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 160.2 | +0.7% | +0.3123 to +1.954 | yes: power given |
| response time (ms), mean | 146.9 | 150 | +2.2% | -0.09402 to +6.428 | no |
| response time (ms), 95th percentile | 294.4 | 296.1 | +0.6% | -6.992 to +10.33 | no |
| response time (ms), 99th percentile | 421.4 | 408.1 | -3.1% | -40.87 to +14.37 | no |
| time over the response line (% of samples) | 0.5289 | 0.4139 | -21.7% | -0.3112 to +0.08133 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 | -100.0% | -1.1 to -0.09985 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.5 | +2.5 (native is 0) | +1.183 to +3.817 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 0.3283 | -0.5% | -0.3728 to +0.3695 | no |
| utilisation (used / allocatable) | 0.03834 | 0.04367 | +13.9% | +0.004231 to +0.006421 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9202 | 1.048 | +13.9% | +0.1015 to +0.1541 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01025 | +0.0103 (native is 0) | +0.008645 to +0.01186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9202 | 1.058 | +15.0% | +0.1105 to +0.1657 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.1 | 608.1 | -11.4% | -90.46 to -65.55 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.031 | 10.16 | +12.5% | +0.4403 to +1.815 | yes: power given |
| pods started | 4.1 | 7.6 | +85.4% | +1.874 to +5.126 | yes: power given |
| pod start wait, total (s) | 6.8 | 12.3 | +80.9% | +2.226 to +8.774 | yes: LOSS |
| pod start wait, mean (s) | 1.683 | 1.62 | -3.8% | -0.322 to +0.1956 | no |
| host CPU busy, the real machine under kind (%) | 27.38 | 32.45 | +18.5% | +4.13 to +5.995 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*