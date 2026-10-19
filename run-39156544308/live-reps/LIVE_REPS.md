# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.7 | 172.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.7 | 172.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 517.7 | 410.6 |
| response time (ms), 95th percentile | 2220 | 1817 |
| response time (ms), 99th percentile | 5509 | 4997 |
| time over the response line (% of samples) | 23.96 | 20.63 |
| failed requests (%) | 3.994 | 4.332 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.027 | 1.08 |
| utilisation (used / allocatable) | 0.09716 | 0.09701 |
| CPU used (cores), mean | 2.332 | 2.328 |
| Omni's own CPU (cores), mean | 0 | 0.01081 |
| CPU used with Omni's own (cores), mean | 2.332 | 2.339 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.5 | 300.4 |
| HPA replicas, mean | 15.24 | 15.47 |
| pods started | 4.3 | 3.3 |
| pod start wait, total (s) | 10.9 | 7.4 |
| pod start wait, mean (s) | 2.244 | 2.152 |
| host CPU busy, the real machine under kind (%) | 68.02 | 67.78 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 290.3 | 305.2 |
| second app: response time (ms), 99th percentile | 2386 | 1477 |
| second app: time over the response line (% of samples) | 14.75 | 14.95 |
| second app: failed requests (%) | 12.8 | 12.96 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.516 | 1.518 | +0.1% | -0.0009456 to +0.004612 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.7 | 172.8 | +0.1% | -0.2174 to +0.5492 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.7 | 172.8 | +0.1% | -0.2174 to +0.5492 | no |
| response time (ms), mean | 517.7 | 410.6 | -20.7% | -171.4 to -42.79 | yes: GAIN |
| response time (ms), 95th percentile | 2220 | 1817 | -18.2% | -736.5 to -69.98 | yes: GAIN |
| response time (ms), 99th percentile | 5509 | 4997 | -9.3% | -1547 to +522.2 | no |
| time over the response line (% of samples) | 23.96 | 20.63 | -13.9% | -5.507 to -1.139 | yes: GAIN |
| failed requests (%) | 3.994 | 4.332 | +8.4% | -0.4922 to +1.167 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 8.1 | -9.0% | -1.364 to -0.2358 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 | +33.3 (native is 0) | +31.36 to +35.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.027 | 1.08 | +5.2% | -0.617 to +0.7237 | no |
| utilisation (used / allocatable) | 0.09716 | 0.09701 | -0.2% | -0.00153 to +0.001227 | no |
| CPU used (cores), mean | 2.332 | 2.328 | -0.2% | -0.03673 to +0.02946 | no |
| Omni's own CPU (cores), mean | 0 | 0.01081 | +0.0108 (native is 0) | +0.009503 to +0.01212 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.339 | +0.3% | -0.02504 to +0.03939 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.5 | 300.4 | -0.4% | -6.701 to +4.439 | no |
| HPA replicas, mean | 15.24 | 15.47 | +1.5% | -0.06226 to +0.5276 | no |
| pods started | 4.3 | 3.3 | -23.3% | -1.954 to -0.04626 | yes: GAIN |
| pod start wait, total (s) | 10.9 | 7.4 | -32.1% | -10.8 to +3.797 | no |
| pod start wait, mean (s) | 2.244 | 2.152 | -4.1% | -1.199 to +1.015 | no |
| host CPU busy, the real machine under kind (%) | 68.02 | 67.78 | -0.3% | -0.8119 to +0.3456 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 290.3 | 305.2 | +5.1% | -12.01 to +41.69 | no |
| second app: response time (ms), 99th percentile | 2386 | 1477 | -38.1% | -3020 to +1200 | no |
| second app: time over the response line (% of samples) | 14.75 | 14.95 | +1.3% | -0.4137 to +0.8043 | no |
| second app: failed requests (%) | 12.8 | 12.96 | +1.2% | -0.5111 to +0.8273 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*