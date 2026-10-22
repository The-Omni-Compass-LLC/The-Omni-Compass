# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.9 | 173 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.9 | 173 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 565.5 | 511.6 |
| response time (ms), 95th percentile | 2569 | 2399 |
| response time (ms), 99th percentile | 6016 | 5547 |
| time over the response line (% of samples) | 24.54 | 24.4 |
| failed requests (%) | 3.896 | 3.309 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 70 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.765 | 0.5317 |
| utilisation (used / allocatable) | 0.09861 | 0.09746 |
| CPU used (cores), mean | 2.367 | 2.339 |
| Omni's own CPU (cores), mean | 0 | 0.03221 |
| CPU used with Omni's own (cores), mean | 2.367 | 2.371 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.1 | 302 |
| HPA replicas, mean | 14.94 | 15.77 |
| pods started | 5.4 | 5.3 |
| pod start wait, total (s) | 8.7 | 9.1 |
| pod start wait, mean (s) | 1.631 | 1.77 |
| host CPU busy, the real machine under kind (%) | 68.66 | 69.01 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 259.4 | 271.8 |
| second app: response time (ms), 99th percentile | 820.1 | 1449 |
| second app: time over the response line (% of samples) | 14.85 | 14.64 |
| second app: failed requests (%) | 13.5 | 13.5 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.519 | +0.2% | +0.0007579 to +0.005909 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 172.9 | 173 | +0.1% | -0.2607 to +0.5311 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.9 | 173 | +0.1% | -0.2607 to +0.5311 | no |
| response time (ms), mean | 565.5 | 511.6 | -9.5% | -121.4 to +13.71 | no |
| response time (ms), 95th percentile | 2569 | 2399 | -6.6% | -677 to +336.9 | no |
| response time (ms), 99th percentile | 6016 | 5547 | -7.8% | -1246 to +308.8 | no |
| time over the response line (% of samples) | 24.54 | 24.4 | -0.5% | -1.415 to +1.147 | no |
| failed requests (%) | 3.896 | 3.309 | -15.1% | -1.628 to +0.4551 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.3 | -5.7% | -1.108 to +0.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.8 | +44.8 (native is 0) | +37.17 to +52.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.765 | 0.5317 | -30.5% | -0.8031 to +0.3364 | no |
| utilisation (used / allocatable) | 0.09861 | 0.09746 | -1.2% | -0.001774 to -0.0005305 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.367 | 2.339 | -1.2% | -0.04258 to -0.01273 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03221 | +0.0322 (native is 0) | +0.02786 to +0.03656 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.367 | 2.371 | +0.2% | -0.009398 to +0.01851 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.1 | 302 | +1.0% | +0.6016 to +5.191 | yes, up (shown, not judged) |
| HPA replicas, mean | 14.94 | 15.77 | +5.6% | +0.3752 to +1.293 | yes: power given |
| pods started | 5.4 | 5.3 | -1.9% | -0.8872 to +0.6872 | no |
| pod start wait, total (s) | 8.7 | 9.1 | +4.6% | -2.731 to +3.531 | no |
| pod start wait, mean (s) | 1.631 | 1.77 | +8.5% | -0.3603 to +0.638 | no |
| host CPU busy, the real machine under kind (%) | 68.66 | 69.01 | +0.5% | -0.1853 to +0.8724 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 259.4 | 271.8 | +4.8% | -5.501 to +30.26 | no |
| second app: response time (ms), 99th percentile | 820.1 | 1449 | +76.7% | +27.6 to +1230 | yes: LOSS |
| second app: time over the response line (% of samples) | 14.85 | 14.64 | -1.4% | -0.6305 to +0.2145 | no |
| second app: failed requests (%) | 13.5 | 13.5 | +0.0% | -0.3087 to +0.3135 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*