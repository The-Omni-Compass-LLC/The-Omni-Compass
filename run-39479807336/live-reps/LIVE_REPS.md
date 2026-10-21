# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.34 | 11.77 |
| node-hours | 5.039 | 5.034 | 4.753 | 4.931 |
| energy, parked workers still on at idle power (Wh, declared model) | 528.3 | 528.3 | 527.2 | 528.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.3 | 528.3 | 506.4 | 521 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 752.2 | 1080 | 734.5 | 1203 |
| response time (ms), 95th percentile | 2969 | 4119 | 3098 | 4499 |
| response time (ms), 99th percentile | 4041 | 5429 | 4247 | 6036 |
| time over the response line (% of samples) | 28.08 | 38.86 | 28.37 | 43.77 |
| failed requests (%) | 0.04202 | 0.3539 | 0.03845 | 0.4937 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 17.6 | 15.3 | 18.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 51 | 48 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.33 | 46.82 | 27.9 | 54.09 |
| utilisation (used / allocatable) | 0.03664 | 0.03737 | 0.03821 | 0.03901 |
| CPU used (cores), mean | 1.759 | 1.794 | 1.738 | 1.839 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0124 | 0.01277 |
| CPU used with Omni's own (cores), mean | 1.759 | 1.794 | 1.751 | 1.852 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 727.1 | 712.2 | 703.1 | 687.2 |
| HPA replicas, mean | 4.044 | 4.028 | 4.446 | 4.816 |
| pods started | 0.3 | 0.1 | 1.1 | 1.2 |
| pod start wait, total (s) | 0.8 | 0.3 | 1.7 | 2.9 |
| pod start wait, mean (s) | 0.55 | 0.3 | 1.1 | 1.55 |
| host CPU busy, the real machine under kind (%) | 53.99 | 61.44 | 55.94 | 64.88 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 911.9 | 1049 | 932.9 | 1107 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.64 | 11.44 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 7.229 | 0.1333 | 22.47 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 39.4 | 0.6 | 159.5 |
| queue: job turnaround, submitted to done, mean (s) | 222.3 | 328.8 | 236.9 | 380 |
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
| worker nodes in service, mean | 12 | 11.77 | -1.9% | -0.486 to +0.03335 | no |
| node-hours | 5.034 | 4.931 | -2.1% | -0.2185 to +0.01192 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.3 | 528.1 | -0.0% | -3.931 to +3.572 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.3 | 521 | -1.4% | -16.21 to +1.658 | no |
| response time (ms), mean | 1080 | 1203 | +11.4% | -3.137 to +249.4 | no |
| response time (ms), 95th percentile | 4119 | 4499 | +9.2% | -66.88 to +825.7 | no |
| response time (ms), 99th percentile | 5429 | 6036 | +11.2% | -108.9 to +1321 | no |
| time over the response line (% of samples) | 38.86 | 43.77 | +12.6% | -0.9148 to +10.74 | no |
| failed requests (%) | 0.3539 | 0.4937 | +39.5% | -0.1653 to +0.445 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 18.6 | +5.7% | +0.246 to +1.754 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 | +48 (native is 0) | +41.77 to +54.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 46.82 | 54.09 | +15.5% | -41.73 to +56.27 | no |
| utilisation (used / allocatable) | 0.03737 | 0.03901 | +4.4% | -0.003007 to +0.006275 | no |
| CPU used (cores), mean | 1.794 | 1.839 | +2.5% | -0.168 to +0.2585 | no |
| Omni's own CPU (cores), mean | 0 | 0.01277 | +0.0128 (native is 0) | +0.01157 to +0.01397 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.794 | 1.852 | +3.2% | -0.1551 to +0.2711 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 712.2 | 687.2 | -3.5% | -104.7 to +54.69 | no |
| HPA replicas, mean | 4.028 | 4.816 | +19.6% | -0.1575 to +1.734 | no |
| pods started | 0.1 | 1.2 | +1100.0% | +0.3887 to +1.811 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.9 | +866.7% | +0.3837 to +4.816 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.55 | +416.7% | +0.2073 to +2.293 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.44 | 64.88 | +5.6% | +1.835 to +5.057 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1049 | 1107 | +5.5% | +23.21 to +93.19 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.44 | -4.6% | -1.147 to +0.03694 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.229 | 22.47 | +210.8% | -1.002 to +31.49 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 39.4 | 159.5 | +304.8% | -3.194 to +243.4 | no |
| queue: job turnaround, submitted to done, mean (s) | 328.8 | 380 | +15.6% | +9.086 to +93.3 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | -2.318e-15 to +8.967e-16 | EVEN, the same (under one part in a million) |
| node-hours | 5.039 | 5.034 | -0.1% | -0.01873 to +0.008732 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.3 | 528.3 | +0.0% | -2.231 to +2.285 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.3 | 528.3 | +0.0% | -2.231 to +2.285 | no |
| response time (ms), mean | 752.2 | 1080 | +43.6% | +182.4 to +473.1 | yes: LOSS |
| response time (ms), 95th percentile | 2969 | 4119 | +38.7% | +576.4 to +1724 | yes: LOSS |
| response time (ms), 99th percentile | 4041 | 5429 | +34.4% | +554.1 to +2223 | yes: LOSS |
| time over the response line (% of samples) | 28.08 | 38.86 | +38.4% | +7.34 to +14.21 | yes: LOSS |
| failed requests (%) | 0.04202 | 0.3539 | +742.2% | -0.2452 to +0.8689 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 17.6 | +18.1% | +1.871 to +3.529 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.33 | 46.82 | +130.3% | -0.9477 to +53.93 | no |
| utilisation (used / allocatable) | 0.03664 | 0.03737 | +2.0% | -0.001336 to +0.002795 | no |
| CPU used (cores), mean | 1.759 | 1.794 | +2.0% | -0.06414 to +0.1341 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.759 | 1.794 | +2.0% | -0.06414 to +0.1341 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 727.1 | 712.2 | -2.0% | -48.77 to +19.09 | no |
| HPA replicas, mean | 4.044 | 4.028 | -0.4% | -0.2464 to +0.2144 | no |
| pods started | 0.3 | 0.1 | -66.7% | -0.7642 to +0.3642 | no |
| pod start wait, total (s) | 0.8 | 0.3 | -62.5% | -2.017 to +1.017 | no |
| pod start wait, mean (s) | 0.55 | 0.3 | -45.5% | -1.409 to +0.9089 | no |
| host CPU busy, the real machine under kind (%) | 53.99 | 61.44 | +13.8% | +5.539 to +9.351 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 911.9 | 1049 | +15.0% | +84.61 to +189.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 7.229 | +4589.2% | -5.207 to +19.36 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 39.4 | +5528.6% | -25.5 to +102.9 | no |
| queue: job turnaround, submitted to done, mean (s) | 222.3 | 328.8 | +47.9% | +61.03 to +151.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.34 | -5.5% | -1.279 to -0.04342 | yes: GAIN |
| node-hours | 5.039 | 4.753 | -5.7% | -0.5463 to -0.02545 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 528.3 | 527.2 | -0.2% | -3.497 to +1.349 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.3 | 506.4 | -4.1% | -41.46 to -2.271 | yes: GAIN |
| response time (ms), mean | 752.2 | 734.5 | -2.4% | -51.98 to +16.58 | no |
| response time (ms), 95th percentile | 2969 | 3098 | +4.3% | -19.93 to +277.7 | no |
| response time (ms), 99th percentile | 4041 | 4247 | +5.1% | -245.5 to +657.3 | no |
| time over the response line (% of samples) | 28.08 | 28.37 | +1.0% | -0.6442 to +1.219 | no |
| failed requests (%) | 0.04202 | 0.03845 | -8.5% | -0.04937 to +0.04224 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 15.3 | +2.7% | +0.03062 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51 | +51 (native is 0) | +36.12 to +65.88 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.33 | 27.9 | +37.3% | -5.913 to +21.07 | no |
| utilisation (used / allocatable) | 0.03664 | 0.03821 | +4.3% | -0.000982 to +0.004108 | no |
| CPU used (cores), mean | 1.759 | 1.738 | -1.2% | -0.0966 to +0.05566 | no |
| Omni's own CPU (cores), mean | 0 | 0.0124 | +0.0124 (native is 0) | +0.01164 to +0.01316 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.759 | 1.751 | -0.5% | -0.08444 to +0.0683 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 727.1 | 703.1 | -3.3% | -67.62 to +19.76 | no |
| HPA replicas, mean | 4.044 | 4.446 | +9.9% | +0.1521 to +0.6523 | yes: power given |
| pods started | 0.3 | 1.1 | +266.7% | -0.07931 to +1.679 | no |
| pod start wait, total (s) | 0.8 | 1.7 | +112.5% | -0.8667 to +2.667 | no |
| pod start wait, mean (s) | 0.55 | 1.1 | +100.0% | -0.5614 to +1.661 | no |
| host CPU busy, the real machine under kind (%) | 53.99 | 55.94 | +3.6% | +1.354 to +2.545 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 911.9 | 932.9 | +2.3% | +8.624 to +33.38 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.64 | -11.3% | -2.587 to -0.1354 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.1333 | -13.5% | -0.1018 to +0.06018 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | -14.3% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 222.3 | 236.9 | +6.5% | +7.038 to +22.03 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.34 | -5.5% | -1.279 to -0.04342 | yes: GAIN |
| node-hours | 5.034 | 4.753 | -5.6% | -0.5382 to -0.02355 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 528.3 | 527.2 | -0.2% | -3.899 to +1.698 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.3 | 506.4 | -4.1% | -41.39 to -2.395 | yes: GAIN |
| response time (ms), mean | 1080 | 734.5 | -32.0% | -484.2 to -206.7 | yes: GAIN |
| response time (ms), 95th percentile | 4119 | 3098 | -24.8% | -1561 to -481.7 | yes: GAIN |
| response time (ms), 99th percentile | 5429 | 4247 | -21.8% | -1878 to -487.1 | yes: GAIN |
| time over the response line (% of samples) | 38.86 | 28.37 | -27.0% | -13.86 to -7.121 | yes: GAIN |
| failed requests (%) | 0.3539 | 0.03845 | -89.1% | -0.9121 to +0.2812 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 15.3 | -13.1% | -3.058 to -1.542 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51 | +51 (native is 0) | +36.12 to +65.88 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 46.82 | 27.9 | -40.4% | -44.68 to +6.85 | no |
| utilisation (used / allocatable) | 0.03737 | 0.03821 | +2.2% | -0.001914 to +0.003582 | no |
| CPU used (cores), mean | 1.794 | 1.738 | -3.1% | -0.1615 to +0.0506 | no |
| Omni's own CPU (cores), mean | 0 | 0.0124 | +0.0124 (native is 0) | +0.01164 to +0.01316 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.794 | 1.751 | -2.4% | -0.1495 to +0.06332 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 712.2 | 703.1 | -1.3% | -53.84 to +35.66 | no |
| HPA replicas, mean | 4.028 | 4.446 | +10.4% | +0.1522 to +0.6842 | yes: power given |
| pods started | 0.1 | 1.1 | +1000.0% | +0.416 to +1.584 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.7 | +466.7% | +0.5604 to +2.24 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.1 | +266.7% | +0.08073 to +1.519 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.44 | 55.94 | -8.9% | -7.033 to -3.958 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1049 | 932.9 | -11.1% | -160.4 to -71.35 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.64 | -11.3% | -2.587 to -0.1354 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 7.229 | 0.1333 | -98.2% | -19.31 to +5.123 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 39.4 | 0.6 | -98.5% | -103 to +25.36 | no |
| queue: job turnaround, submitted to done, mean (s) | 328.8 | 236.9 | -28.0% | -131.6 to -52.28 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.77 | -1.9% | -0.486 to +0.03335 | no |
| node-hours | 5.039 | 4.931 | -2.1% | -0.2239 to +0.007254 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.3 | 528.1 | -0.0% | -2.665 to +2.36 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.3 | 521 | -1.4% | -15.7 to +1.197 | no |
| response time (ms), mean | 752.2 | 1203 | +59.9% | +290.2 to +611.6 | yes: LOSS |
| response time (ms), 95th percentile | 2969 | 4499 | +51.5% | +1088 to +1972 | yes: LOSS |
| response time (ms), 99th percentile | 4041 | 6036 | +49.4% | +1252 to +2738 | yes: LOSS |
| time over the response line (% of samples) | 28.08 | 43.77 | +55.9% | +8.494 to +22.88 | yes: LOSS |
| failed requests (%) | 0.04202 | 0.4937 | +1075.1% | -0.401 to +1.304 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 | 18.6 | +24.8% | +2.686 to +4.714 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 | +48 (native is 0) | +41.77 to +54.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.33 | 54.09 | +166.1% | -6.43 to +73.95 | no |
| utilisation (used / allocatable) | 0.03664 | 0.03901 | +6.4% | -0.00189 to +0.006616 | no |
| CPU used (cores), mean | 1.759 | 1.839 | +4.6% | -0.1116 to +0.2721 | no |
| Omni's own CPU (cores), mean | 0 | 0.01277 | +0.0128 (native is 0) | +0.01157 to +0.01397 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.759 | 1.852 | +5.3% | -0.09858 to +0.2846 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 727.1 | 687.2 | -5.5% | -119 to +39.32 | no |
| HPA replicas, mean | 4.044 | 4.816 | +19.1% | -0.05405 to +1.598 | no |
| pods started | 0.3 | 1.2 | +300.0% | -0.1366 to +1.937 | no |
| pod start wait, total (s) | 0.8 | 2.9 | +262.5% | -0.9056 to +5.106 | no |
| pod start wait, mean (s) | 0.55 | 1.55 | +181.8% | -0.508 to +2.508 | no |
| host CPU busy, the real machine under kind (%) | 53.99 | 64.88 | +20.2% | +9.115 to +12.67 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 911.9 | 1107 | +21.4% | +145.7 to +244.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.44 | -4.6% | -1.147 to +0.03694 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 22.47 | +14475.7% | +3.061 to +41.57 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 159.5 | +22685.7% | +34.26 to +283.3 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 222.3 | 380 | +70.9% | +121.4 to +193.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*