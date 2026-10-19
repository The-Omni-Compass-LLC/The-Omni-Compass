# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 516.9 | 515.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.9 | 515.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 262.4 | 146.3 |
| response time (ms), 95th percentile | 663.8 | 279.5 |
| response time (ms), 99th percentile | 2171 | 1257 |
| time over the response line (% of samples) | 18.98 | 12.39 |
| failed requests (%) | 11.99 | 10.43 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.4 | 21.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.51 |
| utilisation (used / allocatable) | 0.1016 | 0.09966 |
| CPU used (cores), mean | 2.438 | 2.392 |
| Omni's own CPU (cores), mean | 0 | 0.00883 |
| CPU used with Omni's own (cores), mean | 2.438 | 2.401 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.2 | 319.4 |
| HPA replicas, mean | 9.568 | 9.556 |
| pods started | 4.7 | 4.7 |
| pod start wait, total (s) | 17.7 | 16.2 |
| pod start wait, mean (s) | 3.423 | 2.583 |
| host CPU busy, the real machine under kind (%) | 68.56 | 67.68 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.566e-16 to +7.895e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.515 | 4.517 | +0.0% | -0.003939 to +0.008273 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516.9 | 515.9 | -0.2% | -1.814 to -0.1673 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.9 | 515.9 | -0.2% | -1.814 to -0.1673 | yes: GAIN |
| response time (ms), mean | 262.4 | 146.3 | -44.3% | -155.1 to -77.12 | yes: GAIN |
| response time (ms), 95th percentile | 663.8 | 279.5 | -57.9% | -492 to -276.5 | yes: GAIN |
| response time (ms), 99th percentile | 2171 | 1257 | -42.1% | -1345 to -483.1 | yes: GAIN |
| time over the response line (% of samples) | 18.98 | 12.39 | -34.7% | -9.339 to -3.829 | yes: GAIN |
| failed requests (%) | 11.99 | 10.43 | -12.9% | -2.34 to -0.7632 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.4 | 21.7 | -20.8% | -6.821 to -4.579 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.3 | +37.3 (native is 0) | +28.38 to +46.22 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4267 | 0.51 | +19.5% | -0.3059 to +0.4726 | no |
| utilisation (used / allocatable) | 0.1016 | 0.09966 | -1.9% | -0.002852 to -0.0009854 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.438 | 2.392 | -1.9% | -0.06844 to -0.02365 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00883 | +0.00883 (native is 0) | +0.007416 to +0.01024 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.438 | 2.401 | -1.5% | -0.05857 to -0.01586 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.2 | 319.4 | +1.3% | +0.1615 to +8.224 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.568 | 9.556 | -0.1% | -0.3949 to +0.3715 | no |
| pods started | 4.7 | 4.7 | +0.0% | -2.079 to +2.079 | no |
| pod start wait, total (s) | 17.7 | 16.2 | -8.5% | -10.33 to +7.327 | no |
| pod start wait, mean (s) | 3.423 | 2.583 | -24.5% | -1.841 to +0.1608 | no |
| host CPU busy, the real machine under kind (%) | 68.56 | 67.68 | -1.3% | -1.641 to -0.1227 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*