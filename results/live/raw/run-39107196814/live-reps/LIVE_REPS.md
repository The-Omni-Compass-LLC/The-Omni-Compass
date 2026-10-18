# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.438 |
| node-hours | 2.514 | 2.28 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 255.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 524 | 472.4 |
| response time (ms), 95th percentile | 3175 | 3122 |
| response time (ms), 99th percentile | 4703 | 4761 |
| time over the response line (% of samples) | 15.67 | 15.09 |
| failed requests (%) | 0.01081 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190 | 191.9 |
| utilisation (used / allocatable) | 0.06182 | 0.0682 |
| CPU used (cores), mean | 1.484 | 1.48 |
| Omni's own CPU (cores), mean | 0 | 0.02042 |
| CPU used with Omni's own (cores), mean | 1.484 | 1.5 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 418 |
| HPA replicas, mean | 2.118 | 2.329 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 3.3 | 8 |
| pod start wait, mean (s) | 3.3 | 4.2 |
| host CPU busy, the real machine under kind (%) | 42.63 | 43.28 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 582.1 | 585.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.124 |

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
| worker nodes in service, mean | 6 | 5.438 | -9.4% | -1.02 to -0.1033 | yes: GAIN |
| node-hours | 2.514 | 2.28 | -9.3% | -0.427 to -0.04057 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.5 | +0.1% | -0.836 to +1.625 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 255.8 | -6.3% | -31.76 to -2.77 | yes: GAIN |
| response time (ms), mean | 524 | 472.4 | -9.8% | -65.46 to -37.58 | yes: GAIN |
| response time (ms), 95th percentile | 3175 | 3122 | -1.7% | -203.7 to +97.27 | no |
| response time (ms), 99th percentile | 4703 | 4761 | +1.2% | -242.8 to +357.5 | no |
| time over the response line (% of samples) | 15.67 | 15.09 | -3.7% | -1.052 to -0.1085 | yes: GAIN |
| failed requests (%) | 0.01081 | 0 | -100.0% | -0.03526 to +0.01364 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 10.1 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 | +11.8 (native is 0) | +11.06 to +12.54 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190 | 191.9 | +1.0% | -3.159 to +7.022 | no |
| utilisation (used / allocatable) | 0.06182 | 0.0682 | +10.3% | +0.0004334 to +0.01232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.484 | 1.48 | -0.3% | -0.04581 to +0.03791 | no |
| Omni's own CPU (cores), mean | 0 | 0.02042 | +0.0204 (native is 0) | +0.01631 to +0.02453 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.484 | 1.5 | +1.1% | -0.02536 to +0.0583 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 418 | -6.5% | -61.75 to +3.232 | no |
| HPA replicas, mean | 2.118 | 2.329 | +10.0% | -0.1317 to +0.5544 | no |
| pods started | 0.1 | 0.6 | +500.0% | -0.1079 to +1.108 | no |
| pod start wait, total (s) | 3.3 | 8 | +142.4% | -14.74 to +24.14 | no |
| pod start wait, mean (s) | 3.3 | 4.2 | +27.3% | -11.09 to +12.89 | no |
| host CPU busy, the real machine under kind (%) | 42.63 | 43.28 | +1.5% | +0.3764 to +0.9271 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 582.1 | 585.3 | +0.5% | -0.4908 to +6.891 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.124 | -14.6% | -1.539 to -0.2125 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*