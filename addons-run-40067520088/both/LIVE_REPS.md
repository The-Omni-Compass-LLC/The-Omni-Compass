# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 159.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 159.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 105 | 68.11 |
| response time (ms), 95th percentile | 223 | 103.7 |
| response time (ms), 99th percentile | 330.6 | 134.1 |
| time over the response line (% of samples) | 0.3452 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.16 |
| utilisation (used / allocatable) | 0.03506 | 0.04362 |
| CPU used (cores), mean | 0.8415 | 1.047 |
| Omni's own CPU (cores), mean | 0 | 0.01309 |
| CPU used with Omni's own (cores), mean | 0.8415 | 1.06 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748 | 617.8 |
| HPA replicas, mean | 8.734 | 9.565 |
| pods started | 5 | 6.3 |
| pod start wait, total (s) | 6.3 | 9.2 |
| pod start wait, mean (s) | 1.252 | 1.425 |
| host CPU busy, the real machine under kind (%) | 25.86 | 32.2 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.511 | −0.2% | −0.0122 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 159.9 | +1.1% | +0.3243 to +3.0716 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 159.9 | +1.1% | +0.3243 to +3.0716 | yes: power given |
| response time (ms), mean | 105 | 68.11 | −35.1% | −51.3342 to −22.4827 | yes: GAIN |
| response time (ms), 95th percentile | 223 | 103.7 | −53.5% | −141.6140 to −96.8730 | yes: GAIN |
| response time (ms), 99th percentile | 330.6 | 134.1 | −59.4% | −238.7749 to −154.1403 | yes: GAIN |
| time over the response line (% of samples) | 0.3452 | 0 | −100.0% | −0.6585 to −0.0320 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 | +26.300 (native is 0) | +17.2580 to +35.3420 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.16 | +21.5% | −0.2471 to +0.3038 | no |
| utilisation (used / allocatable) | 0.03506 | 0.04362 | +24.4% | +0.0053 to +0.0118 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8415 | 1.047 | +24.4% | +0.1282 to +0.2826 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01309 | +0.013 (native is 0) | +0.0096 to +0.0166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8415 | 1.06 | +26.0% | +0.1381 to +0.2988 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748 | 617.8 | −17.4% | −163.6813 to −96.7935 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.734 | 9.565 | +9.5% | −0.0384 to +1.7003 | no |
| pods started | 5 | 6.3 | +26.0% | +0.0361 to +2.5639 | yes: power given |
| pod start wait, total (s) | 6.3 | 9.2 | +46.0% | +0.0697 to +5.7303 | yes: LOSS |
| pod start wait, mean (s) | 1.252 | 1.425 | +13.9% | −0.0955 to +0.4426 | no |
| host CPU busy, the real machine under kind (%) | 25.86 | 32.2 | +24.5% | +3.9773 to +8.6883 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*