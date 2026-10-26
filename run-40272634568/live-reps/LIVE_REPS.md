# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.5 | 173.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.5 | 173.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 559.3 | 491.6 |
| response time (ms), 95th percentile | 2369 | 2307 |
| response time (ms), 99th percentile | 5871 | 6003 |
| time over the response line (% of samples) | 26.46 | 23.82 |
| failed requests (%) | 4.02 | 3.893 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7183 | 0.8867 |
| utilisation (used / allocatable) | 0.1008 | 0.1005 |
| CPU used (cores), mean | 2.419 | 2.412 |
| Omni's own CPU (cores), mean | 0 | 0.01275 |
| CPU used with Omni's own (cores), mean | 2.419 | 2.425 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.4 | 286.9 |
| HPA replicas, mean | 15.08 | 15.52 |
| pods started | 5.4 | 3.9 |
| pod start wait, total (s) | 6.5 | 8 |
| pod start wait, mean (s) | 1.203 | 1.817 |
| host CPU busy, the real machine under kind (%) | 69.91 | 70.22 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 282.2 | 229.9 |
| second app: response time (ms), 99th percentile | 1840 | 1547 |
| second app: time over the response line (% of samples) | 15.48 | 15.63 |
| second app: failed requests (%) | 13.67 | 14.18 |

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
| node-hours | 1.516 | 1.518 | +0.1% | −0.0007 to +0.0040 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.5 | 173.6 | +0.1% | −0.3378 to +0.6248 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.5 | 173.6 | +0.1% | −0.3378 to +0.6248 | no |
| response time (ms), mean | 559.3 | 491.6 | −12.1% | −110.9657 to −24.4803 | yes: GAIN |
| response time (ms), 95th percentile | 2369 | 2307 | −2.6% | −422.0684 to +297.9984 | no |
| response time (ms), 99th percentile | 5871 | 6003 | +2.2% | −467.6854 to +729.8782 | no |
| time over the response line (% of samples) | 26.46 | 23.82 | −10.0% | −4.9047 to −0.3910 | yes: GAIN |
| failed requests (%) | 4.02 | 3.893 | −3.2% | −1.0449 to +0.7908 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9 | −6.2% | −1.1001 to −0.0999 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.3 | +46.300 (native is 0) | +34.5412 to +58.0588 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7183 | 0.8867 | +23.4% | −0.4827 to +0.8193 | no |
| utilisation (used / allocatable) | 0.1008 | 0.1005 | −0.3% | −0.0014 to +0.0009 | no |
| CPU used (cores), mean | 2.419 | 2.412 | −0.3% | −0.0344 to +0.0214 | no |
| Omni's own CPU (cores), mean | 0 | 0.01275 | +0.013 (native is 0) | +0.0122 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.419 | 2.425 | +0.3% | −0.0221 to +0.0346 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.4 | 286.9 | +0.2% | −2.6206 to +3.7448 | no |
| HPA replicas, mean | 15.08 | 15.52 | +2.9% | −0.0338 to +0.9121 | no |
| pods started | 5.4 | 3.9 | −27.8% | −2.8593 to −0.1407 | yes: GAIN |
| pod start wait, total (s) | 6.5 | 8 | +23.1% | −1.7909 to +4.7909 | no |
| pod start wait, mean (s) | 1.203 | 1.817 | +51.0% | −0.0955 to +1.3222 | no |
| host CPU busy, the real machine under kind (%) | 69.91 | 70.22 | +0.5% | −0.4354 to +1.0679 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 282.2 | 229.9 | −18.5% | −201.7268 to +97.2368 | no |
| second app: response time (ms), 99th percentile | 1840 | 1547 | −15.9% | −1297.1842 to +711.9596 | no |
| second app: time over the response line (% of samples) | 15.48 | 15.63 | +1.0% | −0.4636 to +0.7803 | no |
| second app: failed requests (%) | 13.67 | 14.18 | +3.7% | −0.2188 to +1.2351 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*