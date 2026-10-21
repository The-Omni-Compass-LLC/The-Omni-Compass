# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.968 | 5.97 |
| node-hours | 4.158 | 4.163 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.6 | 446.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444 | 445.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 167.6 | 93.14 |
| response time (ms), 95th percentile | 342.8 | 123.9 |
| response time (ms), 99th percentile | 646.6 | 307.6 |
| time over the response line (% of samples) | 3.493 | 2.133 |
| failed requests (%) | 1.705 | 1.604 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.33 |
| utilisation (used / allocatable) | 0.05074 | 0.05043 |
| CPU used (cores), mean | 1.211 | 1.204 |
| Omni's own CPU (cores), mean | 0 | 0.00835 |
| CPU used with Omni's own (cores), mean | 1.211 | 1.213 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 544.1 | 548 |
| HPA replicas, mean | 8.748 | 8.742 |
| pods started | 8.5 | 9.1 |
| pod start wait, total (s) | 12.2 | 15.2 |
| pod start wait, mean (s) | 1.44 | 1.618 |
| host CPU busy, the real machine under kind (%) | 36.8 | 36.62 |
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
| worker nodes in service, mean | 5.968 | 5.97 | +0.0% | -0.002131 to +0.006962 | no |
| node-hours | 4.158 | 4.163 | +0.1% | -0.00256 to +0.01189 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.6 | 446.7 | +0.2% | -1.022 to +3.082 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444 | 445.1 | +0.3% | -0.9539 to +3.263 | no |
| response time (ms), mean | 167.6 | 93.14 | -44.4% | -90.4 to -58.5 | yes: GAIN |
| response time (ms), 95th percentile | 342.8 | 123.9 | -63.9% | -251.8 to -185.9 | yes: GAIN |
| response time (ms), 99th percentile | 646.6 | 307.6 | -52.4% | -434 to -243.9 | yes: GAIN |
| time over the response line (% of samples) | 3.493 | 2.133 | -39.0% | -1.876 to -0.8459 | yes: GAIN |
| failed requests (%) | 1.705 | 1.604 | -5.9% | -0.242 to +0.04081 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 7.4 | -26.7% | -3.918 to -1.482 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.1 | +47.1 (native is 0) | +40.91 to +53.29 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.33 | +22.2% | -0.1426 to +0.2626 | no |
| utilisation (used / allocatable) | 0.05074 | 0.05043 | -0.6% | -0.001143 to +0.0005122 | no |
| CPU used (cores), mean | 1.211 | 1.204 | -0.6% | -0.02621 to +0.0123 | no |
| Omni's own CPU (cores), mean | 0 | 0.00835 | +0.00835 (native is 0) | +0.00723 to +0.00947 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.211 | 1.213 | +0.1% | -0.0179 to +0.0207 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 544.1 | 548 | +0.7% | -2.1 to +9.989 | no |
| HPA replicas, mean | 8.748 | 8.742 | -0.1% | -0.6895 to +0.6758 | no |
| pods started | 8.5 | 9.1 | +7.1% | -0.6707 to +1.871 | no |
| pod start wait, total (s) | 12.2 | 15.2 | +24.6% | -0.6474 to +6.647 | no |
| pod start wait, mean (s) | 1.44 | 1.618 | +12.4% | -0.05324 to +0.4097 | no |
| host CPU busy, the real machine under kind (%) | 36.8 | 36.62 | -0.5% | -0.6281 to +0.2688 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 68 | 4.5 |  |
| machine down | omni | 38 | 1.3 | -30 s (-44%) |
| spike | native | 271 | 71.4 |  |
| spike | omni | 269 | 72.5 | -1 s (-1%) |
| runaway pod started | native | 6 | 0.5 |  |
| runaway pod started | omni | 2 | 0.0 | -3 s (-58%) |
| probe blind | native | 67 | 1.2 |  |
| probe blind | omni | 48 | 0.0 | -19 s (-29%) |
| api frozen | native | 15 | 0.5 |  |
| api frozen | omni | 2 | 0.0 | -13 s (-86%) |
| metrics down | native | 1 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+28%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*