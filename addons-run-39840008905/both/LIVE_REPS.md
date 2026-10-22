# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 161.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 133.1 | 85.5 |
| response time (ms), 95th percentile | 267.4 | 131 |
| response time (ms), 99th percentile | 384.1 | 183.9 |
| time over the response line (% of samples) | 0.3475 | 0.01227 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.05333 |
| utilisation (used / allocatable) | 0.03669 | 0.04834 |
| CPU used (cores), mean | 0.8805 | 1.16 |
| Omni's own CPU (cores), mean | 0 | 0.04364 |
| CPU used with Omni's own (cores), mean | 0.8805 | 1.204 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716 | 558.2 |
| HPA replicas, mean | 8.905 | 10.62 |
| pods started | 4.8 | 7.2 |
| pod start wait, total (s) | 7.1 | 10.8 |
| pod start wait, mean (s) | 1.48 | 1.509 |
| host CPU busy, the real machine under kind (%) | 27.59 | 36.86 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.421e-16 to +1.13e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.516 | +0.1% | -0.00646 to +0.00846 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 161.4 | +1.7% | +1.836 to +3.68 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 161.4 | +1.7% | +1.836 to +3.68 | yes: power given |
| response time (ms), mean | 133.1 | 85.5 | -35.8% | -61.88 to -33.41 | yes: GAIN |
| response time (ms), 95th percentile | 267.4 | 131 | -51.0% | -165.9 to -106.8 | yes: GAIN |
| response time (ms), 99th percentile | 384.1 | 183.9 | -52.1% | -236.7 to -163.6 | yes: GAIN |
| time over the response line (% of samples) | 0.3475 | 0.01227 | -96.5% | -0.5734 to -0.09709 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.7 | +62.7 (native is 0) | +17.97 to +107.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2083 | 0.05333 | -74.4% | -0.45 to +0.14 | no |
| utilisation (used / allocatable) | 0.03669 | 0.04834 | +31.8% | +0.008875 to +0.01444 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8805 | 1.16 | +31.8% | +0.213 to +0.3465 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04364 | +0.0436 (native is 0) | +0.03066 to +0.05662 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8805 | 1.204 | +36.7% | +0.2489 to +0.3978 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716 | 558.2 | -22.0% | -181.5 to -134.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.905 | 10.62 | +19.3% | +0.9288 to +2.507 | yes: power given |
| pods started | 4.8 | 7.2 | +50.0% | +0.9225 to +3.878 | yes: power given |
| pod start wait, total (s) | 7.1 | 10.8 | +52.1% | +0.3781 to +7.022 | yes: LOSS |
| pod start wait, mean (s) | 1.48 | 1.509 | +1.9% | -0.4493 to +0.5064 | no |
| host CPU busy, the real machine under kind (%) | 27.59 | 36.86 | +33.6% | +6.87 to +11.66 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*