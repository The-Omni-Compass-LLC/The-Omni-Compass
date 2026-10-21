# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.485 |
| node-hours | 2.514 | 2.301 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 275.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 259.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 602.5 | 537.2 |
| response time (ms), 95th percentile | 3588 | 3467 |
| response time (ms), 99th percentile | 5121 | 5030 |
| time over the response line (% of samples) | 16.87 | 16.53 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 200.9 | 204.9 |
| utilisation (used / allocatable) | 0.06744 | 0.07356 |
| CPU used (cores), mean | 1.619 | 1.606 |
| Omni's own CPU (cores), mean | 0 | 0.02231 |
| CPU used with Omni's own (cores), mean | 1.619 | 1.628 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.6 | 386.8 |
| HPA replicas, mean | 2.164 | 2.494 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 0.1 | 0.4 |
| pod start wait, mean (s) | 0.1 | 0.4 |
| host CPU busy, the real machine under kind (%) | 46.01 | 46.74 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 629.1 | 633.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.149 |

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
| worker nodes in service, mean | 6 | 5.485 | -8.6% | -0.9344 to -0.0948 | yes: GAIN |
| node-hours | 2.514 | 2.301 | -8.5% | -0.3875 to -0.03918 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 275.3 | +0.0% | -0.5728 to +0.8098 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 259.1 | -5.8% | -29.06 to -3.082 | yes: GAIN |
| response time (ms), mean | 602.5 | 537.2 | -10.8% | -74.58 to -55.99 | yes: GAIN |
| response time (ms), 95th percentile | 3588 | 3467 | -3.4% | -220.5 to -21.05 | yes: GAIN |
| response time (ms), 99th percentile | 5121 | 5030 | -1.8% | -342.1 to +160.3 | no |
| time over the response line (% of samples) | 16.87 | 16.53 | -2.0% | -0.845 to +0.16 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.9 | +0.9% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.7 (native is 0) | +10.19 to +13.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 200.9 | 204.9 | +2.0% | -0.07023 to +8.004 | no |
| utilisation (used / allocatable) | 0.06744 | 0.07356 | +9.1% | +0.0005883 to +0.01165 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.619 | 1.606 | -0.8% | -0.03963 to +0.01469 | no |
| Omni's own CPU (cores), mean | 0 | 0.02231 | +0.0223 (native is 0) | +0.0183 to +0.02632 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.619 | 1.628 | +0.6% | -0.01859 to +0.03826 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.6 | 386.8 | -5.6% | -44.38 to -1.09 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.164 | 2.494 | +15.2% | +0.02373 to +0.6362 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.1 | 0.4 | +300.0% | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0.1 | 0.4 | +300.0% | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 46.01 | 46.74 | +1.6% | +0.3562 to +1.097 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 629.1 | 633.7 | +0.7% | -2.766 to +11.97 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.149 | -14.2% | -1.519 to -0.1832 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*