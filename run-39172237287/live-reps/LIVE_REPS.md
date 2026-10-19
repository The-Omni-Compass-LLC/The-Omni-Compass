# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.916 |
| node-hours | 1.494 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.1 | 164.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 162.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 206.9 | 115.4 |
| response time (ms), 95th percentile | 402.7 | 193 |
| response time (ms), 99th percentile | 1384 | 560.1 |
| time over the response line (% of samples) | 7.453 | 5.32 |
| failed requests (%) | 4.352 | 4.013 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5467 | 0.5483 |
| utilisation (used / allocatable) | 0.06753 | 0.06651 |
| CPU used (cores), mean | 1.597 | 1.574 |
| Omni's own CPU (cores), mean | 0 | 0.00942 |
| CPU used with Omni's own (cores), mean | 1.597 | 1.583 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.3 | 433.6 |
| HPA replicas, mean | 8.417 | 9.682 |
| pods started | 5.5 | 7.7 |
| pod start wait, total (s) | 8.7 | 21.4 |
| pod start wait, mean (s) | 1.547 | 2.994 |
| host CPU busy, the real machine under kind (%) | 45.8 | 45.8 |
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
| worker nodes in service, mean | 5.914 | 5.916 | +0.0% | -0.002006 to +0.005856 | no |
| node-hours | 1.494 | 1.49 | -0.3% | -0.01152 to +0.003296 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.1 | 164.4 | -0.4% | -1.57 to +0.2644 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 162.8 | -0.4% | -1.535 to +0.3132 | no |
| response time (ms), mean | 206.9 | 115.4 | -44.2% | -136.3 to -46.57 | yes: GAIN |
| response time (ms), 95th percentile | 402.7 | 193 | -52.1% | -250.5 to -168.7 | yes: GAIN |
| response time (ms), 99th percentile | 1384 | 560.1 | -59.5% | -1305 to -343.8 | yes: GAIN |
| time over the response line (% of samples) | 7.453 | 5.32 | -28.6% | -2.898 to -1.369 | yes: GAIN |
| failed requests (%) | 4.352 | 4.013 | -7.8% | -1.18 to +0.502 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 5.3 | -15.9% | -1.954 to -0.04626 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.8 (native is 0) | +24.8 to +34.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5467 | 0.5483 | +0.3% | -0.4277 to +0.4311 | no |
| utilisation (used / allocatable) | 0.06753 | 0.06651 | -1.5% | -0.002906 to +0.0008574 | no |
| CPU used (cores), mean | 1.597 | 1.574 | -1.5% | -0.06828 to +0.02052 | no |
| Omni's own CPU (cores), mean | 0 | 0.00942 | +0.00942 (native is 0) | +0.007842 to +0.011 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.597 | 1.583 | -0.9% | -0.05908 to +0.03016 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.3 | 433.6 | +1.7% | -2.551 to +17.03 | no |
| HPA replicas, mean | 8.417 | 9.682 | +15.0% | +0.3717 to +2.159 | yes: power given |
| pods started | 5.5 | 7.7 | +40.0% | +0.6621 to +3.738 | yes: power given |
| pod start wait, total (s) | 8.7 | 21.4 | +146.0% | -4.368 to +29.77 | no |
| pod start wait, mean (s) | 1.547 | 2.994 | +93.5% | -1.473 to +4.367 | no |
| host CPU busy, the real machine under kind (%) | 45.8 | 45.8 | -0.0% | -1.114 to +1.104 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 46 | 12.8 |  |
| machine down | omni | 36 | 8.4 | -10 s (-22%) |
| spike | native | 247 | 62.6 |  |
| spike | omni | 231 | 57.1 | -16 s (-7%) |
| runaway pod started | native | 101 | 10.9 |  |
| runaway pod started | omni | 87 | 8.0 | -14 s (-14%) |
| probe blind | native | 71 | 0.6 |  |
| probe blind | omni | 54 | 0.1 | -17 s (-24%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*