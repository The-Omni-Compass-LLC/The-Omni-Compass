# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.521 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 489.9 | 414.5 |
| response time (ms), 95th percentile | 2041 | 1924 |
| response time (ms), 99th percentile | 5103 | 4966 |
| time over the response line (% of samples) | 22.96 | 20.75 |
| failed requests (%) | 2.784 | 3.189 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.47 | 0.6183 |
| utilisation (used / allocatable) | 0.09656 | 0.09571 |
| CPU used (cores), mean | 2.317 | 2.297 |
| Omni's own CPU (cores), mean | 0 | 0.01057 |
| CPU used with Omni's own (cores), mean | 2.317 | 2.308 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300 | 303 |
| HPA replicas, mean | 15.27 | 15.36 |
| pods started | 4.1 | 4.1 |
| pod start wait, total (s) | 8 | 8.9 |
| pod start wait, mean (s) | 1.795 | 1.967 |
| host CPU busy, the real machine under kind (%) | 66.32 | 66.61 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 254.3 | 236.8 |
| second app: response time (ms), 99th percentile | 2045 | 1744 |
| second app: time over the response line (% of samples) | 14 | 13.98 |
| second app: failed requests (%) | 12.13 | 12.45 |

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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.432e-15 to +1.073e-17 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.521 | +0.2% | +0.0003041 to +0.007029 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.8 | +0.1% | -0.2644 to +0.7626 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.8 | +0.1% | -0.2644 to +0.7626 | no |
| response time (ms), mean | 489.9 | 414.5 | -15.4% | -131.3 to -19.42 | yes: GAIN |
| response time (ms), 95th percentile | 2041 | 1924 | -5.7% | -442.7 to +210.3 | no |
| response time (ms), 99th percentile | 5103 | 4966 | -2.7% | -1050 to +775.6 | no |
| time over the response line (% of samples) | 22.96 | 20.75 | -9.6% | -3.443 to -0.9712 | yes: GAIN |
| failed requests (%) | 2.784 | 3.189 | +14.5% | -0.6271 to +1.437 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.2 | -1.2% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.7 | +34.7 (native is 0) | +32.54 to +36.86 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.47 | 0.6183 | +31.6% | -0.5542 to +0.8509 | no |
| utilisation (used / allocatable) | 0.09656 | 0.09571 | -0.9% | -0.002903 to +0.001207 | no |
| CPU used (cores), mean | 2.317 | 2.297 | -0.9% | -0.06968 to +0.02897 | no |
| Omni's own CPU (cores), mean | 0 | 0.01057 | +0.0106 (native is 0) | +0.009348 to +0.01179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.317 | 2.308 | -0.4% | -0.05937 to +0.03979 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 300 | 303 | +1.0% | -3.302 to +9.362 | no |
| HPA replicas, mean | 15.27 | 15.36 | +0.5% | -0.206 to +0.3738 | no |
| pods started | 4.1 | 4.1 | +0.0% | -1.168 to +1.168 | no |
| pod start wait, total (s) | 8 | 8.9 | +11.3% | -3.358 to +5.158 | no |
| pod start wait, mean (s) | 1.795 | 1.967 | +9.6% | -0.3712 to +0.7145 | no |
| host CPU busy, the real machine under kind (%) | 66.32 | 66.61 | +0.4% | -0.6191 to +1.196 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 254.3 | 236.8 | -6.9% | -69.75 to +34.79 | no |
| second app: response time (ms), 99th percentile | 2045 | 1744 | -14.7% | -1515 to +913.2 | no |
| second app: time over the response line (% of samples) | 14 | 13.98 | -0.2% | -0.6928 to +0.6485 | no |
| second app: failed requests (%) | 12.13 | 12.45 | +2.6% | -0.274 to +0.9069 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*