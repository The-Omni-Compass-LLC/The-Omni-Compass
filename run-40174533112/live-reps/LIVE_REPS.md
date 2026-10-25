# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.35 | 7.022 |
| node-hours | 5.038 | 5.032 | 4.336 | 2.938 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 505.1 | 524.2 | 504.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 505.1 | 472.5 | 348.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 508.8 | 120.3 | 479 | 69.74 |
| response time (ms), 95th percentile | 2030 | 163.3 | 2086 | 88.88 |
| response time (ms), 99th percentile | 2955 | 180.3 | 3090 | 119.5 |
| time over the response line (% of samples) | 22.22 | 0 | 21.53 | 0.003591 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 0 | 10.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 68.5 | 27.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 0 | 12.13 | 0.08333 |
| utilisation (used / allocatable) | 0.0327 | 0.006009 | 0.03806 | 0.008818 |
| CPU used (cores), mean | 1.57 | 0.2884 | 1.56 | 0.2485 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01224 | 0.00845 |
| CPU used with Omni's own (cores), mean | 1.57 | 0.2884 | 1.572 | 0.2569 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.7 | 4306 | 728.3 | 3483 |
| HPA replicas, mean | 3.963 | 4.173 | 4.465 | 4.621 |
| pods started | 0.2 | 0.2 | 1.1 | 2.4 |
| pod start wait, total (s) | 0.2 | 0.3 | 1.8 | 3.7 |
| pod start wait, mean (s) | 0.2 | 0.3 | 0.95 | 1.342 |
| host CPU busy, the real machine under kind (%) | 47.84 | 13.36 | 49.19 | 14.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 834.9 | 1508 | 839.6 | 1504 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.405 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 1162 | 0.075 | 1157 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1478 | 0.6 | 1473 |
| queue: job turnaround, submitted to done, mean (s) | 147 | 1162 | 150.5 | 1157 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 7.022 | −41.5% | −5.1795 to −4.7774 | yes: GAIN |
| node-hours | 5.032 | 2.938 | −41.6% | −2.1761 to −2.0119 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 505.1 | 504.3 | −0.2% | −2.4386 to +0.7785 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.1 | 348.1 | −31.1% | −163.2428 to −150.9131 | yes: GAIN |
| response time (ms), mean | 120.3 | 69.74 | −42.0% | −63.1715 to −38.0250 | yes: GAIN |
| response time (ms), 95th percentile | 163.3 | 88.88 | −45.6% | −90.1600 to −58.7620 | yes: GAIN |
| response time (ms), 99th percentile | 180.3 | 119.5 | −33.7% | −73.0888 to −48.5056 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.003591 | +0.004 (native is 0) | −0.0045 to +0.0117 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.8 | +27.800 (native is 0) | +26.0221 to +29.5779 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08333 | +0.083 (native is 0) | −0.0521 to +0.2188 | no |
| utilisation (used / allocatable) | 0.006009 | 0.008818 | +46.7% | +0.0024 to +0.0032 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2884 | 0.2485 | −13.8% | −0.0462 to −0.0337 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00845 | +0.008 (native is 0) | +0.0073 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2884 | 0.2569 | −10.9% | −0.0379 to −0.0251 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4306 | 3483 | −19.1% | −942.2418 to −704.6743 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.173 | 4.621 | +10.7% | +0.1622 to +0.7345 | yes: power given |
| pods started | 0.2 | 2.4 | +1100.0% | +1.1997 to +3.2003 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.7 | +1133.3% | +1.6414 to +5.1586 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.342 | +347.2% | +0.3435 to +1.7398 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 13.36 | 14.38 | +7.6% | +0.7322 to +1.3083 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 1504 | −0.3% | −7.9217 to −0.2783 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1162 | 1157 | −0.4% | −8.1903 to −0.3514 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1478 | 1473 | −0.3% | −8.0858 to −0.3142 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1162 | 1157 | −0.4% | −8.1903 to −0.3514 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.038 | 5.032 | −0.1% | −0.0247 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 505.1 | −3.9% | −23.5107 to −17.1060 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 505.1 | −3.9% | −23.5107 to −17.1060 | yes: GAIN |
| response time (ms), mean | 508.8 | 120.3 | −76.3% | −572.4242 to −204.4285 | yes: GAIN |
| response time (ms), 95th percentile | 2030 | 163.3 | −92.0% | −2778.8891 to −953.7259 | yes: GAIN |
| response time (ms), 99th percentile | 2955 | 180.3 | −93.9% | −4102.9922 to −1445.4940 | yes: GAIN |
| time over the response line (% of samples) | 22.22 | 0 | −100.0% | −33.1804 to −11.2510 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 0 | −100.0% | −15.6939 to −5.3061 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 0 | −100.0% | −15.6051 to −7.9983 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0327 | 0.006009 | −81.6% | −0.0302 to −0.0232 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.57 | 0.2884 | −81.6% | −1.4496 to −1.1130 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.57 | 0.2884 | −81.6% | −1.4496 to −1.1130 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.7 | 4306 | +422.1% | +2993.9296 to +3968.7502 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.963 | 4.173 | +5.3% | +0.0276 to +0.3914 | yes: power given |
| pods started | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| host CPU busy, the real machine under kind (%) | 47.84 | 13.36 | −72.1% | −39.2192 to −29.7453 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 834.9 | 1508 | +80.6% | +615.3400 to +731.2600 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 1162 | +2534127.3% | +1158.4424 to +1164.5076 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1478 | +492400.0% | +1474.2258 to +1480.1742 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 147 | 1162 | +690.0% | +953.6405 to +1075.3512 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.35 | −13.8% | −3.4163 to +0.1148 | no |
| node-hours | 5.038 | 4.336 | −13.9% | −1.4436 to +0.0380 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 524.2 | −0.2% | −3.2362 to +0.8421 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 472.5 | −10.1% | −108.8236 to +2.8628 | no |
| response time (ms), mean | 508.8 | 479 | −5.8% | −46.6770 to −12.7557 | yes: GAIN |
| response time (ms), 95th percentile | 2030 | 2086 | +2.8% | −62.8767 to +175.8897 | no |
| response time (ms), 99th percentile | 2955 | 3090 | +4.6% | −74.7512 to +345.8462 | no |
| time over the response line (% of samples) | 22.22 | 21.53 | −3.1% | −1.4238 to +0.0523 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.4 | −1.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.5 | +68.500 (native is 0) | +34.6585 to +102.3415 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 12.13 | +2.8% | −2.3817 to +3.0317 | no |
| utilisation (used / allocatable) | 0.0327 | 0.03806 | +16.4% | −0.0001 to +0.0108 | no |
| CPU used (cores), mean | 1.57 | 1.56 | −0.6% | −0.0446 to +0.0253 | no |
| Omni's own CPU (cores), mean | 0 | 0.01224 | +0.012 (native is 0) | +0.0114 to +0.0131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.57 | 1.572 | +0.2% | −0.0323 to +0.0375 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.7 | 728.3 | −11.7% | −197.0728 to +4.1977 | no |
| HPA replicas, mean | 3.963 | 4.465 | +12.7% | +0.1975 to +0.8072 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | +0.0436 to +1.7564 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.8 | +800.0% | −0.0242 to +3.2242 | no |
| pod start wait, mean (s) | 0.2 | 0.95 | +375.0% | +0.0498 to +1.4502 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.84 | 49.19 | +2.8% | +0.7666 to +1.9328 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 834.9 | 839.6 | +0.6% | −1.9082 to +11.3082 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.405 | −21.6% | −5.2775 to +0.0880 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.075 | +63.6% | −0.0054 to +0.0637 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 147 | 150.5 | +2.4% | −0.6315 to +7.6649 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.35 | −13.8% | −3.4163 to +0.1148 | no |
| node-hours | 5.032 | 4.336 | −13.8% | −1.4384 to +0.0455 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 505.1 | 524.2 | +3.8% | +15.4139 to +22.8087 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.1 | 472.5 | −6.5% | −91.2459 to +25.9018 | no |
| response time (ms), mean | 120.3 | 479 | +298.1% | +178.3298 to +539.0902 | yes: LOSS |
| response time (ms), 95th percentile | 163.3 | 2086 | +1177.2% | +987.8411 to +2857.7869 | yes: LOSS |
| response time (ms), 99th percentile | 180.3 | 3090 | +1613.9% | +1504.9023 to +4314.6789 | yes: LOSS |
| time over the response line (% of samples) | 0 | 21.53 | +21.530 (native is 0) | +10.9647 to +32.0952 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.4 | +10.400 (native is 0) | +5.2617 to +15.5383 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.5 | +68.500 (native is 0) | +34.6585 to +102.3415 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 12.13 | +12.127 (native is 0) | +8.5196 to +15.7338 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006009 | 0.03806 | +533.5% | +0.0300 to +0.0341 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2884 | 1.56 | +440.9% | +1.0776 to +1.4657 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01224 | +0.012 (native is 0) | +0.0114 to +0.0131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2884 | 1.572 | +445.1% | +1.0895 to +1.4782 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4306 | 728.3 | −83.1% | −4165.2000 to −2990.3550 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.173 | 4.465 | +7.0% | −0.0227 to +0.6085 | no |
| pods started | 0.2 | 1.1 | +450.0% | −0.1900 to +1.9900 | no |
| pod start wait, total (s) | 0.3 | 1.8 | +500.0% | −0.4734 to +3.4734 | no |
| pod start wait, mean (s) | 0.3 | 0.95 | +216.7% | −0.3338 to +1.6338 | no |
| host CPU busy, the real machine under kind (%) | 13.36 | 49.19 | +268.2% | +31.1676 to +40.4963 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 839.6 | −44.3% | −729.4971 to −607.7029 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1162 | 0.075 | −100.0% | −1164.4942 to −1158.3975 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1478 | 0.6 | −100.0% | −1479.9618 to −1473.8382 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1162 | 150.5 | −87.0% | −1073.2492 to −948.7092 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.022 | −41.5% | −5.1795 to −4.7774 | yes: GAIN |
| node-hours | 5.038 | 2.938 | −41.7% | −2.1776 to −2.0230 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 504.3 | −4.0% | −24.7936 to −17.4831 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 348.1 | −33.8% | −182.1659 to −172.6066 | yes: GAIN |
| response time (ms), mean | 508.8 | 69.74 | −86.3% | −635.1853 to −242.8639 | yes: GAIN |
| response time (ms), 95th percentile | 2030 | 88.88 | −95.6% | −2868.0488 to −1013.4882 | yes: GAIN |
| response time (ms), 99th percentile | 2955 | 119.5 | −96.0% | −4173.3159 to −1496.7647 | yes: GAIN |
| time over the response line (% of samples) | 22.22 | 0.003591 | −100.0% | −33.1755 to −11.2487 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 0 | −100.0% | −15.6939 to −5.3061 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.8 | +27.800 (native is 0) | +26.0221 to +29.5779 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 0.08333 | −99.3% | −15.4971 to −7.9395 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0327 | 0.008818 | −73.0% | −0.0270 to −0.0208 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.57 | 0.2485 | −84.2% | −1.4897 to −1.1527 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00845 | +0.008 (native is 0) | +0.0073 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.57 | 0.2569 | −83.6% | −1.4801 to −1.1454 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.7 | 3483 | +322.3% | +2232.5390 to +3083.2247 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.963 | 4.621 | +16.6% | +0.4692 to +0.8465 | yes: power given |
| pods started | 0.2 | 2.4 | +1100.0% | +1.3207 to +3.0793 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.7 | +1750.0% | +1.8395 to +5.1605 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.342 | +570.8% | +0.6816 to +1.6017 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.84 | 14.38 | −69.9% | −37.9921 to −28.9319 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 834.9 | 1504 | +80.2% | +608.8425 to +729.5575 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 1157 | +2524809.1% | +1154.0605 to +1160.3478 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1473 | +491000.0% | +1470.0604 to +1475.9396 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 147 | 1157 | +687.1% | +947.0954 to +1073.3546 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*