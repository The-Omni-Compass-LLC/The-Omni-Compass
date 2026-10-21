# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 123.3 | 78.05 |
| response time (ms), 95th percentile | 250.6 | 117.9 |
| response time (ms), 99th percentile | 369.8 | 158.3 |
| time over the response line (% of samples) | 0.3862 | 0.02424 |
| failed requests (%) | 0.01299 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.1317 |
| utilisation (used / allocatable) | 0.03554 | 0.04612 |
| CPU used (cores), mean | 0.8531 | 1.107 |
| Omni's own CPU (cores), mean | 0 | 0.01313 |
| CPU used with Omni's own (cores), mean | 0.8531 | 1.12 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.9 | 583.8 |
| HPA replicas, mean | 8.798 | 9.117 |
| pods started | 5.5 | 4.8 |
| pod start wait, total (s) | 7.8 | 8.2 |
| pod start wait, mean (s) | 1.43 | 1.688 |
| host CPU busy, the real machine under kind (%) | 27 | 34.7 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | no |
| node-hours | 1.512 | 1.512 | +0.0% | -0.01043 to +0.0111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.6 | +1.6% | +0.9742 to +4.035 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.6 | +1.6% | +0.9742 to +4.035 | yes: power given |
| response time (ms), mean | 123.3 | 78.05 | -36.7% | -58.75 to -31.76 | yes: GAIN |
| response time (ms), 95th percentile | 250.6 | 117.9 | -52.9% | -156.5 to -108.8 | yes: GAIN |
| response time (ms), 99th percentile | 369.8 | 158.3 | -57.2% | -253.3 to -169.8 | yes: GAIN |
| time over the response line (% of samples) | 0.3862 | 0.02424 | -93.7% | -0.674 to -0.04982 | yes: GAIN |
| failed requests (%) | 0.01299 | 0 | -100.0% | -0.04236 to +0.01639 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.3 | +23.3 (native is 0) | +16.82 to +29.78 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.1317 | -50.3% | -0.3916 to +0.1249 | no |
| utilisation (used / allocatable) | 0.03554 | 0.04612 | +29.7% | +0.007928 to +0.01321 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8531 | 1.107 | +29.7% | +0.1903 to +0.3171 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01313 | +0.0131 (native is 0) | +0.01086 to +0.0154 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8531 | 1.12 | +31.3% | +0.2018 to +0.3319 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.9 | 583.8 | -20.9% | -178.3 to -130 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.798 | 9.117 | +3.6% | +0.1266 to +0.5098 | yes: power given |
| pods started | 5.5 | 4.8 | -12.7% | -1.714 to +0.3144 | no |
| pod start wait, total (s) | 7.8 | 8.2 | +5.1% | -1.601 to +2.401 | no |
| pod start wait, mean (s) | 1.43 | 1.688 | +18.1% | -0.08533 to +0.602 | no |
| host CPU busy, the real machine under kind (%) | 27 | 34.7 | +28.5% | +5.775 to +9.613 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*