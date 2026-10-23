# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.516 | 1.513 | 1.513 | 1.512 | 1.515 | 1.516 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.3 | 157.9 | 157.9 | 157.8 | 158.2 | 158.2 | 157.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.3 | 157.9 | 157.9 | 157.8 | 158.2 | 158.2 | 157.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 134.8 | 72.23 | 71.41 | 72.66 | 71.48 | 72.34 | 71.7 | 72.32 |
| response time (ms), 95th percentile | 300.8 | 106.2 | 105.3 | 106 | 103.7 | 104.9 | 104.3 | 107.7 |
| response time (ms), 99th percentile | 494.2 | 146.4 | 148.9 | 158.3 | 140.1 | 142.8 | 142.7 | 145.1 |
| time over the response line (% of samples) | 1.606 | 0.0122 | 0 | 0.04848 | 0.01212 | 0.01212 | 0 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | 16.8 | 17.8 | 14.8 | 15.8 | 19.1 | 20.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 100 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2083 | 0.1067 | 0.1517 | 0.1017 | 0.185 | 0.2967 | 0.24 |
| utilisation (used / allocatable) | 0.0352 | 0.03412 | 0.03376 | 0.03407 | 0.03375 | 0.03395 | 0.03393 | 0.03446 |
| CPU used (cores), mean | 0.8447 | 0.8189 | 0.8102 | 0.8176 | 0.8101 | 0.8147 | 0.8144 | 0.827 |
| Omni's own CPU (cores), mean | 0 | 0.00787 | 0.00553 | 0.00623 | 0.00662 | 0.01238 | 0.02232 | 0.06065 |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8267 | 0.8158 | 0.8238 | 0.8167 | 0.8271 | 0.8367 | 0.8877 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 814.9 | 825 | 816.5 | 821.4 | 820.6 | 819 | 807.7 |
| HPA replicas, mean | 8.141 | 7.762 | 8.035 | 7.599 | 6.959 | 7.131 | 8.278 | 8.39 |
| pods started | 5.5 | 4.3 | 4.9 | 5 | 3.5 | 3.2 | 4.4 | 4.3 |
| pod start wait, total (s) | 9.4 | 5.9 | 6.8 | 7.2 | 5.6 | 4.9 | 7.1 | 6.5 |
| pod start wait, mean (s) | 1.716 | 1.454 | 1.472 | 1.4 | 1.61 | 1.522 | 1.641 | 1.477 |
| host CPU busy, the real machine under kind (%) | 25.61 | 25.11 | 24.79 | 25 | 24.82 | 25.13 | 25.44 | 27 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.515 | 1.516 | +0.1% | -0.0107 to +0.01304 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.3 | -0.1% | -1.333 to +1.094 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.3 | -0.1% | -1.333 to +1.094 | no |
| response time (ms), mean | 134.8 | 72.23 | -46.4% | -88.6 to -36.49 | yes: GAIN |
| response time (ms), 95th percentile | 300.8 | 106.2 | -64.7% | -264 to -125.3 | yes: GAIN |
| response time (ms), 99th percentile | 494.2 | 146.4 | -70.4% | -475.5 to -220 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0.0122 | -99.2% | -2.904 to -0.2842 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.957 to -0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17 (native is 0) | +14.52 to +19.48 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2083 | +11.6% | -0.2324 to +0.2758 | no |
| utilisation (used / allocatable) | 0.0352 | 0.03412 | -3.1% | -0.002161 to +7.084e-06 | no |
| CPU used (cores), mean | 0.8447 | 0.8189 | -3.1% | -0.05185 to +0.00017 | no |
| Omni's own CPU (cores), mean | 0 | 0.00787 | +0.00787 (native is 0) | +0.006626 to +0.009114 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8267 | -2.1% | -0.04323 to +0.007289 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 814.9 | +1.6% | -9.243 to +34.98 | no |
| HPA replicas, mean | 8.141 | 7.762 | -4.7% | -0.9862 to +0.2267 | no |
| pods started | 5.5 | 4.3 | -21.8% | -2.582 to +0.1821 | no |
| pod start wait, total (s) | 9.4 | 5.9 | -37.2% | -5.793 to -1.207 | yes: GAIN |
| pod start wait, mean (s) | 1.716 | 1.454 | -15.3% | -0.6637 to +0.1399 | no |
| host CPU busy, the real machine under kind (%) | 25.61 | 25.11 | -1.9% | -1.202 to +0.2051 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.121e-16 to +2.897e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.513 | -0.1% | -0.01264 to +0.008303 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 157.9 | -0.3% | -1.673 to +0.5734 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 157.9 | -0.3% | -1.673 to +0.5734 | no |
| response time (ms), mean | 134.8 | 71.41 | -47.0% | -89.66 to -37.07 | yes: GAIN |
| response time (ms), 95th percentile | 300.8 | 105.3 | -65.0% | -265.1 to -126 | yes: GAIN |
| response time (ms), 99th percentile | 494.2 | 148.9 | -69.9% | -478.8 to -211.8 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0 | -100.0% | -2.926 to -0.2863 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.957 to -0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.8 | +16.8 (native is 0) | +15.46 to +18.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1067 | -42.9% | -0.3012 to +0.1412 | no |
| utilisation (used / allocatable) | 0.0352 | 0.03376 | -4.1% | -0.002526 to -0.0003448 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8447 | 0.8102 | -4.1% | -0.06062 to -0.008275 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00553 | +0.00553 (native is 0) | +0.004743 to +0.006317 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8158 | -3.4% | -0.05448 to -0.003354 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 825 | +2.9% | +1.775 to +44.22 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.141 | 8.035 | -1.3% | -0.3841 to +0.1716 | no |
| pods started | 5.5 | 4.9 | -10.9% | -1.915 to +0.7146 | no |
| pod start wait, total (s) | 9.4 | 6.8 | -27.7% | -5.445 to +0.2453 | no |
| pod start wait, mean (s) | 1.716 | 1.472 | -14.2% | -0.598 to +0.1094 | no |
| host CPU busy, the real machine under kind (%) | 25.61 | 24.79 | -3.2% | -1.478 to -0.1516 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.515 | 1.513 | -0.2% | -0.01253 to +0.007526 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 157.9 | -0.3% | -1.498 to +0.4796 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 157.9 | -0.3% | -1.498 to +0.4796 | no |
| response time (ms), mean | 134.8 | 72.66 | -46.1% | -87.9 to -36.33 | yes: GAIN |
| response time (ms), 95th percentile | 300.8 | 106 | -64.8% | -264.5 to -125.2 | yes: GAIN |
| response time (ms), 99th percentile | 494.2 | 158.3 | -68.0% | -466.8 to -205 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0.04848 | -97.0% | -2.839 to -0.2765 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.957 to -0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.8 (native is 0) | +15.17 to +20.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1517 | -18.8% | -0.1714 to +0.1014 | no |
| utilisation (used / allocatable) | 0.0352 | 0.03407 | -3.2% | -0.002449 to +0.0001906 | no |
| CPU used (cores), mean | 0.8447 | 0.8176 | -3.2% | -0.05878 to +0.004574 | no |
| Omni's own CPU (cores), mean | 0 | 0.00623 | +0.00623 (native is 0) | +0.005153 to +0.007307 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8238 | -2.5% | -0.05188 to +0.01013 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 816.5 | +1.8% | -9.518 to +38.33 | no |
| HPA replicas, mean | 8.141 | 7.599 | -6.7% | -1.004 to -0.08207 | yes: GAIN |
| pods started | 5.5 | 5 | -9.1% | -1.343 to +0.343 | no |
| pod start wait, total (s) | 9.4 | 7.2 | -23.4% | -4.38 to -0.01991 | yes: GAIN |
| pod start wait, mean (s) | 1.716 | 1.4 | -18.4% | -0.6086 to -0.0228 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 25.61 | 25 | -2.4% | -1.372 to +0.1683 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.512 | -0.2% | -0.01365 to +0.007645 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 157.8 | -0.4% | -1.79 to +0.5257 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 157.8 | -0.4% | -1.79 to +0.5257 | no |
| response time (ms), mean | 134.8 | 71.48 | -47.0% | -89.99 to -36.61 | yes: GAIN |
| response time (ms), 95th percentile | 300.8 | 103.7 | -65.5% | -268.2 to -126.1 | yes: GAIN |
| response time (ms), 99th percentile | 494.2 | 140.1 | -71.7% | -488.5 to -219.7 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0.01212 | -99.2% | -2.898 to -0.2905 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.957 to -0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.8 | +14.8 (native is 0) | +11.59 to +18.01 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1017 | -45.5% | -0.2836 to +0.1136 | no |
| utilisation (used / allocatable) | 0.0352 | 0.03375 | -4.1% | -0.002723 to -0.000161 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8447 | 0.8101 | -4.1% | -0.06536 to -0.003864 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00662 | +0.00662 (native is 0) | +0.005437 to +0.007803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8167 | -3.3% | -0.05774 to +0.001753 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 821.4 | +2.4% | -6.095 to +44.88 | no |
| HPA replicas, mean | 8.141 | 6.959 | -14.5% | -1.808 to -0.5564 | yes: GAIN |
| pods started | 5.5 | 3.5 | -36.4% | -2.954 to -1.046 | yes: GAIN |
| pod start wait, total (s) | 9.4 | 5.6 | -40.4% | -6.273 to -1.327 | yes: GAIN |
| pod start wait, mean (s) | 1.716 | 1.61 | -6.2% | -0.5355 to +0.3231 | no |
| host CPU busy, the real machine under kind (%) | 25.61 | 24.82 | -3.1% | -1.558 to -0.004467 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.88e-16 to +6.104e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.515 | +0.0% | -0.008102 to +0.008435 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | -0.2% | -1.198 to +0.6818 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | -0.2% | -1.198 to +0.6818 | no |
| response time (ms), mean | 134.8 | 72.34 | -46.3% | -88.59 to -36.28 | yes: GAIN |
| response time (ms), 95th percentile | 300.8 | 104.9 | -65.1% | -265.9 to -126.1 | yes: GAIN |
| response time (ms), 99th percentile | 494.2 | 142.8 | -71.1% | -488.2 to -214.6 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0.01212 | -99.2% | -2.909 to -0.2793 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.957 to -0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.8 | +15.8 (native is 0) | +12.16 to +19.44 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.185 | -0.9% | -0.2197 to +0.2163 | no |
| utilisation (used / allocatable) | 0.0352 | 0.03395 | -3.5% | -0.002102 to -0.0003963 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8447 | 0.8147 | -3.5% | -0.05044 to -0.009511 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01238 | +0.0124 (native is 0) | +0.01026 to +0.0145 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8271 | -2.1% | -0.03646 to +0.001268 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 820.6 | +2.3% | +3.737 to +33.38 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.141 | 7.131 | -12.4% | -1.669 to -0.3518 | yes: GAIN |
| pods started | 5.5 | 3.2 | -41.8% | -2.979 to -1.621 | yes: GAIN |
| pod start wait, total (s) | 9.4 | 4.9 | -47.9% | -6.768 to -2.232 | yes: GAIN |
| pod start wait, mean (s) | 1.716 | 1.522 | -11.3% | -0.5541 to +0.1651 | no |
| host CPU busy, the real machine under kind (%) | 25.61 | 25.13 | -1.8% | -1.042 to +0.09641 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | no |
| node-hours | 1.515 | 1.516 | +0.0% | -0.007897 to +0.00923 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | -0.2% | -1.226 to +0.7356 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | -0.2% | -1.226 to +0.7356 | no |
| response time (ms), mean | 134.8 | 71.7 | -46.8% | -89.5 to -36.66 | yes: GAIN |
| response time (ms), 95th percentile | 300.8 | 104.3 | -65.3% | -266.1 to -127 | yes: GAIN |
| response time (ms), 99th percentile | 494.2 | 142.7 | -71.1% | -486.3 to -216.7 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0 | -100.0% | -2.926 to -0.2863 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.957 to -0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | +19.1 (native is 0) | +17.65 to +20.55 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.2967 | +58.9% | -0.1794 to +0.3994 | no |
| utilisation (used / allocatable) | 0.0352 | 0.03393 | -3.6% | -0.002259 to -0.0002638 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8447 | 0.8144 | -3.6% | -0.05421 to -0.00633 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02232 | +0.0223 (native is 0) | +0.01908 to +0.02556 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8367 | -0.9% | -0.02984 to +0.01394 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 819 | +2.1% | -3.97 to +37.96 | no |
| HPA replicas, mean | 8.141 | 8.278 | +1.7% | -0.1998 to +0.4735 | no |
| pods started | 5.5 | 4.4 | -20.0% | -2.29 to +0.08979 | no |
| pod start wait, total (s) | 9.4 | 7.1 | -24.5% | -4.824 to +0.2245 | no |
| pod start wait, mean (s) | 1.716 | 1.641 | -4.4% | -0.4527 to +0.3022 | no |
| host CPU busy, the real machine under kind (%) | 25.61 | 25.44 | -0.7% | -0.7767 to +0.4412 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.511 | -0.3% | -0.01534 to +0.007006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 157.9 | -0.4% | -1.75 to +0.5915 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 157.9 | -0.4% | -1.75 to +0.5915 | no |
| response time (ms), mean | 134.8 | 72.32 | -46.3% | -88.02 to -36.9 | yes: GAIN |
| response time (ms), 95th percentile | 300.8 | 107.7 | -64.2% | -261.8 to -124.5 | yes: GAIN |
| response time (ms), 99th percentile | 494.2 | 145.1 | -70.6% | -479.3 to -218.9 | yes: GAIN |
| time over the response line (% of samples) | 1.606 | 0.01212 | -99.2% | -2.904 to -0.2841 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.6 | 0 | -100.0% | -2.957 to -0.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.4 | +20.4 (native is 0) | +18.34 to +22.46 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.24 | +28.6% | -0.2422 to +0.3488 | no |
| utilisation (used / allocatable) | 0.0352 | 0.03446 | -2.1% | -0.001737 to +0.0002646 | no |
| CPU used (cores), mean | 0.8447 | 0.827 | -2.1% | -0.04169 to +0.00635 | no |
| Omni's own CPU (cores), mean | 0 | 0.06065 | +0.0606 (native is 0) | +0.05088 to +0.07042 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8447 | 0.8877 | +5.1% | +0.02434 to +0.06162 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802 | 807.7 | +0.7% | -18.63 to +29.95 | no |
| HPA replicas, mean | 8.141 | 8.39 | +3.1% | -0.07223 to +0.5695 | no |
| pods started | 5.5 | 4.3 | -21.8% | -2.623 to +0.2226 | no |
| pod start wait, total (s) | 9.4 | 6.5 | -30.9% | -5.71 to -0.0899 | yes: GAIN |
| pod start wait, mean (s) | 1.716 | 1.477 | -14.0% | -0.5845 to +0.1055 | no |
| host CPU busy, the real machine under kind (%) | 25.61 | 27 | +5.5% | +0.9284 to +1.864 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.718e-16 to +4.495e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.513 | -0.2% | -0.0125 to +0.005833 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | -0.3% | -1.296 to +0.4356 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | -0.3% | -1.296 to +0.4356 | no |
| response time (ms), mean | 72.23 | 71.41 | -1.1% | -2.196 to +0.5527 | no |
| response time (ms), 95th percentile | 106.2 | 105.3 | -0.8% | -4.394 to +2.633 | no |
| response time (ms), 99th percentile | 146.4 | 148.9 | +1.7% | -21.16 to +26.07 | no |
| time over the response line (% of samples) | 0.0122 | 0 | -100.0% | -0.03978 to +0.01539 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17 | 16.8 | -1.2% | -3.268 to +2.868 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.1067 | -48.8% | -0.2972 to +0.09386 | no |
| utilisation (used / allocatable) | 0.03412 | 0.03376 | -1.1% | -0.001031 to +0.0003144 | no |
| CPU used (cores), mean | 0.8189 | 0.8102 | -1.1% | -0.02476 to +0.007546 | no |
| Omni's own CPU (cores), mean | 0.00787 | 0.00553 | -29.7% | -0.002881 to -0.001799 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8267 | 0.8158 | -1.3% | -0.02735 to +0.005459 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.9 | 825 | +1.2% | -10.86 to +31.12 | no |
| HPA replicas, mean | 7.762 | 8.035 | +3.5% | -0.2661 to +0.8131 | no |
| pods started | 4.3 | 4.9 | +14.0% | -0.9526 to +2.153 | no |
| pod start wait, total (s) | 5.9 | 6.8 | +15.3% | -0.9299 to +2.73 | no |
| pod start wait, mean (s) | 1.454 | 1.472 | +1.2% | -0.2793 to +0.3145 | no |
| host CPU busy, the real machine under kind (%) | 25.11 | 24.79 | -1.3% | -0.776 to +0.1434 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | no |
| node-hours | 1.516 | 1.513 | -0.2% | -0.008718 to +0.001385 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | -0.2% | -0.8827 to +0.1034 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | -0.2% | -0.8827 to +0.1034 | no |
| response time (ms), mean | 72.23 | 72.66 | +0.6% | -0.4911 to +1.346 | no |
| response time (ms), 95th percentile | 106.2 | 106 | -0.2% | -2.855 to +2.495 | no |
| response time (ms), 99th percentile | 146.4 | 158.3 | +8.1% | -9.835 to +33.56 | no |
| time over the response line (% of samples) | 0.0122 | 0.04848 | +297.6% | -0.04598 to +0.1186 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17 | 17.8 | +4.7% | -2.797 to +4.397 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.1517 | -27.2% | -0.2955 to +0.1822 | no |
| utilisation (used / allocatable) | 0.03412 | 0.03407 | -0.2% | -0.0005125 to +0.0004072 | no |
| CPU used (cores), mean | 0.8189 | 0.8176 | -0.2% | -0.0123 to +0.009773 | no |
| Omni's own CPU (cores), mean | 0.00787 | 0.00623 | -20.8% | -0.002093 to -0.001187 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8267 | 0.8238 | -0.4% | -0.01393 to +0.008128 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.9 | 816.5 | +0.2% | -11.42 to +14.49 | no |
| HPA replicas, mean | 7.762 | 7.599 | -2.1% | -0.8737 to +0.5473 | no |
| pods started | 4.3 | 5 | +16.3% | -0.7326 to +2.133 | no |
| pod start wait, total (s) | 5.9 | 7.2 | +22.0% | -1.377 to +3.977 | no |
| pod start wait, mean (s) | 1.454 | 1.4 | -3.7% | -0.3931 to +0.2855 | no |
| host CPU busy, the real machine under kind (%) | 25.11 | 25 | -0.4% | -0.4531 to +0.2458 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.512 | -0.3% | -0.009264 to +0.0009302 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.8 | -0.3% | -1.036 to +0.01018 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.8 | -0.3% | -1.036 to +0.01018 | no |
| response time (ms), mean | 72.23 | 71.48 | -1.0% | -1.848 to +0.3329 | no |
| response time (ms), 95th percentile | 106.2 | 103.7 | -2.3% | -5.876 to +0.8931 | no |
| response time (ms), 99th percentile | 146.4 | 140.1 | -4.3% | -24.58 to +11.91 | no |
| time over the response line (% of samples) | 0.0122 | 0.01212 | -0.6% | -0.04107 to +0.04092 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17 | 14.8 | -12.9% | -5.136 to +0.7358 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.1017 | -51.2% | -0.2614 to +0.04808 | no |
| utilisation (used / allocatable) | 0.03412 | 0.03375 | -1.1% | -0.0009624 to +0.0002315 | no |
| CPU used (cores), mean | 0.8189 | 0.8101 | -1.1% | -0.0231 to +0.005556 | no |
| Omni's own CPU (cores), mean | 0.00787 | 0.00662 | -15.9% | -0.001535 to -0.0009654 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8267 | 0.8167 | -1.2% | -0.02457 to +0.004524 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.9 | 821.4 | +0.8% | -6.524 to +19.57 | no |
| HPA replicas, mean | 7.762 | 6.959 | -10.3% | -1.258 to -0.3466 | yes: GAIN |
| pods started | 4.3 | 3.5 | -18.6% | -2.14 to +0.5403 | no |
| pod start wait, total (s) | 5.9 | 5.6 | -5.1% | -2.239 to +1.639 | no |
| pod start wait, mean (s) | 1.454 | 1.61 | +10.7% | -0.1129 to +0.4243 | no |
| host CPU busy, the real machine under kind (%) | 25.11 | 24.82 | -1.1% | -0.622 to +0.05637 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.009e-15 to +8.318e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.515 | -0.1% | -0.009051 to +0.007051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.2 | -0.1% | -0.9906 to +0.7133 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.2 | -0.1% | -0.9906 to +0.7133 | no |
| response time (ms), mean | 72.23 | 72.34 | +0.2% | -0.8564 to +1.073 | no |
| response time (ms), 95th percentile | 106.2 | 104.9 | -1.2% | -3.743 to +1.128 | no |
| response time (ms), 99th percentile | 146.4 | 142.8 | -2.5% | -27.43 to +20.17 | no |
| time over the response line (% of samples) | 0.0122 | 0.01212 | -0.6% | -0.04107 to +0.04092 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17 | 15.8 | -7.1% | -4.997 to +2.597 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.185 | -11.2% | -0.2069 to +0.1603 | no |
| utilisation (used / allocatable) | 0.03412 | 0.03395 | -0.5% | -0.0006061 to +0.0002618 | no |
| CPU used (cores), mean | 0.8189 | 0.8147 | -0.5% | -0.01455 to +0.006283 | no |
| Omni's own CPU (cores), mean | 0.00787 | 0.01238 | +57.3% | +0.003589 to +0.005431 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8267 | 0.8271 | +0.0% | -0.01024 to +0.011 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.9 | 820.6 | +0.7% | -3.339 to +14.72 | no |
| HPA replicas, mean | 7.762 | 7.131 | -8.1% | -1.185 to -0.07636 | yes: GAIN |
| pods started | 4.3 | 3.2 | -25.6% | -2.382 to +0.1818 | no |
| pod start wait, total (s) | 5.9 | 4.9 | -16.9% | -2.349 to +0.3488 | no |
| pod start wait, mean (s) | 1.454 | 1.522 | +4.6% | -0.1701 to +0.3048 | no |
| host CPU busy, the real machine under kind (%) | 25.11 | 25.13 | +0.1% | -0.3045 to +0.356 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.924e-16 to +7.924e-16 | no |
| node-hours | 1.516 | 1.516 | -0.0% | -0.008548 to +0.007548 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 158.2 | -0.1% | -0.9859 to +0.7342 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 158.2 | -0.1% | -0.9859 to +0.7342 | no |
| response time (ms), mean | 72.23 | 71.7 | -0.7% | -1.425 to +0.3571 | no |
| response time (ms), 95th percentile | 106.2 | 104.3 | -1.8% | -4.413 to +0.6742 | no |
| response time (ms), 99th percentile | 146.4 | 142.7 | -2.6% | -17.44 to +9.975 | no |
| time over the response line (% of samples) | 0.0122 | 0 | -100.0% | -0.03978 to +0.01539 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17 | 19.1 | +12.4% | -0.6071 to +4.807 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.2967 | +42.4% | -0.1782 to +0.3549 | no |
| utilisation (used / allocatable) | 0.03412 | 0.03393 | -0.5% | -0.000528 to +0.000159 | no |
| CPU used (cores), mean | 0.8189 | 0.8144 | -0.5% | -0.01267 to +0.003815 | no |
| Omni's own CPU (cores), mean | 0.00787 | 0.02232 | +183.6% | +0.01242 to +0.01648 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8267 | 0.8367 | +1.2% | +0.001042 to +0.019 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.9 | 819 | +0.5% | -3.169 to +11.42 | no |
| HPA replicas, mean | 7.762 | 8.278 | +6.7% | +0.07936 to +0.9537 | yes: power given |
| pods started | 4.3 | 4.4 | +2.3% | -0.99 to +1.19 | no |
| pod start wait, total (s) | 5.9 | 7.1 | +20.3% | -0.6714 to +3.071 | no |
| pod start wait, mean (s) | 1.454 | 1.641 | +12.8% | -0.0692 to +0.4425 | no |
| host CPU busy, the real machine under kind (%) | 25.11 | 25.44 | +1.3% | +0.08472 to +0.5765 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.511 | -0.4% | -0.01164 to +0.0009701 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 157.9 | -0.3% | -1.112 to +0.1924 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 157.9 | -0.3% | -1.112 to +0.1924 | no |
| response time (ms), mean | 72.23 | 72.32 | +0.1% | -0.6515 to +0.8149 | no |
| response time (ms), 95th percentile | 106.2 | 107.7 | +1.4% | +0.1359 to +2.855 | yes: LOSS |
| response time (ms), 99th percentile | 146.4 | 145.1 | -0.9% | -24.51 to +21.84 | no |
| time over the response line (% of samples) | 0.0122 | 0.01212 | -0.6% | -0.04107 to +0.04092 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17 | 20.4 | +20.0% | +0.6772 to +6.123 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.24 | +15.2% | -0.1553 to +0.2186 | no |
| utilisation (used / allocatable) | 0.03412 | 0.03446 | +1.0% | +9.258e-05 to +0.0005885 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8189 | 0.827 | +1.0% | +0.002222 to +0.01412 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00787 | 0.06065 | +670.6% | +0.04423 to +0.06133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8267 | 0.8877 | +7.4% | +0.05014 to +0.07177 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 814.9 | 807.7 | -0.9% | -12.51 to -1.907 | yes, down (shown, not judged) |
| HPA replicas, mean | 7.762 | 8.39 | +8.1% | +0.2373 to +1.019 | yes: power given |
| pods started | 4.3 | 4.3 | +0.0% | -1.508 to +1.508 | no |
| pod start wait, total (s) | 5.9 | 6.5 | +10.2% | -2.081 to +3.281 | no |
| pod start wait, mean (s) | 1.454 | 1.477 | +1.5% | -0.336 to +0.3808 | no |
| host CPU busy, the real machine under kind (%) | 25.11 | 27 | +7.5% | +1.443 to +2.346 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*