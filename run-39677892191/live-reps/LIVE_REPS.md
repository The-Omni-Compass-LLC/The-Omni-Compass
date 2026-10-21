# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.509 | 1.516 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.3 | 159.1 | 159.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.3 | 159.1 | 159.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 125.7 | 128.6 | 124.1 | 127.7 |
| response time (ms), 95th percentile | 261.3 | 258.4 | 250.9 | 255 |
| response time (ms), 99th percentile | 369.5 | 358.3 | 356 | 358.2 |
| time over the response line (% of samples) | 0.4139 | 0.2595 | 0.2319 | 0.2071 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 1.8 | 1.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.1067 | 0.24 | 0.4983 |
| utilisation (used / allocatable) | 0.03731 | 0.04178 | 0.03779 | 0.04232 |
| CPU used (cores), mean | 0.8956 | 1.003 | 0.907 | 1.016 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00549 | 0.00865 |
| CPU used with Omni's own (cores), mean | 0.8956 | 1.003 | 0.9125 | 1.024 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.3 | 634.3 | 698.4 | 627.3 |
| HPA replicas, mean | 8.921 | 8.884 | 9.958 | 9.926 |
| pods started | 4.6 | 5 | 7.4 | 7 |
| pod start wait, total (s) | 7.3 | 7.8 | 11.2 | 12 |
| pod start wait, mean (s) | 1.563 | 1.577 | 1.495 | 1.707 |
| host CPU busy, the real machine under kind (%) | 26.52 | 30.49 | 27.25 | 31.3 |
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

