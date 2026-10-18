# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

Each square here is its first 100 repetitions (repetitions 1 to 100; the grid's 1-, 10- and 100-repetition squares are nested).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1618 | 901.1 | 2223 | 1468 | 2100 | 1361 | 1849 | 1153 | 1653 | 1127 | 1827 | 1013 |
| response time (ms), 99th percentile | 4022 | 3294 | 5375 | 4839 | 5038 | 4452 | 4548 | 3899 | 3744 | 3442 | 4611 | 3524 |
| time over the response line (% of samples) | 27.23 | 15.11 | 26.15 | 13.34 | 24.02 | 12.29 | 30.19 | 14.97 | 26.59 | 14.78 | 30.23 | 17.26 |
| failed requests (%) | 9.318 | 8.175 | 5.891 | 5.281 | 5.707 | 4.726 | 7.513 | 6.359 | 7.925 | 6.852 | 10.27 | 9.207 |
| HPA replicas, mean | 9.699 | 9.69 | 9.733 | 9.747 | 9.692 | 9.709 | 9.663 | 9.692 | 9.638 | 9.584 | 9.737 | 9.724 |
| pods started | 4.13 | 4.27 | 3.67 | 3.29 | 3.91 | 3.65 | 4.2 | 3.96 | 4.51 | 4.6 | 3.75 | 3.92 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 185.1 | 185.1 | 184.8 | 183.8 | 183.4 | 186.2 | 185.8 | 184.4 | 184.1 | 186.7 | 186.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.1 | 185.1 | 184.8 | 183.8 | 183.4 | 186.2 | 185.8 | 184.4 | 184.1 | 186.7 | 186.5 |
| CPU used with Omni's own (cores), mean | 2.463 | 2.436 | 2.495 | 2.46 | 2.376 | 2.337 | 2.538 | 2.503 | 2.386 | 2.359 | 2.586 | 2.567 |
| host CPU busy, the real machine under kind (%) | 71.93 | 71.43 | 72.64 | 71.9 | 69.43 | 68.46 | 74.27 | 73.55 | 69.79 | 69.22 | 75.49 | 75.25 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0.001 | 0 | 0.001 | 0 | 0 | 0 | 0 | 0 | 0.002 | 0.013 | 0.021 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1618 | 901.1 | -44.3% | -829.5 to -603.7 | better |
| response time (ms), 99th percentile | 4022 | 3294 | -18.1% | -989.2 to -467.9 | better |
| time over the response line (% of samples) | 27.23 | 15.11 | -44.5% | -13.7 to -10.54 | better |
| failed requests (%) | 9.318 | 8.175 | -12.3% | -1.485 to -0.802 | better |
| HPA replicas, mean | 9.699 | 9.69 | -0.1% | -0.0293 to +0.009493 | better (inside the noise) |
| pods started | 4.13 | 4.27 | +3.4% | -0.1509 to +0.4309 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.776e-16 to +1.355e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 185.1 | -0.2% | -0.5488 to -0.1549 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.1 | -0.2% | -0.5488 to -0.1549 | better |
| CPU used with Omni's own (cores), mean | 2.463 | 2.436 | -1.1% | -0.03666 to -0.01706 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 71.93 | 71.43 | -0.7% | -0.7519 to -0.2559 | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.623e+05 | WORSE |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | better |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.143e-05 | WORSE |
| organism behind its window (s) | 0 | 0.001 | +0.001 | -0.00096 to +0.00296 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 8, worse on 2 (organism energy (J); organism work per energy), inside the noise on 1

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2223 | 1468 | -33.9% | -904.8 to -604 | better |
| response time (ms), 99th percentile | 5375 | 4839 | -10.0% | -751.8 to -320.4 | better |
| time over the response line (% of samples) | 26.15 | 13.34 | -49.0% | -14.01 to -11.61 | better |
| failed requests (%) | 5.891 | 5.281 | -10.4% | -0.8317 to -0.3891 | better |
| HPA replicas, mean | 9.733 | 9.747 | +0.1% | -0.003948 to +0.03314 | WORSE (inside the noise) |
| pods started | 3.67 | 3.29 | -10.4% | -0.6745 to -0.08547 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.463e-16 to +1.397e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 184.8 | -0.1% | -0.4054 to -0.1433 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 184.8 | -0.1% | -0.4054 to -0.1433 | better |
| CPU used with Omni's own (cores), mean | 2.495 | 2.46 | -1.4% | -0.04313 to -0.027 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.64 | 71.9 | -1.0% | -0.9376 to -0.5446 | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | WORSE |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | better |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.244e-05 to -8.243e-05 | WORSE |
| organism behind its window (s) | 0 | 0.001 | +0.001 | -0.00096 to +0.00296 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 7, worse on 0, inside the noise on 2

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2100 | 1361 | -35.2% | -893.5 to -585.6 | better |
| response time (ms), 99th percentile | 5038 | 4452 | -11.6% | -773.8 to -397.5 | better |
| time over the response line (% of samples) | 24.02 | 12.29 | -48.8% | -13.07 to -10.38 | better |
| failed requests (%) | 5.707 | 4.726 | -17.2% | -1.237 to -0.7244 | better |
| HPA replicas, mean | 9.692 | 9.709 | +0.2% | -0.002567 to +0.03574 | WORSE (inside the noise) |
| pods started | 3.91 | 3.65 | -6.6% | -0.5808 to +0.06082 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.951e-16 to +1.175e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.4 | -0.2% | -0.5424 to -0.2462 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.4 | -0.2% | -0.5424 to -0.2462 | better |
| CPU used with Omni's own (cores), mean | 2.376 | 2.337 | -1.7% | -0.04699 to -0.03187 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.43 | 68.46 | -1.4% | -1.176 to -0.7703 | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 7, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 1

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1849 | 1153 | -37.7% | -806.4 to -586 | better |
| response time (ms), 99th percentile | 4548 | 3899 | -14.3% | -866.1 to -431.1 | better |
| time over the response line (% of samples) | 30.19 | 14.97 | -50.4% | -17.05 to -13.39 | better |
| failed requests (%) | 7.513 | 6.359 | -15.4% | -1.421 to -0.8859 | better |
| HPA replicas, mean | 9.663 | 9.692 | +0.3% | +0.009279 to +0.04754 | WORSE |
| pods started | 4.2 | 3.96 | -5.7% | -0.535 to +0.05498 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.097e-16 to -1.658e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.2 | 185.8 | -0.2% | -0.4834 to -0.2044 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.2 | 185.8 | -0.2% | -0.4834 to -0.2044 | better |
| CPU used with Omni's own (cores), mean | 2.538 | 2.503 | -1.4% | -0.04517 to -0.0252 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.27 | 73.55 | -1.0% | -0.9828 to -0.462 | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.377e+05 | WORSE |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | better |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 8, worse on 0, inside the noise on 1

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1653 | 1127 | -31.9% | -621 to -432.4 | better |
| response time (ms), 99th percentile | 3744 | 3442 | -8.1% | -513.7 to -89.92 | better |
| time over the response line (% of samples) | 26.59 | 14.78 | -44.4% | -13.54 to -10.1 | better |
| failed requests (%) | 7.925 | 6.852 | -13.5% | -1.415 to -0.7321 | better |
| HPA replicas, mean | 9.638 | 9.584 | -0.6% | -0.08978 to -0.01753 | better |
| pods started | 4.51 | 4.6 | +2.0% | -0.2513 to +0.4313 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.084e-16 to +5.315e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.1 | -0.2% | -0.6056 to -0.1587 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.1 | -0.2% | -0.6056 to -0.1587 | better |
| CPU used with Omni's own (cores), mean | 2.386 | 2.359 | -1.1% | -0.03711 to -0.01609 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.79 | 69.22 | -0.8% | -0.8329 to -0.3204 | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | better |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0.002 | +0.002 | -0.0007578 to +0.004758 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 7, worse on 0, inside the noise on 2

100 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1827 | 1013 | -44.6% | -947.7 to -681.2 | better |
| response time (ms), 99th percentile | 4611 | 3524 | -23.6% | -1369 to -805 | better |
| time over the response line (% of samples) | 30.23 | 17.26 | -42.9% | -14.41 to -11.53 | better |
| failed requests (%) | 10.27 | 9.207 | -10.4% | -1.344 to -0.7852 | better |
| HPA replicas, mean | 9.737 | 9.724 | -0.1% | -0.03321 to +0.006771 | better (inside the noise) |
| pods started | 3.75 | 3.92 | +4.5% | -0.1236 to +0.4636 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.095e-16 to +3.227e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.7 | 186.5 | -0.1% | -0.4492 to -0.04105 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.7 | 186.5 | -0.1% | -0.4492 to -0.04105 | better |
| CPU used with Omni's own (cores), mean | 2.586 | 2.567 | -0.7% | -0.02746 to -0.009558 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 75.49 | 75.25 | -0.3% | -0.4404 to -0.03522 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.013 | 0.021 | +61.5% | -0.00404 to +0.02004 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
