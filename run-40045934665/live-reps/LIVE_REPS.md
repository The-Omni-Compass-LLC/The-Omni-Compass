# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.969 |
| node-hours | 4.153 | 4.158 |
| energy, parked workers still on at idle power (Wh, declared model) | 447.3 | 446.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.7 | 445.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 170 | 93.94 |
| response time (ms), 95th percentile | 350.5 | 125 |
| response time (ms), 99th percentile | 598.1 | 219.2 |
| time over the response line (% of samples) | 3.781 | 2.143 |
| failed requests (%) | 1.986 | 1.793 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5867 | 0.4367 |
| utilisation (used / allocatable) | 0.05309 | 0.05158 |
| CPU used (cores), mean | 1.268 | 1.232 |
| Omni's own CPU (cores), mean | 0 | 0.00816 |
| CPU used with Omni's own (cores), mean | 1.268 | 1.24 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 526.5 | 535.9 |
| HPA replicas, mean | 8.732 | 8.75 |
| pods started | 8.1 | 8.2 |
| pod start wait, total (s) | 13.3 | 13.3 |
| pod start wait, mean (s) | 1.654 | 1.609 |
| host CPU busy, the real machine under kind (%) | 37.7 | 36.87 |
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
| worker nodes in service, mean | 5.969 | 5.969 | -0.0% | -0.005052 to +0.003786 | no |
| node-hours | 4.153 | 4.158 | +0.1% | -0.000967 to +0.01136 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 447.3 | 446.8 | -0.1% | -1.357 to +0.4811 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 445.7 | 445.2 | -0.1% | -1.439 to +0.492 | no |
| response time (ms), mean | 170 | 93.94 | -44.8% | -93.47 to -58.72 | yes: GAIN |
| response time (ms), 95th percentile | 350.5 | 125 | -64.3% | -260.2 to -190.9 | yes: GAIN |
| response time (ms), 99th percentile | 598.1 | 219.2 | -63.3% | -434.6 to -323.3 | yes: GAIN |
| time over the response line (% of samples) | 3.781 | 2.143 | -43.3% | -2.026 to -1.249 | yes: GAIN |
| failed requests (%) | 1.986 | 1.793 | -9.7% | -0.3242 to -0.06241 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 7.8 | -26.4% | -4.053 to -1.547 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.2 | +42.2 (native is 0) | +34.91 to +49.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5867 | 0.4367 | -25.6% | -0.4915 to +0.1915 | no |
| utilisation (used / allocatable) | 0.05309 | 0.05158 | -2.8% | -0.002483 to -0.0005205 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.268 | 1.232 | -2.8% | -0.05954 to -0.01245 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00816 | +0.00816 (native is 0) | +0.007193 to +0.009127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.268 | 1.24 | -2.2% | -0.05068 to -0.00499 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 526.5 | 535.9 | +1.8% | -3.89 to +22.74 | no |
| HPA replicas, mean | 8.732 | 8.75 | +0.2% | -0.6363 to +0.6721 | no |
| pods started | 8.1 | 8.2 | +1.2% | -1.309 to +1.509 | no |
| pod start wait, total (s) | 13.3 | 13.3 | +0.0% | -3.287 to +3.287 | no |
| pod start wait, mean (s) | 1.654 | 1.609 | -2.8% | -0.3251 to +0.2334 | no |
| host CPU busy, the real machine under kind (%) | 37.7 | 36.87 | -2.2% | -1.331 to -0.32 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 65 | 5.2 |  |
| machine down | omni | 37 | 1.2 | -28 s (-43%) |
| spike | native | 284 | 81.1 |  |
| spike | omni | 274 | 82.8 | -11 s (-4%) |
| runaway pod started | native | 1 | 0.3 |  |
| runaway pod started | omni | 2 | 0.0 | +1 s (+60%) |
| probe blind | native | 43 | 1.1 |  |
| probe blind | omni | 60 | 0.0 | +17 s (+40%) |
| api frozen | native | 8 | 0.4 |  |
| api frozen | omni | 4 | 0.0 | -5 s (-57%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-52%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*