# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.504 |
| node-hours | 2.514 | 1.888 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 224.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 145.7 | 106 |
| response time (ms), 95th percentile | 327.4 | 318.1 |
| response time (ms), 99th percentile | 419.3 | 430.5 |
| time over the response line (% of samples) | 0.7367 | 0.8459 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 1.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.492 | 7.287 |
| utilisation (used / allocatable) | 0.05748 | 0.07617 |
| CPU used (cores), mean | 1.379 | 1.354 |
| Omni's own CPU (cores), mean | 0 | 0.01909 |
| CPU used with Omni's own (cores), mean | 1.379 | 1.373 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.6 | 395.4 |
| HPA replicas, mean | 2.183 | 2.13 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.1 | 0.1 |
| pod start wait, mean (s) | 0.1 | 0.1 |
| host CPU busy, the real machine under kind (%) | 38.86 | 39.88 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 720.8 | 720.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.337 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.025 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.1 |
| queue: job turnaround, submitted to done, mean (s) | 26.58 | 26.89 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 4.504 | -24.9% | -2.113 to -0.8791 | yes: GAIN |
| node-hours | 2.514 | 1.888 | -24.9% | -0.8865 to -0.3654 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 | -0.1% | -1.015 to +0.7247 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 224.3 | -17.4% | -66.93 to -27.35 | yes: GAIN |
| response time (ms), mean | 145.7 | 106 | -27.3% | -50.32 to -29.13 | yes: GAIN |
| response time (ms), 95th percentile | 327.4 | 318.1 | -2.8% | -36.35 to +17.76 | no |
| response time (ms), 99th percentile | 419.3 | 430.5 | +2.7% | -1.705 to +24.09 | no |
| time over the response line (% of samples) | 0.7367 | 0.8459 | +14.8% | -0.1707 to +0.3892 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 1.7 | +0.0% | -0.754 to +0.754 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.7 | +38.7 (native is 0) | +30.61 to +46.79 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.492 | 7.287 | -2.7% | -2.582 to +2.172 | no |
| utilisation (used / allocatable) | 0.05748 | 0.07617 | +32.5% | +0.009816 to +0.02756 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.379 | 1.354 | -1.9% | -0.08406 to +0.03238 | no |
| Omni's own CPU (cores), mean | 0 | 0.01909 | +0.0191 (native is 0) | +0.01766 to +0.02052 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.379 | 1.373 | -0.5% | -0.06528 to +0.05178 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.6 | 395.4 | -16.7% | -119.5 to -38.96 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.183 | 2.13 | -2.4% | -0.2275 to +0.1219 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, mean (s) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| host CPU busy, the real machine under kind (%) | 38.86 | 39.88 | +2.6% | +0.7776 to +1.255 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 720.8 | 720.4 | -0.1% | -1.477 to +0.6769 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.337 | -44.4% | -3.687 to -1.64 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.025 | +20.0% | -0.02547 to +0.03381 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 26.58 | 26.89 | +1.2% | +0.1898 to +0.4352 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*