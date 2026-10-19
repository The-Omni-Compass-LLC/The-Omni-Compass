# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.192 |
| node-hours | 2.515 | 2.179 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 248.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 513.3 | 460.1 |
| response time (ms), 95th percentile | 3045 | 3076 |
| response time (ms), 99th percentile | 4624 | 4774 |
| time over the response line (% of samples) | 15.77 | 15.01 |
| failed requests (%) | 0.01075 | 0.01036 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189 | 187.3 |
| utilisation (used / allocatable) | 0.06206 | 0.07146 |
| CPU used (cores), mean | 1.489 | 1.473 |
| Omni's own CPU (cores), mean | 0 | 0.02029 |
| CPU used with Omni's own (cores), mean | 1.489 | 1.493 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.1 | 403.4 |
| HPA replicas, mean | 2.193 | 2.077 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 42.49 | 42.92 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 580.5 | 578.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.734 |

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
| worker nodes in service, mean | 6 | 5.192 | -13.5% | -1.352 to -0.2639 | yes: GAIN |
| node-hours | 2.515 | 2.179 | -13.4% | -0.5705 to -0.1026 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.5 | +0.1% | -0.8326 to +1.23 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 248.1 | -9.2% | -43.02 to -7.432 | yes: GAIN |
| response time (ms), mean | 513.3 | 460.1 | -10.4% | -70.07 to -36.4 | yes: GAIN |
| response time (ms), 95th percentile | 3045 | 3076 | +1.0% | -125.3 to +186.9 | no |
| response time (ms), 99th percentile | 4624 | 4774 | +3.2% | -121.8 to +422.2 | no |
| time over the response line (% of samples) | 15.77 | 15.01 | -4.8% | -1.292 to -0.2292 | yes: GAIN |
| failed requests (%) | 0.01075 | 0.01036 | -3.6% | -0.001272 to +0.0004922 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 | +11.5 (native is 0) | +10.89 to +12.11 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189 | 187.3 | -0.9% | -7.323 to +3.809 | no |
| utilisation (used / allocatable) | 0.06206 | 0.07146 | +15.2% | +0.002828 to +0.01598 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.489 | 1.473 | -1.1% | -0.03286 to +0.0003556 | no |
| Omni's own CPU (cores), mean | 0 | 0.02029 | +0.0203 (native is 0) | +0.01614 to +0.02444 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.489 | 1.493 | +0.3% | -0.01457 to +0.02264 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.1 | 403.4 | -9.0% | -70.97 to -8.478 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.193 | 2.077 | -5.3% | -0.4415 to +0.21 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| host CPU busy, the real machine under kind (%) | 42.49 | 42.92 | +1.0% | -0.1567 to +1.019 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 580.5 | 578.6 | -0.3% | -8.993 to +5.193 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.734 | -21.1% | -2.064 to -0.4672 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*