# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.518 | 1.516 | 1.518 | 1.516 | 1.521 | 1.521 | 1.517 | 1.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | 158.7 | 158.5 | 159 | 159.2 | 158.7 | 157.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | 158.7 | 158.5 | 159 | 159.2 | 158.7 | 157.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 144.2 | 75.68 | 75.07 | 76.06 | 75.55 | 75.91 | 75.95 | 76.11 |
| response time (ms), 95th percentile | 329.7 | 115.6 | 113.5 | 114.8 | 114.7 | 115.7 | 115.6 | 116.1 |
| response time (ms), 99th percentile | 526.3 | 155.2 | 155.9 | 154.7 | 165.1 | 161.5 | 160.1 | 161.3 |
| time over the response line (% of samples) | 2.172 | 0.01212 | 0.01212 | 0.02424 | 0.02424 | 0.01212 | 0.01212 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.1 | 15 | 16.6 | 15.6 | 15.3 | 19.3 | 19.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 90 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2917 | 0.3467 | 0 | 0.185 | 0.21 | 0.1583 | 0.185 |
| utilisation (used / allocatable) | 0.03657 | 0.03512 | 0.03494 | 0.03533 | 0.03493 | 0.03535 | 0.03537 | 0.03577 |
| CPU used (cores), mean | 0.8778 | 0.8428 | 0.8386 | 0.848 | 0.8384 | 0.8484 | 0.8488 | 0.8586 |
| Omni's own CPU (cores), mean | 0 | 0.00809 | 0.00574 | 0.00633 | 0.00692 | 0.01293 | 0.02328 | 0.06381 |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.8509 | 0.8444 | 0.8543 | 0.8453 | 0.8613 | 0.872 | 0.9224 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 805.2 | 809.8 | 805.4 | 812.3 | 796.4 | 793.5 | 795.8 |
| HPA replicas, mean | 8.138 | 7.66 | 7.931 | 8.232 | 7.349 | 7.141 | 8.482 | 8.292 |
| pods started | 5.2 | 3.8 | 3.8 | 3.4 | 3.4 | 3.4 | 3.6 | 3.9 |
| pod start wait, total (s) | 7.1 | 6.5 | 5.6 | 5.3 | 5.4 | 4.9 | 4.8 | 5.8 |
| pod start wait, mean (s) | 1.403 | 1.755 | 1.47 | 1.605 | 1.562 | 1.445 | 1.387 | 1.42 |
| host CPU busy, the real machine under kind (%) | 26.45 | 25.84 | 25.49 | 25.77 | 25.6 | 25.99 | 26.41 | 28 |
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
| node-hours | 1.518 | 1.516 | −0.1% | −0.0075 to +0.0048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −1.2500 to +0.2787 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −1.2500 to +0.2787 | no |
| response time (ms), mean | 144.2 | 75.68 | −47.5% | −97.5853 to −39.3825 | yes: GAIN |
| response time (ms), 95th percentile | 329.7 | 115.6 | −65.0% | −289.9911 to −138.3559 | yes: GAIN |
| response time (ms), 99th percentile | 526.3 | 155.2 | −70.5% | −508.2521 to −233.9521 | yes: GAIN |
| time over the response line (% of samples) | 2.172 | 0.01212 | −99.4% | −3.5270 to −0.7932 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.1 | +16.100 (native is 0) | +13.3102 to +18.8898 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2917 | +82.3% | −0.1695 to +0.4329 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03512 | −4.0% | −0.0027 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8778 | 0.8428 | −4.0% | −0.0657 to −0.0043 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00809 | +0.008 (native is 0) | +0.0067 to +0.0095 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.8509 | −3.1% | −0.0564 to +0.0026 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 805.2 | +1.5% | −12.2018 to +35.7063 | no |
| HPA replicas, mean | 8.138 | 7.66 | −5.9% | −1.0368 to +0.0808 | no |
| pods started | 5.2 | 3.8 | −26.9% | −2.4228 to −0.3772 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 6.5 | −8.5% | −2.9410 to +1.7410 | no |
| pod start wait, mean (s) | 1.403 | 1.755 | +25.0% | −0.0115 to +0.7138 | no |
| host CPU busy, the real machine under kind (%) | 26.45 | 25.84 | −2.3% | −1.4481 to +0.2298 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.518 | +0.1% | −0.0006 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.7 | −0.2% | −0.6653 to +0.0663 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.7 | −0.2% | −0.6653 to +0.0663 | no |
| response time (ms), mean | 144.2 | 75.07 | −47.9% | −98.3234 to −39.8691 | yes: GAIN |
| response time (ms), 95th percentile | 329.7 | 113.5 | −65.6% | −292.6542 to −139.8598 | yes: GAIN |
| response time (ms), 99th percentile | 526.3 | 155.9 | −70.4% | −514.4060 to −226.4650 | yes: GAIN |
| time over the response line (% of samples) | 2.172 | 0.01212 | −99.4% | −3.5223 to −0.7978 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 | +15.000 (native is 0) | +12.9489 to +17.0511 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.3467 | +116.7% | −0.1504 to +0.5237 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03494 | −4.5% | −0.0030 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8778 | 0.8386 | −4.5% | −0.0710 to −0.0073 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00574 | +0.006 (native is 0) | +0.0048 to +0.0067 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.8444 | −3.8% | −0.0645 to −0.0023 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 809.8 | +2.1% | −8.1870 to +40.7954 | no |
| HPA replicas, mean | 8.138 | 7.931 | −2.5% | −0.6677 to +0.2545 | no |
| pods started | 5.2 | 3.8 | −26.9% | −2.6707 to −0.1293 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.6 | −21.1% | −4.4637 to +1.4637 | no |
| pod start wait, mean (s) | 1.403 | 1.47 | +4.8% | −0.3112 to +0.4455 | no |
| host CPU busy, the real machine under kind (%) | 26.45 | 25.49 | −3.6% | −1.8719 to −0.0433 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.516 | −0.1% | −0.0113 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −1.3503 to +0.3885 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −1.3503 to +0.3885 | no |
| response time (ms), mean | 144.2 | 76.06 | −47.2% | −96.7835 to −39.4248 | yes: GAIN |
| response time (ms), 95th percentile | 329.7 | 114.8 | −65.2% | −291.1236 to −138.7974 | yes: GAIN |
| response time (ms), 99th percentile | 526.3 | 154.7 | −70.6% | −511.6875 to −231.5317 | yes: GAIN |
| time over the response line (% of samples) | 2.172 | 0.02424 | −98.9% | −3.5166 to −0.7793 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 | +16.600 (native is 0) | +15.2428 to +17.9572 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0 | −100.0% | −0.3443 to +0.0243 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03533 | −3.4% | −0.0026 to +0.0002 | no |
| CPU used (cores), mean | 0.8778 | 0.848 | −3.4% | −0.0634 to +0.0039 | no |
| Omni's own CPU (cores), mean | 0 | 0.00633 | +0.006 (native is 0) | +0.0053 to +0.0073 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.8543 | −2.7% | −0.0564 to +0.0096 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 805.4 | +1.5% | −15.8640 to +39.6800 | no |
| HPA replicas, mean | 8.138 | 8.232 | +1.2% | −0.2407 to +0.4287 | no |
| pods started | 5.2 | 3.4 | −34.6% | −2.9583 to −0.6417 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.3 | −25.4% | −4.0316 to +0.4316 | no |
| pod start wait, mean (s) | 1.403 | 1.605 | +14.4% | −0.1213 to +0.5242 | no |
| host CPU busy, the real machine under kind (%) | 26.45 | 25.77 | −2.6% | −1.5497 to +0.1953 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.521 | +0.2% | −0.0027 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159 | −0.0% | −0.4773 to +0.4423 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159 | −0.0% | −0.4773 to +0.4423 | no |
| response time (ms), mean | 144.2 | 75.55 | −47.6% | −97.6070 to −39.6316 | yes: GAIN |
| response time (ms), 95th percentile | 329.7 | 114.7 | −65.2% | −291.2439 to −138.9031 | yes: GAIN |
| response time (ms), 99th percentile | 526.3 | 165.1 | −68.6% | −493.8579 to −228.5929 | yes: GAIN |
| time over the response line (% of samples) | 2.172 | 0.02424 | −98.9% | −3.5086 to −0.7872 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.6 | +15.600 (native is 0) | +11.9340 to +19.2660 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.185 | +15.6% | −0.2346 to +0.2846 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03493 | −4.5% | −0.0030 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8778 | 0.8384 | −4.5% | −0.0710 to −0.0079 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00692 | +0.007 (native is 0) | +0.0056 to +0.0082 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.8453 | −3.7% | −0.0630 to −0.0020 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 812.3 | +2.4% | −4.4798 to +42.1233 | no |
| HPA replicas, mean | 8.138 | 7.349 | −9.7% | −1.4407 to −0.1367 | yes: GAIN |
| pods started | 5.2 | 3.4 | −34.6% | −2.8003 to −0.7997 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.4 | −23.9% | −4.5423 to +1.1423 | no |
| pod start wait, mean (s) | 1.403 | 1.562 | +11.3% | −0.2580 to +0.5756 | no |
| host CPU busy, the real machine under kind (%) | 26.45 | 25.6 | −3.2% | −1.5874 to −0.0995 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.521 | +0.2% | −0.0018 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.2 | +0.1% | −0.3936 to +0.6575 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.2 | +0.1% | −0.3936 to +0.6575 | no |
| response time (ms), mean | 144.2 | 75.91 | −47.3% | −97.4198 to −39.0982 | yes: GAIN |
| response time (ms), 95th percentile | 329.7 | 115.7 | −64.9% | −290.3501 to −137.6389 | yes: GAIN |
| response time (ms), 99th percentile | 526.3 | 161.5 | −69.3% | −507.3264 to −222.1782 | yes: GAIN |
| time over the response line (% of samples) | 2.172 | 0.01212 | −99.4% | −3.5303 to −0.7898 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.3 | +15.300 (native is 0) | +11.6363 to +18.9637 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.21 | +31.2% | −0.2134 to +0.3134 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03535 | −3.3% | −0.0027 to +0.0003 | no |
| CPU used (cores), mean | 0.8778 | 0.8484 | −3.3% | −0.0649 to +0.0062 | no |
| Omni's own CPU (cores), mean | 0 | 0.01293 | +0.013 (native is 0) | +0.0107 to +0.0151 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.8613 | −1.9% | −0.0500 to +0.0171 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 796.4 | +0.4% | −35.7430 to +41.6956 | no |
| HPA replicas, mean | 8.138 | 7.141 | −12.2% | −1.5409 to −0.4526 | yes: GAIN |
| pods started | 5.2 | 3.4 | −34.6% | −2.6793 to −0.9207 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 4.9 | −31.0% | −4.4820 to +0.0820 | no |
| pod start wait, mean (s) | 1.403 | 1.445 | +3.0% | −0.3347 to +0.4180 | no |
| host CPU busy, the real machine under kind (%) | 26.45 | 25.99 | −1.7% | −1.3867 to +0.4661 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.517 | −0.0% | −0.0061 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.7 | −0.2% | −1.1593 to +0.4718 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.7 | −0.2% | −1.1593 to +0.4718 | no |
| response time (ms), mean | 144.2 | 75.95 | −47.3% | −97.5421 to −38.8963 | yes: GAIN |
| response time (ms), 95th percentile | 329.7 | 115.6 | −64.9% | −290.3879 to −137.8761 | yes: GAIN |
| response time (ms), 99th percentile | 526.3 | 160.1 | −69.6% | −504.6566 to −227.7696 | yes: GAIN |
| time over the response line (% of samples) | 2.172 | 0.01212 | −99.4% | −3.5303 to −0.7898 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +18.1295 to +20.4705 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.1583 | −1.0% | −0.3116 to +0.3082 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03537 | −3.3% | −0.0028 to +0.0004 | no |
| CPU used (cores), mean | 0.8778 | 0.8488 | −3.3% | −0.0664 to +0.0084 | no |
| Omni's own CPU (cores), mean | 0 | 0.02328 | +0.023 (native is 0) | +0.0198 to +0.0268 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.872 | −0.7% | −0.0399 to +0.0285 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 793.5 | +0.0% | −38.4381 to +38.5366 | no |
| HPA replicas, mean | 8.138 | 8.482 | +4.2% | +0.1555 to +0.5318 | yes: power given |
| pods started | 5.2 | 3.6 | −30.8% | −2.9572 to −0.2428 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 4.8 | −32.4% | −4.1790 to −0.4210 | yes: GAIN |
| pod start wait, mean (s) | 1.403 | 1.387 | −1.2% | −0.2604 to +0.2271 | no |
| host CPU busy, the real machine under kind (%) | 26.45 | 26.41 | −0.1% | −0.9654 to +0.8939 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.508 | −0.7% | −0.0189 to −0.0011 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 157.8 | −0.8% | −2.2835 to −0.2013 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 157.8 | −0.8% | −2.2835 to −0.2013 | yes: GAIN |
| response time (ms), mean | 144.2 | 76.11 | −47.2% | −96.7394 to −39.3681 | yes: GAIN |
| response time (ms), 95th percentile | 329.7 | 116.1 | −64.8% | −289.5883 to −137.7617 | yes: GAIN |
| response time (ms), 99th percentile | 526.3 | 161.3 | −69.4% | −498.4454 to −231.6216 | yes: GAIN |
| time over the response line (% of samples) | 2.172 | 0 | −100.0% | −3.5446 to −0.7998 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | −100.0% | −3.5821 to −0.8179 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.9 | +19.900 (native is 0) | +17.5529 to +22.2471 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.185 | +15.6% | −0.2355 to +0.2855 | no |
| utilisation (used / allocatable) | 0.03657 | 0.03577 | −2.2% | −0.0018 to +0.0002 | no |
| CPU used (cores), mean | 0.8778 | 0.8586 | −2.2% | −0.0439 to +0.0055 | no |
| Omni's own CPU (cores), mean | 0 | 0.06381 | +0.064 (native is 0) | +0.0535 to +0.0741 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8778 | 0.9224 | +5.1% | +0.0268 to +0.0624 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 793.5 | 795.8 | +0.3% | −23.3094 to +28.0521 | no |
| HPA replicas, mean | 8.138 | 8.292 | +1.9% | −0.0684 to +0.3765 | no |
| pods started | 5.2 | 3.9 | −25.0% | −2.0578 to −0.5422 | yes: GAIN |
| pod start wait, total (s) | 7.1 | 5.8 | −18.3% | −3.1790 to +0.5790 | no |
| pod start wait, mean (s) | 1.403 | 1.42 | +1.2% | −0.3280 to +0.3613 | no |
| host CPU busy, the real machine under kind (%) | 26.45 | 28 | +5.9% | +0.9817 to +2.1239 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.1% | −0.0042 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.7 | +0.1% | −0.4874 to +0.8598 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.7 | +0.1% | −0.4874 to +0.8598 | no |
| response time (ms), mean | 75.68 | 75.07 | −0.8% | −1.3766 to +0.1520 | no |
| response time (ms), 95th percentile | 115.6 | 113.5 | −1.8% | −4.0071 to −0.1599 | yes: GAIN |
| response time (ms), 99th percentile | 155.2 | 155.9 | +0.4% | −12.4779 to +13.8111 | no |
| time over the response line (% of samples) | 0.01212 | 0.01212 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.1 | 15 | −6.8% | −3.6558 to +1.4558 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0.3467 | +18.9% | −0.2263 to +0.3363 | no |
| utilisation (used / allocatable) | 0.03512 | 0.03494 | −0.5% | −0.0006 to +0.0002 | no |
| CPU used (cores), mean | 0.8428 | 0.8386 | −0.5% | −0.0143 to +0.0060 | no |
| Omni's own CPU (cores), mean | 0.00809 | 0.00574 | −29.0% | −0.0028 to −0.0019 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8509 | 0.8444 | −0.8% | −0.0168 to +0.0038 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.2 | 809.8 | +0.6% | −10.2405 to +19.3446 | no |
| HPA replicas, mean | 7.66 | 7.931 | +3.5% | −0.3520 to +0.8949 | no |
| pods started | 3.8 | 3.8 | ±0.0% | −1.5080 to +1.5080 | no |
| pod start wait, total (s) | 6.5 | 5.6 | −13.8% | −4.3297 to +2.5297 | no |
| pod start wait, mean (s) | 1.755 | 1.47 | −16.2% | −0.6514 to +0.0833 | no |
| host CPU busy, the real machine under kind (%) | 25.84 | 25.49 | −1.3% | −0.6532 to −0.0437 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.516 | 1.516 | −0.0% | −0.0111 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.5 | +0.0% | −0.9430 to +0.9525 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.5 | +0.0% | −0.9430 to +0.9525 | no |
| response time (ms), mean | 75.68 | 76.06 | +0.5% | −1.9346 to +2.6941 | no |
| response time (ms), 95th percentile | 115.6 | 114.8 | −0.7% | −4.4687 to +2.8947 | no |
| response time (ms), 99th percentile | 155.2 | 154.7 | −0.3% | −16.2389 to +15.2239 | no |
| time over the response line (% of samples) | 0.01212 | 0.02424 | +100.0% | −0.0519 to +0.0761 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.1 | 16.6 | +3.1% | −2.7562 to +3.7562 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0 | −100.0% | −0.5017 to −0.0816 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03512 | 0.03533 | +0.6% | −0.0010 to +0.0014 | no |
| CPU used (cores), mean | 0.8428 | 0.848 | +0.6% | −0.0240 to +0.0344 | no |
| Omni's own CPU (cores), mean | 0.00809 | 0.00633 | −21.8% | −0.0022 to −0.0013 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8509 | 0.8543 | +0.4% | −0.0258 to +0.0327 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.2 | 805.4 | +0.0% | −24.4067 to +24.7182 | no |
| HPA replicas, mean | 7.66 | 8.232 | +7.5% | +0.0200 to +1.1241 | yes: power given |
| pods started | 3.8 | 3.4 | −10.5% | −2.0588 to +1.2588 | no |
| pod start wait, total (s) | 6.5 | 5.3 | −18.5% | −4.6189 to +2.2189 | no |
| pod start wait, mean (s) | 1.755 | 1.605 | −8.5% | −0.5704 to +0.2709 | no |
| host CPU busy, the real machine under kind (%) | 25.84 | 25.77 | −0.3% | −0.8584 to +0.7223 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.521 | +0.3% | −0.0037 to +0.0124 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159 | +0.3% | −0.3509 to +1.2872 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159 | +0.3% | −0.3509 to +1.2872 | no |
| response time (ms), mean | 75.68 | 75.55 | −0.2% | −1.4342 to +1.1634 | no |
| response time (ms), 95th percentile | 115.6 | 114.7 | −0.8% | −3.2133 to +1.4133 | no |
| response time (ms), 99th percentile | 155.2 | 165.1 | +6.4% | −15.0352 to +34.7886 | no |
| time over the response line (% of samples) | 0.01212 | 0.02424 | +100.0% | −0.0371 to +0.0613 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.1 | 15.6 | −3.1% | −3.9263 to +2.9263 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0.185 | −36.6% | −0.3613 to +0.1479 | no |
| utilisation (used / allocatable) | 0.03512 | 0.03493 | −0.5% | −0.0006 to +0.0002 | no |
| CPU used (cores), mean | 0.8428 | 0.8384 | −0.5% | −0.0146 to +0.0057 | no |
| Omni's own CPU (cores), mean | 0.00809 | 0.00692 | −14.5% | −0.0016 to −0.0008 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8509 | 0.8453 | −0.7% | −0.0159 to +0.0048 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.2 | 812.3 | +0.9% | −10.9602 to +25.0992 | no |
| HPA replicas, mean | 7.66 | 7.349 | −4.1% | −1.1179 to +0.4965 | no |
| pods started | 3.8 | 3.4 | −10.5% | −1.9155 to +1.1155 | no |
| pod start wait, total (s) | 6.5 | 5.4 | −16.9% | −3.7217 to +1.5217 | no |
| pod start wait, mean (s) | 1.755 | 1.562 | −11.0% | −0.5837 to +0.1989 | no |
| host CPU busy, the real machine under kind (%) | 25.84 | 25.6 | −0.9% | −0.6985 to +0.2298 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.521 | +0.3% | −0.0026 to +0.0126 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.2 | +0.4% | −0.1905 to +1.4258 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.2 | +0.4% | −0.1905 to +1.4258 | no |
| response time (ms), mean | 75.68 | 75.91 | +0.3% | −1.3333 to +1.7831 | no |
| response time (ms), 95th percentile | 115.6 | 115.7 | +0.2% | −3.1572 to +3.5152 | no |
| response time (ms), 99th percentile | 155.2 | 161.5 | +4.1% | −11.0638 to +23.7634 | no |
| time over the response line (% of samples) | 0.01212 | 0.01212 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.1 | 15.3 | −5.0% | −3.6373 to +2.0373 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0.21 | −28.0% | −0.3191 to +0.1557 | no |
| utilisation (used / allocatable) | 0.03512 | 0.03535 | +0.7% | −0.0004 to +0.0008 | no |
| CPU used (cores), mean | 0.8428 | 0.8484 | +0.7% | −0.0085 to +0.0197 | no |
| Omni's own CPU (cores), mean | 0.00809 | 0.01293 | +59.8% | +0.0039 to +0.0058 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8509 | 0.8613 | +1.2% | −0.0036 to +0.0245 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.2 | 796.4 | −1.1% | −33.8730 to +16.3211 | no |
| HPA replicas, mean | 7.66 | 7.141 | −6.8% | −1.0091 to −0.0283 | yes: GAIN |
| pods started | 3.8 | 3.4 | −10.5% | −1.5285 to +0.7285 | no |
| pod start wait, total (s) | 6.5 | 4.9 | −24.6% | −3.2927 to +0.0927 | no |
| pod start wait, mean (s) | 1.755 | 1.445 | −17.6% | −0.4632 to −0.1558 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 25.84 | 25.99 | +0.6% | −0.2333 to +0.5310 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.517 | +0.1% | −0.0075 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.7 | +0.1% | −0.7510 to +1.0349 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.7 | +0.1% | −0.7510 to +1.0349 | no |
| response time (ms), mean | 75.68 | 75.95 | +0.3% | −0.8101 to +1.3395 | no |
| response time (ms), 95th percentile | 115.6 | 115.6 | +0.0% | −2.0849 to +2.1679 | no |
| response time (ms), 99th percentile | 155.2 | 160.1 | +3.2% | −8.0645 to +17.8425 | no |
| time over the response line (% of samples) | 0.01212 | 0.01212 | ±0.0% | −0.0409 to +0.0409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.1 | 19.3 | +19.9% | −0.3813 to +6.7813 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0.1583 | −45.7% | −0.4713 to +0.2047 | no |
| utilisation (used / allocatable) | 0.03512 | 0.03537 | +0.7% | −0.0003 to +0.0008 | no |
| CPU used (cores), mean | 0.8428 | 0.8488 | +0.7% | −0.0084 to +0.0204 | no |
| Omni's own CPU (cores), mean | 0.00809 | 0.02328 | +187.8% | +0.0130 to +0.0174 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8509 | 0.872 | +2.5% | +0.0073 to +0.0351 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.2 | 793.5 | −1.5% | −35.6382 to +12.2323 | no |
| HPA replicas, mean | 7.66 | 8.482 | +10.7% | +0.2292 to +1.4141 | yes: power given |
| pods started | 3.8 | 3.6 | −5.3% | −1.8792 to +1.4792 | no |
| pod start wait, total (s) | 6.5 | 4.8 | −26.2% | −4.8097 to +1.4097 | no |
| pod start wait, mean (s) | 1.755 | 1.387 | −21.0% | −0.6690 to −0.0667 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 25.84 | 26.41 | +2.2% | +0.1707 to +0.9761 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.516 | 1.508 | −0.6% | −0.0179 to +0.0005 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 157.8 | −0.5% | −1.6964 to +0.1829 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 157.8 | −0.5% | −1.6964 to +0.1829 | no |
| response time (ms), mean | 75.68 | 76.11 | +0.6% | −0.7470 to +1.6073 | no |
| response time (ms), 95th percentile | 115.6 | 116.1 | +0.4% | −1.7061 to +2.7031 | no |
| response time (ms), 99th percentile | 155.2 | 161.3 | +3.9% | −10.2565 to +22.3937 | no |
| time over the response line (% of samples) | 0.01212 | 0 | −100.0% | −0.0395 to +0.0153 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 16.1 | 19.9 | +23.6% | +0.8258 to +6.7742 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2917 | 0.185 | −36.6% | −0.2027 to −0.0106 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03512 | 0.03577 | +1.9% | +0.0000 to +0.0013 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8428 | 0.8586 | +1.9% | +0.0012 to +0.0304 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00809 | 0.06381 | +688.8% | +0.0468 to +0.0647 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8509 | 0.9224 | +8.4% | +0.0502 to +0.0929 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.2 | 795.8 | −1.2% | −30.3913 to +11.6296 | no |
| HPA replicas, mean | 7.66 | 8.292 | +8.3% | +0.1017 to +1.1624 | yes: power given |
| pods started | 3.8 | 3.9 | +2.6% | −1.2676 to +1.4676 | no |
| pod start wait, total (s) | 6.5 | 5.8 | −10.8% | −3.4405 to +2.0405 | no |
| pod start wait, mean (s) | 1.755 | 1.42 | −19.1% | −0.6896 to +0.0206 | no |
| host CPU busy, the real machine under kind (%) | 25.84 | 28 | +8.4% | +1.5252 to +2.7986 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*