# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.259 | 5.081 |
| node-hours | 2.515 | 2.518 | 2.204 | 2.127 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.1 | 270.8 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.1 | 247.5 | 241.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 254.5 | 236.3 | 233.1 | 207.6 |
| response time (ms), 95th percentile | 845.6 | 852.6 | 917.2 | 884.9 |
| response time (ms), 99th percentile | 1266 | 1306 | 1300 | 1510 |
| time over the response line (% of samples) | 10.02 | 8.746 | 11.59 | 7.409 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.2 | 7.7 | 6.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 174.8 | 130.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.127 | 9.742 | 9.947 | 10.29 |
| utilisation (used / allocatable) | 0.05551 | 0.05515 | 0.06312 | 0.06576 |
| CPU used (cores), mean | 1.332 | 1.324 | 1.327 | 1.332 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04747 | 0.04595 |
| CPU used with Omni's own (cores), mean | 1.332 | 1.324 | 1.375 | 1.377 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.7 | 496.9 | 449.9 | 436.4 |
| HPA replicas, mean | 1.921 | 2.133 | 2.656 | 2.543 |
| pods started | 0 | 0.6 | 1.8 | 1 |
| pod start wait, total (s) | 0 | 1.3 | 4.2 | 1.6 |
| pod start wait, mean (s) | 0 | 0.42 | 1.42 | 0.8 |
| host CPU busy, the real machine under kind (%) | 37.79 | 37.38 | 39.82 | 39.9 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 752.4 | 747.6 | 755.1 | 757.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.561 | 4.219 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.08333 | 0.06667 | 0.04167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | 0.4 | 0.3 |
| queue: job turnaround, submitted to done, mean (s) | 58.11 | 57.02 | 63.45 | 65 |
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
| worker nodes in service, mean | 6 | 5.081 | -15.3% | -1.571 to -0.267 | yes: GAIN |
| node-hours | 2.518 | 2.127 | -15.5% | -0.6662 to -0.1161 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 270.6 | -0.2% | -1.783 to +0.7302 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 241.7 | -10.8% | -50.27 to -8.527 | yes: GAIN |
| response time (ms), mean | 236.3 | 207.6 | -12.2% | -56.51 to -0.9971 | yes: GAIN |
| response time (ms), 95th percentile | 852.6 | 884.9 | +3.8% | -156.2 to +220.8 | no |
| response time (ms), 99th percentile | 1306 | 1510 | +15.7% | -160.4 to +569.6 | no |
| time over the response line (% of samples) | 8.746 | 7.409 | -15.3% | -2.758 to +0.08478 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 6.7 | +8.1% | -0.1952 to +1.195 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.5 | +130 (native is 0) | +92.76 to +168.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.742 | 10.3 | +5.7% | -0.7301 to +1.837 | no |
| utilisation (used / allocatable) | 0.05515 | 0.06576 | +19.2% | +0.003984 to +0.01723 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.324 | 1.332 | +0.6% | -0.021 to +0.03676 | no |
| Omni's own CPU (cores), mean | 0 | 0.04595 | +0.046 (native is 0) | +0.03986 to +0.05204 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.324 | 1.377 | +4.1% | +0.02068 to +0.08697 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.9 | 436.4 | -12.2% | -98.12 to -22.95 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.133 | 2.543 | +19.2% | -0.03533 to +0.8564 | no |
| pods started | 0.6 | 1 | +66.7% | -0.9572 to +1.757 | no |
| pod start wait, total (s) | 1.3 | 1.6 | +23.1% | -2.399 to +2.999 | no |
| pod start wait, mean (s) | 0.42 | 0.8 | +90.5% | -0.1312 to +0.8912 | no |
| host CPU busy, the real machine under kind (%) | 37.38 | 39.9 | +6.7% | +1.467 to +3.572 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.6 | 757.3 | +1.3% | -1.65 to +21.05 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.219 | -29.7% | -3.042 to -0.5208 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.04167 | -50.0% | -0.07308 to -0.01025 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.02 | 65 | +14.0% | -1.31 to +17.28 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.793e-16 to +1.057e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.518 | +0.1% | -0.007991 to +0.01466 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.1 | +0.1% | -1.013 to +1.791 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.1 | +0.1% | -1.013 to +1.791 | no |
| response time (ms), mean | 254.5 | 236.3 | -7.1% | -55.89 to +19.51 | no |
| response time (ms), 95th percentile | 845.6 | 852.6 | +0.8% | -152.2 to +166.2 | no |
| response time (ms), 99th percentile | 1266 | 1306 | +3.2% | -156.8 to +236.7 | no |
| time over the response line (% of samples) | 10.02 | 8.746 | -12.7% | -4.628 to +2.08 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.2 | -10.1% | -1.379 to -0.0214 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.127 | 9.742 | +6.7% | -1.501 to +2.731 | no |
| utilisation (used / allocatable) | 0.05551 | 0.05515 | -0.6% | -0.001463 to +0.000752 | no |
| CPU used (cores), mean | 1.332 | 1.324 | -0.6% | -0.03512 to +0.01805 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.332 | 1.324 | -0.6% | -0.03512 to +0.01805 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.7 | 496.9 | +0.3% | -7.521 to +10.09 | no |
| HPA replicas, mean | 1.921 | 2.133 | +11.0% | -0.112 to +0.5357 | no |
| pods started | 0 | 0.6 | +0.6 (native is 0) | -0.5285 to +1.728 | no |
| pod start wait, total (s) | 0 | 1.3 | +1.3 (native is 0) | -1.179 to +3.779 | no |
| pod start wait, mean (s) | 0 | 0.42 | +0.42 (native is 0) | -0.2143 to +1.054 | no |
| host CPU busy, the real machine under kind (%) | 37.79 | 37.38 | -1.1% | -0.9862 to +0.1813 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.4 | 747.6 | -0.6% | -14.58 to +4.978 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.08333 | +122.2% | +0.01974 to +0.07193 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.11 | 57.02 | -1.9% | -9.947 to +7.772 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.259 | -12.3% | -1.331 to -0.1508 | yes: GAIN |
| node-hours | 2.515 | 2.204 | -12.4% | -0.5546 to -0.06664 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.8 | +0.0% | -1.114 to +1.206 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 247.5 | -8.6% | -41.6 to -4.903 | yes: GAIN |
| response time (ms), mean | 254.5 | 233.1 | -8.4% | -43.82 to +1.023 | no |
| response time (ms), 95th percentile | 845.6 | 917.2 | +8.5% | -65.64 to +208.8 | no |
| response time (ms), 99th percentile | 1266 | 1300 | +2.7% | -229 to +297.3 | no |
| time over the response line (% of samples) | 10.02 | 11.59 | +15.6% | -0.1146 to +3.247 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.7 | +11.6% | -0.07931 to +1.679 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 174.8 | +175 (native is 0) | +113.9 to +235.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.127 | 9.947 | +9.0% | -0.6212 to +2.261 | no |
| utilisation (used / allocatable) | 0.05551 | 0.06312 | +13.7% | +0.001864 to +0.01336 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.332 | 1.327 | -0.4% | -0.03783 to +0.02827 | no |
| Omni's own CPU (cores), mean | 0 | 0.04747 | +0.0475 (native is 0) | +0.0413 to +0.05364 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.332 | 1.375 | +3.2% | +0.006564 to +0.07881 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.7 | 449.9 | -9.2% | -79.77 to -11.67 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.921 | 2.656 | +38.3% | +0.3382 to +1.132 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.4179 to +3.182 | yes: power given |
| pod start wait, total (s) | 0 | 4.2 | +4.2 (native is 0) | +1.058 to +7.342 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.42 | +1.42 (native is 0) | +0.5223 to +2.318 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.79 | 39.82 | +5.4% | +1.61 to +2.467 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.4 | 755.1 | +0.4% | -3.743 to +9.143 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.561 | -24.0% | -2.575 to -0.3027 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.06667 | +77.8% | -0.01537 to +0.07371 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.11 | 63.45 | +9.2% | -0.516 to +11.2 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.259 | -12.3% | -1.331 to -0.1508 | yes: GAIN |
| node-hours | 2.518 | 2.204 | -12.5% | -0.5616 to -0.06626 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 270.8 | -0.1% | -1.342 to +0.6553 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 247.5 | -8.7% | -42.48 to -4.801 | yes: GAIN |
| response time (ms), mean | 236.3 | 233.1 | -1.4% | -28.72 to +22.29 | no |
| response time (ms), 95th percentile | 852.6 | 917.2 | +7.6% | -46.59 to +175.7 | no |
| response time (ms), 99th percentile | 1306 | 1300 | -0.4% | -143.6 to +132 | no |
| time over the response line (% of samples) | 8.746 | 11.59 | +32.5% | +0.09806 to +5.582 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 7.7 | +24.2% | +0.02055 to +2.979 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 174.8 | +175 (native is 0) | +113.9 to +235.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.742 | 9.947 | +2.1% | -1.254 to +1.664 | no |
| utilisation (used / allocatable) | 0.05515 | 0.06312 | +14.4% | +0.002445 to +0.01349 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.324 | 1.327 | +0.3% | -0.03936 to +0.04687 | no |
| Omni's own CPU (cores), mean | 0 | 0.04747 | +0.0475 (native is 0) | +0.0413 to +0.05364 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.324 | 1.375 | +3.9% | +0.004484 to +0.09797 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.9 | 449.9 | -9.5% | -79.99 to -14.03 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.133 | 2.656 | +24.5% | +0.1379 to +0.9081 | yes: power given |
| pods started | 0.6 | 1.8 | +200.0% | +0.1444 to +2.256 | yes: power given |
| pod start wait, total (s) | 1.3 | 4.2 | +223.1% | +0.4118 to +5.388 | yes: LOSS |
| pod start wait, mean (s) | 0.42 | 1.42 | +238.1% | +0.1239 to +1.876 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.38 | 39.82 | +6.5% | +1.804 to +3.078 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.6 | 755.1 | +1.0% | -1.748 to +16.75 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.561 | -24.0% | -2.575 to -0.3027 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.06667 | -20.0% | -0.05437 to +0.02103 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.02 | 63.45 | +11.3% | -3.658 to +16.52 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.081 | -15.3% | -1.571 to -0.267 | yes: GAIN |
| node-hours | 2.515 | 2.127 | -15.4% | -0.6578 to -0.1178 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.6 | -0.1% | -0.8841 to +0.6101 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 241.7 | -10.7% | -49.18 to -8.841 | yes: GAIN |
| response time (ms), mean | 254.5 | 207.6 | -18.4% | -76.31 to -17.58 | yes: GAIN |
| response time (ms), 95th percentile | 845.6 | 884.9 | +4.7% | -54.91 to +133.6 | no |
| response time (ms), 99th percentile | 1266 | 1510 | +19.3% | -22.26 to +511.3 | no |
| time over the response line (% of samples) | 10.02 | 7.409 | -26.1% | -6.867 to +1.646 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.7 | -2.9% | -1.256 to +0.8556 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.5 | +130 (native is 0) | +92.76 to +168.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.127 | 10.3 | +12.8% | -0.3393 to +2.676 | no |
| utilisation (used / allocatable) | 0.05551 | 0.06576 | +18.5% | +0.003134 to +0.01737 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.332 | 1.332 | -0.0% | -0.02931 to +0.028 | no |
| Omni's own CPU (cores), mean | 0 | 0.04595 | +0.046 (native is 0) | +0.03986 to +0.05204 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.332 | 1.377 | +3.4% | +0.01475 to +0.07584 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.7 | 436.4 | -12.0% | -100 to -18.46 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.921 | 2.543 | +32.4% | +0.33 to +0.9149 | yes: power given |
| pods started | 0 | 1 | +1 (native is 0) | +0.174 to +1.826 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | +0.1225 to +3.078 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.8 (native is 0) | +0.1427 to +1.457 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.79 | 39.9 | +5.6% | +1.246 to +2.988 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.4 | 757.3 | +0.7% | +1.199 to +8.601 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.219 | -29.7% | -3.042 to -0.5208 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.04167 | +11.1% | -0.03152 to +0.03985 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.3 | +50.0% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.11 | 65 | +11.9% | +2.023 to +11.77 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*