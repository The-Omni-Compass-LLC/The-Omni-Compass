# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.517 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 515.3 | 513.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.3 | 513.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 273.1 | 151.8 |
| response time (ms), 95th percentile | 716.7 | 294.8 |
| response time (ms), 99th percentile | 2259 | 1389 |
| time over the response line (% of samples) | 17.42 | 10.51 |
| failed requests (%) | 9.221 | 7.967 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.8 | 19.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.4067 |
| utilisation (used / allocatable) | 0.09887 | 0.09679 |
| CPU used (cores), mean | 2.373 | 2.323 |
| Omni's own CPU (cores), mean | 0 | 0.02893 |
| CPU used with Omni's own (cores), mean | 2.373 | 2.352 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 308.3 | 313.9 |
| HPA replicas, mean | 9.583 | 10.52 |
| pods started | 5.5 | 8.4 |
| pod start wait, total (s) | 8.6 | 14.9 |
| pod start wait, mean (s) | 1.574 | 1.743 |
| host CPU busy, the real machine under kind (%) | 66.83 | 66.49 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.014e-15 to +6.588e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.517 | 4.512 | -0.1% | -0.01095 to +0.001283 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515.3 | 513.4 | -0.4% | -2.765 to -0.9395 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.3 | 513.4 | -0.4% | -2.765 to -0.9395 | yes: GAIN |
| response time (ms), mean | 273.1 | 151.8 | -44.4% | -154.6 to -87.95 | yes: GAIN |
| response time (ms), 95th percentile | 716.7 | 294.8 | -58.9% | -517.2 to -326.6 | yes: GAIN |
| response time (ms), 99th percentile | 2259 | 1389 | -38.5% | -1275 to -465.2 | yes: GAIN |
| time over the response line (% of samples) | 17.42 | 10.51 | -39.7% | -9.54 to -4.296 | yes: GAIN |
| failed requests (%) | 9.221 | 7.967 | -13.6% | -2.153 to -0.356 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.8 | 19.5 | -27.2% | -8.81 to -5.79 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.3 | +53.3 (native is 0) | +45.04 to +61.56 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.4067 | +17.9% | -0.1167 to +0.24 | no |
| utilisation (used / allocatable) | 0.09887 | 0.09679 | -2.1% | -0.002872 to -0.001299 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.373 | 2.323 | -2.1% | -0.06892 to -0.03117 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02893 | +0.0289 (native is 0) | +0.02584 to +0.03202 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.373 | 2.352 | -0.9% | -0.03857 to -0.003653 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 308.3 | 313.9 | +1.8% | +4.041 to +7.291 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.583 | 10.52 | +9.7% | -0.01972 to +1.886 | no |
| pods started | 5.5 | 8.4 | +52.7% | +0.1929 to +5.607 | yes: power given |
| pod start wait, total (s) | 8.6 | 14.9 | +73.3% | +0.4786 to +12.12 | yes: LOSS |
| pod start wait, mean (s) | 1.574 | 1.743 | +10.7% | -0.1495 to +0.4867 | no |
| host CPU busy, the real machine under kind (%) | 66.83 | 66.49 | -0.5% | -0.8914 to +0.2059 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*