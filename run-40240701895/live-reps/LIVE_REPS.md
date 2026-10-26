# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.407 |
| node-hours | 2.519 | 2.267 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 253.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 357.7 | 309.8 |
| response time (ms), 95th percentile | 1211 | 1188 |
| response time (ms), 99th percentile | 1770 | 1719 |
| time over the response line (% of samples) | 20.52 | 19.51 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 10.81 |
| utilisation (used / allocatable) | 0.05909 | 0.06687 |
| CPU used (cores), mean | 1.418 | 1.433 |
| Omni's own CPU (cores), mean | 0 | 0.01619 |
| CPU used with Omni's own (cores), mean | 1.418 | 1.449 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 423.5 |
| HPA replicas, mean | 2.004 | 2.088 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 41.57 | 42.45 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 775.6 | 775.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.938 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.1958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 83.2 | 81.72 |
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
| worker nodes in service, mean | 6 | 5.407 | −9.9% | −1.2469 to +0.0608 | no |
| node-hours | 2.519 | 2.267 | −10.0% | −0.5245 to +0.0210 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.4 | −0.0% | −1.0857 to +0.8184 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 253.8 | −6.9% | −38.7870 to +1.2614 | no |
| response time (ms), mean | 357.7 | 309.8 | −13.4% | −68.9971 to −26.9347 | yes: GAIN |
| response time (ms), 95th percentile | 1211 | 1188 | −1.9% | −119.7542 to +72.5892 | no |
| response time (ms), 99th percentile | 1770 | 1719 | −2.9% | −250.6777 to +148.5483 | no |
| time over the response line (% of samples) | 20.52 | 19.51 | −4.9% | −2.1983 to +0.1950 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.3 | −1.0% | −0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 | +29.300 (native is 0) | +14.2992 to +44.3008 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 10.81 | +2.1% | −1.8443 to +2.2876 | no |
| utilisation (used / allocatable) | 0.05909 | 0.06687 | +13.2% | −0.0015 to +0.0171 | no |
| CPU used (cores), mean | 1.418 | 1.433 | +1.0% | −0.0190 to +0.0475 | no |
| Omni's own CPU (cores), mean | 0 | 0.01619 | +0.016 (native is 0) | +0.0149 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.449 | +2.1% | −0.0019 to +0.0628 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 423.5 | −9.6% | −103.3944 to +12.9399 | no |
| HPA replicas, mean | 2.004 | 2.088 | +4.2% | −0.0939 to +0.2603 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 41.57 | 42.45 | +2.1% | +0.5214 to +1.2301 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.6 | 775.3 | −0.0% | −4.1008 to +3.5008 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.938 | −17.7% | −2.1624 to +0.0376 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.1958 | −21.7% | −0.1105 to +0.0021 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.8 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.2 | 81.72 | −1.8% | −5.0853 to +2.1186 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*