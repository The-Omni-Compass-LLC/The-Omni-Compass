# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 162.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 162.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 157.5 | 95.9 |
| response time (ms), 95th percentile | 310.3 | 152.3 |
| response time (ms), 99th percentile | 443.5 | 188.9 |
| time over the response line (% of samples) | 0.5137 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.4433 |
| utilisation (used / allocatable) | 0.0379 | 0.05164 |
| CPU used (cores), mean | 0.9095 | 1.239 |
| Omni's own CPU (cores), mean | 0 | 0.01346 |
| CPU used with Omni's own (cores), mean | 0.9095 | 1.253 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.7 | 518.5 |
| HPA replicas, mean | 8.991 | 9.252 |
| pods started | 4.5 | 4.5 |
| pod start wait, total (s) | 12.9 | 9.7 |
| pod start wait, mean (s) | 2.465 | 2.07 |
| host CPU busy, the real machine under kind (%) | 28.15 | 37.83 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.108e-17 to +1.735e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.518 | +0.2% | -0.007113 to +0.01311 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 162.5 | +2.2% | +2.192 to +4.664 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 162.5 | +2.2% | +2.192 to +4.664 | yes: power given |
| response time (ms), mean | 157.5 | 95.9 | -39.1% | -65.03 to -58.14 | yes: GAIN |
| response time (ms), 95th percentile | 310.3 | 152.3 | -50.9% | -166.7 to -149.5 | yes: GAIN |
| response time (ms), 99th percentile | 443.5 | 188.9 | -57.4% | -281.9 to -227.3 | yes: GAIN |
| time over the response line (% of samples) | 0.5137 | 0 | -100.0% | -0.7359 to -0.2914 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.1 (native is 0) | +16.87 to +17.33 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.4433 | +51.1% | -0.1202 to +0.4202 | no |
| utilisation (used / allocatable) | 0.0379 | 0.05164 | +36.3% | +0.0129 to +0.01459 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9095 | 1.239 | +36.3% | +0.3096 to +0.3502 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01346 | +0.0135 (native is 0) | +0.0128 to +0.01412 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9095 | 1.253 | +37.7% | +0.3226 to +0.3641 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 692.7 | 518.5 | -25.1% | -181.8 to -166.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.991 | 9.252 | +2.9% | -0.02632 to +0.549 | no |
| pods started | 4.5 | 4.5 | +0.0% | -1.216 to +1.216 | no |
| pod start wait, total (s) | 12.9 | 9.7 | -24.8% | -9.993 to +3.593 | no |
| pod start wait, mean (s) | 2.465 | 2.07 | -16.0% | -1.514 to +0.7236 | no |
| host CPU busy, the real machine under kind (%) | 28.15 | 37.83 | +34.4% | +9.167 to +10.2 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*