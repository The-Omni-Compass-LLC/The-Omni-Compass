# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5 | 5.143 |
| node-hours | 2.513 | 2.514 | 2.095 | 2.156 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 | 271.6 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272 | 240.1 | 245.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 316.4 | 358.1 | 277.6 | 318.3 |
| response time (ms), 95th percentile | 1070 | 1478 | 1095 | 1519 |
| response time (ms), 99th percentile | 1577 | 2206 | 1571 | 2288 |
| time over the response line (% of samples) | 16.26 | 13.22 | 15.37 | 12.76 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8.7 | 8.4 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 46.9 | 35 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.2 | 18.81 | 9.905 | 19.03 |
| utilisation (used / allocatable) | 0.05858 | 0.05861 | 0.0694 | 0.06769 |
| CPU used (cores), mean | 1.406 | 1.407 | 1.382 | 1.399 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.017 | 0.01869 |
| CPU used with Omni's own (cores), mean | 1.406 | 1.407 | 1.399 | 1.418 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.2 | 476.9 | 422.7 | 428.2 |
| HPA replicas, mean | 1.95 | 1.996 | 1.955 | 2.118 |
| pods started | 0.2 | 0.2 | 0 | 0.5 |
| pod start wait, total (s) | 0.4 | 0.3 | 0 | 0.8 |
| pod start wait, mean (s) | 0.2 | 0.15 | 0 | 0.8 |
| host CPU busy, the real machine under kind (%) | 39.75 | 42.29 | 40.82 | 43.41 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 771.5 | 804.2 | 775.5 | 810.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.203 | 4.423 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.8458 | 0.01667 | 1.004 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.6 | 0 | 2.6 |
| queue: job turnaround, submitted to done, mean (s) | 78.3 | 109.7 | 81.36 | 115.9 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.143 | -14.3% | -1.451 to -0.2623 | yes: GAIN |
| node-hours | 2.514 | 2.156 | -14.2% | -0.6061 to -0.1099 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.1 | +0.0% | -0.967 to +1.23 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 245.1 | -9.9% | -45.58 to -8.09 | yes: GAIN |
| response time (ms), mean | 358.1 | 318.3 | -11.1% | -72.1 to -7.496 | yes: GAIN |
| response time (ms), 95th percentile | 1478 | 1519 | +2.8% | -126.9 to +208.5 | no |
| response time (ms), 99th percentile | 2206 | 2288 | +3.7% | -100 to +265 | no |
| time over the response line (% of samples) | 13.22 | 12.76 | -3.5% | -1.734 to +0.7999 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.8 | +1.1% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35 | +35 (native is 0) | +27.73 to +42.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.81 | 19.03 | +1.2% | -3.527 to +3.964 | no |
| utilisation (used / allocatable) | 0.05861 | 0.06769 | +15.5% | +0.00264 to +0.01552 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.407 | 1.399 | -0.6% | -0.04454 to +0.02902 | no |
| Omni's own CPU (cores), mean | 0 | 0.01869 | +0.0187 (native is 0) | +0.01571 to +0.02167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.418 | +0.8% | -0.02566 to +0.04751 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.9 | 428.2 | -10.2% | -84.93 to -12.48 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.996 | 2.118 | +6.1% | -0.09105 to +0.3348 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.3786 to +0.9786 | no |
| pod start wait, total (s) | 0.3 | 0.8 | +166.7% | -0.5796 to +1.58 | no |
| pod start wait, mean (s) | 0.15 | 0.8 | +433.3% | -0.1768 to +1.477 | no |
| host CPU busy, the real machine under kind (%) | 42.29 | 43.41 | +2.6% | +0.7943 to +1.439 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 804.2 | 810.9 | +0.8% | +0.5555 to +12.84 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.423 | -26.3% | -2.593 to -0.5623 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8458 | 1.004 | +18.7% | -0.09449 to +0.4112 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.6 | +62.5% | -0.3488 to +2.349 | no |
| queue: job turnaround, submitted to done, mean (s) | 109.7 | 115.9 | +5.6% | -0.4388 to +12.81 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.167e-15 to +6.345e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.514 | +0.0% | -0.008216 to +0.009882 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 | +0.0% | -0.8354 to +0.9849 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272 | +0.0% | -0.8354 to +0.9849 | no |
| response time (ms), mean | 316.4 | 358.1 | +13.2% | +5.155 to +78.39 | yes: LOSS |
| response time (ms), 95th percentile | 1070 | 1478 | +38.1% | +76.67 to +738.7 | yes: LOSS |
| response time (ms), 99th percentile | 1577 | 2206 | +39.9% | +122.8 to +1136 | yes: LOSS |
| time over the response line (% of samples) | 16.26 | 13.22 | -18.7% | -4.956 to -1.122 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8.7 | +1.2% | -0.99 to +1.19 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.2 | 18.81 | +104.5% | +4.822 to +14.4 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05858 | 0.05861 | +0.1% | -0.001164 to +0.001232 | no |
| CPU used (cores), mean | 1.406 | 1.407 | +0.1% | -0.02793 to +0.02958 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.406 | 1.407 | +0.1% | -0.02793 to +0.02958 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.2 | 476.9 | +0.6% | -7.862 to +13.33 | no |
| HPA replicas, mean | 1.95 | 1.996 | +2.4% | -0.07201 to +0.1647 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.4 | 0.3 | -25.0% | -1.29 to +1.09 | no |
| pod start wait, mean (s) | 0.2 | 0.15 | -25.0% | -0.6449 to +0.5449 | no |
| host CPU busy, the real machine under kind (%) | 39.75 | 42.29 | +6.4% | +1.914 to +3.158 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.5 | 804.2 | +4.2% | +12.34 to +53.06 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.8458 | +1461.5% | +0.6296 to +0.9537 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.6 | +300.0% | +0.4612 to +1.939 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.3 | 109.7 | +40.1% | +12.62 to +50.14 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5 | -16.7% | -1.707 to -0.2934 | yes: GAIN |
| node-hours | 2.513 | 2.095 | -16.7% | -0.7116 to -0.1256 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | -0.1% | -0.8752 to +0.1926 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 240.1 | -11.7% | -54.1 to -9.422 | yes: GAIN |
| response time (ms), mean | 316.4 | 277.6 | -12.3% | -56.59 to -21 | yes: GAIN |
| response time (ms), 95th percentile | 1070 | 1095 | +2.3% | -47.41 to +97.64 | no |
| response time (ms), 99th percentile | 1577 | 1571 | -0.3% | -81.95 to +71.04 | no |
| time over the response line (% of samples) | 16.26 | 15.37 | -5.5% | -2.003 to +0.2083 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8.4 | -2.3% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 | +46.9 (native is 0) | +30.23 to +63.57 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.2 | 9.905 | +7.7% | -1.149 to +2.559 | no |
| utilisation (used / allocatable) | 0.05858 | 0.0694 | +18.5% | +0.003674 to +0.01798 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.406 | 1.382 | -1.7% | -0.06847 to +0.02024 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.01555 to +0.01845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.399 | -0.5% | -0.05155 to +0.03732 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.2 | 422.7 | -10.9% | -85.71 to -17.27 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.95 | 1.955 | +0.2% | -0.09538 to +0.1049 | no |
| pods started | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.4 | 0 | -100.0% | -1.305 to +0.5048 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 39.75 | 40.82 | +2.7% | +0.8638 to +1.272 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.5 | 775.5 | +0.5% | +1.022 to +6.978 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.203 | -29.9% | -2.951 to -0.6426 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.01667 | -69.2% | -0.07834 to +0.003342 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0 | -100.0% | -0.7694 to -0.03062 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 78.3 | 81.36 | +3.9% | +0.488 to +5.629 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5 | -16.7% | -1.707 to -0.2934 | yes: GAIN |
| node-hours | 2.514 | 2.095 | -16.7% | -0.7158 to -0.1231 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.6 | -0.2% | -1.057 to +0.2248 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 240.1 | -11.7% | -54.19 to -9.482 | yes: GAIN |
| response time (ms), mean | 358.1 | 277.6 | -22.5% | -129.9 to -31.21 | yes: GAIN |
| response time (ms), 95th percentile | 1478 | 1095 | -25.9% | -716 to -49.12 | yes: GAIN |
| response time (ms), 99th percentile | 2206 | 1571 | -28.8% | -1146 to -124 | yes: GAIN |
| time over the response line (% of samples) | 13.22 | 15.37 | +16.2% | +0.7655 to +3.518 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.4 | -3.4% | -0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 | +46.9 (native is 0) | +30.23 to +63.57 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.81 | 9.905 | -47.3% | -14.03 to -3.784 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05861 | 0.0694 | +18.4% | +0.002565 to +0.01902 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.407 | 1.382 | -1.8% | -0.05685 to +0.006978 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.01555 to +0.01845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.399 | -0.6% | -0.03965 to +0.02377 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.9 | 422.7 | -11.4% | -98.05 to -10.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.996 | 1.955 | -2.1% | -0.1413 to +0.05815 | no |
| pods started | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.15 | 0 | -100.0% | -0.4893 to +0.1893 | no |
| host CPU busy, the real machine under kind (%) | 42.29 | 40.82 | -3.5% | -2.102 to -0.8336 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 804.2 | 775.5 | -3.6% | -46.8 to -10.6 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.203 | -29.9% | -2.951 to -0.6426 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8458 | 0.01667 | -98.0% | -1.015 to -0.6436 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0 | -100.0% | -2.505 to -0.6952 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 109.7 | 81.36 | -25.8% | -45.55 to -11.09 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.143 | -14.3% | -1.451 to -0.2623 | yes: GAIN |
| node-hours | 2.513 | 2.156 | -14.2% | -0.602 to -0.1124 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.1 | +0.1% | -0.984 to +1.397 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 245.1 | -9.8% | -45.39 to -8.125 | yes: GAIN |
| response time (ms), mean | 316.4 | 318.3 | +0.6% | -27.77 to +31.71 | no |
| response time (ms), 95th percentile | 1070 | 1519 | +41.9% | +125.2 to +771.7 | yes: LOSS |
| response time (ms), 99th percentile | 1577 | 2288 | +45.2% | +190.5 to +1233 | yes: LOSS |
| time over the response line (% of samples) | 16.26 | 12.76 | -21.6% | -6.294 to -0.7191 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8.8 | +2.3% | -1.182 to +1.582 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35 | +35 (native is 0) | +27.73 to +42.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.2 | 19.03 | +106.8% | +1.701 to +17.96 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05858 | 0.06769 | +15.6% | +0.003471 to +0.01476 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.406 | 1.399 | -0.5% | -0.05967 to +0.04579 | no |
| Omni's own CPU (cores), mean | 0 | 0.01869 | +0.0187 (native is 0) | +0.01571 to +0.02167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.418 | +0.8% | -0.04147 to +0.06498 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.2 | 428.2 | -9.7% | -75.4 to -16.54 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.95 | 2.118 | +8.6% | -0.08025 to +0.4167 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.4 | 0.8 | +100.0% | -0.6769 to +1.477 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 39.75 | 43.41 | +9.2% | +2.843 to +4.461 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.5 | 810.9 | +5.1% | +13.41 to +65.39 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.423 | -26.3% | -2.593 to -0.5623 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 1.004 | +1753.8% | +0.5637 to +1.336 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 2.6 | +550.0% | +0.1544 to +4.246 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 78.3 | 115.9 | +48.0% | +13.95 to +61.19 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*