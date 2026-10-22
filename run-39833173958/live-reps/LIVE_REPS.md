# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s | omni, a decision every 10 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.513 | 1.516 | 1.518 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.6 | 157.9 | 158.1 | 157.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.6 | 157.9 | 158.1 | 157.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 121.4 | 68.07 | 66.97 | 67.96 | 67.94 |
| response time (ms), 95th percentile | 262 | 99.39 | 98.81 | 99.3 | 99.32 |
| response time (ms), 99th percentile | 447.1 | 132.2 | 135 | 133.6 | 133.8 |
| time over the response line (% of samples) | 1.367 | 0.0241 | 0 | 0 | 0.01212 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.1 | 17.1 | 19.8 | 20 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | nan | 100 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.21 | 0.1833 | 0.2383 | 0.2933 |
| utilisation (used / allocatable) | 0.03335 | 0.03267 | 0.03229 | 0.03256 | 0.0326 |
| CPU used (cores), mean | 0.8003 | 0.7841 | 0.7751 | 0.7814 | 0.7824 |
| Omni's own CPU (cores), mean | 0 | 0.02257 | 0.00787 | 0.03207 | 0.06113 |
| CPU used with Omni's own (cores), mean | 0.8003 | 0.8066 | 0.7829 | 0.8135 | 0.8435 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 861.3 | 868 | 876 | 867.1 | 872.7 |
| HPA replicas, mean | 7.996 | 8.117 | 7.477 | 8.035 | 7.879 |
| pods started | 5.6 | 5.4 | 4.8 | 5 | 4.8 |
| pod start wait, total (s) | 8.7 | 8 | 5.8 | 7.1 | 6 |
| pod start wait, mean (s) | 1.542 | 1.5 | 1.163 | 1.312 | 1.292 |
| host CPU busy, the real machine under kind (%) | 24.75 | 25.06 | 24.29 | 25.26 | 26.24 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.514 | 1.513 | -0.1% | -0.00805 to +0.004716 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.6 | -0.2% | -1.065 to +0.4514 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.6 | -0.2% | -1.065 to +0.4514 | no |
| response time (ms), mean | 121.4 | 68.07 | -44.0% | -81.14 to -25.61 | yes: GAIN |
| response time (ms), 95th percentile | 262 | 99.39 | -62.1% | -235.4 to -89.89 | yes: GAIN |
| response time (ms), 99th percentile | 447.1 | 132.2 | -70.4% | -456.6 to -173.2 | yes: GAIN |
| time over the response line (% of samples) | 1.367 | 0.0241 | -98.2% | -2.509 to -0.1772 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 0 | -100.0% | -3.374 to -0.2256 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.1 | +20.1 (native is 0) | +18.3 to +21.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.21 | +57.5% | -0.1431 to +0.2964 | no |
| utilisation (used / allocatable) | 0.03335 | 0.03267 | -2.0% | -0.00135 to -1.999e-06 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8003 | 0.7841 | -2.0% | -0.03239 to -4.797e-05 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02257 | +0.0226 (native is 0) | +0.01888 to +0.02626 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8003 | 0.8066 | +0.8% | -0.006703 to +0.01941 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 861.3 | 868 | +0.8% | -6.47 to +19.74 | no |
| HPA replicas, mean | 7.996 | 8.117 | +1.5% | -0.2932 to +0.5362 | no |
| pods started | 5.6 | 5.4 | -3.6% | -1.142 to +0.7417 | no |
| pod start wait, total (s) | 8.7 | 8 | -8.0% | -2.887 to +1.487 | no |
| pod start wait, mean (s) | 1.542 | 1.5 | -2.7% | -0.292 to +0.2091 | no |
| host CPU busy, the real machine under kind (%) | 24.75 | 25.06 | +1.3% | -0.0797 to +0.7065 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.363e-16 to +8.692e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | +0.000406 to +0.003261 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.9 | -0.0% | -0.2663 to +0.23 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.9 | -0.0% | -0.2663 to +0.23 | no |
| response time (ms), mean | 121.4 | 66.97 | -44.9% | -82.97 to -25.98 | yes: GAIN |
| response time (ms), 95th percentile | 262 | 98.81 | -62.3% | -236.8 to -89.56 | yes: GAIN |
| response time (ms), 99th percentile | 447.1 | 135 | -69.8% | -456.7 to -167.5 | yes: GAIN |
| time over the response line (% of samples) | 1.367 | 0 | -100.0% | -2.545 to -0.1897 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 0 | -100.0% | -3.374 to -0.2256 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.1 (native is 0) | +13.65 to +20.55 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1833 | +37.5% | -0.1624 to +0.2624 | no |
| utilisation (used / allocatable) | 0.03335 | 0.03229 | -3.2% | -0.002074 to -2.829e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8003 | 0.7751 | -3.2% | -0.04978 to -0.000679 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00787 | +0.00787 (native is 0) | +0.006504 to +0.009236 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8003 | 0.7829 | -2.2% | -0.04099 to +0.006271 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 861.3 | 876 | +1.7% | -9.974 to +39.34 | no |
| HPA replicas, mean | 7.996 | 7.477 | -6.5% | -1.07 to +0.03382 | no |
| pods started | 5.6 | 4.8 | -14.3% | -2.223 to +0.6226 | no |
| pod start wait, total (s) | 8.7 | 5.8 | -33.3% | -5.586 to -0.214 | yes: GAIN |
| pod start wait, mean (s) | 1.542 | 1.163 | -24.6% | -0.8491 to +0.09099 | no |
| host CPU busy, the real machine under kind (%) | 24.75 | 24.29 | -1.9% | -1.125 to +0.2051 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 10 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 10 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.514 | 1.518 | +0.2% | -0.001603 to +0.008603 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 158.1 | +0.1% | -0.2954 to +0.7363 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 158.1 | +0.1% | -0.2954 to +0.7363 | no |
| response time (ms), mean | 121.4 | 67.96 | -44.0% | -81.45 to -25.52 | yes: GAIN |
| response time (ms), 95th percentile | 262 | 99.3 | -62.1% | -235.1 to -90.31 | yes: GAIN |
| response time (ms), 99th percentile | 447.1 | 133.6 | -70.1% | -454.9 to -172.2 | yes: GAIN |
| time over the response line (% of samples) | 1.367 | 0 | -100.0% | -2.545 to -0.1897 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 0 | -100.0% | -3.374 to -0.2256 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 | +19.8 (native is 0) | +18.05 to +21.55 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.2383 | +78.8% | -0.1378 to +0.3478 | no |
| utilisation (used / allocatable) | 0.03335 | 0.03256 | -2.4% | -0.001717 to +0.0001464 | no |
| CPU used (cores), mean | 0.8003 | 0.7814 | -2.4% | -0.04122 to +0.003513 | no |
| Omni's own CPU (cores), mean | 0 | 0.03207 | +0.0321 (native is 0) | +0.02689 to +0.03725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8003 | 0.8135 | +1.7% | -0.004553 to +0.03099 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 861.3 | 867.1 | +0.7% | -18.41 to +30.02 | no |
| HPA replicas, mean | 7.996 | 8.035 | +0.5% | -0.3059 to +0.3857 | no |
| pods started | 5.6 | 5 | -10.7% | -1.566 to +0.3656 | no |
| pod start wait, total (s) | 8.7 | 7.1 | -18.4% | -4.105 to +0.9053 | no |
| pod start wait, mean (s) | 1.542 | 1.312 | -14.9% | -0.7143 to +0.2538 | no |
| host CPU busy, the real machine under kind (%) | 24.75 | 25.26 | +2.1% | +0.08102 to +0.9388 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.511 | -0.2% | -0.01059 to +0.003258 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 157.4 | -0.3% | -1.341 to +0.3173 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 157.4 | -0.3% | -1.341 to +0.3173 | no |
| response time (ms), mean | 121.4 | 67.94 | -44.1% | -80.7 to -26.32 | yes: GAIN |
| response time (ms), 95th percentile | 262 | 99.32 | -62.1% | -234.1 to -91.3 | yes: GAIN |
| response time (ms), 99th percentile | 447.1 | 133.8 | -70.1% | -452.3 to -174.4 | yes: GAIN |
| time over the response line (% of samples) | 1.367 | 0.01212 | -99.1% | -2.525 to -0.1854 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 0 | -100.0% | -3.374 to -0.2256 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20 (native is 0) | +16.23 to +23.77 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.2933 | +120.0% | -0.09749 to +0.4175 | no |
| utilisation (used / allocatable) | 0.03335 | 0.0326 | -2.2% | -0.001579 to +8.508e-05 | no |
| CPU used (cores), mean | 0.8003 | 0.7824 | -2.2% | -0.03789 to +0.002042 | no |
| Omni's own CPU (cores), mean | 0 | 0.06113 | +0.0611 (native is 0) | +0.05074 to +0.07152 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8003 | 0.8435 | +5.4% | +0.02706 to +0.05935 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 861.3 | 872.7 | +1.3% | -18.03 to +40.82 | no |
| HPA replicas, mean | 7.996 | 7.879 | -1.5% | -0.8022 to +0.5699 | no |
| pods started | 5.6 | 4.8 | -14.3% | -1.742 to +0.1417 | no |
| pod start wait, total (s) | 8.7 | 6 | -31.0% | -5.037 to -0.3626 | yes: GAIN |
| pod start wait, mean (s) | 1.542 | 1.292 | -16.2% | -0.6379 to +0.1374 | no |
| host CPU busy, the real machine under kind (%) | 24.75 | 26.24 | +6.0% | +1.148 to +1.845 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 60 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.702e-16 to +1.003e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.516 | +0.2% | -0.00246 to +0.00946 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 157.9 | +0.2% | -0.3178 to +0.8946 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 157.9 | +0.2% | -0.3178 to +0.8946 | no |
| response time (ms), mean | 68.07 | 66.97 | -1.6% | -2.02 to -0.1748 | yes: GAIN |
| response time (ms), 95th percentile | 99.39 | 98.81 | -0.6% | -2.08 to +0.9345 | no |
| response time (ms), 99th percentile | 132.2 | 135 | +2.1% | -5.19 to +10.78 | no |
| time over the response line (% of samples) | 0.0241 | 0 | -100.0% | -0.0786 to +0.03041 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.1 | 17.1 | -14.9% | -6.504 to +0.5043 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.1833 | -12.7% | -0.2271 to +0.1738 | no |
| utilisation (used / allocatable) | 0.03267 | 0.03229 | -1.1% | -0.0009212 to +0.0001703 | no |
| CPU used (cores), mean | 0.7841 | 0.7751 | -1.1% | -0.02211 to +0.004088 | no |
| Omni's own CPU (cores), mean | 0.02257 | 0.00787 | -65.1% | -0.01704 to -0.01236 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8066 | 0.7829 | -2.9% | -0.0379 to -0.009521 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 868 | 876 | +0.9% | -9.63 to +25.73 | no |
| HPA replicas, mean | 8.117 | 7.477 | -7.9% | -1.107 to -0.1728 | yes: GAIN |
| pods started | 5.4 | 4.8 | -11.1% | -1.778 to +0.5778 | no |
| pod start wait, total (s) | 8 | 5.8 | -27.5% | -4.603 to +0.2034 | no |
| pod start wait, mean (s) | 1.5 | 1.163 | -22.5% | -0.8419 to +0.1666 | no |
| host CPU busy, the real machine under kind (%) | 25.06 | 24.29 | -3.1% | -1.141 to -0.4058 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 10 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 10 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.513 | 1.518 | +0.3% | -0.002445 to +0.01278 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 158.1 | +0.3% | -0.2495 to +1.304 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 158.1 | +0.3% | -0.2495 to +1.304 | no |
| response time (ms), mean | 68.07 | 67.96 | -0.2% | -0.6904 to +0.48 | no |
| response time (ms), 95th percentile | 99.39 | 99.3 | -0.1% | -1.53 to +1.358 | no |
| response time (ms), 99th percentile | 132.2 | 133.6 | +1.0% | -8.738 to +11.43 | no |
| time over the response line (% of samples) | 0.0241 | 0 | -100.0% | -0.0786 to +0.03041 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.1 | 19.8 | -1.5% | -2.869 to +2.269 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 100 | +11.1% | -12.62 to +32.62 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.2383 | +13.5% | -0.1069 to +0.1636 | no |
| utilisation (used / allocatable) | 0.03267 | 0.03256 | -0.3% | -0.0006581 to +0.0004385 | no |
| CPU used (cores), mean | 0.7841 | 0.7814 | -0.3% | -0.01579 to +0.01052 | no |
| Omni's own CPU (cores), mean | 0.02257 | 0.03207 | +42.1% | +0.007908 to +0.01109 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8066 | 0.8135 | +0.9% | -0.005845 to +0.01958 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 868 | 867.1 | -0.1% | -19.23 to +17.56 | no |
| HPA replicas, mean | 8.117 | 8.035 | -1.0% | -0.579 to +0.4157 | no |
| pods started | 5.4 | 5 | -7.4% | -1.477 to +0.6769 | no |
| pod start wait, total (s) | 8 | 7.1 | -11.3% | -3.924 to +2.124 | no |
| pod start wait, mean (s) | 1.5 | 1.312 | -12.6% | -0.7505 to +0.3729 | no |
| host CPU busy, the real machine under kind (%) | 25.06 | 25.26 | +0.8% | -0.1054 to +0.4985 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.588e-16 to +1.014e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.511 | -0.1% | -0.007296 to +0.003296 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 157.4 | -0.1% | -0.7514 to +0.3406 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 157.4 | -0.1% | -0.7514 to +0.3406 | no |
| response time (ms), mean | 68.07 | 67.94 | -0.2% | -1.044 to +0.7789 | no |
| response time (ms), 95th percentile | 99.39 | 99.32 | -0.1% | -1.943 to +1.807 | no |
| response time (ms), 99th percentile | 132.2 | 133.8 | +1.2% | -8.694 to +11.82 | no |
| time over the response line (% of samples) | 0.0241 | 0.01212 | -49.7% | -0.07565 to +0.0517 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.1 | 20 | -0.5% | -4.291 to +4.091 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 90 | +0.0% | -33.72 to +33.72 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.2933 | +39.7% | -0.1507 to +0.3174 | no |
| utilisation (used / allocatable) | 0.03267 | 0.0326 | -0.2% | -0.0007672 to +0.0006251 | no |
| CPU used (cores), mean | 0.7841 | 0.7824 | -0.2% | -0.01841 to +0.015 | no |
| Omni's own CPU (cores), mean | 0.02257 | 0.06113 | +170.8% | +0.03181 to +0.04531 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8066 | 0.8435 | +4.6% | +0.01764 to +0.05607 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 868 | 872.7 | +0.5% | -21.24 to +30.75 | no |
| HPA replicas, mean | 8.117 | 7.879 | -2.9% | -0.8133 to +0.3379 | no |
| pods started | 5.4 | 4.8 | -11.1% | -1.825 to +0.6251 | no |
| pod start wait, total (s) | 8 | 6 | -25.0% | -4.237 to +0.2367 | no |
| pod start wait, mean (s) | 1.5 | 1.292 | -13.9% | -0.5166 to +0.09901 | no |
| host CPU busy, the real machine under kind (%) | 25.06 | 26.24 | +4.7% | +0.6083 to +1.758 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*