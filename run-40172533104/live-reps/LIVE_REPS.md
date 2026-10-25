# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.25 | 11.01 |
| node-hours | 5.035 | 5.024 | 4.292 | 4.615 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 524.5 | 523.2 | 525.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 524.5 | 468.2 | 494.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 389.1 | 636 | 390.2 | 708.7 |
| response time (ms), 95th percentile | 1448 | 2543 | 1655 | 2916 |
| response time (ms), 99th percentile | 2147 | 3460 | 2461 | 4112 |
| time over the response line (% of samples) | 15.9 | 20.71 | 17.87 | 24.09 |
| failed requests (%) | 0 | 0.03859 | 0 | 0.06368 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 11 | 9.2 | 12.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 90.5 | 79.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.472 | 15.24 | 11.48 | 15.94 |
| utilisation (used / allocatable) | 0.03187 | 0.03367 | 0.03707 | 0.03758 |
| CPU used (cores), mean | 1.53 | 1.616 | 1.499 | 1.657 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01284 | 0.01301 |
| CPU used with Omni's own (cores), mean | 1.53 | 1.616 | 1.512 | 1.67 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 833.3 | 802.5 | 751.3 | 729 |
| HPA replicas, mean | 4.036 | 3.876 | 4.563 | 4.619 |
| pods started | 0.1 | 0.3 | 1.2 | 1.5 |
| pod start wait, total (s) | 0.1 | 0.5 | 2.2 | 2.4 |
| pod start wait, mean (s) | 0.1 | 0.35 | 1.1 | 1.183 |
| host CPU busy, the real machine under kind (%) | 46.16 | 53 | 48.13 | 55.45 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 797.9 | 888 | 811.8 | 923.4 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.214 | 10.28 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.9792 | 0.075 | 4.967 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 3.1 | 0.6 | 39.6 |
| queue: job turnaround, submitted to done, mean (s) | 108.8 | 183.1 | 121.4 | 218.8 |
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
| worker nodes in service, mean | 12 | 11.01 | −8.2% | −2.1882 to +0.2155 | no |
| node-hours | 5.024 | 4.615 | −8.1% | −0.9149 to +0.0965 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 525.7 | +0.2% | −0.5307 to +2.9411 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 494.7 | −5.7% | −68.2229 to +8.5500 | no |
| response time (ms), mean | 636 | 708.7 | +11.4% | −14.1395 to +159.5380 | no |
| response time (ms), 95th percentile | 2543 | 2916 | +14.7% | +47.9649 to +698.5461 | yes: LOSS |
| response time (ms), 99th percentile | 3460 | 4112 | +18.8% | +247.6092 to +1055.9206 | yes: LOSS |
| time over the response line (% of samples) | 20.71 | 24.09 | +16.3% | −1.1689 to +7.9121 | no |
| failed requests (%) | 0.03859 | 0.06368 | +65.0% | −0.0334 to +0.0835 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 12.7 | +15.5% | +0.0463 to +3.3537 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.5 | +79.500 (native is 0) | +40.0690 to +118.9310 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 15.95 | +4.6% | −3.1375 to +4.5475 | no |
| utilisation (used / allocatable) | 0.03367 | 0.03758 | +11.6% | +0.0006 to +0.0072 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.616 | 1.657 | +2.6% | −0.0119 to +0.0945 | no |
| Omni's own CPU (cores), mean | 0 | 0.01301 | +0.013 (native is 0) | +0.0121 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.616 | 1.67 | +3.4% | +0.0016 to +0.1070 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.5 | 729 | −9.2% | −132.2612 to −14.7463 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.876 | 4.619 | +19.2% | +0.4613 to +1.0262 | yes: power given |
| pods started | 0.3 | 1.5 | +400.0% | +0.2583 to +2.1417 | yes: power given |
| pod start wait, total (s) | 0.5 | 2.4 | +380.0% | +0.6182 to +3.1818 | yes: LOSS |
| pod start wait, mean (s) | 0.35 | 1.183 | +238.1% | +0.2827 to +1.3840 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53 | 55.45 | +4.6% | +0.9664 to +3.9345 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 888 | 923.4 | +4.0% | +6.0168 to +64.7832 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.28 | −14.3% | −3.7365 to +0.2958 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9792 | 4.967 | +407.2% | −1.9025 to +9.8775 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.1 | 39.6 | +1177.4% | −14.5289 to +87.5289 | no |
| queue: job turnaround, submitted to done, mean (s) | 183.1 | 218.8 | +19.5% | +10.3619 to +60.9215 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.035 | 5.024 | −0.2% | −0.0268 to +0.0048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 524.5 | +0.0% | −1.4289 to +1.6700 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 524.5 | +0.0% | −1.4289 to +1.6700 | no |
| response time (ms), mean | 389.1 | 636 | +63.4% | +52.2691 to +441.5045 | yes: LOSS |
| response time (ms), 95th percentile | 1448 | 2543 | +75.6% | +221.9958 to +1967.6302 | yes: LOSS |
| response time (ms), 99th percentile | 2147 | 3460 | +61.1% | +292.1724 to +2333.5376 | yes: LOSS |
| time over the response line (% of samples) | 15.9 | 20.71 | +30.2% | +2.3159 to +7.3041 | yes: LOSS |
| failed requests (%) | 0 | 0.03859 | +0.039 (native is 0) | −0.0083 to +0.0854 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 11 | +32.5% | +1.5295 to +3.8705 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.472 | 15.24 | +60.9% | +0.4498 to +11.0869 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03187 | 0.03367 | +5.7% | +0.0001 to +0.0035 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.53 | 1.616 | +5.7% | +0.0059 to +0.1672 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.53 | 1.616 | +5.7% | +0.0059 to +0.1672 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 833.3 | 802.5 | −3.7% | −60.2613 to −1.3422 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.036 | 3.876 | −4.0% | −0.3460 to +0.0257 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.4396 to +1.2396 | no |
| pod start wait, mean (s) | 0.1 | 0.35 | +250.0% | −0.3637 to +0.8637 | no |
| host CPU busy, the real machine under kind (%) | 46.16 | 53 | +14.8% | +4.4527 to +9.2313 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 797.9 | 888 | +11.3% | +20.8145 to +159.3855 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.9792 | +1858.3% | −0.1924 to +2.0507 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 3.1 | +675.0% | −1.4580 to +6.8580 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.8 | 183.1 | +68.4% | +17.3547 to +131.3787 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.25 | −14.6% | −3.4497 to −0.0434 | yes: GAIN |
| node-hours | 5.035 | 4.292 | −14.8% | −1.4505 to −0.0367 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 523.2 | −0.2% | −2.5376 to +0.0741 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 468.2 | −10.7% | −109.4811 to −2.8741 | yes: GAIN |
| response time (ms), mean | 389.1 | 390.2 | +0.3% | −38.0133 to +40.0342 | no |
| response time (ms), 95th percentile | 1448 | 1655 | +14.3% | +8.2405 to +404.7365 | yes: LOSS |
| response time (ms), 99th percentile | 2147 | 2461 | +14.6% | −16.6494 to +643.4594 | no |
| time over the response line (% of samples) | 15.9 | 17.87 | +12.4% | −2.7966 to +6.7364 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 9.2 | +10.8% | −0.2410 to +2.0410 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 90.5 | +90.500 (native is 0) | +49.2978 to +131.7022 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.472 | 11.48 | +21.2% | +0.5748 to +3.4385 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03187 | 0.03707 | +16.3% | +0.0003 to +0.0101 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.53 | 1.499 | −2.0% | −0.0931 to +0.0319 | no |
| Omni's own CPU (cores), mean | 0 | 0.01284 | +0.013 (native is 0) | +0.0118 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.53 | 1.512 | −1.2% | −0.0800 to +0.0445 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 833.3 | 751.3 | −9.8% | −157.7132 to −6.2868 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.036 | 4.563 | +13.1% | +0.0597 to +0.9956 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.2 | +2100.0% | +0.4671 to +3.7329 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.1 | +1000.0% | +0.3470 to +1.6530 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.16 | 48.13 | +4.3% | +0.6535 to +3.2858 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 797.9 | 811.8 | +1.7% | +0.7733 to +27.0267 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.214 | −23.2% | −5.4448 to −0.1281 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.075 | +50.0% | −0.0298 to +0.0798 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.8 | 121.4 | +11.6% | −1.0803 to +26.2970 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.25 | −14.6% | −3.4497 to −0.0434 | yes: GAIN |
| node-hours | 5.024 | 4.292 | −14.6% | −1.4424 to −0.0228 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 523.2 | −0.3% | −3.1918 to +0.4873 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 468.2 | −10.7% | −109.1174 to −3.4789 | yes: GAIN |
| response time (ms), mean | 636 | 390.2 | −38.7% | −446.3708 to −45.3818 | yes: GAIN |
| response time (ms), 95th percentile | 2543 | 1655 | −34.9% | −1728.1064 to −48.5426 | yes: GAIN |
| response time (ms), 99th percentile | 3460 | 2461 | −28.9% | −1956.5480 to −42.3520 | yes: GAIN |
| time over the response line (% of samples) | 20.71 | 17.87 | −13.7% | −8.2954 to +2.6150 | no |
| failed requests (%) | 0.03859 | 0 | −100.0% | −0.0854 to +0.0083 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 9.2 | −16.4% | −3.0972 to −0.5028 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 90.5 | +90.500 (native is 0) | +49.2978 to +131.7022 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 11.48 | −24.7% | −8.6210 to +1.0976 | no |
| utilisation (used / allocatable) | 0.03367 | 0.03707 | +10.1% | −0.0026 to +0.0094 | no |
| CPU used (cores), mean | 1.616 | 1.499 | −7.2% | −0.1912 to −0.0430 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01284 | +0.013 (native is 0) | +0.0118 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.616 | 1.512 | −6.5% | −0.1783 to −0.0303 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.5 | 751.3 | −6.4% | −144.1459 to +41.7493 | no |
| HPA replicas, mean | 3.876 | 4.563 | +17.7% | +0.3315 to +1.0441 | yes: power given |
| pods started | 0.3 | 1.2 | +300.0% | −0.2410 to +2.0410 | no |
| pod start wait, total (s) | 0.5 | 2.2 | +340.0% | −0.3525 to +3.7525 | no |
| pod start wait, mean (s) | 0.35 | 1.1 | +214.3% | −0.2367 to +1.7367 | no |
| host CPU busy, the real machine under kind (%) | 53 | 48.13 | −9.2% | −7.3078 to −2.4369 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 888 | 811.8 | −8.6% | −144.2723 to −8.1277 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.214 | −23.2% | −5.4448 to −0.1281 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9792 | 0.075 | −92.3% | −1.9810 to +0.1727 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.1 | 0.6 | −80.6% | −6.4360 to +1.4360 | no |
| queue: job turnaround, submitted to done, mean (s) | 183.1 | 121.4 | −33.7% | −119.5044 to −4.0122 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.01 | −8.2% | −2.1882 to +0.2155 | no |
| node-hours | 5.035 | 4.615 | −8.3% | −0.9187 to +0.0782 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 525.7 | +0.3% | −0.3527 to +3.0042 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 494.7 | −5.7% | −68.1219 to +8.6901 | no |
| response time (ms), mean | 389.1 | 708.7 | +82.1% | +90.8275 to +548.3446 | yes: LOSS |
| response time (ms), 95th percentile | 1448 | 2916 | +101.4% | +562.7566 to +2373.3804 | yes: LOSS |
| response time (ms), 99th percentile | 2147 | 4112 | +91.5% | +786.1395 to +3143.1003 | yes: LOSS |
| time over the response line (% of samples) | 15.9 | 24.09 | +51.4% | +3.1791 to +13.1842 | yes: LOSS |
| failed requests (%) | 0 | 0.06368 | +0.064 (native is 0) | −0.0194 to +0.1468 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 12.7 | +53.0% | +2.3159 to +6.4841 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.5 | +79.500 (native is 0) | +40.0690 to +118.9310 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.472 | 15.95 | +68.3% | +1.2926 to +11.6541 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03187 | 0.03758 | +17.9% | +0.0031 to +0.0083 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.53 | 1.657 | +8.4% | +0.0323 to +0.2233 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01301 | +0.013 (native is 0) | +0.0121 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.53 | 1.67 | +9.2% | +0.0457 to +0.2359 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 833.3 | 729 | −12.5% | −149.4765 to −59.1345 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.036 | 4.619 | +14.5% | +0.2945 to +0.8729 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.6311 to +2.1689 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.4 | +2300.0% | +0.9076 to +3.6924 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.183 | +1083.3% | +0.3436 to +1.8231 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.16 | 55.45 | +20.1% | +6.1816 to +12.4033 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 797.9 | 923.4 | +15.7% | +44.9904 to +206.0096 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.28 | −14.3% | −3.7365 to +0.2958 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 4.967 | +9833.3% | −1.2281 to +11.0614 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 39.6 | +9800.0% | −11.3886 to +89.7886 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.8 | 218.8 | +101.1% | +40.7455 to +179.2711 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*