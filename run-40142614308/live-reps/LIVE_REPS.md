# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.935 |
| node-hours | 2.514 | 2.067 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 237.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 251.8 | 214.5 |
| response time (ms), 95th percentile | 882.9 | 880.1 |
| response time (ms), 99th percentile | 1400 | 1440 |
| time over the response line (% of samples) | 9.89 | 9.187 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.23 | 9.788 |
| utilisation (used / allocatable) | 0.05622 | 0.06961 |
| CPU used (cores), mean | 1.349 | 1.343 |
| Omni's own CPU (cores), mean | 0 | 0.01624 |
| CPU used with Omni's own (cores), mean | 1.349 | 1.359 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.4 | 422.1 |
| HPA replicas, mean | 2.039 | 2.369 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.1 | 0.2 |
| pod start wait, mean (s) | 0.1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 38.81 | 39.73 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 749.2 | 752.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.219 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.075 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 58.91 | 62.36 |
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
| worker nodes in service, mean | 6 | 4.935 | −17.7% | −1.8639 to −0.2660 | yes: GAIN |
| node-hours | 2.514 | 2.067 | −17.8% | −0.7790 to −0.1134 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.2 | +0.1% | −0.8344 to +1.2683 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 237.6 | −12.3% | −58.1437 to −8.5016 | yes: GAIN |
| response time (ms), mean | 251.8 | 214.5 | −14.8% | −65.1622 to −9.4389 | yes: GAIN |
| response time (ms), 95th percentile | 882.9 | 880.1 | −0.3% | −162.0862 to +156.4652 | no |
| response time (ms), 99th percentile | 1400 | 1440 | +2.9% | −156.1251 to +236.3237 | no |
| time over the response line (% of samples) | 9.89 | 9.187 | −7.1% | −2.3406 to +0.9351 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.5 | −3.0% | −0.7642 to +0.3642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.5 | +41.500 (native is 0) | +31.6850 to +51.3150 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.23 | 9.788 | −12.9% | −3.2121 to +0.3221 | no |
| utilisation (used / allocatable) | 0.05622 | 0.06961 | +23.8% | +0.0024 to +0.0244 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.349 | 1.343 | −0.5% | −0.0365 to +0.0242 | no |
| Omni's own CPU (cores), mean | 0 | 0.01624 | +0.016 (native is 0) | +0.0145 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.349 | 1.359 | +0.8% | −0.0204 to +0.0406 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.4 | 422.1 | −13.4% | −117.9856 to −12.6923 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.039 | 2.369 | +16.2% | +0.0941 to +0.5667 | yes: power given |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, mean (s) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| host CPU busy, the real machine under kind (%) | 38.81 | 39.73 | +2.4% | +0.4631 to +1.3808 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.2 | 752.2 | +0.4% | −2.0804 to +8.0804 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.219 | −29.7% | −3.0152 to −0.5467 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.075 | −5.3% | −0.0303 to +0.0219 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.91 | 62.36 | +5.9% | −0.8927 to +7.7927 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*