# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.3 | 173 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.3 | 173 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 556 | 501.9 |
| response time (ms), 95th percentile | 2273 | 2364 |
| response time (ms), 99th percentile | 5474 | 5676 |
| time over the response line (% of samples) | 27.06 | 24.88 |
| failed requests (%) | 3.725 | 3.508 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.147 | 1.612 |
| utilisation (used / allocatable) | 0.1014 | 0.1002 |
| CPU used (cores), mean | 2.434 | 2.404 |
| Omni's own CPU (cores), mean | 0 | 0.01226 |
| CPU used with Omni's own (cores), mean | 2.434 | 2.417 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 288.7 | 291.5 |
| HPA replicas, mean | 15.1 | 15.31 |
| pods started | 5.5 | 3.9 |
| pod start wait, total (s) | 9 | 6.6 |
| pod start wait, mean (s) | 1.65 | 1.617 |
| host CPU busy, the real machine under kind (%) | 70.82 | 70.52 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 250.4 | 255.4 |
| second app: response time (ms), 99th percentile | 1591 | 1396 |
| second app: time over the response line (% of samples) | 15.77 | 15.59 |
| second app: failed requests (%) | 14.25 | 14.25 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.702e-16 to +1.003e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.513 | -0.0% | -0.007055 to +0.006055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.3 | 173 | -0.2% | -1.105 to +0.491 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.3 | 173 | -0.2% | -1.105 to +0.491 | no |
| response time (ms), mean | 556 | 501.9 | -9.7% | -110.3 to +2.11 | no |
| response time (ms), 95th percentile | 2273 | 2364 | +4.0% | -257.7 to +438.9 | no |
| response time (ms), 99th percentile | 5474 | 5676 | +3.7% | -597.3 to +1003 | no |
| time over the response line (% of samples) | 27.06 | 24.88 | -8.0% | -4.206 to -0.1392 | yes: GAIN |
| failed requests (%) | 3.725 | 3.508 | -5.8% | -1.312 to +0.8771 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.8 | -3.3% | -0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 | +39.8 (native is 0) | +27.34 to +52.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.147 | 1.612 | +40.6% | -0.08743 to +1.017 | no |
| utilisation (used / allocatable) | 0.1014 | 0.1002 | -1.2% | -0.002024 to -0.0004241 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.434 | 2.404 | -1.2% | -0.04858 to -0.01018 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01226 | +0.0123 (native is 0) | +0.01144 to +0.01308 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.434 | 2.417 | -0.7% | -0.03614 to +0.001901 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 288.7 | 291.5 | +1.0% | +1.136 to +4.482 | yes, up (shown, not judged) |
| HPA replicas, mean | 15.1 | 15.31 | +1.4% | -0.0724 to +0.4849 | no |
| pods started | 5.5 | 3.9 | -29.1% | -2.728 to -0.4715 | yes: GAIN |
| pod start wait, total (s) | 9 | 6.6 | -26.7% | -5.225 to +0.4252 | no |
| pod start wait, mean (s) | 1.65 | 1.617 | -2.0% | -0.4659 to +0.3992 | no |
| host CPU busy, the real machine under kind (%) | 70.82 | 70.52 | -0.4% | -0.7591 to +0.1585 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 250.4 | 255.4 | +2.0% | -28.4 to +38.45 | no |
| second app: response time (ms), 99th percentile | 1591 | 1396 | -12.2% | -766 to +377 | no |
| second app: time over the response line (% of samples) | 15.77 | 15.59 | -1.1% | -0.7887 to +0.4313 | no |
| second app: failed requests (%) | 14.25 | 14.25 | -0.0% | -0.3504 to +0.3443 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*