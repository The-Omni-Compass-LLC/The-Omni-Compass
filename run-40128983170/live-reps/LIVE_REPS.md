# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.516 | 1.515 | 1.515 | 1.516 | 1.517 | 1.516 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.6 | 158.5 | 158.5 | 158.7 | 158.8 | 158.6 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.6 | 158.5 | 158.5 | 158.7 | 158.8 | 158.6 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 145.3 | 76.35 | 75.82 | 75.59 | 76.6 | 77.13 | 76 | 76.67 |
| response time (ms), 95th percentile | 315.4 | 110.1 | 110.5 | 110.3 | 109.8 | 111.7 | 111 | 112.1 |
| response time (ms), 99th percentile | 503.4 | 144.3 | 149.8 | 139.5 | 143.9 | 156.3 | 146.2 | 154.2 |
| time over the response line (% of samples) | 1.417 | 0.01212 | 0 | 0.01212 | 0 | 0.03651 | 0.03636 | 0.02424 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | 16.1 | 18.8 | 17.2 | 17.5 | 20.6 | 20 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 70 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1067 | 0.16 | 0.1317 | 0.1333 | 0.235 | 0.165 | 0.1583 |
| utilisation (used / allocatable) | 0.0373 | 0.03577 | 0.03539 | 0.03535 | 0.03597 | 0.03606 | 0.03562 | 0.03588 |
| CPU used (cores), mean | 0.8951 | 0.8584 | 0.8493 | 0.8485 | 0.8633 | 0.8653 | 0.8549 | 0.8611 |
| Omni's own CPU (cores), mean | 0 | 0.00766 | 0.00546 | 0.00617 | 0.00668 | 0.01254 | 0.02199 | 0.06017 |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.8661 | 0.8547 | 0.8546 | 0.87 | 0.8779 | 0.8769 | 0.9213 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 765.9 | 778.1 | 776.8 | 764.8 | 762.6 | 766.8 | 768.1 |
| HPA replicas, mean | 8.415 | 8.268 | 8.174 | 8.311 | 7.588 | 7.723 | 8.507 | 8.18 |
| pods started | 5.5 | 3.5 | 4.7 | 4.4 | 4.1 | 4.2 | 5.4 | 4.3 |
| pod start wait, total (s) | 8 | 5.6 | 6.6 | 6.1 | 6 | 6.8 | 8.4 | 6.3 |
| pod start wait, mean (s) | 1.466 | 1.6 | 1.412 | 1.425 | 1.503 | 1.617 | 1.546 | 1.507 |
| host CPU busy, the real machine under kind (%) | 26.86 | 26.04 | 25.8 | 25.9 | 26.09 | 26.53 | 26.57 | 27.97 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | +0.0006 to +0.0021 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.6 | −0.1% | −0.5128 to +0.0900 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.6 | −0.1% | −0.5128 to +0.0900 | no |
| response time (ms), mean | 145.3 | 76.35 | −47.5% | −90.7978 to −47.1568 | yes: GAIN |
| response time (ms), 95th percentile | 315.4 | 110.1 | −65.1% | −257.9669 to −152.6201 | yes: GAIN |
| response time (ms), 99th percentile | 503.4 | 144.3 | −71.3% | −466.3565 to −251.8393 | yes: GAIN |
| time over the response line (% of samples) | 1.417 | 0.01212 | −99.1% | −2.4631 to −0.3475 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.4228 to −0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +15.3498 to +20.2502 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1067 | +36.2% | −0.1416 to +0.1982 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03577 | −4.1% | −0.0027 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8951 | 0.8584 | −4.1% | −0.0643 to −0.0092 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00766 | +0.008 (native is 0) | +0.0066 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.8661 | −3.2% | −0.0556 to −0.0025 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 765.9 | +2.6% | +1.2373 to +37.8686 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.415 | 8.268 | −1.7% | −0.7516 to +0.4575 | no |
| pods started | 5.5 | 3.5 | −36.4% | −2.9537 to −1.0463 | yes: GAIN |
| pod start wait, total (s) | 8 | 5.6 | −30.0% | −4.6920 to −0.1080 | yes: GAIN |
| pod start wait, mean (s) | 1.466 | 1.6 | +9.1% | −0.3241 to +0.5917 | no |
| host CPU busy, the real machine under kind (%) | 26.86 | 26.04 | −3.0% | −1.4345 to −0.1984 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.515 | +0.0% | −0.0015 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.5 | −0.2% | −0.7564 to +0.0226 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.5 | −0.2% | −0.7564 to +0.0226 | no |
| response time (ms), mean | 145.3 | 75.82 | −47.8% | −91.2384 to −47.7748 | yes: GAIN |
| response time (ms), 95th percentile | 315.4 | 110.5 | −65.0% | −256.4906 to −153.2504 | yes: GAIN |
| response time (ms), 99th percentile | 503.4 | 149.8 | −70.2% | −460.2065 to −247.0835 | yes: GAIN |
| time over the response line (% of samples) | 1.417 | 0 | −100.0% | −2.4785 to −0.3563 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.4228 to −0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.1 | +16.100 (native is 0) | +15.1198 to +17.0802 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.16 | +104.3% | −0.1403 to +0.3037 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03539 | −5.1% | −0.0028 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8951 | 0.8493 | −5.1% | −0.0670 to −0.0247 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00546 | +0.005 (native is 0) | +0.0047 to +0.0062 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.8547 | −4.5% | −0.0609 to −0.0199 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 778.1 | +4.3% | +23.0812 to +40.5366 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.415 | 8.174 | −2.9% | −0.4448 to −0.0384 | yes: GAIN |
| pods started | 5.5 | 4.7 | −14.5% | −1.5388 to −0.0612 | yes: GAIN |
| pod start wait, total (s) | 8 | 6.6 | −17.5% | −3.4841 to +0.6841 | no |
| pod start wait, mean (s) | 1.466 | 1.412 | −3.7% | −0.3409 to +0.2319 | no |
| host CPU busy, the real machine under kind (%) | 26.86 | 25.8 | −4.0% | −1.6100 to −0.5184 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.515 | +0.1% | −0.0003 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.5 | −0.2% | −0.6143 to −0.1026 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.5 | −0.2% | −0.6143 to −0.1026 | yes: GAIN |
| response time (ms), mean | 145.3 | 75.59 | −48.0% | −91.6735 to −47.7956 | yes: GAIN |
| response time (ms), 95th percentile | 315.4 | 110.3 | −65.0% | −257.6147 to −152.5633 | yes: GAIN |
| response time (ms), 99th percentile | 503.4 | 139.5 | −72.3% | −470.4348 to −257.4530 | yes: GAIN |
| time over the response line (% of samples) | 1.417 | 0.01212 | −99.1% | −2.4544 to −0.3562 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.4228 to −0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | +18.800 (native is 0) | +17.5028 to +20.0972 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1317 | +68.1% | −0.1598 to +0.2664 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03535 | −5.2% | −0.0029 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8951 | 0.8485 | −5.2% | −0.0687 to −0.0247 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00617 | +0.006 (native is 0) | +0.0054 to +0.0070 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.8546 | −4.5% | −0.0618 to −0.0193 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 776.8 | +4.1% | +15.6909 to +45.1912 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.415 | 8.311 | −1.2% | −0.3531 to +0.1440 | no |
| pods started | 5.5 | 4.4 | −20.0% | −2.1900 to −0.0100 | yes: GAIN |
| pod start wait, total (s) | 8 | 6.1 | −23.8% | −4.3187 to +0.5187 | no |
| pod start wait, mean (s) | 1.466 | 1.425 | −2.8% | −0.3963 to +0.3139 | no |
| host CPU busy, the real machine under kind (%) | 26.86 | 25.9 | −3.6% | −1.6108 to −0.3021 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0008 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.7 | −0.1% | −0.5414 to +0.2575 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.7 | −0.1% | −0.5414 to +0.2575 | no |
| response time (ms), mean | 145.3 | 76.6 | −47.3% | −90.7212 to −46.7302 | yes: GAIN |
| response time (ms), 95th percentile | 315.4 | 109.8 | −65.2% | −258.6239 to −152.5751 | yes: GAIN |
| response time (ms), 99th percentile | 503.4 | 143.9 | −71.4% | −472.8496 to −246.2966 | yes: GAIN |
| time over the response line (% of samples) | 1.417 | 0 | −100.0% | −2.4785 to −0.3563 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.4228 to −0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 | +17.200 (native is 0) | +13.9342 to +20.4658 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1333 | +70.2% | −0.1200 to +0.2300 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03597 | −3.6% | −0.0023 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8951 | 0.8633 | −3.6% | −0.0547 to −0.0090 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00668 | +0.007 (native is 0) | +0.0056 to +0.0078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.87 | −2.8% | −0.0473 to −0.0031 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 764.8 | +2.5% | −8.5380 to +45.5430 | no |
| HPA replicas, mean | 8.415 | 7.588 | −9.8% | −1.4605 to −0.1942 | yes: GAIN |
| pods started | 5.5 | 4.1 | −25.5% | −2.3048 to −0.4952 | yes: GAIN |
| pod start wait, total (s) | 8 | 6 | −25.0% | −3.9075 to −0.0925 | yes: GAIN |
| pod start wait, mean (s) | 1.466 | 1.503 | +2.5% | −0.3736 to +0.4479 | no |
| host CPU busy, the real machine under kind (%) | 26.86 | 26.09 | −2.9% | −1.5235 to −0.0184 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.517 | +0.2% | +0.0007 to +0.0043 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.8 | −0.0% | −0.3941 to +0.3730 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.8 | −0.0% | −0.3941 to +0.3730 | no |
| response time (ms), mean | 145.3 | 77.13 | −46.9% | −89.9186 to −46.4704 | yes: GAIN |
| response time (ms), 95th percentile | 315.4 | 111.7 | −64.6% | −256.6340 to −150.6680 | yes: GAIN |
| response time (ms), 99th percentile | 503.4 | 156.3 | −69.0% | −453.9456 to −240.4014 | yes: GAIN |
| time over the response line (% of samples) | 1.417 | 0.03651 | −97.4% | −2.4149 to −0.3469 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.4228 to −0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.500 (native is 0) | +14.0571 to +20.9429 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.235 | +200.0% | −0.0654 to +0.3787 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03606 | −3.3% | −0.0022 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8951 | 0.8653 | −3.3% | −0.0528 to −0.0068 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01254 | +0.013 (native is 0) | +0.0108 to +0.0143 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.8779 | −1.9% | −0.0388 to +0.0042 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 762.6 | +2.2% | −2.4952 to +35.0169 | no |
| HPA replicas, mean | 8.415 | 7.723 | −8.2% | −1.2698 to −0.1155 | yes: GAIN |
| pods started | 5.5 | 4.2 | −23.6% | −2.3690 to −0.2310 | yes: GAIN |
| pod start wait, total (s) | 8 | 6.8 | −15.0% | −3.6962 to +1.2962 | no |
| pod start wait, mean (s) | 1.466 | 1.617 | +10.3% | −0.2118 to +0.5127 | no |
| host CPU busy, the real machine under kind (%) | 26.86 | 26.53 | −1.2% | −0.9110 to +0.2595 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0002 to +0.0039 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.6 | −0.1% | −0.6589 to +0.2620 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.6 | −0.1% | −0.6589 to +0.2620 | no |
| response time (ms), mean | 145.3 | 76 | −47.7% | −91.3124 to −47.3375 | yes: GAIN |
| response time (ms), 95th percentile | 315.4 | 111 | −64.8% | −257.1351 to −151.6979 | yes: GAIN |
| response time (ms), 99th percentile | 503.4 | 146.2 | −71.0% | −467.7775 to −246.6571 | yes: GAIN |
| time over the response line (% of samples) | 1.417 | 0.03636 | −97.4% | −2.4144 to −0.3477 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.4228 to −0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.6 | +20.600 (native is 0) | +18.8740 to +22.3260 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.165 | +110.6% | −0.1563 to +0.3297 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03562 | −4.5% | −0.0029 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8951 | 0.8549 | −4.5% | −0.0698 to −0.0107 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02199 | +0.022 (native is 0) | +0.0191 to +0.0249 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.8769 | −2.0% | −0.0459 to +0.0093 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 766.8 | +2.7% | −11.9106 to +52.8355 | no |
| HPA replicas, mean | 8.415 | 8.507 | +1.1% | −0.1878 to +0.3708 | no |
| pods started | 5.5 | 5.4 | −1.8% | −1.0204 to +0.8204 | no |
| pod start wait, total (s) | 8 | 8.4 | +5.0% | −3.0750 to +3.8750 | no |
| pod start wait, mean (s) | 1.466 | 1.546 | +5.5% | −0.4266 to +0.5866 | no |
| host CPU busy, the real machine under kind (%) | 26.86 | 26.57 | −1.1% | −1.1376 to +0.5592 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0056 to +0.0053 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.5 | −0.2% | −0.9279 to +0.2934 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.5 | −0.2% | −0.9279 to +0.2934 | no |
| response time (ms), mean | 145.3 | 76.67 | −47.2% | −90.1040 to −47.2150 | yes: GAIN |
| response time (ms), 95th percentile | 315.4 | 112.1 | −64.5% | −254.6297 to −151.9243 | yes: GAIN |
| response time (ms), 99th percentile | 503.4 | 154.2 | −69.4% | −449.4302 to −249.0758 | yes: GAIN |
| time over the response line (% of samples) | 1.417 | 0.02424 | −98.3% | −2.4300 to −0.3563 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 | 0 | −100.0% | −2.4228 to −0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20 | +20.000 (native is 0) | +17.5452 to +22.4548 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.1583 | +102.1% | −0.0982 to +0.2582 | no |
| utilisation (used / allocatable) | 0.0373 | 0.03588 | −3.8% | −0.0021 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8951 | 0.8611 | −3.8% | −0.0513 to −0.0168 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06017 | +0.060 (native is 0) | +0.0515 to +0.0688 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8951 | 0.9213 | +2.9% | +0.0130 to +0.0392 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.3 | 768.1 | +2.9% | +9.0879 to +34.5232 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.415 | 8.18 | −2.8% | −0.9160 to +0.4460 | no |
| pods started | 5.5 | 4.3 | −21.8% | −2.4972 to +0.0972 | no |
| pod start wait, total (s) | 8 | 6.3 | −21.3% | −5.0047 to +1.6047 | no |
| pod start wait, mean (s) | 1.466 | 1.507 | +2.8% | −0.4328 to +0.5137 | no |
| host CPU busy, the real machine under kind (%) | 26.86 | 27.97 | +4.1% | +0.6294 to +1.5894 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.516 | 1.515 | −0.0% | −0.0027 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −0.4335 to +0.1226 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −0.4335 to +0.1226 | no |
| response time (ms), mean | 76.35 | 75.82 | −0.7% | −1.4650 to +0.4063 | no |
| response time (ms), 95th percentile | 110.1 | 110.5 | +0.4% | −2.1495 to +2.9955 | no |
| response time (ms), 99th percentile | 144.3 | 149.8 | +3.8% | −12.4637 to +23.3695 | no |
| time over the response line (% of samples) | 0.01212 | 0 | −100.0% | −0.0395 to +0.0153 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.8 | 16.1 | −9.6% | −3.8072 to +0.4072 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.16 | +50.0% | −0.1632 to +0.2699 | no |
| utilisation (used / allocatable) | 0.03577 | 0.03539 | −1.1% | −0.0008 to +0.0000 | no |
| CPU used (cores), mean | 0.8584 | 0.8493 | −1.1% | −0.0195 to +0.0012 | no |
| Omni's own CPU (cores), mean | 0.00766 | 0.00546 | −28.7% | −0.0026 to −0.0018 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8661 | 0.8547 | −1.3% | −0.0216 to −0.0011 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.9 | 778.1 | +1.6% | −1.1072 to +25.6191 | no |
| HPA replicas, mean | 8.268 | 8.174 | −1.1% | −0.5940 to +0.4049 | no |
| pods started | 3.5 | 4.7 | +34.3% | +0.3879 to +2.0121 | yes: power given |
| pod start wait, total (s) | 5.6 | 6.6 | +17.9% | −0.8159 to +2.8159 | no |
| pod start wait, mean (s) | 1.6 | 1.412 | −11.8% | −0.6195 to +0.2428 | no |
| host CPU busy, the real machine under kind (%) | 26.04 | 25.8 | −1.0% | −0.4212 to −0.0742 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.516 | 1.515 | −0.0% | −0.0013 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −0.3441 to +0.0501 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −0.3441 to +0.0501 | no |
| response time (ms), mean | 76.35 | 75.59 | −1.0% | −1.5469 to +0.0323 | no |
| response time (ms), 95th percentile | 110.1 | 110.3 | +0.2% | −1.1782 to +1.5872 | no |
| response time (ms), 99th percentile | 144.3 | 139.5 | −3.4% | −18.1998 to +8.5078 | no |
| time over the response line (% of samples) | 0.01212 | 0.01212 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.8 | 18.8 | +5.6% | −1.6551 to +3.6551 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1317 | +23.4% | −0.2497 to +0.2997 | no |
| utilisation (used / allocatable) | 0.03577 | 0.03535 | −1.2% | −0.0009 to +0.0001 | no |
| CPU used (cores), mean | 0.8584 | 0.8485 | −1.2% | −0.0225 to +0.0026 | no |
| Omni's own CPU (cores), mean | 0.00766 | 0.00617 | −19.5% | −0.0018 to −0.0011 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8661 | 0.8546 | −1.3% | −0.0239 to +0.0010 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.9 | 776.8 | +1.4% | −0.8521 to +22.6283 | no |
| HPA replicas, mean | 8.268 | 8.311 | +0.5% | −0.5337 to +0.6187 | no |
| pods started | 3.5 | 4.4 | +25.7% | −0.3818 to +2.1818 | no |
| pod start wait, total (s) | 5.6 | 6.1 | +8.9% | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 1.6 | 1.425 | −10.9% | −0.5670 to +0.2170 | no |
| host CPU busy, the real machine under kind (%) | 26.04 | 25.9 | −0.5% | −0.3700 to +0.0901 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | +0.0% | −0.0021 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.7 | +0.0% | −0.2794 to +0.4183 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.7 | +0.0% | −0.2794 to +0.4183 | no |
| response time (ms), mean | 76.35 | 76.6 | +0.3% | −0.7079 to +1.2111 | no |
| response time (ms), 95th percentile | 110.1 | 109.8 | −0.3% | −1.9643 to +1.3523 | no |
| response time (ms), 99th percentile | 144.3 | 143.9 | −0.3% | −12.0698 to +11.1194 | no |
| time over the response line (% of samples) | 0.01212 | 0 | −100.0% | −0.0395 to +0.0153 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.8 | 17.2 | −3.4% | −2.9410 to +1.7410 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1333 | +25.0% | −0.1404 to +0.1937 | no |
| utilisation (used / allocatable) | 0.03577 | 0.03597 | +0.6% | −0.0006 to +0.0010 | no |
| CPU used (cores), mean | 0.8584 | 0.8633 | +0.6% | −0.0141 to +0.0239 | no |
| Omni's own CPU (cores), mean | 0.00766 | 0.00668 | −12.8% | −0.0011 to −0.0009 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8661 | 0.87 | +0.4% | −0.0151 to +0.0229 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.9 | 764.8 | −0.1% | −24.3016 to +22.2008 | no |
| HPA replicas, mean | 8.268 | 7.588 | −8.2% | −1.1627 to −0.1979 | yes: GAIN |
| pods started | 3.5 | 4.1 | +17.1% | −0.4228 to +1.6228 | no |
| pod start wait, total (s) | 5.6 | 6 | +7.1% | −1.6841 to +2.4841 | no |
| pod start wait, mean (s) | 1.6 | 1.503 | −6.0% | −0.5672 to +0.3739 | no |
| host CPU busy, the real machine under kind (%) | 26.04 | 26.09 | +0.2% | −0.4039 to +0.4950 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.516 | 1.517 | +0.1% | −0.0004 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.8 | +0.1% | −0.0486 to +0.4503 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.8 | +0.1% | −0.0486 to +0.4503 | no |
| response time (ms), mean | 76.35 | 77.13 | +1.0% | −0.8523 to +2.4179 | no |
| response time (ms), 95th percentile | 110.1 | 111.7 | +1.5% | −1.1583 to +4.4433 | no |
| response time (ms), 99th percentile | 144.3 | 156.3 | +8.3% | +3.3745 to +20.4743 | yes: LOSS |
| time over the response line (% of samples) | 0.01212 | 0.03651 | +201.2% | −0.0308 to +0.0796 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.8 | 17.5 | −1.7% | −2.8912 to +2.2912 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.235 | +120.3% | −0.1102 to +0.3669 | no |
| utilisation (used / allocatable) | 0.03577 | 0.03606 | +0.8% | −0.0004 to +0.0010 | no |
| CPU used (cores), mean | 0.8584 | 0.8653 | +0.8% | −0.0107 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0.00766 | 0.01254 | +63.7% | +0.0041 to +0.0056 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8661 | 0.8779 | +1.4% | −0.0061 to +0.0297 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.9 | 762.6 | −0.4% | −17.6547 to +11.0705 | no |
| HPA replicas, mean | 8.268 | 7.723 | −6.6% | −1.0786 to −0.0126 | yes: GAIN |
| pods started | 3.5 | 4.2 | +20.0% | −0.3144 to +1.7144 | no |
| pod start wait, total (s) | 5.6 | 6.8 | +21.4% | −0.9539 to +3.3539 | no |
| pod start wait, mean (s) | 1.6 | 1.617 | +1.0% | −0.4210 to +0.4543 | no |
| host CPU busy, the real machine under kind (%) | 26.04 | 26.53 | +1.9% | +0.0207 to +0.9608 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | +0.0% | −0.0014 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.6 | +0.0% | −0.2994 to +0.3254 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.6 | +0.0% | −0.2994 to +0.3254 | no |
| response time (ms), mean | 76.35 | 76 | −0.5% | −1.6242 to +0.9289 | no |
| response time (ms), 95th percentile | 110.1 | 111 | +0.8% | −1.3514 to +3.1054 | no |
| response time (ms), 99th percentile | 144.3 | 146.2 | +1.3% | −17.6414 to +21.4026 | no |
| time over the response line (% of samples) | 0.01212 | 0.03636 | +200.0% | −0.0123 to +0.0608 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.8 | 20.6 | +15.7% | −0.5347 to +6.1347 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.165 | +54.7% | −0.2822 to +0.3989 | no |
| utilisation (used / allocatable) | 0.03577 | 0.03562 | −0.4% | −0.0008 to +0.0005 | no |
| CPU used (cores), mean | 0.8584 | 0.8549 | −0.4% | −0.0194 to +0.0123 | no |
| Omni's own CPU (cores), mean | 0.00766 | 0.02199 | +187.1% | +0.0125 to +0.0162 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8661 | 0.8769 | +1.2% | −0.0057 to +0.0273 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.9 | 766.8 | +0.1% | −20.5746 to +22.3936 | no |
| HPA replicas, mean | 8.268 | 8.507 | +2.9% | −0.3649 to +0.8421 | no |
| pods started | 3.5 | 5.4 | +54.3% | +0.8100 to +2.9900 | yes: power given |
| pod start wait, total (s) | 5.6 | 8.4 | +50.0% | +0.2811 to +5.3189 | yes: LOSS |
| pod start wait, mean (s) | 1.6 | 1.546 | −3.4% | −0.3977 to +0.2901 | no |
| host CPU busy, the real machine under kind (%) | 26.04 | 26.57 | +2.0% | +0.0342 to +1.0204 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.514 | −0.1% | −0.0073 to +0.0043 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −0.6573 to +0.4457 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −0.6573 to +0.4457 | no |
| response time (ms), mean | 76.35 | 76.67 | +0.4% | −0.3814 to +1.0169 | no |
| response time (ms), 95th percentile | 110.1 | 112.1 | +1.8% | +0.1073 to +3.9257 | yes: LOSS |
| response time (ms), 99th percentile | 144.3 | 154.2 | +6.8% | −0.3273 to +20.0171 | no |
| time over the response line (% of samples) | 0.01212 | 0.02424 | +100.0% | −0.0371 to +0.0613 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.8 | 20 | +12.4% | +0.4544 to +3.9456 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1583 | +48.4% | −0.1997 to +0.3030 | no |
| utilisation (used / allocatable) | 0.03577 | 0.03588 | +0.3% | −0.0006 to +0.0008 | no |
| CPU used (cores), mean | 0.8584 | 0.8611 | +0.3% | −0.0143 to +0.0196 | no |
| Omni's own CPU (cores), mean | 0.00766 | 0.06017 | +685.5% | +0.0450 to +0.0601 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8661 | 0.9213 | +6.4% | +0.0319 to +0.0785 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.9 | 768.1 | +0.3% | −10.3515 to +14.8567 | no |
| HPA replicas, mean | 8.268 | 8.18 | −1.1% | −0.3352 to +0.1594 | no |
| pods started | 3.5 | 4.3 | +22.9% | −0.2003 to +1.8003 | no |
| pod start wait, total (s) | 5.6 | 6.3 | +12.5% | −1.3525 to +2.7525 | no |
| pod start wait, mean (s) | 1.6 | 1.507 | −5.8% | −0.5294 to +0.3427 | no |
| host CPU busy, the real machine under kind (%) | 26.04 | 27.97 | +7.4% | +1.4143 to +2.4374 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*