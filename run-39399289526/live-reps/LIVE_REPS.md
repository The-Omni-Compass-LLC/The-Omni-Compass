# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.4 | 173 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.4 | 173 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 582.2 | 501.2 |
| response time (ms), 95th percentile | 2528 | 2389 |
| response time (ms), 99th percentile | 6054 | 5584 |
| time over the response line (% of samples) | 26.28 | 24.06 |
| failed requests (%) | 4.259 | 4.098 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 8.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.28 | 1.498 |
| utilisation (used / allocatable) | 0.1004 | 0.09902 |
| CPU used (cores), mean | 2.41 | 2.376 |
| Omni's own CPU (cores), mean | 0 | 0.01178 |
| CPU used with Omni's own (cores), mean | 2.41 | 2.388 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294 | 299.2 |
| HPA replicas, mean | 15.07 | 15.41 |
| pods started | 5.1 | 3.5 |
| pod start wait, total (s) | 8.9 | 6.3 |
| pod start wait, mean (s) | 1.719 | 1.736 |
| host CPU busy, the real machine under kind (%) | 70.33 | 70.31 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 298.3 | 282.6 |
| second app: response time (ms), 99th percentile | 1091 | 933.5 |
| second app: time over the response line (% of samples) | 15.24 | 15.24 |
| second app: failed requests (%) | 13.84 | 14.22 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.044e-17 to +5.733e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.515 | -0.0% | -0.006958 to +0.005958 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.4 | 173 | -0.2% | -1.082 to +0.4113 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.4 | 173 | -0.2% | -1.082 to +0.4113 | no |
| response time (ms), mean | 582.2 | 501.2 | -13.9% | -129.8 to -32.19 | yes: GAIN |
| response time (ms), 95th percentile | 2528 | 2389 | -5.5% | -499.4 to +220.9 | no |
| response time (ms), 99th percentile | 6054 | 5584 | -7.8% | -1116 to +176.8 | no |
| time over the response line (% of samples) | 26.28 | 24.06 | -8.4% | -4.451 to +0.01601 | no |
| failed requests (%) | 4.259 | 4.098 | -3.8% | -0.7872 to +0.4648 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 8.6 | -7.5% | -1.529 to +0.1294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.1 (native is 0) | +30.77 to +33.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.28 | 1.498 | +17.1% | -0.5738 to +1.01 | no |
| utilisation (used / allocatable) | 0.1004 | 0.09902 | -1.4% | -0.002802 to +9.266e-06 | no |
| CPU used (cores), mean | 2.41 | 2.376 | -1.4% | -0.06725 to +0.0002224 | no |
| Omni's own CPU (cores), mean | 0 | 0.01178 | +0.0118 (native is 0) | +0.01039 to +0.01317 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.41 | 2.388 | -0.9% | -0.05614 to +0.01267 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 294 | 299.2 | +1.8% | -2.354 to +12.74 | no |
| HPA replicas, mean | 15.07 | 15.41 | +2.2% | +0.01564 to +0.6583 | yes: power given |
| pods started | 5.1 | 3.5 | -31.4% | -2.566 to -0.6344 | yes: GAIN |
| pod start wait, total (s) | 8.9 | 6.3 | -29.2% | -4.965 to -0.2348 | yes: GAIN |
| pod start wait, mean (s) | 1.719 | 1.736 | +1.0% | -0.4172 to +0.4506 | no |
| host CPU busy, the real machine under kind (%) | 70.33 | 70.31 | -0.0% | -0.4924 to +0.4476 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 298.3 | 282.6 | -5.3% | -43.06 to +11.62 | no |
| second app: response time (ms), 99th percentile | 1091 | 933.5 | -14.4% | -635.6 to +321.3 | no |
| second app: time over the response line (% of samples) | 15.24 | 15.24 | +0.0% | -0.609 to +0.6189 | no |
| second app: failed requests (%) | 13.84 | 14.22 | +2.7% | -0.07183 to +0.8278 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*