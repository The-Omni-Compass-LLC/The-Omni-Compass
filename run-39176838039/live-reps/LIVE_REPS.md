# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.336 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 492 | 490.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 492 | 490.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 362.6 | 185.2 |
| response time (ms), 95th percentile | 953.7 | 396.7 |
| response time (ms), 99th percentile | 1853 | 1093 |
| time over the response line (% of samples) | 20.26 | 4.819 |
| failed requests (%) | 2.101 | 1.732 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 33.1 | 13.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4067 | 0.9683 |
| utilisation (used / allocatable) | 0.09455 | 0.09161 |
| CPU used (cores), mean | 2.269 | 2.199 |
| Omni's own CPU (cores), mean | 0 | 0.01133 |
| CPU used with Omni's own (cores), mean | 2.269 | 2.21 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300 | 308.4 |
| HPA replicas, mean | 9.9 | 12.54 |
| pods started | 5 | 17.7 |
| pod start wait, total (s) | 8.5 | 32.8 |
| pod start wait, mean (s) | 1.7 | 1.852 |
| host CPU busy, the real machine under kind (%) | 64.97 | 63.63 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.206e-16 to +5.43e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.336 | 4.337 | +0.0% | -0.007296 to +0.008963 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 492 | 490.1 | -0.4% | -2.867 to -0.8928 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 492 | 490.1 | -0.4% | -2.867 to -0.8928 | yes: GAIN |
| response time (ms), mean | 362.6 | 185.2 | -48.9% | -185.2 to -169.6 | yes: GAIN |
| response time (ms), 95th percentile | 953.7 | 396.7 | -58.4% | -595.8 to -518.4 | yes: GAIN |
| response time (ms), 99th percentile | 1853 | 1093 | -41.0% | -945.8 to -574.6 | yes: GAIN |
| time over the response line (% of samples) | 20.26 | 4.819 | -76.2% | -16.14 to -14.75 | yes: GAIN |
| failed requests (%) | 2.101 | 1.732 | -17.6% | -0.478 to -0.2616 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 33.1 | 13.7 | -58.6% | -21.46 to -17.34 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.3 | +78.3 (native is 0) | +69.08 to +87.52 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4067 | 0.9683 | +138.1% | +0.101 to +1.022 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09455 | 0.09161 | -3.1% | -0.003555 to -0.002327 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.269 | 2.199 | -3.1% | -0.08532 to -0.05584 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01133 | +0.0113 (native is 0) | +0.01095 to +0.01171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.269 | 2.21 | -2.6% | -0.07406 to -0.04444 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300 | 308.4 | +2.8% | +6.629 to +10.15 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.9 | 12.54 | +26.7% | +2.234 to +3.053 | yes: power given |
| pods started | 5 | 17.7 | +254.0% | +9.43 to +15.97 | yes: power given |
| pod start wait, total (s) | 8.5 | 32.8 | +285.9% | +18.06 to +30.54 | yes: LOSS |
| pod start wait, mean (s) | 1.7 | 1.852 | +8.9% | -0.2165 to +0.5202 | no |
| host CPU busy, the real machine under kind (%) | 64.97 | 63.63 | -2.1% | -1.83 to -0.8448 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*