# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.516 | 1.518 | 1.518 | 1.518 | 1.518 | 1.52 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.3 | 158.5 | 158.4 | 158.7 | 158.5 | 158.7 | 158.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.3 | 158.5 | 158.4 | 158.7 | 158.5 | 158.7 | 158.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 138.7 | 73.37 | 72.72 | 72.84 | 74.09 | 73.72 | 73.62 | 74.47 |
| response time (ms), 95th percentile | 309.3 | 108.6 | 108.6 | 108.2 | 110 | 109.3 | 109.5 | 112.9 |
| response time (ms), 99th percentile | 506.8 | 143.5 | 146.6 | 141.6 | 165.2 | 160.9 | 144.6 | 155.3 |
| time over the response line (% of samples) | 1.859 | 0.02424 | 0 | 0.01212 | 0.01212 | 0.03636 | 0.03636 | 0.02424 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.6 | 14.3 | 17.5 | 16 | 17.4 | 19.9 | 20.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 70 | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.185 | 0.1567 | 0.21 | 0.1067 | 0.05333 | 0.1317 | 0.2383 |
| utilisation (used / allocatable) | 0.03557 | 0.03417 | 0.03387 | 0.03386 | 0.03433 | 0.03407 | 0.03425 | 0.03488 |
| CPU used (cores), mean | 0.8537 | 0.82 | 0.8128 | 0.8126 | 0.8238 | 0.8176 | 0.822 | 0.8371 |
| Omni's own CPU (cores), mean | 0 | 0.00758 | 0.00541 | 0.00613 | 0.0067 | 0.01253 | 0.02233 | 0.06186 |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.8276 | 0.8182 | 0.8188 | 0.8305 | 0.8301 | 0.8444 | 0.899 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 830.9 | 838.1 | 839.7 | 826.9 | 829.7 | 823.4 | 813.2 |
| HPA replicas, mean | 8.115 | 7.497 | 7.907 | 7.872 | 7.072 | 7.472 | 8.156 | 8.444 |
| pods started | 5.4 | 3.6 | 3.3 | 4.3 | 3.5 | 4.5 | 4.6 | 4.9 |
| pod start wait, total (s) | 7.9 | 5.6 | 4.7 | 6.9 | 5.1 | 6.2 | 6.1 | 6.9 |
| pod start wait, mean (s) | 1.467 | 1.475 | 1.41 | 1.615 | 1.417 | 1.35 | 1.373 | 1.443 |
| host CPU busy, the real machine under kind (%) | 25.79 | 25.01 | 24.83 | 24.8 | 25.16 | 25.12 | 25.64 | 27.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.516 | -0.1% | -0.003362 to +0.001696 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.3 | -0.3% | -0.8835 to +0.03863 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.3 | -0.3% | -0.8835 to +0.03863 | no |
| response time (ms), mean | 138.7 | 73.37 | -47.1% | -92.45 to -38.27 | yes: GAIN |
| response time (ms), 95th percentile | 309.3 | 108.6 | -64.9% | -274.9 to -126.5 | yes: GAIN |
| response time (ms), 99th percentile | 506.8 | 143.5 | -71.7% | -504 to -222.5 | yes: GAIN |
| time over the response line (% of samples) | 1.859 | 0.02424 | -98.7% | -3.153 to -0.517 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | -100.0% | -3.431 to -0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.6 | +15.6 (native is 0) | +11.83 to +19.37 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.185 | +42.3% | -0.2481 to +0.3581 | no |
| utilisation (used / allocatable) | 0.03557 | 0.03417 | -4.0% | -0.002359 to -0.0004525 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8537 | 0.82 | -4.0% | -0.05661 to -0.01086 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00758 | +0.00758 (native is 0) | +0.006162 to +0.008998 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.8276 | -3.1% | -0.04794 to -0.004362 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 830.9 | +2.8% | +1.546 to +43.15 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.115 | 7.497 | -7.6% | -1.287 to +0.04927 | no |
| pods started | 5.4 | 3.6 | -33.3% | -2.856 to -0.7444 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 5.6 | -29.1% | -4.563 to -0.03674 | yes: GAIN |
| pod start wait, mean (s) | 1.467 | 1.475 | +0.6% | -0.2797 to +0.2964 | no |
| host CPU busy, the real machine under kind (%) | 25.79 | 25.01 | -3.0% | -1.403 to -0.1527 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.517 | 1.519 | +0.1% | -0.003052 to +0.007052 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.5 | -0.1% | -0.6262 to +0.2365 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.5 | -0.1% | -0.6262 to +0.2365 | no |
| response time (ms), mean | 138.7 | 72.72 | -47.6% | -93.04 to -38.99 | yes: GAIN |
| response time (ms), 95th percentile | 309.3 | 108.6 | -64.9% | -274.9 to -126.5 | yes: GAIN |
| response time (ms), 99th percentile | 506.8 | 146.6 | -71.1% | -504.9 to -215.4 | yes: GAIN |
| time over the response line (% of samples) | 1.859 | 0 | -100.0% | -3.195 to -0.5233 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | -100.0% | -3.431 to -0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.3 | +14.3 (native is 0) | +12.36 to +16.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.1567 | +20.5% | -0.2106 to +0.2639 | no |
| utilisation (used / allocatable) | 0.03557 | 0.03387 | -4.8% | -0.002626 to -0.0007883 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8537 | 0.8128 | -4.8% | -0.06302 to -0.01892 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00541 | +0.00541 (native is 0) | +0.004434 to +0.006386 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.8182 | -4.2% | -0.05682 to -0.01429 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 838.1 | +3.7% | +10.05 to +49.09 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.115 | 7.907 | -2.6% | -0.8736 to +0.4565 | no |
| pods started | 5.4 | 3.3 | -38.9% | -3.337 to -0.8633 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 4.7 | -40.5% | -5.58 to -0.8204 | yes: GAIN |
| pod start wait, mean (s) | 1.467 | 1.41 | -3.9% | -0.3734 to +0.2601 | no |
| host CPU busy, the real machine under kind (%) | 25.79 | 24.83 | -3.7% | -1.571 to -0.3592 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.145e-15 to -9.868e-17 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.518 | +0.1% | -0.003294 to +0.005961 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.4 | -0.2% | -0.7673 to +0.2235 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.4 | -0.2% | -0.7673 to +0.2235 | no |
| response time (ms), mean | 138.7 | 72.84 | -47.5% | -93.13 to -38.65 | yes: GAIN |
| response time (ms), 95th percentile | 309.3 | 108.2 | -65.0% | -276.5 to -125.7 | yes: GAIN |
| response time (ms), 99th percentile | 506.8 | 141.6 | -72.1% | -509 to -221.4 | yes: GAIN |
| time over the response line (% of samples) | 1.859 | 0.01212 | -99.3% | -3.173 to -0.5205 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | -100.0% | -3.431 to -0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.5 (native is 0) | +14.9 to +20.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.21 | +61.5% | -0.2511 to +0.4111 | no |
| utilisation (used / allocatable) | 0.03557 | 0.03386 | -4.8% | -0.00278 to -0.0006464 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8537 | 0.8126 | -4.8% | -0.06672 to -0.01551 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00613 | +0.00613 (native is 0) | +0.004993 to +0.007267 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.8188 | -4.1% | -0.05992 to -0.01005 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 839.7 | +3.9% | -2.595 to +64.91 | no |
| HPA replicas, mean | 8.115 | 7.872 | -3.0% | -0.5729 to +0.08719 | no |
| pods started | 5.4 | 4.3 | -20.4% | -1.887 to -0.3128 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 6.9 | -12.7% | -2.617 to +0.6171 | no |
| pod start wait, mean (s) | 1.467 | 1.615 | +10.1% | -0.02943 to +0.3261 | no |
| host CPU busy, the real machine under kind (%) | 25.79 | 24.8 | -3.9% | -1.875 to -0.1151 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.519 | +0.1% | -0.002729 to +0.006729 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.7 | -0.0% | -0.5937 to +0.5156 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.7 | -0.0% | -0.5937 to +0.5156 | no |
| response time (ms), mean | 138.7 | 74.09 | -46.6% | -91.45 to -37.84 | yes: GAIN |
| response time (ms), 95th percentile | 309.3 | 110 | -64.4% | -274 to -124.7 | yes: GAIN |
| response time (ms), 99th percentile | 506.8 | 165.2 | -67.4% | -474.9 to -208.3 | yes: GAIN |
| time over the response line (% of samples) | 1.859 | 0.01212 | -99.3% | -3.173 to -0.5205 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | -100.0% | -3.431 to -0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16 (native is 0) | +12.16 to +19.84 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.1067 | -17.9% | -0.2453 to +0.1987 | no |
| utilisation (used / allocatable) | 0.03557 | 0.03433 | -3.5% | -0.002084 to -0.0004099 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8537 | 0.8238 | -3.5% | -0.05001 to -0.009837 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0067 | +0.0067 (native is 0) | +0.005372 to +0.008028 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.8305 | -2.7% | -0.04225 to -0.0042 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 826.9 | +2.3% | +0.008567 to +36.8 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.115 | 7.072 | -12.9% | -1.588 to -0.4986 | yes: GAIN |
| pods started | 5.4 | 3.5 | -35.2% | -2.611 to -1.189 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 5.1 | -35.4% | -4.182 to -1.418 | yes: GAIN |
| pod start wait, mean (s) | 1.467 | 1.417 | -3.4% | -0.344 to +0.244 | no |
| host CPU busy, the real machine under kind (%) | 25.79 | 25.16 | -2.5% | -1.25 to -0.01581 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.038e-15 to +3.277e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.518 | +0.1% | -0.002713 to +0.00638 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.5 | -0.1% | -0.6908 to +0.3256 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.5 | -0.1% | -0.6908 to +0.3256 | no |
| response time (ms), mean | 138.7 | 73.72 | -46.9% | -91.92 to -38.11 | yes: GAIN |
| response time (ms), 95th percentile | 309.3 | 109.3 | -64.7% | -274.6 to -125.5 | yes: GAIN |
| response time (ms), 99th percentile | 506.8 | 160.9 | -68.3% | -473.6 to -218.2 | yes: GAIN |
| time over the response line (% of samples) | 1.859 | 0.03636 | -98.0% | -3.143 to -0.5019 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | -100.0% | -3.431 to -0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.4 (native is 0) | +14.68 to +20.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.05333 | -59.0% | -0.272 to +0.1187 | no |
| utilisation (used / allocatable) | 0.03557 | 0.03407 | -4.2% | -0.002579 to -0.0004333 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8537 | 0.8176 | -4.2% | -0.0619 to -0.0104 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01253 | +0.0125 (native is 0) | +0.01038 to +0.01468 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.8301 | -2.8% | -0.04758 to +0.000341 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 829.7 | +2.6% | -2.973 to +45.41 | no |
| HPA replicas, mean | 8.115 | 7.472 | -7.9% | -1.08 to -0.2068 | yes: GAIN |
| pods started | 5.4 | 4.5 | -16.7% | -1.611 to -0.1887 | yes: GAIN |
| pod start wait, total (s) | 7.9 | 6.2 | -21.5% | -3.517 to +0.1174 | no |
| pod start wait, mean (s) | 1.467 | 1.35 | -8.0% | -0.4401 to +0.2068 | no |
| host CPU busy, the real machine under kind (%) | 25.79 | 25.12 | -2.6% | -1.443 to +0.09185 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.576e-16 to +3.8e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.52 | +0.2% | -0.001779 to +0.008113 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.7 | +0.0% | -0.491 to +0.5221 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.7 | +0.0% | -0.491 to +0.5221 | no |
| response time (ms), mean | 138.7 | 73.62 | -46.9% | -92.39 to -37.82 | yes: GAIN |
| response time (ms), 95th percentile | 309.3 | 109.5 | -64.6% | -275.4 to -124.1 | yes: GAIN |
| response time (ms), 99th percentile | 506.8 | 144.6 | -71.5% | -503.5 to -220.8 | yes: GAIN |
| time over the response line (% of samples) | 1.859 | 0.03636 | -98.0% | -3.128 to -0.5173 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | -100.0% | -3.431 to -0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.9 | +19.9 (native is 0) | +17.73 to +22.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.1317 | +1.3% | -0.146 to +0.1493 | no |
| utilisation (used / allocatable) | 0.03557 | 0.03425 | -3.7% | -0.002492 to -0.0001515 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8537 | 0.822 | -3.7% | -0.05981 to -0.003635 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02233 | +0.0223 (native is 0) | +0.01863 to +0.02603 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.8444 | -1.1% | -0.03476 to +0.01598 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 823.4 | +1.8% | -9.183 to +38.95 | no |
| HPA replicas, mean | 8.115 | 8.156 | +0.5% | -0.2326 to +0.314 | no |
| pods started | 5.4 | 4.6 | -14.8% | -1.742 to +0.1417 | no |
| pod start wait, total (s) | 7.9 | 6.1 | -22.8% | -3.641 to +0.04075 | no |
| pod start wait, mean (s) | 1.467 | 1.373 | -6.4% | -0.3398 to +0.1531 | no |
| host CPU busy, the real machine under kind (%) | 25.79 | 25.64 | -0.6% | -0.902 to +0.5921 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.576e-16 to +3.8e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.512 | -0.3% | -0.01192 to +0.003585 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158.1 | -0.4% | -1.499 to +0.2657 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 158.1 | -0.4% | -1.499 to +0.2657 | no |
| response time (ms), mean | 138.7 | 74.47 | -46.3% | -91.03 to -37.48 | yes: GAIN |
| response time (ms), 95th percentile | 309.3 | 112.9 | -63.5% | -269.5 to -123.4 | yes: GAIN |
| response time (ms), 99th percentile | 506.8 | 155.3 | -69.4% | -483.3 to -219.6 | yes: GAIN |
| time over the response line (% of samples) | 1.859 | 0.02424 | -98.7% | -3.159 to -0.5101 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | -100.0% | -3.431 to -0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.3 (native is 0) | +17.25 to +23.35 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.13 | 0.2383 | +83.3% | -0.1576 to +0.3743 | no |
| utilisation (used / allocatable) | 0.03557 | 0.03488 | -1.9% | -0.001453 to +6.826e-05 | no |
| CPU used (cores), mean | 0.8537 | 0.8371 | -1.9% | -0.03488 to +0.001638 | no |
| Omni's own CPU (cores), mean | 0 | 0.06186 | +0.0619 (native is 0) | +0.0513 to +0.07242 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8537 | 0.899 | +5.3% | +0.03241 to +0.05807 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 808.5 | 813.2 | +0.6% | -20.16 to +29.57 | no |
| HPA replicas, mean | 8.115 | 8.444 | +4.1% | -0.123 to +0.7811 | no |
| pods started | 5.4 | 4.9 | -9.3% | -1.343 to +0.343 | no |
| pod start wait, total (s) | 7.9 | 6.9 | -12.7% | -2.784 to +0.7843 | no |
| pod start wait, mean (s) | 1.467 | 1.443 | -1.6% | -0.2998 to +0.2531 | no |
| host CPU busy, the real machine under kind (%) | 25.79 | 27.27 | +5.7% | +0.9454 to +2.006 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.066e-16 to +9.395e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.2% | -0.0036 to +0.009267 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.5 | +0.1% | -0.4392 to +0.8943 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.5 | +0.1% | -0.4392 to +0.8943 | no |
| response time (ms), mean | 73.37 | 72.72 | -0.9% | -1.519 to +0.2131 | no |
| response time (ms), 95th percentile | 108.6 | 108.6 | -0.0% | -2.235 to +2.214 | no |
| response time (ms), 99th percentile | 143.5 | 146.6 | +2.2% | -12.6 to +18.82 | no |
| time over the response line (% of samples) | 0.02424 | 0 | -100.0% | -0.0608 to +0.01232 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 15.6 | 14.3 | -8.3% | -3.869 to +1.269 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.1567 | -15.3% | -0.3317 to +0.275 | no |
| utilisation (used / allocatable) | 0.03417 | 0.03387 | -0.9% | -0.0007141 to +0.0001111 | no |
| CPU used (cores), mean | 0.82 | 0.8128 | -0.9% | -0.01714 to +0.002668 | no |
| Omni's own CPU (cores), mean | 0.00758 | 0.00541 | -28.6% | -0.002652 to -0.001688 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8276 | 0.8182 | -1.1% | -0.01939 to +0.0005836 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.9 | 838.1 | +0.9% | +0.09731 to +14.34 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.497 | 7.907 | +5.5% | +0.0007771 to +0.8195 | yes: power given |
| pods started | 3.6 | 3.3 | -8.3% | -1.772 to +1.172 | no |
| pod start wait, total (s) | 5.6 | 4.7 | -16.1% | -3.69 to +1.89 | no |
| pod start wait, mean (s) | 1.475 | 1.41 | -4.4% | -0.3234 to +0.1934 | no |
| host CPU busy, the real machine under kind (%) | 25.01 | 24.83 | -0.7% | -0.3911 to +0.01642 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.91e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.1% | -0.003284 to +0.007617 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.4 | +0.1% | -0.4151 to +0.7162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.4 | +0.1% | -0.4151 to +0.7162 | no |
| response time (ms), mean | 73.37 | 72.84 | -0.7% | -1.718 to +0.6598 | no |
| response time (ms), 95th percentile | 108.6 | 108.2 | -0.4% | -3.345 to +2.417 | no |
| response time (ms), 99th percentile | 143.5 | 141.6 | -1.3% | -14.14 to +10.28 | no |
| time over the response line (% of samples) | 0.02424 | 0.01212 | -50.0% | -0.06134 to +0.0371 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 15.6 | 17.5 | +12.2% | -0.786 to +4.586 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.21 | +13.5% | -0.2346 to +0.2846 | no |
| utilisation (used / allocatable) | 0.03417 | 0.03386 | -0.9% | -0.0008155 to +0.0002003 | no |
| CPU used (cores), mean | 0.82 | 0.8126 | -0.9% | -0.01957 to +0.004807 | no |
| Omni's own CPU (cores), mean | 0.00758 | 0.00613 | -19.1% | -0.001826 to -0.001074 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8276 | 0.8188 | -1.1% | -0.02116 to +0.003496 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.9 | 839.7 | +1.1% | -8.565 to +26.18 | no |
| HPA replicas, mean | 7.497 | 7.872 | +5.0% | -0.1495 to +0.9012 | no |
| pods started | 3.6 | 4.3 | +19.4% | -0.5639 to +1.964 | no |
| pod start wait, total (s) | 5.6 | 6.9 | +23.2% | -1.156 to +3.756 | no |
| pod start wait, mean (s) | 1.475 | 1.615 | +9.5% | -0.2332 to +0.5132 | no |
| host CPU busy, the real machine under kind (%) | 25.01 | 24.8 | -0.9% | -0.6008 to +0.1669 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.735e-16 to +1.417e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.519 | +0.2% | -0.002954 to +0.008621 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.7 | +0.2% | -0.316 to +1.083 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.7 | +0.2% | -0.316 to +1.083 | no |
| response time (ms), mean | 73.37 | 74.09 | +1.0% | -0.5388 to +1.968 | no |
| response time (ms), 95th percentile | 108.6 | 110 | +1.2% | -1.867 to +4.523 | no |
| response time (ms), 99th percentile | 143.5 | 165.2 | +15.1% | +0.01862 to +43.27 | yes: LOSS |
| time over the response line (% of samples) | 0.02424 | 0.01212 | -50.0% | -0.06134 to +0.0371 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 15.6 | 16 | +2.6% | -1.601 to +2.401 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.1067 | -42.3% | -0.3174 to +0.1608 | no |
| utilisation (used / allocatable) | 0.03417 | 0.03433 | +0.5% | -0.0001899 to +0.0005071 | no |
| CPU used (cores), mean | 0.82 | 0.8238 | +0.5% | -0.004557 to +0.01217 | no |
| Omni's own CPU (cores), mean | 0.00758 | 0.0067 | -11.6% | -0.001055 to -0.0007054 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8276 | 0.8305 | +0.4% | -0.005339 to +0.01119 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.9 | 826.9 | -0.5% | -11.42 to +3.537 | no |
| HPA replicas, mean | 7.497 | 7.072 | -5.7% | -0.7838 to -0.06582 | yes: GAIN |
| pods started | 3.6 | 3.5 | -2.8% | -0.8872 to +0.6872 | no |
| pod start wait, total (s) | 5.6 | 5.1 | -8.9% | -2.054 to +1.054 | no |
| pod start wait, mean (s) | 1.475 | 1.417 | -4.0% | -0.325 to +0.2083 | no |
| host CPU busy, the real machine under kind (%) | 25.01 | 25.16 | +0.6% | -0.1228 to +0.4126 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.494e-16 to +6.718e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.2% | -0.002671 to +0.008004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.5 | +0.2% | -0.3122 to +0.7919 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.5 | +0.2% | -0.3122 to +0.7919 | no |
| response time (ms), mean | 73.37 | 73.72 | +0.5% | -0.5987 to +1.291 | no |
| response time (ms), 95th percentile | 108.6 | 109.3 | +0.6% | -2.011 to +3.277 | no |
| response time (ms), 99th percentile | 143.5 | 160.9 | +12.1% | -2.755 to +37.4 | no |
| time over the response line (% of samples) | 0.02424 | 0.03636 | +50.0% | -0.0638 to +0.08804 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 15.6 | 17.4 | +11.5% | -0.956 to +4.556 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.05333 | -71.2% | -0.4047 to +0.1414 | no |
| utilisation (used / allocatable) | 0.03417 | 0.03407 | -0.3% | -0.0005016 to +0.0003004 | no |
| CPU used (cores), mean | 0.82 | 0.8176 | -0.3% | -0.01204 to +0.007209 | no |
| Omni's own CPU (cores), mean | 0.00758 | 0.01253 | +65.3% | +0.004176 to +0.005724 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8276 | 0.8301 | +0.3% | -0.006932 to +0.012 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.9 | 829.7 | -0.1% | -9.312 to +7.058 | no |
| HPA replicas, mean | 7.497 | 7.472 | -0.3% | -0.8317 to +0.7827 | no |
| pods started | 3.6 | 4.5 | +25.0% | -0.3818 to +2.182 | no |
| pod start wait, total (s) | 5.6 | 6.2 | +10.7% | -1.765 to +2.965 | no |
| pod start wait, mean (s) | 1.475 | 1.35 | -8.5% | -0.5036 to +0.2536 | no |
| host CPU busy, the real machine under kind (%) | 25.01 | 25.12 | +0.4% | -0.2051 to +0.4092 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.52 | +0.3% | -0.001926 to +0.009926 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.7 | +0.3% | -0.1817 to +1.058 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.7 | +0.3% | -0.1817 to +1.058 | no |
| response time (ms), mean | 73.37 | 73.62 | +0.3% | -0.5521 to +1.057 | no |
| response time (ms), 95th percentile | 108.6 | 109.5 | +0.8% | -2.465 to +4.288 | no |
| response time (ms), 99th percentile | 143.5 | 144.6 | +0.8% | -18.98 to +21.19 | no |
| time over the response line (% of samples) | 0.02424 | 0.03636 | +50.0% | -0.0371 to +0.06134 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 15.6 | 19.9 | +27.6% | +1.065 to +7.535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.1317 | -28.8% | -0.2676 to +0.1609 | no |
| utilisation (used / allocatable) | 0.03417 | 0.03425 | +0.2% | -0.0005431 to +0.0007107 | no |
| CPU used (cores), mean | 0.82 | 0.822 | +0.2% | -0.01303 to +0.01706 | no |
| Omni's own CPU (cores), mean | 0.00758 | 0.02233 | +194.6% | +0.01244 to +0.01706 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8276 | 0.8444 | +2.0% | +0.001883 to +0.03164 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.9 | 823.4 | -0.9% | -27.31 to +12.38 | no |
| HPA replicas, mean | 7.497 | 8.156 | +8.8% | +0.03335 to +1.285 | yes: power given |
| pods started | 3.6 | 4.6 | +27.8% | -0.508 to +2.508 | no |
| pod start wait, total (s) | 5.6 | 6.1 | +8.9% | -2.366 to +3.366 | no |
| pod start wait, mean (s) | 1.475 | 1.373 | -6.9% | -0.5123 to +0.309 | no |
| host CPU busy, the real machine under kind (%) | 25.01 | 25.64 | +2.5% | +0.3 to +0.9458 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.512 | -0.2% | -0.01096 to +0.00429 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.1 | -0.1% | -0.9753 to +0.5865 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.1 | -0.1% | -0.9753 to +0.5865 | no |
| response time (ms), mean | 73.37 | 74.47 | +1.5% | -0.02345 to +2.23 | no |
| response time (ms), 95th percentile | 108.6 | 112.9 | +3.9% | +0.2432 to +8.201 | yes: LOSS |
| response time (ms), 99th percentile | 143.5 | 155.3 | +8.2% | -3.38 to +26.9 | no |
| time over the response line (% of samples) | 0.02424 | 0.02424 | +0.0% | -0.04087 to +0.04087 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 15.6 | 20.3 | +30.1% | +1.344 to +8.056 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.2383 | +28.8% | -0.1191 to +0.2258 | no |
| utilisation (used / allocatable) | 0.03417 | 0.03488 | +2.1% | +0.0001478 to +0.001278 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.82 | 0.8371 | +2.1% | +0.003547 to +0.03068 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00758 | 0.06186 | +716.1% | +0.04512 to +0.06344 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8276 | 0.899 | +8.6% | +0.05222 to +0.09057 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 830.9 | 813.2 | -2.1% | -33.64 to -1.646 | yes, down (shown, not judged) |
| HPA replicas, mean | 7.497 | 8.444 | +12.6% | +0.5439 to +1.352 | yes: power given |
| pods started | 3.6 | 4.9 | +36.1% | -0.0509 to +2.651 | no |
| pod start wait, total (s) | 5.6 | 6.9 | +23.2% | -0.9882 to +3.588 | no |
| pod start wait, mean (s) | 1.475 | 1.443 | -2.1% | -0.3411 to +0.2778 | no |
| host CPU busy, the real machine under kind (%) | 25.01 | 27.27 | +9.0% | +1.684 to +2.823 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*