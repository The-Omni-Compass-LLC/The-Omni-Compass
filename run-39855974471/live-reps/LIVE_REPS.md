# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s | omni, a decision every 10 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.518 | 1.515 | 1.517 | 1.516 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.4 | 159.7 | 159.6 | 159.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 159.4 | 159.7 | 159.6 | 159.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 173.4 | 86.85 | 86.81 | 87.36 | 88.48 |
| response time (ms), 95th percentile | 400.3 | 130.9 | 132.2 | 132.4 | 135.3 |
| response time (ms), 99th percentile | 654.7 | 184.9 | 181.2 | 180.9 | 194.3 |
| time over the response line (% of samples) | 2.958 | 0.0119 | 0.03636 | 0.07295 | 0.04871 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | 17.9 | 22.2 | 24.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | nan | 60 | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.1083 | 0.1633 | 0.3733 | 0.16 |
| utilisation (used / allocatable) | 0.04158 | 0.03963 | 0.03966 | 0.04009 | 0.04082 |
| CPU used (cores), mean | 0.9978 | 0.9512 | 0.9518 | 0.9621 | 0.9797 |
| Omni's own CPU (cores), mean | 0 | 0.0253 | 0.00886 | 0.03633 | 0.06983 |
| CPU used with Omni's own (cores), mean | 0.9978 | 0.9765 | 0.9607 | 0.9984 | 1.049 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 667.2 | 695.6 | 690.7 | 684.7 | 673.8 |
| HPA replicas, mean | 8.656 | 9.199 | 8.471 | 9.219 | 9.346 |
| pods started | 4.7 | 3.8 | 3.7 | 4.6 | 5.1 |
| pod start wait, total (s) | 7.6 | 6 | 5.5 | 6.1 | 8.6 |
| pod start wait, mean (s) | 1.632 | 1.512 | 1.448 | 1.387 | 1.742 |
| host CPU busy, the real machine under kind (%) | 29.81 | 29.5 | 28.95 | 30.03 | 31.6 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.179e-16 to +1.661e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.515 | -0.2% | -0.009143 to +0.003476 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.4 | -0.5% | -1.446 to -0.09798 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 159.4 | -0.5% | -1.446 to -0.09798 | yes: GAIN |
| response time (ms), mean | 173.4 | 86.85 | -49.9% | -105.6 to -67.51 | yes: GAIN |
| response time (ms), 95th percentile | 400.3 | 130.9 | -67.3% | -327.9 to -210.9 | yes: GAIN |
| response time (ms), 99th percentile | 654.7 | 184.9 | -71.8% | -571.8 to -367.8 | yes: GAIN |
| time over the response line (% of samples) | 2.958 | 0.0119 | -99.6% | -4.058 to -1.834 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | -100.0% | -4.216 to -1.784 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | +19.6 (native is 0) | +18.08 to +21.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.1083 | +3.2% | -0.1978 to +0.2045 | no |
| utilisation (used / allocatable) | 0.04158 | 0.03963 | -4.7% | -0.002599 to -0.001285 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9978 | 0.9512 | -4.7% | -0.06238 to -0.03084 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0253 | +0.0253 (native is 0) | +0.02193 to +0.02867 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9978 | 0.9765 | -2.1% | -0.03552 to -0.007091 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 667.2 | 695.6 | +4.2% | +20.79 to +35.83 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.656 | 9.199 | +6.3% | +0.2409 to +0.8438 | yes: power given |
| pods started | 4.7 | 3.8 | -19.1% | -2.041 to +0.241 | no |
| pod start wait, total (s) | 7.6 | 6 | -21.1% | -3.892 to +0.692 | no |
| pod start wait, mean (s) | 1.632 | 1.512 | -7.4% | -0.5044 to +0.2644 | no |
| host CPU busy, the real machine under kind (%) | 29.81 | 29.5 | -1.0% | -0.6476 to +0.02613 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.259e-16 to +1.547e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.517 | -0.0% | -0.0057 to +0.004366 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.7 | -0.3% | -1.071 to +0.05563 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 159.7 | -0.3% | -1.071 to +0.05563 | no |
| response time (ms), mean | 173.4 | 86.81 | -49.9% | -106.5 to -66.68 | yes: GAIN |
| response time (ms), 95th percentile | 400.3 | 132.2 | -67.0% | -326.9 to -209.4 | yes: GAIN |
| response time (ms), 99th percentile | 654.7 | 181.2 | -72.3% | -586.1 to -360.9 | yes: GAIN |
| time over the response line (% of samples) | 2.958 | 0.03636 | -98.8% | -4.01 to -1.833 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | -100.0% | -4.216 to -1.784 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | +17.9 (native is 0) | +15.55 to +20.25 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.1633 | +55.6% | -0.09794 to +0.2146 | no |
| utilisation (used / allocatable) | 0.04158 | 0.03966 | -4.6% | -0.002772 to -0.001062 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9978 | 0.9518 | -4.6% | -0.06652 to -0.02548 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00886 | +0.00886 (native is 0) | +0.007819 to +0.009901 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9978 | 0.9607 | -3.7% | -0.05681 to -0.01748 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 667.2 | 690.7 | +3.5% | +7.485 to +39.52 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.656 | 8.471 | -2.1% | -0.5546 to +0.1839 | no |
| pods started | 4.7 | 3.7 | -21.3% | -2.066 to +0.06632 | no |
| pod start wait, total (s) | 7.6 | 5.5 | -27.6% | -4.079 to -0.1208 | yes: GAIN |
| pod start wait, mean (s) | 1.632 | 1.448 | -11.2% | -0.4584 to +0.09176 | no |
| host CPU busy, the real machine under kind (%) | 29.81 | 28.95 | -2.9% | -1.589 to -0.1343 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 10 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 10 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.848e-16 to +1.847e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.515 | -0.2% | -0.01034 to +0.005002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.6 | -0.4% | -1.483 to +0.2493 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 159.6 | -0.4% | -1.483 to +0.2493 | no |
| response time (ms), mean | 173.4 | 87.36 | -49.6% | -105.1 to -66.96 | yes: GAIN |
| response time (ms), 95th percentile | 400.3 | 132.4 | -66.9% | -326.3 to -209.5 | yes: GAIN |
| response time (ms), 99th percentile | 654.7 | 180.9 | -72.4% | -578.6 to -369 | yes: GAIN |
| time over the response line (% of samples) | 2.958 | 0.07295 | -97.5% | -3.948 to -1.822 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | -100.0% | -4.216 to -1.784 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.2 | +22.2 (native is 0) | +18.3 to +26.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.3733 | +255.6% | -0.03161 to +0.5683 | no |
| utilisation (used / allocatable) | 0.04158 | 0.04009 | -3.6% | -0.002257 to -0.0007177 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9978 | 0.9621 | -3.6% | -0.05418 to -0.01723 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03633 | +0.0363 (native is 0) | +0.03209 to +0.04057 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9978 | 0.9984 | +0.1% | -0.01522 to +0.01648 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 667.2 | 684.7 | +2.6% | +0.9221 to +33.99 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.656 | 9.219 | +6.5% | +0.1319 to +0.9927 | yes: power given |
| pods started | 4.7 | 4.6 | -2.1% | -1.137 to +0.9366 | no |
| pod start wait, total (s) | 7.6 | 6.1 | -19.7% | -3.666 to +0.6657 | no |
| pod start wait, mean (s) | 1.632 | 1.387 | -15.0% | -0.6594 to +0.1694 | no |
| host CPU busy, the real machine under kind (%) | 29.81 | 30.03 | +0.7% | -0.2237 to +0.6573 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.452e-16 to +1.609e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.511 | -0.5% | -0.01608 to +0.002076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.3 | -0.6% | -1.799 to -0.02545 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 159.3 | -0.6% | -1.799 to -0.02545 | yes: GAIN |
| response time (ms), mean | 173.4 | 88.48 | -49.0% | -103.6 to -66.2 | yes: GAIN |
| response time (ms), 95th percentile | 400.3 | 135.3 | -66.2% | -322.7 to -207.4 | yes: GAIN |
| response time (ms), 99th percentile | 654.7 | 194.3 | -70.3% | -556.3 to -364.4 | yes: GAIN |
| time over the response line (% of samples) | 2.958 | 0.04871 | -98.4% | -3.978 to -1.84 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3 | 0 | -100.0% | -4.216 to -1.784 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.8 | +24.8 (native is 0) | +18.44 to +31.16 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.16 | +52.4% | -0.06316 to +0.1732 | no |
| utilisation (used / allocatable) | 0.04158 | 0.04082 | -1.8% | -0.00147 to -4.24e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9978 | 0.9797 | -1.8% | -0.03529 to -0.001018 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06983 | +0.0698 (native is 0) | +0.06142 to +0.07824 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9978 | 1.049 | +5.2% | +0.03629 to +0.06706 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 667.2 | 673.8 | +1.0% | -10.68 to +23.79 | no |
| HPA replicas, mean | 8.656 | 9.346 | +8.0% | -0.1242 to +1.504 | no |
| pods started | 4.7 | 5.1 | +8.5% | -1.941 to +2.741 | no |
| pod start wait, total (s) | 7.6 | 8.6 | +13.2% | -2.845 to +4.845 | no |
| pod start wait, mean (s) | 1.632 | 1.742 | +6.7% | -0.2715 to +0.4915 | no |
| host CPU busy, the real machine under kind (%) | 29.81 | 31.6 | +6.0% | +1.293 to +2.285 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 60 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.286e-16 to +9.063e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.517 | +0.1% | -0.003455 to +0.007788 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.7 | +0.2% | -0.3414 to +0.8694 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.7 | +0.2% | -0.3414 to +0.8694 | no |
| response time (ms), mean | 86.85 | 86.81 | -0.0% | -1.342 to +1.271 | no |
| response time (ms), 95th percentile | 130.9 | 132.2 | +1.0% | -1.985 to +4.526 | no |
| response time (ms), 99th percentile | 184.9 | 181.2 | -2.0% | -26.52 to +19.06 | no |
| time over the response line (% of samples) | 0.0119 | 0.03636 | +205.5% | -0.06489 to +0.1138 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 17.9 | -8.7% | -3.887 to +0.4866 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.1633 | +50.8% | -0.2327 to +0.3427 | no |
| utilisation (used / allocatable) | 0.03963 | 0.03966 | +0.1% | -0.000556 to +0.0006062 | no |
| CPU used (cores), mean | 0.9512 | 0.9518 | +0.1% | -0.01335 to +0.01455 | no |
| Omni's own CPU (cores), mean | 0.0253 | 0.00886 | -65.0% | -0.01879 to -0.01409 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9765 | 0.9607 | -1.6% | -0.03118 to -0.0004987 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.6 | 690.7 | -0.7% | -19.58 to +9.961 | no |
| HPA replicas, mean | 9.199 | 8.471 | -7.9% | -1.055 to -0.4006 | yes: GAIN |
| pods started | 3.8 | 3.7 | -2.6% | -1.02 to +0.8204 | no |
| pod start wait, total (s) | 6 | 5.5 | -8.3% | -2.26 to +1.26 | no |
| pod start wait, mean (s) | 1.512 | 1.448 | -4.2% | -0.4363 to +0.3097 | no |
| host CPU busy, the real machine under kind (%) | 29.5 | 28.95 | -1.9% | -1.117 to +0.01492 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 10 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 10 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.148e-16 to +1.403e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.516 | +0.0% | -0.006952 to +0.007285 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.6 | +0.1% | -0.63 to +0.94 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.6 | +0.1% | -0.63 to +0.94 | no |
| response time (ms), mean | 86.85 | 87.36 | +0.6% | -0.9558 to +1.979 | no |
| response time (ms), 95th percentile | 130.9 | 132.4 | +1.1% | -1.79 to +4.777 | no |
| response time (ms), 99th percentile | 184.9 | 180.9 | -2.2% | -22.63 to +14.61 | no |
| time over the response line (% of samples) | 0.0119 | 0.07295 | +512.8% | -0.01258 to +0.1347 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 22.2 | +13.3% | -1.435 to +6.635 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 60 | -33.3% | -78.28 to +18.28 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.3733 | +244.6% | -0.01849 to +0.5485 | no |
| utilisation (used / allocatable) | 0.03963 | 0.04009 | +1.1% | -0.0002401 to +0.001149 | no |
| CPU used (cores), mean | 0.9512 | 0.9621 | +1.1% | -0.005764 to +0.02758 | no |
| Omni's own CPU (cores), mean | 0.0253 | 0.03633 | +43.6% | +0.009469 to +0.01259 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9765 | 0.9984 | +2.2% | +0.004908 to +0.03896 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.6 | 684.7 | -1.6% | -26.83 to +5.121 | no |
| HPA replicas, mean | 9.199 | 9.219 | +0.2% | -0.5123 to +0.5522 | no |
| pods started | 3.8 | 4.6 | +21.1% | -0.2556 to +1.856 | no |
| pod start wait, total (s) | 6 | 6.1 | +1.7% | -2.045 to +2.245 | no |
| pod start wait, mean (s) | 1.512 | 1.387 | -8.3% | -0.5207 to +0.2707 | no |
| host CPU busy, the real machine under kind (%) | 29.5 | 30.03 | +1.8% | -0.008341 to +1.063 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## omni deciding every 5 s vs omni at its default, every 15 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.511 | -0.3% | -0.01436 to +0.006031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.3 | -0.1% | -1.129 to +0.8477 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.3 | -0.1% | -1.129 to +0.8477 | no |
| response time (ms), mean | 86.85 | 88.48 | +1.9% | -0.0479 to +3.308 | no |
| response time (ms), 95th percentile | 130.9 | 135.3 | +3.3% | +0.1925 to +8.49 | yes: LOSS |
| response time (ms), 99th percentile | 184.9 | 194.3 | +5.1% | -10.25 to +29.05 | no |
| time over the response line (% of samples) | 0.0119 | 0.04871 | +309.2% | -0.03475 to +0.1084 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 24.8 | +26.5% | -0.9144 to +11.31 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 85 | -5.6% | -40.57 to +30.57 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.16 | +47.7% | -0.1831 to +0.2864 | no |
| utilisation (used / allocatable) | 0.03963 | 0.04082 | +3.0% | +0.0004585 to +0.001913 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9512 | 0.9797 | +3.0% | +0.011 to +0.0459 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.0253 | 0.06983 | +176.0% | +0.03912 to +0.04994 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9765 | 1.049 | +7.5% | +0.053 to +0.09296 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.6 | 673.8 | -3.1% | -38.49 to -5.019 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.199 | 9.346 | +1.6% | -0.7427 to +1.037 | no |
| pods started | 3.8 | 5.1 | +34.2% | -0.2099 to +2.81 | no |
| pod start wait, total (s) | 6 | 8.6 | +43.3% | -0.4942 to +5.694 | no |
| pod start wait, mean (s) | 1.512 | 1.742 | +15.2% | -0.165 to +0.625 | no |
| host CPU busy, the real machine under kind (%) | 29.5 | 31.6 | +7.1% | +1.408 to +2.791 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*