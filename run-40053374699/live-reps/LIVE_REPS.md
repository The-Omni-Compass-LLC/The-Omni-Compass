# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.042 | 5.981 |
| node-hours | 2.513 | 2.515 | 2.116 | 2.504 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.8 | 271.3 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 271.8 | 241.2 | 271 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 240.7 | 129.6 | 221.5 | 97.23 |
| response time (ms), 95th percentile | 712.3 | 221.6 | 809.7 | 210.1 |
| response time (ms), 99th percentile | 1022 | 322.3 | 1165 | 318.5 |
| time over the response line (% of samples) | 11.96 | 0.1692 | 12.84 | 0.1554 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 0 | 8.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 48.8 | 13.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.663 | 1046 | 9.012 | 1043 |
| utilisation (used / allocatable) | 0.0562 | 0.05882 | 0.06747 | 0.05944 |
| CPU used (cores), mean | 1.349 | 1.412 | 1.334 | 1.422 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01626 | 0.01241 |
| CPU used with Omni's own (cores), mean | 1.349 | 1.412 | 1.35 | 1.435 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.5 | 460.1 | 430.6 | 455.6 |
| HPA replicas, mean | 1.967 | 2.069 | 2.358 | 2.092 |
| pods started | 0 | 0.4 | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.8 | 0 | 0.1 |
| pod start wait, mean (s) | 0 | 0.55 | 0 | 0.1 |
| host CPU busy, the real machine under kind (%) | 38.21 | 43.54 | 39.13 | 44.45 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 739.2 | 1422 | 744.4 | 1426 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.356 | 5.734 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 129.5 | 0.05833 | 129.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 602.9 | 0.4 | 594.3 |
| queue: job turnaround, submitted to done, mean (s) | 45.49 | 789.9 | 51.52 | 790.1 |
| queue: jobs unfinished at the window's end | 0 | 9.8 | 0 | 9 |

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
| worker nodes in service, mean | 6 | 5.981 | -0.3% | -0.04641 to +0.007715 | no |
| node-hours | 2.515 | 2.504 | -0.5% | -0.02287 to -1.876e-05 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.6 | -0.1% | -1.43 to +0.9143 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271 | -0.3% | -2.004 to +0.2716 | no |
| response time (ms), mean | 129.6 | 97.23 | -25.0% | -39.67 to -24.99 | yes: GAIN |
| response time (ms), 95th percentile | 221.6 | 210.1 | -5.2% | -19.6 to -3.482 | yes: GAIN |
| response time (ms), 99th percentile | 322.3 | 318.5 | -1.2% | -18.91 to +11.34 | no |
| time over the response line (% of samples) | 0.1692 | 0.1554 | -8.2% | -0.1714 to +0.1436 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.9 | +13.9 (native is 0) | +10.54 to +17.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1046 | 1043 | -0.2% | -71.68 to +66.47 | no |
| utilisation (used / allocatable) | 0.05882 | 0.05944 | +1.1% | -0.0005221 to +0.001763 | no |
| CPU used (cores), mean | 1.412 | 1.422 | +0.7% | -0.01421 to +0.03519 | no |
| Omni's own CPU (cores), mean | 0 | 0.01241 | +0.0124 (native is 0) | +0.01151 to +0.01331 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.412 | 1.435 | +1.6% | -0.001748 to +0.04755 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.1 | 455.6 | -1.0% | -12.7 to +3.625 | no |
| HPA replicas, mean | 2.069 | 2.092 | +1.1% | -0.08211 to +0.1274 | no |
| pods started | 0.4 | 0.1 | -75.0% | -0.8889 to +0.2889 | no |
| pod start wait, total (s) | 0.8 | 0.1 | -87.5% | -1.918 to +0.5181 | no |
| pod start wait, mean (s) | 0.55 | 0.1 | -81.8% | -1.212 to +0.3124 | no |
| host CPU busy, the real machine under kind (%) | 43.54 | 44.45 | +2.1% | -0.1399 to +1.948 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1422 | 1426 | +0.2% | -5.705 to +12.71 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.734 | -4.4% | -0.6487 to +0.1164 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 129.5 | 129.6 | +0.0% | -43.92 to +43.98 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 602.9 | 594.3 | -1.4% | -159.5 to +142.3 | no |
| queue: job turnaround, submitted to done, mean (s) | 789.9 | 790.1 | +0.0% | -60.57 to +60.84 | no |
| queue: jobs unfinished at the window's end | 9.8 | 9 | -8.2% | -3.203 to +1.603 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.938e-15 to +5.17e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.515 | +0.1% | -0.003168 to +0.008835 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.8 | +0.4% | -0.2745 to +2.484 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 271.8 | +0.4% | -0.2745 to +2.484 | no |
| response time (ms), mean | 240.7 | 129.6 | -46.2% | -165.9 to -56.27 | yes: GAIN |
| response time (ms), 95th percentile | 712.3 | 221.6 | -68.9% | -733.3 to -248.2 | yes: GAIN |
| response time (ms), 99th percentile | 1022 | 322.3 | -68.5% | -1040 to -360.3 | yes: GAIN |
| time over the response line (% of samples) | 11.96 | 0.1692 | -98.6% | -19.31 to -4.283 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 0 | -100.0% | -12.23 to -4.367 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.663 | 1046 | +11968.5% | +769.1 to +1305 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0562 | 0.05882 | +4.7% | -0.001068 to +0.006295 | no |
| CPU used (cores), mean | 1.349 | 1.412 | +4.7% | -0.02562 to +0.1511 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.349 | 1.412 | +4.7% | -0.02562 to +0.1511 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.5 | 460.1 | -5.0% | -55.19 to +6.391 | no |
| HPA replicas, mean | 1.967 | 2.069 | +5.2% | -0.03678 to +0.2411 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | -0.3583 to +1.958 | no |
| pod start wait, mean (s) | 0 | 0.55 | +0.55 (native is 0) | -0.1338 to +1.234 | no |
| host CPU busy, the real machine under kind (%) | 38.21 | 43.54 | +14.0% | +3.451 to +7.214 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.2 | 1422 | +92.4% | +593.8 to +772.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 129.5 | +282527.3% | +98.76 to +160.2 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 602.9 | +301350.0% | +504.6 to +700.8 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 45.49 | 789.9 | +1636.4% | +582.3 to +906.5 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.8 | +9.8 (native is 0) | +3.395 to +16.21 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.042 | -16.0% | -1.751 to -0.1647 | yes: GAIN |
| node-hours | 2.513 | 2.116 | -15.8% | -0.7314 to -0.06147 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.3 | +0.2% | -0.5524 to +1.61 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 241.2 | -10.9% | -55.09 to -4.014 | yes: GAIN |
| response time (ms), mean | 240.7 | 221.5 | -8.0% | -32.04 to -6.351 | yes: GAIN |
| response time (ms), 95th percentile | 712.3 | 809.7 | +13.7% | +19.33 to +175.4 | yes: LOSS |
| response time (ms), 99th percentile | 1022 | 1165 | +14.0% | +37.52 to +248.1 | yes: LOSS |
| time over the response line (% of samples) | 11.96 | 12.84 | +7.3% | -0.2211 to +1.97 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.7 | +4.8% | -0.2911 to +1.091 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.8 | +48.8 (native is 0) | +30.62 to +66.98 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.663 | 9.012 | +4.0% | -1.364 to +2.061 | no |
| utilisation (used / allocatable) | 0.0562 | 0.06747 | +20.0% | +0.002147 to +0.02038 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.349 | 1.334 | -1.1% | -0.06135 to +0.0316 | no |
| Omni's own CPU (cores), mean | 0 | 0.01626 | +0.0163 (native is 0) | +0.01485 to +0.01767 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.349 | 1.35 | +0.1% | -0.04607 to +0.04884 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.5 | 430.6 | -11.1% | -97.32 to -10.47 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.967 | 2.358 | +19.9% | +0.2212 to +0.5602 | yes: power given |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 38.21 | 39.13 | +2.4% | +0.3832 to +1.456 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.2 | 744.4 | +0.7% | +0.06615 to +10.33 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.356 | -27.4% | -2.946 to -0.3413 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05833 | +27.3% | -0.02481 to +0.04981 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 45.49 | 51.53 | +13.3% | +1.295 to +10.77 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.042 | -16.0% | -1.751 to -0.1647 | yes: GAIN |
| node-hours | 2.515 | 2.116 | -15.9% | -0.7353 to -0.06326 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.3 | -0.2% | -2.684 to +1.532 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 241.2 | -11.3% | -57.24 to -4.076 | yes: GAIN |
| response time (ms), mean | 129.6 | 221.5 | +70.9% | +33.6 to +150.2 | yes: LOSS |
| response time (ms), 95th percentile | 221.6 | 809.7 | +265.4% | +292.8 to +883.4 | yes: LOSS |
| response time (ms), 99th percentile | 322.3 | 1165 | +261.5% | +442.9 to +1242 | yes: LOSS |
| time over the response line (% of samples) | 0.1692 | 12.84 | +7485.7% | +4.783 to +20.55 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.7 | +8.7 (native is 0) | +4.681 to +12.72 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.8 | +48.8 (native is 0) | +30.62 to +66.98 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1046 | 9.012 | -99.1% | -1304 to -769.1 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05882 | 0.06747 | +14.7% | +0.00167 to +0.01563 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.412 | 1.334 | -5.5% | -0.1975 to +0.04228 | no |
| Omni's own CPU (cores), mean | 0 | 0.01626 | +0.0163 (native is 0) | +0.01485 to +0.01767 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.412 | 1.35 | -4.3% | -0.1821 to +0.05937 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.1 | 430.6 | -6.4% | -56.12 to -2.876 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.069 | 2.358 | +13.9% | +0.09049 to +0.4866 | yes: power given |
| pods started | 0.4 | 0 | -100.0% | -0.9001 to +0.1001 | no |
| pod start wait, total (s) | 0.8 | 0 | -100.0% | -1.958 to +0.3583 | no |
| pod start wait, mean (s) | 0.55 | 0 | -100.0% | -1.234 to +0.1338 | no |
| host CPU busy, the real machine under kind (%) | 43.54 | 39.13 | -10.1% | -6.439 to -2.387 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1422 | 744.4 | -47.7% | -765.6 to -590.6 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.319 | -61.4% | -4.302 to -3.061 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 129.5 | 0.05833 | -100.0% | -160.2 to -98.77 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 602.9 | 0.4 | -99.9% | -700.4 to -504.6 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 789.9 | 51.52 | -93.5% | -896.5 to -580.3 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.8 | 0 | -100.0% | -16.21 to -3.395 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.981 | -0.3% | -0.04641 to +0.007715 | no |
| node-hours | 2.513 | 2.504 | -0.3% | -0.02009 to +0.002871 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.6 | +0.3% | -0.8876 to +2.582 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 271 | +0.1% | -1.263 to +1.74 | no |
| response time (ms), mean | 240.7 | 97.23 | -59.6% | -204.3 to -82.54 | yes: GAIN |
| response time (ms), 95th percentile | 712.3 | 210.1 | -70.5% | -747.5 to -257 | yes: GAIN |
| response time (ms), 99th percentile | 1022 | 318.5 | -68.8% | -1039 to -368.1 | yes: GAIN |
| time over the response line (% of samples) | 11.96 | 0.1554 | -98.7% | -19.36 to -4.251 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 0 | -100.0% | -12.23 to -4.367 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.9 | +13.9 (native is 0) | +10.54 to +17.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.663 | 1043 | +11938.4% | +806 to +1263 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0562 | 0.05944 | +5.8% | -0.0003982 to +0.006867 | no |
| CPU used (cores), mean | 1.349 | 1.422 | +5.4% | -0.01026 to +0.1567 | no |
| Omni's own CPU (cores), mean | 0 | 0.01241 | +0.0124 (native is 0) | +0.01151 to +0.01331 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.349 | 1.435 | +6.3% | +0.002774 to +0.1685 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.5 | 455.6 | -6.0% | -59.54 to +1.671 | no |
| HPA replicas, mean | 1.967 | 2.092 | +6.3% | -0.04737 to +0.297 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 38.21 | 44.45 | +16.3% | +4.306 to +8.166 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 739.2 | 1426 | +92.9% | +603.3 to +770.3 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.734 | -4.4% | -0.6487 to +0.1164 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 129.6 | +282590.9% | +85.56 to +173.5 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 594.3 | +297050.0% | +431.8 to +756.4 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 45.49 | 790.1 | +1636.7% | +599.2 to +889.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9 | +9 (native is 0) | +3.317 to +14.68 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*