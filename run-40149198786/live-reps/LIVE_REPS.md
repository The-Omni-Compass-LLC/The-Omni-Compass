# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.889 | 5.977 |
| node-hours | 2.516 | 2.511 | 2.056 | 2.504 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 283.9 | 271.6 | 284.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 283.9 | 236.6 | 283.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 272.4 | 555.6 | 237.9 | 551.6 |
| response time (ms), 95th percentile | 878 | 1247 | 899.9 | 1216 |
| response time (ms), 99th percentile | 1260 | 1675 | 1329 | 1693 |
| time over the response line (% of samples) | 14.1 | 46.63 | 13.82 | 47.18 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 22.6 | 7.2 | 22.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.2 | 20.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.367 | 2.153 | 8.867 | 2.278 |
| utilisation (used / allocatable) | 0.05642 | 0.09149 | 0.06867 | 0.09227 |
| CPU used (cores), mean | 1.354 | 2.196 | 1.323 | 2.207 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0144 | 0.00854 |
| CPU used with Omni's own (cores), mean | 1.354 | 2.196 | 1.337 | 2.215 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.4 | 311.4 | 426.8 | 308.6 |
| HPA replicas, mean | 1.937 | 2.091 | 2.274 | 2.51 |
| pods started | 0 | 0.2 | 0.4 | 0.1 |
| pod start wait, total (s) | 0 | 0.4 | 1.1 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 | 1.1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 38.27 | 69.62 | 38.64 | 70.19 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 758 | 1361 | 758 | 1368 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.167 | 5.756 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 482.8 | 0.02083 | 510.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 886.5 | 0 | 904.2 |
| queue: job turnaround, submitted to done, mean (s) | 65.53 | 798.3 | 64.82 | 807.8 |
| queue: jobs unfinished at the window's end | 0 | 10.7 | 0 | 10.6 |

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
| worker nodes in service, mean | 6 | 5.977 | −0.4% | −0.0566 to +0.0116 | no |
| node-hours | 2.511 | 2.504 | −0.3% | −0.0265 to +0.0127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 283.9 | 284.3 | +0.2% | −0.5035 to +1.3671 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 283.9 | 283.6 | −0.1% | −2.1179 to +1.5690 | no |
| response time (ms), mean | 555.6 | 551.6 | −0.7% | −29.9603 to +22.0170 | no |
| response time (ms), 95th percentile | 1247 | 1216 | −2.5% | −110.2518 to +48.3008 | no |
| response time (ms), 99th percentile | 1675 | 1693 | +1.1% | −96.4746 to +133.1358 | no |
| time over the response line (% of samples) | 46.63 | 47.18 | +1.2% | −2.2032 to +3.3028 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.6 | 22.5 | −0.4% | −0.7263 to +0.5263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.8 | +20.800 (native is 0) | +14.9034 to +26.6966 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.153 | 2.278 | +5.8% | −0.2055 to +0.4555 | no |
| utilisation (used / allocatable) | 0.09149 | 0.09227 | +0.8% | −0.0008 to +0.0024 | no |
| CPU used (cores), mean | 2.196 | 2.207 | +0.5% | −0.0316 to +0.0537 | no |
| Omni's own CPU (cores), mean | 0 | 0.00854 | +0.009 (native is 0) | +0.0072 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.196 | 2.215 | +0.9% | −0.0226 to +0.0617 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 311.4 | 308.6 | −0.9% | −8.6074 to +3.0166 | no |
| HPA replicas, mean | 2.091 | 2.51 | +20.0% | +0.1284 to +0.7094 | yes: power given |
| pods started | 0.2 | 0.1 | −50.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.4 | 0.2 | −50.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 69.62 | 70.19 | +0.8% | −0.5709 to +1.7082 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1361 | 1368 | +0.5% | −17.1294 to +30.5294 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.756 | −4.1% | −0.7297 to +0.2415 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 482.8 | 510.3 | +5.7% | −30.9318 to +86.0250 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 886.5 | 904.2 | +2.0% | −40.4656 to +75.7231 | no |
| queue: job turnaround, submitted to done, mean (s) | 798.3 | 807.8 | +1.2% | −21.7029 to +40.7029 | no |
| queue: jobs unfinished at the window's end | 10.7 | 10.6 | −0.9% | −1.1366 to +0.9366 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.511 | −0.2% | −0.0153 to +0.0053 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 283.9 | +4.6% | +10.6584 to +14.3327 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 283.9 | +4.6% | +10.6584 to +14.3327 | yes: power given |
| response time (ms), mean | 272.4 | 555.6 | +103.9% | +205.5837 to +360.7363 | yes: LOSS |
| response time (ms), 95th percentile | 878 | 1247 | +42.0% | +134.6658 to +602.6642 | yes: LOSS |
| response time (ms), 99th percentile | 1260 | 1675 | +32.9% | +10.6107 to +819.3897 | yes: LOSS |
| time over the response line (% of samples) | 14.1 | 46.63 | +230.7% | +22.1374 to +42.9175 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 22.6 | +232.4% | +12.6046 to +18.9954 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.367 | 2.153 | −77.0% | −9.9632 to −4.4634 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05642 | 0.09149 | +62.2% | +0.0312 to +0.0390 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.354 | 2.196 | +62.2% | +0.7480 to +0.9355 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.354 | 2.196 | +62.2% | +0.7480 to +0.9355 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.4 | 311.4 | −36.5% | −220.5829 to −137.4046 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.937 | 2.091 | +8.0% | +0.0389 to +0.2695 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 38.27 | 69.62 | +81.9% | +28.0280 to +34.6673 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758 | 1361 | +79.5% | +483.7091 to +722.0909 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 482.8 | +891145.7% | +196.7068 to +768.7010 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 886.5 | +177205.9% | +424.0683 to +1347.9909 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.53 | 798.3 | +1118.3% | +529.7590 to +935.7327 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.7 | +10.700 (native is 0) | +3.7973 to +17.6027 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.889 | −18.5% | −1.9744 to −0.2468 | yes: GAIN |
| node-hours | 2.516 | 2.056 | −18.3% | −0.8222 to −0.0975 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.6 | +0.1% | −0.4846 to +0.9675 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 236.6 | −12.8% | −62.1020 to −7.3443 | yes: GAIN |
| response time (ms), mean | 272.4 | 237.9 | −12.7% | −50.3611 to −18.6841 | yes: GAIN |
| response time (ms), 95th percentile | 878 | 899.9 | +2.5% | −31.0282 to +74.7582 | no |
| response time (ms), 99th percentile | 1260 | 1329 | +5.4% | −28.0400 to +165.3120 | no |
| time over the response line (% of samples) | 14.1 | 13.82 | −2.0% | −1.0077 to +0.4454 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.2 | +5.9% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 | +41.200 (native is 0) | +24.7676 to +57.6324 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.367 | 8.867 | −5.3% | −2.3909 to +1.3909 | no |
| utilisation (used / allocatable) | 0.05642 | 0.06867 | +21.7% | +0.0022 to +0.0223 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.354 | 1.323 | −2.3% | −0.0582 to −0.0038 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0144 | +0.014 (native is 0) | +0.0130 to +0.0158 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.354 | 1.337 | −1.2% | −0.0442 to +0.0110 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.4 | 426.8 | −13.0% | −116.5494 to −10.4988 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.937 | 2.274 | +17.4% | +0.1720 to +0.5027 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.2676 to +2.4676 | no |
| pod start wait, mean (s) | 0 | 1.1 | +1.100 (native is 0) | −0.2676 to +2.4676 | no |
| host CPU busy, the real machine under kind (%) | 38.27 | 38.64 | +1.0% | −0.0635 to +0.7954 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758 | 758 | ±0.0% | −4.4480 to +4.4480 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.167 | −30.6% | −3.2188 to −0.4472 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.02083 | −61.5% | −0.0607 to −0.0059 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0 | −100.0% | −0.8770 to −0.1230 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 65.53 | 64.82 | −1.1% | −4.3919 to +2.9752 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.889 | −18.5% | −1.9744 to −0.2468 | yes: GAIN |
| node-hours | 2.511 | 2.056 | −18.1% | −0.8249 to −0.0849 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 283.9 | 271.6 | −4.3% | −14.2732 to −10.2350 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 283.9 | 236.6 | −16.6% | −75.9073 to −18.5302 | yes: GAIN |
| response time (ms), mean | 555.6 | 237.9 | −57.2% | −405.6024 to −229.7628 | yes: GAIN |
| response time (ms), 95th percentile | 1247 | 899.9 | −27.8% | −575.8683 to −117.7317 | yes: GAIN |
| response time (ms), 99th percentile | 1675 | 1329 | −20.7% | −770.0241 to +77.2957 | no |
| time over the response line (% of samples) | 46.63 | 13.82 | −70.4% | −43.4199 to −22.1974 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.6 | 7.2 | −68.1% | −18.2050 to −12.5950 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 | +41.200 (native is 0) | +24.7676 to +57.6324 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.153 | 8.867 | +311.8% | +4.5296 to +8.8970 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09149 | 0.06867 | −24.9% | −0.0329 to −0.0128 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.196 | 1.323 | −39.7% | −0.9773 to −0.7683 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0144 | +0.014 (native is 0) | +0.0130 to +0.0158 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.196 | 1.337 | −39.1% | −0.9635 to −0.7533 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 311.4 | 426.8 | +37.1% | +92.7646 to +138.1748 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.091 | 2.274 | +8.8% | +0.0235 to +0.3429 | yes: power given |
| pods started | 0.2 | 0.4 | +100.0% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 0.4 | 1.1 | +175.0% | −1.0859 to +2.4859 | no |
| pod start wait, mean (s) | 0.2 | 1.1 | +450.0% | −0.6249 to +2.4249 | no |
| host CPU busy, the real machine under kind (%) | 69.62 | 38.64 | −44.5% | −34.0052 to −27.9582 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1361 | 758 | −44.3% | −722.2053 to −483.5947 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.025 | −66.2% | −4.0361 to −3.9131 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 482.8 | 0.02083 | −100.0% | −768.7564 to −196.7181 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 886.5 | 0 | −100.0% | −1348.8048 to −424.2543 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 798.3 | 64.82 | −91.9% | −936.6673 to −530.2411 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.7 | 0 | −100.0% | −17.6027 to −3.7973 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.977 | −0.4% | −0.0566 to +0.0116 | no |
| node-hours | 2.516 | 2.504 | −0.5% | −0.0308 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 284.3 | +4.8% | +10.9875 to +14.8672 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 283.6 | +4.5% | +9.9382 to +14.5040 | yes: power given |
| response time (ms), mean | 272.4 | 551.6 | +102.5% | +211.8162 to +346.5606 | yes: LOSS |
| response time (ms), 95th percentile | 878 | 1216 | +38.5% | +93.8372 to +581.5418 | yes: LOSS |
| response time (ms), 99th percentile | 1260 | 1693 | +34.4% | +34.2627 to +832.3989 | yes: LOSS |
| time over the response line (% of samples) | 14.1 | 47.18 | +234.6% | +23.6642 to +42.4904 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 22.5 | +230.9% | +12.5180 to +18.8820 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.8 | +20.800 (native is 0) | +14.9034 to +26.6966 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.367 | 2.278 | −75.7% | −9.8638 to −4.3128 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05642 | 0.09227 | +63.5% | +0.0322 to +0.0395 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.354 | 2.207 | +63.0% | +0.7666 to +0.9390 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00854 | +0.009 (native is 0) | +0.0072 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.354 | 2.215 | +63.6% | +0.7758 to +0.9469 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.4 | 308.6 | −37.1% | −225.1628 to −138.4155 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.937 | 2.51 | +29.6% | +0.3105 to +0.8357 | yes: power given |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 38.27 | 70.19 | +83.4% | +28.8375 to +34.9951 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758 | 1368 | +80.4% | +494.3755 to +724.8245 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.756 | −4.1% | −0.7297 to +0.2415 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 510.3 | +942001.0% | +205.7788 to +814.7222 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 904.2 | +180731.7% | +434.9271 to +1372.3896 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 65.53 | 807.8 | +1132.8% | +539.3357 to +945.1560 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.6 | +10.600 (native is 0) | +3.7456 to +17.4544 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*