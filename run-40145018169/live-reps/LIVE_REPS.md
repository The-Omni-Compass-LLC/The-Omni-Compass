# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.615 | 4.669 |
| node-hours | 2.512 | 2.515 | 1.936 | 1.957 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 269.7 | 270.1 | 269.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 269.7 | 226.6 | 228 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 207.2 | 211.1 | 168.8 | 187.5 |
| response time (ms), 95th percentile | 589.7 | 620.1 | 566.5 | 660.1 |
| response time (ms), 99th percentile | 867.6 | 919.2 | 826.1 | 989 |
| time over the response line (% of samples) | 7.877 | 8.627 | 7.405 | 8.617 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 6.3 | 5.9 | 6.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 43.4 | 69.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.538 | 6.657 | 7.323 | 7.217 |
| utilisation (used / allocatable) | 0.05398 | 0.05258 | 0.06967 | 0.06897 |
| CPU used (cores), mean | 1.296 | 1.262 | 1.263 | 1.26 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01479 | 0.01686 |
| CPU used with Omni's own (cores), mean | 1.296 | 1.262 | 1.278 | 1.277 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.1 | 520.4 | 427.6 | 432.6 |
| HPA replicas, mean | 1.983 | 1.941 | 2.15 | 2.211 |
| pods started | 0.1 | 0 | 0 | 0.2 |
| pod start wait, total (s) | 0.2 | 0 | 0 | 0.4 |
| pod start wait, mean (s) | 0.2 | 0 | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 36.74 | 37.38 | 37.37 | 38.18 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 737 | 739.6 | 737.7 | 742.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.607 | 3.82 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1208 | 0.0375 | 0.1083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.7 | 0.3 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 44.7 | 46.36 | 43.27 | 48.85 |
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
| worker nodes in service, mean | 6 | 4.669 | −22.2% | −2.1480 to −0.5134 | yes: GAIN |
| node-hours | 2.515 | 1.957 | −22.2% | −0.9029 to −0.2134 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.8 | +0.0% | −0.6807 to +0.8698 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 228 | −15.5% | −67.6303 to −15.8513 | yes: GAIN |
| response time (ms), mean | 211.1 | 187.5 | −11.2% | −36.1236 to −11.1279 | yes: GAIN |
| response time (ms), 95th percentile | 620.1 | 660.1 | +6.5% | −25.7277 to +105.7317 | no |
| response time (ms), 99th percentile | 919.2 | 989 | +7.6% | −49.3872 to +188.9468 | no |
| time over the response line (% of samples) | 8.627 | 8.617 | −0.1% | −1.4480 to +1.4283 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 6.4 | +1.6% | −0.6113 to +0.8113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 69.3 | +69.300 (native is 0) | +50.9946 to +87.6054 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.657 | 7.217 | +8.4% | −1.2366 to +2.3566 | no |
| utilisation (used / allocatable) | 0.05258 | 0.06897 | +31.2% | +0.0058 to +0.0270 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.262 | 1.26 | −0.2% | −0.0308 to +0.0263 | no |
| Omni's own CPU (cores), mean | 0 | 0.01686 | +0.017 (native is 0) | +0.0147 to +0.0190 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.262 | 1.277 | +1.2% | −0.0151 to +0.0444 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 520.4 | 432.6 | −16.9% | −145.9537 to −29.7747 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.941 | 2.211 | +13.9% | +0.0816 to +0.4578 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 37.38 | 38.18 | +2.1% | +0.4063 to +1.1928 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 739.6 | 742.1 | +0.3% | −0.8593 to +5.8593 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.82 | −36.3% | −3.4103 to −0.9500 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.1083 | −10.3% | −0.0471 to +0.0221 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.5 | −28.6% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 46.36 | 48.85 | +5.4% | −2.1790 to +7.1457 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.512 | 2.515 | +0.1% | −0.0043 to +0.0100 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 269.7 | −0.1% | −0.9639 to +0.6349 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 269.7 | −0.1% | −0.9639 to +0.6349 | no |
| response time (ms), mean | 207.2 | 211.1 | +1.9% | −12.6617 to +20.5468 | no |
| response time (ms), 95th percentile | 589.7 | 620.1 | +5.2% | −56.0750 to +116.8410 | no |
| response time (ms), 99th percentile | 867.6 | 919.2 | +6.0% | −95.5339 to +198.7789 | no |
| time over the response line (% of samples) | 7.877 | 8.627 | +9.5% | −1.3379 to +2.8371 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 6.3 | +16.7% | −0.0204 to +1.8204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.538 | 6.657 | −11.7% | −2.5408 to +0.7775 | no |
| utilisation (used / allocatable) | 0.05398 | 0.05258 | −2.6% | −0.0033 to +0.0005 | no |
| CPU used (cores), mean | 1.296 | 1.262 | −2.6% | −0.0785 to +0.0115 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.296 | 1.262 | −2.6% | −0.0785 to +0.0115 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.1 | 520.4 | +3.2% | −5.1487 to +37.8615 | no |
| HPA replicas, mean | 1.983 | 1.941 | −2.1% | −0.1045 to +0.0202 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 36.74 | 37.38 | +1.7% | +0.2434 to +1.0343 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 737 | 739.6 | +0.4% | −1.0969 to +6.2969 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1208 | +123.1% | +0.0196 to +0.1137 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.7 | +75.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 44.7 | 46.36 | +3.7% | −2.5929 to +5.9179 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.615 | −23.1% | −2.1218 to −0.6490 | yes: GAIN |
| node-hours | 2.512 | 1.936 | −22.9% | −0.8869 to −0.2649 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 270.1 | +0.1% | −0.3714 to +0.8382 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 226.6 | −16.1% | −66.8221 to −19.8237 | yes: GAIN |
| response time (ms), mean | 207.2 | 168.8 | −18.5% | −59.2463 to −17.4047 | yes: GAIN |
| response time (ms), 95th percentile | 589.7 | 566.5 | −3.9% | −129.0397 to +82.7727 | no |
| response time (ms), 99th percentile | 867.6 | 826.1 | −4.8% | −195.8739 to +112.9335 | no |
| time over the response line (% of samples) | 7.877 | 7.405 | −6.0% | −1.5332 to +0.5891 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5.9 | +9.3% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.4 | +43.400 (native is 0) | +37.5966 to +49.2034 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.538 | 7.323 | −2.9% | −1.9078 to +1.4778 | no |
| utilisation (used / allocatable) | 0.05398 | 0.06967 | +29.1% | +0.0064 to +0.0250 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.296 | 1.263 | −2.5% | −0.0613 to −0.0036 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01479 | +0.015 (native is 0) | +0.0129 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.296 | 1.278 | −1.4% | −0.0478 to +0.0125 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.1 | 427.6 | −15.2% | −121.0866 to −31.8115 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.15 | +8.4% | −0.0850 to +0.4189 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 36.74 | 37.37 | +1.7% | +0.2032 to +1.0677 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 737 | 737.7 | +0.1% | −5.0626 to +6.4626 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.607 | −39.9% | −3.5778 to −1.2076 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0375 | −30.8% | −0.0657 to +0.0324 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 44.7 | 43.27 | −3.2% | −5.7998 to +2.9415 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.615 | −23.1% | −2.1218 to −0.6490 | yes: GAIN |
| node-hours | 2.515 | 1.936 | −23.0% | −0.8919 to −0.2656 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 270.1 | +0.1% | −0.3430 to +1.1388 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 226.6 | −16.0% | −66.5333 to −19.7835 | yes: GAIN |
| response time (ms), mean | 211.1 | 168.8 | −20.0% | −60.0873 to −24.4488 | yes: GAIN |
| response time (ms), 95th percentile | 620.1 | 566.5 | −8.6% | −114.2266 to +7.1936 | no |
| response time (ms), 99th percentile | 919.2 | 826.1 | −10.1% | −204.0972 to +17.9118 | no |
| time over the response line (% of samples) | 8.627 | 7.405 | −14.2% | −2.6937 to +0.2505 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 5.9 | −6.3% | −1.0911 to +0.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.4 | +43.400 (native is 0) | +37.5966 to +49.2034 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.657 | 7.323 | +10.0% | −1.3111 to +2.6444 | no |
| utilisation (used / allocatable) | 0.05258 | 0.06967 | +32.5% | +0.0067 to +0.0274 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.262 | 1.263 | +0.1% | −0.0399 to +0.0420 | no |
| Omni's own CPU (cores), mean | 0 | 0.01479 | +0.015 (native is 0) | +0.0129 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.262 | 1.278 | +1.3% | −0.0247 to +0.0563 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 520.4 | 427.6 | −17.8% | −151.7768 to −33.8341 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.941 | 2.15 | +10.8% | −0.0460 to +0.4642 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 37.38 | 37.37 | −0.0% | −0.4721 to +0.4653 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 739.6 | 737.7 | −0.3% | −6.5290 to +2.7290 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.607 | −39.9% | −3.5778 to −1.2076 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.0375 | −69.0% | −0.1299 to −0.0367 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.3 | −57.1% | −0.7694 to −0.0306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 46.36 | 43.27 | −6.7% | −6.7468 to +0.5635 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.669 | −22.2% | −2.1480 to −0.5134 | yes: GAIN |
| node-hours | 2.512 | 1.957 | −22.1% | −0.8972 to −0.2134 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 269.8 | −0.0% | −0.8858 to +0.7460 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 228 | −15.5% | −68.0211 to −15.7896 | yes: GAIN |
| response time (ms), mean | 207.2 | 187.5 | −9.5% | −27.6667 to −11.6998 | yes: GAIN |
| response time (ms), 95th percentile | 589.7 | 660.1 | +11.9% | +36.9208 to +103.8492 | yes: LOSS |
| response time (ms), 99th percentile | 867.6 | 989 | +14.0% | +32.2631 to +210.5415 | yes: LOSS |
| time over the response line (% of samples) | 7.877 | 8.617 | +9.4% | −0.2195 to +1.6990 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 6.4 | +18.5% | −0.1184 to +2.1184 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 69.3 | +69.300 (native is 0) | +50.9946 to +87.6054 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.538 | 7.217 | −4.3% | −2.1294 to +1.4861 | no |
| utilisation (used / allocatable) | 0.05398 | 0.06897 | +27.8% | +0.0057 to +0.0243 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.296 | 1.26 | −2.8% | −0.0891 to +0.0177 | no |
| Omni's own CPU (cores), mean | 0 | 0.01686 | +0.017 (native is 0) | +0.0147 to +0.0190 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.296 | 1.277 | −1.5% | −0.0737 to +0.0360 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.1 | 432.6 | −14.2% | −114.2431 to −28.7724 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.211 | +11.5% | +0.0268 to +0.4283 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.8556 to +1.2556 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 36.74 | 38.18 | +3.9% | +1.0500 to +1.8269 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 737 | 742.1 | +0.7% | +0.2433 to +9.9567 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.82 | −36.3% | −3.4103 to −0.9500 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1083 | +100.0% | +0.0119 to +0.0964 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 44.7 | 48.85 | +9.3% | +0.1917 to +8.0999 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*