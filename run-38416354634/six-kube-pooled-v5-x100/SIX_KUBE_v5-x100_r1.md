# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

Each square here is its first 1 repetition (repetitions 1 to 1; the grid's 1-, 10- and 100-repetition squares are nested).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 6021 | 3373 | 6153 | 3304 | 476.2 | 218.6 | 3924 | 2612 | 5784 | 5127 | 3148 | 4461 |
| response time (ms), 99th percentile | 8573 | 7295 | 8142 | 6198 | 930 | 408.9 | 7898 | 5403 | 8178 | 9299 | 5009 | 8221 |
| time over the response line (% of samples) | 81.14 | 75.43 | 78.33 | 70.81 | 4.215 | 0.5344 | 77.71 | 73.51 | 81.09 | 74.58 | 54.63 | 38.83 |
| failed requests (%) | 64 | 65.14 | 62.22 | 60.54 | 0 | 0 | 64 | 64.86 | 66.91 | 61.69 | 0.4432 | 10.39 |
| HPA replicas, mean | 9.955 | 9.864 | 10 | 10 | 9.731 | 9.678 | 10 | 9.908 | 9.88 | 9.879 | 9.888 | 9.888 |
| pods started | 1 | 3 | 0 | 0 | 5 | 6 | 0 | 2 | 4 | 4 | 5 | 5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 291.5 | 286.2 | 291 | 287.6 | 272.6 | 273.2 | 289.9 | 284.5 | 478.9 | 469 | 719.4 | 713.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 291.5 | 286.2 | 291 | 287.6 | 272.6 | 273.2 | 289.9 | 284.5 | 478.9 | 469 | 719.4 | 713.5 |
| CPU used with Omni's own (cores), mean | 3.314 | 3.037 | 3.295 | 3.124 | 2.193 | 2.177 | 3.291 | 3.056 | 3.191 | 2.888 | 3.243 | 3.069 |
| host CPU busy, the real machine under kind (%) | 98.56 | 99 | 98.33 | 98.7 | 65.1 | 68.38 | 98.32 | 98.78 | 98.45 | 98.93 | 94.06 | 97.45 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 | 6.88e+12 | 6.88e+12 | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 | 1.103e+15 | 1.103e+15 | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 | 2.589 | 2.551 | 2.524 | 2.439 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 | 0.006235 | 0.006235 | 0.01188 | 0.01188 |
| organism behind its window (s) | 1.3 | 2.2 | 1.8 | 1.7 | 0.4 | 0.6 | 1.6 | 2.9 | 3.5 | 4.9 | 4.5 | 5.6 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 6021 | 3373 | -44.0% |  | better (inside the noise) |
| response time (ms), 99th percentile | 8573 | 7295 | -14.9% |  | better (inside the noise) |
| time over the response line (% of samples) | 81.14 | 75.43 | -7.0% |  | better (inside the noise) |
| failed requests (%) | 64 | 65.14 | +1.8% |  | WORSE (inside the noise) |
| HPA replicas, mean | 9.955 | 9.864 | -0.9% |  | better (inside the noise) |
| pods started | 1 | 3 | +200.0% |  | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 291.5 | 286.2 | -1.8% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 291.5 | 286.2 | -1.8% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.314 | 3.037 | -8.4% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 98.56 | 99 | +0.4% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% |  | same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% |  | better (inside the noise) |
| organism work per energy | 1.377 | 1.376 | -0.1% |  | WORSE (inside the noise) |
| organism behind its window (s) | 1.3 | 2.2 | +69.2% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 6153 | 3304 | -46.3% |  | better (inside the noise) |
| response time (ms), 99th percentile | 8142 | 6198 | -23.9% |  | better (inside the noise) |
| time over the response line (% of samples) | 78.33 | 70.81 | -9.6% |  | better (inside the noise) |
| failed requests (%) | 62.22 | 60.54 | -2.7% |  | better (inside the noise) |
| HPA replicas, mean | 10 | 10 | +0.0% |  | same (under one part in a million) |
| pods started | 0 | 0 | +0 |  | same |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 291 | 287.6 | -1.2% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 291 | 287.6 | -1.2% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.295 | 3.124 | -5.2% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 98.33 | 98.7 | +0.4% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% |  | same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% |  | better (inside the noise) |
| organism work per energy | 1.118 | 1.117 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 1.8 | 1.7 | -5.6% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 476.2 | 218.6 | -54.1% |  | better (inside the noise) |
| response time (ms), 99th percentile | 930 | 408.9 | -56.0% |  | better (inside the noise) |
| time over the response line (% of samples) | 4.215 | 0.5344 | -87.3% |  | better (inside the noise) |
| failed requests (%) | 0 | 0 | +0 |  | same |
| HPA replicas, mean | 9.731 | 9.678 | -0.5% |  | better (inside the noise) |
| pods started | 5 | 6 | +20.0% |  | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 273.2 | +0.2% |  | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 273.2 | +0.2% |  | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.193 | 2.177 | -0.8% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 65.1 | 68.38 | +5.0% |  | shown, not judged (more or less is not better by itself) |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% |  | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% |  | better (inside the noise) |
| organism work per energy | 0.006054 | 0.006054 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 0.4 | 0.6 | +50.0% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3924 | 2612 | -33.4% |  | better (inside the noise) |
| response time (ms), 99th percentile | 7898 | 5403 | -31.6% |  | better (inside the noise) |
| time over the response line (% of samples) | 77.71 | 73.51 | -5.4% |  | better (inside the noise) |
| failed requests (%) | 64 | 64.86 | +1.4% |  | WORSE (inside the noise) |
| HPA replicas, mean | 10 | 9.908 | -0.9% |  | better (inside the noise) |
| pods started | 0 | 2 | +2 |  | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 289.9 | 284.5 | -1.9% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 289.9 | 284.5 | -1.9% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.291 | 3.056 | -7.1% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 98.32 | 98.78 | +0.5% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% |  | same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% |  | better (inside the noise) |
| organism work per energy | 0.3794 | 0.3793 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 1.6 | 2.9 | +81.2% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 100 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5784 | 5127 | -11.4% |  | better (inside the noise) |
| response time (ms), 99th percentile | 8178 | 9299 | +13.7% |  | WORSE (inside the noise) |
| time over the response line (% of samples) | 81.09 | 74.58 | -8.0% |  | better (inside the noise) |
| failed requests (%) | 66.91 | 61.69 | -7.8% |  | better (inside the noise) |
| HPA replicas, mean | 9.88 | 9.879 | -0.0% |  | better (inside the noise) |
| pods started | 4 | 4 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 478.9 | 469 | -2.1% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 478.9 | 469 | -2.1% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.191 | 2.888 | -9.5% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 98.45 | 98.93 | +0.5% |  | shown, not judged (more or less is not better by itself) |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% |  | same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% |  | better (inside the noise) |
| organism work per energy | 0.006235 | 0.006235 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 3.5 | 4.9 | +40.0% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 100 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3148 | 4461 | +41.7% |  | WORSE (inside the noise) |
| response time (ms), 99th percentile | 5009 | 8221 | +64.1% |  | WORSE (inside the noise) |
| time over the response line (% of samples) | 54.63 | 38.83 | -28.9% |  | better (inside the noise) |
| failed requests (%) | 0.4432 | 10.39 | +2244.4% |  | WORSE (inside the noise) |
| HPA replicas, mean | 9.888 | 9.888 | +0.0% |  | WORSE (inside the noise) |
| pods started | 5 | 5 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 719.4 | 713.5 | -0.8% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 719.4 | 713.5 | -0.8% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.243 | 3.069 | -5.4% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 94.06 | 97.45 | +3.6% |  | shown, not judged (more or less is not better by itself) |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% |  | same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% |  | better (inside the noise) |
| organism work per energy | 0.01188 | 0.01188 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 4.5 | 5.6 | +24.4% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
