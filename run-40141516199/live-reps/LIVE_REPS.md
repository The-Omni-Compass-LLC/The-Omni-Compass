# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.988 |
| node-hours | 2.511 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 145 | 108.9 |
| response time (ms), 95th percentile | 249.3 | 234.9 |
| response time (ms), 99th percentile | 360 | 362 |
| time over the response line (% of samples) | 0.216 | 0.2312 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1118 | 1138 |
| utilisation (used / allocatable) | 0.05982 | 0.05997 |
| CPU used (cores), mean | 1.436 | 1.437 |
| Omni's own CPU (cores), mean | 0 | 0.01218 |
| CPU used with Omni's own (cores), mean | 1.436 | 1.449 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.1 | 451.8 |
| HPA replicas, mean | 2.112 | 2.041 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.1667 |
| host CPU busy, the real machine under kind (%) | 44.54 | 44.86 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1430 | 1472 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.796 |
| queue: job wait, submitted to its first pod running, mean (s) | 154.7 | 154.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 657 | 651 |
| queue: job turnaround, submitted to done, mean (s) | 829.8 | 836.1 |
| queue: jobs unfinished at the window's end | 11 | 10.6 |

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
| worker nodes in service, mean | 6 | 5.988 | −0.2% | −0.0385 to +0.0149 | no |
| node-hours | 2.511 | 2.51 | −0.1% | −0.0139 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.2 | +0.1% | −0.7847 to +1.4199 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.8 | −0.0% | −1.0865 to +0.9801 | no |
| response time (ms), mean | 145 | 108.9 | −24.9% | −43.6138 to −28.6182 | yes: GAIN |
| response time (ms), 95th percentile | 249.3 | 234.9 | −5.8% | −27.9649 to −0.8791 | yes: GAIN |
| response time (ms), 99th percentile | 360 | 362 | +0.5% | −23.1990 to +27.0366 | no |
| time over the response line (% of samples) | 0.216 | 0.2312 | +7.1% | −0.0974 to +0.1278 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.600 (native is 0) | +10.2109 to +14.9891 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1118 | 1138 | +1.8% | −52.7177 to +93.3610 | no |
| utilisation (used / allocatable) | 0.05982 | 0.05997 | +0.3% | −0.0016 to +0.0019 | no |
| CPU used (cores), mean | 1.436 | 1.437 | +0.1% | −0.0374 to +0.0394 | no |
| Omni's own CPU (cores), mean | 0 | 0.01218 | +0.012 (native is 0) | +0.0112 to +0.0131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.436 | 1.449 | +0.9% | −0.0251 to +0.0514 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.1 | 451.8 | −0.3% | −13.5310 to +10.9275 | no |
| HPA replicas, mean | 2.112 | 2.041 | −3.4% | −0.1803 to +0.0378 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.1667 | +0.167 (native is 0) | −0.2103 to +0.5437 | no |
| host CPU busy, the real machine under kind (%) | 44.54 | 44.86 | +0.7% | −0.6862 to +1.3415 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1430 | 1472 | +2.9% | −16.4308 to +99.6308 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.796 | −3.4% | −1.0802 to +0.6728 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 154.7 | 154.8 | +0.1% | −29.5197 to +29.7280 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 657 | 651 | −0.9% | −146.4356 to +134.4356 | no |
| queue: job turnaround, submitted to done, mean (s) | 829.8 | 836.1 | +0.8% | −25.3429 to +37.9679 | no |
| queue: jobs unfinished at the window's end | 11 | 10.6 | −3.6% | −1.4769 to +0.6769 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*