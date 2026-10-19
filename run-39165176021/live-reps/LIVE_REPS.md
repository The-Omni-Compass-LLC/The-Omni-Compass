# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.039 |
| node-hours | 2.512 | 2.113 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 242 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 456.2 | 406.4 |
| response time (ms), 95th percentile | 2785 | 2735 |
| response time (ms), 99th percentile | 4232 | 4318 |
| time over the response line (% of samples) | 14.89 | 14.48 |
| failed requests (%) | 0 | 0.04854 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174 | 179.6 |
| utilisation (used / allocatable) | 0.05791 | 0.06911 |
| CPU used (cores), mean | 1.39 | 1.384 |
| Omni's own CPU (cores), mean | 0 | 0.01997 |
| CPU used with Omni's own (cores), mean | 1.39 | 1.404 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.2 | 421.7 |
| HPA replicas, mean | 2.058 | 2.345 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.1 |
| pod start wait, mean (s) | 0 | 0.1 |
| host CPU busy, the real machine under kind (%) | 40.1 | 40.8 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 543.8 | 550.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.517 |

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
| worker nodes in service, mean | 6 | 5.039 | -16.0% | -1.459 to -0.4626 | yes: GAIN |
| node-hours | 2.512 | 2.113 | -15.9% | -0.6047 to -0.1937 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.2 | +0.3% | -0.3898 to +1.835 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 242 | -10.9% | -44.56 to -14.52 | yes: GAIN |
| response time (ms), mean | 456.2 | 406.4 | -10.9% | -76.91 to -22.61 | yes: GAIN |
| response time (ms), 95th percentile | 2785 | 2735 | -1.8% | -222.1 to +122.7 | no |
| response time (ms), 99th percentile | 4232 | 4318 | +2.0% | -39.49 to +211.3 | no |
| time over the response line (% of samples) | 14.89 | 14.48 | -2.7% | -0.9242 to +0.1098 | no |
| failed requests (%) | 0 | 0.04854 | +0.0485 (native is 0) | -0.06126 to +0.1583 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.4 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.7 | +12.7 (native is 0) | +11.53 to +13.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174 | 179.6 | +3.2% | +1.526 to +9.707 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05791 | 0.06911 | +19.3% | +0.004466 to +0.01793 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.39 | 1.384 | -0.4% | -0.05469 to +0.04322 | no |
| Omni's own CPU (cores), mean | 0 | 0.01997 | +0.02 (native is 0) | +0.01548 to +0.02446 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.39 | 1.404 | +1.0% | -0.0341 to +0.06257 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.2 | 421.7 | -11.8% | -96.66 to -16.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.058 | 2.345 | +13.9% | -0.0501 to +0.623 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 40.1 | 40.8 | +1.8% | +0.3873 to +1.032 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 543.8 | 550.5 | +1.2% | +0.8591 to +12.54 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.517 | -24.7% | -2.201 to -0.7659 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*