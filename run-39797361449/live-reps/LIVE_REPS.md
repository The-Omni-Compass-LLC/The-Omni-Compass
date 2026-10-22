# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s | omni, a decision every 10 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.511 | 1.513 | 1.511 | 1.512 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | 158.9 | 159 | 159.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.1 | 158.9 | 159 | 159.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 165.1 | 84.49 | 83.91 | 85.46 | 86.33 |
| response time (ms), 95th percentile | 363.2 | 127.7 | 127.5 | 131.5 | 133.4 |
| response time (ms), 99th percentile | 601 | 179.6 | 170.9 | 187.8 | 182.9 |
| time over the response line (% of samples) | 2.308 | 0 | 0 | 0.0119 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | 17.2 | 20.3 | 21 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan | 90 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.2183 | 0.2417 | 0.2717 | 0.1917 |
| utilisation (used / allocatable) | 0.04089 | 0.03887 | 0.03891 | 0.03934 | 0.03971 |
| CPU used (cores), mean | 0.9815 | 0.9329 | 0.9339 | 0.9443 | 0.9531 |
| Omni's own CPU (cores), mean | 0 | 0.02667 | 0.00927 | 0.03821 | 0.07446 |
| CPU used with Omni's own (cores), mean | 0.9815 | 0.9596 | 0.9432 | 0.9825 | 1.028 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 678.8 | 703.7 | 700.8 | 693.4 | 689.9 |
| HPA replicas, mean | 8.709 | 9.12 | 8.402 | 9.001 | 8.839 |
| pods started | 4.4 | 3.4 | 2.8 | 3.7 | 2.9 |
| pod start wait, total (s) | 6.7 | 4 | 4.4 | 5.7 | 4.1 |
| pod start wait, mean (s) | 1.497 | 1.24 | 1.558 | 1.645 | 1.448 |
| host CPU busy, the real machine under kind (%) | 29.62 | 29.36 | 28.8 | 30.03 | 31.71 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.511 | 1.513 | +0.1% | +0.0001997 to +0.003467 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | -0.2% | -0.5502 to +0.02991 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.1 | -0.2% | -0.5502 to +0.02991 | no |
| response time (ms), mean | 165.1 | 84.49 | -48.8% | -101 to -60.19 | yes: GAIN |
| response time (ms), 95th percentile | 363.2 | 127.7 | -64.8% | -287.8 to -183.2 | yes: GAIN |
| response time (ms), 99th percentile | 601 | 179.6 | -70.1% | -527.1 to -315.7 | yes: GAIN |
| time over the response line (% of samples) | 2.308 | 0 | -100.0% | -3.319 to -1.298 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | -100.0% | -3.957 to -1.243 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | +19.6 (native is 0) | +18.29 to +20.91 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.2183 | +167.3% | -0.007801 to +0.2811 | no |
| utilisation (used / allocatable) | 0.04089 | 0.03887 | -4.9% | -0.003139 to -0.000905 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9815 | 0.9329 | -4.9% | -0.07533 to -0.02172 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02667 | +0.0267 (native is 0) | +0.02319 to +0.03015 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9815 | 0.9596 | -2.2% | -0.04614 to +0.002432 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 678.8 | 703.7 | +3.7% | +9.376 to +40.34 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.709 | 9.12 | +4.7% | -0.1424 to +0.963 | no |
| pods started | 4.4 | 3.4 | -22.7% | -2.508 to +0.508 | no |
| pod start wait, total (s) | 6.7 | 4 | -40.3% | -5.377 to -0.0225 | yes: GAIN |
| pod start wait, mean (s) | 1.497 | 1.24 | -17.1% | -0.6094 to +0.09611 | no |
| host CPU busy, the real machine under kind (%) | 29.62 | 29.36 | -0.9% | -0.7678 to +0.2579 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.511 | -0.0% | -0.004572 to +0.004239 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | -0.3% | -0.8228 to -0.07849 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | -0.3% | -0.8228 to -0.07849 | yes: GAIN |
| response time (ms), mean | 165.1 | 83.91 | -49.2% | -102 to -60.41 | yes: GAIN |
| response time (ms), 95th percentile | 363.2 | 127.5 | -64.9% | -288.3 to -183 | yes: GAIN |
| response time (ms), 99th percentile | 601 | 170.9 | -71.6% | -539 to -321.2 | yes: GAIN |
| time over the response line (% of samples) | 2.308 | 0 | -100.0% | -3.319 to -1.298 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | -100.0% | -3.957 to -1.243 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 | +17.2 (native is 0) | +14.19 to +20.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.2417 | +195.9% | -0.02709 to +0.3471 | no |
| utilisation (used / allocatable) | 0.04089 | 0.03891 | -4.8% | -0.003189 to -0.0007749 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9815 | 0.9339 | -4.8% | -0.07653 to -0.0186 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00927 | +0.00927 (native is 0) | +0.008173 to +0.01037 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9815 | 0.9432 | -3.9% | -0.0664 to -0.01019 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 678.8 | 700.8 | +3.2% | +1.254 to +42.81 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.709 | 8.402 | -3.5% | -0.8295 to +0.2144 | no |
| pods started | 4.4 | 2.8 | -36.4% | -2.677 to -0.5231 | yes: GAIN |
| pod start wait, total (s) | 6.7 | 4.4 | -34.3% | -5.41 to +0.8097 | no |
| pod start wait, mean (s) | 1.497 | 1.558 | +4.1% | -0.4764 to +0.5998 | no |
| host CPU busy, the real machine under kind (%) | 29.62 | 28.8 | -2.8% | -1.735 to +0.1054 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 10 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 10 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.108e-16 to +1.066e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.512 | +0.0% | -0.004142 to +0.005475 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | -0.2% | -0.693 to +0.1207 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | -0.2% | -0.693 to +0.1207 | no |
| response time (ms), mean | 165.1 | 85.46 | -48.2% | -99.8 to -59.49 | yes: GAIN |
| response time (ms), 95th percentile | 363.2 | 131.5 | -63.8% | -282.8 to -180.6 | yes: GAIN |
| response time (ms), 99th percentile | 601 | 187.8 | -68.7% | -512.3 to -314 | yes: GAIN |
| time over the response line (% of samples) | 2.308 | 0.0119 | -99.5% | -3.317 to -1.276 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | -100.0% | -3.957 to -1.243 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.3 (native is 0) | +18.3 to +22.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.2717 | +232.7% | +0.008135 to +0.3719 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04089 | 0.03934 | -3.8% | -0.002654 to -0.0004454 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9815 | 0.9443 | -3.8% | -0.06369 to -0.01069 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03821 | +0.0382 (native is 0) | +0.03417 to +0.04225 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9815 | 0.9825 | +0.1% | -0.02222 to +0.02426 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 678.8 | 693.4 | +2.1% | -7.484 to +36.59 | no |
| HPA replicas, mean | 8.709 | 9.001 | +3.3% | +0.0669 to +0.5159 | yes: power given |
| pods started | 4.4 | 3.7 | -15.9% | -1.769 to +0.369 | no |
| pod start wait, total (s) | 6.7 | 5.7 | -14.9% | -3.36 to +1.36 | no |
| pod start wait, mean (s) | 1.497 | 1.645 | +9.9% | -0.1977 to +0.4943 | no |
| host CPU busy, the real machine under kind (%) | 29.62 | 30.03 | +1.4% | -0.4788 to +1.312 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.242e-16 to +5.794e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.514 | +0.2% | -0.002749 to +0.007749 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.3 | -0.0% | -0.5063 to +0.5035 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.3 | -0.0% | -0.5063 to +0.5035 | no |
| response time (ms), mean | 165.1 | 86.33 | -47.7% | -98.72 to -58.85 | yes: GAIN |
| response time (ms), 95th percentile | 363.2 | 133.4 | -63.3% | -280.3 to -179.3 | yes: GAIN |
| response time (ms), 99th percentile | 601 | 182.9 | -69.6% | -516.8 to -319.4 | yes: GAIN |
| time over the response line (% of samples) | 2.308 | 0 | -100.0% | -3.319 to -1.298 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0 | -100.0% | -3.957 to -1.243 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21 | +21 (native is 0) | +18.43 to +23.57 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.1917 | +134.7% | -0.1368 to +0.3568 | no |
| utilisation (used / allocatable) | 0.04089 | 0.03971 | -2.9% | -0.002204 to -0.0001568 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9815 | 0.9531 | -2.9% | -0.0529 to -0.003763 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07446 | +0.0745 (native is 0) | +0.06536 to +0.08356 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9815 | 1.028 | +4.7% | +0.02446 to +0.0678 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 678.8 | 689.9 | +1.6% | -6.987 to +29.2 | no |
| HPA replicas, mean | 8.709 | 8.839 | +1.5% | -0.3938 to +0.6538 | no |
| pods started | 4.4 | 2.9 | -34.1% | -2.408 to -0.5921 | yes: GAIN |
| pod start wait, total (s) | 6.7 | 4.1 | -38.8% | -4.738 to -0.462 | yes: GAIN |
| pod start wait, mean (s) | 1.497 | 1.448 | -3.2% | -0.3847 to +0.288 | no |
| host CPU busy, the real machine under kind (%) | 29.62 | 31.71 | +7.1% | +1.399 to +2.787 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 60 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.511 | -0.1% | -0.006346 to +0.002346 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.9 | -0.1% | -0.6187 to +0.2377 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.9 | -0.1% | -0.6187 to +0.2377 | no |
| response time (ms), mean | 84.49 | 83.91 | -0.7% | -1.402 to +0.2384 | no |
| response time (ms), 95th percentile | 127.7 | 127.5 | -0.1% | -1.393 to +1.116 | no |
| response time (ms), 99th percentile | 179.6 | 170.9 | -4.8% | -21.22 to +3.86 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 17.2 | -12.2% | -5.439 to +0.6385 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.2417 | +10.7% | -0.1954 to +0.2421 | no |
| utilisation (used / allocatable) | 0.03887 | 0.03891 | +0.1% | -0.0004098 to +0.0004902 | no |
| CPU used (cores), mean | 0.9329 | 0.9339 | +0.1% | -0.009836 to +0.01176 | no |
| Omni's own CPU (cores), mean | 0.02667 | 0.00927 | -65.2% | -0.01984 to -0.01496 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9596 | 0.9432 | -1.7% | -0.02823 to -0.004645 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.7 | 700.8 | -0.4% | -14.31 to +8.65 | no |
| HPA replicas, mean | 9.12 | 8.402 | -7.9% | -1.144 to -0.2914 | yes: GAIN |
| pods started | 3.4 | 2.8 | -17.6% | -1.566 to +0.3656 | no |
| pod start wait, total (s) | 4 | 4.4 | +10.0% | -0.9146 to +1.715 | no |
| pod start wait, mean (s) | 1.24 | 1.558 | +25.7% | -0.02038 to +0.657 | no |
| host CPU busy, the real machine under kind (%) | 29.36 | 28.8 | -1.9% | -1.142 to +0.02221 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 10 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 10 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.512 | -0.1% | -0.00587 to +0.003537 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159 | -0.0% | -0.5224 to +0.4704 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159 | -0.0% | -0.5224 to +0.4704 | no |
| response time (ms), mean | 84.49 | 85.46 | +1.2% | -0.1982 to +2.142 | no |
| response time (ms), 95th percentile | 127.7 | 131.5 | +3.0% | +0.4394 to +7.116 | yes: LOSS |
| response time (ms), 99th percentile | 179.6 | 187.8 | +4.6% | -7.203 to +23.78 | no |
| time over the response line (% of samples) | 0 | 0.0119 | +0.0119 (native is 0) | -0.01502 to +0.03883 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 20.3 | +3.6% | -1.588 to +2.988 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 90 | -10.0% | -32.62 to +12.62 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.2717 | +24.4% | -0.1296 to +0.2363 | no |
| utilisation (used / allocatable) | 0.03887 | 0.03934 | +1.2% | +5.66e-05 to +0.0008881 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9329 | 0.9443 | +1.2% | +0.001358 to +0.02131 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.02667 | 0.03821 | +43.3% | +0.01041 to +0.01267 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9596 | 0.9825 | +2.4% | +0.01251 to +0.03324 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.7 | 693.4 | -1.5% | -23.27 to +2.656 | no |
| HPA replicas, mean | 9.12 | 9.001 | -1.3% | -0.7361 to +0.4984 | no |
| pods started | 3.4 | 3.7 | +8.8% | -1.092 to +1.692 | no |
| pod start wait, total (s) | 4 | 5.7 | +42.5% | -0.913 to +4.313 | no |
| pod start wait, mean (s) | 1.24 | 1.645 | +32.7% | +0.0207 to +0.7893 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 29.36 | 30.03 | +2.3% | +0.009782 to +1.333 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.242e-16 to +5.794e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.514 | +0.0% | -0.004903 to +0.006236 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.3 | +0.2% | -0.3757 to +0.8933 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.3 | +0.2% | -0.3757 to +0.8933 | no |
| response time (ms), mean | 84.49 | 86.33 | +2.2% | +0.3671 to +3.305 | yes: LOSS |
| response time (ms), 95th percentile | 127.7 | 133.4 | +4.5% | +1.758 to +9.633 | yes: LOSS |
| response time (ms), 99th percentile | 179.6 | 182.9 | +1.8% | -8.077 to +14.69 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 21 | +7.1% | -0.892 to +3.692 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | +0.0% | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.1917 | -12.2% | -0.3271 to +0.2738 | no |
| utilisation (used / allocatable) | 0.03887 | 0.03971 | +2.2% | +0.0001775 to +0.001505 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9329 | 0.9531 | +2.2% | +0.00426 to +0.03613 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.02667 | 0.07446 | +179.2% | +0.04203 to +0.05355 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9596 | 1.028 | +7.1% | +0.04856 to +0.08741 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.7 | 689.9 | -2.0% | -24.18 to -3.33 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.12 | 8.839 | -3.1% | -0.8149 to +0.2543 | no |
| pods started | 3.4 | 2.9 | -14.7% | -1.727 to +0.7274 | no |
| pod start wait, total (s) | 4 | 4.1 | +2.5% | -1.268 to +1.468 | no |
| pod start wait, mean (s) | 1.24 | 1.448 | +16.8% | -0.1759 to +0.5925 | no |
| host CPU busy, the real machine under kind (%) | 29.36 | 31.71 | +8.0% | +1.761 to +2.934 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*