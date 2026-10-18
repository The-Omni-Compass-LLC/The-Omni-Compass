# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.914 |
| node-hours | 1.494 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.3 | 164.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.8 | 163.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 186.5 | 125.1 |
| response time (ms), 95th percentile | 406.7 | 177.3 |
| response time (ms), 99th percentile | 1404 | 720.9 |
| time over the response line (% of samples) | 7.471 | 5.495 |
| failed requests (%) | 4.569 | 4.196 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.955 |
| utilisation (used / allocatable) | 0.0691 | 0.06789 |
| CPU used (cores), mean | 1.635 | 1.606 |
| Omni's own CPU (cores), mean | 0 | 0.00972 |
| CPU used with Omni's own (cores), mean | 1.635 | 1.616 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 410.2 | 414.9 |
| HPA replicas, mean | 8.637 | 10.39 |
| pods started | 5 | 7.6 |
| pod start wait, total (s) | 15.5 | 29.4 |
| pod start wait, mean (s) | 2.698 | 3.765 |
| host CPU busy, the real machine under kind (%) | 46.69 | 46.46 |
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
| worker nodes in service, mean | 5.917 | 5.914 | -0.1% | -0.00917 to +0.001903 | no |
| node-hours | 1.494 | 1.491 | -0.2% | -0.01129 to +0.00551 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.3 | 164.9 | -0.3% | -1.382 to +0.454 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.8 | 163.2 | -0.3% | -1.475 to +0.4135 | no |
| response time (ms), mean | 186.5 | 125.1 | -33.0% | -93.63 to -29.36 | yes: GAIN |
| response time (ms), 95th percentile | 406.7 | 177.3 | -56.4% | -260.3 to -198.5 | yes: GAIN |
| response time (ms), 99th percentile | 1404 | 720.9 | -48.6% | -1258 to -107.9 | yes: GAIN |
| time over the response line (% of samples) | 7.471 | 5.495 | -26.4% | -3.213 to -0.739 | yes: GAIN |
| failed requests (%) | 4.569 | 4.196 | -8.2% | -0.8539 to +0.1081 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 5.6 | -12.5% | -1.679 to +0.07931 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.5 | +32.5 (native is 0) | +27.06 to +37.94 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.955 | +220.1% | +0.09239 to +1.221 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0691 | 0.06789 | -1.7% | -0.00244 to +2.489e-05 | no |
| CPU used (cores), mean | 1.635 | 1.606 | -1.8% | -0.05791 to -0.000633 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00972 | +0.00972 (native is 0) | +0.008402 to +0.01104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.635 | 1.616 | -1.2% | -0.04755 to +0.008448 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 410.2 | 414.9 | +1.1% | -1.407 to +10.78 | no |
| HPA replicas, mean | 8.637 | 10.39 | +20.4% | +0.9027 to +2.614 | yes: power given |
| pods started | 5 | 7.6 | +52.0% | +1.011 to +4.189 | yes: power given |
| pod start wait, total (s) | 15.5 | 29.4 | +89.7% | -5.513 to +33.31 | no |
| pod start wait, mean (s) | 2.698 | 3.765 | +39.6% | -1.393 to +3.527 | no |
| host CPU busy, the real machine under kind (%) | 46.69 | 46.46 | -0.5% | -0.8235 to +0.3539 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 56 | 13.7 |  |
| machine down | omni | 49 | 9.5 | -7 s (-12%) |
| spike | native | 251 | 64.4 |  |
| spike | omni | 251 | 53.8 | +0 s (+0%) |
| runaway pod started | native | 98 | 10.2 |  |
| runaway pod started | omni | 81 | 6.8 | -17 s (-17%) |
| probe blind | native | 63 | 0.1 |  |
| probe blind | omni | 60 | 0.1 | -3 s (-5%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*