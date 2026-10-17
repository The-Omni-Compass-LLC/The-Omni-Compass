# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.993 | 6 |
| node-hours | 1.51 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 161 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.9 | 161.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 75.87 | 77.02 |
| response time (ms), 95th percentile | 113.3 | 114.3 |
| response time (ms), 99th percentile | 130.1 | 128.9 |
| time over the response line (% of samples) | 0 | 0.01235 |
| failed requests (%) | 0 | 0.01235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.11 | 0.05333 |
| utilisation (used / allocatable) | 0.0471 | 0.04725 |
| CPU used (cores), mean | 1.129 | 1.134 |
| Omni's own CPU (cores), mean | 0 | 0.00835 |
| CPU used with Omni's own (cores), mean | 1.129 | 1.142 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 573.2 | 573.6 |
| HPA replicas, mean | 2.755 | 2.615 |
| pods started | 1.4 | 1.2 |
| pod start wait, total (s) | 4.4 | 2.8 |
| pod start wait, mean (s) | 2.65 | 1.6 |
| host CPU busy, the real machine under kind (%) | 35.05 | 35.28 |
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
| worker nodes in service, mean | 5.993 | 6 | +0.1% | -0.008655 to +0.02237 | no |
| node-hours | 1.51 | 1.514 | +0.3% | -0.006745 to +0.01519 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161 | 161.2 | +0.1% | -0.7065 to +1.082 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.9 | 161.2 | +0.2% | -0.6327 to +1.266 | no |
| response time (ms), mean | 75.87 | 77.02 | +1.5% | -0.4973 to +2.784 | no |
| response time (ms), 95th percentile | 113.3 | 114.3 | +0.9% | -1.119 to +3.062 | no |
| response time (ms), 99th percentile | 130.1 | 128.9 | -0.9% | -9.499 to +7.123 | no |
| time over the response line (% of samples) | 0 | 0.01235 | +0.0123 (native is 0) | -0.01558 to +0.04027 | no |
| failed requests (%) | 0 | 0.01235 | +0.0123 (native is 0) | -0.01558 to +0.04027 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.11 | 0.05333 | -51.5% | -0.2774 to +0.1641 | no |
| utilisation (used / allocatable) | 0.0471 | 0.04725 | +0.3% | -0.0008541 to +0.001149 | no |
| CPU used (cores), mean | 1.129 | 1.134 | +0.4% | -0.01916 to +0.02846 | no |
| Omni's own CPU (cores), mean | 0 | 0.00835 | +0.00835 (native is 0) | +0.007138 to +0.009562 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.129 | 1.142 | +1.2% | -0.01153 to +0.03753 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 573.2 | 573.6 | +0.1% | -11.62 to +12.41 | no |
| HPA replicas, mean | 2.755 | 2.615 | -5.1% | -0.3795 to +0.09861 | no |
| pods started | 1.4 | 1.2 | -14.3% | -0.8573 to +0.4573 | no |
| pod start wait, total (s) | 4.4 | 2.8 | -36.4% | -7.462 to +4.262 | no |
| pod start wait, mean (s) | 2.65 | 1.6 | -39.6% | -3.245 to +1.145 | no |
| host CPU busy, the real machine under kind (%) | 35.05 | 35.28 | +0.7% | -0.4581 to +0.9233 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*