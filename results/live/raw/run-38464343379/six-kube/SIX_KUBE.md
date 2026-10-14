# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2880 | 4255 |
| response time (ms), 99th percentile | 6244 | 6670 |
| time over the response line (% of samples) | 66.33 | 64.2 |
| failed requests (%) | 51.43 | 50.41 |
| HPA replicas, mean | 9.836 | 15.19 |
| pods started | 5.1 | 10.9 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 463.1 | 464 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 463.1 | 464 |
| CPU used with Omni's own (cores), mean | 2.57 | 2.611 |
| host CPU busy, the real machine under kind (%) | 80.43 | 88.55 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 1.79 | 2.36 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 3 (response time (ms), 95th percentile; HPA replicas, mean; pods started), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2880 | 4255 | +47.7% | +218.4 to +2531 | higher |
| response time (ms), 99th percentile | 6244 | 6670 | +6.8% | -1809 to +2662 | higher (inside the noise) |
| time over the response line (% of samples) | 66.33 | 64.2 | -3.2% | -3.464 to -0.7894 | lower |
| failed requests (%) | 51.43 | 50.41 | -2.0% | -4.389 to +2.339 | lower (inside the noise) |
| HPA replicas, mean | 9.836 | 15.19 | +54.4% | +4.879 to +5.831 | higher |
| pods started | 5.1 | 10.9 | +113.7% | +5.498 to +6.102 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.588e-16 to +1.014e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 463.1 | 464 | +0.2% | -0.8966 to +2.636 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 463.1 | 464 | +0.2% | -0.8966 to +2.636 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.57 | 2.611 | +1.6% | +0.001611 to +0.08056 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 80.43 | 88.55 | +10.1% | +7.155 to +9.083 | shown, not judged |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | lower |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.79 | 2.36 | +31.8% | +0.3001 to +0.8399 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
