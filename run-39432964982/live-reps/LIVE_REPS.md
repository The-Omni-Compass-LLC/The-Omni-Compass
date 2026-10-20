# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.227 |
| node-hours | 2.519 | 2.192 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 250.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 529.4 | 484.9 |
| response time (ms), 95th percentile | 3054 | 3054 |
| response time (ms), 99th percentile | 4304 | 4307 |
| time over the response line (% of samples) | 17.64 | 16.79 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 197.1 | 200.8 |
| utilisation (used / allocatable) | 0.0635 | 0.0747 |
| CPU used (cores), mean | 1.524 | 1.553 |
| Omni's own CPU (cores), mean | 0 | 0.01949 |
| CPU used with Omni's own (cores), mean | 1.524 | 1.573 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.6 | 386.3 |
| HPA replicas, mean | 2.31 | 2.37 |
| pods started | 0.2 | 0.5 |
| pod start wait, total (s) | 1.3 | 0.6 |
| pod start wait, mean (s) | 1.3 | 0.45 |
| host CPU busy, the real machine under kind (%) | 44.75 | 45.5 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 612.7 | 615.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.759 |

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
| worker nodes in service, mean | 6 | 5.227 | -12.9% | -1.316 to -0.2303 | yes: GAIN |
| node-hours | 2.519 | 2.192 | -13.0% | -0.5551 to -0.09866 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.6 | +0.1% | -0.8028 to +1.378 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 250.3 | -8.8% | -41.36 to -6.719 | yes: GAIN |
| response time (ms), mean | 529.4 | 484.9 | -8.4% | -56.52 to -32.62 | yes: GAIN |
| response time (ms), 95th percentile | 3054 | 3054 | -0.0% | -111.8 to +111.6 | no |
| response time (ms), 99th percentile | 4304 | 4307 | +0.1% | -212.4 to +217.3 | no |
| time over the response line (% of samples) | 17.64 | 16.79 | -4.8% | -1.313 to -0.3848 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 10.4 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 | +11.8 (native is 0) | +11.06 to +12.54 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 197.1 | 200.8 | +1.9% | -1.893 to +9.313 | no |
| utilisation (used / allocatable) | 0.0635 | 0.0747 | +17.6% | +0.004291 to +0.01812 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.553 | +1.9% | -0.02852 to +0.0871 | no |
| Omni's own CPU (cores), mean | 0 | 0.01949 | +0.0195 (native is 0) | +0.0155 to +0.02348 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.573 | +3.2% | -0.009399 to +0.107 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.6 | 386.3 | -10.9% | -76.59 to -18.01 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.31 | 2.37 | +2.6% | -0.3271 to +0.4454 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 1.3 | 0.6 | -53.8% | -2.834 to +1.434 | no |
| pod start wait, mean (s) | 1.3 | 0.45 | -65.4% | -2.859 to +1.159 | no |
| host CPU busy, the real machine under kind (%) | 44.75 | 45.5 | +1.7% | +0.4074 to +1.091 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 612.7 | 615.7 | +0.5% | -3.616 to +9.616 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.759 | -20.7% | -2.091 to -0.3905 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*