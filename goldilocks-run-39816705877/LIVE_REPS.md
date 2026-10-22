# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.5 | 76.28 |
| response time (ms), 95th percentile | 293.1 | 116.7 |
| response time (ms), 99th percentile | 428.4 | 155.6 |
| time over the response line (% of samples) | 0.7035 | 0.02439 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.02667 |
| utilisation (used / allocatable) | 0.0328 | 0.04639 |
| CPU used (cores), mean | 0.7872 | 1.113 |
| Omni's own CPU (cores), mean | 0 | 0.0268 |
| CPU used with Omni's own (cores), mean | 0.7872 | 1.14 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.8 | 580.5 |
| HPA replicas, mean | 9.682 | 11.92 |
| pods started | 2.7 | 4.5 |
| pod start wait, total (s) | 3.1 | 7.9 |
| pod start wait, mean (s) | 1.058 | 1.585 |
| host CPU busy, the real machine under kind (%) | 23.73 | 33.79 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.495e-16 to +2.718e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.513 | -0.3% | -0.0129 to +0.00357 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.7 | +1.6% | +1.865 to +3.281 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.7 | +1.6% | +1.865 to +3.281 | yes: power given |
| response time (ms), mean | 137.5 | 76.28 | -44.5% | -79.09 to -43.33 | yes: GAIN |
| response time (ms), 95th percentile | 293.1 | 116.7 | -60.2% | -210.8 to -141.9 | yes: GAIN |
| response time (ms), 99th percentile | 428.4 | 155.6 | -63.7% | -320.6 to -225 | yes: GAIN |
| time over the response line (% of samples) | 0.7035 | 0.02439 | -96.5% | -1.177 to -0.1811 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0 | -100.0% | -1.006 to +0.005799 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 | +48 (native is 0) | +18.97 to +77.03 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.02667 | +6.7% | -0.002103 to +0.005437 | no |
| utilisation (used / allocatable) | 0.0328 | 0.04639 | +41.4% | +0.01028 to +0.0169 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7872 | 1.113 | +41.4% | +0.2468 to +0.4057 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0268 | +0.0268 (native is 0) | +0.02105 to +0.03255 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7872 | 1.14 | +44.8% | +0.2694 to +0.4367 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.8 | 580.5 | -27.1% | -256.1 to -176.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.682 | 11.92 | +23.2% | +0.9646 to +3.52 | yes: power given |
| pods started | 2.7 | 4.5 | +66.7% | -0.2456 to +3.846 | no |
| pod start wait, total (s) | 3.1 | 7.9 | +154.8% | +1.003 to +8.597 | yes: LOSS |
| pod start wait, mean (s) | 1.058 | 1.585 | +49.8% | +0.1984 to +0.8547 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.73 | 33.79 | +42.4% | +7.589 to +12.54 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*