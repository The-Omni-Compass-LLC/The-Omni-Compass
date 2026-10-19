# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 516 | 515 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516 | 515 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 275.7 | 153.9 |
| response time (ms), 95th percentile | 696.2 | 330.7 |
| response time (ms), 99th percentile | 2702 | 1441 |
| time over the response line (% of samples) | 18.56 | 12.4 |
| failed requests (%) | 11.07 | 9.856 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.2 | 21.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.27 |
| utilisation (used / allocatable) | 0.1005 | 0.09851 |
| CPU used (cores), mean | 2.412 | 2.364 |
| Omni's own CPU (cores), mean | 0 | 0.00879 |
| CPU used with Omni's own (cores), mean | 2.412 | 2.373 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 318.2 | 326.4 |
| HPA replicas, mean | 9.555 | 9.627 |
| pods started | 5.4 | 6.1 |
| pod start wait, total (s) | 8.1 | 9.9 |
| pod start wait, mean (s) | 1.523 | 1.502 |
| host CPU busy, the real machine under kind (%) | 67.85 | 66.85 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.038e-15 to +3.277e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.516 | +0.0% | -0.004389 to +0.008722 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516 | 515 | -0.2% | -2.109 to +0.01358 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516 | 515 | -0.2% | -2.109 to +0.01358 | no |
| response time (ms), mean | 275.7 | 153.9 | -44.2% | -158.8 to -84.65 | yes: GAIN |
| response time (ms), 95th percentile | 696.2 | 330.7 | -52.5% | -456.4 to -274.7 | yes: GAIN |
| response time (ms), 99th percentile | 2702 | 1441 | -46.7% | -2064 to -458.3 | yes: GAIN |
| time over the response line (% of samples) | 18.56 | 12.4 | -33.2% | -8.608 to -3.697 | yes: GAIN |
| failed requests (%) | 11.07 | 9.856 | -10.9% | -1.938 to -0.4845 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.2 | 21.4 | -21.3% | -7.053 to -4.547 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 | +38.3 (native is 0) | +29.92 to +46.68 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2183 | 0.27 | +23.7% | -0.1724 to +0.2757 | no |
| utilisation (used / allocatable) | 0.1005 | 0.09851 | -2.0% | -0.002604 to -0.001378 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.412 | 2.364 | -2.0% | -0.06251 to -0.03308 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00879 | +0.00879 (native is 0) | +0.007176 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.412 | 2.373 | -1.6% | -0.05415 to -0.02386 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 318.2 | 326.4 | +2.6% | +1.932 to +14.4 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.555 | 9.627 | +0.8% | -0.314 to +0.4579 | no |
| pods started | 5.4 | 6.1 | +13.0% | -1.869 to +3.269 | no |
| pod start wait, total (s) | 8.1 | 9.9 | +22.2% | -3.301 to +6.901 | no |
| pod start wait, mean (s) | 1.523 | 1.502 | -1.4% | -0.3798 to +0.3382 | no |
| host CPU busy, the real machine under kind (%) | 67.85 | 66.85 | -1.5% | -1.421 to -0.5881 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*