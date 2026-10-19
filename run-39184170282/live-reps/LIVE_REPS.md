# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.974 | 5.97 |
| node-hours | 4.158 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.6 | 443.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.2 | 442.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 152.1 | 86.25 |
| response time (ms), 95th percentile | 283.4 | 108.8 |
| response time (ms), 99th percentile | 501.2 | 217.2 |
| time over the response line (% of samples) | 2.688 | 1.779 |
| failed requests (%) | 1.466 | 1.323 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 6.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.34 | 0.6 |
| utilisation (used / allocatable) | 0.04696 | 0.04598 |
| CPU used (cores), mean | 1.122 | 1.098 |
| Omni's own CPU (cores), mean | 0 | 0.00791 |
| CPU used with Omni's own (cores), mean | 1.122 | 1.106 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 589.5 | 600.5 |
| HPA replicas, mean | 8.285 | 7.981 |
| pods started | 9 | 10.2 |
| pod start wait, total (s) | 14.1 | 18.9 |
| pod start wait, mean (s) | 1.562 | 1.811 |
| host CPU busy, the real machine under kind (%) | 33.9 | 33.46 |
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
| worker nodes in service, mean | 5.974 | 5.97 | -0.1% | -0.006137 to -0.001448 | yes: GAIN |
| node-hours | 4.158 | 4.16 | +0.1% | -0.0002133 to +0.00488 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.6 | 443.6 | +0.0% | -0.1889 to +0.2667 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.2 | 442.1 | -0.0% | -0.424 to +0.1018 | no |
| response time (ms), mean | 152.1 | 86.25 | -43.3% | -78.49 to -53.17 | yes: GAIN |
| response time (ms), 95th percentile | 283.4 | 108.8 | -61.6% | -214.6 to -134.8 | yes: GAIN |
| response time (ms), 99th percentile | 501.2 | 217.2 | -56.7% | -388.8 to -179.3 | yes: GAIN |
| time over the response line (% of samples) | 2.688 | 1.779 | -33.8% | -1.509 to -0.3092 | yes: GAIN |
| failed requests (%) | 1.466 | 1.323 | -9.7% | -0.2334 to -0.05243 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 6.5 | -20.7% | -2.918 to -0.4819 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.4 | +49.4 (native is 0) | +40.2 to +58.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.34 | 0.6 | +76.5% | -0.2427 to +0.7627 | no |
| utilisation (used / allocatable) | 0.04696 | 0.04598 | -2.1% | -0.001486 to -0.0004807 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.122 | 1.098 | -2.2% | -0.03643 to -0.01199 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00791 | +0.00791 (native is 0) | +0.007 to +0.00882 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.122 | 1.106 | -1.5% | -0.02833 to -0.004276 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 589.5 | 600.5 | +1.9% | +4.845 to +17.18 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.285 | 7.981 | -3.7% | -1.071 to +0.4627 | no |
| pods started | 9 | 10.2 | +13.3% | -0.9801 to +3.38 | no |
| pod start wait, total (s) | 14.1 | 18.9 | +34.0% | -1.277 to +10.88 | no |
| pod start wait, mean (s) | 1.562 | 1.811 | +16.0% | -0.08713 to +0.5856 | no |
| host CPU busy, the real machine under kind (%) | 33.9 | 33.46 | -1.3% | -0.7375 to -0.1379 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 63 | 3.1 |  |
| machine down | omni | 32 | 1.1 | -31 s (-49%) |
| spike | native | 258 | 57.7 |  |
| spike | omni | 247 | 56.7 | -11 s (-4%) |
| runaway pod started | native | 4 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | -1 s (-37%) |
| probe blind | native | 61 | 0.7 |  |
| probe blind | omni | 60 | 0.0 | -1 s (-2%) |
| api frozen | native | 12 | 0.2 |  |
| api frozen | omni | 3 | 0.0 | -9 s (-77%) |
| metrics down | native | 3 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-27%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*