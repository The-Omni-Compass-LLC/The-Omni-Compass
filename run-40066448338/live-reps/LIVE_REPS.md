# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 516.9 | 515.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.9 | 515.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 265.5 | 153.7 |
| response time (ms), 95th percentile | 689.3 | 326.7 |
| response time (ms), 99th percentile | 2490 | 1637 |
| time over the response line (% of samples) | 19.31 | 12.66 |
| failed requests (%) | 11.82 | 10.39 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.5 | 21.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.38 |
| utilisation (used / allocatable) | 0.1018 | 0.09917 |
| CPU used (cores), mean | 2.442 | 2.38 |
| Omni's own CPU (cores), mean | 0 | 0.0087 |
| CPU used with Omni's own (cores), mean | 2.442 | 2.389 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.1 | 322.7 |
| HPA replicas, mean | 9.534 | 9.556 |
| pods started | 5.6 | 5.2 |
| pod start wait, total (s) | 9.7 | 8 |
| pod start wait, mean (s) | 1.768 | 1.5 |
| host CPU busy, the real machine under kind (%) | 68.62 | 67.32 |
| host cores (the real machine under kind) | 4 | 4 |

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
| node-hours | 4.514 | 4.517 | +0.1% | −0.0061 to +0.0111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516.9 | 515.6 | −0.3% | −2.8835 to +0.2366 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.9 | 515.6 | −0.3% | −2.8835 to +0.2366 | no |
| response time (ms), mean | 265.5 | 153.7 | −42.1% | −165.0882 to −58.5533 | yes: GAIN |
| response time (ms), 95th percentile | 689.3 | 326.7 | −52.6% | −498.6900 to −226.5160 | yes: GAIN |
| response time (ms), 99th percentile | 2490 | 1637 | −34.3% | −2377.5539 to +671.3339 | no |
| time over the response line (% of samples) | 19.31 | 12.66 | −34.4% | −9.4961 to −3.7977 | yes: GAIN |
| failed requests (%) | 11.82 | 10.39 | −12.1% | −2.1728 to −0.6990 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.5 | 21.8 | −23.5% | −7.8705 to −5.5295 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 | +32.200 (native is 0) | +24.0039 to +40.3961 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.38 | +8.6% | −0.2363 to +0.2963 | no |
| utilisation (used / allocatable) | 0.1018 | 0.09917 | −2.5% | −0.0040 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.442 | 2.38 | −2.5% | −0.0948 to −0.0296 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0087 | +0.009 (native is 0) | +0.0072 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.442 | 2.389 | −2.2% | −0.0864 to −0.0206 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.1 | 322.7 | +3.4% | −0.6838 to +21.9339 | no |
| HPA replicas, mean | 9.534 | 9.556 | +0.2% | −0.6359 to +0.6798 | no |
| pods started | 5.6 | 5.2 | −7.1% | −1.7146 to +0.9146 | no |
| pod start wait, total (s) | 9.7 | 8 | −17.5% | −5.0390 to +1.6390 | no |
| pod start wait, mean (s) | 1.768 | 1.5 | −15.2% | −0.5716 to +0.0355 | no |
| host CPU busy, the real machine under kind (%) | 68.62 | 67.32 | −1.9% | −2.0730 to −0.5174 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*