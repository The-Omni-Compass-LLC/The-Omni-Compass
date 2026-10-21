# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.046 | 5.29 |
| node-hours | 2.519 | 2.517 | 2.118 | 2.216 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.5 | 272.2 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.5 | 242.2 | 249.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 305.3 | 340.6 | 270.5 | 312.7 |
| response time (ms), 95th percentile | 997.3 | 1347 | 1048 | 1390 |
| response time (ms), 99th percentile | 1461 | 2023 | 1521 | 2011 |
| time over the response line (% of samples) | 13.61 | 12.01 | 13.27 | 12.26 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.3 | 8.2 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 51.9 | 28.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 83.33 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.08 | 16.48 | 10.47 | 17.76 |
| utilisation (used / allocatable) | 0.05936 | 0.05921 | 0.06964 | 0.06726 |
| CPU used (cores), mean | 1.425 | 1.421 | 1.392 | 1.416 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01732 | 0.0171 |
| CPU used with Omni's own (cores), mean | 1.425 | 1.421 | 1.409 | 1.433 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 466.5 | 417.6 | 425.5 |
| HPA replicas, mean | 1.942 | 2.062 | 2.231 | 2.369 |
| pods started | 0.1 | 0.2 | 0.2 | 0.6 |
| pod start wait, total (s) | 0.3 | 0.4 | 0.4 | 0.9 |
| pod start wait, mean (s) | 0.3 | 0.2 | 0.4 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.27 | 42.91 | 41.07 | 43.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 770.4 | 798.2 | 770.7 | 799 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.295 | 4.747 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.7792 | 0.03333 | 0.9708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.9 | 0.2 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 76.83 | 105.3 | 76.62 | 106 |
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
| worker nodes in service, mean | 6 | 5.29 | -11.8% | -1.386 to -0.03348 | yes: GAIN |
| node-hours | 2.517 | 2.216 | -12.0% | -0.5811 to -0.02081 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.1 | -0.1% | -1.355 to +0.5786 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 249.8 | -8.3% | -43.95 to -1.416 | yes: GAIN |
| response time (ms), mean | 340.6 | 312.7 | -8.2% | -42.09 to -13.62 | yes: GAIN |
| response time (ms), 95th percentile | 1347 | 1390 | +3.1% | -40.29 to +124.7 | no |
| response time (ms), 99th percentile | 2023 | 2011 | -0.6% | -143.2 to +118.9 | no |
| time over the response line (% of samples) | 12.01 | 12.26 | +2.1% | -0.6275 to +1.134 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 7.9 | -4.8% | -1.671 to +0.8707 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.4 | +28.4 (native is 0) | +19.3 to +37.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.48 | 17.76 | +7.7% | -0.2578 to +2.811 | no |
| utilisation (used / allocatable) | 0.05921 | 0.06726 | +13.6% | +0.001193 to +0.0149 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.421 | 1.416 | -0.4% | -0.04046 to +0.02931 | no |
| Omni's own CPU (cores), mean | 0 | 0.0171 | +0.0171 (native is 0) | +0.01452 to +0.01968 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.433 | +0.8% | -0.02211 to +0.04516 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.5 | 425.5 | -8.8% | -74.74 to -7.331 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.062 | 2.369 | +14.9% | +0.04174 to +0.5725 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | -0.5796 to +1.58 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | -0.05776 to +1.458 | no |
| host CPU busy, the real machine under kind (%) | 42.91 | 43.58 | +1.6% | +0.2117 to +1.128 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 798.2 | 799 | +0.1% | -1.872 to +3.472 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.747 | -20.9% | -2.409 to -0.09777 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.9708 | +24.6% | -0.003117 to +0.3865 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 1.9 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.3 | 106 | +0.7% | -1.297 to +2.78 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.193e-15 to +3.046e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.519 | 2.517 | -0.1% | -0.008207 to +0.002874 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.5 | -0.1% | -1.073 to +0.5787 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.5 | -0.1% | -1.073 to +0.5787 | no |
| response time (ms), mean | 305.3 | 340.6 | +11.5% | -2.874 to +73.35 | no |
| response time (ms), 95th percentile | 997.3 | 1347 | +35.1% | +24.69 to +675.5 | yes: LOSS |
| response time (ms), 99th percentile | 1461 | 2023 | +38.5% | +80.53 to +1044 | yes: LOSS |
| time over the response line (% of samples) | 13.61 | 12.01 | -11.8% | -4.649 to +1.448 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.3 | +2.5% | -0.9081 to +1.308 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.08 | 16.48 | +63.6% | +0.7028 to +12.11 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05936 | 0.05921 | -0.3% | -0.001074 to +0.0007738 | no |
| CPU used (cores), mean | 1.425 | 1.421 | -0.3% | -0.02577 to +0.01857 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.425 | 1.421 | -0.3% | -0.02577 to +0.01857 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 466.5 | +0.5% | -5.339 to +10.31 | no |
| HPA replicas, mean | 1.942 | 2.062 | +6.2% | +0.00437 to +0.2357 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | -1.09 to +1.29 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | -33.3% | -0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 40.27 | 42.91 | +6.6% | +2.032 to +3.248 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.4 | 798.2 | +3.6% | +4.898 to +50.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.7792 | +1338.5% | +0.4902 to +0.9598 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.9 | +375.0% | +0.05949 to +2.941 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 76.83 | 105.3 | +37.0% | +8.346 to +48.5 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.046 | -15.9% | -1.666 to -0.2412 | yes: GAIN |
| node-hours | 2.519 | 2.117 | -15.9% | -0.6979 to -0.1057 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.2 | -0.2% | -1.408 to +0.3989 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 242.2 | -11.2% | -52.89 to -8.194 | yes: GAIN |
| response time (ms), mean | 305.3 | 270.5 | -11.4% | -47.97 to -21.77 | yes: GAIN |
| response time (ms), 95th percentile | 997.3 | 1048 | +5.0% | -18.47 to +119 | no |
| response time (ms), 99th percentile | 1461 | 1521 | +4.1% | -82.62 to +203.6 | no |
| time over the response line (% of samples) | 13.61 | 13.27 | -2.5% | -1.021 to +0.3519 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.2 | +1.2% | -0.8802 to +1.08 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.9 | +51.9 (native is 0) | +30.2 to +73.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.08 | 10.47 | +3.9% | -1.435 to +2.225 | no |
| utilisation (used / allocatable) | 0.05936 | 0.06964 | +17.3% | +0.002354 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.425 | 1.392 | -2.3% | -0.06161 to -0.004597 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01732 | +0.0173 (native is 0) | +0.01531 to +0.01933 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.425 | 1.409 | -1.1% | -0.04338 to +0.01181 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 417.6 | -10.0% | -83.17 to -9.716 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.231 | +14.9% | -0.007657 to +0.587 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | -0.8802 to +1.08 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | -0.8802 to +1.08 | no |
| host CPU busy, the real machine under kind (%) | 40.27 | 41.07 | +2.0% | +0.5095 to +1.083 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.4 | 770.7 | +0.0% | -2.882 to +3.482 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.295 | -28.4% | -2.903 to -0.5071 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.03333 | -38.5% | -0.06356 to +0.0219 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.2 | -50.0% | -0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 76.83 | 76.62 | -0.3% | -3.269 to +2.844 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.046 | -15.9% | -1.666 to -0.2412 | yes: GAIN |
| node-hours | 2.517 | 2.118 | -15.9% | -0.6951 to -0.1033 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.2 | -0.1% | -1.186 to +0.6709 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 242.2 | -11.1% | -52.61 to -7.975 | yes: GAIN |
| response time (ms), mean | 340.6 | 270.5 | -20.6% | -109.6 to -30.6 | yes: GAIN |
| response time (ms), 95th percentile | 1347 | 1048 | -22.3% | -587.3 to -12.29 | yes: GAIN |
| response time (ms), 99th percentile | 2023 | 1521 | -24.8% | -912.9 to -90.18 | yes: GAIN |
| time over the response line (% of samples) | 12.01 | 13.27 | +10.5% | -1.419 to +3.951 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.2 | -1.2% | -1.19 to +0.99 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.9 | +51.9 (native is 0) | +30.2 to +73.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.48 | 10.47 | -36.5% | -11.96 to -0.06963 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05921 | 0.06964 | +17.6% | +0.002288 to +0.01857 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.421 | 1.392 | -2.1% | -0.05896 to -5.534e-05 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01732 | +0.0173 (native is 0) | +0.01531 to +0.01933 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.409 | -0.9% | -0.03985 to +0.01548 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.5 | 417.6 | -10.5% | -88.19 to -9.665 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.062 | 2.231 | +8.2% | -0.1784 to +0.5177 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.584 to +0.584 | no |
| pod start wait, total (s) | 0.4 | 0.4 | +0.0% | -1.168 to +1.168 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | -0.6121 to +1.012 | no |
| host CPU busy, the real machine under kind (%) | 42.91 | 41.07 | -4.3% | -2.444 to -1.243 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 798.2 | 770.7 | -3.4% | -51.44 to -3.561 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.295 | -28.4% | -2.903 to -0.5071 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.03333 | -95.7% | -0.9832 to -0.5085 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.2 | -89.5% | -3.133 to -0.2674 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 105.3 | 76.62 | -27.2% | -48.56 to -8.713 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.29 | -11.8% | -1.386 to -0.03348 | yes: GAIN |
| node-hours | 2.519 | 2.216 | -12.1% | -0.5836 to -0.02358 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 | -0.2% | -1.362 to +0.09135 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 249.8 | -8.4% | -44.22 to -1.643 | yes: GAIN |
| response time (ms), mean | 305.3 | 312.7 | +2.4% | -30.11 to +44.89 | no |
| response time (ms), 95th percentile | 997.3 | 1390 | +39.3% | +33.61 to +751 | yes: LOSS |
| response time (ms), 99th percentile | 1461 | 2011 | +37.6% | +48.58 to +1051 | yes: LOSS |
| time over the response line (% of samples) | 13.61 | 12.26 | -9.9% | -4.45 to +1.755 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 7.9 | -2.5% | -1.358 to +0.9583 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.4 | +28.4 (native is 0) | +19.3 to +37.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.08 | 17.76 | +76.3% | +1.573 to +13.8 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05936 | 0.06726 | +13.3% | +0.001296 to +0.01449 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.425 | 1.416 | -0.6% | -0.04723 to +0.02888 | no |
| Omni's own CPU (cores), mean | 0 | 0.0171 | +0.0171 (native is 0) | +0.01452 to +0.01968 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.425 | 1.433 | +0.6% | -0.02971 to +0.04557 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 425.5 | -8.3% | -69.71 to -7.396 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.942 | 2.369 | +22.0% | +0.227 to +0.6274 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0.3 | 0.9 | +200.0% | -0.4769 to +1.677 | no |
| pod start wait, mean (s) | 0.3 | 0.9 | +200.0% | -0.4769 to +1.677 | no |
| host CPU busy, the real machine under kind (%) | 40.27 | 43.58 | +8.2% | +2.482 to +4.137 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.4 | 799 | +3.7% | +5.082 to +52.12 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.747 | -20.9% | -2.409 to -0.09777 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.9708 | +1692.3% | +0.502 to +1.331 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.9 | +375.0% | +0.2726 to +2.727 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 76.83 | 106 | +38.0% | +7.901 to +50.43 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*