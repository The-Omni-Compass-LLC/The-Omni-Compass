# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 161.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 131.6 | 83.21 |
| response time (ms), 95th percentile | 269.4 | 132.7 |
| response time (ms), 99th percentile | 404.3 | 183.9 |
| time over the response line (% of samples) | 0.5642 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0 |
| utilisation (used / allocatable) | 0.03625 | 0.04748 |
| CPU used (cores), mean | 0.8701 | 1.14 |
| Omni's own CPU (cores), mean | 0 | 0.017 |
| CPU used with Omni's own (cores), mean | 0.8701 | 1.157 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.7 | 570 |
| HPA replicas, mean | 8.861 | 10.01 |
| pods started | 5.2 | 6.8 |
| pod start wait, total (s) | 8 | 10.2 |
| pod start wait, mean (s) | 1.547 | 1.51 |
| host CPU busy, the real machine under kind (%) | 27.19 | 35.36 |
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
| node-hours | 1.516 | 1.518 | +0.1% | −0.0087 to +0.0117 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 161.5 | +1.7% | +1.2456 to +4.2178 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 161.5 | +1.7% | +1.2456 to +4.2178 | yes: power given |
| response time (ms), mean | 131.6 | 83.21 | −36.8% | −62.8107 to −34.0460 | yes: GAIN |
| response time (ms), 95th percentile | 269.4 | 132.7 | −50.8% | −158.1985 to −115.2875 | yes: GAIN |
| response time (ms), 99th percentile | 404.3 | 183.9 | −54.5% | −260.5074 to −180.1826 | yes: GAIN |
| time over the response line (% of samples) | 0.5642 | 0 | −100.0% | −0.9078 to −0.2206 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | −100.0% | −0.6455 to +0.0455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 | +37.000 (native is 0) | +22.9505 to +51.0495 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0 | −100.0% | −0.2657 to +0.0023 | no |
| utilisation (used / allocatable) | 0.03625 | 0.04748 | +31.0% | +0.0078 to +0.0147 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8701 | 1.14 | +31.0% | +0.1864 to +0.3525 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.0127 to +0.0213 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8701 | 1.157 | +32.9% | +0.1996 to +0.3733 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 723.7 | 570 | −21.2% | −190.0303 to −117.2420 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.861 | 10.01 | +12.9% | +0.4275 to +1.8618 | yes: power given |
| pods started | 5.2 | 6.8 | +30.8% | −0.0242 to +3.2242 | no |
| pod start wait, total (s) | 8 | 10.2 | +27.5% | −1.1176 to +5.5176 | no |
| pod start wait, mean (s) | 1.547 | 1.51 | −2.4% | −0.4136 to +0.3407 | no |
| host CPU busy, the real machine under kind (%) | 27.19 | 35.36 | +30.0% | +5.7950 to +10.5290 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*