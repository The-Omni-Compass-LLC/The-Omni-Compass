# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.914 |
| node-hours | 1.496 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.4 | 164.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.8 | 163.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 198.3 | 119.3 |
| response time (ms), 95th percentile | 334.5 | 146.1 |
| response time (ms), 99th percentile | 1168 | 631 |
| time over the response line (% of samples) | 6.799 | 5.14 |
| failed requests (%) | 4.594 | 4.098 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4233 | 0.52 |
| utilisation (used / allocatable) | 0.06794 | 0.0663 |
| CPU used (cores), mean | 1.608 | 1.568 |
| Omni's own CPU (cores), mean | 0 | 0.02812 |
| CPU used with Omni's own (cores), mean | 1.608 | 1.596 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.5 | 422.4 |
| HPA replicas, mean | 8.488 | 10.07 |
| pods started | 5.6 | 10.4 |
| pod start wait, total (s) | 16.9 | 21.6 |
| pod start wait, mean (s) | 2.914 | 2.104 |
| host CPU busy, the real machine under kind (%) | 46.1 | 46.12 |
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
| worker nodes in service, mean | 5.916 | 5.914 | -0.0% | -0.006325 to +0.001918 | no |
| node-hours | 1.496 | 1.493 | -0.2% | -0.00938 to +0.003991 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.4 | 164.7 | -0.4% | -1.388 to +0.1405 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.8 | 163.1 | -0.4% | -1.481 to +0.1547 | no |
| response time (ms), mean | 198.3 | 119.3 | -39.9% | -125.9 to -32.27 | yes: GAIN |
| response time (ms), 95th percentile | 334.5 | 146.1 | -56.3% | -220.9 to -155.8 | yes: GAIN |
| response time (ms), 99th percentile | 1168 | 631 | -46.0% | -1083 to +9.692 | no |
| time over the response line (% of samples) | 6.799 | 5.14 | -24.4% | -2.492 to -0.8271 | yes: GAIN |
| failed requests (%) | 4.594 | 4.098 | -10.8% | -1.079 to +0.08789 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.3 | -13.1% | -1.457 to -0.1427 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 | +43.7 (native is 0) | +40.52 to +46.88 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4233 | 0.52 | +22.8% | -0.2892 to +0.4826 | no |
| utilisation (used / allocatable) | 0.06794 | 0.0663 | -2.4% | -0.002767 to -0.0005193 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.608 | 1.568 | -2.5% | -0.06646 to -0.01264 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02812 | +0.0281 (native is 0) | +0.02503 to +0.03121 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.608 | 1.596 | -0.7% | -0.03798 to +0.01513 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.5 | 422.4 | +2.1% | +3.263 to +14.44 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.488 | 10.07 | +18.7% | +0.6827 to +2.486 | yes: power given |
| pods started | 5.6 | 10.4 | +85.7% | +3.692 to +5.908 | yes: power given |
| pod start wait, total (s) | 16.9 | 21.6 | +27.8% | -12.27 to +21.67 | no |
| pod start wait, mean (s) | 2.914 | 2.104 | -27.8% | -3.86 to +2.24 | no |
| host CPU busy, the real machine under kind (%) | 46.1 | 46.12 | +0.0% | -0.7734 to +0.8051 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 60 | 12.6 |  |
| machine down | omni | 38 | 8.8 | -22 s (-37%) |
| spike | native | 246 | 55.9 |  |
| spike | omni | 236 | 49.6 | -10 s (-4%) |
| runaway pod started | native | 88 | 9.1 |  |
| runaway pod started | omni | 73 | 6.5 | -15 s (-17%) |
| probe blind | native | 54 | 0.2 |  |
| probe blind | omni | 60 | 0.1 | +6 s (+11%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*