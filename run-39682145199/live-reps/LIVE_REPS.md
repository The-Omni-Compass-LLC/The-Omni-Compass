# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.52 | 1.512 | 1.512 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.7 | 158.8 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.7 | 158.8 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 139.7 | 145.4 | 136.1 | 142.7 |
| response time (ms), 95th percentile | 287.1 | 294.9 | 270 | 280.8 |
| response time (ms), 99th percentile | 394.8 | 410.1 | 380.3 | 391.1 |
| time over the response line (% of samples) | 0.4644 | 0.5059 | 0.3214 | 0.3233 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 2.1 | 1.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.2933 | 0.4583 | 0.39 |
| utilisation (used / allocatable) | 0.03804 | 0.04235 | 0.03856 | 0.04308 |
| CPU used (cores), mean | 0.9129 | 1.016 | 0.9255 | 1.034 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00572 | 0.00924 |
| CPU used with Omni's own (cores), mean | 0.9129 | 1.016 | 0.9312 | 1.043 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 691.9 | 625.2 | 684.3 | 615.5 |
| HPA replicas, mean | 8.89 | 8.944 | 10.25 | 9.916 |
| pods started | 5.1 | 4.7 | 7.5 | 7 |
| pod start wait, total (s) | 8 | 7.5 | 12 | 11.4 |
| pod start wait, mean (s) | 1.56 | 1.59 | 1.572 | 1.617 |
| host CPU busy, the real machine under kind (%) | 27.14 | 31.07 | 27.61 | 31.94 |
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

