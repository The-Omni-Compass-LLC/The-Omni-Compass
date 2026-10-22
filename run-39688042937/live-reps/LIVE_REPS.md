# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.508 | 1.515 | 1.508 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 160 | 158.4 | 160.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 160 | 158.4 | 160.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 146.9 | 149.2 | 144.8 | 147.5 |
| response time (ms), 95th percentile | 289.7 | 293.5 | 289 | 291.5 |
| response time (ms), 99th percentile | 408.4 | 406.3 | 398.7 | 415.7 |
| time over the response line (% of samples) | 0.3353 | 0.2449 | 0.3078 | 0.2944 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 1.4 | 1.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.1617 | 0.4367 | 0.2217 |
| utilisation (used / allocatable) | 0.03779 | 0.0424 | 0.03834 | 0.04248 |
| CPU used (cores), mean | 0.9069 | 1.018 | 0.9201 | 1.02 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00552 | 0.00882 |
| CPU used with Omni's own (cores), mean | 0.9069 | 1.018 | 0.9256 | 1.028 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695 | 623.3 | 686.4 | 623 |
| HPA replicas, mean | 8.961 | 8.911 | 9.692 | 9.87 |
| pods started | 4.6 | 4.7 | 6.8 | 6.2 |
| pod start wait, total (s) | 6.3 | 5.9 | 10.3 | 9.4 |
| pod start wait, mean (s) | 1.35 | 1.253 | 1.482 | 1.501 |
| host CPU busy, the real machine under kind (%) | 26.92 | 30.73 | 27.49 | 31.4 |
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

