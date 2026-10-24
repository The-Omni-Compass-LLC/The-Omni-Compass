# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1392 | 1392 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1392 | 1392 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 480 | 311 |
| response time (ms), 95th percentile | 1880 | 1105 |
| response time (ms), 99th percentile | 5046 | 4756 |
| time over the response line (% of samples) | 34.27 | 22.9 |
| failed requests (%) | 20.03 | 17.19 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 84.33 | 69 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 46.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.989 | 2.506 |
| utilisation (used / allocatable) | 0.1114 | 0.1101 |
| CPU used (cores), mean | 2.673 | 2.643 |
| Omni's own CPU (cores), mean | 0 | 0.009467 |
| CPU used with Omni's own (cores), mean | 2.673 | 2.653 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.5 | 303.8 |
| HPA replicas, mean | 9.892 | 12.99 |
| pods started | 7 | 13.67 |
| pod start wait, total (s) | 11 | 23.33 |
| pod start wait, mean (s) | 1.545 | 1.81 |
| host CPU busy, the real machine under kind (%) | 75.22 | 75.19 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 12.01 | 12.02 | +0.1% | −0.0016 to +0.0283 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1392 | 1392 | −0.0% | −4.8592 to +4.0995 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1392 | 1392 | −0.0% | −4.8592 to +4.0995 | no |
| response time (ms), mean | 480 | 311 | −35.2% | −431.5595 to +93.6222 | no |
| response time (ms), 95th percentile | 1880 | 1105 | −41.2% | −2029.1931 to +477.9331 | no |
| response time (ms), 99th percentile | 5046 | 4756 | −5.8% | −815.4362 to +234.5236 | no |
| time over the response line (% of samples) | 34.27 | 22.9 | −33.2% | −33.3094 to +10.5681 | no |
| failed requests (%) | 20.03 | 17.19 | −14.2% | −9.3226 to +3.6398 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 84.33 | 69 | −18.2% | −19.1282 to −11.5384 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.7 | +105.667 (native is 0) | +94.4642 to +116.8692 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.989 | 2.506 | −16.2% | −1.3479 to +0.3812 | no |
| utilisation (used / allocatable) | 0.1114 | 0.1101 | −1.1% | −0.0035 to +0.0010 | no |
| CPU used (cores), mean | 2.673 | 2.643 | −1.1% | −0.0833 to +0.0244 | no |
| Omni's own CPU (cores), mean | 0 | 0.009467 | +0.009 (native is 0) | +0.0039 to +0.0150 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.673 | 2.653 | −0.7% | −0.0750 to +0.0350 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.5 | 303.8 | +1.5% | −7.7385 to +16.4291 | no |
| HPA replicas, mean | 9.892 | 12.99 | +31.3% | −5.6634 to +11.8520 | no |
| pods started | 7 | 13.67 | +95.2% | −0.5050 to +13.8383 | no |
| pod start wait, total (s) | 11 | 23.33 | +112.1% | +8.5384 to +16.1282 | yes: LOSS |
| pod start wait, mean (s) | 1.545 | 1.81 | +17.1% | −0.9953 to +1.5235 | no |
| host CPU busy, the real machine under kind (%) | 75.22 | 75.19 | −0.0% | −1.1702 to +1.1077 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.007 | 120 | 100.0% | 0 | 1.01 | yes |
| omni | 2 | long |  |  |  | 0 | 1.035 | 120 | 100.0% | 0 | 1.15 | yes |
| omni | 3 | long |  |  |  | 0 | 1.015 | 120 | 100.0% | 0 | 1.09 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*