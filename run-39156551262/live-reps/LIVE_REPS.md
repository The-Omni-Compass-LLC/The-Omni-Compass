# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.2 |
| node-hours | 2.513 | 2.177 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 248.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 551.5 | 500.1 |
| response time (ms), 95th percentile | 3262 | 3383 |
| response time (ms), 99th percentile | 4742 | 4904 |
| time over the response line (% of samples) | 16.22 | 15.4 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 196.4 | 196.5 |
| utilisation (used / allocatable) | 0.06356 | 0.07411 |
| CPU used (cores), mean | 1.525 | 1.537 |
| Omni's own CPU (cores), mean | 0 | 0.02276 |
| CPU used with Omni's own (cores), mean | 1.525 | 1.56 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.4 | 388.6 |
| HPA replicas, mean | 2.22 | 2.258 |
| pods started | 0.4 | 0.3 |
| pod start wait, total (s) | 16.7 | 4.5 |
| pod start wait, mean (s) | 13.9 | 4.5 |
| host CPU busy, the real machine under kind (%) | 43.93 | 44.85 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 601.6 | 608.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.71 |

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
| worker nodes in service, mean | 6 | 5.2 | -13.3% | -1.326 to -0.2742 | yes: GAIN |
| node-hours | 2.513 | 2.177 | -13.4% | -0.5545 to -0.1181 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 274 | +0.1% | -0.9281 to +1.373 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 248.8 | -9.1% | -41.2 to -8.624 | yes: GAIN |
| response time (ms), mean | 551.5 | 500.1 | -9.3% | -70.89 to -31.93 | yes: GAIN |
| response time (ms), 95th percentile | 3262 | 3383 | +3.7% | -6.377 to +248.6 | no |
| response time (ms), 99th percentile | 4742 | 4904 | +3.4% | +65.06 to +260.3 | yes: LOSS |
| time over the response line (% of samples) | 16.22 | 15.4 | -5.0% | -1.319 to -0.3098 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.4 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 | +11.8 (native is 0) | +11.06 to +12.54 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 196.4 | 196.5 | +0.1% | -8.281 to +8.485 | no |
| utilisation (used / allocatable) | 0.06356 | 0.07411 | +16.6% | +0.004139 to +0.01696 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.525 | 1.537 | +0.8% | -0.01289 to +0.03601 | no |
| Omni's own CPU (cores), mean | 0 | 0.02276 | +0.0228 (native is 0) | +0.01778 to +0.02774 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.525 | 1.56 | +2.3% | +0.0102 to +0.05844 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.4 | 388.6 | -10.7% | -80.85 to -12.55 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.22 | 2.258 | +1.7% | -0.2926 to +0.3678 | no |
| pods started | 0.4 | 0.3 | -25.0% | -0.6278 to +0.4278 | no |
| pod start wait, total (s) | 16.7 | 4.5 | -73.1% | -35.91 to +11.51 | no |
| pod start wait, mean (s) | 13.9 | 4.5 | -67.6% | -30.98 to +12.18 | no |
| host CPU busy, the real machine under kind (%) | 43.93 | 44.85 | +2.1% | +0.3958 to +1.453 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 601.6 | 608.6 | +1.2% | -1.921 to +15.92 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.71 | -21.5% | -2.068 to -0.513 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*