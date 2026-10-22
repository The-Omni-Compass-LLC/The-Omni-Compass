# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.573 |
| node-hours | 2.514 | 2.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 261.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 599.5 | 535.3 |
| response time (ms), 95th percentile | 3457 | 3467 |
| response time (ms), 99th percentile | 5045 | 4973 |
| time over the response line (% of samples) | 17.15 | 16.47 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 200.9 | 206.1 |
| utilisation (used / allocatable) | 0.06598 | 0.07216 |
| CPU used (cores), mean | 1.584 | 1.605 |
| Omni's own CPU (cores), mean | 0 | 0.05712 |
| CPU used with Omni's own (cores), mean | 1.584 | 1.662 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.8 | 391.1 |
| HPA replicas, mean | 2.371 | 2.083 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 45.69 | 47.43 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 625.8 | 636.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.299 |

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
| worker nodes in service, mean | 6 | 5.573 | -7.1% | -0.8336 to -0.02072 | yes: GAIN |
| node-hours | 2.514 | 2.335 | -7.1% | -0.3531 to -0.006216 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.9 | +0.0% | -1.02 to +1.128 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 261.5 | -4.9% | -26.56 to -0.1542 | yes: GAIN |
| response time (ms), mean | 599.5 | 535.3 | -10.7% | -80.91 to -47.59 | yes: GAIN |
| response time (ms), 95th percentile | 3457 | 3467 | +0.3% | -102.2 to +123.5 | no |
| response time (ms), 99th percentile | 5045 | 4973 | -1.4% | -353.5 to +210.4 | no |
| time over the response line (% of samples) | 17.15 | 16.47 | -3.9% | -1.252 to -0.1003 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.9 | +0.9% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.9 | +7.9 (native is 0) | +6.338 to +9.462 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 200.9 | 206.1 | +2.6% | +0.9626 to +9.364 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06598 | 0.07216 | +9.4% | +0.0009232 to +0.01144 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.584 | 1.605 | +1.3% | -0.02082 to +0.0627 | no |
| Omni's own CPU (cores), mean | 0 | 0.05712 | +0.0571 (native is 0) | +0.05255 to +0.06169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.584 | 1.662 | +4.9% | +0.03411 to +0.122 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.8 | 391.1 | -6.4% | -51.49 to -1.862 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.371 | 2.083 | -12.2% | -0.6922 to +0.1157 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 45.69 | 47.43 | +3.8% | +1.379 to +2.107 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 625.8 | 636.5 | +1.7% | +5.179 to +16.22 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.299 | -11.7% | -1.337 to -0.06392 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*