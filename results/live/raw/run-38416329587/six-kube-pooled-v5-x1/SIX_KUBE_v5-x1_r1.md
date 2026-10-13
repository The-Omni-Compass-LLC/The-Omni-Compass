# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

Each square here is its first 1 repetition (repetitions 1 to 1; the grid's 1-, 10- and 100-repetition squares are nested).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1176 | 453.1 | 3012 | 1581 | 1943 | 1226 | 605.1 | 213.5 | 2619 | 1531 | 1125 | 539.8 |
| response time (ms), 99th percentile | 3016 | 2505 | 6933 | 5845 | 5404 | 5939 | 1552 | 641 | 6084 | 4585 | 3592 | 2333 |
| time over the response line (% of samples) | 14.93 | 4.224 | 38.9 | 24.6 | 35.89 | 19.78 | 8.701 | 1.965 | 47.59 | 32.42 | 14.65 | 5.556 |
| failed requests (%) | 0 | 0 | 9.863 | 8.046 | 12.6 | 8.667 | 0 | 0 | 18.28 | 16.67 | 0 | 0.1235 |
| HPA replicas, mean | 9.615 | 9.676 | 9.805 | 9.868 | 9.935 | 9.867 | 9.52 | 9.56 | 9.837 | 9.867 | 9.664 | 9.648 |
| pods started | 6 | 6 | 3 | 2 | 1 | 2 | 6 | 6 | 2 | 2 | 5 | 6 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 182.4 | 189.6 | 189.4 | 188.8 | 188.6 | 181.1 | 180.7 | 192.5 | 190.5 | 183.1 | 182.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 182.4 | 189.6 | 189.4 | 188.8 | 188.6 | 181.1 | 180.7 | 192.5 | 190.5 | 183.1 | 182.6 |
| CPU used with Omni's own (cores), mean | 2.255 | 2.196 | 2.922 | 2.925 | 2.943 | 2.859 | 1.973 | 1.907 | 3.142 | 3.182 | 2.237 | 2.163 |
| host CPU busy, the real machine under kind (%) | 66.75 | 64.78 | 84.29 | 84.03 | 85.13 | 83.89 | 60.01 | 58.24 | 91.01 | 91.7 | 65.83 | 64.99 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1176 | 453.1 | -61.5% |  | better (inside the noise) |
| response time (ms), 99th percentile | 3016 | 2505 | -16.9% |  | better (inside the noise) |
| time over the response line (% of samples) | 14.93 | 4.224 | -71.7% |  | better (inside the noise) |
| failed requests (%) | 0 | 0 | +0 |  | same |
| HPA replicas, mean | 9.615 | 9.676 | +0.6% |  | WORSE (inside the noise) |
| pods started | 6 | 6 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 182.4 | -0.5% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 182.4 | -0.5% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.255 | 2.196 | -2.6% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 66.75 | 64.78 | -3.0% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% |  | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% |  | better (inside the noise) |
| organism work per energy | 1.404 | 1.403 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3012 | 1581 | -47.5% |  | better (inside the noise) |
| response time (ms), 99th percentile | 6933 | 5845 | -15.7% |  | better (inside the noise) |
| time over the response line (% of samples) | 38.9 | 24.6 | -36.8% |  | better (inside the noise) |
| failed requests (%) | 9.863 | 8.046 | -18.4% |  | better (inside the noise) |
| HPA replicas, mean | 9.805 | 9.868 | +0.6% |  | WORSE (inside the noise) |
| pods started | 3 | 2 | -33.3% |  | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same |
| energy, parked workers still on at idle power (Wh, declared model) | 189.6 | 189.4 | -0.1% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.6 | 189.4 | -0.1% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.922 | 2.925 | +0.1% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.29 | 84.03 | -0.3% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% |  | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% |  | better (inside the noise) |
| organism work per energy | 1.125 | 1.124 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1943 | 1226 | -36.9% |  | better (inside the noise) |
| response time (ms), 99th percentile | 5404 | 5939 | +9.9% |  | WORSE (inside the noise) |
| time over the response line (% of samples) | 35.89 | 19.78 | -44.9% |  | better (inside the noise) |
| failed requests (%) | 12.6 | 8.667 | -31.2% |  | better (inside the noise) |
| HPA replicas, mean | 9.935 | 9.867 | -0.7% |  | better (inside the noise) |
| pods started | 1 | 2 | +100.0% |  | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.8 | 188.6 | -0.1% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.8 | 188.6 | -0.1% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.943 | 2.859 | -2.8% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.13 | 83.89 | -1.5% |  | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% |  | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% |  | better (inside the noise) |
| organism work per energy | 0.006603 | 0.006603 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 605.1 | 213.5 | -64.7% |  | better (inside the noise) |
| response time (ms), 99th percentile | 1552 | 641 | -58.7% |  | better (inside the noise) |
| time over the response line (% of samples) | 8.701 | 1.965 | -77.4% |  | better (inside the noise) |
| failed requests (%) | 0 | 0 | +0 |  | same |
| HPA replicas, mean | 9.52 | 9.56 | +0.4% |  | WORSE (inside the noise) |
| pods started | 6 | 6 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.7 | -0.3% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.7 | -0.3% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.973 | 1.907 | -3.3% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 60.01 | 58.24 | -2.9% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% |  | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% |  | better (inside the noise) |
| organism work per energy | 0.382 | 0.382 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2619 | 1531 | -41.5% |  | better (inside the noise) |
| response time (ms), 99th percentile | 6084 | 4585 | -24.6% |  | better (inside the noise) |
| time over the response line (% of samples) | 47.59 | 32.42 | -31.9% |  | better (inside the noise) |
| failed requests (%) | 18.28 | 16.67 | -8.8% |  | better (inside the noise) |
| HPA replicas, mean | 9.837 | 9.867 | +0.3% |  | WORSE (inside the noise) |
| pods started | 2 | 2 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.5 | 190.5 | -1.0% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.5 | 190.5 | -1.0% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.142 | 3.182 | +1.3% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.01 | 91.7 | +0.8% |  | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% |  | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% |  | better (inside the noise) |
| organism work per energy | 0.006799 | 0.006799 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1125 | 539.8 | -52.0% |  | better (inside the noise) |
| response time (ms), 99th percentile | 3592 | 2333 | -35.1% |  | better (inside the noise) |
| time over the response line (% of samples) | 14.65 | 5.556 | -62.1% |  | better (inside the noise) |
| failed requests (%) | 0 | 0.1235 | +0.123 |  | WORSE (inside the noise) |
| HPA replicas, mean | 9.664 | 9.648 | -0.2% |  | better (inside the noise) |
| pods started | 5 | 6 | +20.0% |  | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 182.6 | -0.3% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 182.6 | -0.3% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.237 | 2.163 | -3.3% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 65.83 | 64.99 | -1.3% |  | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% |  | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% |  | better (inside the noise) |
| organism work per energy | 0.01277 | 0.01277 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
