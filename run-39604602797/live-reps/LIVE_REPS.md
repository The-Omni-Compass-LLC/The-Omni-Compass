# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.915 |
| node-hours | 1.493 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.3 | 163.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.6 | 162.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 204.9 | 113.6 |
| response time (ms), 95th percentile | 354.3 | 145.5 |
| response time (ms), 99th percentile | 1684 | 609 |
| time over the response line (% of samples) | 6.34 | 4.723 |
| failed requests (%) | 3.704 | 3.474 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 4.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5683 | 0.54 |
| utilisation (used / allocatable) | 0.06431 | 0.06226 |
| CPU used (cores), mean | 1.521 | 1.473 |
| Omni's own CPU (cores), mean | 0 | 0.00866 |
| CPU used with Omni's own (cores), mean | 1.521 | 1.482 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.6 | 448.9 |
| HPA replicas, mean | 8.369 | 9.117 |
| pods started | 5.7 | 6 |
| pod start wait, total (s) | 18 | 17.8 |
| pod start wait, mean (s) | 3.34 | 2.383 |
| host CPU busy, the real machine under kind (%) | 43.72 | 43.13 |
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
| worker nodes in service, mean | 5.914 | 5.915 | +0.0% | -0.002612 to +0.005122 | no |
| node-hours | 1.493 | 1.492 | -0.0% | -0.00754 to +0.006206 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.3 | 163.8 | -0.3% | -1.232 to +0.1985 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.6 | 162.2 | -0.3% | -1.183 to +0.1994 | no |
| response time (ms), mean | 204.9 | 113.6 | -44.6% | -155.5 to -27.23 | yes: GAIN |
| response time (ms), 95th percentile | 354.3 | 145.5 | -58.9% | -256.3 to -161.1 | yes: GAIN |
| response time (ms), 99th percentile | 1684 | 609 | -63.8% | -2122 to -27.72 | yes: GAIN |
| time over the response line (% of samples) | 6.34 | 4.723 | -25.5% | -2.643 to -0.5898 | yes: GAIN |
| failed requests (%) | 3.704 | 3.474 | -6.2% | -0.8664 to +0.4066 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 4.8 | -20.0% | -2.2 to -0.1997 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.9 | +24.9 (native is 0) | +20.54 to +29.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5683 | 0.54 | -5.0% | -0.5091 to +0.4525 | no |
| utilisation (used / allocatable) | 0.06431 | 0.06226 | -3.2% | -0.004004 to -0.0001034 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.521 | 1.473 | -3.2% | -0.09338 to -0.003028 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00866 | +0.00866 (native is 0) | +0.007545 to +0.009775 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.521 | 1.482 | -2.6% | -0.08436 to +0.005274 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.6 | 448.9 | +2.6% | +2.552 to +20.11 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.369 | 9.117 | +8.9% | +0.1897 to +1.306 | yes: power given |
| pods started | 5.7 | 6 | +5.3% | -1.486 to +2.086 | no |
| pod start wait, total (s) | 18 | 17.8 | -1.1% | -30.11 to +29.71 | no |
| pod start wait, mean (s) | 3.34 | 2.383 | -28.6% | -5.391 to +3.478 | no |
| host CPU busy, the real machine under kind (%) | 43.72 | 43.13 | -1.3% | -1.708 to +0.5349 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 55 | 13.2 |  |
| machine down | omni | 40 | 10.0 | -15 s (-27%) |
| spike | native | 232 | 39.8 |  |
| spike | omni | 221 | 35.7 | -11 s (-5%) |
| runaway pod started | native | 84 | 6.2 |  |
| runaway pod started | omni | 48 | 3.8 | -36 s (-43%) |
| probe blind | native | 60 | 0.2 |  |
| probe blind | omni | 60 | 0.1 | +0 s (+0%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*