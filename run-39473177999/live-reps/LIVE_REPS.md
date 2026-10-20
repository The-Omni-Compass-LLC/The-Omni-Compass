# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.97 |
| node-hours | 4.154 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 441.8 | 442.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 440.2 | 440.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 162.5 | 95.81 |
| response time (ms), 95th percentile | 290.3 | 104.4 |
| response time (ms), 99th percentile | 737.6 | 436.2 |
| time over the response line (% of samples) | 2.743 | 1.751 |
| failed requests (%) | 1.095 | 1.07 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.13 |
| utilisation (used / allocatable) | 0.04402 | 0.0433 |
| CPU used (cores), mean | 1.051 | 1.034 |
| Omni's own CPU (cores), mean | 0 | 0.00774 |
| CPU used with Omni's own (cores), mean | 1.051 | 1.042 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 640.7 | 648.8 |
| HPA replicas, mean | 8.021 | 7.951 |
| pods started | 8.7 | 10.6 |
| pod start wait, total (s) | 13.9 | 18.8 |
| pod start wait, mean (s) | 1.602 | 1.798 |
| host CPU busy, the real machine under kind (%) | 34.66 | 34.43 |
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
| worker nodes in service, mean | 5.969 | 5.97 | +0.0% | -0.003965 to +0.005005 | no |
| node-hours | 4.154 | 4.16 | +0.1% | -0.001295 to +0.01363 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 441.8 | 442.2 | +0.1% | -0.4255 to +1.189 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 440.2 | 440.6 | +0.1% | -0.5951 to +1.408 | no |
| response time (ms), mean | 162.5 | 95.81 | -41.0% | -97.49 to -35.88 | yes: GAIN |
| response time (ms), 95th percentile | 290.3 | 104.4 | -64.0% | -234.1 to -137.7 | yes: GAIN |
| response time (ms), 99th percentile | 737.6 | 436.2 | -40.9% | -481.6 to -121.1 | yes: GAIN |
| time over the response line (% of samples) | 2.743 | 1.751 | -36.2% | -1.744 to -0.2397 | yes: GAIN |
| failed requests (%) | 1.095 | 1.07 | -2.3% | -0.1416 to +0.09107 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6.1 | -20.8% | -3.224 to +0.02417 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.4 | +48.4 (native is 0) | +38.57 to +58.23 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.13 | -56.4% | -0.5534 to +0.2168 | no |
| utilisation (used / allocatable) | 0.04402 | 0.0433 | -1.6% | -0.001287 to -0.0001397 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.051 | 1.034 | -1.6% | -0.03105 to -0.003081 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00774 | +0.00774 (native is 0) | +0.006503 to +0.008977 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.051 | 1.042 | -0.9% | -0.02291 to +0.004263 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 640.7 | 648.8 | +1.3% | +0.518 to +15.79 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.021 | 7.951 | -0.9% | -0.7903 to +0.6503 | no |
| pods started | 8.7 | 10.6 | +21.8% | +0.1658 to +3.634 | yes: power given |
| pod start wait, total (s) | 13.9 | 18.8 | +35.3% | -0.2189 to +10.02 | no |
| pod start wait, mean (s) | 1.602 | 1.798 | +12.2% | -0.1306 to +0.5228 | no |
| host CPU busy, the real machine under kind (%) | 34.66 | 34.43 | -0.6% | -0.6376 to +0.1887 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 51 | 2.8 |  |
| machine down | omni | 43 | 1.4 | -8 s (-17%) |
| spike | native | 233 | 52.4 |  |
| spike | omni | 224 | 49.0 | -9 s (-4%) |
| runaway pod started | native | 7 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | -5 s (-72%) |
| probe blind | native | 61 | 0.7 |  |
| probe blind | omni | 60 | 0.1 | -1 s (-2%) |
| api frozen | native | 6 | 0.2 |  |
| api frozen | omni | 2 | 0.0 | -4 s (-71%) |
| metrics down | native | 4 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -2 s (-53%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*