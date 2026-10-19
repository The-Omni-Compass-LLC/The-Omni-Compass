# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 172 | 172.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172 | 172.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 492.3 | 391.3 |
| response time (ms), 95th percentile | 2106 | 1750 |
| response time (ms), 99th percentile | 5111 | 4994 |
| time over the response line (% of samples) | 22.06 | 18.87 |
| failed requests (%) | 3.521 | 3.964 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.415 | 1.513 |
| utilisation (used / allocatable) | 0.09461 | 0.09323 |
| CPU used (cores), mean | 2.271 | 2.237 |
| Omni's own CPU (cores), mean | 0 | 0.01061 |
| CPU used with Omni's own (cores), mean | 2.271 | 2.248 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.4 | 318.3 |
| HPA replicas, mean | 15.15 | 15.11 |
| pods started | 4.2 | 3.8 |
| pod start wait, total (s) | 11 | 10.9 |
| pod start wait, mean (s) | 2.23 | 2.49 |
| host CPU busy, the real machine under kind (%) | 65.86 | 65.39 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 273.2 | 286.5 |
| second app: response time (ms), 99th percentile | 1376 | 1053 |
| second app: time over the response line (% of samples) | 13.4 | 13.33 |
| second app: failed requests (%) | 11.86 | 11.77 |

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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.224e-15 to -1.901e-17 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.519 | +0.2% | -0.0001692 to +0.006169 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172 | 172.1 | +0.0% | -0.5435 to +0.6683 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172 | 172.1 | +0.0% | -0.5435 to +0.6683 | no |
| response time (ms), mean | 492.3 | 391.3 | -20.5% | -161.4 to -40.49 | yes: GAIN |
| response time (ms), 95th percentile | 2106 | 1750 | -16.9% | -749.6 to +37.46 | no |
| response time (ms), 99th percentile | 5111 | 4994 | -2.3% | -902.4 to +668.8 | no |
| time over the response line (% of samples) | 22.06 | 18.87 | -14.5% | -4.814 to -1.574 | yes: GAIN |
| failed requests (%) | 3.521 | 3.964 | +12.6% | -0.6058 to +1.493 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.5 | -3.8% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 | +32.3 (native is 0) | +29.84 to +34.76 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.415 | 1.513 | +6.9% | -0.9067 to +1.103 | no |
| utilisation (used / allocatable) | 0.09461 | 0.09323 | -1.5% | -0.002661 to -9.607e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.271 | 2.237 | -1.5% | -0.06386 to -0.002306 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01061 | +0.0106 (native is 0) | +0.008996 to +0.01222 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.271 | 2.248 | -1.0% | -0.05413 to +0.009184 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.4 | 318.3 | +1.9% | -1.21 to +13 | no |
| HPA replicas, mean | 15.15 | 15.11 | -0.3% | -0.3126 to +0.2355 | no |
| pods started | 4.2 | 3.8 | -9.5% | -1.24 to +0.4396 | no |
| pod start wait, total (s) | 11 | 10.9 | -0.9% | -5.174 to +4.974 | no |
| pod start wait, mean (s) | 2.23 | 2.49 | +11.7% | -0.5443 to +1.065 | no |
| host CPU busy, the real machine under kind (%) | 65.86 | 65.39 | -0.7% | -1.179 to +0.2233 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 273.2 | 286.5 | +4.9% | -11.98 to +38.53 | no |
| second app: response time (ms), 99th percentile | 1376 | 1053 | -23.5% | -1221 to +575.2 | no |
| second app: time over the response line (% of samples) | 13.4 | 13.33 | -0.6% | -0.6297 to +0.4785 | no |
| second app: failed requests (%) | 11.86 | 11.77 | -0.8% | -0.5489 to +0.3587 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*