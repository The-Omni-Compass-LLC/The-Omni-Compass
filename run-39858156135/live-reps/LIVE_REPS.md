# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.922 | 5.917 |
| node-hours | 1.491 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.6 | 164.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.2 | 162.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 226.8 | 114.4 |
| response time (ms), 95th percentile | 427.1 | 202.3 |
| response time (ms), 99th percentile | 1418 | 692.9 |
| time over the response line (% of samples) | 8.124 | 5.508 |
| failed requests (%) | 4.658 | 4.085 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.9083 |
| utilisation (used / allocatable) | 0.06822 | 0.06679 |
| CPU used (cores), mean | 1.616 | 1.581 |
| Omni's own CPU (cores), mean | 0 | 0.02832 |
| CPU used with Omni's own (cores), mean | 1.616 | 1.609 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.1 | 428.9 |
| HPA replicas, mean | 8.387 | 11.35 |
| pods started | 5.4 | 9.7 |
| pod start wait, total (s) | 8.6 | 26.7 |
| pod start wait, mean (s) | 1.628 | 2.633 |
| host CPU busy, the real machine under kind (%) | 46.27 | 46.56 |
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
| worker nodes in service, mean | 5.922 | 5.917 | -0.1% | -0.01089 to +0.0006522 | no |
| node-hours | 1.491 | 1.491 | -0.0% | -0.008276 to +0.007998 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.6 | 164.5 | -0.1% | -1.052 to +0.774 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.2 | 162.9 | -0.1% | -1.116 to +0.6426 | no |
| response time (ms), mean | 226.8 | 114.4 | -49.5% | -164 to -60.75 | yes: GAIN |
| response time (ms), 95th percentile | 427.1 | 202.3 | -52.6% | -262.8 to -186.7 | yes: GAIN |
| response time (ms), 99th percentile | 1418 | 692.9 | -51.1% | -1366 to -84.81 | yes: GAIN |
| time over the response line (% of samples) | 8.124 | 5.508 | -32.2% | -3.443 to -1.789 | yes: GAIN |
| failed requests (%) | 4.658 | 4.085 | -12.3% | -1.03 to -0.1159 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 5.6 | -13.8% | -1.82 to +0.02037 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.1 | +44.1 (native is 0) | +41.5 to +46.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.9083 | +581.2% | +0.2503 to +1.3 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06822 | 0.06679 | -2.1% | -0.003202 to +0.0003245 | no |
| CPU used (cores), mean | 1.616 | 1.581 | -2.2% | -0.0768 to +0.005986 | no |
| Omni's own CPU (cores), mean | 0 | 0.02832 | +0.0283 (native is 0) | +0.02358 to +0.03306 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.616 | 1.609 | -0.4% | -0.04662 to +0.03245 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.1 | 428.9 | +1.6% | -2.255 to +15.91 | no |
| HPA replicas, mean | 8.387 | 11.35 | +35.3% | +2.15 to +3.776 | yes: power given |
| pods started | 5.4 | 9.7 | +79.6% | +3.036 to +5.564 | yes: power given |
| pod start wait, total (s) | 8.6 | 26.7 | +210.5% | -1.953 to +38.15 | no |
| pod start wait, mean (s) | 1.628 | 2.633 | +61.7% | -0.6975 to +2.707 | no |
| host CPU busy, the real machine under kind (%) | 46.27 | 46.56 | +0.6% | -0.7773 to +1.353 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 64 | 15.5 |  |
| machine down | omni | 40 | 9.2 | -24 s (-37%) |
| spike | native | 246 | 62.6 |  |
| spike | omni | 247 | 55.9 | +1 s (+0%) |
| runaway pod started | native | 114 | 11.0 |  |
| runaway pod started | omni | 83 | 7.8 | -31 s (-27%) |
| probe blind | native | 65 | 0.6 |  |
| probe blind | omni | 60 | 0.0 | -5 s (-8%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*