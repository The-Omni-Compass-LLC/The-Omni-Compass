# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

Each square here is its first 1 repetition (repetitions 1 to 1; the grid's 1-, 10- and 100-repetition squares are nested).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1387 | 586.8 | 1006 | 396.9 | 3071 | 2585 | 314.8 | 79.7 | 287.9 | 92.32 | 297.9 | 99.84 |
| response time (ms), 99th percentile | 3282 | 3205 | 2750 | 947.5 | 6699 | 7226 | 490.3 | 132 | 565.8 | 149.5 | 467.4 | 188.7 |
| time over the response line (% of samples) | 33.92 | 6.533 | 18.82 | 3.558 | 39.17 | 15.25 | 0.9357 | 0 | 1.395 | 0 | 0.9302 | 0.221 |
| failed requests (%) | 0.16 | 0.1333 | 0.2941 | 0.1227 | 2.708 | 1.186 | 0 | 0 | 0 | 0 | 0 | 0 |
| HPA replicas, mean | 9.65 | 9.627 | 9.542 | 9.658 | 9.656 | 9.685 | 9.485 | 9.455 | 9.483 | 9.421 | 9.474 | 9.485 |
| pods started | 6 | 6 | 6 | 5 | 6 | 5 | 7 | 7 | 7 | 7 | 7 | 7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 190.1 | 189.7 | 186.1 | 185.1 | 191.4 | 190.1 | 176.1 | 175.2 | 177 | 177 | 176.8 | 176.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.1 | 189.7 | 186.1 | 185.1 | 191.4 | 190.1 | 176.1 | 175.2 | 177 | 177 | 176.8 | 176.6 |
| CPU used with Omni's own (cores), mean | 2.919 | 2.887 | 2.606 | 2.485 | 3.073 | 3.023 | 1.596 | 1.53 | 1.653 | 1.639 | 1.642 | 1.557 |
| host CPU busy, the real machine under kind (%) | 83.79 | 84.09 | 76.05 | 74.3 | 87.69 | 86.46 | 46.82 | 45.38 | 50.17 | 50.24 | 49.38 | 49.57 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 | 0.1 | 0.1 | 0.1 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1387 | 586.8 | -57.7% |  | better (inside the noise) |
| response time (ms), 99th percentile | 3282 | 3205 | -2.3% |  | better (inside the noise) |
| time over the response line (% of samples) | 33.92 | 6.533 | -80.7% |  | better (inside the noise) |
| failed requests (%) | 0.16 | 0.1333 | -16.7% |  | better (inside the noise) |
| HPA replicas, mean | 9.65 | 9.627 | -0.2% |  | better (inside the noise) |
| pods started | 6 | 6 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same |
| energy, parked workers still on at idle power (Wh, declared model) | 190.1 | 189.7 | -0.2% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.1 | 189.7 | -0.2% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.919 | 2.887 | -1.1% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 83.79 | 84.09 | +0.4% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% |  | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% |  | better (inside the noise) |
| organism work per energy | 1.377 | 1.376 | -0.1% |  | WORSE (inside the noise) |
| organism behind its window (s) | 0.1 | 0 | -100.0% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1006 | 396.9 | -60.5% |  | better (inside the noise) |
| response time (ms), 99th percentile | 2750 | 947.5 | -65.6% |  | better (inside the noise) |
| time over the response line (% of samples) | 18.82 | 3.558 | -81.1% |  | better (inside the noise) |
| failed requests (%) | 0.2941 | 0.1227 | -58.3% |  | better (inside the noise) |
| HPA replicas, mean | 9.542 | 9.658 | +1.2% |  | WORSE (inside the noise) |
| pods started | 6 | 5 | -16.7% |  | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same |
| energy, parked workers still on at idle power (Wh, declared model) | 186.1 | 185.1 | -0.5% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.1 | 185.1 | -0.5% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.606 | 2.485 | -4.7% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 76.05 | 74.3 | -2.3% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% |  | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% |  | better (inside the noise) |
| organism work per energy | 1.123 | 1.123 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3071 | 2585 | -15.8% |  | better (inside the noise) |
| response time (ms), 99th percentile | 6699 | 7226 | +7.9% |  | WORSE (inside the noise) |
| time over the response line (% of samples) | 39.17 | 15.25 | -61.1% |  | better (inside the noise) |
| failed requests (%) | 2.708 | 1.186 | -56.2% |  | better (inside the noise) |
| HPA replicas, mean | 9.656 | 9.685 | +0.3% |  | WORSE (inside the noise) |
| pods started | 6 | 5 | -16.7% |  | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same |
| energy, parked workers still on at idle power (Wh, declared model) | 191.4 | 190.1 | -0.6% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.4 | 190.1 | -0.6% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.073 | 3.023 | -1.6% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 87.69 | 86.46 | -1.4% |  | shown, not judged (more or less is not better by itself) |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% |  | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% |  | better (inside the noise) |
| organism work per energy | 0.006055 | 0.006055 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 314.8 | 79.7 | -74.7% |  | better (inside the noise) |
| response time (ms), 99th percentile | 490.3 | 132 | -73.1% |  | better (inside the noise) |
| time over the response line (% of samples) | 0.9357 | 0 | -100.0% |  | better (inside the noise) |
| failed requests (%) | 0 | 0 | +0 |  | same |
| HPA replicas, mean | 9.485 | 9.455 | -0.3% |  | better (inside the noise) |
| pods started | 7 | 7 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same |
| energy, parked workers still on at idle power (Wh, declared model) | 176.1 | 175.2 | -0.5% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.1 | 175.2 | -0.5% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.596 | 1.53 | -4.1% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 46.82 | 45.38 | -3.1% |  | shown, not judged (more or less is not better by itself) |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% |  | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% |  | better (inside the noise) |
| organism work per energy | 0.3913 | 0.3912 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 287.9 | 92.32 | -67.9% |  | better (inside the noise) |
| response time (ms), 99th percentile | 565.8 | 149.5 | -73.6% |  | better (inside the noise) |
| time over the response line (% of samples) | 1.395 | 0 | -100.0% |  | better (inside the noise) |
| failed requests (%) | 0 | 0 | +0 |  | same |
| HPA replicas, mean | 9.483 | 9.421 | -0.7% |  | better (inside the noise) |
| pods started | 7 | 7 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177 | 177 | -0.0% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177 | 177 | -0.0% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.653 | 1.639 | -0.9% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 50.17 | 50.24 | +0.1% |  | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% |  | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% |  | better (inside the noise) |
| organism work per energy | 0.006233 | 0.006233 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.1 | +0.0% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 297.9 | 99.84 | -66.5% |  | better (inside the noise) |
| response time (ms), 99th percentile | 467.4 | 188.7 | -59.6% |  | better (inside the noise) |
| time over the response line (% of samples) | 0.9302 | 0.221 | -76.2% |  | better (inside the noise) |
| failed requests (%) | 0 | 0 | +0 |  | same |
| HPA replicas, mean | 9.474 | 9.485 | +0.1% |  | WORSE (inside the noise) |
| pods started | 7 | 7 | +0.0% |  | same |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 176.8 | 176.6 | -0.1% |  | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176.8 | 176.6 | -0.1% |  | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.642 | 1.557 | -5.1% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 49.38 | 49.57 | +0.4% |  | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% |  | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% |  | WORSE (inside the noise) |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% |  | better (inside the noise) |
| organism work per energy | 0.012 | 0.012 | -0.0% |  | WORSE (inside the noise) |
| organism behind its window (s) | 0.1 | 0.1 | +0.0% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
