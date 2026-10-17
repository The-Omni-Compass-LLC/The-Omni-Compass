# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 162 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 145.5 | 89.42 |
| response time (ms), 95th percentile | 302.2 | 140.9 |
| response time (ms), 99th percentile | 442.4 | 176.2 |
| time over the response line (% of samples) | 0.6959 | 0.0122 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2417 | 0.08 |
| utilisation (used / allocatable) | 0.03745 | 0.04996 |
| CPU used (cores), mean | 0.8989 | 1.199 |
| Omni's own CPU (cores), mean | 0 | 0.0131 |
| CPU used with Omni's own (cores), mean | 0.8989 | 1.212 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701 | 540.2 |
| HPA replicas, mean | 8.865 | 9.132 |
| pods started | 4.9 | 4.5 |
| pod start wait, total (s) | 12.5 | 11 |
| pod start wait, mean (s) | 2.435 | 2.312 |
| host CPU busy, the real machine under kind (%) | 27.82 | 36.68 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.087e-17 to +1.147e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.1% | -0.008151 to +0.01082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 162 | +1.9% | +2.099 to +3.868 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 162 | +1.9% | +2.099 to +3.868 | yes: power given |
| response time (ms), mean | 145.5 | 89.42 | -38.5% | -69.41 to -42.7 | yes: GAIN |
| response time (ms), 95th percentile | 302.2 | 140.9 | -53.4% | -191.2 to -131.3 | yes: GAIN |
| response time (ms), 99th percentile | 442.4 | 176.2 | -60.2% | -305.6 to -226.8 | yes: GAIN |
| time over the response line (% of samples) | 0.6959 | 0.0122 | -98.2% | -0.986 to -0.3815 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 | -100.0% | -0.9694 to -0.2306 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.3 | +17.3 (native is 0) | +16.4 to +18.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2417 | 0.08 | -66.9% | -0.3452 to +0.02183 | no |
| utilisation (used / allocatable) | 0.03745 | 0.04996 | +33.4% | +0.009461 to +0.01556 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8989 | 1.199 | +33.4% | +0.2271 to +0.3734 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0131 | +0.0131 (native is 0) | +0.01187 to +0.01433 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8989 | 1.212 | +34.9% | +0.2391 to +0.3876 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701 | 540.2 | -22.9% | -191 to -130.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.865 | 9.132 | +3.0% | +0.1157 to +0.4183 | yes: power given |
| pods started | 4.9 | 4.5 | -8.2% | -1.091 to +0.2911 | no |
| pod start wait, total (s) | 12.5 | 11 | -12.0% | -8.015 to +5.015 | no |
| pod start wait, mean (s) | 2.435 | 2.312 | -5.1% | -1.134 to +0.887 | no |
| host CPU busy, the real machine under kind (%) | 27.82 | 36.68 | +31.9% | +6.808 to +10.93 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*