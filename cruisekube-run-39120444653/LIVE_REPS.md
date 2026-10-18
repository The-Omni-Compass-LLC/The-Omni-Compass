# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.6 | 162.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.6 | 162.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 86.22 | 86.11 |
| response time (ms), 95th percentile | 133.4 | 131.7 |
| response time (ms), 99th percentile | 154.4 | 155.8 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.1222 |
| utilisation (used / allocatable) | 0.05011 | 0.04979 |
| CPU used (cores), mean | 1.203 | 1.195 |
| Omni's own CPU (cores), mean | 0 | 0.009511 |
| CPU used with Omni's own (cores), mean | 1.203 | 1.204 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 536.9 | 540.2 |
| HPA replicas, mean | 2.837 | 2.891 |
| pods started | 1.6 | 1.111 |
| pod start wait, total (s) | 6.2 | 5 |
| pod start wait, mean (s) | 3.6 | 2.833 |
| host CPU busy, the real machine under kind (%) | 37.26 | 37.43 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

Omni-Compass stayed native in 9 of 9 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.037e-16 to +4.984e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.519 | +0.4% | -0.002123 to +0.01472 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.5 | 162.2 | +0.4% | -0.1706 to +1.533 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 162.2 | +0.4% | -0.1706 to +1.533 | no |
| response time (ms), mean | 84.81 | 86.11 | +1.5% | +0.2815 to +2.313 | yes: LOSS |
| response time (ms), 95th percentile | 130.9 | 131.7 | +0.7% | -1.628 to +3.363 | no |
| response time (ms), 99th percentile | 151.1 | 155.8 | +3.1% | +0.2916 to +8.983 | yes: LOSS |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1796 | 0.1222 | -32.0% | -0.3259 to +0.2111 | no |
| utilisation (used / allocatable) | 0.04986 | 0.04979 | -0.2% | -0.0008604 to +0.0007091 | no |
| CPU used (cores), mean | 1.197 | 1.195 | -0.2% | -0.02065 to +0.01702 | no |
| Omni's own CPU (cores), mean | 0 | 0.009511 | +0.00951 (native is 0) | +0.00876 to +0.01026 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.197 | 1.204 | +0.6% | -0.01127 to +0.02666 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 539.6 | 540.2 | +0.1% | -7.279 to +8.447 | no |
| HPA replicas, mean | 2.85 | 2.891 | +1.4% | -0.156 to +0.238 | no |
| pods started | 1.667 | 1.111 | -33.3% | -1.506 to +0.3945 | no |
| pod start wait, total (s) | 6.778 | 5 | -26.2% | -8.52 to +4.965 | no |
| pod start wait, mean (s) | 3.889 | 2.833 | -27.1% | -4.105 to +1.994 | no |
| host CPU busy, the real machine under kind (%) | 37.07 | 37.43 | +1.0% | -0.1263 to +0.8564 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*