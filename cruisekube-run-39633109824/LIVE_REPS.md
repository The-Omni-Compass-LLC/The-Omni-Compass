# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.2 | 160.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.2 | 160.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 70.75 | 70.58 |
| response time (ms), 95th percentile | 103.5 | 104 |
| response time (ms), 99th percentile | 117.8 | 121.6 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.135 |
| utilisation (used / allocatable) | 0.04539 | 0.04479 |
| CPU used (cores), mean | 1.089 | 1.075 |
| Omni's own CPU (cores), mean | 0 | 0.00842 |
| CPU used with Omni's own (cores), mean | 1.089 | 1.083 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 596.5 | 603.6 |
| HPA replicas, mean | 2.757 | 2.776 |
| pods started | 1.6 | 1.7 |
| pod start wait, total (s) | 2 | 2.4 |
| pod start wait, mean (s) | 1.167 | 1.35 |
| host CPU busy, the real machine under kind (%) | 34.52 | 34.45 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.531e-16 to +1.264e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.511 | -0.4% | -0.01611 to +0.003111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.2 | 160.4 | -0.5% | -1.818 to +0.222 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.2 | 160.4 | -0.5% | -1.818 to +0.222 | no |
| response time (ms), mean | 70.75 | 70.58 | -0.3% | -1.206 to +0.8512 | no |
| response time (ms), 95th percentile | 103.5 | 104 | +0.5% | -1.893 to +2.934 | no |
| response time (ms), 99th percentile | 117.8 | 121.6 | +3.3% | -3.161 to +10.9 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.135 | +65.3% | -0.07155 to +0.1782 | no |
| utilisation (used / allocatable) | 0.04539 | 0.04479 | -1.3% | -0.001234 to +3.604e-05 | no |
| CPU used (cores), mean | 1.089 | 1.075 | -1.3% | -0.02961 to +0.0008649 | no |
| Omni's own CPU (cores), mean | 0 | 0.00842 | +0.00842 (native is 0) | +0.007217 to +0.009623 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.089 | 1.083 | -0.5% | -0.02081 to +0.008902 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 596.5 | 603.6 | +1.2% | +0.5594 to +13.6 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.757 | 2.776 | +0.7% | -0.1145 to +0.1533 | no |
| pods started | 1.6 | 1.7 | +6.3% | -0.5263 to +0.7263 | no |
| pod start wait, total (s) | 2 | 2.4 | +20.0% | -0.5656 to +1.366 | no |
| pod start wait, mean (s) | 1.167 | 1.35 | +15.7% | -0.2038 to +0.5705 | no |
| host CPU busy, the real machine under kind (%) | 34.52 | 34.45 | -0.2% | -0.5386 to +0.3936 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*