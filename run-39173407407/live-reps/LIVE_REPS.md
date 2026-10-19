# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.338 | 4.33 |
| energy, parked workers still on at idle power (Wh, declared model) | 483.5 | 480.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.5 | 480.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 286.4 | 144 |
| response time (ms), 95th percentile | 731.4 | 275.2 |
| response time (ms), 99th percentile | 1531 | 875.8 |
| time over the response line (% of samples) | 13.03 | 3.203 |
| failed requests (%) | 1.2 | 0.9387 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.8 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 8.333 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.7083 |
| utilisation (used / allocatable) | 0.08125 | 0.07762 |
| CPU used (cores), mean | 1.95 | 1.863 |
| Omni's own CPU (cores), mean | 0 | 0.00961 |
| CPU used with Omni's own (cores), mean | 1.95 | 1.872 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 362.5 | 381.4 |
| HPA replicas, mean | 9.808 | 11.2 |
| pods started | 5.5 | 16.6 |
| pod start wait, total (s) | 8.1 | 29.4 |
| pod start wait, mean (s) | 1.453 | 1.739 |
| host CPU busy, the real machine under kind (%) | 56.04 | 54.23 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.033e-16 to +9.586e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.338 | 4.33 | -0.2% | -0.01437 to -0.000965 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 483.5 | 480.3 | -0.7% | -3.998 to -2.397 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.5 | 480.3 | -0.7% | -3.998 to -2.397 | yes: GAIN |
| response time (ms), mean | 286.4 | 144 | -49.7% | -180 to -104.8 | yes: GAIN |
| response time (ms), 95th percentile | 731.4 | 275.2 | -62.4% | -572.2 to -340.1 | yes: GAIN |
| response time (ms), 99th percentile | 1531 | 875.8 | -42.8% | -918.2 to -393.1 | yes: GAIN |
| time over the response line (% of samples) | 13.03 | 3.203 | -75.4% | -14.12 to -5.545 | yes: GAIN |
| failed requests (%) | 1.2 | 0.9387 | -21.8% | -0.4159 to -0.1076 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.8 | 8.2 | -65.5% | -21.16 to -10.04 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.1 | +63.1 (native is 0) | +46.57 to +79.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.7083 | +58.6% | -0.1304 to +0.6537 | no |
| utilisation (used / allocatable) | 0.08125 | 0.07762 | -4.5% | -0.004338 to -0.002932 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.95 | 1.863 | -4.5% | -0.1041 to -0.07038 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00961 | +0.00961 (native is 0) | +0.007996 to +0.01122 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.95 | 1.872 | -4.0% | -0.09492 to -0.06034 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 362.5 | 381.4 | +5.2% | +5.234 to +32.63 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.808 | 11.2 | +14.2% | +0.05933 to +2.721 | yes: power given |
| pods started | 5.5 | 16.6 | +201.8% | +7.132 to +15.07 | yes: power given |
| pod start wait, total (s) | 8.1 | 29.4 | +263.0% | +13.04 to +29.56 | yes: LOSS |
| pod start wait, mean (s) | 1.453 | 1.739 | +19.7% | +0.002583 to +0.5693 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.04 | 54.23 | -3.2% | -2.31 to -1.313 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*