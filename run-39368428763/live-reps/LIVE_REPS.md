# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.241 | 5.452 |
| node-hours | 2.512 | 2.514 | 2.193 | 2.285 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.6 | 273.5 | 274 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.6 | 249.6 | 256.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 397.9 | 380.6 | 359.3 | 326.2 |
| response time (ms), 95th percentile | 1397 | 1586 | 1463 | 1543 |
| response time (ms), 99th percentile | 2014 | 2292 | 2059 | 2300 |
| time over the response line (% of samples) | 21.43 | 16.92 | 20.49 | 15.52 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.7 | 10.9 | 11.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 44 | 35 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.24 | 12.15 | 11.64 | 12.32 |
| utilisation (used / allocatable) | 0.06349 | 0.06286 | 0.07379 | 0.06985 |
| CPU used (cores), mean | 1.524 | 1.509 | 1.527 | 1.519 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01881 | 0.01715 |
| CPU used with Omni's own (cores), mean | 1.524 | 1.509 | 1.546 | 1.536 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.7 | 440 | 391.6 | 405 |
| HPA replicas, mean | 1.923 | 2.032 | 2.003 | 2.28 |
| pods started | 0.1 | 0.2 | 0.1 | 0.6 |
| pod start wait, total (s) | 0.3 | 0.5 | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.3 | 0.25 | 0.2 | 0.9 |
| host CPU busy, the real machine under kind (%) | 43.51 | 43.47 | 44.48 | 44.3 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 795.4 | 796.8 | 799.8 | 799.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.671 | 4.988 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.05417 | 0.08333 | 0.0375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.3 | 0.4 | 0.3 |
| queue: job turnaround, submitted to done, mean (s) | 102.4 | 106.1 | 106.9 | 108.4 |
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
| worker nodes in service, mean | 6 | 5.452 | -9.1% | -1.069 to -0.02695 | yes: GAIN |
| node-hours | 2.514 | 2.285 | -9.1% | -0.4493 to -0.00799 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 274 | +0.1% | -0.3725 to +1.072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 256.7 | -6.2% | -33.25 to -0.4961 | yes: GAIN |
| response time (ms), mean | 380.6 | 326.2 | -14.3% | -72.27 to -36.39 | yes: GAIN |
| response time (ms), 95th percentile | 1586 | 1543 | -2.7% | -152.5 to +67.33 | no |
| response time (ms), 99th percentile | 2292 | 2300 | +0.4% | -188.3 to +204.4 | no |
| time over the response line (% of samples) | 16.92 | 15.52 | -8.3% | -2.067 to -0.7319 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11.1 | +3.7% | -0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35 | +35 (native is 0) | +26.76 to +43.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.15 | 12.32 | +1.4% | -2.203 to +2.533 | no |
| utilisation (used / allocatable) | 0.06286 | 0.06985 | +11.1% | +0.0004049 to +0.01359 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.509 | 1.519 | +0.7% | -0.01446 to +0.03565 | no |
| Omni's own CPU (cores), mean | 0 | 0.01715 | +0.0171 (native is 0) | +0.0159 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 1.536 | +1.8% | +0.002908 to +0.05258 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440 | 405 | -7.9% | -70.16 to +0.3033 | no |
| HPA replicas, mean | 2.032 | 2.28 | +12.2% | +0.06467 to +0.4319 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.5 | 0.9 | +80.0% | -0.6228 to +1.423 | no |
| pod start wait, mean (s) | 0.25 | 0.9 | +260.0% | +0.01803 to +1.282 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.47 | 44.3 | +1.9% | +0.552 to +1.11 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 796.8 | 799.7 | +0.4% | -2.285 to +8.085 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.988 | -16.9% | -1.932 to -0.09195 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0375 | -30.8% | -0.0569 to +0.02357 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 106.1 | 108.4 | +2.2% | -2.459 to +7.109 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.794e-16 to +2.242e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.514 | +0.1% | -0.003414 to +0.007414 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.6 | +0.1% | -0.4915 to +0.8609 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 273.6 | +0.1% | -0.4915 to +0.8609 | no |
| response time (ms), mean | 397.9 | 380.6 | -4.4% | -40.47 to +5.752 | no |
| response time (ms), 95th percentile | 1397 | 1586 | +13.5% | +14.38 to +363.6 | yes: LOSS |
| response time (ms), 99th percentile | 2014 | 2292 | +13.8% | -10.46 to +567.6 | no |
| time over the response line (% of samples) | 21.43 | 16.92 | -21.0% | -7.528 to -1.485 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.7 | -0.9% | -0.8872 to +0.6872 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.24 | 12.15 | +8.1% | -1.324 to +3.141 | no |
| utilisation (used / allocatable) | 0.06349 | 0.06286 | -1.0% | -0.001646 to +0.0003681 | no |
| CPU used (cores), mean | 1.524 | 1.509 | -1.0% | -0.03951 to +0.008835 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.524 | 1.509 | -1.0% | -0.03951 to +0.008835 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.7 | 440 | +1.2% | -2.808 to +13.25 | no |
| HPA replicas, mean | 1.923 | 2.032 | +5.6% | -0.0226 to +0.2388 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | -1.182 to +1.582 | no |
| pod start wait, mean (s) | 0.3 | 0.25 | -16.7% | -0.9804 to +0.8804 | no |
| host CPU busy, the real machine under kind (%) | 43.51 | 43.47 | -0.1% | -0.3673 to +0.2752 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.4 | 796.8 | +0.2% | -5.379 to +8.179 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.05417 | -27.8% | -0.05596 to +0.01429 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.3 | -50.0% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 102.4 | 106.1 | +3.7% | -2.291 to +9.791 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.241 | -12.7% | -1.44 to -0.07856 | yes: GAIN |
| node-hours | 2.512 | 2.193 | -12.7% | -0.6031 to -0.03561 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.5 | +0.0% | -0.7184 to +0.7552 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 249.6 | -8.7% | -45.24 to -2.407 | yes: GAIN |
| response time (ms), mean | 397.9 | 359.3 | -9.7% | -57.85 to -19.34 | yes: GAIN |
| response time (ms), 95th percentile | 1397 | 1463 | +4.7% | -23.55 to +156 | no |
| response time (ms), 99th percentile | 2014 | 2059 | +2.3% | -123.2 to +214.4 | no |
| time over the response line (% of samples) | 21.43 | 20.49 | -4.4% | -1.934 to +0.04756 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.9 | +0.9% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44 | +44 (native is 0) | +30.47 to +57.53 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.24 | 11.64 | +3.5% | -1.835 to +2.622 | no |
| utilisation (used / allocatable) | 0.06349 | 0.07379 | +16.2% | +0.0009837 to +0.01961 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.527 | +0.2% | -0.0188 to +0.02488 | no |
| Omni's own CPU (cores), mean | 0 | 0.01881 | +0.0188 (native is 0) | +0.0167 to +0.02092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.546 | +1.4% | +0.0005296 to +0.04316 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.7 | 391.6 | -9.9% | -81.21 to -5.141 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.923 | 2.003 | +4.1% | -0.06876 to +0.2275 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.2 | -33.3% | -0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | -33.3% | -0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 43.51 | 44.48 | +2.2% | +0.6639 to +1.272 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.4 | 799.8 | +0.6% | -1.558 to +10.36 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.671 | -22.1% | -2.358 to -0.2996 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.08333 | +11.1% | -0.07455 to +0.09122 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | -33.3% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 102.4 | 106.9 | +4.4% | -1.77 to +10.8 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.241 | -12.7% | -1.44 to -0.07856 | yes: GAIN |
| node-hours | 2.514 | 2.193 | -12.8% | -0.6055 to -0.0372 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.5 | -0.1% | -0.8888 to +0.5563 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 249.6 | -8.8% | -45.35 to -2.661 | yes: GAIN |
| response time (ms), mean | 380.6 | 359.3 | -5.6% | -41.57 to -0.9012 | yes: GAIN |
| response time (ms), 95th percentile | 1586 | 1463 | -7.7% | -276.7 to +31.23 | no |
| response time (ms), 99th percentile | 2292 | 2059 | -10.2% | -469.2 to +3.183 | no |
| time over the response line (% of samples) | 16.92 | 20.49 | +21.1% | +0.9046 to +6.222 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.9 | +1.9% | -0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44 | +44 (native is 0) | +30.47 to +57.53 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.15 | 11.64 | -4.2% | -2.921 to +1.891 | no |
| utilisation (used / allocatable) | 0.06286 | 0.07379 | +17.4% | +0.001249 to +0.02062 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.509 | 1.527 | +1.2% | -0.01637 to +0.05312 | no |
| Omni's own CPU (cores), mean | 0 | 0.01881 | +0.0188 (native is 0) | +0.0167 to +0.02092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 1.546 | +2.5% | +0.003467 to +0.0709 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440 | 391.6 | -11.0% | -91.08 to -5.706 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.032 | 2.003 | -1.4% | -0.1976 to +0.1402 | no |
| pods started | 0.2 | 0.1 | -50.0% | -0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.5 | 0.2 | -60.0% | -1.564 to +0.9639 | no |
| pod start wait, mean (s) | 0.25 | 0.2 | -20.0% | -0.8124 to +0.7124 | no |
| host CPU busy, the real machine under kind (%) | 43.47 | 44.48 | +2.3% | +0.5647 to +1.463 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 796.8 | 799.8 | +0.4% | -5.197 to +11.2 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.671 | -22.1% | -2.358 to -0.2996 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.08333 | +53.8% | -0.06721 to +0.1255 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | -0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 106.1 | 106.9 | +0.7% | -6.615 to +8.14 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.452 | -9.1% | -1.069 to -0.02695 | yes: GAIN |
| node-hours | 2.512 | 2.285 | -9.0% | -0.4473 to -0.006076 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 274 | +0.2% | -0.05106 to +1.12 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 256.7 | -6.1% | -33.18 to -0.2029 | yes: GAIN |
| response time (ms), mean | 397.9 | 326.2 | -18.0% | -97.7 to -45.67 | yes: GAIN |
| response time (ms), 95th percentile | 1397 | 1543 | +10.5% | -11.14 to +303.9 | no |
| response time (ms), 99th percentile | 2014 | 2300 | +14.2% | -55.32 to +628.6 | no |
| time over the response line (% of samples) | 21.43 | 15.52 | -27.6% | -9.339 to -2.474 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11.1 | +2.8% | -0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35 | +35 (native is 0) | +26.76 to +43.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.24 | 12.32 | +9.5% | -1.771 to +3.918 | no |
| utilisation (used / allocatable) | 0.06349 | 0.06985 | +10.0% | +0.0001725 to +0.01255 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.519 | -0.3% | -0.02451 to +0.01503 | no |
| Omni's own CPU (cores), mean | 0 | 0.01715 | +0.0171 (native is 0) | +0.0159 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.536 | +0.8% | -0.006771 to +0.03159 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.7 | 405 | -6.8% | -60.37 to +0.9506 | no |
| HPA replicas, mean | 1.923 | 2.28 | +18.5% | +0.1819 to +0.5309 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | +0.123 to +0.877 | yes: power given |
| pod start wait, total (s) | 0.3 | 0.9 | +200.0% | -0.3048 to +1.505 | no |
| pod start wait, mean (s) | 0.3 | 0.9 | +200.0% | -0.3048 to +1.505 | no |
| host CPU busy, the real machine under kind (%) | 43.51 | 44.3 | +1.8% | +0.4481 to +1.122 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 795.4 | 799.7 | +0.5% | -1.363 to +9.963 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.988 | -16.9% | -1.932 to -0.09195 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.0375 | -50.0% | -0.08292 to +0.007919 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.3 | -50.0% | -0.7828 to +0.1828 | no |
| queue: job turnaround, submitted to done, mean (s) | 102.4 | 108.4 | +5.9% | -0.1115 to +12.26 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*