# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.086 |
| node-hours | 2.51 | 2.132 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 244 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 370.3 | 348.7 |
| response time (ms), 95th percentile | 1373 | 1462 |
| response time (ms), 99th percentile | 1941 | 1989 |
| time over the response line (% of samples) | 14.78 | 14.95 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.92 | 10.96 |
| utilisation (used / allocatable) | 0.06043 | 0.0718 |
| CPU used (cores), mean | 1.45 | 1.439 |
| Omni's own CPU (cores), mean | 0 | 0.01675 |
| CPU used with Omni's own (cores), mean | 1.45 | 1.456 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 409.6 |
| HPA replicas, mean | 1.97 | 2.05 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.3 |
| pod start wait, mean (s) | 0 | 0.3 |
| host CPU busy, the real machine under kind (%) | 42.09 | 42.68 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 795.7 | 798.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.445 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4583 | 0.325 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 99.77 | 104.5 |
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
| worker nodes in service, mean | 6 | 5.086 | −15.2% | −1.7061 to −0.1229 | yes: GAIN |
| node-hours | 2.51 | 2.132 | −15.1% | −0.7083 to −0.0483 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.7 | +0.2% | −0.3973 to +1.6224 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 244 | −10.3% | −52.9039 to −3.2919 | yes: GAIN |
| response time (ms), mean | 370.3 | 348.7 | −5.8% | −48.3560 to +5.1737 | no |
| response time (ms), 95th percentile | 1373 | 1462 | +6.5% | −26.3597 to +204.5517 | no |
| response time (ms), 99th percentile | 1941 | 1989 | +2.5% | −109.2129 to +206.0243 | no |
| time over the response line (% of samples) | 14.78 | 14.95 | +1.1% | −0.8921 to +1.2169 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 9.1 | +12.3% | −0.5080 to +2.5080 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.7 | +45.700 (native is 0) | +24.0902 to +67.3098 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.92 | 10.96 | +10.5% | −0.8103 to +2.8836 | no |
| utilisation (used / allocatable) | 0.06043 | 0.0718 | +18.8% | +0.0014 to +0.0214 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.45 | 1.439 | −0.8% | −0.0409 to +0.0183 | no |
| Omni's own CPU (cores), mean | 0 | 0.01675 | +0.017 (native is 0) | +0.0151 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.456 | +0.4% | −0.0249 to +0.0359 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 409.6 | −11.3% | −99.1392 to −5.4247 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.97 | 2.05 | +4.0% | −0.1852 to +0.3448 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 42.09 | 42.68 | +1.4% | −0.0395 to +1.2174 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 795.7 | 798.8 | +0.4% | −3.2930 to +9.4930 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.445 | −25.9% | −2.7821 to −0.3273 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4583 | 0.325 | −29.1% | −0.5042 to +0.2375 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.9 | 1.6 | −44.8% | −5.0252 to +2.4252 | no |
| queue: job turnaround, submitted to done, mean (s) | 99.77 | 104.5 | +4.7% | −3.9551 to +13.4218 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*