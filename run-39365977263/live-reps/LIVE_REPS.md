# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.064 |
| node-hours | 2.512 | 2.123 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 244 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 504.1 | 453.8 |
| response time (ms), 95th percentile | 3009 | 3087 |
| response time (ms), 99th percentile | 4467 | 4502 |
| time over the response line (% of samples) | 15.6 | 15.27 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 186.8 | 188.2 |
| utilisation (used / allocatable) | 0.06194 | 0.07275 |
| CPU used (cores), mean | 1.487 | 1.471 |
| Omni's own CPU (cores), mean | 0 | 0.02261 |
| CPU used with Omni's own (cores), mean | 1.487 | 1.494 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.5 | 399.4 |
| HPA replicas, mean | 1.979 | 2.181 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 42.33 | 43.08 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 575.9 | 581.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.541 |

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
| worker nodes in service, mean | 6 | 5.064 | -15.6% | -1.445 to -0.428 | yes: GAIN |
| node-hours | 2.512 | 2.123 | -15.5% | -0.5989 to -0.1794 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.4 | +0.1% | -0.9381 to +1.679 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 244 | -10.7% | -44.57 to -13.62 | yes: GAIN |
| response time (ms), mean | 504.1 | 453.8 | -10.0% | -69.57 to -31.02 | yes: GAIN |
| response time (ms), 95th percentile | 3009 | 3087 | +2.6% | -14.53 to +170.7 | no |
| response time (ms), 99th percentile | 4467 | 4502 | +0.8% | -75.25 to +145.1 | no |
| time over the response line (% of samples) | 15.6 | 15.27 | -2.2% | -0.7606 to +0.08867 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.9 | -1.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.7 (native is 0) | +10.87 to +12.53 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 186.8 | 188.2 | +0.8% | -3.799 to +6.776 | no |
| utilisation (used / allocatable) | 0.06194 | 0.07275 | +17.5% | +0.004678 to +0.01694 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.471 | -1.0% | -0.04569 to +0.01544 | no |
| Omni's own CPU (cores), mean | 0 | 0.02261 | +0.0226 (native is 0) | +0.01878 to +0.02644 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.494 | +0.5% | -0.02542 to +0.04039 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.5 | 399.4 | -10.6% | -75.44 to -18.89 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 2.181 | +10.2% | -0.1067 to +0.5116 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 42.33 | 43.08 | +1.8% | +0.3271 to +1.162 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 575.9 | 581.6 | +1.0% | +1.027 to +10.37 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.541 | -24.3% | -2.194 to -0.7231 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*