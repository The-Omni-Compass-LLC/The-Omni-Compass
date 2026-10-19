# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.969 |
| node-hours | 4.156 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.9 | 443.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.4 | 442.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 156 | 89.44 |
| response time (ms), 95th percentile | 308.6 | 112 |
| response time (ms), 99th percentile | 603.4 | 439.5 |
| time over the response line (% of samples) | 3.131 | 2.043 |
| failed requests (%) | 1.489 | 1.321 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3983 | 0.5367 |
| utilisation (used / allocatable) | 0.04728 | 0.04673 |
| CPU used (cores), mean | 1.129 | 1.116 |
| Omni's own CPU (cores), mean | 0 | 0.00746 |
| CPU used with Omni's own (cores), mean | 1.129 | 1.123 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 605.8 | 605.7 |
| HPA replicas, mean | 8.156 | 8 |
| pods started | 8.5 | 8.5 |
| pod start wait, total (s) | 13.6 | 14.5 |
| pod start wait, mean (s) | 1.602 | 1.72 |
| host CPU busy, the real machine under kind (%) | 34.07 | 33.81 |
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
| worker nodes in service, mean | 5.97 | 5.969 | -0.0% | -0.003061 to +0.001824 | no |
| node-hours | 4.156 | 4.159 | +0.1% | -0.005867 to +0.01031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.9 | 443.9 | +0.0% | -0.7939 to +0.8108 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.4 | 442.3 | -0.0% | -0.8505 to +0.8007 | no |
| response time (ms), mean | 156 | 89.44 | -42.7% | -91.61 to -41.49 | yes: GAIN |
| response time (ms), 95th percentile | 308.6 | 112 | -63.7% | -237.1 to -156.1 | yes: GAIN |
| response time (ms), 99th percentile | 603.4 | 439.5 | -27.2% | -528.4 to +200.6 | no |
| time over the response line (% of samples) | 3.131 | 2.043 | -34.7% | -1.767 to -0.4081 | yes: GAIN |
| failed requests (%) | 1.489 | 1.321 | -11.3% | -0.2895 to -0.04761 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 6.9 | -24.2% | -3.81 to -0.5899 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.7 (native is 0) | +32.88 to +50.52 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3983 | 0.5367 | +34.7% | -0.3735 to +0.6501 | no |
| utilisation (used / allocatable) | 0.04728 | 0.04673 | -1.2% | -0.001357 to +0.0002456 | no |
| CPU used (cores), mean | 1.129 | 1.116 | -1.2% | -0.03235 to +0.005636 | no |
| Omni's own CPU (cores), mean | 0 | 0.00746 | +0.00746 (native is 0) | +0.00621 to +0.00871 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.129 | 1.123 | -0.5% | -0.02385 to +0.01206 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 605.8 | 605.7 | -0.0% | -14.48 to +14.46 | no |
| HPA replicas, mean | 8.156 | 8 | -1.9% | -0.7219 to +0.4115 | no |
| pods started | 8.5 | 8.5 | +0.0% | -1.545 to +1.545 | no |
| pod start wait, total (s) | 13.6 | 14.5 | +6.6% | -3.01 to +4.81 | no |
| pod start wait, mean (s) | 1.602 | 1.72 | +7.4% | -0.2472 to +0.4843 | no |
| host CPU busy, the real machine under kind (%) | 34.07 | 33.81 | -0.8% | -0.7904 to +0.2542 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 56 | 3.8 |  |
| machine down | omni | 29 | 0.8 | -27 s (-48%) |
| spike | native | 246 | 64.2 |  |
| spike | omni | 248 | 64.5 | +2 s (+1%) |
| runaway pod started | native | 2 | 0.1 |  |
| runaway pod started | omni | 2 | 0.0 | +0 s (+2%) |
| probe blind | native | 63 | 1.0 |  |
| probe blind | omni | 60 | 0.0 | -3 s (-5%) |
| api frozen | native | 8 | 0.3 |  |
| api frozen | omni | 3 | 0.0 | -6 s (-69%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -0 s (-10%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*