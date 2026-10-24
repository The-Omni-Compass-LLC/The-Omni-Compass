# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.322 |
| node-hours | 2.517 | 2.233 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 250 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 279.1 | 241.6 |
| response time (ms), 95th percentile | 852.3 | 896.6 |
| response time (ms), 99th percentile | 1259 | 1293 |
| time over the response line (% of samples) | 14.4 | 14.06 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 8.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.675 | 8.25 |
| utilisation (used / allocatable) | 0.05703 | 0.06439 |
| CPU used (cores), mean | 1.369 | 1.344 |
| Omni's own CPU (cores), mean | 0 | 0.01604 |
| CPU used with Omni's own (cores), mean | 1.369 | 1.36 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.4 | 445.1 |
| HPA replicas, mean | 1.962 | 2.559 |
| pods started | 0.2 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.5 |
| pod start wait, mean (s) | 0.4 | 0.5 |
| host CPU busy, the real machine under kind (%) | 39.53 | 40.21 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 755.1 | 753.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.888 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.15 | 0.1875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 62.5 | 61.61 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.322 | −11.3% | −1.4565 to +0.1005 | no |
| node-hours | 2.517 | 2.233 | −11.3% | −0.6092 to +0.0408 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.3 | −0.1% | −1.3302 to +0.6947 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 250 | −8.0% | −46.1255 to +2.8858 | no |
| response time (ms), mean | 279.1 | 241.6 | −13.4% | −55.5547 to −19.3703 | yes: GAIN |
| response time (ms), 95th percentile | 852.3 | 896.6 | +5.2% | −43.5780 to +132.2090 | no |
| response time (ms), 99th percentile | 1259 | 1293 | +2.7% | −80.5345 to +148.0557 | no |
| time over the response line (% of samples) | 14.4 | 14.06 | −2.4% | −1.4056 to +0.7159 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 8.5 | +13.3% | −0.3903 to +2.3903 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.5 | +52.500 (native is 0) | +32.0466 to +72.9534 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.675 | 8.25 | +7.5% | −0.6789 to +1.8289 | no |
| utilisation (used / allocatable) | 0.05703 | 0.06439 | +12.9% | −0.0018 to +0.0165 | no |
| CPU used (cores), mean | 1.369 | 1.344 | −1.8% | −0.0643 to +0.0154 | no |
| Omni's own CPU (cores), mean | 0 | 0.01604 | +0.016 (native is 0) | +0.0146 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.369 | 1.36 | −0.6% | −0.0489 to +0.0321 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.4 | 445.1 | −7.4% | −79.9463 to +9.2359 | no |
| HPA replicas, mean | 1.962 | 2.559 | +30.4% | +0.3762 to +0.8184 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | −0.6113 to +0.8113 | no |
| pod start wait, mean (s) | 0.4 | 0.5 | +25.0% | −0.6113 to +0.8113 | no |
| host CPU busy, the real machine under kind (%) | 39.53 | 40.21 | +1.7% | +0.2127 to +1.1412 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.1 | 753.7 | −0.2% | −7.9922 to +5.1922 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.888 | −18.5% | −2.3423 to +0.1180 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.15 | 0.1875 | +25.0% | −0.0159 to +0.0909 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 | −12.5% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.5 | 61.61 | −1.4% | −6.4246 to +4.6413 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*