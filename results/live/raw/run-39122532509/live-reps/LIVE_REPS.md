# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.914 |
| node-hours | 1.497 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.5 | 164.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 163.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 225 | 133.9 |
| response time (ms), 95th percentile | 366.3 | 168.5 |
| response time (ms), 99th percentile | 1551 | 757.5 |
| time over the response line (% of samples) | 7.146 | 5.223 |
| failed requests (%) | 4.406 | 3.744 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6617 | 0.5283 |
| utilisation (used / allocatable) | 0.06806 | 0.06723 |
| CPU used (cores), mean | 1.61 | 1.59 |
| Omni's own CPU (cores), mean | 0 | 0.00935 |
| CPU used with Omni's own (cores), mean | 1.61 | 1.6 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.5 | 414.2 |
| HPA replicas, mean | 8.654 | 9.832 |
| pods started | 5.2 | 6.1 |
| pod start wait, total (s) | 33.1 | 21.3 |
| pod start wait, mean (s) | 6.145 | 3.329 |
| host CPU busy, the real machine under kind (%) | 46.14 | 45.93 |
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
| worker nodes in service, mean | 5.914 | 5.914 | -0.0% | -0.00103 to +0.0004783 | no |
| node-hours | 1.497 | 1.492 | -0.3% | -0.01168 to +0.002015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.5 | 164.8 | -0.4% | -1.493 to +0.06063 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 163.1 | -0.4% | -1.493 to +0.0605 | no |
| response time (ms), mean | 225 | 133.9 | -40.5% | -157.5 to -24.78 | yes: GAIN |
| response time (ms), 95th percentile | 366.3 | 168.5 | -54.0% | -250 to -145.5 | yes: GAIN |
| response time (ms), 99th percentile | 1551 | 757.5 | -51.2% | -1532 to -54.63 | yes: GAIN |
| time over the response line (% of samples) | 7.146 | 5.223 | -26.9% | -2.983 to -0.8628 | yes: GAIN |
| failed requests (%) | 4.406 | 3.744 | -15.0% | -1.227 to -0.09669 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.1 | -20.3% | -2.314 to -0.2856 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 | +29.4 (native is 0) | +24.85 to +33.95 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6617 | 0.5283 | -20.2% | -0.7252 to +0.4586 | no |
| utilisation (used / allocatable) | 0.06806 | 0.06723 | -1.2% | -0.002752 to +0.001089 | no |
| CPU used (cores), mean | 1.61 | 1.59 | -1.2% | -0.06505 to +0.02561 | no |
| Omni's own CPU (cores), mean | 0 | 0.00935 | +0.00935 (native is 0) | +0.008016 to +0.01068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.6 | -0.6% | -0.05481 to +0.03407 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.5 | 414.2 | +0.2% | -13.92 to +15.19 | no |
| HPA replicas, mean | 8.654 | 9.832 | +13.6% | +0.0453 to +2.309 | yes: power given |
| pods started | 5.2 | 6.1 | +17.3% | -0.4254 to +2.225 | no |
| pod start wait, total (s) | 33.1 | 21.3 | -35.6% | -34.3 to +10.7 | no |
| pod start wait, mean (s) | 6.145 | 3.329 | -45.8% | -7.539 to +1.907 | no |
| host CPU busy, the real machine under kind (%) | 46.14 | 45.93 | -0.5% | -1.257 to +0.8334 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 58 | 14.3 |  |
| machine down | omni | 32 | 9.6 | -26 s (-45%) |
| spike | native | 237 | 48.8 |  |
| spike | omni | 238 | 41.5 | +1 s (+0%) |
| runaway pod started | native | 82 | 8.2 |  |
| runaway pod started | omni | 68 | 6.0 | -14 s (-18%) |
| probe blind | native | 62 | 0.5 |  |
| probe blind | omni | 60 | 0.1 | -2 s (-3%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*