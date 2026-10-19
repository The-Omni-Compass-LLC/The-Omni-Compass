# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 116.5 | 75.07 |
| response time (ms), 95th percentile | 242.7 | 117.3 |
| response time (ms), 99th percentile | 363.5 | 151.2 |
| time over the response line (% of samples) | 0.3838 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2117 | 0.2883 |
| utilisation (used / allocatable) | 0.03548 | 0.04536 |
| CPU used (cores), mean | 0.8516 | 1.089 |
| Omni's own CPU (cores), mean | 0 | 0.01129 |
| CPU used with Omni's own (cores), mean | 0.8516 | 1.1 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.3 | 595.8 |
| HPA replicas, mean | 8.806 | 8.964 |
| pods started | 4.8 | 5.1 |
| pod start wait, total (s) | 5.9 | 6.6 |
| pod start wait, mean (s) | 1.217 | 1.3 |
| host CPU busy, the real machine under kind (%) | 26.43 | 33.47 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.439e-17 to +1.367e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.514 | -0.4% | -0.01371 to +0.00204 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 160.7 | +1.1% | +0.4855 to +2.896 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 160.7 | +1.1% | +0.4855 to +2.896 | yes: power given |
| response time (ms), mean | 116.5 | 75.07 | -35.6% | -56.78 to -26.17 | yes: GAIN |
| response time (ms), 95th percentile | 242.7 | 117.3 | -51.7% | -153.4 to -97.43 | yes: GAIN |
| response time (ms), 99th percentile | 363.5 | 151.2 | -58.4% | -259.7 to -165 | yes: GAIN |
| time over the response line (% of samples) | 0.3838 | 0 | -100.0% | -0.6942 to -0.07335 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18 (native is 0) | +17.17 to +18.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2117 | 0.2883 | +36.2% | -0.202 to +0.3554 | no |
| utilisation (used / allocatable) | 0.03548 | 0.04536 | +27.8% | +0.006639 to +0.01312 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8516 | 1.089 | +27.8% | +0.1593 to +0.3149 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01129 | +0.0113 (native is 0) | +0.00977 to +0.01281 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8516 | 1.1 | +29.2% | +0.1692 to +0.3276 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 739.3 | 595.8 | -19.4% | -175.4 to -111.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.806 | 8.964 | +1.8% | +0.04022 to +0.2759 | yes: power given |
| pods started | 4.8 | 5.1 | +6.2% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 5.9 | 6.6 | +11.9% | -1.209 to +2.609 | no |
| pod start wait, mean (s) | 1.217 | 1.3 | +6.8% | -0.2649 to +0.4316 | no |
| host CPU busy, the real machine under kind (%) | 26.43 | 33.47 | +26.6% | +4.684 to +9.394 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*