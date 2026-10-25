# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.52 | 1.512 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.4 | 161.3 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.4 | 161.3 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 148 | 147.6 | 92.58 | 92.81 |
| response time (ms), 95th percentile | 293.2 | 298.1 | 153.1 | 151.1 |
| response time (ms), 99th percentile | 410.1 | 429.6 | 190.9 | 191 |
| time over the response line (% of samples) | 0.4494 | 0.58 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.4 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 30.8 | 23.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.02667 | 0.1067 | 0.2217 |
| utilisation (used / allocatable) | 0.0373 | 0.03724 | 0.0495 | 0.04928 |
| CPU used (cores), mean | 0.8952 | 0.8937 | 1.188 | 1.183 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00951 | 0.00891 |
| CPU used with Omni's own (cores), mean | 0.8952 | 0.8937 | 1.197 | 1.192 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.3 | 705 | 543.4 | 545.2 |
| HPA replicas, mean | 8.912 | 9.594 | 10.34 | 10.3 |
| pods started | 5 | 3.6 | 7.2 | 3.5 |
| pod start wait, total (s) | 7.1 | 6.1 | 12.5 | 5.4 |
| pod start wait, mean (s) | 1.42 | 1.708 | 1.752 | 1.568 |
| host CPU busy, the real machine under kind (%) | 26.77 | 27.02 | 35.13 | 35.18 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.512 | −0.6% | −0.0168 to −0.0005 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 161.3 | +1.2% | +0.9602 to +2.7498 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 161.3 | +1.2% | +0.9602 to +2.7498 | yes: power given |
| response time (ms), mean | 147.6 | 92.81 | −37.1% | −65.7935 to −43.8548 | yes: GAIN |
| response time (ms), 95th percentile | 298.1 | 151.1 | −49.3% | −168.8255 to −125.2665 | yes: GAIN |
| response time (ms), 99th percentile | 429.6 | 191 | −55.5% | −280.2530 to −196.9636 | yes: GAIN |
| time over the response line (% of samples) | 0.58 | 0 | −100.0% | −0.9710 to −0.1890 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | −100.0% | −0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.7 | +23.700 (native is 0) | +19.2132 to +28.1868 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.2217 | +731.3% | −0.0696 to +0.4596 | no |
| utilisation (used / allocatable) | 0.03724 | 0.04928 | +32.3% | +0.0101 to +0.0140 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8937 | 1.183 | +32.3% | +0.2414 to +0.3364 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00891 | +0.009 (native is 0) | +0.0080 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8937 | 1.192 | +33.3% | +0.2496 to +0.3460 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705 | 545.2 | −22.7% | −178.9241 to −140.5428 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.594 | 10.3 | +7.4% | −0.0294 to +1.4410 | no |
| pods started | 3.6 | 3.5 | −2.8% | −1.0802 to +0.8802 | no |
| pod start wait, total (s) | 6.1 | 5.4 | −11.5% | −3.0855 to +1.6855 | no |
| pod start wait, mean (s) | 1.708 | 1.568 | −8.2% | −0.6067 to +0.3267 | no |
| host CPU busy, the real machine under kind (%) | 27.02 | 35.18 | +30.2% | +6.8124 to +9.5189 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.517 | 1.52 | +0.2% | +0.0019 to +0.0051 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.4 | +0.2% | +0.1376 to +0.5928 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.4 | +0.2% | +0.1376 to +0.5928 | yes: power given |
| response time (ms), mean | 148 | 147.6 | −0.3% | −3.2446 to +2.4835 | no |
| response time (ms), 95th percentile | 293.2 | 298.1 | +1.7% | −6.1008 to +16.0558 | no |
| response time (ms), 99th percentile | 410.1 | 429.6 | +4.8% | +3.7701 to +35.2861 | yes: LOSS |
| time over the response line (% of samples) | 0.4494 | 0.58 | +29.1% | −0.1081 to +0.3692 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.4 | +300.0% | −0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.02667 | −66.7% | −0.1740 to +0.0673 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03724 | −0.2% | −0.0006 to +0.0004 | no |
| CPU used (cores), mean | 0.8952 | 0.8937 | −0.2% | −0.0136 to +0.0106 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8952 | 0.8937 | −0.2% | −0.0136 to +0.0106 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.3 | 705 | +0.2% | −8.2305 to +11.6513 | no |
| HPA replicas, mean | 8.912 | 9.594 | +7.7% | +0.5740 to +0.7897 | yes: power given |
| pods started | 5 | 3.6 | −28.0% | −1.7694 to −1.0306 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 6.1 | −14.1% | −3.3844 to +1.3844 | no |
| pod start wait, mean (s) | 1.42 | 1.708 | +20.3% | −0.2536 to +0.8302 | no |
| host CPU busy, the real machine under kind (%) | 26.77 | 27.02 | +0.9% | −0.0574 to +0.5526 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.517 | 1.512 | −0.4% | −0.0144 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.3 | +1.4% | +1.2953 to +3.2359 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.3 | +1.4% | +1.2953 to +3.2359 | yes: power given |
| response time (ms), mean | 148 | 92.58 | −37.5% | −64.4200 to −46.4502 | yes: GAIN |
| response time (ms), 95th percentile | 293.2 | 153.1 | −47.8% | −152.1269 to −128.0321 | yes: GAIN |
| response time (ms), 99th percentile | 410.1 | 190.9 | −53.4% | −249.3204 to −188.9870 | yes: GAIN |
| time over the response line (% of samples) | 0.4494 | 0 | −100.0% | −0.6853 to −0.2135 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.8 | +30.800 (native is 0) | +25.4493 to +36.1507 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | +33.3% | −0.1630 to +0.2164 | no |
| utilisation (used / allocatable) | 0.0373 | 0.0495 | +32.7% | +0.0097 to +0.0147 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8952 | 1.188 | +32.7% | +0.2319 to +0.3537 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00951 | +0.010 (native is 0) | +0.0083 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8952 | 1.197 | +33.8% | +0.2404 to +0.3641 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.3 | 543.4 | −22.7% | −189.5508 to −130.1713 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.912 | 10.34 | +16.0% | +0.8166 to +2.0323 | yes: power given |
| pods started | 5 | 7.2 | +44.0% | +1.1444 to +3.2556 | yes: power given |
| pod start wait, total (s) | 7.1 | 12.5 | +76.1% | +2.4759 to +8.3241 | yes: LOSS |
| pod start wait, mean (s) | 1.42 | 1.752 | +23.4% | +0.0000 to +0.6650 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.77 | 35.13 | +31.2% | +6.7274 to +9.9894 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.52 | 1.512 | −0.6% | −0.0174 to −0.0003 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 161.3 | +1.2% | +1.0077 to +2.7932 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 161.3 | +1.2% | +1.0077 to +2.7932 | yes: power given |
| response time (ms), mean | 147.6 | 92.58 | −37.3% | −65.8927 to −44.2164 | yes: GAIN |
| response time (ms), 95th percentile | 298.1 | 153.1 | −48.7% | −166.0541 to −124.0599 | yes: GAIN |
| response time (ms), 99th percentile | 429.6 | 190.9 | −55.6% | −274.7288 to −202.6348 | yes: GAIN |
| time over the response line (% of samples) | 0.58 | 0 | −100.0% | −0.9710 to −0.1890 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | −100.0% | −0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.8 | +30.800 (native is 0) | +25.4493 to +36.1507 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1067 | +300.0% | −0.0487 to +0.2087 | no |
| utilisation (used / allocatable) | 0.03724 | 0.0495 | +32.9% | +0.0101 to +0.0144 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8937 | 1.188 | +32.9% | +0.2422 to +0.3463 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00951 | +0.010 (native is 0) | +0.0083 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8937 | 1.197 | +34.0% | +0.2507 to +0.3568 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705 | 543.4 | −22.9% | −183.4841 to −139.6588 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.594 | 10.34 | +7.7% | +0.1310 to +1.3542 | yes: power given |
| pods started | 3.6 | 7.2 | +100.0% | +2.4715 to +4.7285 | yes: power given |
| pod start wait, total (s) | 6.1 | 12.5 | +104.9% | +3.6772 to +9.1228 | yes: LOSS |
| pod start wait, mean (s) | 1.708 | 1.752 | +2.6% | −0.4160 to +0.5044 | no |
| host CPU busy, the real machine under kind (%) | 27.02 | 35.13 | +30.0% | +6.6879 to +9.5336 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.512 | −0.3% | −0.0132 to +0.0029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.3 | +1.4% | +1.3298 to +3.1106 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.3 | +1.4% | +1.3298 to +3.1106 | yes: power given |
| response time (ms), mean | 148 | 92.81 | −37.3% | −64.2733 to −46.1361 | yes: GAIN |
| response time (ms), 95th percentile | 293.2 | 151.1 | −48.5% | −155.1828 to −128.9542 | yes: GAIN |
| response time (ms), 99th percentile | 410.1 | 191 | −53.4% | −252.4358 to −185.7246 | yes: GAIN |
| time over the response line (% of samples) | 0.4494 | 0 | −100.0% | −0.6853 to −0.2135 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.7 | +23.700 (native is 0) | +19.2132 to +28.1868 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.2217 | +177.1% | −0.0701 to +0.3535 | no |
| utilisation (used / allocatable) | 0.0373 | 0.04928 | +32.1% | +0.0097 to +0.0143 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8952 | 1.183 | +32.1% | +0.2316 to +0.3432 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00891 | +0.009 (native is 0) | +0.0080 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8952 | 1.192 | +33.1% | +0.2399 to +0.3528 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.3 | 545.2 | −22.5% | −184.6706 to −131.3756 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.912 | 10.3 | +15.6% | +0.7358 to +2.0395 | yes: power given |
| pods started | 5 | 3.5 | −30.0% | −2.7274 to −0.2726 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.4 | −23.9% | −4.0374 to +0.6374 | no |
| pod start wait, mean (s) | 1.42 | 1.568 | +10.4% | −0.1411 to +0.4378 | no |
| host CPU busy, the real machine under kind (%) | 26.77 | 35.18 | +31.4% | +6.8601 to +9.9664 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*