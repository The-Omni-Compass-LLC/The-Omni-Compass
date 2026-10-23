# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.42 | 11.35 |
| node-hours | 5.033 | 5.029 | 4.787 | 4.761 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 526.4 | 525.4 | 527.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 526.4 | 507.4 | 506.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 497.1 | 691.2 | 536.4 | 816.5 |
| response time (ms), 95th percentile | 1896 | 3360 | 2362 | 4022 |
| response time (ms), 99th percentile | 2767 | 5032 | 3544 | 5536 |
| time over the response line (% of samples) | 19.8 | 23.74 | 22.15 | 25.16 |
| failed requests (%) | 0 | 0.02191 | 0 | 0.3596 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 14.44 | 13.1 | 15.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 210.5 | 106 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 21.67 | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.51 | 15.7 | 14.4 | 27.62 |
| utilisation (used / allocatable) | 0.03368 | 0.03549 | 0.03614 | 0.03829 |
| CPU used (cores), mean | 1.617 | 1.703 | 1.646 | 1.733 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03847 | 0.0296 |
| CPU used with Omni's own (cores), mean | 1.617 | 1.703 | 1.684 | 1.762 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.9 | 755.4 | 743.7 | 710.3 |
| HPA replicas, mean | 4.011 | 4.047 | 5.59 | 5.252 |
| pods started | 0.1 | 0.4444 | 4.2 | 2.9 |
| pod start wait, total (s) | 0.1 | 1.333 | 9.4 | 5.1 |
| pod start wait, mean (s) | 0.1 | 0.8889 | 1.743 | 1.468 |
| host CPU busy, the real machine under kind (%) | 48.66 | 55.55 | 53.11 | 60.54 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 826.9 | 939.8 | 856.6 | 994.7 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.97 | 10.98 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.4444 | 0.08333 | 1.837 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.111 | 0.5 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 138.8 | 237.3 | 163.8 | 305.4 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.3 | -5.8% | -1.967 to +0.569 | no |
| node-hours | 5.029 | 4.739 | -5.8% | -0.8202 to +0.2404 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 527.8 | +0.3% | -0.1295 to +2.983 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 505.8 | -3.9% | -60.57 to +19.32 | no |
| response time (ms), mean | 691.2 | 879.5 | +27.2% | +58.64 to +317.9 | yes: LOSS |
| response time (ms), 95th percentile | 3360 | 4369 | +30.1% | +355.5 to +1664 | yes: LOSS |
| response time (ms), 99th percentile | 5032 | 5983 | +18.9% | +295.4 to +1606 | yes: LOSS |
| time over the response line (% of samples) | 23.74 | 26.45 | +11.4% | +1.227 to +4.182 | yes: LOSS |
| failed requests (%) | 0.02191 | 0.3995 | +1723.7% | +0.1164 to +0.6388 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.44 | 15.78 | +9.2% | +0.4739 to +2.193 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.7 | +107 (native is 0) | +82.37 to +131 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.7 | 29.44 | +87.5% | -0.8556 to +28.33 | no |
| utilisation (used / allocatable) | 0.03549 | 0.03911 | +10.2% | -0.0006132 to +0.007849 | no |
| CPU used (cores), mean | 1.703 | 1.762 | +3.5% | -0.01996 to +0.1379 | no |
| Omni's own CPU (cores), mean | 0 | 0.03073 | +0.0307 (native is 0) | +0.02424 to +0.03722 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.703 | 1.793 | +5.3% | +0.008009 to +0.1714 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.4 | 695.6 | -7.9% | -128.3 to +8.804 | no |
| HPA replicas, mean | 4.047 | 5.246 | +29.6% | +0.7434 to +1.655 | yes: power given |
| pods started | 0.4444 | 3.111 | +600.0% | +1.392 to +3.941 | yes: power given |
| pod start wait, total (s) | 1.333 | 5.556 | +316.7% | +1.798 to +6.646 | yes: LOSS |
| pod start wait, mean (s) | 0.8889 | 1.52 | +71.0% | -0.6598 to +1.923 | no |
| host CPU busy, the real machine under kind (%) | 55.55 | 61.64 | +11.0% | +4.141 to +8.034 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 939.8 | 1019 | +8.5% | +35.63 to +123.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.9 | -9.1% | -2.964 to +0.7711 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4444 | 1.995 | +349.0% | -1.871 to +4.973 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.111 | 1.667 | +50.0% | -0.002868 to +1.114 | no |
| queue: job turnaround, submitted to done, mean (s) | 237.3 | 328.8 | +38.6% | +40.44 to +142.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -3.958e-15 to +1.019e-17 | EVEN, the same (under one part in a million) |
| node-hours | 5.032 | 5.029 | -0.1% | -0.01719 to +0.012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 526.4 | +0.1% | -0.5728 to +1.951 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 526.4 | +0.1% | -0.5728 to +1.951 | no |
| response time (ms), mean | 530.6 | 691.2 | +30.3% | +86.56 to +234.7 | yes: LOSS |
| response time (ms), 95th percentile | 2057 | 3360 | +63.3% | +650.9 to +1954 | yes: LOSS |
| response time (ms), 99th percentile | 2992 | 5032 | +68.2% | +1001 to +3080 | yes: LOSS |
| time over the response line (% of samples) | 21.6 | 23.74 | +9.9% | -0.3995 to +4.677 | no |
| failed requests (%) | 0 | 0.02191 | +0.0219 (native is 0) | -0.003353 to +0.04717 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.56 | 14.44 | +36.8% | +1.132 to +6.646 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.06 | 15.7 | +20.2% | +0.2046 to +5.077 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03426 | 0.03549 | +3.6% | -2.925e-05 to +0.002486 | no |
| CPU used (cores), mean | 1.644 | 1.703 | +3.6% | -0.001404 to +0.1193 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.644 | 1.703 | +3.6% | -0.001404 to +0.1193 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 772.3 | 755.4 | -2.2% | -44.55 to +10.72 | no |
| HPA replicas, mean | 4.007 | 4.047 | +1.0% | -0.108 to +0.1889 | no |
| pods started | 0.1111 | 0.4444 | +300.0% | -0.051 to +0.7177 | no |
| pod start wait, total (s) | 0.1111 | 1.333 | +1100.0% | -0.5713 to +3.016 | no |
| pod start wait, mean (s) | 0.1111 | 0.8889 | +700.0% | -0.146 to +1.702 | no |
| host CPU busy, the real machine under kind (%) | 49.28 | 55.55 | +12.7% | +4.659 to +7.886 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 837 | 939.8 | +12.3% | +51.8 to +153.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06944 | 0.4444 | +540.0% | +0.2552 to +0.4948 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 1.111 | +100.0% | -0.002868 to +1.114 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.4 | 237.3 | +58.8% | +47.02 to +128.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.42 | -4.8% | -1.567 to +0.4137 | no |
| node-hours | 5.033 | 4.787 | -4.9% | -0.6611 to +0.1698 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 525.4 | +0.0% | -1.617 to +1.81 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 507.4 | -3.4% | -49.34 to +13.39 | no |
| response time (ms), mean | 497.1 | 536.4 | +7.9% | +3.356 to +75.38 | yes: LOSS |
| response time (ms), 95th percentile | 1896 | 2362 | +24.6% | +197 to +734.5 | yes: LOSS |
| response time (ms), 99th percentile | 2767 | 3544 | +28.1% | +432.6 to +1123 | yes: LOSS |
| time over the response line (% of samples) | 19.8 | 22.15 | +11.8% | +0.4602 to +4.232 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 13.1 | +27.2% | +0.3498 to +5.25 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 210.5 | +210 (native is 0) | +131.4 to +289.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.51 | 14.4 | +15.1% | -1.603 to +5.383 | no |
| utilisation (used / allocatable) | 0.03368 | 0.03614 | +7.3% | -0.0002644 to +0.00518 | no |
| CPU used (cores), mean | 1.617 | 1.646 | +1.8% | -0.009313 to +0.06764 | no |
| Omni's own CPU (cores), mean | 0 | 0.03847 | +0.0385 (native is 0) | +0.03569 to +0.04125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.617 | 1.684 | +4.2% | +0.02776 to +0.1075 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.9 | 743.7 | -5.4% | -84.23 to -0.2176 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.011 | 5.59 | +39.4% | +1.242 to +1.915 | yes: power given |
| pods started | 0.1 | 4.2 | +4100.0% | +2.064 to +6.136 | yes: power given |
| pod start wait, total (s) | 0.1 | 9.4 | +9300.0% | +4.032 to +14.57 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.743 | +1643.5% | +0.8869 to +2.4 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.66 | 53.11 | +9.2% | +3.483 to +5.426 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 826.9 | 856.6 | +3.6% | +10.16 to +49.24 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.97 | -8.6% | -2.74 to +0.6859 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.08333 | +17.6% | -0.03627 to +0.06127 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | -16.7% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.8 | 163.8 | +18.0% | +13.19 to +36.85 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.36 | -5.3% | -1.757 to +0.4759 | no |
| node-hours | 5.029 | 4.762 | -5.3% | -0.7407 to +0.2059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 526 | -0.1% | -2.302 to +1.545 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 505.9 | -3.9% | -55.88 to +14.95 | no |
| response time (ms), mean | 691.2 | 574.8 | -16.8% | -181.9 to -50.85 | yes: GAIN |
| response time (ms), 95th percentile | 3360 | 2550 | -24.1% | -1376 to -244 | yes: GAIN |
| response time (ms), 99th percentile | 5032 | 3832 | -23.8% | -2005 to -394.8 | yes: GAIN |
| time over the response line (% of samples) | 23.74 | 23.65 | -0.4% | -0.8814 to +0.6907 | no |
| failed requests (%) | 0.02191 | 0 | -100.0% | -0.04717 to +0.003353 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.44 | 13.22 | -8.5% | -1.969 to -0.4752 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 202.9 | +203 (native is 0) | +114.9 to +290.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.7 | 15.23 | -3.0% | -3.653 to +2.712 | no |
| utilisation (used / allocatable) | 0.03549 | 0.03692 | +4.0% | -0.002543 to +0.005407 | no |
| CPU used (cores), mean | 1.703 | 1.673 | -1.8% | -0.06636 to +0.006457 | no |
| Omni's own CPU (cores), mean | 0 | 0.039 | +0.039 (native is 0) | +0.03614 to +0.04186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.703 | 1.712 | +0.5% | -0.02543 to +0.04353 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.4 | 727.4 | -3.7% | -98.3 to +42.34 | no |
| HPA replicas, mean | 4.047 | 5.607 | +38.5% | +1.197 to +1.923 | yes: power given |
| pods started | 0.4444 | 4.667 | +950.0% | +2.16 to +6.284 | yes: power given |
| pod start wait, total (s) | 1.333 | 10.44 | +683.3% | +2.993 to +15.23 | yes: LOSS |
| pod start wait, mean (s) | 0.8889 | 1.937 | +117.9% | -0.285 to +2.382 | no |
| host CPU busy, the real machine under kind (%) | 55.55 | 53.89 | -3.0% | -3.092 to -0.2365 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 939.8 | 870 | -7.4% | -105 to -34.57 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.86 | -9.5% | -3.071 to +0.789 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4444 | 0.08333 | -81.2% | -0.4661 to -0.2561 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.111 | 0.4444 | -60.0% | -1.21 to -0.1231 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 237.3 | 176.4 | -25.7% | -93.64 to -28.19 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.35 | -5.4% | -1.766 to +0.472 | no |
| node-hours | 5.033 | 4.761 | -5.4% | -0.7364 to +0.1925 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 527.3 | +0.4% | +0.09554 to +3.733 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 506.9 | -3.5% | -53.73 to +16.76 | no |
| response time (ms), mean | 497.1 | 816.5 | +64.3% | +141.5 to +497.4 | yes: LOSS |
| response time (ms), 95th percentile | 1896 | 4022 | +112.1% | +996.6 to +3254 | yes: LOSS |
| response time (ms), 99th percentile | 2767 | 5536 | +100.1% | +1375 to +4163 | yes: LOSS |
| time over the response line (% of samples) | 19.8 | 25.16 | +27.1% | +2.879 to +7.848 | yes: LOSS |
| failed requests (%) | 0 | 0.3596 | +0.36 (native is 0) | +0.1044 to +0.6147 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 15.5 | +50.5% | +3.1 to +7.3 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106 | +106 (native is 0) | +84.63 to +127.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.51 | 27.62 | +120.8% | +1.011 to +29.21 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03368 | 0.03829 | +13.7% | +0.001404 to +0.007811 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.617 | 1.733 | +7.2% | +0.01556 to +0.216 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0296 | +0.0296 (native is 0) | +0.02335 to +0.03585 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.617 | 1.762 | +9.0% | +0.0405 to +0.2502 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.9 | 710.3 | -9.6% | -120.9 to -30.36 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.011 | 5.252 | +30.9% | +0.8032 to +1.678 | yes: power given |
| pods started | 0.1 | 2.9 | +2800.0% | +1.594 to +4.006 | yes: power given |
| pod start wait, total (s) | 0.1 | 5.1 | +5000.0% | +2.388 to +7.612 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.468 | +1368.3% | +0.9009 to +1.836 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.66 | 60.54 | +24.4% | +8.73 to +15.03 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 826.9 | 994.7 | +20.3% | +80.45 to +255.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.98 | -8.5% | -2.67 to +0.6237 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1.838 | +2494.1% | -1.281 to +4.814 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.6 | +166.7% | +0.3256 to +1.674 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 138.8 | 305.4 | +120.1% | +83.07 to +250.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*