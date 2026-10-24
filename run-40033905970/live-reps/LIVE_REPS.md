# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.917 |
| node-hours | 1.49 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.3 | 165 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.7 | 163.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 209.6 | 142.6 |
| response time (ms), 95th percentile | 390 | 187.9 |
| response time (ms), 99th percentile | 1229 | 1011 |
| time over the response line (% of samples) | 8.045 | 5.949 |
| failed requests (%) | 5.149 | 4.393 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 5.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 1.05 |
| utilisation (used / allocatable) | 0.0706 | 0.06942 |
| CPU used (cores), mean | 1.671 | 1.643 |
| Omni's own CPU (cores), mean | 0 | 0.01029 |
| CPU used with Omni's own (cores), mean | 1.671 | 1.653 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.5 | 404.7 |
| HPA replicas, mean | 8.631 | 10.43 |
| pods started | 5 | 6.1 |
| pod start wait, total (s) | 16.3 | 19.8 |
| pod start wait, mean (s) | 3.27 | 3.052 |
| host CPU busy, the real machine under kind (%) | 48.31 | 47.66 |
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
| worker nodes in service, mean | 5.917 | 5.917 | -0.0% | -0.008605 to +0.00795 | no |
| node-hours | 1.49 | 1.49 | +0.0% | -0.00534 to +0.005507 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.3 | 165 | -0.1% | -0.7991 to +0.3553 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.7 | 163.5 | -0.1% | -0.8191 to +0.3628 | no |
| response time (ms), mean | 209.6 | 142.6 | -32.0% | -117.5 to -16.51 | yes: GAIN |
| response time (ms), 95th percentile | 390 | 187.9 | -51.8% | -264.7 to -139.5 | yes: GAIN |
| response time (ms), 99th percentile | 1229 | 1011 | -17.7% | -1034 to +599.4 | no |
| time over the response line (% of samples) | 8.045 | 5.949 | -26.1% | -3.036 to -1.156 | yes: GAIN |
| failed requests (%) | 5.149 | 4.393 | -14.7% | -1.029 to -0.4834 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 5.7 | -16.2% | -1.726 to -0.4737 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.4 | +28.4 (native is 0) | +23.58 to +33.22 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 1.05 | +556.2% | +0.2633 to +1.517 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0706 | 0.06942 | -1.7% | -0.002548 to +0.0002009 | no |
| CPU used (cores), mean | 1.671 | 1.643 | -1.7% | -0.06111 to +0.004971 | no |
| Omni's own CPU (cores), mean | 0 | 0.01029 | +0.0103 (native is 0) | +0.008835 to +0.01174 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.671 | 1.653 | -1.1% | -0.05027 to +0.01471 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.5 | 404.7 | +1.0% | -3.507 to +11.9 | no |
| HPA replicas, mean | 8.631 | 10.43 | +20.8% | +0.3168 to +3.275 | yes: power given |
| pods started | 5 | 6.1 | +22.0% | -0.4249 to +2.625 | no |
| pod start wait, total (s) | 16.3 | 19.8 | +21.5% | -24.79 to +31.79 | no |
| pod start wait, mean (s) | 3.27 | 3.052 | -6.7% | -5.091 to +4.655 | no |
| host CPU busy, the real machine under kind (%) | 48.31 | 47.66 | -1.3% | -1.488 to +0.1947 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 62 | 14.2 |  |
| machine down | omni | 45 | 10.7 | -17 s (-28%) |
| spike | native | 259 | 63.1 |  |
| spike | omni | 254 | 59.3 | -5 s (-2%) |
| runaway pod started | native | 116 | 12.0 |  |
| runaway pod started | omni | 86 | 7.5 | -31 s (-26%) |
| probe blind | native | 66 | 0.4 |  |
| probe blind | omni | 54 | 0.1 | -11 s (-17%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*