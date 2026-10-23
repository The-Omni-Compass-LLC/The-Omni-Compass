# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.917 |
| node-hours | 1.49 | 1.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 164.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 162.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 204.3 | 119 |
| response time (ms), 95th percentile | 410.4 | 189.4 |
| response time (ms), 99th percentile | 1168 | 1028 |
| time over the response line (% of samples) | 7.951 | 5.14 |
| failed requests (%) | 4.666 | 3.748 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 5.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4733 | 0.96 |
| utilisation (used / allocatable) | 0.0687 | 0.0665 |
| CPU used (cores), mean | 1.625 | 1.574 |
| Omni's own CPU (cores), mean | 0 | 0.00978 |
| CPU used with Omni's own (cores), mean | 1.625 | 1.584 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.9 | 423.4 |
| HPA replicas, mean | 8.48 | 10.1 |
| pods started | 5.3 | 7 |
| pod start wait, total (s) | 17.3 | 18.9 |
| pod start wait, mean (s) | 3.375 | 2.852 |
| host CPU busy, the real machine under kind (%) | 46.61 | 45.69 |
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
| worker nodes in service, mean | 5.913 | 5.917 | +0.1% | -0.001608 to +0.00888 | no |
| node-hours | 1.49 | 1.488 | -0.2% | -0.009472 to +0.004083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 164.1 | -0.5% | -1.71 to -0.02526 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 162.6 | -0.5% | -1.678 to +0.08889 | no |
| response time (ms), mean | 204.3 | 119 | -41.7% | -119.5 to -51.04 | yes: GAIN |
| response time (ms), 95th percentile | 410.4 | 189.4 | -53.8% | -254.7 to -187.3 | yes: GAIN |
| response time (ms), 99th percentile | 1168 | 1028 | -12.0% | -1057 to +776.3 | no |
| time over the response line (% of samples) | 7.951 | 5.14 | -35.4% | -3.698 to -1.924 | yes: GAIN |
| failed requests (%) | 4.666 | 3.748 | -19.7% | -1.38 to -0.457 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 5.4 | -20.6% | -2.24 to -0.5604 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31 | +31 (native is 0) | +26.77 to +35.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4733 | 0.96 | +102.8% | -0.02527 to +0.9986 | no |
| utilisation (used / allocatable) | 0.0687 | 0.0665 | -3.2% | -0.004067 to -0.0003373 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.625 | 1.574 | -3.1% | -0.09569 to -0.006638 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00978 | +0.00978 (native is 0) | +0.00825 to +0.01131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.625 | 1.584 | -2.5% | -0.08478 to +0.00202 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 413.9 | 423.4 | +2.3% | +2.123 to +16.83 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.48 | 10.1 | +19.1% | +0.6313 to +2.615 | yes: power given |
| pods started | 5.3 | 7 | +32.1% | -0.209 to +3.609 | no |
| pod start wait, total (s) | 17.3 | 18.9 | +9.2% | -23 to +26.2 | no |
| pod start wait, mean (s) | 3.375 | 2.852 | -15.5% | -5.285 to +4.24 | no |
| host CPU busy, the real machine under kind (%) | 46.61 | 45.69 | -2.0% | -2.002 to +0.1622 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 66 | 15.3 |  |
| machine down | omni | 40 | 9.4 | -27 s (-40%) |
| spike | native | 244 | 56.5 |  |
| spike | omni | 243 | 47.1 | -1 s (-1%) |
| runaway pod started | native | 97 | 9.9 |  |
| runaway pod started | omni | 72 | 5.7 | -25 s (-26%) |
| probe blind | native | 68 | 0.6 |  |
| probe blind | omni | 54 | 0.0 | -14 s (-20%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*