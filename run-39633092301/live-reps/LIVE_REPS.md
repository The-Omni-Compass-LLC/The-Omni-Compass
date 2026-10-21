# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.967 |
| node-hours | 4.158 | 4.157 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.6 | 442.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 171.7 | 91.08 |
| response time (ms), 95th percentile | 330 | 114.7 |
| response time (ms), 99th percentile | 688.1 | 247.5 |
| time over the response line (% of samples) | 3.432 | 1.734 |
| failed requests (%) | 1.501 | 1.36 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3933 | 0.3217 |
| utilisation (used / allocatable) | 0.04899 | 0.04787 |
| CPU used (cores), mean | 1.17 | 1.143 |
| Omni's own CPU (cores), mean | 0 | 0.00778 |
| CPU used with Omni's own (cores), mean | 1.17 | 1.15 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 574.3 | 583 |
| HPA replicas, mean | 8.38 | 8.135 |
| pods started | 8.3 | 8 |
| pod start wait, total (s) | 12.3 | 12.8 |
| pod start wait, mean (s) | 1.488 | 1.577 |
| host CPU busy, the real machine under kind (%) | 35.4 | 34.95 |
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
| worker nodes in service, mean | 5.969 | 5.967 | -0.0% | -0.004028 to +0.0003585 | no |
| node-hours | 4.158 | 4.157 | -0.0% | -0.007967 to +0.005411 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.5 | -0.2% | -1.754 to +0.3966 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.6 | 442.8 | -0.2% | -1.861 to +0.3124 | no |
| response time (ms), mean | 171.7 | 91.08 | -47.0% | -104.4 to -56.87 | yes: GAIN |
| response time (ms), 95th percentile | 330 | 114.7 | -65.3% | -259.9 to -170.8 | yes: GAIN |
| response time (ms), 99th percentile | 688.1 | 247.5 | -64.0% | -539.9 to -341.2 | yes: GAIN |
| time over the response line (% of samples) | 3.432 | 1.734 | -49.5% | -2.343 to -1.054 | yes: GAIN |
| failed requests (%) | 1.501 | 1.36 | -9.4% | -0.2828 to +0.0008909 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 6.1 | -40.8% | -6.218 to -2.182 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 | +42 (native is 0) | +34.26 to +49.74 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3933 | 0.3217 | -18.2% | -0.3287 to +0.1853 | no |
| utilisation (used / allocatable) | 0.04899 | 0.04787 | -2.3% | -0.001943 to -0.000301 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.17 | 1.143 | -2.3% | -0.04676 to -0.007594 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00778 | +0.00778 (native is 0) | +0.006735 to +0.008825 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.17 | 1.15 | -1.7% | -0.0383 to -0.0004919 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 574.3 | 583 | +1.5% | +0.9606 to +16.3 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.38 | 8.135 | -2.9% | -0.761 to +0.2712 | no |
| pods started | 8.3 | 8 | -3.6% | -1.518 to +0.9181 | no |
| pod start wait, total (s) | 12.3 | 12.8 | +4.1% | -2.739 to +3.739 | no |
| pod start wait, mean (s) | 1.488 | 1.577 | +6.0% | -0.1805 to +0.3586 | no |
| host CPU busy, the real machine under kind (%) | 35.4 | 34.95 | -1.3% | -0.7648 to -0.1387 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 81 | 4.4 |  |
| machine down | omni | 33 | 0.9 | -48 s (-60%) |
| spike | native | 256 | 67.3 |  |
| spike | omni | 249 | 59.7 | -7 s (-3%) |
| runaway pod started | native | 6 | 0.4 |  |
| runaway pod started | omni | 1 | 0.0 | -4 s (-75%) |
| probe blind | native | 86 | 1.6 |  |
| probe blind | omni | 60 | 0.0 | -26 s (-30%) |
| api frozen | native | 7 | 0.4 |  |
| api frozen | omni | 2 | 0.0 | -5 s (-71%) |
| metrics down | native | 1 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | +1 s (+74%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*