# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.841 | 5.891 |
| node-hours | 2.515 | 2.51 | 2.033 | 2.471 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 284.6 | 272.8 | 285.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 284.6 | 236.4 | 281.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 317.1 | 591.8 | 288.3 | 587 |
| response time (ms), 95th percentile | 1090 | 1271 | 1166 | 1343 |
| response time (ms), 99th percentile | 1617 | 1764 | 1688 | 1762 |
| time over the response line (% of samples) | 15.06 | 50.32 | 14.59 | 48.66 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 23.3 | 7.2 | 23.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 45.7 | 16.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.98 | 2.44 | 10.44 | 2.208 |
| utilisation (used / allocatable) | 0.05951 | 0.0938 | 0.07455 | 0.09523 |
| CPU used (cores), mean | 1.428 | 2.251 | 1.418 | 2.246 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01679 | 0.00896 |
| CPU used with Omni's own (cores), mean | 1.428 | 2.251 | 1.435 | 2.255 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 303 | 398.5 | 299.8 |
| HPA replicas, mean | 1.955 | 2.034 | 2.078 | 2.021 |
| pods started | 0 | 0.3 | 0.4 | 0.1 |
| pod start wait, total (s) | 0 | 0.8 | 0.5 | 0.2 |
| pod start wait, mean (s) | 0 | 0.55 | 0.35 | 0.2 |
| host CPU busy, the real machine under kind (%) | 40.68 | 71.99 | 41.52 | 71.97 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 775.3 | 1400 | 780.5 | 1396 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.02 | 4.517 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 533.6 | 0.09167 | 536.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 914.7 | 0.4 | 924.3 |
| queue: job turnaround, submitted to done, mean (s) | 83.3 | 855.5 | 87.46 | 841.3 |
| queue: jobs unfinished at the window's end | 0 | 11.1 | 0 | 11.3 |

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
| worker nodes in service, mean | 6 | 5.891 | -1.8% | -0.2118 to -0.005307 | yes: GAIN |
| node-hours | 2.51 | 2.471 | -1.6% | -0.08419 to +0.004249 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 284.6 | 285.1 | +0.2% | -0.238 to +1.281 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.6 | 281.7 | -1.0% | -6.335 to +0.5581 | no |
| response time (ms), mean | 591.8 | 587 | -0.8% | -53.75 to +44.17 | no |
| response time (ms), 95th percentile | 1271 | 1343 | +5.6% | -53.78 to +196.9 | no |
| response time (ms), 99th percentile | 1764 | 1762 | -0.1% | -156 to +151.2 | no |
| time over the response line (% of samples) | 50.32 | 48.66 | -3.3% | -4.098 to +0.7774 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 23.1 | -0.9% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.5 | +16.5 (native is 0) | +11.85 to +21.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.44 | 2.208 | -9.5% | -0.5864 to +0.1231 | no |
| utilisation (used / allocatable) | 0.0938 | 0.09523 | +1.5% | -5.361e-05 to +0.002903 | no |
| CPU used (cores), mean | 2.251 | 2.246 | -0.2% | -0.02017 to +0.009031 | no |
| Omni's own CPU (cores), mean | 0 | 0.00896 | +0.00896 (native is 0) | +0.008399 to +0.009521 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.251 | 2.255 | +0.2% | -0.01101 to +0.01779 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303 | 299.8 | -1.0% | -6.536 to +0.2547 | no |
| HPA replicas, mean | 2.034 | 2.021 | -0.6% | -0.09813 to +0.07248 | no |
| pods started | 0.3 | 0.1 | -66.7% | -0.7642 to +0.3642 | no |
| pod start wait, total (s) | 0.8 | 0.2 | -75.0% | -1.998 to +0.7985 | no |
| pod start wait, mean (s) | 0.55 | 0.2 | -63.6% | -1.362 to +0.6623 | no |
| host CPU busy, the real machine under kind (%) | 71.99 | 71.97 | -0.0% | -0.5153 to +0.4668 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1400 | 1396 | -0.3% | -16.23 to +8.827 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.517 | -24.7% | -1.914 to -1.052 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 533.6 | 536.6 | +0.6% | -42.25 to +48.35 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 914.7 | 924.3 | +1.1% | -30.79 to +50.09 | no |
| queue: job turnaround, submitted to done, mean (s) | 855.5 | 841.3 | -1.7% | -44.71 to +16.35 | no |
| queue: jobs unfinished at the window's end | 11.1 | 11.3 | +1.8% | -0.3642 to +0.7642 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.744e-15 to -6.308e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.51 | -0.2% | -0.01108 to +0.002079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 284.6 | +4.5% | +10.07 to +14.55 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 284.6 | +4.5% | +10.07 to +14.55 | yes: power given |
| response time (ms), mean | 317.1 | 591.8 | +86.6% | +196.3 to +353.1 | yes: LOSS |
| response time (ms), 95th percentile | 1090 | 1271 | +16.7% | -303.6 to +667.1 | no |
| response time (ms), 99th percentile | 1617 | 1764 | +9.1% | -568.4 to +861.5 | no |
| time over the response line (% of samples) | 15.06 | 50.32 | +234.2% | +27.05 to +43.48 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 23.3 | +219.2% | +12.35 to +19.65 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.98 | 2.44 | -77.8% | -11.48 to -5.597 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05951 | 0.0938 | +57.6% | +0.02864 to +0.03994 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.428 | 2.251 | +57.6% | +0.6874 to +0.9586 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.428 | 2.251 | +57.6% | +0.6874 to +0.9586 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 303 | -34.8% | -205.1 to -118.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.034 | +4.0% | -0.05982 to +0.2176 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | -0.4526 to +2.053 | no |
| pod start wait, mean (s) | 0 | 0.55 | +0.55 (native is 0) | -0.2837 to +1.384 | no |
| host CPU busy, the real machine under kind (%) | 40.68 | 71.99 | +77.0% | +28.56 to +34.05 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.3 | 1400 | +80.6% | +549.3 to +700.3 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 533.6 | +1280430.0% | +213.3 to +853.8 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 914.7 | +228574.2% | +456.9 to +1372 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 83.3 | 855.5 | +927.0% | +605.9 to +938.6 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.1 | +11.1 (native is 0) | +3.755 to +18.44 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.841 | -19.3% | -1.96 to -0.357 | yes: GAIN |
| node-hours | 2.515 | 2.033 | -19.1% | -0.8191 to -0.144 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.8 | +0.2% | -0.1946 to +1.249 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 236.4 | -13.2% | -61.4 to -10.45 | yes: GAIN |
| response time (ms), mean | 317.1 | 288.3 | -9.1% | -38.5 to -19.09 | yes: GAIN |
| response time (ms), 95th percentile | 1090 | 1166 | +7.0% | +27.57 to +124.6 | yes: LOSS |
| response time (ms), 99th percentile | 1617 | 1688 | +4.4% | +0.9043 to +140.9 | yes: LOSS |
| time over the response line (% of samples) | 15.06 | 14.59 | -3.1% | -1.134 to +0.2135 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.2 | -1.4% | -0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.7 | +45.7 (native is 0) | +32.87 to +58.53 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.98 | 10.44 | -4.9% | -1.947 to +0.8737 | no |
| utilisation (used / allocatable) | 0.05951 | 0.07455 | +25.3% | +0.004303 to +0.02577 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.428 | 1.418 | -0.7% | -0.03213 to +0.01249 | no |
| Omni's own CPU (cores), mean | 0 | 0.01679 | +0.0168 (native is 0) | +0.01549 to +0.01809 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.428 | 1.435 | +0.5% | -0.01502 to +0.02896 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 398.5 | -14.3% | -111.8 to -20.79 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.078 | +6.3% | -0.0798 to +0.3251 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1952 to +1.195 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.35 (native is 0) | -0.0647 to +0.7647 | no |
| host CPU busy, the real machine under kind (%) | 40.68 | 41.52 | +2.1% | +0.3172 to +1.36 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.3 | 780.5 | +0.7% | +1.329 to +9.071 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.02 | -33.0% | -3.281 to -0.6792 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.09167 | +120.0% | -0.0254 to +0.1254 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.3 | 87.46 | +5.0% | -0.1576 to +8.474 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.841 | -19.3% | -1.96 to -0.357 | yes: GAIN |
| node-hours | 2.51 | 2.033 | -19.0% | -0.8144 to -0.1396 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 284.6 | 272.8 | -4.1% | -14.06 to -9.516 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.6 | 236.4 | -16.9% | -74.78 to -21.69 | yes: GAIN |
| response time (ms), mean | 591.8 | 288.3 | -51.3% | -381.7 to -225.3 | yes: GAIN |
| response time (ms), 95th percentile | 1271 | 1166 | -8.3% | -605.2 to +393.9 | no |
| response time (ms), 99th percentile | 1764 | 1688 | -4.3% | -840.4 to +689 | no |
| time over the response line (% of samples) | 50.32 | 14.59 | -71.0% | -44.33 to -27.13 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 7.2 | -69.1% | -20.01 to -12.19 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.7 | +45.7 (native is 0) | +32.87 to +58.53 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.44 | 10.44 | +327.9% | +4.907 to +11.09 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0938 | 0.07455 | -20.5% | -0.02911 to -0.009399 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.251 | 1.418 | -37.0% | -0.9777 to -0.688 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01679 | +0.0168 (native is 0) | +0.01549 to +0.01809 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.251 | 1.435 | -36.2% | -0.9614 to -0.6707 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303 | 398.5 | +31.5% | +66.28 to +124.8 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.034 | 2.078 | +2.2% | -0.1554 to +0.243 | no |
| pods started | 0.3 | 0.4 | +33.3% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.8 | 0.5 | -37.5% | -1.195 to +0.5953 | no |
| pod start wait, mean (s) | 0.55 | 0.35 | -36.4% | -1.012 to +0.6121 | no |
| host CPU busy, the real machine under kind (%) | 71.99 | 41.52 | -42.3% | -33.36 to -27.58 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1400 | 780.5 | -44.3% | -693.9 to -545.3 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.015 | -66.4% | -4.016 to -3.953 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 533.6 | 0.09167 | -100.0% | -853.7 to -213.2 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 914.7 | 0.4 | -100.0% | -1372 to -456.9 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 855.5 | 87.46 | -89.8% | -932 to -604.2 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.1 | 0 | -100.0% | -18.44 to -3.755 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.891 | -1.8% | -0.2118 to -0.005307 | yes: GAIN |
| node-hours | 2.515 | 2.471 | -1.8% | -0.08918 to +0.0002354 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 285.1 | +4.7% | +10.47 to +15.2 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 281.7 | +3.5% | +5.758 to +13.09 | yes: power given |
| response time (ms), mean | 317.1 | 587 | +85.1% | +217.4 to +322.5 | yes: LOSS |
| response time (ms), 95th percentile | 1090 | 1343 | +23.3% | -149.9 to +656.6 | no |
| response time (ms), 99th percentile | 1617 | 1762 | +8.9% | -519.6 to +808 | no |
| time over the response line (% of samples) | 15.06 | 48.66 | +223.2% | +26.03 to +41.19 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 23.1 | +216.4% | +12.28 to +19.32 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.5 | +16.5 (native is 0) | +11.85 to +21.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.98 | 2.208 | -79.9% | -11.54 to -5.992 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05951 | 0.09523 | +60.0% | +0.0292 to +0.04224 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.428 | 2.246 | +57.2% | +0.6742 to +0.9607 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00896 | +0.00896 (native is 0) | +0.008399 to +0.009521 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.428 | 2.255 | +57.9% | +0.6837 to +0.9691 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 299.8 | -35.5% | -211 to -119 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.021 | +3.4% | -0.08517 to +0.2173 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.68 | 71.97 | +76.9% | +28.41 to +34.15 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 775.3 | 1396 | +80.1% | +540.5 to +701.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.517 | -24.7% | -1.914 to -1.052 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 536.6 | +1287745.8% | +217.3 to +855.8 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 924.3 | +230987.0% | +465.9 to +1382 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 83.3 | 841.3 | +910.0% | +574.9 to +941.1 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.3 | +11.3 (native is 0) | +3.858 to +18.74 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*