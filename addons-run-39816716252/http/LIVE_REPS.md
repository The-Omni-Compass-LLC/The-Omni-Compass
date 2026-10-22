# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 199.8 | 84.99 |
| response time (ms), 95th percentile | 476.4 | 128.8 |
| response time (ms), 99th percentile | 657.7 | 268.2 |
| time over the response line (% of samples) | 5.358 | 0.2317 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 55.56 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02667 |
| utilisation (used / allocatable) | 0.0303 | 0.04656 |
| CPU used (cores), mean | 0.7272 | 1.117 |
| Omni's own CPU (cores), mean | 0 | 0.03431 |
| CPU used with Omni's own (cores), mean | 0.7272 | 1.152 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 861.3 | 584.2 |
| HPA replicas, mean | 2.894 | 2.533 |
| pods started | 3 | 2.6 |
| pod start wait, total (s) | 4.3 | 3.6 |
| pod start wait, mean (s) | 1.417 | 1.35 |
| host CPU busy, the real machine under kind (%) | 23.49 | 35.45 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.516 | -0.1% | -0.009838 to +0.007504 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.3 | +2.3% | +2.326 to +4.912 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.3 | +2.3% | +2.326 to +4.912 | yes: power given |
| response time (ms), mean | 199.8 | 84.99 | -57.5% | -139.6 to -90.02 | yes: GAIN |
| response time (ms), 95th percentile | 476.4 | 128.8 | -73.0% | -413.6 to -281.7 | yes: GAIN |
| response time (ms), 99th percentile | 657.7 | 268.2 | -59.2% | -465.3 to -313.7 | yes: GAIN |
| time over the response line (% of samples) | 5.358 | 0.2317 | -95.7% | -7.885 to -2.369 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 0.1 | -98.0% | -7.59 to -2.41 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 | +12.2 (native is 0) | +8.185 to +16.22 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02667 | -50.0% | -0.1349 to +0.08161 | no |
| utilisation (used / allocatable) | 0.0303 | 0.04656 | +53.7% | +0.01257 to +0.01995 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7272 | 1.117 | +53.7% | +0.3017 to +0.4788 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03431 | +0.0343 (native is 0) | +0.02952 to +0.0391 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7272 | 1.152 | +58.4% | +0.3315 to +0.5176 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 861.3 | 584.2 | -32.2% | -306.9 to -247.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.894 | 2.533 | -12.5% | -0.6041 to -0.1175 | yes: GAIN |
| pods started | 3 | 2.6 | -13.3% | -1.003 to +0.2032 | no |
| pod start wait, total (s) | 4.3 | 3.6 | -16.3% | -2.247 to +0.8471 | no |
| pod start wait, mean (s) | 1.417 | 1.35 | -4.7% | -0.423 to +0.2897 | no |
| host CPU busy, the real machine under kind (%) | 23.49 | 35.45 | +50.9% | +9.323 to +14.6 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*