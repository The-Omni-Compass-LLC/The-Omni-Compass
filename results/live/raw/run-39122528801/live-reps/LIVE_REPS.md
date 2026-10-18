# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.3 | 172.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.3 | 172.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 526.3 | 452.6 |
| response time (ms), 95th percentile | 2303 | 2226 |
| response time (ms), 99th percentile | 5560 | 4905 |
| time over the response line (% of samples) | 23.87 | 21.26 |
| failed requests (%) | 3.509 | 3.537 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.332 | 1.228 |
| utilisation (used / allocatable) | 0.09704 | 0.09562 |
| CPU used (cores), mean | 2.329 | 2.295 |
| Omni's own CPU (cores), mean | 0 | 0.01069 |
| CPU used with Omni's own (cores), mean | 2.329 | 2.306 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.7 | 308.3 |
| HPA replicas, mean | 15.04 | 15.19 |
| pods started | 4.9 | 3.6 |
| pod start wait, total (s) | 12.2 | 9.4 |
| pod start wait, mean (s) | 2.177 | 2.239 |
| host CPU busy, the real machine under kind (%) | 67.54 | 67.18 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 274 | 253.9 |
| second app: response time (ms), 99th percentile | 1789 | 1041 |
| second app: time over the response line (% of samples) | 14.6 | 14.17 |
| second app: failed requests (%) | 12.73 | 12.84 |

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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.147e-15 to +8.087e-17 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.517 | +0.2% | -0.0001763 to +0.006843 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.3 | 172.4 | +0.1% | -0.487 to +0.6918 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.3 | 172.4 | +0.1% | -0.487 to +0.6918 | no |
| response time (ms), mean | 526.3 | 452.6 | -14.0% | -115.1 to -32.28 | yes: GAIN |
| response time (ms), 95th percentile | 2303 | 2226 | -3.3% | -431.4 to +278.4 | no |
| response time (ms), 99th percentile | 5560 | 4905 | -11.8% | -1509 to +200.2 | no |
| time over the response line (% of samples) | 23.87 | 21.26 | -11.0% | -4.442 to -0.7968 | yes: GAIN |
| failed requests (%) | 3.509 | 3.537 | +0.8% | -0.5272 to +0.584 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8 | -7.0% | -1.1 to -0.09985 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.1 | +33.1 (native is 0) | +31.3 to +34.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.332 | 1.228 | -7.8% | -1.103 to +0.8965 | no |
| utilisation (used / allocatable) | 0.09704 | 0.09562 | -1.5% | -0.002751 to -7.686e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.329 | 2.295 | -1.5% | -0.06603 to -0.001845 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01069 | +0.0107 (native is 0) | +0.009419 to +0.01196 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.329 | 2.306 | -1.0% | -0.05553 to +0.00903 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.7 | 308.3 | +1.8% | -0.8672 to +11.97 | no |
| HPA replicas, mean | 15.04 | 15.19 | +1.0% | -0.1778 to +0.4665 | no |
| pods started | 4.9 | 3.6 | -26.5% | -2.369 to -0.231 | yes: GAIN |
| pod start wait, total (s) | 12.2 | 9.4 | -23.0% | -6.066 to +0.4658 | no |
| pod start wait, mean (s) | 2.177 | 2.239 | +2.8% | -0.5577 to +0.6815 | no |
| host CPU busy, the real machine under kind (%) | 67.54 | 67.18 | -0.5% | -1.039 to +0.3176 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 274 | 253.9 | -7.3% | -53.53 to +13.27 | no |
| second app: response time (ms), 99th percentile | 1789 | 1041 | -41.8% | -1819 to +323.3 | no |
| second app: time over the response line (% of samples) | 14.6 | 14.17 | -2.9% | -0.8323 to -0.02461 | yes: GAIN |
| second app: failed requests (%) | 12.73 | 12.84 | +0.8% | -0.3437 to +0.5601 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*