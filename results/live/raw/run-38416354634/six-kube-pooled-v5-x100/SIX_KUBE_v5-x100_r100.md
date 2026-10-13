# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

Each square here is its first 100 repetitions (repetitions 1 to 100; the grid's 1-, 10- and 100-repetition squares are nested).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3451 | 3241 | 3724 | 2922 | 3578 | 3101 | 4339 | 3640 | 2600 | 2951 | 2738 | 3974 |
| response time (ms), 99th percentile | 5595 | 5468 | 5998 | 5651 | 5894 | 5707 | 6512 | 6186 | 4449 | 5069 | 5370 | 6407 |
| time over the response line (% of samples) | 57.16 | 51.95 | 60 | 53.33 | 57.39 | 51.1 | 59.38 | 54.78 | 51.02 | 45.57 | 59.55 | 54.89 |
| failed requests (%) | 39.81 | 39.05 | 42.21 | 41.12 | 38.73 | 37.72 | 41.65 | 42.71 | 32.11 | 32.41 | 42.54 | 42.32 |
| HPA replicas, mean | 9.849 | 9.844 | 9.87 | 9.866 | 9.864 | 9.857 | 9.857 | 9.85 | 9.831 | 9.815 | 9.894 | 9.862 |
| pods started | 3.34 | 3.34 | 2.78 | 2.84 | 3.02 | 3.11 | 3.03 | 3.15 | 5.22 | 5.31 | 5.13 | 5.12 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 284.7 | 282.1 | 285.4 | 283.5 | 284.7 | 282.6 | 286.3 | 283.6 | 470.2 | 466.2 | 708.5 | 700.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.7 | 282.1 | 285.4 | 283.5 | 284.7 | 282.6 | 286.3 | 283.6 | 470.2 | 466.2 | 708.5 | 700.4 |
| CPU used with Omni's own (cores), mean | 2.975 | 2.809 | 3.02 | 2.898 | 2.989 | 2.862 | 3.078 | 2.912 | 2.852 | 2.699 | 2.962 | 2.755 |
| host CPU busy, the real machine under kind (%) | 88.43 | 90.95 | 90.33 | 91.5 | 89.82 | 91.61 | 91.08 | 93.28 | 86.91 | 89.85 | 89.85 | 92.69 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 | 6.88e+12 | 6.88e+12 | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 | 1.103e+15 | 1.103e+15 | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 | 2.589 | 2.551 | 2.524 | 2.439 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 | 0.006235 | 0.006235 | 0.01188 | 0.01188 |
| organism behind its window (s) | 1.607 | 2.007 | 0.831 | 1.207 | 1.294 | 1.241 | 1.061 | 2.019 | 2.808 | 8.565 | 4.589 | 202.2 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3451 | 3241 | -6.1% | -608.4 to +188.4 | better (inside the noise) |
| response time (ms), 99th percentile | 5595 | 5468 | -2.3% | -480.3 to +226.5 | better (inside the noise) |
| time over the response line (% of samples) | 57.16 | 51.95 | -9.1% | -5.858 to -4.558 | better |
| failed requests (%) | 39.81 | 39.05 | -1.9% | -1.905 to +0.3841 | better (inside the noise) |
| HPA replicas, mean | 9.849 | 9.844 | -0.1% | -0.01613 to +0.005837 | better (inside the noise) |
| pods started | 3.34 | 3.34 | +0.0% | -0.2598 to +0.2598 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.981e-16 to +1.041e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.7 | 282.1 | -0.9% | -3.083 to -2.115 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.7 | 282.1 | -0.9% | -3.083 to -2.115 | better |
| CPU used with Omni's own (cores), mean | 2.975 | 2.809 | -5.6% | -0.1931 to -0.1403 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.43 | 90.95 | +2.9% | +1.926 to +3.126 | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | WORSE |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | WORSE |
| organism behind its window (s) | 1.607 | 2.007 | +24.9% | +0.2685 to +0.5315 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3724 | 2922 | -21.5% | -1122 to -483 | better |
| response time (ms), 99th percentile | 5998 | 5651 | -5.8% | -701.7 to +7.227 | better (inside the noise) |
| time over the response line (% of samples) | 60 | 53.33 | -11.1% | -7.553 to -5.793 | better |
| failed requests (%) | 42.21 | 41.12 | -2.6% | -1.637 to -0.5405 | better |
| HPA replicas, mean | 9.87 | 9.866 | -0.0% | -0.01593 to +0.007924 | better (inside the noise) |
| pods started | 2.78 | 2.84 | +2.2% | -0.2169 to +0.3369 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.477e-16 to +9.313e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.4 | 283.5 | -0.7% | -2.291 to -1.594 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.4 | 283.5 | -0.7% | -2.291 to -1.594 | better |
| CPU used with Omni's own (cores), mean | 3.02 | 2.898 | -4.0% | -0.1338 to -0.1084 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 90.33 | 91.5 | +1.3% | +0.8837 to +1.449 | shown, not judged (more or less is not better by itself) |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | WORSE |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | better |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | WORSE |
| organism behind its window (s) | 0.831 | 1.207 | +45.2% | +0.2601 to +0.4919 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 6, worse on 0, inside the noise on 3

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3578 | 3101 | -13.3% | -780.8 to -174.2 | better |
| response time (ms), 99th percentile | 5894 | 5707 | -3.2% | -535.7 to +163.2 | better (inside the noise) |
| time over the response line (% of samples) | 57.39 | 51.1 | -11.0% | -7.028 to -5.552 | better |
| failed requests (%) | 38.73 | 37.72 | -2.6% | -1.653 to -0.3593 | better |
| HPA replicas, mean | 9.864 | 9.857 | -0.1% | -0.02076 to +0.006826 | better (inside the noise) |
| pods started | 3.02 | 3.11 | +3.0% | -0.2326 to +0.4126 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.706e-16 to +4.548e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.7 | 282.6 | -0.7% | -2.515 to -1.718 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.7 | 282.6 | -0.7% | -2.515 to -1.718 | better |
| CPU used with Omni's own (cores), mean | 2.989 | 2.862 | -4.2% | -0.1449 to -0.1083 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.82 | 91.61 | +2.0% | +1.379 to +2.193 | shown, not judged (more or less is not better by itself) |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.294 | 1.241 | -4.1% | -0.1791 to +0.07315 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4339 | 3640 | -16.1% | -1106 to -292.5 | better |
| response time (ms), 99th percentile | 6512 | 6186 | -5.0% | -690.2 to +38.3 | better (inside the noise) |
| time over the response line (% of samples) | 59.38 | 54.78 | -7.7% | -5.252 to -3.945 | better |
| failed requests (%) | 41.65 | 42.71 | +2.5% | -0.3939 to +2.503 | WORSE (inside the noise) |
| HPA replicas, mean | 9.857 | 9.85 | -0.1% | -0.01908 to +0.00454 | better (inside the noise) |
| pods started | 3.03 | 3.15 | +4.0% | -0.1417 to +0.3817 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.921e-16 to +1.053e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 286.3 | 283.6 | -0.9% | -3.133 to -2.246 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.3 | 283.6 | -0.9% | -3.133 to -2.246 | better |
| CPU used with Omni's own (cores), mean | 3.078 | 2.912 | -5.4% | -0.1892 to -0.143 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.08 | 93.28 | +2.4% | +1.636 to +2.752 | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | WORSE |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | better |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | WORSE |
| organism behind its window (s) | 1.061 | 2.019 | +90.3% | +0.8322 to +1.084 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 100 copies: better on 5, worse on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), inside the noise on 2; OFF THE CLOCK in 1 of 100 repetitions (the organism ended up to 167 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2600 | 2951 | +13.5% | +71.19 to +631.8 | WORSE |
| response time (ms), 99th percentile | 4449 | 5069 | +13.9% | +261.3 to +978.5 | WORSE |
| time over the response line (% of samples) | 51.02 | 45.57 | -10.7% | -6.238 to -4.668 | better |
| failed requests (%) | 32.11 | 32.41 | +0.9% | -0.8535 to +1.438 | WORSE (inside the noise) |
| HPA replicas, mean | 9.831 | 9.815 | -0.2% | -0.02326 to -0.007519 | better |
| pods started | 5.22 | 5.31 | +1.7% | -0.01824 to +0.1982 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.179e-16 to +3.31e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 470.2 | 466.2 | -0.9% | -4.712 to -3.312 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 470.2 | 466.2 | -0.9% | -4.712 to -3.312 | better |
| CPU used with Omni's own (cores), mean | 2.852 | 2.699 | -5.3% | -0.1767 to -0.1284 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.91 | 89.85 | +3.4% | +2.392 to +3.498 | shown, not judged (more or less is not better by itself) |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | better |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | same (under one part in a million) |
| organism behind its window (s) | 2.808 | 8.565 | +205.0% | +1.749 to +9.765 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 100 copies: better on 5, worse on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism energy (J); organism work per energy), inside the noise on 2; OFF THE CLOCK in 49 of 100 repetitions (the organism ended up to 635 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2738 | 3974 | +45.1% | +947.9 to +1524 | WORSE |
| response time (ms), 99th percentile | 5370 | 6407 | +19.3% | +717.2 to +1357 | WORSE |
| time over the response line (% of samples) | 59.55 | 54.89 | -7.8% | -5.631 to -3.696 | better |
| failed requests (%) | 42.54 | 42.32 | -0.5% | -1.185 to +0.7427 | better (inside the noise) |
| HPA replicas, mean | 9.894 | 9.862 | -0.3% | -0.03947 to -0.02379 | better |
| pods started | 5.13 | 5.12 | -0.2% | -0.1045 to +0.08445 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.413e-16 to +6.824e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 708.5 | 700.4 | -1.1% | -9.142 to -6.948 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 708.5 | 700.4 | -1.1% | -9.142 to -6.948 | better |
| CPU used with Omni's own (cores), mean | 2.962 | 2.755 | -7.0% | -0.2345 to -0.1784 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.85 | 92.69 | +3.2% | +2.122 to +3.544 | shown, not judged (more or less is not better by itself) |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | WORSE |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | better |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | WORSE |
| organism behind its window (s) | 4.589 | 202.2 | +4305.9% | +160.8 to +234.4 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