Omni-Compass stayed native in 3 of 10 repetitions (repetitions 2, 4, 5): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.235e-16 to +6.788e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.509 | -0.2% | -0.01054 to +0.004536 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 159.5 | -0.1% | -0.9022 to +0.5189 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 159.5 | -0.1% | -0.9022 to +0.5189 | no |
| response time (ms), mean | 145.4 | 142.7 | -1.9% | -6.313 to +0.7976 | no |
| response time (ms), 95th percentile | 294.9 | 280.8 | -4.8% | -31.73 to +3.389 | no |
| response time (ms), 99th percentile | 410.1 | 391.1 | -4.6% | -43.6 to +5.659 | no |
| time over the response line (% of samples) | 0.5059 | 0.3233 | -36.1% | -0.3835 to +0.01836 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | +0.7274 to +2.273 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.39 | +33.0% | -0.3476 to +0.5409 | no |
| utilisation (used / allocatable) | 0.04235 | 0.04308 | +1.7% | +4.207e-05 to +0.001419 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.016 | 1.034 | +1.7% | +0.00101 to +0.03406 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00924 | +0.00924 (native is 0) | +0.007549 to +0.01093 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 1.043 | +2.6% | +0.009322 to +0.04422 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 625.2 | 615.5 | -1.5% | -19.08 to -0.133 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.944 | 9.916 | +10.9% | +0.3494 to +1.594 | yes: power given |
| pods started | 4.7 | 7 | +48.9% | +1.129 to +3.471 | yes: power given |
| pod start wait, total (s) | 7.5 | 11.4 | +52.0% | +1.553 to +6.247 | yes: LOSS |
| pod start wait, mean (s) | 1.59 | 1.617 | +1.7% | -0.2348 to +0.2893 | no |
| host CPU busy, the real machine under kind (%) | 31.07 | 31.94 | +2.8% | +0.3102 to +1.425 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.512 | -0.5% | -0.01355 to -0.003122 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.7 | +0.1% | -0.4618 to +0.666 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.7 | +0.1% | -0.4618 to +0.666 | no |
| response time (ms), mean | 139.7 | 145.4 | +4.1% | +0.4795 to +10.91 | yes: LOSS |
| response time (ms), 95th percentile | 287.1 | 294.9 | +2.7% | -10.59 to +26.3 | no |
| response time (ms), 99th percentile | 394.8 | 410.1 | +3.9% | -6.919 to +37.55 | no |
| time over the response line (% of samples) | 0.4644 | 0.5059 | +8.9% | -0.1561 to +0.239 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.2933 | +53.0% | -0.2079 to +0.4112 | no |
| utilisation (used / allocatable) | 0.03804 | 0.04235 | +11.3% | +0.003751 to +0.004869 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9129 | 1.016 | +11.3% | +0.09002 to +0.1169 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.9129 | 1.016 | +11.3% | +0.09002 to +0.1169 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 691.9 | 625.2 | -9.6% | -75.95 to -57.54 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.89 | 8.944 | +0.6% | -0.02895 to +0.1384 | no |
| pods started | 5.1 | 4.7 | -7.8% | -0.9001 to +0.1001 | no |
| pod start wait, total (s) | 8 | 7.5 | -6.2% | -2.444 to +1.444 | no |
| pod start wait, mean (s) | 1.56 | 1.59 | +1.9% | -0.2754 to +0.3354 | no |
| host CPU busy, the real machine under kind (%) | 27.14 | 31.07 | +14.5% | +3.418 to +4.442 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.91e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.511 | -0.6% | -0.01692 to -8.033e-05 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 158.8 | -0.5% | -1.553 to +0.03042 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 158.8 | -0.5% | -1.553 to +0.03042 | no |
| response time (ms), mean | 139.7 | 136.1 | -2.6% | -7.242 to -0.04409 | yes: GAIN |
| response time (ms), 95th percentile | 287.1 | 270 | -5.9% | -29.78 to -4.35 | yes: GAIN |
| response time (ms), 99th percentile | 394.8 | 380.3 | -3.7% | -29.49 to +0.5689 | no |
| time over the response line (% of samples) | 0.4644 | 0.3214 | -30.8% | -0.3172 to +0.03124 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.1 | +2.1 (native is 0) | +0.6129 to +3.587 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.4583 | +139.1% | -0.02606 to +0.5594 | no |
| utilisation (used / allocatable) | 0.03804 | 0.03856 | +1.4% | -0.0001361 to +0.001183 | no |
| CPU used (cores), mean | 0.9129 | 0.9255 | +1.4% | -0.003266 to +0.0284 | no |
| Omni's own CPU (cores), mean | 0 | 0.00572 | +0.00572 (native is 0) | +0.004748 to +0.006692 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9129 | 0.9312 | +2.0% | +0.001701 to +0.03487 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 691.9 | 684.3 | -1.1% | -19.04 to +3.835 | no |
| HPA replicas, mean | 8.89 | 10.25 | +15.2% | +0.5914 to +2.12 | yes: power given |
| pods started | 5.1 | 7.5 | +47.1% | +0.7412 to +4.059 | yes: power given |
| pod start wait, total (s) | 8 | 12 | +50.0% | +0.3839 to +7.616 | yes: LOSS |
| pod start wait, mean (s) | 1.56 | 1.572 | +0.8% | -0.3105 to +0.3343 | no |
| host CPU busy, the real machine under kind (%) | 27.14 | 27.61 | +1.7% | -0.1372 to +1.079 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.062e-15 to +1.733e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.511 | -0.0% | -0.01073 to +0.0104 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.7 | 158.8 | -0.5% | -1.948 to +0.2218 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.7 | 158.8 | -0.5% | -1.948 to +0.2218 | no |
| response time (ms), mean | 145.4 | 136.1 | -6.4% | -14.77 to -3.906 | yes: GAIN |
| response time (ms), 95th percentile | 294.9 | 270 | -8.5% | -44.89 to -4.956 | yes: GAIN |
| response time (ms), 99th percentile | 410.1 | 380.3 | -7.3% | -57.35 to -2.199 | yes: GAIN |
| time over the response line (% of samples) | 0.5059 | 0.3214 | -36.5% | -0.4656 to +0.09673 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | -50.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.1 | +2.1 (native is 0) | +0.6129 to +3.587 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.4583 | +56.3% | -0.2319 to +0.5619 | no |
| utilisation (used / allocatable) | 0.04235 | 0.03856 | -8.9% | -0.004381 to -0.003192 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.016 | 0.9255 | -8.9% | -0.1051 to -0.07661 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00572 | +0.00572 (native is 0) | +0.004748 to +0.006692 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.016 | 0.9312 | -8.4% | -0.09993 to -0.07038 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 625.2 | 684.3 | +9.5% | +44.96 to +73.33 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.944 | 10.25 | +14.5% | +0.5438 to +2.058 | yes: power given |
| pods started | 4.7 | 7.5 | +59.6% | +0.9904 to +4.61 | yes: power given |
| pod start wait, total (s) | 7.5 | 12 | +60.0% | +1.008 to +7.992 | yes: LOSS |
| pod start wait, mean (s) | 1.59 | 1.572 | -1.1% | -0.2105 to +0.1742 | no |
| host CPU busy, the real machine under kind (%) | 31.07 | 27.61 | -11.1% | -3.761 to -3.158 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.624e-16 to +6.953e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.509 | -0.7% | -0.02 to -0.002667 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.5 | -0.1% | -0.9157 to +0.7365 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.5 | -0.1% | -0.9157 to +0.7365 | no |
| response time (ms), mean | 139.7 | 142.7 | +2.1% | -1.977 to +7.854 | no |
| response time (ms), 95th percentile | 287.1 | 280.8 | -2.2% | -20 to +7.365 | no |
| response time (ms), 99th percentile | 394.8 | 391.1 | -0.9% | -23.18 to +15.87 | no |
| time over the response line (% of samples) | 0.4644 | 0.3233 | -30.4% | -0.3164 to +0.03417 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | +0.7274 to +2.273 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.39 | +103.5% | -0.253 to +0.6497 | no |
| utilisation (used / allocatable) | 0.03804 | 0.04308 | +13.3% | +0.004272 to +0.00581 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9129 | 1.034 | +13.3% | +0.1025 to +0.1394 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00924 | +0.00924 (native is 0) | +0.007549 to +0.01093 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9129 | 1.043 | +14.3% | +0.1106 to +0.1498 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 691.9 | 615.5 | -11.0% | -86.37 to -66.33 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.89 | 9.916 | +11.5% | +0.4038 to +1.649 | yes: power given |
| pods started | 5.1 | 7 | +37.3% | +0.8634 to +2.937 | yes: power given |
| pod start wait, total (s) | 8 | 11.4 | +42.5% | +1.133 to +5.667 | yes: LOSS |
| pod start wait, mean (s) | 1.56 | 1.617 | +3.7% | -0.161 to +0.2755 | no |
| host CPU busy, the real machine under kind (%) | 27.14 | 31.94 | +17.7% | +4.003 to +5.592 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*