Omni-Compass stayed native in 5 of 10 repetitions (repetitions 1, 4, 5, 7, 8): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.583e-17 to +9.84e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.517 | +0.1% | -0.006593 to +0.01059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 160.2 | +0.1% | -0.707 to +1.154 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 160.2 | +0.1% | -0.707 to +1.154 | no |
| response time (ms), mean | 149.2 | 147.5 | -1.1% | -4.572 to +1.213 | no |
| response time (ms), 95th percentile | 293.5 | 291.5 | -0.7% | -14.37 to +10.35 | no |
| response time (ms), 99th percentile | 406.3 | 415.7 | +2.3% | -6.47 to +25.14 | no |
| time over the response line (% of samples) | 0.2449 | 0.2944 | +20.2% | -0.1094 to +0.2085 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | -0.05441 to +3.054 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1617 | 0.2217 | +37.1% | -0.1617 to +0.2817 | no |
| utilisation (used / allocatable) | 0.0424 | 0.04248 | +0.2% | -0.0006512 to +0.0008058 | no |
| CPU used (cores), mean | 1.018 | 1.02 | +0.2% | -0.01563 to +0.01934 | no |
| Omni's own CPU (cores), mean | 0 | 0.00882 | +0.00882 (native is 0) | +0.007127 to +0.01051 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.018 | 1.028 | +1.0% | -0.008279 to +0.02963 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 623.3 | 623 | -0.0% | -10.22 to +9.7 | no |
| HPA replicas, mean | 8.911 | 9.87 | +10.8% | +0.2226 to +1.695 | yes: power given |
| pods started | 4.7 | 6.2 | +31.9% | -0.1944 to +3.194 | no |
| pod start wait, total (s) | 5.9 | 9.4 | +59.3% | -0.04059 to +7.041 | no |
| pod start wait, mean (s) | 1.253 | 1.501 | +19.8% | -0.07076 to +0.567 | no |
| host CPU busy, the real machine under kind (%) | 30.73 | 31.4 | +2.2% | +0.2349 to +1.113 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | no |
| node-hours | 1.508 | 1.515 | +0.4% | -0.002166 to +0.0155 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 160 | +1.1% | +0.737 to +2.706 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 160 | +1.1% | +0.737 to +2.706 | yes: power given |
| response time (ms), mean | 146.9 | 149.2 | +1.6% | -0.5977 to +5.262 | no |
| response time (ms), 95th percentile | 289.7 | 293.5 | +1.3% | -4.161 to +11.72 | no |
| response time (ms), 99th percentile | 408.4 | 406.3 | -0.5% | -31.3 to +27.15 | no |
| time over the response line (% of samples) | 0.3353 | 0.2449 | -27.0% | -0.2471 to +0.06633 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.1617 | -26.0% | -0.4112 to +0.2978 | no |
| utilisation (used / allocatable) | 0.03779 | 0.0424 | +12.2% | +0.003928 to +0.005305 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9069 | 1.018 | +12.2% | +0.09426 to +0.1273 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 0.9069 | 1.018 | +12.2% | +0.09426 to +0.1273 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695 | 623.3 | -10.3% | -82.32 to -61.01 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.961 | 8.911 | -0.6% | -0.1499 to +0.05051 | no |
| pods started | 4.6 | 4.7 | +2.2% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 6.3 | 5.9 | -6.3% | -2.159 to +1.359 | no |
| pod start wait, mean (s) | 1.35 | 1.253 | -7.2% | -0.4434 to +0.25 | no |
| host CPU busy, the real machine under kind (%) | 26.92 | 30.73 | +14.1% | +3.342 to +4.267 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.003e-15 to +4.702e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.508 | 1.508 | +0.0% | -0.006103 to +0.006436 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.4 | +0.1% | -0.5132 to +0.8048 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.4 | +0.1% | -0.5132 to +0.8048 | no |
| response time (ms), mean | 146.9 | 144.8 | -1.4% | -5.52 to +1.298 | no |
| response time (ms), 95th percentile | 289.7 | 289 | -0.3% | -13.88 to +12.4 | no |
| response time (ms), 99th percentile | 408.4 | 398.7 | -2.4% | -38.22 to +18.7 | no |
| time over the response line (% of samples) | 0.3353 | 0.3078 | -8.2% | -0.2158 to +0.161 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0.1 | -66.7% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.4 | +1.4 (native is 0) | +0.2715 to +2.528 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.4367 | +100.0% | +0.0003497 to +0.4363 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03779 | 0.03834 | +1.4% | -7.122e-05 to +0.001166 | no |
| CPU used (cores), mean | 0.9069 | 0.9201 | +1.4% | -0.001709 to +0.02798 | no |
| Omni's own CPU (cores), mean | 0 | 0.00552 | +0.00552 (native is 0) | +0.004769 to +0.006271 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9069 | 0.9256 | +2.1% | +0.003175 to +0.03413 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695 | 686.4 | -1.2% | -18.69 to +1.6 | no |
| HPA replicas, mean | 8.961 | 9.692 | +8.2% | +0.1149 to +1.347 | yes: power given |
| pods started | 4.6 | 6.8 | +47.8% | +0.5899 to +3.81 | yes: power given |
| pod start wait, total (s) | 6.3 | 10.3 | +63.5% | +0.0821 to +7.918 | yes: LOSS |
| pod start wait, mean (s) | 1.35 | 1.482 | +9.8% | -0.2409 to +0.5047 | no |
| host CPU busy, the real machine under kind (%) | 26.92 | 27.49 | +2.1% | +0.1853 to +0.9624 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.895e-16 to +2.566e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.508 | -0.4% | -0.01494 to +0.001938 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 158.4 | -1.0% | -2.519 to -0.632 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 158.4 | -1.0% | -2.519 to -0.632 | yes: GAIN |
| response time (ms), mean | 149.2 | 144.8 | -3.0% | -6.468 to -2.419 | yes: GAIN |
| response time (ms), 95th percentile | 293.5 | 289 | -1.5% | -18.82 to +9.776 | no |
| response time (ms), 99th percentile | 406.3 | 398.7 | -1.9% | -32.5 to +17.12 | no |
| time over the response line (% of samples) | 0.2449 | 0.3078 | +25.7% | -0.0365 to +0.1624 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.4 | +1.4 (native is 0) | +0.2715 to +2.528 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1617 | 0.4367 | +170.1% | -0.1446 to +0.6946 | no |
| utilisation (used / allocatable) | 0.0424 | 0.03834 | -9.6% | -0.004759 to -0.00338 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.018 | 0.9201 | -9.6% | -0.1142 to -0.08111 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00552 | +0.00552 (native is 0) | +0.004769 to +0.006271 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.018 | 0.9256 | -9.1% | -0.109 to -0.0753 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 623.3 | 686.4 | +10.1% | +49.85 to +76.39 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.911 | 9.692 | +8.8% | +0.1547 to +1.407 | yes: power given |
| pods started | 4.7 | 6.8 | +44.7% | +0.5023 to +3.698 | yes: power given |
| pod start wait, total (s) | 5.9 | 10.3 | +74.6% | +0.295 to +8.505 | yes: LOSS |
| pod start wait, mean (s) | 1.253 | 1.482 | +18.2% | -0.1278 to +0.5849 | no |
| host CPU busy, the real machine under kind (%) | 30.73 | 27.49 | -10.5% | -3.509 to -2.952 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.623e-16 to +1.25e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.508 | 1.517 | +0.6% | -0.00271 to +0.02004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 160.2 | +1.2% | +0.8137 to +3.076 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 160.2 | +1.2% | +0.8137 to +3.076 | yes: power given |
| response time (ms), mean | 146.9 | 147.5 | +0.4% | -2.562 to +3.867 | no |
| response time (ms), 95th percentile | 289.7 | 291.5 | +0.6% | -10.13 to +13.67 | no |
| response time (ms), 99th percentile | 408.4 | 415.7 | +1.8% | -26.18 to +40.7 | no |
| time over the response line (% of samples) | 0.3353 | 0.2944 | -12.2% | -0.2886 to +0.2069 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0.1 | -66.7% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.5 (native is 0) | -0.05441 to +3.054 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.2217 | +1.5% | -0.3699 to +0.3766 | no |
| utilisation (used / allocatable) | 0.03779 | 0.04248 | +12.4% | +0.003743 to +0.005644 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9069 | 1.02 | +12.4% | +0.08984 to +0.1355 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00882 | +0.00882 (native is 0) | +0.007127 to +0.01051 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9069 | 1.028 | +13.4% | +0.09727 to +0.1457 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695 | 623 | -10.3% | -83.76 to -60.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.961 | 9.87 | +10.1% | +0.1992 to +1.619 | yes: power given |
| pods started | 4.6 | 6.2 | +34.8% | -0.09273 to +3.293 | no |
| pod start wait, total (s) | 6.3 | 9.4 | +49.2% | -0.2458 to +6.446 | no |
| pod start wait, mean (s) | 1.35 | 1.501 | +11.2% | -0.1721 to +0.4749 | no |
| host CPU busy, the real machine under kind (%) | 26.92 | 31.4 | +16.6% | +3.774 to +5.183 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*