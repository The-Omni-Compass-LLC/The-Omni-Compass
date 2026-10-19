# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.028 |
| node-hours | 2.514 | 2.107 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 241.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 446.6 | 396.4 |
| response time (ms), 95th percentile | 2688 | 2692 |
| response time (ms), 99th percentile | 4265 | 4169 |
| time over the response line (% of samples) | 14.94 | 14.26 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 175.7 | 172.9 |
| utilisation (used / allocatable) | 0.05859 | 0.06965 |
| CPU used (cores), mean | 1.406 | 1.387 |
| Omni's own CPU (cores), mean | 0 | 0.02038 |
| CPU used with Omni's own (cores), mean | 1.406 | 1.407 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 418.2 |
| HPA replicas, mean | 1.971 | 2.203 |
| pods started | 0.3 | 0.5 |
| pod start wait, total (s) | 2.9 | 0.6 |
| pod start wait, mean (s) | 1.75 | 0.45 |
| host CPU busy, the real machine under kind (%) | 39.99 | 40.36 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 542.7 | 539.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.511 |

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
| worker nodes in service, mean | 6 | 5.028 | -16.2% | -1.501 to -0.4434 | yes: GAIN |
| node-hours | 2.514 | 2.107 | -16.2% | -0.6299 to -0.184 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.8 | -0.0% | -1.115 to +0.8893 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 241.3 | -11.3% | -47.29 to -14 | yes: GAIN |
| response time (ms), mean | 446.6 | 396.4 | -11.2% | -64.59 to -35.86 | yes: GAIN |
| response time (ms), 95th percentile | 2688 | 2692 | +0.1% | -141.8 to +149.7 | no |
| response time (ms), 99th percentile | 4265 | 4169 | -2.2% | -239.7 to +49.08 | no |
| time over the response line (% of samples) | 14.94 | 14.26 | -4.6% | -1.274 to -0.09063 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.3 | -1.1% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.8 | +12.8 (native is 0) | +11.15 to +14.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 175.7 | 172.9 | -1.6% | -9.782 to +4.189 | no |
| utilisation (used / allocatable) | 0.05859 | 0.06965 | +18.9% | +0.003648 to +0.01847 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.406 | 1.387 | -1.4% | -0.0588 to +0.02065 | no |
| Omni's own CPU (cores), mean | 0 | 0.02038 | +0.0204 (native is 0) | +0.01647 to +0.02429 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.407 | +0.1% | -0.03869 to +0.04129 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 418.2 | -10.7% | -87.93 to -12.59 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.971 | 2.203 | +11.7% | -0.0472 to +0.5095 | no |
| pods started | 0.3 | 0.5 | +66.7% | -0.4573 to +0.8573 | no |
| pod start wait, total (s) | 2.9 | 0.6 | -79.3% | -7.514 to +2.914 | no |
| pod start wait, mean (s) | 1.75 | 0.45 | -74.3% | -4.056 to +1.456 | no |
| host CPU busy, the real machine under kind (%) | 39.99 | 40.36 | +0.9% | -0.3011 to +1.025 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 542.7 | 539.8 | -0.5% | -12.16 to +6.356 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.511 | -24.8% | -2.258 to -0.7196 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*