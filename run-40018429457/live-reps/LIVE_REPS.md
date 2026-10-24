# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.516 | 1.516 | 1.514 | 1.516 | 1.515 | 1.516 | 1.514 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | 158.7 | 158.8 | 158.8 | 158.9 | 158.8 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | 158.7 | 158.8 | 158.8 | 158.9 | 158.8 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 151.8 | 78.84 | 79.77 | 78.82 | 79.57 | 79.42 | 80.05 | 80.33 |
| response time (ms), 95th percentile | 332.2 | 116.7 | 117.7 | 115.5 | 117 | 117.4 | 118.3 | 119.3 |
| response time (ms), 99th percentile | 514.3 | 150.5 | 161.1 | 157.3 | 163 | 170.5 | 152.3 | 159.3 |
| time over the response line (% of samples) | 1.559 | 0 | 0 | 0 | 0.04848 | 0.03636 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | 16 | 18.6 | 18.4 | 18 | 19.5 | 19.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.21 | 0.05167 | 0.1583 | 0.1333 | 0.16 | 0.07833 | 0.05167 |
| utilisation (used / allocatable) | 0.03846 | 0.0368 | 0.03712 | 0.03651 | 0.03666 | 0.03671 | 0.03726 | 0.03756 |
| CPU used (cores), mean | 0.9231 | 0.8832 | 0.891 | 0.8762 | 0.8799 | 0.8811 | 0.8942 | 0.9015 |
| Omni's own CPU (cores), mean | 0 | 0.00813 | 0.00579 | 0.00652 | 0.00729 | 0.0132 | 0.02358 | 0.06402 |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.8913 | 0.8967 | 0.8828 | 0.8871 | 0.8943 | 0.9178 | 0.9655 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 739.1 | 734.7 | 746.3 | 745.2 | 745.9 | 731.5 | 727.3 |
| HPA replicas, mean | 8.495 | 8.221 | 8.523 | 8.469 | 7.719 | 7.567 | 8.959 | 8.747 |
| pods started | 5.4 | 4.1 | 4.1 | 3.8 | 3.9 | 4.6 | 4.1 | 4.2 |
| pod start wait, total (s) | 7.7 | 6.1 | 6.1 | 5.3 | 5.6 | 6.3 | 6.9 | 6.8 |
| pod start wait, mean (s) | 1.42 | 1.54 | 1.567 | 1.367 | 1.468 | 1.353 | 1.663 | 1.6 |
| host CPU busy, the real machine under kind (%) | 27.73 | 26.88 | 27 | 26.71 | 26.88 | 27.1 | 27.78 | 29.22 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.588e-16 to +1.014e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | +0.0% | -0.001019 to +0.001352 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | -0.2% | -0.6825 to -0.01225 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | -0.2% | -0.6825 to -0.01225 | yes: GAIN |
| response time (ms), mean | 151.8 | 78.84 | -48.1% | -93.95 to -52.02 | yes: GAIN |
| response time (ms), 95th percentile | 332.2 | 116.7 | -64.9% | -272.4 to -158.7 | yes: GAIN |
| response time (ms), 99th percentile | 514.3 | 150.5 | -70.7% | -465.4 to -262.2 | yes: GAIN |
| time over the response line (% of samples) | 1.559 | 0 | -100.0% | -2.536 to -0.5825 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | -100.0% | -2.142 to -0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.5 (native is 0) | +15.06 to +19.94 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.21 | +59.5% | -0.1017 to +0.2584 | no |
| utilisation (used / allocatable) | 0.03846 | 0.0368 | -4.3% | -0.002752 to -0.0005765 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9231 | 0.8832 | -4.3% | -0.06605 to -0.01383 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00813 | +0.00813 (native is 0) | +0.007022 to +0.009238 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.8913 | -3.4% | -0.05721 to -0.006419 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 739.1 | +3.0% | +3.87 to +39.18 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.495 | 8.221 | -3.2% | -0.6826 to +0.1345 | no |
| pods started | 5.4 | 4.1 | -24.1% | -2.058 to -0.5422 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 6.1 | -20.8% | -3.79 to +0.5905 | no |
| pod start wait, mean (s) | 1.42 | 1.54 | +8.5% | -0.3627 to +0.6027 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 26.88 | -3.1% | -1.585 to -0.1154 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.451e-16 to +4.675e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.514 | -0.2% | -0.008034 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.7 | -0.4% | -1.276 to +0.09499 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.7 | -0.4% | -1.276 to +0.09499 | no |
| response time (ms), mean | 151.8 | 79.77 | -47.5% | -92.74 to -51.37 | yes: GAIN |
| response time (ms), 95th percentile | 332.2 | 117.7 | -64.6% | -271.1 to -158.1 | yes: GAIN |
| response time (ms), 99th percentile | 514.3 | 161.1 | -68.7% | -458 to -248.4 | yes: GAIN |
| time over the response line (% of samples) | 1.559 | 0 | -100.0% | -2.536 to -0.5825 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | -100.0% | -2.142 to -0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16 (native is 0) | +14.93 to +17.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.05167 | -60.8% | -0.2069 to +0.04689 | no |
| utilisation (used / allocatable) | 0.03846 | 0.03712 | -3.5% | -0.00231 to -0.0003727 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9231 | 0.891 | -3.5% | -0.05544 to -0.008946 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00579 | +0.00579 (native is 0) | +0.005099 to +0.006481 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.8967 | -2.9% | -0.0491 to -0.003705 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 734.7 | +2.4% | +3.325 to +31.04 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.495 | 8.523 | +0.3% | -0.2258 to +0.2816 | no |
| pods started | 5.4 | 4.1 | -24.1% | -2.421 to -0.1791 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 6.1 | -20.8% | -3.224 to +0.02417 | no |
| pod start wait, mean (s) | 1.42 | 1.567 | +10.3% | -0.213 to +0.5064 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 27 | -2.6% | -1.431 to -0.02512 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.91e-16 to +1.805e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | -0.0% | -0.001211 to +0.0008772 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | -0.3% | -0.8165 to -0.1429 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | -0.3% | -0.8165 to -0.1429 | yes: GAIN |
| response time (ms), mean | 151.8 | 78.82 | -48.1% | -93.82 to -52.19 | yes: GAIN |
| response time (ms), 95th percentile | 332.2 | 115.5 | -65.2% | -273.7 to -159.7 | yes: GAIN |
| response time (ms), 99th percentile | 514.3 | 157.3 | -69.4% | -460.4 to -253.7 | yes: GAIN |
| time over the response line (% of samples) | 1.559 | 0 | -100.0% | -2.536 to -0.5825 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | -100.0% | -2.142 to -0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.6 | +18.6 (native is 0) | +16.84 to +20.36 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1583 | +20.3% | -0.163 to +0.2164 | no |
| utilisation (used / allocatable) | 0.03846 | 0.03651 | -5.1% | -0.003023 to -0.0008859 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9231 | 0.8762 | -5.1% | -0.07255 to -0.02126 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00652 | +0.00652 (native is 0) | +0.005654 to +0.007386 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.8828 | -4.4% | -0.06541 to -0.01537 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 746.3 | +4.0% | +16.41 to +41.13 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.495 | 8.469 | -0.3% | -0.3303 to +0.2788 | no |
| pods started | 5.4 | 3.8 | -29.6% | -2.825 to -0.3749 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 5.3 | -31.2% | -4.372 to -0.428 | yes: GAIN |
| pod start wait, mean (s) | 1.42 | 1.367 | -3.8% | -0.3282 to +0.2216 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 26.71 | -3.7% | -1.648 to -0.3924 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.193e-15 to +3.046e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.515 | -0.1% | -0.001992 to +0.0003253 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | -0.3% | -0.7703 to -0.192 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | -0.3% | -0.7703 to -0.192 | yes: GAIN |
| response time (ms), mean | 151.8 | 79.57 | -47.6% | -92.92 to -51.59 | yes: GAIN |
| response time (ms), 95th percentile | 332.2 | 117 | -64.8% | -272.7 to -157.7 | yes: GAIN |
| response time (ms), 99th percentile | 514.3 | 163 | -68.3% | -452.4 to -250.3 | yes: GAIN |
| time over the response line (% of samples) | 1.559 | 0.04848 | -96.9% | -2.467 to -0.5542 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | -100.0% | -2.142 to -0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.4 (native is 0) | +15.7 to +21.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.1333 | +1.3% | -0.1256 to +0.1289 | no |
| utilisation (used / allocatable) | 0.03846 | 0.03666 | -4.7% | -0.002775 to -0.0008327 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9231 | 0.8799 | -4.7% | -0.0666 to -0.01998 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00729 | +0.00729 (native is 0) | +0.006276 to +0.008304 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.8871 | -3.9% | -0.05861 to -0.0134 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 745.2 | +3.9% | +15.19 to +40.12 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.495 | 7.719 | -9.1% | -1.246 to -0.306 | yes: GAIN |
| pods started | 5.4 | 3.9 | -27.8% | -2.108 to -0.8921 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 5.6 | -27.3% | -3.767 to -0.4327 | yes: GAIN |
| pod start wait, mean (s) | 1.42 | 1.468 | +3.4% | -0.31 to +0.4067 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 26.88 | -3.1% | -1.463 to -0.2304 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.471e-16 to +8.471e-16 | no |
| node-hours | 1.516 | 1.516 | +0.0% | -0.000713 to +0.001046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | -0.2% | -0.5866 to -0.1276 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | -0.2% | -0.5866 to -0.1276 | yes: GAIN |
| response time (ms), mean | 151.8 | 79.42 | -47.7% | -92.68 to -52.13 | yes: GAIN |
| response time (ms), 95th percentile | 332.2 | 117.4 | -64.7% | -270.7 to -159 | yes: GAIN |
| response time (ms), 99th percentile | 514.3 | 170.5 | -66.8% | -436.6 to -251.1 | yes: GAIN |
| time over the response line (% of samples) | 1.559 | 0.03636 | -97.7% | -2.483 to -0.5625 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | -100.0% | -2.142 to -0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18 (native is 0) | +15.66 to +20.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.16 | +21.5% | -0.1105 to +0.1671 | no |
| utilisation (used / allocatable) | 0.03846 | 0.03671 | -4.6% | -0.002633 to -0.0008708 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9231 | 0.8811 | -4.6% | -0.06318 to -0.0209 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0132 | +0.0132 (native is 0) | +0.01139 to +0.01501 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.8943 | -3.1% | -0.04885 to -0.008831 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 745.9 | +3.9% | +16.36 to +40.23 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.495 | 7.567 | -10.9% | -1.222 to -0.6348 | yes: GAIN |
| pods started | 5.4 | 4.6 | -14.8% | -1.364 to -0.2358 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 6.3 | -18.2% | -3.159 to +0.3586 | no |
| pod start wait, mean (s) | 1.42 | 1.353 | -4.7% | -0.3824 to +0.2491 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 27.1 | -2.3% | -1.153 to -0.1037 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.586e-16 to +6.033e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.514 | -0.1% | -0.008116 to +0.003782 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.8 | -0.3% | -1.214 to +0.2091 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.8 | -0.3% | -1.214 to +0.2091 | no |
| response time (ms), mean | 151.8 | 80.05 | -47.3% | -92.43 to -51.13 | yes: GAIN |
| response time (ms), 95th percentile | 332.2 | 118.3 | -64.4% | -270.6 to -157.3 | yes: GAIN |
| response time (ms), 99th percentile | 514.3 | 152.3 | -70.4% | -472.7 to -251.3 | yes: GAIN |
| time over the response line (% of samples) | 1.559 | 0 | -100.0% | -2.536 to -0.5825 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | -100.0% | -2.142 to -0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.5 | +19.5 (native is 0) | +18.06 to +20.94 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.07833 | -40.5% | -0.2022 to +0.09555 | no |
| utilisation (used / allocatable) | 0.03846 | 0.03726 | -3.1% | -0.002187 to -0.0002265 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9231 | 0.8942 | -3.1% | -0.05248 to -0.005436 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02358 | +0.0236 (native is 0) | +0.02055 to +0.02661 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.9178 | -0.6% | -0.02679 to +0.01604 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 731.5 | +1.9% | -2.009 to +29.97 | no |
| HPA replicas, mean | 8.495 | 8.959 | +5.5% | +0.08776 to +0.8409 | yes: power given |
| pods started | 5.4 | 4.1 | -24.1% | -2.608 to +0.008141 | no |
| pod start wait, total (s) | 7.7 | 6.9 | -10.4% | -3.25 to +1.65 | no |
| pod start wait, mean (s) | 1.42 | 1.663 | +17.1% | -0.05974 to +0.5464 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 27.78 | +0.2% | -0.5398 to +0.6353 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.51 | -0.4% | -0.015 to +0.002667 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.5 | -0.5% | -1.925 to +0.2335 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.5 | -0.5% | -1.925 to +0.2335 | no |
| response time (ms), mean | 151.8 | 80.33 | -47.1% | -91.95 to -51.04 | yes: GAIN |
| response time (ms), 95th percentile | 332.2 | 119.3 | -64.1% | -269 to -156.9 | yes: GAIN |
| response time (ms), 99th percentile | 514.3 | 159.3 | -69.0% | -449.2 to -261 | yes: GAIN |
| time over the response line (% of samples) | 1.559 | 0 | -100.0% | -2.536 to -0.5825 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | -100.0% | -2.142 to -0.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | +19.7 (native is 0) | +18.39 to +21.01 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.05167 | -60.8% | -0.2069 to +0.04689 | no |
| utilisation (used / allocatable) | 0.03846 | 0.03756 | -2.3% | -0.001646 to -0.0001593 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9231 | 0.9015 | -2.3% | -0.0395 to -0.003822 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06402 | +0.064 (native is 0) | +0.05587 to +0.07217 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9231 | 0.9655 | +4.6% | +0.02878 to +0.05593 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.6 | 727.3 | +1.4% | -3.622 to +23.09 | no |
| HPA replicas, mean | 8.495 | 8.747 | +3.0% | -0.04667 to +0.5507 | no |
| pods started | 5.4 | 4.2 | -22.2% | -2.079 to -0.3207 | yes: GAIN |
| pod start wait, total (s) | 7.7 | 6.8 | -11.7% | -3.223 to +1.423 | no |
| pod start wait, mean (s) | 1.42 | 1.6 | +12.7% | -0.2301 to +0.5901 | no |
| host CPU busy, the real machine under kind (%) | 27.73 | 29.22 | +5.4% | +1.071 to +1.912 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.116e-15 to +5.833e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.514 | -0.2% | -0.008566 to +0.002899 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.7 | -0.2% | -0.8257 to +0.3393 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.7 | -0.2% | -0.8257 to +0.3393 | no |
| response time (ms), mean | 78.84 | 79.77 | +1.2% | -0.09696 to +1.959 | no |
| response time (ms), 95th percentile | 116.7 | 117.7 | +0.8% | -0.8496 to +2.82 | no |
| response time (ms), 99th percentile | 150.5 | 161.1 | +7.1% | -3.715 to +24.97 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 16 | -8.6% | -3.473 to +0.4734 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.05167 | -75.4% | -0.2911 to -0.02555 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0368 | 0.03712 | +0.9% | -0.0005242 to +0.00117 | no |
| CPU used (cores), mean | 0.8832 | 0.891 | +0.9% | -0.01258 to +0.02808 | no |
| Omni's own CPU (cores), mean | 0.00813 | 0.00579 | -28.8% | -0.002789 to -0.001891 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 0.8967 | +0.6% | -0.01496 to +0.02578 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.1 | 734.7 | -0.6% | -18.21 to +9.533 | no |
| HPA replicas, mean | 8.221 | 8.523 | +3.7% | -0.01478 to +0.6187 | no |
| pods started | 4.1 | 4.1 | +0.0% | -1.066 to +1.066 | no |
| pod start wait, total (s) | 6.1 | 6.1 | +0.0% | -2.079 to +2.079 | no |
| pod start wait, mean (s) | 1.54 | 1.567 | +1.7% | -0.5711 to +0.6245 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 27 | +0.5% | -0.2925 to +0.5374 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.391e-15 to +3.247e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | -0.0% | -0.001687 to +0.00102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.8 | -0.1% | -0.3934 to +0.1287 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.8 | -0.1% | -0.3934 to +0.1287 | no |
| response time (ms), mean | 78.84 | 78.82 | -0.0% | -1.025 to +0.987 | no |
| response time (ms), 95th percentile | 116.7 | 115.5 | -1.0% | -2.862 to +0.5739 | no |
| response time (ms), 99th percentile | 150.5 | 157.3 | +4.5% | -9.203 to +22.67 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 18.6 | +6.3% | -1.478 to +3.678 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.1583 | -24.6% | -0.2864 to +0.1831 | no |
| utilisation (used / allocatable) | 0.0368 | 0.03651 | -0.8% | -0.0009055 to +0.0003252 | no |
| CPU used (cores), mean | 0.8832 | 0.8762 | -0.8% | -0.02173 to +0.007804 | no |
| Omni's own CPU (cores), mean | 0.00813 | 0.00652 | -19.8% | -0.001951 to -0.001269 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 0.8828 | -1.0% | -0.02355 to +0.0064 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.1 | 746.3 | +1.0% | -5.059 to +19.55 | no |
| HPA replicas, mean | 8.221 | 8.469 | +3.0% | -0.1813 to +0.6778 | no |
| pods started | 4.1 | 3.8 | -7.3% | -1.772 to +1.172 | no |
| pod start wait, total (s) | 6.1 | 5.3 | -13.1% | -2.61 to +1.01 | no |
| pod start wait, mean (s) | 1.54 | 1.367 | -11.3% | -0.5896 to +0.243 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 26.71 | -0.6% | -0.5194 to +0.1792 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.523e-15 to +2.792e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.515 | -0.1% | -0.002005 to +5.333e-06 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.8 | -0.1% | -0.3468 to +0.07932 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.8 | -0.1% | -0.3468 to +0.07932 | no |
| response time (ms), mean | 78.84 | 79.57 | +0.9% | -0.3376 to +1.797 | no |
| response time (ms), 95th percentile | 116.7 | 117 | +0.3% | -1.747 to +2.472 | no |
| response time (ms), 99th percentile | 150.5 | 163 | +8.3% | -8.344 to +33.32 | no |
| time over the response line (% of samples) | 0 | 0.04848 | +0.0485 (native is 0) | -0.01214 to +0.1091 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 18.4 | +5.1% | -1.471 to +3.271 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.1333 | -36.5% | -0.2783 to +0.125 | no |
| utilisation (used / allocatable) | 0.0368 | 0.03666 | -0.4% | -0.0007908 to +0.0005117 | no |
| CPU used (cores), mean | 0.8832 | 0.8799 | -0.4% | -0.01898 to +0.01228 | no |
| Omni's own CPU (cores), mean | 0.00813 | 0.00729 | -10.3% | -0.001079 to -0.0006011 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 0.8871 | -0.5% | -0.0198 to +0.01142 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.1 | 745.2 | +0.8% | -8.57 to +20.84 | no |
| HPA replicas, mean | 8.221 | 7.719 | -6.1% | -0.9446 to -0.05885 | yes: GAIN |
| pods started | 4.1 | 3.9 | -4.9% | -1.256 to +0.8556 | no |
| pod start wait, total (s) | 6.1 | 5.6 | -8.2% | -2.914 to +1.914 | no |
| pod start wait, mean (s) | 1.54 | 1.468 | -4.7% | -0.581 to +0.4376 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 26.88 | +0.0% | -0.2607 to +0.2678 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.014e-15 to +6.588e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | +0.0% | -0.001257 to +0.001257 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.9 | -0.0% | -0.2192 to +0.1997 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.9 | -0.0% | -0.2192 to +0.1997 | no |
| response time (ms), mean | 78.84 | 79.42 | +0.7% | -0.2447 to +1.408 | no |
| response time (ms), 95th percentile | 116.7 | 117.4 | +0.6% | -1.134 to +2.56 | no |
| response time (ms), 99th percentile | 150.5 | 170.5 | +13.3% | +5.903 to +34.09 | yes: LOSS |
| time over the response line (% of samples) | 0 | 0.03636 | +0.0364 (native is 0) | -0.005518 to +0.07825 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 18 | +2.9% | -1.558 to +2.558 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.16 | -23.8% | -0.1695 to +0.06948 | no |
| utilisation (used / allocatable) | 0.0368 | 0.03671 | -0.2% | -0.0007996 to +0.0006249 | no |
| CPU used (cores), mean | 0.8832 | 0.8811 | -0.2% | -0.01919 to +0.015 | no |
| Omni's own CPU (cores), mean | 0.00813 | 0.0132 | +62.4% | +0.004312 to +0.005828 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 0.8943 | +0.3% | -0.01443 to +0.02038 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.1 | 745.9 | +0.9% | -11.36 to +24.9 | no |
| HPA replicas, mean | 8.221 | 7.567 | -8.0% | -1.055 to -0.2529 | yes: GAIN |
| pods started | 4.1 | 4.6 | +12.2% | -0.4685 to +1.469 | no |
| pod start wait, total (s) | 6.1 | 6.3 | +3.3% | -1.14 to +1.54 | no |
| pod start wait, mean (s) | 1.54 | 1.353 | -12.1% | -0.5724 to +0.1991 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 27.1 | +0.8% | -0.1313 to +0.5755 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.264e-15 to +5.531e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.514 | -0.2% | -0.008206 to +0.003539 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.8 | -0.1% | -0.7021 to +0.3922 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.8 | -0.1% | -0.7021 to +0.3922 | no |
| response time (ms), mean | 78.84 | 80.05 | +1.5% | -0.3906 to +2.81 | no |
| response time (ms), 95th percentile | 116.7 | 118.3 | +1.4% | -1.613 to +4.815 | no |
| response time (ms), 99th percentile | 150.5 | 152.3 | +1.2% | -22.14 to +25.8 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 19.5 | +11.4% | -1.109 to +5.109 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.07833 | -62.7% | -0.2931 to +0.0298 | no |
| utilisation (used / allocatable) | 0.0368 | 0.03726 | +1.2% | -0.0002432 to +0.001158 | no |
| CPU used (cores), mean | 0.8832 | 0.8942 | +1.2% | -0.005837 to +0.0278 | no |
| Omni's own CPU (cores), mean | 0.00813 | 0.02358 | +190.0% | +0.01347 to +0.01743 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 0.9178 | +3.0% | +0.009099 to +0.04377 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.1 | 731.5 | -1.0% | -18.69 to +3.606 | no |
| HPA replicas, mean | 8.221 | 8.959 | +9.0% | +0.3282 to +1.149 | yes: power given |
| pods started | 4.1 | 4.1 | +0.0% | -1.617 to +1.617 | no |
| pod start wait, total (s) | 6.1 | 6.9 | +13.1% | -1.829 to +3.429 | no |
| pod start wait, mean (s) | 1.54 | 1.663 | +8.0% | -0.3501 to +0.5968 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 27.78 | +3.3% | +0.4326 to +1.363 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.939e-16 to +1.249e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.51 | -0.4% | -0.01513 to +0.00246 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | -0.3% | -1.44 to +0.4434 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | -0.3% | -1.44 to +0.4434 | no |
| response time (ms), mean | 78.84 | 80.33 | +1.9% | +0.5541 to +2.43 | yes: LOSS |
| response time (ms), 95th percentile | 116.7 | 119.3 | +2.2% | +0.9822 to +4.218 | yes: LOSS |
| response time (ms), 99th percentile | 150.5 | 159.3 | +5.8% | -8.679 to +26.15 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.5 | 19.7 | +12.6% | +0.04615 to +4.354 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.05167 | -75.4% | -0.3203 to +0.003601 | no |
| utilisation (used / allocatable) | 0.0368 | 0.03756 | +2.1% | +0.0002865 to +0.001237 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8832 | 0.9015 | +2.1% | +0.006875 to +0.02969 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00813 | 0.06402 | +687.5% | +0.04884 to +0.06294 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8913 | 0.9655 | +8.3% | +0.05792 to +0.09042 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.1 | 727.3 | -1.6% | -18.24 to -5.349 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.221 | 8.747 | +6.4% | +0.1584 to +0.8938 | yes: power given |
| pods started | 4.1 | 4.2 | +2.4% | -0.9366 to +1.137 | no |
| pod start wait, total (s) | 6.1 | 6.8 | +11.5% | -1.407 to +2.807 | no |
| pod start wait, mean (s) | 1.54 | 1.6 | +3.9% | -0.3321 to +0.4521 | no |
| host CPU busy, the real machine under kind (%) | 26.88 | 29.22 | +8.7% | +1.907 to +2.777 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*