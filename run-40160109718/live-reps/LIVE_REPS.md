# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.513 | 1.516 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.5 | 158.8 | 159.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.5 | 158.8 | 159.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 114.6 | 117.8 | 114.3 | 117.1 |
| response time (ms), 95th percentile | 237.3 | 243.9 | 233.6 | 239.9 |
| response time (ms), 99th percentile | 332.1 | 349.1 | 340.5 | 326.6 |
| time over the response line (% of samples) | 0.2189 | 0.2196 | 0.2056 | 0.1282 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 1.7 | 0.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1883 | 0.2083 | 0.22 |
| utilisation (used / allocatable) | 0.03668 | 0.04098 | 0.03673 | 0.04044 |
| CPU used (cores), mean | 0.8802 | 0.9835 | 0.8816 | 0.9707 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00517 | 0.00799 |
| CPU used with Omni's own (cores), mean | 0.8802 | 0.9835 | 0.8868 | 0.9787 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.1 | 646.3 | 715.9 | 654.3 |
| HPA replicas, mean | 8.813 | 8.839 | 9.702 | 9.561 |
| pods started | 4.8 | 4.8 | 6.6 | 6.1 |
| pod start wait, total (s) | 7.5 | 7.6 | 10.5 | 8.8 |
| pod start wait, mean (s) | 1.57 | 1.577 | 1.585 | 1.409 |
| host CPU busy, the real machine under kind (%) | 25.89 | 29.55 | 26.12 | 29.7 |
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

