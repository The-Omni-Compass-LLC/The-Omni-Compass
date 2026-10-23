# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.791 |
| node-hours | 2.517 | 2.009 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 233.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 425 | 379.5 |
| response time (ms), 95th percentile | 2492 | 2505 |
| response time (ms), 99th percentile | 3903 | 3831 |
| time over the response line (% of samples) | 14.87 | 14.61 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 172.9 | 173.2 |
| utilisation (used / allocatable) | 0.05618 | 0.07209 |
| CPU used (cores), mean | 1.348 | 1.373 |
| Omni's own CPU (cores), mean | 0 | 0.0149 |
| CPU used with Omni's own (cores), mean | 1.348 | 1.388 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 408.4 |
| HPA replicas, mean | 2.077 | 2.065 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 1.7 | 1 |
| pod start wait, mean (s) | 1.7 | 1 |
| host CPU busy, the real machine under kind (%) | 39.21 | 39.93 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 531.6 | 537.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.24 |

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
| worker nodes in service, mean | 6 | 4.791 | -20.1% | -1.954 to -0.4639 | yes: GAIN |
| node-hours | 2.517 | 2.009 | -20.2% | -0.8127 to -0.2033 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.9 | +0.2% | -1.168 to +2.182 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 233.8 | -13.9% | -59.89 to -15.3 | yes: GAIN |
| response time (ms), mean | 425 | 379.5 | -10.7% | -63.79 to -27.11 | yes: GAIN |
| response time (ms), 95th percentile | 2492 | 2505 | +0.5% | -91.3 to +118.1 | no |
| response time (ms), 99th percentile | 3903 | 3831 | -1.8% | -226.3 to +82.62 | no |
| time over the response line (% of samples) | 14.87 | 14.61 | -1.7% | -0.6814 to +0.1652 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.1 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.7 | +10.7 (native is 0) | +9.228 to +12.17 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 172.9 | 173.2 | +0.2% | -4.254 to +5.008 | no |
| utilisation (used / allocatable) | 0.05618 | 0.07209 | +28.3% | +0.006555 to +0.02526 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.348 | 1.373 | +1.8% | -0.01283 to +0.06267 | no |
| Omni's own CPU (cores), mean | 0 | 0.0149 | +0.0149 (native is 0) | +0.01406 to +0.01574 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.348 | 1.388 | +3.0% | +0.002097 to +0.07754 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 408.4 | -17.6% | -142 to -33.04 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.077 | 2.065 | -0.6% | -0.1822 to +0.1583 | no |
| pods started | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 1.7 | 1 | -41.2% | -3.846 to +2.446 | no |
| pod start wait, mean (s) | 1.7 | 1 | -41.2% | -3.846 to +2.446 | no |
| host CPU busy, the real machine under kind (%) | 39.21 | 39.93 | +1.8% | +0.2772 to +1.169 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 531.6 | 537.5 | +1.1% | -2.935 to +14.73 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.24 | -29.3% | -2.844 to -0.6762 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*