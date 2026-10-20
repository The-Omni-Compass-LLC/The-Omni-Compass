# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.97 |
| node-hours | 4.158 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 441.4 | 441.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 439.9 | 439.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.6 | 85.78 |
| response time (ms), 95th percentile | 284.6 | 108 |
| response time (ms), 99th percentile | 590.2 | 329.3 |
| time over the response line (% of samples) | 2.747 | 1.602 |
| failed requests (%) | 1.095 | 0.9945 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 4.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5317 | 0.3433 |
| utilisation (used / allocatable) | 0.04299 | 0.04238 |
| CPU used (cores), mean | 1.027 | 1.012 |
| Omni's own CPU (cores), mean | 0 | 0.00726 |
| CPU used with Omni's own (cores), mean | 1.027 | 1.019 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 672.5 | 676.7 |
| HPA replicas, mean | 7.774 | 7.407 |
| pods started | 8.7 | 8.8 |
| pod start wait, total (s) | 14.2 | 16.2 |
| pod start wait, mean (s) | 1.633 | 1.846 |
| host CPU busy, the real machine under kind (%) | 31.37 | 31.23 |
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
| worker nodes in service, mean | 5.97 | 5.97 | -0.0% | -0.003122 to +0.001961 | no |
| node-hours | 4.158 | 4.16 | +0.1% | -0.005268 to +0.009435 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 441.4 | 441.4 | -0.0% | -0.8097 to +0.8012 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 439.9 | 439.8 | -0.0% | -0.8574 to +0.7864 | no |
| response time (ms), mean | 137.6 | 85.78 | -37.7% | -76.48 to -27.14 | yes: GAIN |
| response time (ms), 95th percentile | 284.6 | 108 | -62.0% | -231.1 to -122.1 | yes: GAIN |
| response time (ms), 99th percentile | 590.2 | 329.3 | -44.2% | -416.1 to -105.6 | yes: GAIN |
| time over the response line (% of samples) | 2.747 | 1.602 | -41.7% | -1.991 to -0.2989 | yes: GAIN |
| failed requests (%) | 1.095 | 0.9945 | -9.2% | -0.2298 to +0.02929 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 4.9 | -43.0% | -6.399 to -1.001 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.3 | +40.3 (native is 0) | +29.57 to +51.03 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5317 | 0.3433 | -35.4% | -0.6179 to +0.2413 | no |
| utilisation (used / allocatable) | 0.04299 | 0.04238 | -1.4% | -0.001461 to +0.0002501 | no |
| CPU used (cores), mean | 1.027 | 1.012 | -1.4% | -0.03505 to +0.005887 | no |
| Omni's own CPU (cores), mean | 0 | 0.00726 | +0.00726 (native is 0) | +0.005749 to +0.008771 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.027 | 1.019 | -0.7% | -0.02676 to +0.01212 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 672.5 | 676.7 | +0.6% | -11.1 to +19.42 | no |
| HPA replicas, mean | 7.774 | 7.407 | -4.7% | -1.184 to +0.4502 | no |
| pods started | 8.7 | 8.8 | +1.1% | -1.601 to +1.801 | no |
| pod start wait, total (s) | 14.2 | 16.2 | +14.1% | -3.103 to +7.103 | no |
| pod start wait, mean (s) | 1.633 | 1.846 | +13.1% | -0.2326 to +0.6599 | no |
| host CPU busy, the real machine under kind (%) | 31.37 | 31.23 | -0.5% | -0.4895 to +0.1942 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 55 | 2.9 |  |
| machine down | omni | 25 | 0.7 | -31 s (-55%) |
| spike | native | 226 | 53.5 |  |
| spike | omni | 214 | 49.1 | -11 s (-5%) |
| runaway pod started | native | 3 | 0.1 |  |
| runaway pod started | omni | 2 | 0.0 | -1 s (-39%) |
| probe blind | native | 63 | 1.1 |  |
| probe blind | omni | 60 | 0.1 | -3 s (-5%) |
| api frozen | native | 5 | 0.3 |  |
| api frozen | omni | 3 | 0.0 | -2 s (-45%) |
| metrics down | native | 3 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-34%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*