# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.7 | 161.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 85.3 | 86.05 |
| response time (ms), 95th percentile | 131.4 | 132 |
| response time (ms), 99th percentile | 148.9 | 150.7 |
| time over the response line (% of samples) | 0 | 0.01227 |
| failed requests (%) | 0 | 0.01227 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05333 |
| utilisation (used / allocatable) | 0.04956 | 0.04994 |
| CPU used (cores), mean | 1.189 | 1.199 |
| Omni's own CPU (cores), mean | 0 | 0.00976 |
| CPU used with Omni's own (cores), mean | 1.189 | 1.208 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 541.4 | 537.1 |
| HPA replicas, mean | 2.852 | 2.831 |
| pods started | 1.2 | 1.6 |
| pod start wait, total (s) | 1.9 | 2.6 |
| pod start wait, mean (s) | 1.45 | 1.417 |
| host CPU busy, the real machine under kind (%) | 36.67 | 37.38 |
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

Omni-Compass stayed native in 9 of 10 repetitions (repetitions 1, 2, 3, 4, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0108 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.6 | −0.0% | −1.0876 to +0.9368 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.7 | 161.6 | −0.0% | −1.0876 to +0.9368 | no |
| response time (ms), mean | 85.3 | 86.05 | +0.9% | +0.0372 to +1.4544 | yes: LOSS |
| response time (ms), 95th percentile | 131.4 | 132 | +0.5% | −0.7855 to +2.0565 | no |
| response time (ms), 99th percentile | 148.9 | 150.7 | +1.2% | −2.9935 to +6.4741 | no |
| time over the response line (% of samples) | 0 | 0.01227 | +0.012 (native is 0) | −0.0155 to +0.0400 | no |
| failed requests (%) | 0 | 0.01227 | +0.012 (native is 0) | −0.0155 to +0.0400 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05333 | +100.0% | −0.0816 to +0.1349 | no |
| utilisation (used / allocatable) | 0.04956 | 0.04994 | +0.8% | −0.0005 to +0.0013 | no |
| CPU used (cores), mean | 1.189 | 1.199 | +0.8% | −0.0128 to +0.0309 | no |
| Omni's own CPU (cores), mean | 0 | 0.00976 | +0.010 (native is 0) | +0.0090 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.189 | 1.208 | +1.6% | −0.0032 to +0.0408 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 541.4 | 537.1 | −0.8% | −14.5461 to +5.9437 | no |
| HPA replicas, mean | 2.852 | 2.831 | −0.7% | −0.3096 to +0.2683 | no |
| pods started | 1.2 | 1.6 | +33.3% | −0.6228 to +1.4228 | no |
| pod start wait, total (s) | 1.9 | 2.6 | +36.8% | −1.2385 to +2.6385 | no |
| pod start wait, mean (s) | 1.45 | 1.417 | −2.3% | −0.7635 to +0.6968 | no |
| host CPU busy, the real machine under kind (%) | 36.67 | 37.38 | +1.9% | +0.2315 to +1.1963 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*