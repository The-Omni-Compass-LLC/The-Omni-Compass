# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 160.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 160.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 185.9 | 79.54 |
| response time (ms), 95th percentile | 437.8 | 122 |
| response time (ms), 99th percentile | 595 | 273.1 |
| time over the response line (% of samples) | 4.113 | 0.2684 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.1 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.135 |
| utilisation (used / allocatable) | 0.0305 | 0.04555 |
| CPU used (cores), mean | 0.732 | 1.093 |
| Omni's own CPU (cores), mean | 0 | 0.00901 |
| CPU used with Omni's own (cores), mean | 0.732 | 1.102 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.7 | 594 |
| HPA replicas, mean | 2.802 | 2.318 |
| pods started | 2.7 | 2.1 |
| pod start wait, total (s) | 21.8 | 18.3 |
| pod start wait, mean (s) | 8 | 8.667 |
| host CPU busy, the real machine under kind (%) | 23.16 | 33.53 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.702e-16 to +1.003e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.513 | -0.2% | -0.01088 to +0.005214 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 160.8 | +2.0% | +2.013 to +4.268 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 160.8 | +2.0% | +2.013 to +4.268 | yes: power given |
| response time (ms), mean | 185.9 | 79.54 | -57.2% | -134.8 to -77.99 | yes: GAIN |
| response time (ms), 95th percentile | 437.8 | 122 | -72.1% | -382.6 to -249.1 | yes: GAIN |
| response time (ms), 99th percentile | 595 | 273.1 | -54.1% | -385.2 to -258.6 | yes: GAIN |
| time over the response line (% of samples) | 4.113 | 0.2684 | -93.5% | -6.366 to -1.325 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.1 | 0.4 | -90.2% | -6.133 to -1.267 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.1 | +4.1 (native is 0) | +3.874 to +4.326 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.135 | -68.4% | -0.4622 to -0.1212 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0305 | 0.04555 | +49.3% | +0.01205 to +0.01804 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.732 | 1.093 | +49.3% | +0.2891 to +0.433 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00901 | +0.00901 (native is 0) | +0.007768 to +0.01025 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.732 | 1.102 | +50.6% | +0.297 to +0.4432 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.7 | 594 | -30.7% | -285.4 to -242 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.802 | 2.318 | -17.3% | -0.7048 to -0.2618 | yes: GAIN |
| pods started | 2.7 | 2.1 | -22.2% | -1.1 to -0.09985 | yes: GAIN |
| pod start wait, total (s) | 21.8 | 18.3 | -16.1% | -8.307 to +1.307 | no |
| pod start wait, mean (s) | 8 | 8.667 | +8.3% | +0.006468 to +1.327 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.16 | 33.53 | +44.8% | +8.133 to +12.6 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*