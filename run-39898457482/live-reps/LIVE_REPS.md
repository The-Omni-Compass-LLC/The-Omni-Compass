# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.98 | 12 |
| node-hours | 5.034 | 5.028 | 5.016 | 5.022 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 529.4 | 527.6 | 529.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 529.4 | 526.8 | 529.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 661.7 | 1076 | 758.9 | 1299 |
| response time (ms), 95th percentile | 2737 | 4578 | 3512 | 5512 |
| response time (ms), 99th percentile | 3831 | 6414 | 5057 | 7396 |
| time over the response line (% of samples) | 29.25 | 36.3 | 30.45 | 40.7 |
| failed requests (%) | 0 | 0.02937 | 0.006472 | 0.1774 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 17.7 | 15.7 | 19 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 151.2 | 139.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 5 | 15 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 21.66 | 16.77 | 32.96 |
| utilisation (used / allocatable) | 0.03597 | 0.03987 | 0.03764 | 0.04062 |
| CPU used (cores), mean | 1.727 | 1.914 | 1.804 | 1.949 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0409 | 0.04341 |
| CPU used with Omni's own (cores), mean | 1.727 | 1.914 | 1.845 | 1.993 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.3 | 665.1 | 701.4 | 652.4 |
| HPA replicas, mean | 4.147 | 4.02 | 5.574 | 5.205 |
| pods started | 0 | 0 | 4.9 | 4.3 |
| pod start wait, total (s) | 0 | 0 | 12.1 | 10.6 |
| pod start wait, mean (s) | 0 | 0 | 2.468 | 2.354 |
| host CPU busy, the real machine under kind (%) | 52.16 | 61.74 | 57.77 | 67.79 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 875.5 | 1051 | 933 | 1124 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 11.95 | 11.99 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 14.36 | 0.1125 | 17.13 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 134 | 0.8 | 97.6 |
| queue: job turnaround, submitted to done, mean (s) | 189.5 | 316.6 | 233.1 | 402 |
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
| worker nodes in service, mean | 12 | 12 | -0.0% | -0.0138 to +0.005338 | no |
| node-hours | 5.028 | 5.022 | -0.1% | -0.02558 to +0.01269 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 529.4 | 529.5 | +0.0% | -2.452 to +2.799 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 529.4 | 529.4 | +0.0% | -2.538 to +2.618 | no |
| response time (ms), mean | 1076 | 1299 | +20.7% | +135.1 to +311 | yes: LOSS |
| response time (ms), 95th percentile | 4578 | 5512 | +20.4% | +615.6 to +1252 | yes: LOSS |
| response time (ms), 99th percentile | 6414 | 7396 | +15.3% | +502.3 to +1460 | yes: LOSS |
| time over the response line (% of samples) | 36.3 | 40.7 | +12.1% | +1.402 to +7.398 | yes: LOSS |
| failed requests (%) | 0.02937 | 0.1774 | +504.0% | -0.03499 to +0.3311 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.7 | 19 | +7.3% | +0.8172 to +1.783 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 139.1 | +139 (native is 0) | +129.3 to +148.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.66 | 32.96 | +52.2% | -0.002944 to +22.6 | no |
| utilisation (used / allocatable) | 0.03987 | 0.04062 | +1.9% | -0.001005 to +0.002507 | no |
| CPU used (cores), mean | 1.914 | 1.949 | +1.9% | -0.0483 to +0.1192 | no |
| Omni's own CPU (cores), mean | 0 | 0.04341 | +0.0434 (native is 0) | +0.04107 to +0.04575 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.914 | 1.993 | +4.1% | -0.004261 to +0.162 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.1 | 652.4 | -1.9% | -43.27 to +17.87 | no |
| HPA replicas, mean | 4.02 | 5.205 | +29.5% | +0.7314 to +1.639 | yes: power given |
| pods started | 0 | 4.3 | +4.3 (native is 0) | +2.828 to +5.772 | yes: power given |
| pod start wait, total (s) | 0 | 10.6 | +10.6 (native is 0) | +5.901 to +15.3 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.354 | +2.35 (native is 0) | +2.035 to +2.674 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.74 | 67.79 | +9.8% | +5.392 to +6.699 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1051 | 1124 | +6.9% | +59.58 to +85.62 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.99 | -0.1% | -0.03182 to +0.01231 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 14.36 | 17.13 | +19.3% | -9.58 to +15.11 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 134 | 97.6 | -27.2% | -111.5 to +38.67 | no |
| queue: job turnaround, submitted to done, mean (s) | 316.6 | 402 | +27.0% | +67.34 to +103.5 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | +2.128e-16 to +3.695e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.034 | 5.028 | -0.1% | -0.02083 to +0.01017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 529.4 | +0.4% | +0.4943 to +3.966 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 529.4 | +0.4% | +0.4943 to +3.966 | yes: power given |
| response time (ms), mean | 661.7 | 1076 | +62.6% | +313.7 to +515.2 | yes: LOSS |
| response time (ms), 95th percentile | 2737 | 4578 | +67.2% | +1415 to +2267 | yes: LOSS |
| response time (ms), 99th percentile | 3831 | 6414 | +67.5% | +2009 to +3159 | yes: LOSS |
| time over the response line (% of samples) | 29.25 | 36.3 | +24.1% | +5.436 to +8.651 | yes: LOSS |
| failed requests (%) | 0 | 0.02937 | +0.0294 (native is 0) | +0.002195 to +0.05655 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 17.7 | +26.4% | +2.579 to +4.821 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 21.66 | +51.2% | +3.935 to +10.74 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03597 | 0.03987 | +10.8% | +0.002944 to +0.004856 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.727 | 1.914 | +10.8% | +0.1413 to +0.2331 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.727 | 1.914 | +10.8% | +0.1413 to +0.2331 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.3 | 665.1 | -8.9% | -80.16 to -50.26 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.147 | 4.02 | -3.1% | -0.3305 to +0.0749 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 52.16 | 61.74 | +18.4% | +8.275 to +10.89 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 875.5 | 1051 | +20.1% | +136.8 to +214.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 14.36 | +21443.8% | +6.121 to +22.47 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 134 | +26700.0% | +48.36 to +218.6 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 189.5 | 316.6 | +67.1% | +98.54 to +155.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.98 | -0.2% | -0.07618 to +0.02947 | no |
| node-hours | 5.034 | 5.016 | -0.3% | -0.04713 to +0.0123 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 527.6 | +0.1% | -1.292 to +2.173 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 526.8 | -0.1% | -3.132 to +2.55 | no |
| response time (ms), mean | 661.7 | 758.9 | +14.7% | +54.02 to +140.3 | yes: LOSS |
| response time (ms), 95th percentile | 2737 | 3512 | +28.3% | +542.7 to +1007 | yes: LOSS |
| response time (ms), 99th percentile | 3831 | 5057 | +32.0% | +856.4 to +1597 | yes: LOSS |
| time over the response line (% of samples) | 29.25 | 30.45 | +4.1% | -0.6675 to +3.068 | no |
| failed requests (%) | 0 | 0.006472 | +0.00647 (native is 0) | -0.008168 to +0.02111 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 15.7 | +12.1% | +0.3491 to +3.051 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 151.2 | +151 (native is 0) | +105.1 to +197.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 16.77 | +17.1% | -0.7552 to +5.655 | no |
| utilisation (used / allocatable) | 0.03597 | 0.03764 | +4.6% | +0.001057 to +0.002281 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.727 | 1.804 | +4.5% | +0.0434 to +0.1112 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0409 | +0.0409 (native is 0) | +0.0392 to +0.0426 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.727 | 1.845 | +6.8% | +0.08285 to +0.1536 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.3 | 701.4 | -4.0% | -40.17 to -17.57 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.147 | 5.574 | +34.4% | +1.129 to +1.725 | yes: power given |
| pods started | 0 | 4.9 | +4.9 (native is 0) | +3.759 to +6.041 | yes: power given |
| pod start wait, total (s) | 0 | 12.1 | +12.1 (native is 0) | +9.113 to +15.09 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.468 | +2.47 (native is 0) | +2.168 to +2.769 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.16 | 57.77 | +10.8% | +4.766 to +6.46 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 875.5 | 933 | +6.6% | +37.57 to +77.43 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.95 | -0.4% | -0.1495 to +0.05784 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.1125 | +68.8% | -0.0177 to +0.1094 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | -0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 189.5 | 233.1 | +23.0% | +30.57 to +56.56 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.98 | -0.2% | -0.07618 to +0.02947 | no |
| node-hours | 5.028 | 5.016 | -0.2% | -0.04733 to +0.02316 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 529.4 | 527.6 | -0.3% | -3.967 to +0.3879 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 529.4 | 526.8 | -0.5% | -5.592 to +0.5497 | no |
| response time (ms), mean | 1076 | 758.9 | -29.5% | -417.1 to -217.4 | yes: GAIN |
| response time (ms), 95th percentile | 4578 | 3512 | -23.3% | -1481 to -650.6 | yes: GAIN |
| response time (ms), 99th percentile | 6414 | 5057 | -21.2% | -1856 to -857.9 | yes: GAIN |
| time over the response line (% of samples) | 36.3 | 30.45 | -16.1% | -6.796 to -4.891 | yes: GAIN |
| failed requests (%) | 0.02937 | 0.006472 | -78.0% | -0.05709 to +0.01129 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.7 | 15.7 | -11.3% | -2.477 to -1.523 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 151.2 | +151 (native is 0) | +105.1 to +197.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.66 | 16.77 | -22.6% | -7.343 to -2.434 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03987 | 0.03764 | -5.6% | -0.002968 to -0.001494 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.914 | 1.804 | -5.7% | -0.1416 to -0.07819 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0409 | +0.0409 (native is 0) | +0.0392 to +0.0426 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.914 | 1.845 | -3.6% | -0.1006 to -0.03742 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 665.1 | 701.4 | +5.5% | +25.69 to +47 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.02 | 5.574 | +38.7% | +1.275 to +1.834 | yes: power given |
| pods started | 0 | 4.9 | +4.9 (native is 0) | +3.759 to +6.041 | yes: power given |
| pod start wait, total (s) | 0 | 12.1 | +12.1 (native is 0) | +9.113 to +15.09 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.468 | +2.47 (native is 0) | +2.168 to +2.769 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.74 | 57.77 | -6.4% | -5.169 to -2.774 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1051 | 933 | -11.3% | -150.3 to -86.26 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 11.95 | -0.4% | -0.1495 to +0.05784 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 14.36 | 0.1125 | -99.2% | -22.46 to -6.036 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 134 | 0.8 | -99.4% | -218.5 to -47.88 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 316.6 | 233.1 | -26.4% | -109 to -58.11 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -0.0138 to +0.005338 | no |
| node-hours | 5.034 | 5.022 | -0.2% | -0.02744 to +0.003883 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.1 | 529.5 | +0.5% | +0.4556 to +4.351 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.1 | 529.4 | +0.4% | +0.3679 to +4.172 | yes: power given |
| response time (ms), mean | 661.7 | 1299 | +96.3% | +533.4 to +741.4 | yes: LOSS |
| response time (ms), 95th percentile | 2737 | 5512 | +101.4% | +2346 to +3203 | yes: LOSS |
| response time (ms), 99th percentile | 3831 | 7396 | +93.1% | +3021 to +4109 | yes: LOSS |
| time over the response line (% of samples) | 29.25 | 40.7 | +39.1% | +7.428 to +15.46 | yes: LOSS |
| failed requests (%) | 0 | 0.1774 | +0.177 (native is 0) | +0.007376 to +0.3474 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 19 | +35.7% | +3.934 to +6.066 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 139.1 | +139 (native is 0) | +129.3 to +148.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.32 | 32.96 | +130.1% | +5.522 to +31.75 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03597 | 0.04062 | +12.9% | +0.003217 to +0.006085 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.727 | 1.949 | +12.9% | +0.1537 to +0.2917 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04341 | +0.0434 (native is 0) | +0.04107 to +0.04575 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.727 | 1.993 | +15.4% | +0.1965 to +0.3356 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.3 | 652.4 | -10.7% | -100 to -55.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.147 | 5.205 | +25.5% | +0.6333 to +1.481 | yes: power given |
| pods started | 0 | 4.3 | +4.3 (native is 0) | +2.828 to +5.772 | yes: power given |
| pod start wait, total (s) | 0 | 10.6 | +10.6 (native is 0) | +5.901 to +15.3 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.354 | +2.35 (native is 0) | +2.035 to +2.674 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.16 | 67.79 | +30.0% | +14.65 to +16.61 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 875.5 | 1124 | +28.4% | +214.7 to +282.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.99 | -0.1% | -0.03182 to +0.01231 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 17.13 | +25593.8% | +3.099 to +31.03 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 97.6 | +19420.0% | +19.59 to +174.6 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 189.5 | 402 | +112.2% | +182.4 to +242.7 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*