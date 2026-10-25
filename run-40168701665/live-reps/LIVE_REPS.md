# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.592 | 5.689 |
| node-hours | 2.515 | 2.511 | 2.347 | 2.382 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 | 272.8 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 272.4 | 260 | 262.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 353.8 | 344.3 | 348.4 | 358.7 |
| response time (ms), 95th percentile | 1264 | 1254 | 1282 | 1375 |
| response time (ms), 99th percentile | 1993 | 2139 | 1922 | 2272 |
| time over the response line (% of samples) | 17.97 | 16.35 | 17.94 | 16.94 |
| failed requests (%) | 0 | 0 | 0.01058 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.4 | 10.6 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 15.2 | 18 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 12.54 | 11.78 | 11.31 |
| utilisation (used / allocatable) | 0.06104 | 0.06156 | 0.06561 | 0.06329 |
| CPU used (cores), mean | 1.465 | 1.477 | 1.456 | 1.441 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01176 | 0.01334 |
| CPU used with Omni's own (cores), mean | 1.465 | 1.477 | 1.468 | 1.454 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.8 | 444.9 | 427.1 | 438.9 |
| HPA replicas, mean | 2.171 | 2.093 | 2.447 | 2.466 |
| pods started | 0 | 0 | 0.4 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 1.1 | 1.7 |
| pod start wait, mean (s) | 0 | 0 | 1.1 | 1.5 |
| host CPU busy, the real machine under kind (%) | 41.91 | 42.82 | 42.45 | 43.3 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 776 | 780.5 | 777.9 | 784 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.31 | 5.446 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.2292 | 0.1083 | 0.2083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | 0.6 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 85.94 | 91.65 | 86.86 | 94.77 |
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
| worker nodes in service, mean | 6 | 5.689 | −5.2% | −0.8177 to +0.1962 | no |
| node-hours | 2.511 | 2.382 | −5.1% | −0.3408 to +0.0828 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.2 | −0.1% | −0.9812 to +0.5853 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 262.4 | −3.6% | −26.2937 to +6.4228 | no |
| response time (ms), mean | 344.3 | 358.7 | +4.2% | −13.2492 to +42.0456 | no |
| response time (ms), 95th percentile | 1254 | 1375 | +9.6% | −79.4232 to +320.7512 | no |
| response time (ms), 99th percentile | 2139 | 2272 | +6.2% | −143.8486 to +410.5228 | no |
| time over the response line (% of samples) | 16.35 | 16.94 | +3.6% | −0.2541 to +1.4266 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.6 | +1.9% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +13.2432 to +22.7568 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.54 | 11.3 | −9.8% | −2.9110 to +0.4443 | no |
| utilisation (used / allocatable) | 0.06156 | 0.06329 | +2.8% | −0.0015 to +0.0050 | no |
| CPU used (cores), mean | 1.477 | 1.441 | −2.5% | −0.0929 to +0.0201 | no |
| Omni's own CPU (cores), mean | 0 | 0.01334 | +0.013 (native is 0) | +0.0123 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.477 | 1.454 | −1.6% | −0.0799 to +0.0338 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.9 | 438.9 | −1.4% | −18.1050 to +6.0736 | no |
| HPA replicas, mean | 2.093 | 2.466 | +17.8% | +0.1089 to +0.6378 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0 | 1.7 | +1.700 (native is 0) | −0.1485 to +3.5485 | no |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | −0.2602 to +3.2602 | no |
| host CPU busy, the real machine under kind (%) | 42.82 | 43.3 | +1.1% | +0.1695 to +0.7959 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.5 | 784 | +0.4% | −1.9502 to +8.9502 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.446 | −9.2% | −1.4274 to +0.3191 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2292 | 0.2083 | −9.1% | −0.0900 to +0.0484 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.65 | 94.77 | +3.4% | −0.7832 to +7.0165 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.511 | −0.1% | −0.0102 to +0.0032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 | −0.0% | −0.7811 to +0.6336 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 272.4 | −0.0% | −0.7811 to +0.6336 | no |
| response time (ms), mean | 353.8 | 344.3 | −2.7% | −29.6284 to +10.5229 | no |
| response time (ms), 95th percentile | 1264 | 1254 | −0.8% | −159.3253 to +139.9043 | no |
| response time (ms), 99th percentile | 1993 | 2139 | +7.3% | −189.4994 to +481.4376 | no |
| time over the response line (% of samples) | 17.97 | 16.35 | −9.0% | −2.7390 to −0.5053 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.4 | −1.0% | −0.8113 to +0.6113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 12.54 | +8.8% | −1.0594 to +3.0860 | no |
| utilisation (used / allocatable) | 0.06104 | 0.06156 | +0.9% | −0.0004 to +0.0014 | no |
| CPU used (cores), mean | 1.465 | 1.477 | +0.9% | −0.0084 to +0.0336 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.465 | 1.477 | +0.9% | −0.0084 to +0.0336 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.8 | 444.9 | −1.1% | −13.5119 to +3.7452 | no |
| HPA replicas, mean | 2.171 | 2.093 | −3.6% | −0.3235 to +0.1671 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 41.91 | 42.82 | +2.2% | +0.4992 to +1.3044 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776 | 780.5 | +0.6% | −0.5720 to +9.5720 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.2292 | +223.5% | +0.0816 to +0.2350 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.94 | 91.65 | +6.6% | −0.8573 to +12.2823 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.592 | −6.8% | −0.9989 to +0.1834 | no |
| node-hours | 2.515 | 2.347 | −6.7% | −0.4159 to +0.0798 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.8 | +0.1% | −0.0202 to +0.7093 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 260 | −4.6% | −31.0722 to +6.1029 | no |
| response time (ms), mean | 353.8 | 348.4 | −1.5% | −13.0606 to +2.2008 | no |
| response time (ms), 95th percentile | 1264 | 1282 | +1.5% | −41.9671 to +78.7451 | no |
| response time (ms), 99th percentile | 1993 | 1922 | −3.6% | −289.3610 to +147.4282 | no |
| time over the response line (% of samples) | 17.97 | 17.94 | −0.2% | −0.6741 to +0.6050 | no |
| failed requests (%) | 0 | 0.01058 | +0.011 (native is 0) | −0.0134 to +0.0345 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.6 | +1.0% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.2 | +15.200 (native is 0) | +11.7645 to +18.6355 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 11.78 | +2.2% | −1.5270 to +2.0304 | no |
| utilisation (used / allocatable) | 0.06104 | 0.06561 | +7.5% | −0.0026 to +0.0118 | no |
| CPU used (cores), mean | 1.465 | 1.456 | −0.6% | −0.0268 to +0.0095 | no |
| Omni's own CPU (cores), mean | 0 | 0.01176 | +0.012 (native is 0) | +0.0106 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.468 | +0.2% | −0.0157 to +0.0219 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.8 | 427.1 | −5.0% | −57.4767 to +12.1200 | no |
| HPA replicas, mean | 2.171 | 2.447 | +12.7% | −0.0213 to +0.5740 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.3086 to +2.5086 | no |
| pod start wait, mean (s) | 0 | 1.1 | +1.100 (native is 0) | −0.3086 to +2.5086 | no |
| host CPU busy, the real machine under kind (%) | 41.91 | 42.45 | +1.3% | +0.1565 to +0.9068 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776 | 777.9 | +0.2% | −2.0389 to +5.8389 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.31 | −11.5% | −1.6120 to +0.2320 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.1083 | +52.9% | −0.0245 to +0.0995 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.94 | 86.86 | +1.1% | −3.3402 to +5.1818 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.592 | −6.8% | −0.9989 to +0.1834 | no |
| node-hours | 2.511 | 2.347 | −6.6% | −0.4113 to +0.0822 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.8 | +0.2% | −0.4101 to +1.2467 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 260 | −4.6% | −31.1124 to +6.2906 | no |
| response time (ms), mean | 344.3 | 348.4 | +1.2% | −17.8672 to +26.1130 | no |
| response time (ms), 95th percentile | 1254 | 1282 | +2.2% | −84.2943 to +140.4933 | no |
| response time (ms), 99th percentile | 2139 | 1922 | −10.1% | −584.4625 to +150.5915 | no |
| time over the response line (% of samples) | 16.35 | 17.94 | +9.7% | +0.4399 to +2.7353 | yes: LOSS |
| failed requests (%) | 0 | 0.01058 | +0.011 (native is 0) | −0.0134 to +0.0345 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.6 | +1.9% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.2 | +15.200 (native is 0) | +11.7645 to +18.6355 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.54 | 11.78 | −6.1% | −2.1261 to +0.6027 | no |
| utilisation (used / allocatable) | 0.06156 | 0.06561 | +6.6% | −0.0024 to +0.0105 | no |
| CPU used (cores), mean | 1.477 | 1.456 | −1.4% | −0.0530 to +0.0106 | no |
| Omni's own CPU (cores), mean | 0 | 0.01176 | +0.012 (native is 0) | +0.0106 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.477 | 1.468 | −0.6% | −0.0421 to +0.0232 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.9 | 427.1 | −4.0% | −44.2972 to +8.7072 | no |
| HPA replicas, mean | 2.093 | 2.447 | +16.9% | +0.0802 to +0.6289 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.3086 to +2.5086 | no |
| pod start wait, mean (s) | 0 | 1.1 | +1.100 (native is 0) | −0.3086 to +2.5086 | no |
| host CPU busy, the real machine under kind (%) | 42.82 | 42.45 | −0.9% | −0.7338 to −0.0065 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.5 | 777.9 | −0.3% | −5.3228 to +0.1228 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.31 | −11.5% | −1.6120 to +0.2320 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2292 | 0.1083 | −52.7% | −0.2113 to −0.0304 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.6 | −33.3% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.65 | 86.86 | −5.2% | −8.2876 to −1.2957 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.689 | −5.2% | −0.8177 to +0.1962 | no |
| node-hours | 2.515 | 2.382 | −5.3% | −0.3456 to +0.0806 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.2 | −0.1% | −1.0883 to +0.5449 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 262.4 | −3.7% | −26.2886 to +6.2702 | no |
| response time (ms), mean | 353.8 | 358.7 | +1.4% | −10.6493 to +20.3403 | no |
| response time (ms), 95th percentile | 1264 | 1375 | +8.8% | −30.4361 to +252.3431 | no |
| response time (ms), 99th percentile | 1993 | 2272 | +14.0% | −4.5191 to +563.1315 | no |
| time over the response line (% of samples) | 17.97 | 16.94 | −5.8% | −1.9076 to −0.1642 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.6 | +1.0% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +13.2432 to +22.7568 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.53 | 11.3 | −1.9% | −2.4817 to +2.0417 | no |
| utilisation (used / allocatable) | 0.06104 | 0.06329 | +3.7% | −0.0018 to +0.0063 | no |
| CPU used (cores), mean | 1.465 | 1.441 | −1.6% | −0.0652 to +0.0176 | no |
| Omni's own CPU (cores), mean | 0 | 0.01334 | +0.013 (native is 0) | +0.0123 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.454 | −0.7% | −0.0522 to +0.0312 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.8 | 438.9 | −2.4% | −30.8386 to +9.0405 | no |
| HPA replicas, mean | 2.171 | 2.466 | +13.6% | +0.0422 to +0.5481 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0 | 1.7 | +1.700 (native is 0) | −0.1485 to +3.5485 | no |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | −0.2602 to +3.2602 | no |
| host CPU busy, the real machine under kind (%) | 41.91 | 43.3 | +3.3% | +1.0166 to +1.7523 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776 | 784 | +1.0% | +0.4902 to +15.5098 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.446 | −9.2% | −1.4274 to +0.3191 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.2083 | +194.1% | +0.0618 to +0.2132 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.94 | 94.77 | +10.3% | +0.1776 to +17.4807 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*