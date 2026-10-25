# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.123 | 5.996 |
| node-hours | 2.519 | 2.511 | 2.146 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 285.6 | 271.3 | 285.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 285.6 | 243.7 | 285.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 268.9 | 609.6 | 247.9 | 590.3 |
| response time (ms), 95th percentile | 828.6 | 1299 | 947.2 | 1279 |
| response time (ms), 99th percentile | 1198 | 1790 | 1363 | 1777 |
| time over the response line (% of samples) | 14.06 | 52.44 | 13.58 | 51.08 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 24.1 | 7.7 | 23.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 37 | 19.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.705 | 2.172 | 10.57 | 2.135 |
| utilisation (used / allocatable) | 0.05649 | 0.09629 | 0.06753 | 0.0957 |
| CPU used (cores), mean | 1.356 | 2.311 | 1.363 | 2.295 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.016 | 0.00892 |
| CPU used with Omni's own (cores), mean | 1.356 | 2.311 | 1.379 | 2.304 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486 | 296 | 427.6 | 297.8 |
| HPA replicas, mean | 1.946 | 2.015 | 2.313 | 2.574 |
| pods started | 0.2 | 0.3 | 0.3 | 0.7 |
| pod start wait, total (s) | 0.4 | 0.7 | 0.7 | 1.3 |
| pod start wait, mean (s) | 0.2 | 0.7 | 0.7 | 0.8 |
| host CPU busy, the real machine under kind (%) | 38.88 | 74.22 | 40.03 | 74.04 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 750.9 | 1455 | 755.3 | 1446 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.502 | 5.882 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 651.2 | 0.04167 | 646.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1134 | 0.2 | 1129 |
| queue: job turnaround, submitted to done, mean (s) | 59.51 | 938.6 | 62.07 | 929.7 |
| queue: jobs unfinished at the window's end | 0 | 14.4 | 0 | 13.7 |

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
| worker nodes in service, mean | 6 | 5.996 | −0.1% | −0.0132 to +0.0051 | no |
| node-hours | 2.511 | 2.51 | −0.0% | −0.0104 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.6 | 285.4 | −0.1% | −1.3107 to +0.9191 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.6 | 285.3 | −0.1% | −1.4082 to +0.7624 | no |
| response time (ms), mean | 609.6 | 590.3 | −3.2% | −40.7504 to +2.0854 | no |
| response time (ms), 95th percentile | 1299 | 1279 | −1.6% | −69.9793 to +29.0253 | no |
| response time (ms), 99th percentile | 1790 | 1777 | −0.7% | −123.8404 to +98.5722 | no |
| time over the response line (% of samples) | 52.44 | 51.08 | −2.6% | −3.6770 to +0.9554 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.1 | 23.9 | −0.8% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 | +19.800 (native is 0) | +15.9731 to +23.6269 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.172 | 2.135 | −1.7% | −0.3072 to +0.2338 | no |
| utilisation (used / allocatable) | 0.09629 | 0.0957 | −0.6% | −0.0021 to +0.0009 | no |
| CPU used (cores), mean | 2.311 | 2.295 | −0.7% | −0.0504 to +0.0189 | no |
| Omni's own CPU (cores), mean | 0 | 0.00892 | +0.009 (native is 0) | +0.0079 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.311 | 2.304 | −0.3% | −0.0419 to +0.0282 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296 | 297.8 | +0.6% | −3.0800 to +6.7025 | no |
| HPA replicas, mean | 2.015 | 2.574 | +27.8% | +0.3296 to +0.7899 | yes: power given |
| pods started | 0.3 | 0.7 | +133.3% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.7 | 1.3 | +85.7% | −1.0588 to +2.2588 | no |
| pod start wait, mean (s) | 0.7 | 0.8 | +14.3% | −0.9900 to +1.1900 | no |
| host CPU busy, the real machine under kind (%) | 74.22 | 74.04 | −0.3% | −1.6731 to +1.3014 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 1446 | −0.6% | −39.7375 to +22.1375 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.882 | −2.0% | −1.6125 to +1.3772 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 651.2 | 646.3 | −0.8% | −41.5955 to +31.6966 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1134 | 1129 | −0.5% | −41.8352 to +30.0896 | no |
| queue: job turnaround, submitted to done, mean (s) | 938.6 | 929.7 | −0.9% | −39.3103 to +21.5770 | no |
| queue: jobs unfinished at the window's end | 14.4 | 13.7 | −4.9% | −1.8209 to +0.4209 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.519 | 2.511 | −0.3% | −0.0137 to −0.0019 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 285.6 | +5.1% | +11.8358 to +16.0898 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 285.6 | +5.1% | +11.8358 to +16.0898 | yes: power given |
| response time (ms), mean | 268.9 | 609.6 | +126.7% | +288.5363 to +392.8527 | yes: LOSS |
| response time (ms), 95th percentile | 828.6 | 1299 | +56.8% | +269.9705 to +671.5335 | yes: LOSS |
| response time (ms), 99th percentile | 1198 | 1790 | +49.4% | +238.2900 to +945.9160 | yes: LOSS |
| time over the response line (% of samples) | 14.06 | 52.44 | +272.9% | +30.9677 to +45.7828 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 24.1 | +234.7% | +13.1383 to +20.6617 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.705 | 2.172 | −75.1% | −8.5055 to −4.5612 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05649 | 0.09629 | +70.5% | +0.0341 to +0.0456 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.356 | 2.311 | +70.5% | +0.8174 to +1.0933 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.356 | 2.311 | +70.5% | +0.8174 to +1.0933 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486 | 296 | −39.1% | −234.2879 to −145.7244 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.946 | 2.015 | +3.5% | −0.0552 to +0.1914 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.4 | 0.7 | +75.0% | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | −0.1079 to +1.1079 | no |
| host CPU busy, the real machine under kind (%) | 38.88 | 74.22 | +90.9% | +32.5731 to +38.1096 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.9 | 1455 | +93.8% | +631.9018 to +776.6982 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 651.2 | +1116327.0% | +394.4960 to +907.8856 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1134 | +226791.2% | +761.7921 to +1506.1196 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.51 | 938.6 | +1477.1% | +734.8670 to +1023.2247 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.4 | +14.400 (native is 0) | +8.4039 to +20.3961 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.123 | −14.6% | −1.6269 to −0.1275 | yes: GAIN |
| node-hours | 2.519 | 2.146 | −14.8% | −0.6844 to −0.0619 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.3 | −0.1% | −1.3236 to +0.7504 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 243.7 | −10.3% | −50.9299 to −4.8183 | yes: GAIN |
| response time (ms), mean | 268.9 | 247.9 | −7.8% | −40.3276 to −1.6520 | yes: GAIN |
| response time (ms), 95th percentile | 828.6 | 947.2 | +14.3% | −6.2262 to +243.3132 | no |
| response time (ms), 99th percentile | 1198 | 1363 | +13.8% | −46.1351 to +375.7067 | no |
| time over the response line (% of samples) | 14.06 | 13.58 | −3.4% | −1.3745 to +0.4071 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.7 | +6.9% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 | +37.000 (native is 0) | +25.2802 to +48.7198 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.705 | 10.57 | +21.4% | +0.3923 to +3.3343 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05649 | 0.06753 | +19.6% | +0.0014 to +0.0207 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.356 | 1.363 | +0.6% | −0.0109 to +0.0261 | no |
| Omni's own CPU (cores), mean | 0 | 0.016 | +0.016 (native is 0) | +0.0146 to +0.0174 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.356 | 1.379 | +1.7% | +0.0046 to +0.0427 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486 | 427.6 | −12.0% | −106.8916 to −9.9904 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.946 | 2.313 | +18.8% | +0.1024 to +0.6298 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.4 | 0.7 | +75.0% | −1.1326 to +1.7326 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | −0.6310 to +1.6310 | no |
| host CPU busy, the real machine under kind (%) | 38.88 | 40.03 | +2.9% | +0.9125 to +1.3748 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.9 | 755.3 | +0.6% | −0.0120 to +8.8120 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.502 | −25.0% | −2.7034 to −0.2923 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.04167 | −28.6% | −0.0375 to +0.0042 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | −60.0% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.51 | 62.07 | +4.3% | −0.2673 to +5.3839 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.123 | −14.6% | −1.6269 to −0.1275 | yes: GAIN |
| node-hours | 2.511 | 2.145 | −14.6% | −0.6774 to −0.0533 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 285.6 | 271.3 | −5.0% | −16.5457 to −11.9531 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.6 | 243.7 | −14.6% | −66.3408 to −17.3330 | yes: GAIN |
| response time (ms), mean | 609.6 | 247.9 | −59.3% | −418.4623 to −304.9065 | yes: GAIN |
| response time (ms), 95th percentile | 1299 | 947.2 | −27.1% | −628.1735 to −76.2435 | yes: GAIN |
| response time (ms), 99th percentile | 1790 | 1363 | −23.9% | −901.2865 to +46.6521 | no |
| time over the response line (% of samples) | 52.44 | 13.58 | −74.1% | −46.6396 to −31.0783 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.1 | 7.7 | −68.0% | −19.7754 to −13.0246 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 | +37.000 (native is 0) | +25.2802 to +48.7198 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.172 | 10.57 | +386.6% | +5.6814 to +11.1120 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09629 | 0.06753 | −29.9% | −0.0374 to −0.0201 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.311 | 1.363 | −41.0% | −1.0950 to −0.8005 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.016 | +0.016 (native is 0) | +0.0146 to +0.0174 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.311 | 1.379 | −40.3% | −1.0794 to −0.7841 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296 | 427.6 | +44.4% | +106.9378 to +156.1924 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.015 | 2.313 | +14.8% | +0.1116 to +0.4843 | yes: power given |
| pods started | 0.3 | 0.3 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.7 | 0.7 | ±0.0% | −1.2158 to +1.2158 | no |
| pod start wait, mean (s) | 0.7 | 0.7 | ±0.0% | −1.2158 to +1.2158 | no |
| host CPU busy, the real machine under kind (%) | 74.22 | 40.03 | −46.1% | −37.0530 to −31.3425 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 755.3 | −48.1% | −771.5312 to −628.2688 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 651.2 | 0.04167 | −100.0% | −907.8975 to −394.5174 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1134 | 0.2 | −100.0% | −1506.5158 to −761.9959 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 938.6 | 62.07 | −93.4% | −1019.9428 to −733.0322 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.4 | 0 | −100.0% | −20.3961 to −8.4039 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.996 | −0.1% | −0.0132 to +0.0051 | no |
| node-hours | 2.519 | 2.51 | −0.4% | −0.0138 to −0.0043 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 285.4 | +5.1% | +11.2931 to +16.2408 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 285.3 | +5.0% | +11.1844 to +16.0954 | yes: power given |
| response time (ms), mean | 268.9 | 590.3 | +119.5% | +272.1430 to +370.5811 | yes: LOSS |
| response time (ms), 95th percentile | 828.6 | 1279 | +54.3% | +244.5691 to +655.9809 | yes: LOSS |
| response time (ms), 99th percentile | 1198 | 1777 | +48.4% | +197.8759 to +961.0619 | yes: LOSS |
| time over the response line (% of samples) | 14.06 | 51.08 | +263.2% | +30.0930 to +43.9358 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 23.9 | +231.9% | +13.0363 to +20.3637 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 | +19.800 (native is 0) | +15.9731 to +23.6269 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.705 | 2.135 | −75.5% | −8.4484 to −4.6916 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05649 | 0.0957 | +69.4% | +0.0336 to +0.0448 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.356 | 2.295 | +69.3% | +0.8048 to +1.0744 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00892 | +0.009 (native is 0) | +0.0079 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.356 | 2.304 | +70.0% | +0.8143 to +1.0827 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 486 | 297.8 | −38.7% | −231.3233 to −145.0665 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.946 | 2.574 | +32.3% | +0.3817 to +0.8741 | yes: power given |
| pods started | 0.2 | 0.7 | +250.0% | −0.3430 to +1.3430 | no |
| pod start wait, total (s) | 0.4 | 1.3 | +225.0% | −0.9910 to +2.7910 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | −0.3656 to +1.5656 | no |
| host CPU busy, the real machine under kind (%) | 38.88 | 74.04 | +90.4% | +32.0947 to +38.2164 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.9 | 1446 | +92.6% | +608.2226 to +782.7774 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.882 | −2.0% | −1.6125 to +1.3772 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 646.3 | +1107842.3% | +375.3862 to +917.0964 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1129 | +225616.6% | +734.4570 to +1521.7091 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.51 | 929.7 | +1462.2% | +708.7930 to +1031.5653 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.7 | +13.700 (native is 0) | +7.7913 to +19.6087 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*