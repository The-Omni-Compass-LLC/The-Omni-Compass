# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.4 | 172 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.4 | 172 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 520.3 | 478.2 |
| response time (ms), 95th percentile | 2212 | 2158 |
| response time (ms), 99th percentile | 5245 | 5608 |
| time over the response line (% of samples) | 23.6 | 23.18 |
| failed requests (%) | 3.398 | 2.993 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.453 | 2.087 |
| utilisation (used / allocatable) | 0.09678 | 0.09574 |
| CPU used (cores), mean | 2.323 | 2.298 |
| Omni's own CPU (cores), mean | 0 | 0.03448 |
| CPU used with Omni's own (cores), mean | 2.323 | 2.332 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.1 | 305.1 |
| HPA replicas, mean | 14.98 | 15.41 |
| pods started | 5 | 6.3 |
| pod start wait, total (s) | 8.1 | 13 |
| pod start wait, mean (s) | 1.61 | 2.065 |
| host CPU busy, the real machine under kind (%) | 67.16 | 68.08 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 282.5 | 271.2 |
| second app: response time (ms), 99th percentile | 2716 | 1683 |
| second app: time over the response line (% of samples) | 14.15 | 14.03 |
| second app: failed requests (%) | 12.29 | 12.79 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.514 | 1.513 | -0.1% | -0.01079 to +0.008454 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.4 | 172 | -0.2% | -1.283 to +0.5408 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.4 | 172 | -0.2% | -1.283 to +0.5408 | no |
| response time (ms), mean | 520.3 | 478.2 | -8.1% | -93.37 to +9.192 | no |
| response time (ms), 95th percentile | 2212 | 2158 | -2.4% | -472.1 to +365.5 | no |
| response time (ms), 99th percentile | 5245 | 5608 | +6.9% | -393.6 to +1119 | no |
| time over the response line (% of samples) | 23.6 | 23.18 | -1.8% | -2.017 to +1.18 | no |
| failed requests (%) | 3.398 | 2.993 | -11.9% | -1.106 to +0.2957 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.3 | -4.6% | -1.366 to +0.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.1 (native is 0) | +38.16 to +62.04 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.453 | 2.087 | +43.6% | -0.4274 to +1.694 | no |
| utilisation (used / allocatable) | 0.09678 | 0.09574 | -1.1% | -0.00246 to +0.0003835 | no |
| CPU used (cores), mean | 2.323 | 2.298 | -1.1% | -0.05904 to +0.009205 | no |
| Omni's own CPU (cores), mean | 0 | 0.03448 | +0.0345 (native is 0) | +0.03073 to +0.03823 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.323 | 2.332 | +0.4% | -0.0225 to +0.04162 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.1 | 305.1 | +0.4% | -3.29 to +5.437 | no |
| HPA replicas, mean | 14.98 | 15.41 | +2.8% | +0.0629 to +0.7871 | yes: power given |
| pods started | 5 | 6.3 | +26.0% | -0.1326 to +2.733 | no |
| pod start wait, total (s) | 8.1 | 13 | +60.5% | +1.199 to +8.601 | yes: LOSS |
| pod start wait, mean (s) | 1.61 | 2.065 | +28.3% | -0.08594 to +0.9973 | no |
| host CPU busy, the real machine under kind (%) | 67.16 | 68.08 | +1.4% | +0.2414 to +1.6 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 282.5 | 271.2 | -4.0% | -35.53 to +13.03 | no |
| second app: response time (ms), 99th percentile | 2716 | 1683 | -38.0% | -2334 to +268 | no |
| second app: time over the response line (% of samples) | 14.15 | 14.03 | -0.8% | -0.7575 to +0.5238 | no |
| second app: failed requests (%) | 12.29 | 12.79 | +4.1% | +0.007072 to +0.993 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*