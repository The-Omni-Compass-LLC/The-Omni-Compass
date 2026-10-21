# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.25 |
| node-hours | 2.512 | 2.197 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 250.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 577.4 | 520 |
| response time (ms), 95th percentile | 3301 | 3298 |
| response time (ms), 99th percentile | 4817 | 4837 |
| time over the response line (% of samples) | 17.2 | 16.81 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 199 | 204.9 |
| utilisation (used / allocatable) | 0.06633 | 0.07544 |
| CPU used (cores), mean | 1.592 | 1.584 |
| Omni's own CPU (cores), mean | 0 | 0.02389 |
| CPU used with Omni's own (cores), mean | 1.592 | 1.608 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 419.8 | 380.8 |
| HPA replicas, mean | 2.081 | 2.162 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 45.58 | 46.35 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 623.4 | 626.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.781 |

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
| worker nodes in service, mean | 6 | 5.25 | -12.5% | -1.229 to -0.2711 | yes: GAIN |
| node-hours | 2.512 | 2.197 | -12.5% | -0.5196 to -0.1108 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.3 | -0.1% | -1.118 to +0.6624 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 250.8 | -8.7% | -39.26 to -8.296 | yes: GAIN |
| response time (ms), mean | 577.4 | 520 | -9.9% | -79.64 to -35.05 | yes: GAIN |
| response time (ms), 95th percentile | 3301 | 3298 | -0.1% | -113.4 to +107.6 | no |
| response time (ms), 99th percentile | 4817 | 4837 | +0.4% | -268.2 to +308.4 | no |
| time over the response line (% of samples) | 17.2 | 16.81 | -2.3% | -0.9727 to +0.1845 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 | +11.4 (native is 0) | +10.8 to +12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 199 | 204.9 | +3.0% | -0.2891 to +12.05 | no |
| utilisation (used / allocatable) | 0.06633 | 0.07544 | +13.7% | +0.003014 to +0.0152 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.592 | 1.584 | -0.5% | -0.04187 to +0.02646 | no |
| Omni's own CPU (cores), mean | 0 | 0.02389 | +0.0239 (native is 0) | +0.01982 to +0.02796 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.592 | 1.608 | +1.0% | -0.01905 to +0.05142 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 419.8 | 380.8 | -9.3% | -72.46 to -5.443 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.081 | 2.162 | +3.9% | -0.07933 to +0.2403 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.631 to +1.631 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.631 to +1.631 | no |
| host CPU busy, the real machine under kind (%) | 45.58 | 46.35 | +1.7% | +0.5459 to +0.9931 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 623.4 | 626.9 | +0.6% | -0.407 to +7.407 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.781 | -20.3% | -1.882 to -0.5554 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*