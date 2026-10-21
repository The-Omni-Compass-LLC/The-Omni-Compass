# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 216 | 91.33 |
| response time (ms), 95th percentile | 509.3 | 139.9 |
| response time (ms), 99th percentile | 714.5 | 298 |
| time over the response line (% of samples) | 5.705 | 0.2572 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.055 |
| utilisation (used / allocatable) | 0.03043 | 0.04819 |
| CPU used (cores), mean | 0.7304 | 1.157 |
| Omni's own CPU (cores), mean | 0 | 0.01018 |
| CPU used with Omni's own (cores), mean | 0.7304 | 1.167 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.5 | 561.8 |
| HPA replicas, mean | 2.854 | 2.441 |
| pods started | 2.7 | 2.3 |
| pod start wait, total (s) | 3.4 | 2.8 |
| pod start wait, mean (s) | 1.25 | 1.25 |
| host CPU busy, the real machine under kind (%) | 23.55 | 35.8 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.048e-16 to +8.61e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.514 | -0.2% | -0.0109 to +0.00623 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.4 | +2.4% | +2.565 to +4.998 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.4 | +2.4% | +2.565 to +4.998 | yes: power given |
| response time (ms), mean | 216 | 91.33 | -57.7% | -148 to -101.4 | yes: GAIN |
| response time (ms), 95th percentile | 509.3 | 139.9 | -72.5% | -439.3 to -299.5 | yes: GAIN |
| response time (ms), 99th percentile | 714.5 | 298 | -58.3% | -490.4 to -342.7 | yes: GAIN |
| time over the response line (% of samples) | 5.705 | 0.2572 | -95.5% | -8.062 to -2.833 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 0.2 | -96.2% | -7.211 to -2.789 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 | +4.3 (native is 0) | +3.954 to +4.646 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.055 | +6.5% | -0.1239 to +0.1306 | no |
| utilisation (used / allocatable) | 0.03043 | 0.04819 | +58.4% | +0.01481 to +0.02071 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7304 | 1.157 | +58.4% | +0.3555 to +0.497 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01018 | +0.0102 (native is 0) | +0.009003 to +0.01136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7304 | 1.167 | +59.7% | +0.3645 to +0.5082 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 857.5 | 561.8 | -34.5% | -313.3 to -278.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.854 | 2.441 | -14.5% | -0.637 to -0.1904 | yes: GAIN |
| pods started | 2.7 | 2.3 | -14.8% | -0.9001 to +0.1001 | no |
| pod start wait, total (s) | 3.4 | 2.8 | -17.6% | -1.623 to +0.4228 | no |
| pod start wait, mean (s) | 1.25 | 1.25 | +0.0% | -0.3894 to +0.3894 | EVEN, the same (under one part in a million) |
| host CPU busy, the real machine under kind (%) | 23.55 | 35.8 | +52.0% | +10.22 to +14.29 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*