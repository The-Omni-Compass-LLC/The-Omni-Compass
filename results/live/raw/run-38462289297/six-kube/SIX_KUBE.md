# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2375 | 4446 |
| response time (ms), 99th percentile | 5181 | 6843 |
| time over the response line (% of samples) | 58.6 | 58.2 |
| failed requests (%) | 44.63 | 45.42 |
| HPA replicas, mean | 9.886 | 14.51 |
| pods started | 5.3 | 10.8 |
| worker nodes in service, mean | 6 | 5.997 |
| energy, parked workers still on at idle power (Wh, declared model) | 690.2 | 690 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 690.2 | 689.8 |
| CPU used with Omni's own (cores), mean | 2.474 | 2.514 |
| host CPU busy, the real machine under kind (%) | 77.2 | 87.19 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.524 | 2.439 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 3.03 | 4.13 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: lower on 2 (organism time over the line (% of steps); organism work per energy), higher on 5 (response time (ms), 95th percentile; response time (ms), 99th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2375 | 4446 | +87.2% | +859.2 to +3283 | higher |
| response time (ms), 99th percentile | 5181 | 6843 | +32.1% | +598.3 to +2726 | higher |
| time over the response line (% of samples) | 58.6 | 58.2 | -0.7% | -1.939 to +1.138 | lower (inside the noise) |
| failed requests (%) | 44.63 | 45.42 | +1.8% | -2.367 to +3.945 | higher (inside the noise) |
| HPA replicas, mean | 9.886 | 14.51 | +46.7% | +3.086 to +6.154 | higher |
| pods started | 5.3 | 10.8 | +103.8% | +4.059 to +6.941 | higher |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.009209 to +0.003563 | lower (inside the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | 690.2 | 690 | -0.0% | -3.934 to +3.518 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 690.2 | 689.8 | -0.1% | -4.597 to +3.756 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.474 | 2.514 | +1.6% | +0.005928 to +0.07354 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.2 | 87.19 | +12.9% | +9.43 to +10.55 | shown, not judged |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | higher |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | lower |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | lower |
| organism behind its window (s) | 3.03 | 4.13 | +36.3% | +0.6364 to +1.564 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
