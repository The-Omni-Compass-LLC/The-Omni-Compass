# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 212.4 | 88.58 |
| response time (ms), 95th percentile | 514.7 | 136 |
| response time (ms), 99th percentile | 697 | 255.3 |
| time over the response line (% of samples) | 5.309 | 0.158 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.025 |
| utilisation (used / allocatable) | 0.0306 | 0.04826 |
| CPU used (cores), mean | 0.7345 | 1.158 |
| Omni's own CPU (cores), mean | 0 | 0.01003 |
| CPU used with Omni's own (cores), mean | 0.7345 | 1.168 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851.7 | 557.6 |
| HPA replicas, mean | 2.926 | 2.304 |
| pods started | 2.8 | 2.1 |
| pod start wait, total (s) | 3.8 | 2.8 |
| pod start wait, mean (s) | 1.383 | 1.317 |
| host CPU busy, the real machine under kind (%) | 23.34 | 35.41 |
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
| node-hours | 1.518 | 1.516 | −0.2% | −0.0080 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.7 | +2.4% | +3.0427 to +4.5560 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.7 | +2.4% | +3.0427 to +4.5560 | yes: power given |
| response time (ms), mean | 212.4 | 88.58 | −58.3% | −139.0348 to −108.6167 | yes: GAIN |
| response time (ms), 95th percentile | 514.7 | 136 | −73.6% | −418.7387 to −338.7803 | yes: GAIN |
| response time (ms), 99th percentile | 697 | 255.3 | −63.4% | −503.8119 to −379.4895 | yes: GAIN |
| time over the response line (% of samples) | 5.309 | 0.158 | −97.0% | −6.9967 to −3.3061 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 0.1 | −98.1% | −7.0714 to −3.3286 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.1 | +4.100 (native is 0) | +3.8738 to +4.3262 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.025 | −6.3% | −0.0888 to +0.0855 | no |
| utilisation (used / allocatable) | 0.0306 | 0.04826 | +57.7% | +0.0155 to +0.0198 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7345 | 1.158 | +57.7% | +0.3722 to +0.4755 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01003 | +0.010 (native is 0) | +0.0090 to +0.0111 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7345 | 1.168 | +59.1% | +0.3813 to +0.4864 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 851.7 | 557.6 | −34.5% | −305.7347 to −282.5373 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.926 | 2.304 | −21.2% | −0.8323 to −0.4108 | yes: GAIN |
| pods started | 2.8 | 2.1 | −25.0% | −1.0455 to −0.3545 | yes: GAIN |
| pod start wait, total (s) | 3.8 | 2.8 | −26.3% | −2.2158 to +0.2158 | no |
| pod start wait, mean (s) | 1.383 | 1.317 | −4.8% | −0.4317 to +0.2984 | no |
| host CPU busy, the real machine under kind (%) | 23.34 | 35.41 | +51.7% | +10.6185 to +13.5125 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*