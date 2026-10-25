# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.52 | 1.51 | 1.519 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.4 | 159.5 | 160.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.4 | 159.5 | 160.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 137.9 | 140.3 | 135.2 | 140.8 |
| response time (ms), 95th percentile | 277.5 | 279.2 | 273.2 | 281.7 |
| response time (ms), 99th percentile | 388.3 | 386.2 | 390.4 | 387.5 |
| time over the response line (% of samples) | 0.2439 | 0.2706 | 0.3703 | 0.2961 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 2 | 2.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.135 | 0.02667 | 0.36 |
| utilisation (used / allocatable) | 0.0378 | 0.04228 | 0.03825 | 0.0428 |
| CPU used (cores), mean | 0.9072 | 1.015 | 0.9181 | 1.027 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00567 | 0.00975 |
| CPU used with Omni's own (cores), mean | 0.9072 | 1.015 | 0.9238 | 1.037 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.4 | 626 | 688.5 | 619.3 |
| HPA replicas, mean | 8.974 | 8.872 | 10.19 | 10.21 |
| pods started | 4.3 | 4.8 | 7.3 | 7.2 |
| pod start wait, total (s) | 6.5 | 6.6 | 11.4 | 10.6 |
| pod start wait, mean (s) | 1.347 | 1.382 | 1.519 | 1.441 |
| host CPU busy, the real machine under kind (%) | 26.59 | 30.67 | 27.06 | 31.55 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 3 of 10 repetitions (repetitions 3, 5, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.519 | +0.6% | +0.0044 to +0.0149 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 160.5 | +0.7% | +0.5385 to +1.7256 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 160.5 | +0.7% | +0.5385 to +1.7256 | yes: power given |
| response time (ms), mean | 140.3 | 140.8 | +0.4% | −4.0475 to +5.0667 | no |
| response time (ms), 95th percentile | 279.2 | 281.7 | +0.9% | −11.9814 to +16.8484 | no |
| response time (ms), 99th percentile | 386.2 | 387.5 | +0.3% | −19.2854 to +21.9152 | no |
| time over the response line (% of samples) | 0.2706 | 0.2961 | +9.4% | −0.1415 to +0.1925 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.4 | +2.400 (native is 0) | +0.9615 to +3.8385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.135 | 0.36 | +166.7% | −0.1375 to +0.5875 | no |
| utilisation (used / allocatable) | 0.04228 | 0.0428 | +1.2% | −0.0002 to +0.0012 | no |
| CPU used (cores), mean | 1.015 | 1.027 | +1.2% | −0.0037 to +0.0284 | no |
| Omni's own CPU (cores), mean | 0 | 0.00975 | +0.010 (native is 0) | +0.0079 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.015 | 1.037 | +2.2% | +0.0049 to +0.0393 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 626 | 619.3 | −1.1% | −15.9327 to +2.6716 | no |
| HPA replicas, mean | 8.872 | 10.21 | +15.1% | +0.6164 to +2.0653 | yes: power given |
| pods started | 4.8 | 7.2 | +50.0% | +1.0854 to +3.7146 | yes: power given |
| pod start wait, total (s) | 6.6 | 10.6 | +60.6% | +0.4795 to +7.5205 | yes: LOSS |
| pod start wait, mean (s) | 1.382 | 1.441 | +4.3% | −0.2737 to +0.3927 | no |
| host CPU busy, the real machine under kind (%) | 30.67 | 31.55 | +2.9% | +0.4331 to +1.3320 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.51 | −0.7% | −0.0140 to −0.0067 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.4 | −0.0% | −0.5923 to +0.4751 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.4 | −0.0% | −0.5923 to +0.4751 | no |
| response time (ms), mean | 137.9 | 140.3 | +1.7% | −1.3282 to +6.0734 | no |
| response time (ms), 95th percentile | 277.5 | 279.2 | +0.6% | −9.9858 to +13.4578 | no |
| response time (ms), 99th percentile | 388.3 | 386.2 | −0.5% | −19.8499 to +15.6505 | no |
| time over the response line (% of samples) | 0.2439 | 0.2706 | +10.9% | −0.1230 to +0.1764 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.135 | +30.6% | −0.1932 to +0.2565 | no |
| utilisation (used / allocatable) | 0.0378 | 0.04228 | +11.9% | +0.0038 to +0.0051 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9072 | 1.015 | +11.9% | +0.0922 to +0.1230 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9072 | 1.015 | +11.9% | +0.0922 to +0.1230 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.4 | 626 | −10.0% | −78.8912 to −59.9151 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.974 | 8.872 | −1.1% | −0.3481 to +0.1443 | no |
| pods started | 4.3 | 4.8 | +11.6% | −0.7274 to +1.7274 | no |
| pod start wait, total (s) | 6.5 | 6.6 | +1.5% | −1.9909 to +2.1909 | no |
| pod start wait, mean (s) | 1.347 | 1.382 | +2.6% | −0.3707 to +0.4407 | no |
| host CPU busy, the real machine under kind (%) | 26.59 | 30.67 | +15.3% | +3.5453 to +4.6091 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.519 | −0.1% | −0.0062 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.5 | +0.0% | −0.5075 to +0.5946 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.5 | +0.0% | −0.5075 to +0.5946 | no |
| response time (ms), mean | 137.9 | 135.2 | −1.9% | −6.4231 to +1.0932 | no |
| response time (ms), 95th percentile | 277.5 | 273.2 | −1.6% | −14.6344 to +6.0114 | no |
| response time (ms), 99th percentile | 388.3 | 390.4 | +0.6% | −14.7043 to +18.9903 | no |
| time over the response line (% of samples) | 0.2439 | 0.3703 | +51.8% | +0.0118 to +0.2410 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.02667 | −74.2% | −0.2530 to +0.0996 | no |
| utilisation (used / allocatable) | 0.0378 | 0.03825 | +1.2% | −0.0001 to +0.0011 | no |
| CPU used (cores), mean | 0.9072 | 0.9181 | +1.2% | −0.0035 to +0.0253 | no |
| Omni's own CPU (cores), mean | 0 | 0.00567 | +0.006 (native is 0) | +0.0049 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9072 | 0.9238 | +1.8% | +0.0018 to +0.0314 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.4 | 688.5 | −1.0% | −17.7083 to +3.8708 | no |
| HPA replicas, mean | 8.974 | 10.19 | +13.6% | +0.5095 to +1.9287 | yes: power given |
| pods started | 4.3 | 7.3 | +69.8% | +0.7130 to +5.2870 | yes: power given |
| pod start wait, total (s) | 6.5 | 11.4 | +75.4% | +0.4208 to +9.3792 | yes: LOSS |
| pod start wait, mean (s) | 1.347 | 1.519 | +12.8% | −0.2911 to +0.6349 | no |
| host CPU busy, the real machine under kind (%) | 26.59 | 27.06 | +1.8% | +0.1175 to +0.8309 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.51 | 1.519 | +0.6% | +0.0033 to +0.0154 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.5 | +0.1% | −0.5720 to +0.7763 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.5 | +0.1% | −0.5720 to +0.7763 | no |
| response time (ms), mean | 140.3 | 135.2 | −3.6% | −8.9620 to −1.1132 | yes: GAIN |
| response time (ms), 95th percentile | 279.2 | 273.2 | −2.2% | −19.5096 to +7.4146 | no |
| response time (ms), 99th percentile | 386.2 | 390.4 | +1.1% | −9.3331 to +17.8185 | no |
| time over the response line (% of samples) | 0.2706 | 0.3703 | +36.8% | −0.0420 to +0.2414 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.135 | 0.02667 | −80.2% | −0.2429 to +0.0262 | no |
| utilisation (used / allocatable) | 0.04228 | 0.03825 | −9.5% | −0.0043 to −0.0038 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.015 | 0.9181 | −9.5% | −0.1022 to −0.0912 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00567 | +0.006 (native is 0) | +0.0049 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.015 | 0.9238 | −9.0% | −0.0966 to −0.0855 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 626 | 688.5 | +10.0% | +56.2784 to +68.6904 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.872 | 10.19 | +14.9% | +0.5947 to +2.0473 | yes: power given |
| pods started | 4.8 | 7.3 | +52.1% | +0.8741 to +4.1259 | yes: power given |
| pod start wait, total (s) | 6.6 | 11.4 | +72.7% | +1.3480 to +8.2520 | yes: LOSS |
| pod start wait, mean (s) | 1.382 | 1.519 | +9.9% | −0.1084 to +0.3822 | no |
| host CPU busy, the real machine under kind (%) | 30.67 | 27.06 | −11.7% | −3.9107 to −3.2954 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.519 | −0.0% | −0.0064 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 160.5 | +0.7% | +0.3657 to +1.7812 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 160.5 | +0.7% | +0.3657 to +1.7812 | yes: power given |
| response time (ms), mean | 137.9 | 140.8 | +2.1% | −0.6992 to +6.4636 | no |
| response time (ms), 95th percentile | 277.5 | 281.7 | +1.5% | −7.4920 to +15.8310 | no |
| response time (ms), 99th percentile | 388.3 | 387.5 | −0.2% | −19.9673 to +18.3977 | no |
| time over the response line (% of samples) | 0.2439 | 0.2961 | +21.4% | −0.1430 to +0.2473 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 2.4 | +2.400 (native is 0) | +0.9615 to +3.8385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1033 | 0.36 | +248.4% | −0.0641 to +0.5774 | no |
| utilisation (used / allocatable) | 0.0378 | 0.0428 | +13.2% | +0.0043 to +0.0057 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9072 | 1.027 | +13.2% | +0.1026 to +0.1373 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00975 | +0.010 (native is 0) | +0.0079 to +0.0116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9072 | 1.037 | +14.3% | +0.1108 to +0.1486 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 695.4 | 619.3 | −10.9% | −84.2240 to −67.8434 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.974 | 10.21 | +13.8% | +0.5175 to +1.9603 | yes: power given |
| pods started | 4.3 | 7.2 | +67.4% | +1.1333 to +4.6667 | yes: power given |
| pod start wait, total (s) | 6.5 | 10.6 | +63.1% | +0.8229 to +7.3771 | yes: LOSS |
| pod start wait, mean (s) | 1.347 | 1.441 | +7.0% | −0.2660 to +0.4550 | no |
| host CPU busy, the real machine under kind (%) | 26.59 | 31.55 | +18.7% | +4.2547 to +5.6649 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*