Omni-Compass stayed native in 6 of 10 repetitions (repetitions 1, 2, 4, 5, 7, 8): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0062 to +0.0102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.6 | +0.1% | −0.7644 to +0.9265 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.6 | +0.1% | −0.7644 to +0.9265 | no |
| response time (ms), mean | 117.8 | 117.1 | −0.6% | −3.4301 to +2.0895 | no |
| response time (ms), 95th percentile | 243.9 | 239.9 | −1.7% | −12.3253 to +4.2083 | no |
| response time (ms), 99th percentile | 349.1 | 326.6 | −6.4% | −38.2598 to −6.6936 | yes: GAIN |
| time over the response line (% of samples) | 0.2196 | 0.1282 | −41.6% | −0.2605 to +0.0777 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.22 | +16.8% | −0.2403 to +0.3037 | no |
| utilisation (used / allocatable) | 0.04098 | 0.04044 | −1.3% | −0.0010 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9835 | 0.9707 | −1.3% | −0.0247 to −0.0009 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00799 | +0.008 (native is 0) | +0.0064 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9835 | 0.9787 | −0.5% | −0.0169 to +0.0073 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 646.3 | 654.3 | +1.2% | −0.0089 to +15.9175 | no |
| HPA replicas, mean | 8.839 | 9.561 | +8.2% | +0.0791 to +1.3640 | yes: power given |
| pods started | 4.8 | 6.1 | +27.1% | −0.1717 to +2.7717 | no |
| pod start wait, total (s) | 7.6 | 8.8 | +15.8% | −2.2189 to +4.6189 | no |
| pod start wait, mean (s) | 1.577 | 1.409 | −10.6% | −0.4410 to +0.1053 | no |
| host CPU busy, the real machine under kind (%) | 29.55 | 29.7 | +0.5% | −0.2382 to +0.5400 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0074 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.5 | +0.6% | +0.2259 to +1.7422 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.5 | +0.6% | +0.2259 to +1.7422 | yes: power given |
| response time (ms), mean | 114.6 | 117.8 | +2.7% | +1.5416 to +4.7433 | yes: LOSS |
| response time (ms), 95th percentile | 237.3 | 243.9 | +2.8% | −3.2092 to +16.4792 | no |
| response time (ms), 99th percentile | 332.1 | 349.1 | +5.1% | −1.8820 to +35.8090 | no |
| time over the response line (% of samples) | 0.2189 | 0.2196 | +0.3% | −0.1793 to +0.1807 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1883 | +135.4% | −0.0504 to +0.2670 | no |
| utilisation (used / allocatable) | 0.03668 | 0.04098 | +11.7% | +0.0035 to +0.0051 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8802 | 0.9835 | +11.7% | +0.0836 to +0.1229 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8802 | 0.9835 | +11.7% | +0.0836 to +0.1229 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.1 | 646.3 | −9.9% | −81.8351 to −59.8271 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.813 | 8.839 | +0.3% | −0.1087 to +0.1620 | no |
| pods started | 4.8 | 4.8 | ±0.0% | −0.4769 to +0.4769 | no |
| pod start wait, total (s) | 7.5 | 7.6 | +1.3% | −1.1818 to +1.3818 | no |
| pod start wait, mean (s) | 1.57 | 1.577 | +0.4% | −0.2015 to +0.2148 | no |
| host CPU busy, the real machine under kind (%) | 25.89 | 29.55 | +14.1% | +3.0012 to +4.3196 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.516 | +0.2% | −0.0012 to +0.0082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.8 | +0.2% | −0.1561 to +0.8491 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.8 | +0.2% | −0.1561 to +0.8491 | no |
| response time (ms), mean | 114.6 | 114.3 | −0.2% | −2.9455 to +2.4015 | no |
| response time (ms), 95th percentile | 237.3 | 233.6 | −1.5% | −16.2689 to +8.9329 | no |
| response time (ms), 99th percentile | 332.1 | 340.5 | +2.5% | −10.6161 to +27.4501 | no |
| time over the response line (% of samples) | 0.2189 | 0.2056 | −6.1% | −0.1241 to +0.0974 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.7 | +1.700 (native is 0) | +0.1901 to +3.2099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.2083 | +160.4% | −0.0524 to +0.3091 | no |
| utilisation (used / allocatable) | 0.03668 | 0.03673 | +0.2% | −0.0006 to +0.0008 | no |
| CPU used (cores), mean | 0.8802 | 0.8816 | +0.2% | −0.0155 to +0.0182 | no |
| Omni's own CPU (cores), mean | 0 | 0.00517 | +0.005 (native is 0) | +0.0043 to +0.0061 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8802 | 0.8868 | +0.7% | −0.0104 to +0.0235 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.1 | 715.9 | −0.2% | −14.4797 to +12.0885 | no |
| HPA replicas, mean | 8.813 | 9.702 | +10.1% | +0.1355 to +1.6437 | yes: power given |
| pods started | 4.8 | 6.6 | +37.5% | −0.4316 to +4.0316 | no |
| pod start wait, total (s) | 7.5 | 10.5 | +40.0% | −0.6629 to +6.6629 | no |
| pod start wait, mean (s) | 1.57 | 1.585 | +1.0% | −0.2830 to +0.3131 | no |
| host CPU busy, the real machine under kind (%) | 25.89 | 26.12 | +0.9% | −0.2675 to +0.7181 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0044 to +0.0104 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 158.8 | −0.4% | −1.3319 to +0.0568 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 158.8 | −0.4% | −1.3319 to +0.0568 | no |
| response time (ms), mean | 117.8 | 114.3 | −2.9% | −6.8548 to +0.0259 | no |
| response time (ms), 95th percentile | 243.9 | 233.6 | −4.2% | −19.2112 to −1.3948 | yes: GAIN |
| response time (ms), 99th percentile | 349.1 | 340.5 | −2.4% | −25.6104 to +8.5174 | no |
| time over the response line (% of samples) | 0.2196 | 0.2056 | −6.4% | −0.1480 to +0.1200 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.7 | +1.700 (native is 0) | +0.1901 to +3.2099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.2083 | +10.6% | −0.2218 to +0.2618 | no |
| utilisation (used / allocatable) | 0.04098 | 0.03673 | −10.4% | −0.0050 to −0.0035 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9835 | 0.8816 | −10.4% | −0.1195 to −0.0841 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00517 | +0.005 (native is 0) | +0.0043 to +0.0061 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9835 | 0.8868 | −9.8% | −0.1139 to −0.0794 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 646.3 | 715.9 | +10.8% | +59.2779 to +79.9932 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.839 | 9.702 | +9.8% | +0.1484 to +1.5775 | yes: power given |
| pods started | 4.8 | 6.6 | +37.5% | −0.4060 to +4.0060 | no |
| pod start wait, total (s) | 7.6 | 10.5 | +38.2% | −0.9365 to +6.7365 | no |
| pod start wait, mean (s) | 1.577 | 1.585 | +0.5% | −0.1949 to +0.2118 | no |
| host CPU busy, the real machine under kind (%) | 29.55 | 26.12 | −11.6% | −3.9521 to −2.9182 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.515 | +0.2% | −0.0083 to +0.0133 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.6 | +0.7% | −0.0537 to +2.1838 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.6 | +0.7% | −0.0537 to +2.1838 | no |
| response time (ms), mean | 114.6 | 117.1 | +2.2% | +0.0639 to +4.8805 | yes: LOSS |
| response time (ms), 95th percentile | 237.3 | 239.9 | +1.1% | −5.1698 to +10.3228 | no |
| response time (ms), 99th percentile | 332.1 | 326.6 | −1.7% | −22.3646 to +11.3382 | no |
| time over the response line (% of samples) | 0.2189 | 0.1282 | −41.4% | −0.2134 to +0.0320 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.22 | +175.0% | −0.1168 to +0.3968 | no |
| utilisation (used / allocatable) | 0.03668 | 0.04044 | +10.3% | +0.0028 to +0.0047 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8802 | 0.9707 | +10.3% | +0.0683 to +0.1126 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00799 | +0.008 (native is 0) | +0.0064 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8802 | 0.9787 | +11.2% | +0.0752 to +0.1217 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 717.1 | 654.3 | −8.8% | −76.2931 to −49.4606 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.813 | 9.561 | +8.5% | +0.0844 to +1.4121 | yes: power given |
| pods started | 4.8 | 6.1 | +27.1% | −0.1717 to +2.7717 | no |
| pod start wait, total (s) | 7.5 | 8.8 | +17.3% | −1.6599 to +4.2599 | no |
| pod start wait, mean (s) | 1.57 | 1.409 | −10.3% | −0.4368 to +0.1145 | no |
| host CPU busy, the real machine under kind (%) | 25.89 | 29.7 | +14.7% | +2.8827 to +4.7399 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*