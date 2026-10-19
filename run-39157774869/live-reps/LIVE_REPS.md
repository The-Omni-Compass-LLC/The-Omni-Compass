# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 478.9 | 477.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 478.9 | 477.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 241.7 | 120.8 |
| response time (ms), 95th percentile | 624.6 | 234.5 |
| response time (ms), 99th percentile | 1118 | 555.9 |
| time over the response line (% of samples) | 10.15 | 2.074 |
| failed requests (%) | 0.8771 | 0.7118 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.6 | 6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7733 | 0.83 |
| utilisation (used / allocatable) | 0.07488 | 0.07234 |
| CPU used (cores), mean | 1.797 | 1.736 |
| Omni's own CPU (cores), mean | 0 | 0.00876 |
| CPU used with Omni's own (cores), mean | 1.797 | 1.745 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.7 | 400.6 |
| HPA replicas, mean | 9.775 | 10.31 |
| pods started | 5.7 | 11.9 |
| pod start wait, total (s) | 19.3 | 28.4 |
| pod start wait, mean (s) | 3.098 | 2.474 |
| host CPU busy, the real machine under kind (%) | 51.97 | 50.68 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.53e-16 to +1.974e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.334 | +0.0% | -0.007084 to +0.008417 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 478.9 | 477.2 | -0.3% | -2.54 to -0.733 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 478.9 | 477.2 | -0.3% | -2.54 to -0.733 | yes: GAIN |
| response time (ms), mean | 241.7 | 120.8 | -50.0% | -156.9 to -84.96 | yes: GAIN |
| response time (ms), 95th percentile | 624.6 | 234.5 | -62.5% | -491.5 to -288.7 | yes: GAIN |
| response time (ms), 99th percentile | 1118 | 555.9 | -50.3% | -683.8 to -440.7 | yes: GAIN |
| time over the response line (% of samples) | 10.15 | 2.074 | -79.6% | -12.67 to -3.478 | yes: GAIN |
| failed requests (%) | 0.8771 | 0.7118 | -18.9% | -0.3363 to +0.005576 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.6 | 6 | -67.7% | -17.76 to -7.44 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.5 | +47.5 (native is 0) | +30.11 to +64.89 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7733 | 0.83 | +7.3% | -0.3381 to +0.4514 | no |
| utilisation (used / allocatable) | 0.07488 | 0.07234 | -3.4% | -0.003442 to -0.001628 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.797 | 1.736 | -3.4% | -0.08262 to -0.03908 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00876 | +0.00876 (native is 0) | +0.007205 to +0.01031 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.797 | 1.745 | -2.9% | -0.07279 to -0.0314 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 389.7 | 400.6 | +2.8% | +8.965 to +12.75 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.775 | 10.31 | +5.5% | -0.5003 to +1.579 | no |
| pods started | 5.7 | 11.9 | +108.8% | +2.603 to +9.797 | yes: power given |
| pod start wait, total (s) | 19.3 | 28.4 | +47.2% | -0.8599 to +19.06 | no |
| pod start wait, mean (s) | 3.098 | 2.474 | -20.1% | -1.501 to +0.2532 | no |
| host CPU busy, the real machine under kind (%) | 51.97 | 50.68 | -2.5% | -1.91 to -0.6708 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*