# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.7 | 173.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.7 | 173.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 590 | 510.3 |
| response time (ms), 95th percentile | 2489 | 2282 |
| response time (ms), 99th percentile | 6154 | 6008 |
| time over the response line (% of samples) | 27.54 | 25.34 |
| failed requests (%) | 4.281 | 4.367 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.073 | 2.05 |
| utilisation (used / allocatable) | 0.1021 | 0.1015 |
| CPU used (cores), mean | 2.45 | 2.437 |
| Omni's own CPU (cores), mean | 0 | 0.01248 |
| CPU used with Omni's own (cores), mean | 2.45 | 2.449 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.2 | 288.2 |
| HPA replicas, mean | 15.03 | 15.39 |
| pods started | 5.3 | 3.9 |
| pod start wait, total (s) | 9.6 | 6.1 |
| pod start wait, mean (s) | 1.817 | 1.527 |
| host CPU busy, the real machine under kind (%) | 71.53 | 71.6 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 258.8 | 268.3 |
| second app: response time (ms), 99th percentile | 1511 | 1334 |
| second app: time over the response line (% of samples) | 15.88 | 15.74 |
| second app: failed requests (%) | 14.36 | 14.38 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.517 | +0.1% | -0.004009 to +0.007343 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.7 | 173.8 | +0.1% | -0.4951 to +0.7866 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.7 | 173.8 | +0.1% | -0.4951 to +0.7866 | no |
| response time (ms), mean | 590 | 510.3 | -13.5% | -151.2 to -8.348 | yes: GAIN |
| response time (ms), 95th percentile | 2489 | 2282 | -8.3% | -804.4 to +389.7 | no |
| response time (ms), 99th percentile | 6154 | 6008 | -2.4% | -1081 to +789.1 | no |
| time over the response line (% of samples) | 27.54 | 25.34 | -8.0% | -3.858 to -0.5495 | yes: GAIN |
| failed requests (%) | 4.281 | 4.367 | +2.0% | -1.154 to +1.327 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.1 | -3.2% | -0.8889 to +0.2889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 | +38 (native is 0) | +27.48 to +48.52 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.073 | 2.05 | +91.0% | +0.1324 to +1.821 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1021 | 0.1015 | -0.5% | -0.001339 to +0.0002871 | no |
| CPU used (cores), mean | 2.45 | 2.437 | -0.5% | -0.03214 to +0.006889 | no |
| Omni's own CPU (cores), mean | 0 | 0.01248 | +0.0125 (native is 0) | +0.01177 to +0.01319 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.449 | -0.0% | -0.0198 to +0.01952 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.2 | 288.2 | +0.3% | -1.118 to +2.999 | no |
| HPA replicas, mean | 15.03 | 15.39 | +2.4% | +0.008664 to +0.7223 | yes: power given |
| pods started | 5.3 | 3.9 | -26.4% | -2.477 to -0.3231 | yes: GAIN |
| pod start wait, total (s) | 9.6 | 6.1 | -36.5% | -5.639 to -1.361 | yes: GAIN |
| pod start wait, mean (s) | 1.817 | 1.527 | -15.9% | -0.5838 to +0.005262 | no |
| host CPU busy, the real machine under kind (%) | 71.53 | 71.6 | +0.1% | -0.5387 to +0.6884 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 258.8 | 268.3 | +3.7% | -20.7 to +39.64 | no |
| second app: response time (ms), 99th percentile | 1511 | 1334 | -11.7% | -928.4 to +575.8 | no |
| second app: time over the response line (% of samples) | 15.88 | 15.74 | -0.9% | -0.5754 to +0.3044 | no |
| second app: failed requests (%) | 14.36 | 14.38 | +0.2% | -0.4065 to +0.4497 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*