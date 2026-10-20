# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 523.7 | 437.6 |
| response time (ms), 95th percentile | 2236 | 2103 |
| response time (ms), 99th percentile | 5777 | 4759 |
| time over the response line (% of samples) | 23.98 | 21.7 |
| failed requests (%) | 3.002 | 3.06 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.033 | 0.9 |
| utilisation (used / allocatable) | 0.09638 | 0.09572 |
| CPU used (cores), mean | 2.313 | 2.297 |
| Omni's own CPU (cores), mean | 0 | 0.01124 |
| CPU used with Omni's own (cores), mean | 2.313 | 2.308 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.2 | 302.5 |
| HPA replicas, mean | 15.05 | 15.2 |
| pods started | 5.3 | 4.4 |
| pod start wait, total (s) | 8.8 | 7.5 |
| pod start wait, mean (s) | 1.655 | 1.653 |
| host CPU busy, the real machine under kind (%) | 66.7 | 66.81 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 293.2 | 261.5 |
| second app: response time (ms), 99th percentile | 2032 | 1906 |
| second app: time over the response line (% of samples) | 14.35 | 14.37 |
| second app: failed requests (%) | 12.19 | 12.45 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.363e-16 to +8.692e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.516 | -0.1% | -0.006718 to +0.004051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.3 | -0.2% | -0.8273 to +0.1309 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.3 | -0.2% | -0.8273 to +0.1309 | no |
| response time (ms), mean | 523.7 | 437.6 | -16.5% | -145.4 to -26.9 | yes: GAIN |
| response time (ms), 95th percentile | 2236 | 2103 | -5.9% | -564.3 to +298.3 | no |
| response time (ms), 99th percentile | 5777 | 4759 | -17.6% | -1803 to -232.9 | yes: GAIN |
| time over the response line (% of samples) | 23.98 | 21.7 | -9.5% | -4.573 to -0.0004328 | yes: GAIN |
| failed requests (%) | 3.002 | 3.06 | +2.0% | -0.6341 to +0.7513 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.4 | -3.4% | -1.195 to +0.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.3 (native is 0) | +32.68 to +35.92 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.033 | 0.9 | -12.9% | -0.9668 to +0.7001 | no |
| utilisation (used / allocatable) | 0.09638 | 0.09572 | -0.7% | -0.001756 to +0.0004204 | no |
| CPU used (cores), mean | 2.313 | 2.297 | -0.7% | -0.04215 to +0.01009 | no |
| Omni's own CPU (cores), mean | 0 | 0.01124 | +0.0112 (native is 0) | +0.01016 to +0.01232 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.313 | 2.308 | -0.2% | -0.03082 to +0.02124 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.2 | 302.5 | +0.4% | -2.74 to +5.307 | no |
| HPA replicas, mean | 15.05 | 15.2 | +1.0% | -0.161 to +0.4478 | no |
| pods started | 5.3 | 4.4 | -17.0% | -2.137 to +0.3367 | no |
| pod start wait, total (s) | 8.8 | 7.5 | -14.8% | -3.977 to +1.377 | no |
| pod start wait, mean (s) | 1.655 | 1.653 | -0.1% | -0.2998 to +0.2965 | no |
| host CPU busy, the real machine under kind (%) | 66.7 | 66.81 | +0.2% | -0.8542 to +1.068 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 293.2 | 261.5 | -10.8% | -151.1 to +87.68 | no |
| second app: response time (ms), 99th percentile | 2032 | 1906 | -6.2% | -922.8 to +670.7 | no |
| second app: time over the response line (% of samples) | 14.35 | 14.37 | +0.2% | -1.165 to +1.214 | no |
| second app: failed requests (%) | 12.19 | 12.45 | +2.2% | -0.2886 to +0.8153 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*