# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 154.8 | 83.47 |
| response time (ms), 95th percentile | 325.2 | 129.6 |
| response time (ms), 99th percentile | 471.2 | 163.7 |
| time over the response line (% of samples) | 1.169 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.02667 |
| utilisation (used / allocatable) | 0.03348 | 0.04852 |
| CPU used (cores), mean | 0.8035 | 1.164 |
| Omni's own CPU (cores), mean | 0 | 0.00832 |
| CPU used with Omni's own (cores), mean | 0.8035 | 1.173 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 781.6 | 558.8 |
| HPA replicas, mean | 9.769 | 9.88 |
| pods started | 2.2 | 1 |
| pod start wait, total (s) | 3.3 | 1.8 |
| pod start wait, mean (s) | 1.358 | 1.1 |
| host CPU busy, the real machine under kind (%) | 24.29 | 34.23 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.094e-16 to +1.212e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.512 | -0.4% | -0.01374 to +0.003074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.1 | +1.8% | +2.205 to +3.586 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.1 | +1.8% | +2.205 to +3.586 | yes: power given |
| response time (ms), mean | 154.8 | 83.47 | -46.1% | -91.26 to -51.34 | yes: GAIN |
| response time (ms), 95th percentile | 325.2 | 129.6 | -60.1% | -236.5 to -154.7 | yes: GAIN |
| response time (ms), 99th percentile | 471.2 | 163.7 | -65.3% | -355.6 to -259.4 | yes: GAIN |
| time over the response line (% of samples) | 1.169 | 0 | -100.0% | -1.897 to -0.4417 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | -100.0% | -1.754 to -0.246 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16 (native is 0) | +13.89 to +18.11 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.02667 | +0.0267 (native is 0) | -0.03365 to +0.08699 | no |
| utilisation (used / allocatable) | 0.03348 | 0.04852 | +44.9% | +0.01148 to +0.0186 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8035 | 1.164 | +44.9% | +0.2755 to +0.4465 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00832 | +0.00832 (native is 0) | +0.007486 to +0.009154 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8035 | 1.173 | +46.0% | +0.283 to +0.4556 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 781.6 | 558.8 | -28.5% | -258.2 to -187.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.769 | 9.88 | +1.1% | -0.02757 to +0.2489 | no |
| pods started | 2.2 | 1 | -54.5% | -2.308 to -0.09185 | yes: GAIN |
| pod start wait, total (s) | 3.3 | 1.8 | -45.5% | -3.385 to +0.385 | no |
| pod start wait, mean (s) | 1.358 | 1.1 | -19.0% | -1.021 to +0.5042 | no |
| host CPU busy, the real machine under kind (%) | 24.29 | 34.23 | +40.9% | +7.758 to +12.12 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*