# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.337 | 4.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 477.6 | 475.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.6 | 475.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 242.8 | 126.1 |
| response time (ms), 95th percentile | 615.4 | 259 |
| response time (ms), 99th percentile | 1224 | 767.9 |
| time over the response line (% of samples) | 10.53 | 2.865 |
| failed requests (%) | 0.9243 | 0.7805 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.4 | 6.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.365 | 0.9833 |
| utilisation (used / allocatable) | 0.07236 | 0.06989 |
| CPU used (cores), mean | 1.737 | 1.677 |
| Omni's own CPU (cores), mean | 0 | 0.02839 |
| CPU used with Omni's own (cores), mean | 1.737 | 1.706 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.9 | 442.1 |
| HPA replicas, mean | 9.6 | 10.51 |
| pods started | 6.7 | 13.8 |
| pod start wait, total (s) | 11 | 22.1 |
| pod start wait, mean (s) | 1.722 | 1.527 |
| host CPU busy, the real machine under kind (%) | 50.48 | 49.92 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.104e-16 to +7.88e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.337 | 4.335 | -0.0% | -0.00741 to +0.003743 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 477.6 | 475.8 | -0.4% | -2.668 to -0.9177 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.6 | 475.8 | -0.4% | -2.668 to -0.9177 | yes: GAIN |
| response time (ms), mean | 242.8 | 126.1 | -48.0% | -165.1 to -68.16 | yes: GAIN |
| response time (ms), 95th percentile | 615.4 | 259 | -57.9% | -489.9 to -222.9 | yes: GAIN |
| response time (ms), 99th percentile | 1224 | 767.9 | -37.3% | -672.5 to -240 | yes: GAIN |
| time over the response line (% of samples) | 10.53 | 2.865 | -72.8% | -12.43 to -2.897 | yes: GAIN |
| failed requests (%) | 0.9243 | 0.7805 | -15.6% | -0.2836 to -0.004016 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.4 | 6.6 | -64.1% | -18.9 to -4.704 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 65.8 | +65.8 (native is 0) | +43.85 to +87.75 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.365 | 0.9833 | +169.4% | +0.1248 to +1.112 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07236 | 0.06989 | -3.4% | -0.003328 to -0.001607 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.737 | 1.677 | -3.4% | -0.07988 to -0.03857 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02839 | +0.0284 (native is 0) | +0.02241 to +0.03437 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.737 | 1.706 | -1.8% | -0.04738 to -0.0143 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.9 | 442.1 | +3.1% | +9.105 to +17.21 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.6 | 10.51 | +9.5% | -0.574 to +2.403 | no |
| pods started | 6.7 | 13.8 | +106.0% | +2.197 to +12 | yes: power given |
| pod start wait, total (s) | 11 | 22.1 | +100.9% | +0.3548 to +21.85 | yes: LOSS |
| pod start wait, mean (s) | 1.722 | 1.527 | -11.3% | -0.527 to +0.1367 | no |
| host CPU busy, the real machine under kind (%) | 50.48 | 49.92 | -1.1% | -0.9354 to -0.1743 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*