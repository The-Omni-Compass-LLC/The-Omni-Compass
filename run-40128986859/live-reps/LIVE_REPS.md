# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.5 | 511.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.5 | 511.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 249.1 | 139.9 |
| response time (ms), 95th percentile | 668.7 | 286 |
| response time (ms), 99th percentile | 2107 | 1484 |
| time over the response line (% of samples) | 16.29 | 9.879 |
| failed requests (%) | 8.801 | 7.843 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 18.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.405 | 0.3683 |
| utilisation (used / allocatable) | 0.09543 | 0.09378 |
| CPU used (cores), mean | 2.29 | 2.251 |
| Omni's own CPU (cores), mean | 0 | 0.00847 |
| CPU used with Omni's own (cores), mean | 2.29 | 2.259 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 326.7 | 332.3 |
| HPA replicas, mean | 9.5 | 10.11 |
| pods started | 5.9 | 6.4 |
| pod start wait, total (s) | 8.7 | 10.8 |
| pod start wait, mean (s) | 1.493 | 1.695 |
| host CPU busy, the real machine under kind (%) | 64.51 | 63.77 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 4.512 | 4.515 | +0.1% | −0.0043 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.5 | 511.7 | −0.1% | −1.7217 to +0.2309 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.5 | 511.7 | −0.1% | −1.7217 to +0.2309 | no |
| response time (ms), mean | 249.1 | 139.9 | −43.8% | −148.4061 to −69.8747 | yes: GAIN |
| response time (ms), 95th percentile | 668.7 | 286 | −57.2% | −516.4864 to −248.8436 | yes: GAIN |
| response time (ms), 99th percentile | 2107 | 1484 | −29.6% | −1423.5899 to +177.2319 | no |
| time over the response line (% of samples) | 16.29 | 9.879 | −39.4% | −9.1463 to −3.6826 | yes: GAIN |
| failed requests (%) | 8.801 | 7.843 | −10.9% | −1.6299 to −0.2857 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 18.2 | −27.2% | −8.9004 to −4.6996 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.2 | +38.200 (native is 0) | +28.3644 to +48.0356 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.405 | 0.3683 | −9.1% | −0.2867 to +0.2134 | no |
| utilisation (used / allocatable) | 0.09543 | 0.09378 | −1.7% | −0.0023 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.29 | 2.251 | −1.7% | −0.0562 to −0.0230 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00847 | +0.008 (native is 0) | +0.0071 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.29 | 2.259 | −1.4% | −0.0475 to −0.0148 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 326.7 | 332.3 | +1.7% | +1.3580 to +9.9521 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.5 | 10.11 | +6.5% | −0.5043 to +1.7333 | no |
| pods started | 5.9 | 6.4 | +8.5% | −2.1174 to +3.1174 | no |
| pod start wait, total (s) | 8.7 | 10.8 | +24.1% | −2.9292 to +7.1292 | no |
| pod start wait, mean (s) | 1.493 | 1.695 | +13.5% | −0.0222 to +0.4252 | no |
| host CPU busy, the real machine under kind (%) | 64.51 | 63.77 | −1.1% | −1.1606 to −0.3154 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*