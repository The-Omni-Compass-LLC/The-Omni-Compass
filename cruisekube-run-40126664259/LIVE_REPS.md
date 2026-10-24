# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.977 | 6 |
| node-hours | 1.503 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.6 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 71.29 | 72.28 |
| response time (ms), 95th percentile | 111 | 112.6 |
| response time (ms), 99th percentile | 123 | 127.4 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0 |
| utilisation (used / allocatable) | 0.04534 | 0.04559 |
| CPU used (cores), mean | 1.083 | 1.094 |
| Omni's own CPU (cores), mean | 0 | 0.00869 |
| CPU used with Omni's own (cores), mean | 1.083 | 1.103 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 599.8 | 592.9 |
| HPA replicas, mean | 2.606 | 2.766 |
| pods started | 1.5 | 1.2 |
| pod start wait, total (s) | 2.4 | 1.6 |
| pod start wait, mean (s) | 1.5 | 1.15 |
| host CPU busy, the real machine under kind (%) | 33.41 | 34.29 |
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

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.977 | 6 | +0.4% | −0.0246 to +0.0704 | no |
| node-hours | 1.503 | 1.516 | +0.8% | +0.0038 to +0.0214 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 160.6 | 161 | +0.2% | −1.1147 to +1.8797 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 161 | +0.5% | +0.0910 to +1.5407 | yes: power given |
| response time (ms), mean | 71.29 | 72.28 | +1.4% | −0.1073 to +2.0873 | no |
| response time (ms), 95th percentile | 111 | 112.6 | +1.4% | −0.0191 to +3.0961 | no |
| response time (ms), 99th percentile | 123 | 127.4 | +3.6% | +0.9521 to +7.8617 | yes: LOSS |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0 | −100.0% | −0.1296 to +0.0263 | no |
| utilisation (used / allocatable) | 0.04534 | 0.04559 | +0.6% | −0.0004 to +0.0009 | no |
| CPU used (cores), mean | 1.083 | 1.094 | +1.0% | −0.0007 to +0.0229 | no |
| Omni's own CPU (cores), mean | 0 | 0.00869 | +0.009 (native is 0) | +0.0073 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.083 | 1.103 | +1.8% | +0.0084 to +0.0311 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 599.8 | 592.9 | −1.1% | −13.4597 to −0.2379 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.606 | 2.766 | +6.1% | −0.0605 to +0.3798 | no |
| pods started | 1.5 | 1.2 | −20.0% | −0.8889 to +0.2889 | no |
| pod start wait, total (s) | 2.4 | 1.6 | −33.3% | −2.3379 to +0.7379 | no |
| pod start wait, mean (s) | 1.5 | 1.15 | −23.3% | −1.0041 to +0.3041 | no |
| host CPU busy, the real machine under kind (%) | 33.41 | 34.29 | +2.6% | +0.3448 to +1.4133 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*