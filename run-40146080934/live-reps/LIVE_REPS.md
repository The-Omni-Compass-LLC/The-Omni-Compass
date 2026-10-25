# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.598 | 4.377 |
| node-hours | 2.515 | 2.514 | 1.928 | 1.833 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 269.9 | 270.3 | 269.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 269.9 | 226.2 | 218.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 246.1 | 185.7 | 227.3 | 155.7 |
| response time (ms), 95th percentile | 787.6 | 466.1 | 850 | 484 |
| response time (ms), 99th percentile | 1139 | 755.7 | 1300 | 873.3 |
| time over the response line (% of samples) | 11.72 | 6.45 | 11.64 | 6.136 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 5.2 | 5.9 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 45.7 | 29.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.427 | 13.24 | 9.525 | 12.88 |
| utilisation (used / allocatable) | 0.05448 | 0.05357 | 0.07061 | 0.07437 |
| CPU used (cores), mean | 1.308 | 1.286 | 1.28 | 1.271 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01468 | 0.0153 |
| CPU used with Omni's own (cores), mean | 1.308 | 1.286 | 1.295 | 1.286 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.2 | 521.4 | 423.8 | 413.4 |
| HPA replicas, mean | 1.947 | 1.985 | 2.236 | 2.217 |
| pods started | 0.2 | 0.2 | 0.1 | 0.3 |
| pod start wait, total (s) | 0.7 | 0.5 | 0.1 | 0.5 |
| pod start wait, mean (s) | 0.7 | 0.5 | 0.1 | 0.5 |
| host CPU busy, the real machine under kind (%) | 36.88 | 37.7 | 37.77 | 38.49 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 751.9 | 759.3 | 755 | 762.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.71 | 3.558 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.6792 | 0.05 | 0.6917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.2 | 0.3 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 59.45 | 71.02 | 62.82 | 71.5 |
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
| worker nodes in service, mean | 6 | 4.377 | −27.0% | −2.5950 to −0.6506 | yes: GAIN |
| node-hours | 2.514 | 1.833 | −27.1% | −1.0882 to −0.2742 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 269.7 | −0.1% | −1.5181 to +1.1277 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 218.8 | −18.9% | −81.6667 to −20.5820 | yes: GAIN |
| response time (ms), mean | 185.7 | 155.7 | −16.2% | −35.6394 to −24.4655 | yes: GAIN |
| response time (ms), 95th percentile | 466.1 | 484 | +3.8% | −34.0672 to +69.8502 | no |
| response time (ms), 99th percentile | 755.7 | 873.3 | +15.6% | −33.7837 to +269.1639 | no |
| time over the response line (% of samples) | 6.45 | 6.136 | −4.9% | −1.0075 to +0.3805 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.3 | +1.9% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 | +29.300 (native is 0) | +14.1221 to +44.4779 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.24 | 12.88 | −2.7% | −1.5531 to +0.8264 | no |
| utilisation (used / allocatable) | 0.05357 | 0.07437 | +38.8% | +0.0083 to +0.0333 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.286 | 1.271 | −1.1% | −0.0541 to +0.0249 | no |
| Omni's own CPU (cores), mean | 0 | 0.0153 | +0.015 (native is 0) | +0.0127 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.286 | 1.286 | +0.1% | −0.0389 to +0.0403 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.4 | 413.4 | −20.7% | −175.1641 to −40.7087 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.985 | 2.217 | +11.7% | +0.0252 to +0.4393 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.5 | 0.5 | ±0.0% | −0.8921 to +0.8921 | no |
| pod start wait, mean (s) | 0.5 | 0.5 | ±0.0% | −0.8921 to +0.8921 | no |
| host CPU busy, the real machine under kind (%) | 37.7 | 38.49 | +2.1% | +0.1297 to +1.4567 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.3 | 762.9 | +0.5% | +0.3273 to +6.8727 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.558 | −40.7% | −3.8835 to −1.0015 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6792 | 0.6917 | +1.8% | −0.0945 to +0.1195 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 71.02 | 71.5 | +0.7% | −1.1584 to +2.1084 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.514 | −0.0% | −0.0114 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 269.9 | −0.2% | −1.6303 to +0.6407 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 269.9 | −0.2% | −1.6303 to +0.6407 | no |
| response time (ms), mean | 246.1 | 185.7 | −24.5% | −102.9153 to −17.7970 | yes: GAIN |
| response time (ms), 95th percentile | 787.6 | 466.1 | −40.8% | −551.3024 to −91.7266 | yes: GAIN |
| response time (ms), 99th percentile | 1139 | 755.7 | −33.7% | −653.3641 to −113.1225 | yes: GAIN |
| time over the response line (% of samples) | 11.72 | 6.45 | −45.0% | −10.0031 to −0.5457 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 5.2 | −10.3% | −1.7285 to +0.5285 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.427 | 13.24 | +57.1% | +3.1287 to +6.4947 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05448 | 0.05357 | −1.7% | −0.0021 to +0.0003 | no |
| CPU used (cores), mean | 1.308 | 1.286 | −1.7% | −0.0500 to +0.0063 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.308 | 1.286 | −1.7% | −0.0500 to +0.0063 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.2 | 521.4 | +2.4% | −1.0728 to +25.4749 | no |
| HPA replicas, mean | 1.947 | 1.985 | +2.0% | −0.1186 to +0.1946 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.7 | 0.5 | −28.6% | −1.4064 to +1.0064 | no |
| pod start wait, mean (s) | 0.7 | 0.5 | −28.6% | −1.4064 to +1.0064 | no |
| host CPU busy, the real machine under kind (%) | 36.88 | 37.7 | +2.2% | +0.4109 to +1.2206 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.9 | 759.3 | +1.0% | +0.3655 to +14.4345 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.6792 | +1711.1% | +0.5887 to +0.6946 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.2 | +500.0% | +0.6628 to +1.3372 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.45 | 71.02 | +19.5% | +1.6837 to +21.4496 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.598 | −23.4% | −2.2838 to −0.5199 | yes: GAIN |
| node-hours | 2.515 | 1.928 | −23.4% | −0.9556 to −0.2193 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.3 | −0.1% | −0.8278 to +0.5043 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 226.2 | −16.4% | −71.9795 to −16.4856 | yes: GAIN |
| response time (ms), mean | 246.1 | 227.3 | −7.6% | −29.6112 to −7.8462 | yes: GAIN |
| response time (ms), 95th percentile | 787.6 | 850 | +7.9% | +6.1335 to +118.6345 | yes: LOSS |
| response time (ms), 99th percentile | 1139 | 1300 | +14.1% | +29.0068 to +292.8702 | yes: LOSS |
| time over the response line (% of samples) | 11.72 | 11.64 | −0.7% | −0.9144 to +0.7450 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 5.9 | +1.7% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.7 | +45.700 (native is 0) | +28.3906 to +63.0094 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.427 | 9.525 | +13.0% | −0.3707 to +2.5674 | no |
| utilisation (used / allocatable) | 0.05448 | 0.07061 | +29.6% | +0.0054 to +0.0269 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.308 | 1.28 | −2.1% | −0.0808 to +0.0260 | no |
| Omni's own CPU (cores), mean | 0 | 0.01468 | +0.015 (native is 0) | +0.0130 to +0.0164 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.308 | 1.295 | −1.0% | −0.0666 to +0.0412 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.2 | 423.8 | −16.8% | −146.5784 to −24.1310 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.947 | 2.236 | +14.9% | −0.0034 to +0.5820 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.7 | 0.1 | −85.7% | −1.7285 to +0.5285 | no |
| pod start wait, mean (s) | 0.7 | 0.1 | −85.7% | −1.7285 to +0.5285 | no |
| host CPU busy, the real machine under kind (%) | 36.88 | 37.77 | +2.4% | +0.2009 to +1.5726 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.9 | 755 | +0.4% | −0.5388 to +6.7388 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.71 | −38.2% | −3.6918 to −0.8877 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.05 | +33.3% | −0.0076 to +0.0326 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.45 | 62.82 | +5.7% | −1.1666 to +7.8999 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.598 | −23.4% | −2.2838 to −0.5199 | yes: GAIN |
| node-hours | 2.514 | 1.928 | −23.3% | −0.9551 to −0.2174 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 270.3 | +0.1% | −1.0268 to +1.6929 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 226.2 | −16.2% | −71.2493 to −16.2262 | yes: GAIN |
| response time (ms), mean | 185.7 | 227.3 | +22.4% | −1.1110 to +84.3659 | no |
| response time (ms), 95th percentile | 466.1 | 850 | +82.4% | +143.1804 to +624.6166 | yes: LOSS |
| response time (ms), 99th percentile | 755.7 | 1300 | +72.0% | +170.4133 to +917.9503 | yes: LOSS |
| time over the response line (% of samples) | 6.45 | 11.64 | +80.5% | +0.3397 to +10.0397 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.9 | +13.5% | −0.4209 to +1.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.7 | +45.700 (native is 0) | +28.3906 to +63.0094 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.24 | 9.525 | −28.0% | −5.0801 to −2.3466 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05357 | 0.07061 | +31.8% | +0.0056 to +0.0285 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.286 | 1.28 | −0.4% | −0.0590 to +0.0480 | no |
| Omni's own CPU (cores), mean | 0 | 0.01468 | +0.015 (native is 0) | +0.0130 to +0.0164 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.286 | 1.295 | +0.7% | −0.0442 to +0.0626 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.4 | 423.8 | −18.7% | −167.0706 to −28.0408 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.985 | 2.236 | +12.7% | −0.0232 to +0.5257 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.5 | 0.1 | −80.0% | −1.2396 to +0.4396 | no |
| pod start wait, mean (s) | 0.5 | 0.1 | −80.0% | −1.2396 to +0.4396 | no |
| host CPU busy, the real machine under kind (%) | 37.7 | 37.77 | +0.2% | −0.3960 to +0.5380 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.3 | 755 | −0.6% | −9.8923 to +1.2923 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.71 | −38.2% | −3.6918 to −0.8877 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6792 | 0.05 | −92.6% | −0.6807 to −0.5776 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.3 | −75.0% | −1.3060 to −0.4940 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 71.02 | 62.82 | −11.5% | −16.0394 to −0.3606 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.377 | −27.0% | −2.5950 to −0.6506 | yes: GAIN |
| node-hours | 2.515 | 1.833 | −27.1% | −1.0885 to −0.2763 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 269.7 | −0.3% | −1.6825 to +0.3026 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 218.8 | −19.1% | −82.4034 to −20.8348 | yes: GAIN |
| response time (ms), mean | 246.1 | 155.7 | −36.7% | −133.5122 to −47.3050 | yes: GAIN |
| response time (ms), 95th percentile | 787.6 | 484 | −38.5% | −492.5269 to −114.7191 | yes: GAIN |
| response time (ms), 99th percentile | 1139 | 873.3 | −23.3% | −469.8827 to −61.2237 | yes: GAIN |
| time over the response line (% of samples) | 11.72 | 6.136 | −47.7% | −10.5161 to −0.6597 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 5.3 | −8.6% | −1.6802 to +0.6802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 | +29.300 (native is 0) | +14.1221 to +44.4779 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.427 | 12.88 | +52.8% | +2.8307 to +6.0660 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05448 | 0.07437 | +36.5% | +0.0082 to +0.0316 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.308 | 1.271 | −2.8% | −0.0834 to +0.0104 | no |
| Omni's own CPU (cores), mean | 0 | 0.0153 | +0.015 (native is 0) | +0.0127 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.308 | 1.286 | −1.6% | −0.0690 to +0.0266 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.2 | 413.4 | −18.8% | −153.7767 to −37.6941 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.947 | 2.217 | +13.9% | +0.0283 to +0.5122 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.7 | 0.5 | −28.6% | −0.7642 to +0.3642 | no |
| pod start wait, mean (s) | 0.7 | 0.5 | −28.6% | −0.7642 to +0.3642 | no |
| host CPU busy, the real machine under kind (%) | 36.88 | 38.49 | +4.4% | +0.6958 to +2.5221 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.9 | 762.9 | +1.5% | +1.5886 to +20.4114 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.558 | −40.7% | −3.8835 to −1.0015 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.6917 | +1744.4% | +0.5599 to +0.7485 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.2 | +500.0% | +0.6628 to +1.3372 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.45 | 71.5 | +20.3% | +1.6531 to +22.4302 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*