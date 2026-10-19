# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.2 | 172.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.2 | 172.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 552.7 | 438.9 |
| response time (ms), 95th percentile | 2356 | 2005 |
| response time (ms), 99th percentile | 5639 | 5457 |
| time over the response line (% of samples) | 25.33 | 22.05 |
| failed requests (%) | 3.668 | 4.363 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.178 | 1.113 |
| utilisation (used / allocatable) | 0.09729 | 0.09747 |
| CPU used (cores), mean | 2.335 | 2.339 |
| Omni's own CPU (cores), mean | 0 | 0.01135 |
| CPU used with Omni's own (cores), mean | 2.335 | 2.351 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.5 | 301.6 |
| HPA replicas, mean | 14.92 | 15.38 |
| pods started | 5.5 | 3.6 |
| pod start wait, total (s) | 8.9 | 5.2 |
| pod start wait, mean (s) | 1.606 | 1.505 |
| host CPU busy, the real machine under kind (%) | 68.43 | 68.81 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 288.1 | 267.9 |
| second app: response time (ms), 99th percentile | 1015 | 944 |
| second app: time over the response line (% of samples) | 14.84 | 14.62 |
| second app: failed requests (%) | 13.26 | 13.42 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.517 | +0.3% | +3.656e-05 to +0.009963 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 172.2 | 172.8 | +0.3% | -0.1361 to +1.241 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.2 | 172.8 | +0.3% | -0.1361 to +1.241 | no |
| response time (ms), mean | 552.7 | 438.9 | -20.6% | -182 to -45.69 | yes: GAIN |
| response time (ms), 95th percentile | 2356 | 2005 | -14.9% | -739.1 to +37.36 | no |
| response time (ms), 99th percentile | 5639 | 5457 | -3.2% | -982.4 to +618.3 | no |
| time over the response line (% of samples) | 25.33 | 22.05 | -12.9% | -6.056 to -0.5046 | yes: GAIN |
| failed requests (%) | 3.668 | 4.363 | +18.9% | -0.1655 to +1.555 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.2 | -3.5% | -0.6455 to +0.04553 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.5 | +32.5 (native is 0) | +30.36 to +34.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.178 | 1.113 | -5.5% | -0.7518 to +0.6218 | no |
| utilisation (used / allocatable) | 0.09729 | 0.09747 | +0.2% | -0.001473 to +0.001842 | no |
| CPU used (cores), mean | 2.335 | 2.339 | +0.2% | -0.03534 to +0.04422 | no |
| Omni's own CPU (cores), mean | 0 | 0.01135 | +0.0113 (native is 0) | +0.009615 to +0.01309 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.335 | 2.351 | +0.7% | -0.02287 to +0.05444 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.5 | 301.6 | -0.9% | -11.25 to +5.568 | no |
| HPA replicas, mean | 14.92 | 15.38 | +3.1% | +0.2443 to +0.6705 | yes: power given |
| pods started | 5.5 | 3.6 | -34.5% | -2.937 to -0.8634 | yes: GAIN |
| pod start wait, total (s) | 8.9 | 5.2 | -41.6% | -5.807 to -1.593 | yes: GAIN |
| pod start wait, mean (s) | 1.606 | 1.505 | -6.3% | -0.5374 to +0.3355 | no |
| host CPU busy, the real machine under kind (%) | 68.43 | 68.81 | +0.5% | -0.2403 to +0.9928 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 288.1 | 267.9 | -7.0% | -67.85 to +27.37 | no |
| second app: response time (ms), 99th percentile | 1015 | 944 | -7.0% | -283.6 to +141.4 | no |
| second app: time over the response line (% of samples) | 14.84 | 14.62 | -1.5% | -0.5482 to +0.1082 | no |
| second app: failed requests (%) | 13.26 | 13.42 | +1.2% | -0.2342 to +0.5493 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*