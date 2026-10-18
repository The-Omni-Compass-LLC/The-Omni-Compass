# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2260 | 3297 |
| response time (ms), 99th percentile | 4332 | 5430 |
| time over the response line (% of samples) | 49.42 | 42.06 |
| failed requests (%) | 33.09 | 30.18 |
| HPA replicas, mean | 9.876 | 9.876 |
| pods started | 4.9 | 5 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 707.4 | 703.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 707.4 | 703.4 |
| CPU used with Omni's own (cores), mean | 2.933 | 2.832 |
| host CPU busy, the real machine under kind (%) | 86.88 | 89.01 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 2.74 | 3.99 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: better on 5, worse on 1 (response time (ms), 95th percentile), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2260 | 3297 | +45.9% | +145.9 to +1927 | WORSE |
| response time (ms), 99th percentile | 4332 | 5430 | +25.4% | -95.71 to +2293 | WORSE (inside the noise) |
| time over the response line (% of samples) | 49.42 | 42.06 | -14.9% | -11.17 to -3.561 | better |
| failed requests (%) | 33.09 | 30.18 | -8.8% | -5.669 to -0.1444 | better |
| HPA replicas, mean | 9.876 | 9.876 | -0.0% | -0.007453 to +0.007004 | better (inside the noise) |
| pods started | 4.9 | 5 | +2.0% | -0.1262 to +0.3262 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.063e-16 to +7.286e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 707.4 | 703.4 | -0.6% | -6.612 to -1.392 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 707.4 | 703.4 | -0.6% | -6.612 to -1.392 | better |
| CPU used with Omni's own (cores), mean | 2.933 | 2.832 | -3.4% | -0.1647 to -0.03644 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.88 | 89.01 | +2.4% | +0.7266 to +3.529 | shown, not judged (more or less is not better by itself) |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | better |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | same (under one part in a million) |
| organism behind its window (s) | 2.74 | 3.99 | +45.6% | +0.5629 to +1.937 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
