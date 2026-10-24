# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.917 |
| node-hours | 1.487 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.3 | 164.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 163.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 208.2 | 154 |
| response time (ms), 95th percentile | 395.8 | 194.5 |
| response time (ms), 99th percentile | 1938 | 1687 |
| time over the response line (% of samples) | 7.673 | 5.889 |
| failed requests (%) | 4.394 | 3.965 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.4383 |
| utilisation (used / allocatable) | 0.06778 | 0.06634 |
| CPU used (cores), mean | 1.604 | 1.57 |
| Omni's own CPU (cores), mean | 0 | 0.00964 |
| CPU used with Omni's own (cores), mean | 1.604 | 1.58 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.7 | 424.9 |
| HPA replicas, mean | 8.452 | 9.743 |
| pods started | 5.7 | 6.4 |
| pod start wait, total (s) | 18.9 | 9.8 |
| pod start wait, mean (s) | 3.003 | 1.535 |
| host CPU busy, the real machine under kind (%) | 46.26 | 45.58 |
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
| worker nodes in service, mean | 5.917 | 5.917 | +0.0% | −0.0055 to +0.0057 | no |
| node-hours | 1.487 | 1.493 | +0.4% | −0.0005 to +0.0128 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.3 | 164.7 | +0.2% | −0.6106 to +1.3317 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 163.1 | +0.2% | −0.6014 to +1.3142 | no |
| response time (ms), mean | 208.2 | 154 | −26.0% | −109.2132 to +0.7742 | no |
| response time (ms), 95th percentile | 395.8 | 194.5 | −50.9% | −287.5567 to −114.9903 | yes: GAIN |
| response time (ms), 99th percentile | 1938 | 1687 | −12.9% | −1323.5546 to +822.2344 | no |
| time over the response line (% of samples) | 7.673 | 5.889 | −23.2% | −3.7125 to +0.1454 | no |
| failed requests (%) | 4.394 | 3.965 | −9.8% | −1.1558 to +0.2970 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.6 | −8.2% | −1.8593 to +0.8593 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 | +27.500 (native is 0) | +23.5209 to +31.4791 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.4383 | +39.2% | −0.4457 to +0.6924 | no |
| utilisation (used / allocatable) | 0.06778 | 0.06634 | −2.1% | −0.0038 to +0.0009 | no |
| CPU used (cores), mean | 1.604 | 1.57 | −2.1% | −0.0898 to +0.0217 | no |
| Omni's own CPU (cores), mean | 0 | 0.00964 | +0.010 (native is 0) | +0.0083 to +0.0110 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.604 | 1.58 | −1.5% | −0.0794 to +0.0306 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420.7 | 424.9 | +1.0% | −7.1214 to +15.5507 | no |
| HPA replicas, mean | 8.452 | 9.743 | +15.3% | +0.0837 to +2.4984 | yes: power given |
| pods started | 5.7 | 6.4 | +12.3% | −0.7717 to +2.1717 | no |
| pod start wait, total (s) | 18.9 | 9.8 | −48.1% | −31.6355 to +13.4355 | no |
| pod start wait, mean (s) | 3.003 | 1.535 | −48.9% | −4.6283 to +1.6926 | no |
| host CPU busy, the real machine under kind (%) | 46.26 | 45.58 | −1.5% | −2.0920 to +0.7183 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 50 | 14.0 |  |
| machine down | omni | 46 | 11.5 | -3 s (-7%) |
| spike | native | 242 | 55.2 |  |
| spike | omni | 240 | 48.9 | -2 s (-1%) |
| runaway pod started | native | 95 | 10.5 |  |
| runaway pod started | omni | 83 | 6.5 | -12 s (-13%) |
| probe blind | native | 69 | 0.5 |  |
| probe blind | omni | 54 | 0.1 | -15 s (-21%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*