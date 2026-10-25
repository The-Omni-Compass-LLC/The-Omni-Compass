# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.01 | 7.19 |
| node-hours | 5.028 | 5.015 | 4.612 | 3.006 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 503.5 | 525.6 | 504 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 503.5 | 494.4 | 353.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 579.2 | 127.8 | 570.3 | 74.39 |
| response time (ms), 95th percentile | 2352 | 174.7 | 2546 | 95.9 |
| response time (ms), 99th percentile | 3440 | 201.7 | 3674 | 133.7 |
| time over the response line (% of samples) | 23.28 | 0 | 23.49 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0 | 12.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 63.2 | 27 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.93 | 0 | 16.19 | 0 |
| utilisation (used / allocatable) | 0.0339 | 0.006297 | 0.03778 | 0.00904 |
| CPU used (cores), mean | 1.627 | 0.3022 | 1.655 | 0.2604 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01296 | 0.009289 |
| CPU used with Omni's own (cores), mean | 1.627 | 0.3022 | 1.668 | 0.2697 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.4 | 4080 | 717.6 | 3337 |
| HPA replicas, mean | 4.128 | 4.234 | 4.766 | 4.586 |
| pods started | 0 | 0.3 | 1.4 | 2.111 |
| pod start wait, total (s) | 0 | 0.3 | 2.1 | 3.889 |
| pod start wait, mean (s) | 0 | 0.2 | 0.9833 | 1.333 |
| host CPU busy, the real machine under kind (%) | 49.65 | 13.88 | 51.74 | 15.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 853.2 | 1502 | 869.5 | 1503 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.39 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1156 | 0.075 | 1156 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1472 | 0.6 | 1472 |
| queue: job turnaround, submitted to done, mean (s) | 166.7 | 1156 | 178.6 | 1156 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

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
| worker nodes in service, mean | 12 | 7.19 | −40.1% | −5.1907 to −4.4300 | yes: GAIN |
| node-hours | 5.015 | 3.006 | −40.1% | −2.1621 to −1.8566 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 503.6 | 504 | +0.1% | −1.1612 to +1.9353 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.6 | 353.1 | −29.9% | −161.7592 to −139.2029 | yes: GAIN |
| response time (ms), mean | 128.7 | 74.39 | −42.2% | −64.9883 to −43.5588 | yes: GAIN |
| response time (ms), 95th percentile | 175 | 95.9 | −45.2% | −94.7306 to −63.3861 | yes: GAIN |
| response time (ms), 99th percentile | 203.8 | 133.7 | −34.4% | −79.8881 to −60.2941 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 | +27.000 (native is 0) | +25.0029 to +28.9971 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| utilisation (used / allocatable) | 0.006364 | 0.00904 | +42.1% | +0.0023 to +0.0031 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3055 | 0.2604 | −14.8% | −0.0518 to −0.0383 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.009289 | +0.009 (native is 0) | +0.0082 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3055 | 0.2697 | −11.7% | −0.0421 to −0.0294 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4044 | 3337 | −17.5% | −811.7592 to −602.4916 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.218 | 4.586 | +8.7% | +0.0171 to +0.7192 | yes: power given |
| pods started | 0.3333 | 2.111 | +533.3% | +0.0686 to +3.4870 | yes: power given |
| pod start wait, total (s) | 0.3333 | 3.889 | +1066.7% | +0.1806 to +6.9305 | yes: LOSS |
| pod start wait, mean (s) | 0.2222 | 1.333 | +500.0% | +0.3136 to +1.9086 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 13.92 | 15.06 | +8.2% | +0.7734 to +1.5069 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1503 | 1503 | +0.0% | −3.5146 to +4.4035 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 1156 | +0.0% | −3.6911 to +4.0707 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 1472 | +0.0% | −3.5976 to +4.0420 | no |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 1156 | +0.0% | −3.6911 to +4.0707 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.028 | 5.015 | −0.3% | −0.0281 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 503.5 | −4.1% | −24.3971 to −18.9630 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 503.5 | −4.1% | −24.3971 to −18.9630 | yes: GAIN |
| response time (ms), mean | 579.2 | 127.8 | −77.9% | −649.6393 to −253.1680 | yes: GAIN |
| response time (ms), 95th percentile | 2352 | 174.7 | −92.6% | −3167.3069 to −1186.8241 | yes: GAIN |
| response time (ms), 99th percentile | 3440 | 201.7 | −94.1% | −4671.6010 to −1805.1610 | yes: GAIN |
| time over the response line (% of samples) | 23.28 | 0 | −100.0% | −33.6750 to −12.8861 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 0 | −100.0% | −16.3591 to −7.2409 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.93 | 0 | −100.0% | −20.3187 to −9.5480 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0339 | 0.006297 | −81.4% | −0.0308 to −0.0244 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.627 | 0.3022 | −81.4% | −1.4805 to −1.1690 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.627 | 0.3022 | −81.4% | −1.4805 to −1.1690 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.4 | 4080 | +415.6% | +2882.6217 to +3695.3047 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.128 | 4.234 | +2.6% | −0.1485 to +0.3613 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 49.65 | 13.88 | −72.0% | −40.2329 to −31.3147 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 853.2 | 1502 | +76.1% | +586.7121 to +711.2879 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1156 | +1155558.3% | +1151.5211 to +1159.5956 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1472 | +210142.9% | +1466.9960 to +1475.0040 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 166.7 | 1156 | +593.4% | +923.5336 to +1054.4331 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.01 | −8.3% | −2.3636 to +0.3740 | no |
| node-hours | 5.028 | 4.612 | −8.3% | −0.9913 to +0.1593 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 525.6 | +0.1% | −1.6162 to +2.4116 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 494.4 | −5.9% | −74.2442 to +12.6895 | no |
| response time (ms), mean | 579.2 | 570.3 | −1.5% | −59.5328 to +41.6311 | no |
| response time (ms), 95th percentile | 2352 | 2546 | +8.3% | −68.8266 to +456.8956 | no |
| response time (ms), 99th percentile | 3440 | 3674 | +6.8% | −46.3947 to +513.5037 | no |
| time over the response line (% of samples) | 23.28 | 23.49 | +0.9% | −0.8056 to +1.2179 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 | 12.2 | +3.4% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.2 | +63.200 (native is 0) | +31.4714 to +94.9286 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.93 | 16.19 | +8.4% | −2.3017 to +4.8184 | no |
| utilisation (used / allocatable) | 0.0339 | 0.03778 | +11.5% | −0.0006 to +0.0084 | no |
| CPU used (cores), mean | 1.627 | 1.655 | +1.7% | −0.0025 to +0.0587 | no |
| Omni's own CPU (cores), mean | 0 | 0.01296 | +0.013 (native is 0) | +0.0124 to +0.0136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.627 | 1.668 | +2.5% | +0.0101 to +0.0720 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.4 | 717.6 | −9.3% | −158.4456 to +10.9475 | no |
| HPA replicas, mean | 4.128 | 4.766 | +15.5% | +0.3426 to +0.9335 | yes: power given |
| pods started | 0 | 1.4 | +1.400 (native is 0) | +0.6311 to +2.1689 | yes: power given |
| pod start wait, total (s) | 0 | 2.1 | +2.100 (native is 0) | +0.5751 to +3.6249 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9833 | +0.983 (native is 0) | +0.4229 to +1.5438 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.65 | 51.74 | +4.2% | +1.1072 to +3.0542 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 853.2 | 869.5 | +1.9% | −3.9152 to +36.5152 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 10.39 | −13.4% | −3.7622 to +0.5443 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.075 | −25.0% | −0.0699 to +0.0199 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 166.7 | 178.6 | +7.1% | −2.1321 to +25.9654 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.01 | −8.3% | −2.3636 to +0.3740 | no |
| node-hours | 5.015 | 4.612 | −8.0% | −0.9803 to +0.1743 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 503.5 | 525.6 | +4.4% | +18.8841 to +25.2714 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.5 | 494.4 | −1.8% | −54.8132 to +36.6187 | no |
| response time (ms), mean | 127.8 | 570.3 | +346.2% | +236.3806 to +648.5250 | yes: LOSS |
| response time (ms), 95th percentile | 174.7 | 2546 | +1357.2% | +1304.1478 to +3438.0522 | yes: LOSS |
| response time (ms), 99th percentile | 201.7 | 3674 | +1721.0% | +1938.6768 to +5005.1942 | yes: LOSS |
| time over the response line (% of samples) | 0 | 23.49 | +23.487 (native is 0) | +13.5111 to +33.4623 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.2 | +12.200 (native is 0) | +7.5058 to +16.8942 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.2 | +63.200 (native is 0) | +31.4714 to +94.9286 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 16.19 | +16.192 (native is 0) | +11.3575 to +21.0258 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006297 | 0.03778 | +500.0% | +0.0296 to +0.0334 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3022 | 1.655 | +447.6% | +1.1906 to +1.5151 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01296 | +0.013 (native is 0) | +0.0124 to +0.0136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3022 | 1.668 | +451.9% | +1.2036 to +1.5280 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4080 | 717.6 | −82.4% | −3850.2627 to −2875.1618 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.234 | 4.766 | +12.6% | +0.1957 to +0.8677 | yes: power given |
| pods started | 0.3 | 1.4 | +366.7% | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.1 | +600.0% | +0.0872 to +3.5128 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.9833 | +391.7% | +0.1065 to +1.4602 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 13.88 | 51.74 | +272.7% | +33.1927 to +42.5163 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1502 | 869.5 | −42.1% | −705.4257 to −559.9743 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 0.075 | −100.0% | −1159.6399 to −1151.5268 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 0.6 | −100.0% | −1475.2634 to −1466.9366 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 178.6 | −84.5% | −1048.3341 to −905.7993 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.19 | −40.1% | −5.1907 to −4.4300 | yes: GAIN |
| node-hours | 5.025 | 3.006 | −40.2% | −2.1716 to −1.8671 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.3 | 504 | −4.1% | −24.4111 to −18.3433 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.3 | 353.1 | −32.8% | −182.4547 to −162.0359 | yes: GAIN |
| response time (ms), mean | 618.5 | 74.39 | −88.0% | −757.5808 to −330.5969 | yes: GAIN |
| response time (ms), 95th percentile | 2550 | 95.9 | −96.2% | −3476.0499 to −1431.7001 | yes: GAIN |
| response time (ms), 99th percentile | 3720 | 133.7 | −96.4% | −5056.5944 to −2115.4303 | yes: GAIN |
| time over the response line (% of samples) | 25.09 | 0 | −100.0% | −35.9800 to −14.2035 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.89 | 0 | −100.0% | −17.0802 to −6.6976 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 | +27.000 (native is 0) | +25.0029 to +28.9971 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.83 | 0 | −100.0% | −21.5162 to −10.1431 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03441 | 0.00904 | −73.7% | −0.0286 to −0.0221 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.652 | 0.2604 | −84.2% | −1.5615 to −1.2215 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.009289 | +0.009 (native is 0) | +0.0082 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.652 | 0.2697 | −83.7% | −1.5511 to −1.2133 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.8 | 3337 | +327.4% | +2179.4074 to +2932.7109 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.129 | 4.586 | +11.1% | +0.1364 to +0.7790 | yes: power given |
| pods started | 0 | 2.111 | +2.111 (native is 0) | +0.6504 to +3.5718 | yes: power given |
| pod start wait, total (s) | 0 | 3.889 | +3.889 (native is 0) | +0.6631 to +7.1146 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.333 | +1.333 (native is 0) | +0.6464 to +2.0203 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.28 | 15.06 | −70.1% | −39.8219 to −30.6286 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 865.7 | 1503 | +73.6% | +572.7539 to +701.9128 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1019 | 1156 | +1135118.2% | +1154.0694 to +1158.2083 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 | 1472 | +220750.0% | +1469.5970 to +1473.7364 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 179.4 | 1156 | +544.7% | +908.4893 to +1045.2885 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*