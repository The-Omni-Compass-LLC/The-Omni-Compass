# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.333 |
| energy, parked workers still on at idle power (Wh, declared model) | 485.8 | 484.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.8 | 484.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 306.1 | 168.3 |
| response time (ms), 95th percentile | 791.8 | 377.7 |
| response time (ms), 99th percentile | 1529 | 964.7 |
| time over the response line (% of samples) | 15.47 | 4.72 |
| failed requests (%) | 1.642 | 1.365 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28 | 12.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.475 | 1.017 |
| utilisation (used / allocatable) | 0.08568 | 0.08396 |
| CPU used (cores), mean | 2.056 | 2.015 |
| Omni's own CPU (cores), mean | 0 | 0.03061 |
| CPU used with Omni's own (cores), mean | 2.056 | 2.046 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 349.9 | 357 |
| HPA replicas, mean | 9.762 | 12.21 |
| pods started | 5.5 | 18.3 |
| pod start wait, total (s) | 7.6 | 30.8 |
| pod start wait, mean (s) | 1.418 | 1.697 |
| host CPU busy, the real machine under kind (%) | 59.01 | 58.86 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.216e-15 to +1.5e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.333 | -0.0% | -0.009043 to +0.00871 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 485.8 | 484.7 | -0.2% | -2.262 to +0.05805 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.8 | 484.7 | -0.2% | -2.262 to +0.05805 | no |
| response time (ms), mean | 306.1 | 168.3 | -45.0% | -169.7 to -105.8 | yes: GAIN |
| response time (ms), 95th percentile | 791.8 | 377.7 | -52.3% | -509 to -319.3 | yes: GAIN |
| response time (ms), 99th percentile | 1529 | 964.7 | -36.9% | -746 to -383.4 | yes: GAIN |
| time over the response line (% of samples) | 15.47 | 4.72 | -69.5% | -14.05 to -7.444 | yes: GAIN |
| failed requests (%) | 1.642 | 1.365 | -16.9% | -0.4432 to -0.1103 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28 | 12.2 | -56.4% | -20.33 to -11.27 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.6 | +84.6 (native is 0) | +69.92 to +99.28 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.475 | 1.017 | +114.0% | +0.008945 to +1.074 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08568 | 0.08396 | -2.0% | -0.002761 to -0.0006812 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.056 | 2.015 | -2.0% | -0.06625 to -0.01635 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03061 | +0.0306 (native is 0) | +0.02666 to +0.03456 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.056 | 2.046 | -0.5% | -0.03653 to +0.01515 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 349.9 | 357 | +2.0% | +2.661 to +11.63 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.762 | 12.21 | +25.1% | +1.074 to +3.819 | yes: power given |
| pods started | 5.5 | 18.3 | +232.7% | +8.618 to +16.98 | yes: power given |
| pod start wait, total (s) | 7.6 | 30.8 | +305.3% | +16.19 to +30.21 | yes: LOSS |
| pod start wait, mean (s) | 1.418 | 1.697 | +19.6% | +0.01195 to +0.5446 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.01 | 58.86 | -0.2% | -0.8088 to +0.5238 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*