Omni-Compass stayed native in 4 of 10 repetitions (repetitions 1, 7, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | no |
| node-hours | 1.509 | 1.512 | +0.2% | -0.0053 to +0.01197 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.7 | +0.3% | -0.4588 to +1.427 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.7 | +0.3% | -0.4588 to +1.427 | no |
| response time (ms), mean | 128.6 | 127.7 | -0.7% | -3.692 to +1.98 | no |
| response time (ms), 95th percentile | 258.4 | 255 | -1.3% | -13.34 to +6.645 | no |
| response time (ms), 99th percentile | 358.3 | 358.2 | -0.0% | -19.93 to +19.73 | no |
| time over the response line (% of samples) | 0.2595 | 0.2071 | -20.2% | -0.1611 to +0.05634 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | +0.5315 to +2.469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.4983 | +367.2% | +0.03427 to +0.7491 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04178 | 0.04232 | +1.3% | -5.176e-05 to +0.00113 | no |
| CPU used (cores), mean | 1.003 | 1.016 | +1.3% | -0.001242 to +0.02711 | no |
| Omni's own CPU (cores), mean | 0 | 0.00865 | +0.00865 (native is 0) | +0.006888 to +0.01041 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.003 | 1.024 | +2.2% | +0.006571 to +0.0366 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 634.3 | 627.3 | -1.1% | -15.81 to +1.815 | no |
| HPA replicas, mean | 8.884 | 9.926 | +11.7% | +0.3866 to +1.697 | yes: power given |
| pods started | 5 | 7 | +40.0% | +0.4548 to +3.545 | yes: power given |
| pod start wait, total (s) | 7.8 | 12 | +53.8% | +1.04 to +7.36 | yes: LOSS |
| pod start wait, mean (s) | 1.577 | 1.707 | +8.2% | -0.2306 to +0.4904 | no |
| host CPU busy, the real machine under kind (%) | 30.49 | 31.3 | +2.7% | +0.4389 to +1.178 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.624e-16 to +6.953e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.509 | -0.3% | -0.0156 to +0.005604 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.3 | +0.3% | -0.6374 to +1.583 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.3 | +0.3% | -0.6374 to +1.583 | no |
| response time (ms), mean | 125.7 | 128.6 | +2.3% | -0.9221 to +6.772 | no |
| response time (ms), 95th percentile | 261.3 | 258.4 | -1.1% | -14.38 to +8.597 | no |
| response time (ms), 99th percentile | 369.5 | 358.3 | -3.0% | -33.15 to +10.64 | no |
| time over the response line (% of samples) | 0.4139 | 0.2595 | -37.3% | -0.3216 to +0.01279 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | -50.0% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.1067 | -63.6% | -0.4535 to +0.08014 | no |
| utilisation (used / allocatable) | 0.03731 | 0.04178 | +12.0% | +0.003947 to +0.004988 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8956 | 1.003 | +12.0% | +0.09473 to +0.1197 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.8956 | 1.003 | +12.0% | +0.09473 to +0.1197 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.3 | 634.3 | -10.2% | -82.9 to -61.12 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.921 | 8.884 | -0.4% | -0.08168 to +0.006822 | no |
| pods started | 4.6 | 5 | +8.7% | -0.2911 to +1.091 | no |
| pod start wait, total (s) | 7.3 | 7.8 | +6.8% | -1.385 to +2.385 | no |
| pod start wait, mean (s) | 1.563 | 1.577 | +0.9% | -0.2608 to +0.2875 | no |
| host CPU busy, the real machine under kind (%) | 26.52 | 30.49 | +15.0% | +3.564 to +4.378 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.235e-16 to +6.788e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.2% | +0.001052 to +0.003615 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.1 | +0.2% | +0.1751 to +0.5629 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.1 | +0.2% | +0.1751 to +0.5629 | yes: power given |
| response time (ms), mean | 125.7 | 124.1 | -1.2% | -5.394 to +2.367 | no |
| response time (ms), 95th percentile | 261.3 | 250.9 | -4.0% | -24.92 to +4.135 | no |
| response time (ms), 99th percentile | 369.5 | 356 | -3.7% | -36.59 to +9.539 | no |
| time over the response line (% of samples) | 0.4139 | 0.2319 | -44.0% | -0.4218 to +0.0577 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | -50.0% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.8 | +1.8 (native is 0) | +0.2621 to +3.338 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.24 | -18.2% | -0.3314 to +0.2248 | no |
| utilisation (used / allocatable) | 0.03731 | 0.03779 | +1.3% | -8.574e-05 to +0.001038 | no |
| CPU used (cores), mean | 0.8956 | 0.907 | +1.3% | -0.002058 to +0.02491 | no |
| Omni's own CPU (cores), mean | 0 | 0.00549 | +0.00549 (native is 0) | +0.004493 to +0.006487 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8956 | 0.9125 | +1.9% | +0.003303 to +0.03053 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.3 | 698.4 | -1.1% | -17.69 to +1.869 | no |
| HPA replicas, mean | 8.921 | 9.958 | +11.6% | +0.271 to +1.801 | yes: power given |
| pods started | 4.6 | 7.4 | +60.9% | +0.9904 to +4.61 | yes: power given |
| pod start wait, total (s) | 7.3 | 11.2 | +53.4% | +0.1839 to +7.616 | yes: LOSS |
| pod start wait, mean (s) | 1.563 | 1.495 | -4.4% | -0.3817 to +0.2444 | no |
| host CPU busy, the real machine under kind (%) | 26.52 | 27.25 | +2.7% | +0.3919 to +1.061 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.576e-16 to +3.8e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.509 | 1.516 | +0.5% | -0.002832 to +0.0175 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | -0.1% | -1.208 to +0.9998 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.1 | -0.1% | -1.208 to +0.9998 | no |
| response time (ms), mean | 128.6 | 124.1 | -3.5% | -7.698 to -1.179 | yes: GAIN |
| response time (ms), 95th percentile | 258.4 | 250.9 | -2.9% | -19.34 to +4.33 | no |
| response time (ms), 99th percentile | 358.3 | 356 | -0.6% | -23.7 to +19.15 | no |
| time over the response line (% of samples) | 0.2595 | 0.2319 | -10.7% | -0.2494 to +0.1942 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.8 | +1.8 (native is 0) | +0.2621 to +3.338 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.24 | +125.0% | -0.05093 to +0.3176 | no |
| utilisation (used / allocatable) | 0.04178 | 0.03779 | -9.6% | -0.004343 to -0.003641 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.003 | 0.907 | -9.6% | -0.1042 to -0.08737 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00549 | +0.00549 (native is 0) | +0.004493 to +0.006487 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.003 | 0.9125 | -9.0% | -0.09892 to -0.0817 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 634.3 | 698.4 | +10.1% | +54.15 to +74.05 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.884 | 9.958 | +12.1% | +0.2886 to +1.859 | yes: power given |
| pods started | 5 | 7.4 | +48.0% | +0.7758 to +4.024 | yes: power given |
| pod start wait, total (s) | 7.8 | 11.2 | +43.6% | +0.3802 to +6.42 | yes: LOSS |
| pod start wait, mean (s) | 1.577 | 1.495 | -5.2% | -0.3089 to +0.145 | no |
| host CPU busy, the real machine under kind (%) | 30.49 | 27.25 | -10.6% | -3.464 to -3.025 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.624e-16 to +6.953e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.513 | -0.1% | -0.00591 to +0.002576 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.7 | +0.6% | +0.4217 to +1.492 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.7 | +0.6% | +0.4217 to +1.492 | yes: power given |
| response time (ms), mean | 125.7 | 127.7 | +1.6% | -0.2246 to +4.362 | no |
| response time (ms), 95th percentile | 261.3 | 255 | -2.4% | -16.56 to +4.089 | no |
| response time (ms), 99th percentile | 369.5 | 358.2 | -3.1% | -34.03 to +11.33 | no |
| time over the response line (% of samples) | 0.4139 | 0.2071 | -50.0% | -0.4165 to +0.002895 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | +0.5315 to +2.469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.4983 | +69.9% | -0.228 to +0.638 | no |
| utilisation (used / allocatable) | 0.03731 | 0.04232 | +13.4% | +0.004303 to +0.00571 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8956 | 1.016 | +13.4% | +0.1033 to +0.137 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00865 | +0.00865 (native is 0) | +0.006888 to +0.01041 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8956 | 1.024 | +14.4% | +0.1112 to +0.1465 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.3 | 627.3 | -11.2% | -89.36 to -68.65 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.921 | 9.926 | +11.3% | +0.3717 to +1.637 | yes: power given |
| pods started | 4.6 | 7 | +52.2% | +0.7073 to +4.093 | yes: power given |
| pod start wait, total (s) | 7.3 | 12 | +64.4% | +0.9292 to +8.471 | yes: LOSS |
| pod start wait, mean (s) | 1.563 | 1.707 | +9.2% | -0.1309 to +0.4174 | no |
| host CPU busy, the real machine under kind (%) | 26.52 | 31.3 | +18.0% | +4.165 to +5.393 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*