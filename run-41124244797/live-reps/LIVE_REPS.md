# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.641 |
| node-hours | 2.514 | 2.363 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 275.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 264.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 620.2 | 561.9 |
| response time (ms), 95th percentile | 3500 | 3502 |
| response time (ms), 99th percentile | 4602 | 4620 |
| time over the response line (% of samples) | 18.51 | 17.81 |
| failed requests (%) | 0 | 0.0107 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 206.5 | 212.4 |
| utilisation (used / allocatable) | 0.06916 | 0.07332 |
| CPU used (cores), mean | 1.66 | 1.654 |
| Omni's own CPU (cores), mean | 0 | 0.01886 |
| CPU used with Omni's own (cores), mean | 1.66 | 1.673 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 405.6 | 386.4 |
| HPA replicas, mean | 2.123 | 2.571 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 48.13 | 49.01 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 659.6 | 663.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.426 |

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
| worker nodes in service, mean | 6 | 5.641 | −6.0% | −0.8290 to +0.1102 | no |
| node-hours | 2.514 | 2.363 | −6.0% | −0.3473 to +0.0446 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 275.9 | +0.0% | −1.0891 to +1.2319 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 264.6 | −4.1% | −25.8062 to +3.2989 | no |
| response time (ms), mean | 620.2 | 561.9 | −9.4% | −76.3817 to −40.2329 | yes: GAIN |
| response time (ms), 95th percentile | 3500 | 3502 | +0.1% | −100.9073 to +105.3553 | no |
| response time (ms), 99th percentile | 4602 | 4620 | +0.4% | −154.1578 to +189.1954 | no |
| time over the response line (% of samples) | 18.51 | 17.81 | −3.8% | −1.0505 to −0.3478 | yes: GAIN |
| failed requests (%) | 0 | 0.0107 | +0.011 (native is 0) | −0.0135 to +0.0349 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.2 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12 | +12.000 (native is 0) | +10.4184 to +13.5816 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 206.5 | 212.4 | +2.8% | +1.6351 to +10.0849 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06916 | 0.07332 | +6.0% | −0.0019 to +0.0102 | no |
| CPU used (cores), mean | 1.66 | 1.654 | −0.3% | −0.0475 to +0.0363 | no |
| Omni's own CPU (cores), mean | 0 | 0.01886 | +0.019 (native is 0) | +0.0171 to +0.0206 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.66 | 1.673 | +0.8% | −0.0284 to +0.0550 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 405.6 | 386.4 | −4.7% | −54.6313 to +16.2589 | no |
| HPA replicas, mean | 2.123 | 2.571 | +21.1% | +0.0055 to +0.8907 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| host CPU busy, the real machine under kind (%) | 48.13 | 49.01 | +1.8% | +0.4585 to +1.3024 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 659.6 | 663.5 | +0.6% | −2.3126 to +10.1126 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.426 | −9.6% | −1.2426 to +0.0946 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*