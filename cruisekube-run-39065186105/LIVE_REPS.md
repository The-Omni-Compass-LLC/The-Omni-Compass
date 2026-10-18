# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.872 | 6 |
| node-hours | 1.479 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 163.2 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.8 | 161.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 73.37 | 73.97 |
| response time (ms), 95th percentile | 111.7 | 112.9 |
| response time (ms), 99th percentile | 128.8 | 127.8 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.08167 |
| utilisation (used / allocatable) | 0.0459 | 0.04625 |
| CPU used (cores), mean | 1.077 | 1.11 |
| Omni's own CPU (cores), mean | 0 | 0.00836 |
| CPU used with Omni's own (cores), mean | 1.077 | 1.118 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 602.7 | 582.3 |
| HPA replicas, mean | 2.794 | 2.927 |
| pods started | 1.1 | 1.7 |
| pod start wait, total (s) | 2.9 | 6.6 |
| pod start wait, mean (s) | 2.3 | 3.333 |
| host CPU busy, the real machine under kind (%) | 34.25 | 34.78 |
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

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.872 | 6 | +2.2% | -0.1616 to +0.4177 | no |
| node-hours | 1.479 | 1.519 | +2.7% | -0.03363 to +0.114 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 163.2 | 161.5 | -1.0% | -7.119 to +3.783 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.8 | 161.5 | +0.5% | +0.2971 to +1.218 | yes: power given |
| response time (ms), mean | 73.37 | 73.97 | +0.8% | -0.8752 to +2.072 | no |
| response time (ms), 95th percentile | 111.7 | 112.9 | +1.1% | -0.1709 to +2.67 | no |
| response time (ms), 99th percentile | 128.8 | 127.8 | -0.8% | -7.031 to +4.991 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.08167 | -3.9% | -0.1903 to +0.1836 | no |
| utilisation (used / allocatable) | 0.0459 | 0.04625 | +0.8% | -0.001086 to +0.00179 | no |
| CPU used (cores), mean | 1.077 | 1.11 | +3.1% | -0.05358 to +0.1197 | no |
| Omni's own CPU (cores), mean | 0 | 0.00836 | +0.00836 (native is 0) | +0.007446 to +0.009274 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.077 | 1.118 | +3.8% | -0.04557 to +0.1285 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 602.7 | 582.3 | -3.4% | -68.25 to +27.3 | no |
| HPA replicas, mean | 2.794 | 2.927 | +4.8% | -0.05499 to +0.3213 | no |
| pods started | 1.1 | 1.7 | +54.5% | +0.09985 to +1.1 | yes: power given |
| pod start wait, total (s) | 2.9 | 6.6 | +127.6% | +0.1147 to +7.285 | yes: LOSS |
| pod start wait, mean (s) | 2.3 | 3.333 | +44.9% | -1.31 to +3.377 | no |
| host CPU busy, the real machine under kind (%) | 34.25 | 34.78 | +1.6% | -0.01177 to +1.087 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*