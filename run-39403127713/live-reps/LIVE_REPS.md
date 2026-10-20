# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.335 | 4.333 |
| energy, parked workers still on at idle power (Wh, declared model) | 481.6 | 479.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.6 | 479.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 276.7 | 147.1 |
| response time (ms), 95th percentile | 710.2 | 321 |
| response time (ms), 99th percentile | 1362 | 837.8 |
| time over the response line (% of samples) | 14.25 | 3.981 |
| failed requests (%) | 1.45 | 1.244 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.395 | 1.352 |
| utilisation (used / allocatable) | 0.07884 | 0.07627 |
| CPU used (cores), mean | 1.892 | 1.83 |
| Omni's own CPU (cores), mean | 0 | 0.01 |
| CPU used with Omni's own (cores), mean | 1.892 | 1.84 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 396.7 | 410.7 |
| HPA replicas, mean | 9.622 | 11.09 |
| pods started | 6.6 | 17.4 |
| pod start wait, total (s) | 10.5 | 30.8 |
| pod start wait, mean (s) | 1.61 | 1.714 |
| host CPU busy, the real machine under kind (%) | 54.77 | 53.65 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.25e-15 to +3.623e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.335 | 4.333 | -0.0% | -0.008124 to +0.00479 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 481.6 | 479.7 | -0.4% | -2.58 to -1.147 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.6 | 479.7 | -0.4% | -2.58 to -1.147 | yes: GAIN |
| response time (ms), mean | 276.7 | 147.1 | -46.8% | -177.4 to -81.74 | yes: GAIN |
| response time (ms), 95th percentile | 710.2 | 321 | -54.8% | -523.4 to -255.1 | yes: GAIN |
| response time (ms), 99th percentile | 1362 | 837.8 | -38.5% | -729 to -319.4 | yes: GAIN |
| time over the response line (% of samples) | 14.25 | 3.981 | -72.1% | -15.32 to -5.226 | yes: GAIN |
| failed requests (%) | 1.45 | 1.244 | -14.1% | -0.3349 to -0.07526 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 10.1 | -57.2% | -20.06 to -6.942 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68 | +68 (native is 0) | +46.75 to +89.25 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.395 | 1.352 | +242.2% | +0.3281 to +1.585 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07884 | 0.07627 | -3.3% | -0.00312 to -0.002026 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.892 | 1.83 | -3.3% | -0.07488 to -0.04862 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01 | +0.01 (native is 0) | +0.007899 to +0.0121 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.892 | 1.84 | -2.7% | -0.06399 to -0.03951 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 396.7 | 410.7 | +3.5% | +5.917 to +22.11 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.622 | 11.09 | +15.2% | -0.07355 to +3.001 | no |
| pods started | 6.6 | 17.4 | +163.6% | +5.04 to +16.56 | yes: power given |
| pod start wait, total (s) | 10.5 | 30.8 | +193.3% | +8.326 to +32.27 | yes: LOSS |
| pod start wait, mean (s) | 1.61 | 1.714 | +6.5% | -0.1885 to +0.397 | no |
| host CPU busy, the real machine under kind (%) | 54.77 | 53.65 | -2.0% | -1.499 to -0.7395 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*