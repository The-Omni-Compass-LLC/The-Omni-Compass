# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

Each square here is its first 100 repetitions (repetitions 1 to 100; the grid's 1-, 10- and 100-repetition squares are nested).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2225 | 978.4 | 2607 | 1578 | 2454 | 1523 | 3070 | 2117 | 2895 | 1862 | 2056 | 1167 |
| response time (ms), 99th percentile | 4422 | 2882 | 5000 | 3828 | 5133 | 4249 | 5294 | 4393 | 5224 | 4443 | 4347 | 3162 |
| time over the response line (% of samples) | 43.82 | 27.53 | 45.77 | 33.52 | 44.8 | 32.48 | 48.44 | 36.82 | 50.38 | 40 | 44.96 | 31.93 |
| failed requests (%) | 21.6 | 19.39 | 26.76 | 24.25 | 26.18 | 23.75 | 28.42 | 26.37 | 30.68 | 29.22 | 22.43 | 20.86 |
| HPA replicas, mean | 9.707 | 9.742 | 9.721 | 9.736 | 9.703 | 9.731 | 9.741 | 9.748 | 9.756 | 9.767 | 9.749 | 9.767 |
| pods started | 4.43 | 3.86 | 3.83 | 3.72 | 4.08 | 3.75 | 3.79 | 3.65 | 3.61 | 3.51 | 3.61 | 3.44 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 188.9 | 188.7 | 189.9 | 189.7 | 189.5 | 189.2 | 189.5 | 189.2 | 189.9 | 189.2 | 188.9 | 187.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.9 | 188.7 | 189.9 | 189.7 | 189.5 | 189.2 | 189.5 | 189.2 | 189.9 | 189.2 | 188.9 | 187.9 |
| CPU used with Omni's own (cores), mean | 2.861 | 2.817 | 2.923 | 2.886 | 2.889 | 2.854 | 2.917 | 2.868 | 2.919 | 2.868 | 2.826 | 2.756 |
| host CPU busy, the real machine under kind (%) | 82.44 | 82.1 | 85.19 | 84.68 | 84.09 | 83.88 | 84.15 | 83.7 | 85.38 | 85.51 | 83.13 | 84.17 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.068 | 0.066 | 0.058 | 0.067 | 0.057 | 0.064 | 0.072 | 0.073 | 0.204 | 0.219 | 0.334 | 0.356 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 8, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 0

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2225 | 978.4 | -56.0% | -1459 to -1034 | better |
| response time (ms), 99th percentile | 4422 | 2882 | -34.8% | -1908 to -1172 | better |
| time over the response line (% of samples) | 43.82 | 27.53 | -37.2% | -18.14 to -14.44 | better |
| failed requests (%) | 21.6 | 19.39 | -10.2% | -2.715 to -1.697 | better |
| HPA replicas, mean | 9.707 | 9.742 | +0.4% | +0.01962 to +0.05043 | WORSE |
| pods started | 4.43 | 3.86 | -12.9% | -0.8405 to -0.2995 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.935e-16 to +2.047e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.9 | 188.7 | -0.1% | -0.4547 to -0.08731 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.9 | 188.7 | -0.1% | -0.4547 to -0.08731 | better |
| CPU used with Omni's own (cores), mean | 2.861 | 2.817 | -1.5% | -0.05118 to -0.03704 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 82.44 | 82.1 | -0.4% | -0.5313 to -0.1587 | shown, not judged (more or less is not better by itself) |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | WORSE |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | WORSE |
| organism behind its window (s) | 0.068 | 0.066 | -2.9% | -0.01123 to +0.007231 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2607 | 1578 | -39.5% | -1247 to -812.5 | better |
| response time (ms), 99th percentile | 5000 | 3828 | -23.4% | -1514 to -828.8 | better |
| time over the response line (% of samples) | 45.77 | 33.52 | -26.8% | -13.42 to -11.08 | better |
| failed requests (%) | 26.76 | 24.25 | -9.4% | -3.049 to -1.959 | better |
| HPA replicas, mean | 9.721 | 9.736 | +0.2% | -0.002989 to +0.03265 | WORSE (inside the noise) |
| pods started | 3.83 | 3.72 | -2.9% | -0.4047 to +0.1847 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.848e-16 to +1.96e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.9 | 189.7 | -0.1% | -0.3896 to +0.0225 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.9 | 189.7 | -0.1% | -0.3896 to +0.0225 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.923 | 2.886 | -1.3% | -0.04594 to -0.0272 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.19 | 84.68 | -0.6% | -0.7803 to -0.2253 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | WORSE |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | better |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | WORSE |
| organism behind its window (s) | 0.058 | 0.067 | +15.5% | -0.002176 to +0.02018 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 8, worse on 1 (HPA replicas, mean), inside the noise on 0

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2454 | 1523 | -37.9% | -1122 to -740.7 | better |
| response time (ms), 99th percentile | 5133 | 4249 | -17.2% | -1306 to -462.7 | better |
| time over the response line (% of samples) | 44.8 | 32.48 | -27.5% | -13.74 to -10.91 | better |
| failed requests (%) | 26.18 | 23.75 | -9.3% | -2.905 to -1.961 | better |
| HPA replicas, mean | 9.703 | 9.731 | +0.3% | +0.01385 to +0.04317 | WORSE |
| pods started | 4.08 | 3.75 | -8.1% | -0.5681 to -0.09189 | better |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.179e-16 to +3.133e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.5 | 189.2 | -0.2% | -0.5183 to -0.08919 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.5 | 189.2 | -0.2% | -0.5183 to -0.08919 | better |
| CPU used with Omni's own (cores), mean | 2.889 | 2.854 | -1.2% | -0.04338 to -0.02581 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.09 | 83.88 | -0.3% | -0.4451 to +0.007685 | shown, not judged (more or less is not better by itself) |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | better |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.057 | 0.064 | +12.3% | -0.001475 to +0.01548 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3070 | 2117 | -31.0% | -1209 to -696.9 | better |
| response time (ms), 99th percentile | 5294 | 4393 | -17.0% | -1224 to -578.7 | better |
| time over the response line (% of samples) | 48.44 | 36.82 | -24.0% | -12.94 to -10.29 | better |
| failed requests (%) | 28.42 | 26.37 | -7.2% | -2.594 to -1.51 | better |
| HPA replicas, mean | 9.741 | 9.748 | +0.1% | -0.00826 to +0.02188 | WORSE (inside the noise) |
| pods started | 3.79 | 3.65 | -3.7% | -0.4101 to +0.1301 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.896e-17 to +3.965e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.5 | 189.2 | -0.2% | -0.5498 to -0.1047 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.5 | 189.2 | -0.2% | -0.5498 to -0.1047 | better |
| CPU used with Omni's own (cores), mean | 2.917 | 2.868 | -1.7% | -0.05705 to -0.04106 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.15 | 83.7 | -0.5% | -0.6991 to -0.2126 | shown, not judged (more or less is not better by itself) |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | WORSE |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | better |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | WORSE |
| organism behind its window (s) | 0.072 | 0.073 | +1.4% | -0.006627 to +0.008627 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 7, worse on 0, inside the noise on 2

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2895 | 1862 | -35.7% | -1302 to -763.7 | better |
| response time (ms), 99th percentile | 5224 | 4443 | -15.0% | -1106 to -456.5 | better |
| time over the response line (% of samples) | 50.38 | 40 | -20.6% | -11.93 to -8.842 | better |
| failed requests (%) | 30.68 | 29.22 | -4.8% | -2.103 to -0.815 | better |
| HPA replicas, mean | 9.756 | 9.767 | +0.1% | -0.004679 to +0.02784 | WORSE (inside the noise) |
| pods started | 3.61 | 3.51 | -2.8% | -0.3665 to +0.1665 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.559e-16 to +1.605e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.9 | 189.2 | -0.4% | -1.013 to -0.5085 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.9 | 189.2 | -0.4% | -1.013 to -0.5085 | better |
| CPU used with Omni's own (cores), mean | 2.919 | 2.868 | -1.8% | -0.05925 to -0.04447 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.38 | 85.51 | +0.2% | -0.05751 to +0.3275 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | better |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.204 | 0.219 | +7.4% | -0.01074 to +0.04074 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 7, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 1

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2056 | 1167 | -43.2% | -1050 to -726.1 | better |
| response time (ms), 99th percentile | 4347 | 3162 | -27.3% | -1560 to -809.9 | better |
| time over the response line (% of samples) | 44.96 | 31.93 | -29.0% | -14.53 to -11.53 | better |
| failed requests (%) | 22.43 | 20.86 | -7.0% | -2.014 to -1.116 | better |
| HPA replicas, mean | 9.749 | 9.767 | +0.2% | +0.003149 to +0.033 | WORSE |
| pods started | 3.61 | 3.44 | -4.7% | -0.4177 to +0.0777 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.408e-16 to +3.362e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.9 | 187.9 | -0.5% | -1.299 to -0.7363 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.9 | 187.9 | -0.5% | -1.299 to -0.7363 | better |
| CPU used with Omni's own (cores), mean | 2.826 | 2.756 | -2.5% | -0.07907 to -0.06029 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 83.13 | 84.17 | +1.2% | +0.7929 to +1.283 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | WORSE |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | WORSE |
| organism behind its window (s) | 0.334 | 0.356 | +6.6% | -0.009343 to +0.05334 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
