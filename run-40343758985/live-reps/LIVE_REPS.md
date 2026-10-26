# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.589 | 4.672 |
| node-hours | 2.513 | 2.513 | 1.924 | 1.958 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 269.6 | 269.8 | 269.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 269.6 | 225.5 | 227.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 210.5 | 223.6 | 190.4 | 198 |
| response time (ms), 95th percentile | 611.8 | 667.6 | 683.8 | 710.9 |
| response time (ms), 99th percentile | 881.7 | 964.8 | 956.4 | 1017 |
| time over the response line (% of samples) | 9.139 | 9.604 | 9.34 | 9.826 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5.9 | 6 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 51.3 | 63.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.578 | 7.158 | 8.765 | 7.487 |
| utilisation (used / allocatable) | 0.05359 | 0.05287 | 0.06944 | 0.06599 |
| CPU used (cores), mean | 1.286 | 1.269 | 1.25 | 1.225 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01482 | 0.0163 |
| CPU used with Omni's own (cores), mean | 1.286 | 1.269 | 1.264 | 1.241 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.8 | 520 | 432 | 449.1 |
| HPA replicas, mean | 1.999 | 1.954 | 2.088 | 1.976 |
| pods started | 0 | 0.1 | 0.3 | 0.2 |
| pod start wait, total (s) | 0 | 0.1 | 0.5 | 0.3 |
| pod start wait, mean (s) | 0 | 0.1 | 0.5 | 0.3 |
| host CPU busy, the real machine under kind (%) | 36.42 | 37.03 | 37.28 | 38.04 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 739.1 | 743.3 | 742.1 | 746 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.695 | 3.814 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1167 | 0.05833 | 0.1375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | 0.4 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 45.1 | 49.46 | 48.68 | 51.69 |
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
| worker nodes in service, mean | 6 | 4.672 | −22.1% | −2.1347 to −0.5205 | yes: GAIN |
| node-hours | 2.513 | 1.958 | −22.1% | −0.8966 to −0.2135 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.2 | −0.1% | −1.6101 to +0.8607 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 227.5 | −15.6% | −68.3632 to −15.7945 | yes: GAIN |
| response time (ms), mean | 223.6 | 198 | −11.5% | −34.6074 to −16.6601 | yes: GAIN |
| response time (ms), 95th percentile | 667.6 | 710.9 | +6.5% | +7.3360 to +79.4390 | yes: LOSS |
| response time (ms), 99th percentile | 964.8 | 1017 | +5.5% | −28.3118 to +133.4906 | no |
| time over the response line (% of samples) | 9.604 | 9.826 | +2.3% | −0.5606 to +1.0051 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5.8 | −1.7% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.2 | +63.200 (native is 0) | +38.6659 to +87.7341 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.158 | 7.487 | +4.6% | −1.2121 to +1.8687 | no |
| utilisation (used / allocatable) | 0.05287 | 0.06599 | +24.8% | +0.0049 to +0.0214 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.269 | 1.225 | −3.5% | −0.0979 to +0.0097 | no |
| Omni's own CPU (cores), mean | 0 | 0.0163 | +0.016 (native is 0) | +0.0147 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.269 | 1.241 | −2.2% | −0.0827 to +0.0271 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 520 | 449.1 | −13.6% | −116.6456 to −25.1057 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.954 | 1.976 | +1.1% | −0.1664 to +0.2106 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, mean (s) | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| host CPU busy, the real machine under kind (%) | 37.03 | 38.04 | +2.7% | +0.6418 to +1.3940 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 743.3 | 746 | +0.4% | −1.5526 to +6.9526 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.814 | −36.4% | −3.4120 to −0.9594 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 0.1375 | +17.9% | −0.0283 to +0.0700 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 49.46 | 51.69 | +4.5% | −0.8914 to +5.3498 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.513 | +0.0% | −0.0070 to +0.0073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 269.6 | −0.1% | −1.0152 to +0.6159 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 269.6 | −0.1% | −1.0152 to +0.6159 | no |
| response time (ms), mean | 210.5 | 223.6 | +6.3% | +0.6002 to +25.7206 | yes: LOSS |
| response time (ms), 95th percentile | 611.8 | 667.6 | +9.1% | −10.7293 to +122.2043 | no |
| response time (ms), 99th percentile | 881.7 | 964.8 | +9.4% | −14.6248 to +180.6618 | no |
| time over the response line (% of samples) | 9.139 | 9.604 | +5.1% | −0.2626 to +1.1930 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5.9 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.578 | 7.158 | −16.6% | −3.1407 to +0.3007 | no |
| utilisation (used / allocatable) | 0.05359 | 0.05287 | −1.3% | −0.0019 to +0.0005 | no |
| CPU used (cores), mean | 1.286 | 1.269 | −1.3% | −0.0455 to +0.0111 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.286 | 1.269 | −1.3% | −0.0455 to +0.0111 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.8 | 520 | +1.8% | −3.5981 to +21.9891 | no |
| HPA replicas, mean | 1.999 | 1.954 | −2.3% | −0.1504 to +0.0604 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 36.42 | 37.03 | +1.7% | +0.2713 to +0.9369 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 739.1 | 743.3 | +0.6% | −1.2351 to +9.6351 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1167 | +180.0% | +0.0228 to +0.1272 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | +200.0% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 45.1 | 49.46 | +9.7% | −0.1850 to +8.9183 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.589 | −23.5% | −2.2784 to −0.5436 | yes: GAIN |
| node-hours | 2.513 | 1.924 | −23.4% | −0.9539 to −0.2222 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 269.8 | +0.0% | −1.2245 to +1.2286 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 225.5 | −16.4% | −72.2697 to −16.2845 | yes: GAIN |
| response time (ms), mean | 210.5 | 190.4 | −9.5% | −28.1742 to −11.8418 | yes: GAIN |
| response time (ms), 95th percentile | 611.8 | 683.8 | +11.8% | +28.8512 to +115.1498 | yes: LOSS |
| response time (ms), 99th percentile | 881.7 | 956.4 | +8.5% | +17.1708 to +132.1108 | yes: LOSS |
| time over the response line (% of samples) | 9.139 | 9.34 | +2.2% | −0.2687 to +0.6710 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 6 | +1.7% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.3 | +51.300 (native is 0) | +32.7969 to +69.8031 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.578 | 8.765 | +2.2% | −1.4789 to +1.8522 | no |
| utilisation (used / allocatable) | 0.05359 | 0.06944 | +29.6% | +0.0061 to +0.0256 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.286 | 1.25 | −2.8% | −0.0805 to +0.0075 | no |
| Omni's own CPU (cores), mean | 0 | 0.01482 | +0.015 (native is 0) | +0.0136 to +0.0160 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.286 | 1.264 | −1.7% | −0.0665 to +0.0231 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.8 | 432 | −15.4% | −127.0692 to −30.4133 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.088 | +4.5% | −0.0973 to +0.2763 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| host CPU busy, the real machine under kind (%) | 36.42 | 37.28 | +2.4% | +0.3258 to +1.3942 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 739.1 | 742.1 | +0.4% | +0.0604 to +5.9396 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.695 | −38.4% | −3.6637 to −0.9469 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05833 | +40.0% | −0.0085 to +0.0418 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 45.1 | 48.68 | +7.9% | −0.2523 to +7.4189 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.589 | −23.5% | −2.2784 to −0.5436 | yes: GAIN |
| node-hours | 2.513 | 1.924 | −23.4% | −0.9572 to −0.2193 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.8 | +0.1% | −0.9328 to +1.3361 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 225.5 | −16.4% | −72.0531 to −16.1019 | yes: GAIN |
| response time (ms), mean | 223.6 | 190.4 | −14.8% | −48.5649 to −17.7720 | yes: GAIN |
| response time (ms), 95th percentile | 667.6 | 683.8 | +2.4% | −25.9548 to +58.4808 | no |
| response time (ms), 99th percentile | 964.8 | 956.4 | −0.9% | −58.2356 to +41.4802 | no |
| time over the response line (% of samples) | 9.604 | 9.34 | −2.7% | −1.0974 to +0.5693 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 6 | +1.7% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.3 | +51.300 (native is 0) | +32.7969 to +69.8031 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.158 | 8.765 | +22.4% | +0.1148 to +3.0985 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05287 | 0.06944 | +31.3% | +0.0058 to +0.0273 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.269 | 1.25 | −1.5% | −0.0568 to +0.0181 | no |
| Omni's own CPU (cores), mean | 0 | 0.01482 | +0.015 (native is 0) | +0.0136 to +0.0160 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.269 | 1.264 | −0.4% | −0.0423 to +0.0334 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 520 | 432 | −16.9% | −145.6391 to −30.2344 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.954 | 2.088 | +6.9% | −0.0234 to +0.2924 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 37.03 | 37.28 | +0.7% | −0.3375 to +0.8493 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 743.3 | 742.1 | −0.2% | −4.8442 to +2.4442 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.695 | −38.4% | −3.6637 to −0.9469 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 0.05833 | −50.0% | −0.0986 to −0.0181 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 49.46 | 48.68 | −1.6% | −1.8722 to +0.3055 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.672 | −22.1% | −2.1347 to −0.5205 | yes: GAIN |
| node-hours | 2.513 | 1.958 | −22.1% | −0.8934 to −0.2163 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 269.2 | −0.2% | −1.6940 to +0.5454 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 227.5 | −15.7% | −68.5650 to −15.9919 | yes: GAIN |
| response time (ms), mean | 210.5 | 198 | −5.9% | −23.7409 to −1.2058 | yes: GAIN |
| response time (ms), 95th percentile | 611.8 | 710.9 | +16.2% | +20.7617 to +177.4883 | yes: LOSS |
| response time (ms), 99th percentile | 881.7 | 1017 | +15.4% | −8.1434 to +279.3592 | no |
| time over the response line (% of samples) | 9.139 | 9.826 | +7.5% | −0.1835 to +1.5583 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5.8 | −1.7% | −0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.2 | +63.200 (native is 0) | +38.6659 to +87.7341 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.578 | 7.487 | −12.7% | −2.7441 to +0.5608 | no |
| utilisation (used / allocatable) | 0.05359 | 0.06599 | +23.1% | +0.0051 to +0.0197 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.286 | 1.225 | −4.8% | −0.1310 to +0.0083 | no |
| Omni's own CPU (cores), mean | 0 | 0.0163 | +0.016 (native is 0) | +0.0147 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.286 | 1.241 | −3.5% | −0.1158 to +0.0258 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.8 | 449.1 | −12.1% | −99.1951 to −24.1652 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 1.976 | −1.1% | −0.2049 to +0.1590 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 36.42 | 38.04 | +4.5% | +1.2175 to +2.0264 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 739.1 | 746 | +0.9% | −0.6132 to +14.4132 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.814 | −36.4% | −3.4120 to −0.9594 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.1375 | +230.0% | +0.0069 to +0.1847 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.6 | +200.0% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 45.1 | 51.69 | +14.6% | +0.1780 to +13.0136 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*