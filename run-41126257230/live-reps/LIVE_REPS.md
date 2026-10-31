# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.33 | 4.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 470 | 468.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 470 | 468.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 179.2 | 91.77 |
| response time (ms), 95th percentile | 457.1 | 162.6 |
| response time (ms), 99th percentile | 818.8 | 409.6 |
| time over the response line (% of samples) | 6.211 | 1.219 |
| failed requests (%) | 0.4318 | 0.3433 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 3.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6017 | 0.5817 |
| utilisation (used / allocatable) | 0.06169 | 0.05925 |
| CPU used (cores), mean | 1.481 | 1.422 |
| Omni's own CPU (cores), mean | 0 | 0.008 |
| CPU used with Omni's own (cores), mean | 1.481 | 1.43 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.8 | 503.7 |
| HPA replicas, mean | 9.427 | 9.426 |
| pods started | 7.8 | 13.9 |
| pod start wait, total (s) | 11.8 | 23 |
| pod start wait, mean (s) | 1.486 | 1.615 |
| host CPU busy, the real machine under kind (%) | 43.3 | 42.18 |
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
| node-hours | 4.33 | 4.335 | +0.1% | −0.0026 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 470 | 468.9 | −0.2% | −1.8842 to −0.2224 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 470 | 468.9 | −0.2% | −1.8842 to −0.2224 | yes: GAIN |
| response time (ms), mean | 179.2 | 91.77 | −48.8% | −128.7163 to −46.0874 | yes: GAIN |
| response time (ms), 95th percentile | 457.1 | 162.6 | −64.4% | −418.9970 to −169.9120 | yes: GAIN |
| response time (ms), 99th percentile | 818.8 | 409.6 | −50.0% | −636.9247 to −181.6175 | yes: GAIN |
| time over the response line (% of samples) | 6.211 | 1.219 | −80.4% | −9.5059 to −0.4786 | yes: GAIN |
| failed requests (%) | 0.4318 | 0.3433 | −20.5% | −0.2397 to +0.0627 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 3.3 | −71.3% | −14.6492 to −1.7508 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.700 (native is 0) | +27.9778 to +55.4222 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6017 | 0.5817 | −3.3% | −0.2479 to +0.2079 | no |
| utilisation (used / allocatable) | 0.06169 | 0.05925 | −3.9% | −0.0036 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.481 | 1.422 | −3.9% | −0.0859 to −0.0310 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.008 | +0.008 (native is 0) | +0.0063 to +0.0097 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.481 | 1.43 | −3.4% | −0.0773 to −0.0235 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.8 | 503.7 | +3.7% | +4.8819 to +31.0270 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.427 | 9.426 | −0.0% | −1.4416 to +1.4394 | no |
| pods started | 7.8 | 13.9 | +78.2% | +1.6719 to +10.5281 | yes: power given |
| pod start wait, total (s) | 11.8 | 23 | +94.9% | +2.2480 to +20.1520 | yes: LOSS |
| pod start wait, mean (s) | 1.486 | 1.615 | +8.7% | −0.2558 to +0.5139 | no |
| host CPU busy, the real machine under kind (%) | 43.3 | 42.18 | −2.6% | −1.8075 to −0.4354 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*