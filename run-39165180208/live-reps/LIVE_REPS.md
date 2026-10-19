# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.332 | 4.341 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.8 | 479.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.8 | 479.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 269.6 | 138.4 |
| response time (ms), 95th percentile | 707.3 | 292.7 |
| response time (ms), 99th percentile | 1294 | 708.7 |
| time over the response line (% of samples) | 13.02 | 3.274 |
| failed requests (%) | 1.274 | 1.049 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22 | 8.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8017 | 1.075 |
| utilisation (used / allocatable) | 0.07796 | 0.07516 |
| CPU used (cores), mean | 1.871 | 1.804 |
| Omni's own CPU (cores), mean | 0 | 0.00926 |
| CPU used with Omni's own (cores), mean | 1.871 | 1.813 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 392.7 | 404.4 |
| HPA replicas, mean | 9.687 | 10.67 |
| pods started | 5.2 | 14.7 |
| pod start wait, total (s) | 15.9 | 34.9 |
| pod start wait, mean (s) | 2.476 | 2.467 |
| host CPU busy, the real machine under kind (%) | 54.09 | 52.6 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.332 | 4.341 | +0.2% | +0.0007308 to +0.01594 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 480.8 | 479.8 | -0.2% | -2.103 to +0.2163 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.8 | 479.8 | -0.2% | -2.103 to +0.2163 | no |
| response time (ms), mean | 269.6 | 138.4 | -48.7% | -176.3 to -86.06 | yes: GAIN |
| response time (ms), 95th percentile | 707.3 | 292.7 | -58.6% | -544.3 to -284.9 | yes: GAIN |
| response time (ms), 99th percentile | 1294 | 708.7 | -45.2% | -739.7 to -430.9 | yes: GAIN |
| time over the response line (% of samples) | 13.02 | 3.274 | -74.8% | -14.75 to -4.74 | yes: GAIN |
| failed requests (%) | 1.274 | 1.049 | -17.6% | -0.3755 to -0.07401 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22 | 8.5 | -61.4% | -19.49 to -7.513 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.5 | +57.5 (native is 0) | +40.93 to +74.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8017 | 1.075 | +34.1% | -0.1305 to +0.6771 | no |
| utilisation (used / allocatable) | 0.07796 | 0.07516 | -3.6% | -0.003745 to -0.001856 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.871 | 1.804 | -3.6% | -0.08988 to -0.04455 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00926 | +0.00926 (native is 0) | +0.007531 to +0.01099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.871 | 1.813 | -3.1% | -0.07941 to -0.0365 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 392.7 | 404.4 | +3.0% | +6.843 to +16.56 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.687 | 10.67 | +10.1% | -0.1905 to +2.147 | no |
| pods started | 5.2 | 14.7 | +182.7% | +4.776 to +14.22 | yes: power given |
| pod start wait, total (s) | 15.9 | 34.9 | +119.5% | +7.035 to +30.96 | yes: LOSS |
| pod start wait, mean (s) | 2.476 | 2.467 | -0.4% | -0.8893 to +0.8716 | no |
| host CPU busy, the real machine under kind (%) | 54.09 | 52.6 | -2.8% | -2.186 to -0.7917 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*