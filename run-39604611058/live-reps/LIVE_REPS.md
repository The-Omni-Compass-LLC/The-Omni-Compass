# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.468 |
| node-hours | 2.516 | 2.291 |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 275.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 258.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 610.9 | 548.3 |
| response time (ms), 95th percentile | 3562 | 3461 |
| response time (ms), 99th percentile | 4883 | 4948 |
| time over the response line (% of samples) | 17.6 | 16.96 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 204 | 208.9 |
| utilisation (used / allocatable) | 0.06904 | 0.07523 |
| CPU used (cores), mean | 1.657 | 1.639 |
| Omni's own CPU (cores), mean | 0 | 0.02054 |
| CPU used with Omni's own (cores), mean | 1.657 | 1.66 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.1 | 378.2 |
| HPA replicas, mean | 2.014 | 2.368 |
| pods started | 0 | 0.5 |
| pod start wait, total (s) | 0 | 1.2 |
| pod start wait, mean (s) | 0 | 0.75 |
| host CPU busy, the real machine under kind (%) | 46.93 | 47.65 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 642.7 | 646.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.125 |

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
| worker nodes in service, mean | 6 | 5.468 | -8.9% | -1.005 to -0.05903 | yes: GAIN |
| node-hours | 2.516 | 2.291 | -9.0% | -0.4246 to -0.02637 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 275.5 | -0.2% | -1.535 to +0.6927 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 258.8 | -6.2% | -31.63 to -2.634 | yes: GAIN |
| response time (ms), mean | 610.9 | 548.3 | -10.2% | -77.47 to -47.69 | yes: GAIN |
| response time (ms), 95th percentile | 3562 | 3461 | -2.9% | -261.7 to +58.22 | no |
| response time (ms), 99th percentile | 4883 | 4948 | +1.3% | -180.4 to +310.8 | no |
| time over the response line (% of samples) | 17.6 | 16.96 | -3.6% | -1.014 to -0.2661 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 | +11.8 (native is 0) | +11.14 to +12.46 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 204 | 208.9 | +2.4% | -0.8791 to +10.69 | no |
| utilisation (used / allocatable) | 0.06904 | 0.07523 | +9.0% | -0.0005773 to +0.01296 | no |
| CPU used (cores), mean | 1.657 | 1.639 | -1.1% | -0.0477 to +0.01261 | no |
| Omni's own CPU (cores), mean | 0 | 0.02054 | +0.0205 (native is 0) | +0.01607 to +0.02501 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.657 | 1.66 | +0.2% | -0.02646 to +0.03246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.1 | 378.2 | -6.2% | -57.97 to +8.265 | no |
| HPA replicas, mean | 2.014 | 2.368 | +17.6% | +0.06633 to +0.6414 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0 | 1.2 | +1.2 (native is 0) | -0.7892 to +3.189 | no |
| pod start wait, mean (s) | 0 | 0.75 | +0.75 (native is 0) | -0.251 to +1.751 | no |
| host CPU busy, the real machine under kind (%) | 46.93 | 47.65 | +1.5% | +0.3499 to +1.096 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 642.7 | 646.6 | +0.6% | +0.07833 to +7.722 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.125 | -14.6% | -1.618 to -0.1331 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*