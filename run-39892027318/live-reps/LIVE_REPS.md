# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.507 | 1.52 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | 159.2 | 159.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | 159.2 | 159.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 110.8 | 112.2 | 108 | 112.5 |
| response time (ms), 95th percentile | 233.4 | 233.3 | 225.6 | 225.3 |
| response time (ms), 99th percentile | 342.8 | 329.9 | 316.8 | 318.9 |
| time over the response line (% of samples) | 0.3085 | 0.2446 | 0.166 | 0.2448 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 5.6 | 5.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1583 | 0.08 | 0.385 |
| utilisation (used / allocatable) | 0.0363 | 0.04083 | 0.03671 | 0.04063 |
| CPU used (cores), mean | 0.8711 | 0.98 | 0.881 | 0.9751 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0165 | 0.02713 |
| CPU used with Omni's own (cores), mean | 0.8711 | 0.98 | 0.8975 | 1.002 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.7 | 647.8 | 718.2 | 652.5 |
| HPA replicas, mean | 8.769 | 8.837 | 9.877 | 9.847 |
| pods started | 4.9 | 5.2 | 6.4 | 6.7 |
| pod start wait, total (s) | 6.7 | 6.9 | 9.1 | 10.3 |
| pod start wait, mean (s) | 1.383 | 1.325 | 1.439 | 1.515 |
| host CPU busy, the real machine under kind (%) | 25.5 | 29.38 | 26.41 | 30.39 |
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

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.594e-16 to +7.818e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.507 | 1.511 | +0.3% | -0.001566 to +0.01023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.2 | +0.3% | -0.2554 to +1.063 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.2 | +0.3% | -0.2554 to +1.063 | no |
| response time (ms), mean | 112.2 | 112.5 | +0.3% | -3.355 to +3.968 | no |
| response time (ms), 95th percentile | 233.3 | 225.3 | -3.4% | -19.13 to +3.046 | no |
| response time (ms), 99th percentile | 329.9 | 318.9 | -3.3% | -36.91 to +14.94 | no |
| time over the response line (% of samples) | 0.2446 | 0.2448 | +0.1% | -0.2853 to +0.2856 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.9 | +5.9 (native is 0) | +3.95 to +7.85 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.385 | +143.2% | -0.1068 to +0.5601 | no |
| utilisation (used / allocatable) | 0.04083 | 0.04063 | -0.5% | -0.001286 to +0.0008798 | no |
| CPU used (cores), mean | 0.98 | 0.9751 | -0.5% | -0.03086 to +0.02111 | no |
| Omni's own CPU (cores), mean | 0 | 0.02713 | +0.0271 (native is 0) | +0.02168 to +0.03258 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.98 | 1.002 | +2.3% | -0.007891 to +0.0524 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 647.8 | 652.5 | +0.7% | -12.27 to +21.6 | no |
| HPA replicas, mean | 8.837 | 9.847 | +11.4% | -0.001218 to +2.021 | no |
| pods started | 5.2 | 6.7 | +28.8% | -0.8423 to +3.842 | no |
| pod start wait, total (s) | 6.9 | 10.3 | +49.3% | -0.6911 to +7.491 | no |
| pod start wait, mean (s) | 1.325 | 1.515 | +14.4% | -0.06808 to +0.4489 | no |
| host CPU busy, the real machine under kind (%) | 29.38 | 30.39 | +3.4% | -0.1257 to +2.136 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.128e-16 to +1.279e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.507 | -0.7% | -0.01605 to -0.003947 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | -0.0% | -0.7184 to +0.6235 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | -0.0% | -0.7184 to +0.6235 | no |
| response time (ms), mean | 110.8 | 112.2 | +1.2% | -1.506 to +4.236 | no |
| response time (ms), 95th percentile | 233.4 | 233.3 | -0.0% | -8.11 to +7.905 | no |
| response time (ms), 99th percentile | 342.8 | 329.9 | -3.8% | -42.84 to +17 | no |
| time over the response line (% of samples) | 0.3085 | 0.2446 | -20.7% | -0.3756 to +0.2477 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1583 | +102.1% | -0.09823 to +0.2582 | no |
| utilisation (used / allocatable) | 0.0363 | 0.04083 | +12.5% | +0.003684 to +0.005389 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8711 | 0.98 | +12.5% | +0.08842 to +0.1293 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.8711 | 0.98 | +12.5% | +0.08842 to +0.1293 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.7 | 647.8 | -10.5% | -90.61 to -61.18 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.769 | 8.837 | +0.8% | -0.07545 to +0.2123 | no |
| pods started | 4.9 | 5.2 | +6.1% | -0.5953 to +1.195 | no |
| pod start wait, total (s) | 6.7 | 6.9 | +3.0% | -1.846 to +2.246 | no |
| pod start wait, mean (s) | 1.383 | 1.325 | -4.2% | -0.3395 to +0.2228 | no |
| host CPU busy, the real machine under kind (%) | 25.5 | 29.38 | +15.2% | +3.109 to +4.642 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.929e-16 to +1.051e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.519 | +0.2% | -0.0003794 to +0.005379 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.2 | +0.2% | -0.07919 to +0.736 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.2 | +0.2% | -0.07919 to +0.736 | no |
| response time (ms), mean | 110.8 | 108 | -2.5% | -6.89 to +1.328 | no |
| response time (ms), 95th percentile | 233.4 | 225.6 | -3.3% | -21.27 to +5.714 | no |
| response time (ms), 99th percentile | 342.8 | 316.8 | -7.6% | -50.51 to -1.507 | yes: GAIN |
| time over the response line (% of samples) | 0.3085 | 0.166 | -46.2% | -0.3144 to +0.02934 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.6 | +5.6 (native is 0) | +3.907 to +7.293 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.08 | +2.1% | -0.1525 to +0.1558 | no |
| utilisation (used / allocatable) | 0.0363 | 0.03671 | +1.1% | -0.0003866 to +0.001214 | no |
| CPU used (cores), mean | 0.8711 | 0.881 | +1.1% | -0.009278 to +0.02913 | no |
| Omni's own CPU (cores), mean | 0 | 0.0165 | +0.0165 (native is 0) | +0.0134 to +0.0196 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8711 | 0.8975 | +3.0% | +0.004515 to +0.04834 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.7 | 718.2 | -0.8% | -19.8 to +8.841 | no |
| HPA replicas, mean | 8.769 | 9.877 | +12.6% | +0.1189 to +2.098 | yes: power given |
| pods started | 4.9 | 6.4 | +30.6% | -0.1605 to +3.161 | no |
| pod start wait, total (s) | 6.7 | 9.1 | +35.8% | -0.4652 to +5.265 | no |
| pod start wait, mean (s) | 1.383 | 1.439 | +4.0% | -0.2745 to +0.3858 | no |
| host CPU busy, the real machine under kind (%) | 25.5 | 26.41 | +3.5% | +0.1042 to +1.698 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.507 | 1.519 | +0.8% | +0.006734 to +0.01827 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.2 | +0.2% | -0.2306 to +0.9823 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.2 | +0.2% | -0.2306 to +0.9823 | no |
| response time (ms), mean | 112.2 | 108 | -3.7% | -8.433 to +0.1411 | no |
| response time (ms), 95th percentile | 233.3 | 225.6 | -3.3% | -21.06 to +5.707 | no |
| response time (ms), 99th percentile | 329.9 | 316.8 | -4.0% | -46.17 to +19.99 | no |
| time over the response line (% of samples) | 0.2446 | 0.166 | -32.1% | -0.3444 to +0.1872 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.6 | +5.6 (native is 0) | +3.907 to +7.293 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.08 | -49.5% | -0.3328 to +0.1761 | no |
| utilisation (used / allocatable) | 0.04083 | 0.03671 | -10.1% | -0.004803 to -0.003443 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.98 | 0.881 | -10.1% | -0.1153 to -0.08263 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0165 | +0.0165 (native is 0) | +0.0134 to +0.0196 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.98 | 0.8975 | -8.4% | -0.1009 to -0.06396 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 647.8 | 718.2 | +10.9% | +53.63 to +87.2 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.837 | 9.877 | +11.8% | -0.009219 to +2.089 | no |
| pods started | 5.2 | 6.4 | +23.1% | -0.3379 to +2.738 | no |
| pod start wait, total (s) | 6.9 | 9.1 | +31.9% | +0.2396 to +4.16 | yes: LOSS |
| pod start wait, mean (s) | 1.325 | 1.439 | +8.6% | -0.1291 to +0.3571 | no |
| host CPU busy, the real machine under kind (%) | 29.38 | 26.41 | -10.1% | -3.467 to -2.482 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.046e-16 to +1.193e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.511 | -0.4% | -0.01319 to +0.001857 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.2 | +0.2% | -0.4684 to +1.181 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.2 | +0.2% | -0.4684 to +1.181 | no |
| response time (ms), mean | 110.8 | 112.5 | +1.5% | -0.4355 to +3.778 | no |
| response time (ms), 95th percentile | 233.4 | 225.3 | -3.5% | -16.31 to +0.0164 | no |
| response time (ms), 99th percentile | 342.8 | 318.9 | -7.0% | -44.12 to -3.694 | yes: GAIN |
| time over the response line (% of samples) | 0.3085 | 0.2448 | -20.7% | -0.1885 to +0.06099 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.9 | +5.9 (native is 0) | +3.95 to +7.85 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.385 | +391.5% | -0.07867 to +0.692 | no |
| utilisation (used / allocatable) | 0.0363 | 0.04063 | +11.9% | +0.003196 to +0.005471 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8711 | 0.9751 | +11.9% | +0.0767 to +0.1313 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02713 | +0.0271 (native is 0) | +0.02168 to +0.03258 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8711 | 1.002 | +15.1% | +0.09884 to +0.1634 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.7 | 652.5 | -9.8% | -83.6 to -58.86 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.769 | 9.847 | +12.3% | +0.1386 to +2.018 | yes: power given |
| pods started | 4.9 | 6.7 | +36.7% | -0.4316 to +4.032 | no |
| pod start wait, total (s) | 6.7 | 10.3 | +53.7% | -0.03487 to +7.235 | no |
| pod start wait, mean (s) | 1.383 | 1.515 | +9.5% | -0.06865 to +0.3328 | no |
| host CPU busy, the real machine under kind (%) | 25.5 | 30.39 | +19.1% | +3.534 to +6.228 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*