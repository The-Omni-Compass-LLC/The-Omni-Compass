# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.511 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 508.9 | 506.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.9 | 506.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 236.9 | 132.3 |
| response time (ms), 95th percentile | 656.5 | 252.9 |
| response time (ms), 99th percentile | 2191 | 1541 |
| time over the response line (% of samples) | 14.25 | 7.992 |
| failed requests (%) | 7.252 | 6.25 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.2 | 14.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4483 | 0.45 |
| utilisation (used / allocatable) | 0.09036 | 0.08717 |
| CPU used (cores), mean | 2.169 | 2.092 |
| Omni's own CPU (cores), mean | 0 | 0.00754 |
| CPU used with Omni's own (cores), mean | 2.169 | 2.1 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 339.4 | 357.1 |
| HPA replicas, mean | 9.362 | 9.176 |
| pods started | 5.2 | 5.4 |
| pod start wait, total (s) | 18.3 | 17.2 |
| pod start wait, mean (s) | 3.153 | 2.783 |
| host CPU busy, the real machine under kind (%) | 61.2 | 59.32 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.046e-16 to +1.193e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.511 | 4.512 | +0.0% | -0.00771 to +0.00971 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 508.9 | 506.9 | -0.4% | -3.218 to -0.7136 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.9 | 506.9 | -0.4% | -3.218 to -0.7136 | yes: GAIN |
| response time (ms), mean | 236.9 | 132.3 | -44.1% | -140.8 to -68.31 | yes: GAIN |
| response time (ms), 95th percentile | 656.5 | 252.9 | -61.5% | -508 to -299.1 | yes: GAIN |
| response time (ms), 99th percentile | 2191 | 1541 | -29.7% | -1352 to +51.85 | no |
| time over the response line (% of samples) | 14.25 | 7.992 | -43.9% | -8.92 to -3.604 | yes: GAIN |
| failed requests (%) | 7.252 | 6.25 | -13.8% | -1.911 to -0.09356 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.2 | 14.5 | -34.7% | -9.421 to -5.979 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.9 | +29.9 (native is 0) | +21.51 to +38.29 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4483 | 0.45 | +0.4% | -0.1815 to +0.1849 | no |
| utilisation (used / allocatable) | 0.09036 | 0.08717 | -3.5% | -0.004602 to -0.001782 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.169 | 2.092 | -3.5% | -0.1104 to -0.04276 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00754 | +0.00754 (native is 0) | +0.006157 to +0.008923 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.169 | 2.1 | -3.2% | -0.1042 to -0.03397 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 339.4 | 357.1 | +5.2% | +5.437 to +30.07 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.362 | 9.176 | -2.0% | -0.5049 to +0.1345 | no |
| pods started | 5.2 | 5.4 | +3.8% | -1.374 to +1.774 | no |
| pod start wait, total (s) | 18.3 | 17.2 | -6.0% | -5.68 to +3.48 | no |
| pod start wait, mean (s) | 3.153 | 2.783 | -11.7% | -0.7742 to +0.03409 | no |
| host CPU busy, the real machine under kind (%) | 61.2 | 59.32 | -3.1% | -2.841 to -0.9201 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 25.2 |  |  | 10 |
| compass | 35.4 | +40.5% | +8.1 to +12.3 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*