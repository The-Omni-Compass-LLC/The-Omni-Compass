# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2111 | 2016 |
| response time (ms), 99th percentile | 5000 | 4415 |
| time over the response line (% of samples) | 58.11 | 54.55 |
| failed requests (%) | 47.6 | 46.66 |
| HPA replicas, mean | 9.918 | 9.904 |
| pods started | 5.3 | 5.3 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1064 | 1055 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1064 | 1055 |
| CPU used with Omni's own (cores), mean | 3.004 | 2.842 |
| host CPU busy, the real machine under kind (%) | 89.24 | 90.97 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.524 | 2.439 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 5.03 | 5.95 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2111 | 2016 | -4.5% | -736.8 to +546.8 | better (inside the noise) |
| response time (ms), 99th percentile | 5000 | 4415 | -11.7% | -2235 to +1065 | better (inside the noise) |
| time over the response line (% of samples) | 58.11 | 54.55 | -6.1% | -4.937 to -2.183 | better |
| failed requests (%) | 47.6 | 46.66 | -2.0% | -1.758 to -0.1098 | better |
| HPA replicas, mean | 9.918 | 9.904 | -0.1% | -0.02062 to -0.00695 | better |
| pods started | 5.3 | 5.3 | +0.0% | -0.3372 to +0.3372 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.267e-16 to +1.294e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1064 | 1055 | -0.8% | -13.06 to -4.957 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1064 | 1055 | -0.8% | -13.06 to -4.957 | better |
| CPU used with Omni's own (cores), mean | 3.004 | 2.842 | -5.4% | -0.2273 to -0.09643 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.24 | 90.97 | +1.9% | +0.07675 to +3.384 | shown, not judged (more or less is not better by itself) |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | WORSE |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | better |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | WORSE |
| organism behind its window (s) | 5.03 | 5.95 | +18.3% | +0.2585 to +1.581 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
