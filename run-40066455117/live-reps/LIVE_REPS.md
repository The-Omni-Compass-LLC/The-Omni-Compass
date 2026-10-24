# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.9 | 172.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.9 | 172.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 554.3 | 459.4 |
| response time (ms), 95th percentile | 2412 | 2076 |
| response time (ms), 99th percentile | 5795 | 5371 |
| time over the response line (% of samples) | 24.56 | 22.44 |
| failed requests (%) | 3.994 | 4.268 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9683 | 1.332 |
| utilisation (used / allocatable) | 0.09865 | 0.0977 |
| CPU used (cores), mean | 2.368 | 2.345 |
| Omni's own CPU (cores), mean | 0 | 0.01208 |
| CPU used with Omni's own (cores), mean | 2.368 | 2.357 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.6 | 300.9 |
| HPA replicas, mean | 14.99 | 15.2 |
| pods started | 5.5 | 4.7 |
| pod start wait, total (s) | 10.4 | 8.2 |
| pod start wait, mean (s) | 1.9 | 1.679 |
| host CPU busy, the real machine under kind (%) | 68.95 | 68.73 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 283.2 | 296 |
| second app: response time (ms), 99th percentile | 1831 | 1040 |
| second app: time over the response line (% of samples) | 15.02 | 14.82 |
| second app: failed requests (%) | 13.24 | 13.36 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.516 | +0.0% | −0.0033 to +0.0046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.9 | 172.7 | −0.1% | −0.8530 to +0.5920 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.9 | 172.7 | −0.1% | −0.8530 to +0.5920 | no |
| response time (ms), mean | 554.3 | 459.4 | −17.1% | −160.2413 to −29.6368 | yes: GAIN |
| response time (ms), 95th percentile | 2412 | 2076 | −13.9% | −814.5211 to +143.1681 | no |
| response time (ms), 99th percentile | 5795 | 5371 | −7.3% | −1267.8185 to +420.7057 | no |
| time over the response line (% of samples) | 24.56 | 22.44 | −8.6% | −3.7404 to −0.5088 | yes: GAIN |
| failed requests (%) | 3.994 | 4.268 | +6.9% | −0.8487 to +1.3966 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.3 | −4.6% | −0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.3 | +40.300 (native is 0) | +31.2203 to +49.3797 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9683 | 1.332 | +37.5% | −0.7503 to +1.4770 | no |
| utilisation (used / allocatable) | 0.09865 | 0.0977 | −1.0% | −0.0024 to +0.0005 | no |
| CPU used (cores), mean | 2.368 | 2.345 | −1.0% | −0.0572 to +0.0115 | no |
| Omni's own CPU (cores), mean | 0 | 0.01208 | +0.012 (native is 0) | +0.0110 to +0.0131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.368 | 2.357 | −0.5% | −0.0450 to +0.0234 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.6 | 300.9 | +0.8% | −3.8855 to +8.3745 | no |
| HPA replicas, mean | 14.99 | 15.2 | +1.4% | −0.1127 to +0.5272 | no |
| pods started | 5.5 | 4.7 | −14.5% | −1.4573 to −0.1427 | yes: GAIN |
| pod start wait, total (s) | 10.4 | 8.2 | −21.2% | −4.4316 to +0.0316 | no |
| pod start wait, mean (s) | 1.9 | 1.679 | −11.7% | −0.5197 to +0.0759 | no |
| host CPU busy, the real machine under kind (%) | 68.95 | 68.73 | −0.3% | −0.8107 to +0.3669 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 283.2 | 296 | +4.5% | −22.8637 to +48.4197 | no |
| second app: response time (ms), 99th percentile | 1831 | 1040 | −43.2% | −2153.1788 to +571.7504 | no |
| second app: time over the response line (% of samples) | 15.02 | 14.82 | −1.3% | −0.7263 to +0.3323 | no |
| second app: failed requests (%) | 13.24 | 13.36 | +0.9% | −0.5032 to +0.7420 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*