# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.75 | 7.216 |
| node-hours | 5.027 | 5.026 | 4.504 | 3.021 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 504.5 | 525.1 | 504.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 504.5 | 486 | 354.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 617.5 | 125.9 | 586.4 | 72.97 |
| response time (ms), 95th percentile | 2452 | 171.6 | 2510 | 93.7 |
| response time (ms), 99th percentile | 3425 | 197.3 | 3535 | 128.2 |
| time over the response line (% of samples) | 25.03 | 0.004241 | 24.76 | 0 |
| failed requests (%) | 0.006817 | 0 | 0.007637 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 0 | 12.33 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 58.22 | 25.56 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.72 | 0 | 18.61 | 0.02778 |
| utilisation (used / allocatable) | 0.03427 | 0.006107 | 0.03805 | 0.008711 |
| CPU used (cores), mean | 1.645 | 0.2931 | 1.633 | 0.2522 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01219 | 0.008889 |
| CPU used with Omni's own (cores), mean | 1.645 | 0.2931 | 1.645 | 0.261 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.1 | 4198 | 724.4 | 3438 |
| HPA replicas, mean | 4.064 | 4.145 | 4.15 | 4.412 |
| pods started | 0.2222 | 0.2222 | 0.6667 | 1.667 |
| pod start wait, total (s) | 0.4444 | 0.4444 | 1 | 2.222 |
| pod start wait, mean (s) | 0.2222 | 0.2222 | 0.8333 | 1.167 |
| host CPU busy, the real machine under kind (%) | 50.74 | 14.25 | 52.21 | 15.19 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 872.8 | 1507 | 885.1 | 1504 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.985 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09722 | 1160 | 0.0787 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 | 1476 | 0.7778 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 184.4 | 1160 | 193.8 | 1158 |
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
| worker nodes in service, mean | 12 | 7.216 | -39.9% | -5.374 to -4.195 | yes: GAIN |
| node-hours | 5.026 | 3.021 | -39.9% | -2.255 to -1.753 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 504.5 | +0.0% | -1.252 to +1.32 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 354.3 | -29.8% | -169.2 to -131.3 | yes: GAIN |
| response time (ms), mean | 125.9 | 72.97 | -42.0% | -65.53 to -40.29 | yes: GAIN |
| response time (ms), 95th percentile | 171.6 | 93.7 | -45.4% | -95.35 to -60.4 | yes: GAIN |
| response time (ms), 99th percentile | 197.3 | 128.2 | -35.0% | -88.28 to -50.02 | yes: GAIN |
| time over the response line (% of samples) | 0.004241 | 0 | -100.0% | -0.01402 to +0.005539 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.56 | +25.6 (native is 0) | +24.06 to +27.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.02778 | +0.0278 (native is 0) | -0.03628 to +0.09183 | no |
| utilisation (used / allocatable) | 0.006107 | 0.008711 | +42.6% | +0.002201 to +0.003007 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2931 | 0.2522 | -14.0% | -0.04789 to -0.03405 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.008889 | +0.00889 (native is 0) | +0.007841 to +0.009937 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2931 | 0.261 | -10.9% | -0.03913 to -0.02504 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4198 | 3438 | -18.1% | -895.9 to -624.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.145 | 4.412 | +6.5% | +0.002287 to +0.5325 | yes: power given |
| pods started | 0.2222 | 1.667 | +650.0% | -0.04958 to +2.938 | no |
| pod start wait, total (s) | 0.4444 | 2.222 | +400.0% | -0.3544 to +3.91 | no |
| pod start wait, mean (s) | 0.2222 | 1.167 | +425.0% | -0.04376 to +1.933 | no |
| host CPU busy, the real machine under kind (%) | 14.25 | 15.19 | +6.7% | +0.6585 to +1.239 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1507 | 1504 | -0.1% | -6.717 to +2.273 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1158 | -0.2% | -6.561 to +2.386 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1474 | -0.1% | -6.633 to +2.411 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1158 | -0.2% | -6.561 to +2.386 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -5.22e-15 to +2.062e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.027 | 5.026 | -0.0% | -0.02062 to +0.01765 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 504.5 | -4.0% | -26.09 to -15.74 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 504.5 | -4.0% | -26.09 to -15.74 | yes: GAIN |
| response time (ms), mean | 617.5 | 125.9 | -79.6% | -756.8 to -226.6 | yes: GAIN |
| response time (ms), 95th percentile | 2452 | 171.6 | -93.0% | -3526 to -1034 | yes: GAIN |
| response time (ms), 99th percentile | 3425 | 197.3 | -94.2% | -4963 to -1493 | yes: GAIN |
| time over the response line (% of samples) | 25.03 | 0.004241 | -100.0% | -36.54 to -13.5 | yes: GAIN |
| failed requests (%) | 0.006817 | 0 | -100.0% | -0.02254 to +0.008903 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 0 | -100.0% | -17.31 to -6.688 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.72 | 0 | -100.0% | -19.47 to -9.974 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03427 | 0.006107 | -82.2% | -0.03296 to -0.02337 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.645 | 0.2931 | -82.2% | -1.582 to -1.122 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.645 | 0.2931 | -82.2% | -1.582 to -1.122 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.1 | 4198 | +423.4% | +3012 to +3781 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.064 | 4.145 | +2.0% | -0.1864 to +0.3472 | no |
| pods started | 0.2222 | 0.2222 | +0.0% | -0.7687 to +0.7687 | no |
| pod start wait, total (s) | 0.4444 | 0.4444 | +0.0% | -1.537 to +1.537 | no |
| pod start wait, mean (s) | 0.2222 | 0.2222 | +0.0% | -0.7687 to +0.7687 | no |
| host CPU busy, the real machine under kind (%) | 50.74 | 14.25 | -71.9% | -42.32 to -30.67 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 872.8 | 1507 | +72.6% | +542.7 to +725.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09722 | 1160 | +1193142.9% | +1156 to +1164 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 | 1476 | +221366.7% | +1472 to +1480 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 184.4 | 1160 | +529.1% | +884.2 to +1067 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.75 | -10.4% | -2.945 to +0.4486 | no |
| node-hours | 5.027 | 4.504 | -10.4% | -1.227 to +0.1811 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 525.1 | -0.1% | -1.86 to +1.31 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 486 | -7.5% | -92.26 to +13.36 | no |
| response time (ms), mean | 617.5 | 586.4 | -5.0% | -44.41 to -17.79 | yes: GAIN |
| response time (ms), 95th percentile | 2452 | 2510 | +2.4% | -52.48 to +168.6 | no |
| response time (ms), 99th percentile | 3425 | 3535 | +3.2% | -64.49 to +284 | no |
| time over the response line (% of samples) | 25.03 | 24.76 | -1.1% | -1.025 to +0.4931 | no |
| failed requests (%) | 0.006817 | 0.007637 | +12.0% | -0.02421 to +0.02585 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.33 | +2.8% | -0.051 to +0.7177 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.22 | +58.2 (native is 0) | +33.72 to +82.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.72 | 18.61 | +26.4% | -4.05 to +11.82 | no |
| utilisation (used / allocatable) | 0.03427 | 0.03805 | +11.0% | -0.001494 to +0.009058 | no |
| CPU used (cores), mean | 1.645 | 1.633 | -0.8% | -0.05423 to +0.0295 | no |
| Omni's own CPU (cores), mean | 0 | 0.01219 | +0.0122 (native is 0) | +0.01103 to +0.01334 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.645 | -0.0% | -0.04153 to +0.04117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.1 | 724.4 | -9.7% | -190.6 to +35.23 | no |
| HPA replicas, mean | 4.064 | 4.15 | +2.1% | -0.2919 to +0.4642 | no |
| pods started | 0.2222 | 0.6667 | +200.0% | +0.03932 to +0.8496 | yes: power given |
| pod start wait, total (s) | 0.4444 | 1 | +125.0% | -0.2237 to +1.335 | no |
| pod start wait, mean (s) | 0.2222 | 0.8333 | +275.0% | -0.1022 to +1.324 | no |
| host CPU busy, the real machine under kind (%) | 50.74 | 52.21 | +2.9% | +1.017 to +1.91 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 872.8 | 885.1 | +1.4% | +3.336 to +21.33 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.985 | -16.8% | -4.632 to +0.6015 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09722 | 0.0787 | -19.0% | -0.06686 to +0.02982 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 | 0.7778 | +16.7% | -0.1451 to +0.3673 | no |
| queue: job turnaround, submitted to done, mean (s) | 184.4 | 193.8 | +5.1% | +3.566 to +15.3 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.75 | -10.4% | -2.945 to +0.4486 | no |
| node-hours | 5.026 | 4.504 | -10.4% | -1.234 to +0.1916 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.5 | 525.1 | +4.1% | +16.39 to +24.89 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.5 | 486 | -3.7% | -75.35 to +38.27 | no |
| response time (ms), mean | 125.9 | 586.4 | +365.9% | +198.2 to +722.9 | yes: LOSS |
| response time (ms), 95th percentile | 171.6 | 2510 | +1362.7% | +1088 to +3588 | yes: LOSS |
| response time (ms), 99th percentile | 197.3 | 3535 | +1691.7% | +1613 to +5062 | yes: LOSS |
| time over the response line (% of samples) | 0.004241 | 24.76 | +583748.7% | +13.45 to +36.06 | yes: LOSS |
| failed requests (%) | 0 | 0.007637 | +0.00764 (native is 0) | -0.009973 to +0.02525 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.33 | +12.3 (native is 0) | +7.036 to +17.63 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.22 | +58.2 (native is 0) | +33.72 to +82.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 18.61 | +18.6 (native is 0) | +7.395 to +29.82 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006107 | 0.03805 | +523.1% | +0.02896 to +0.03493 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2931 | 1.633 | +457.0% | +1.105 to +1.574 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01219 | +0.0122 (native is 0) | +0.01103 to +0.01334 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2931 | 1.645 | +461.1% | +1.117 to +1.586 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4198 | 724.4 | -82.7% | -3964 to -2984 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.145 | 4.15 | +0.1% | -0.2717 to +0.2832 | no |
| pods started | 0.2222 | 0.6667 | +200.0% | -0.2335 to +1.122 | no |
| pod start wait, total (s) | 0.4444 | 1 | +125.0% | -0.539 to +1.65 | no |
| pod start wait, mean (s) | 0.2222 | 0.8333 | +275.0% | +0.01022 to +1.212 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.25 | 52.21 | +266.5% | +31.81 to +44.12 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1507 | 885.1 | -41.3% | -720.7 to -522.4 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.0787 | -100.0% | -1164 to -1156 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.7778 | -99.9% | -1479 to -1472 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 193.8 | -83.3% | -1063 to -869.9 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | -100.0% | -24 to -24 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.216 | -39.9% | -5.374 to -4.195 | yes: GAIN |
| node-hours | 5.027 | 3.021 | -39.9% | -2.247 to -1.764 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.4 | 504.5 | -4.0% | -26.17 to -15.59 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.4 | 354.3 | -32.6% | -187.8 to -154.5 | yes: GAIN |
| response time (ms), mean | 617.5 | 72.97 | -88.2% | -820.8 to -268.3 | yes: GAIN |
| response time (ms), 95th percentile | 2452 | 93.7 | -96.2% | -3619 to -1097 | yes: GAIN |
| response time (ms), 99th percentile | 3425 | 128.2 | -96.3% | -5044 to -1550 | yes: GAIN |
| time over the response line (% of samples) | 25.03 | 0 | -100.0% | -36.55 to -13.5 | yes: GAIN |
| failed requests (%) | 0.006817 | 0 | -100.0% | -0.02254 to +0.008903 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 0 | -100.0% | -17.31 to -6.688 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.56 | +25.6 (native is 0) | +24.06 to +27.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.72 | 0.02778 | -99.8% | -19.44 to -9.946 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03427 | 0.008711 | -74.6% | -0.03027 to -0.02085 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.645 | 0.2522 | -84.7% | -1.623 to -1.163 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.008889 | +0.00889 (native is 0) | +0.007841 to +0.009937 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 0.261 | -84.1% | -1.613 to -1.155 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.1 | 3438 | +328.6% | +2348 to +2924 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.064 | 4.412 | +8.6% | +0.09796 to +0.5976 | yes: power given |
| pods started | 0.2222 | 1.667 | +650.0% | +0.2843 to +2.605 | yes: power given |
| pod start wait, total (s) | 0.4444 | 2.222 | +400.0% | +0.1123 to +3.443 | yes: LOSS |
| pod start wait, mean (s) | 0.2222 | 1.167 | +425.0% | +0.1191 to +1.77 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.74 | 15.19 | -70.1% | -41.24 to -29.86 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 872.8 | 1504 | +72.4% | +539.8 to +723.5 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09722 | 1158 | +1190995.2% | +1153 to +1163 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 | 1474 | +221050.0% | +1469 to +1479 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 184.4 | 1158 | +528.0% | +881.3 to +1066 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24 (native is 0) | +24 to +24 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*