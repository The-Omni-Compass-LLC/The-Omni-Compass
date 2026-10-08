# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Source: GitHub Actions workflow `big-organism-detached`, started by run 37564821425 and collected by run 37754612102 (`results/live/raw/run-37754612102/`): the four stacked at 1,000 copies on one rented Azure machine (eastus, `Standard_D8as_v4`, 8 vCPUs, 31 GB), a 10,800 s window an arm (240 organism steps of 45 s), three paired repetitions run one after another on the same machine over 29 hours (2026-10-07 03:07 to 2026-10-08 07:41 UTC), commit `126b8941`, **Omni v3** (`tools/omni_version.py --commit`), the machine deleted after the collect. Native: the stacks' own controllers and the cluster's HPA alone. Three repetitions give wide intervals on the paired rows; every row is shown.

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 1,000 copies: native | The four stacked, duplicates kept, 1,000 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2882 | 150 |
| response time (ms), 99th percentile | 5405 | 165.2 |
| time over the response line (% of samples) | 50.99 | 0 |
| failed requests (%) | 0.1415 | 0 |
| HPA replicas, mean | 9.952 | 9.951 |
| pods started | 5 | 5 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 2005 | 1992 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 2005 | 1992 |
| CPU used with Omni's own (cores), mean | 3.839 | 3.634 |
| host CPU busy, the real machine under kind (%) | 60.66 | 60.06 |
| organism work | 1.293e+14 | 1.293e+14 |
| organism energy (J) | 1.112e+16 | 1.107e+16 |
| organism time over the line (% of steps) | 2.585 | 2.567 |
| organism work per energy | 0.01163 | 0.01167 |
| organism behind its window (s) | 21.8 | 22.37 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 1,000 copies: better on 7, worse on 1 (organism work), inside the noise on 3

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2882 | 150 | -94.8% | -3113 to -2351 | better |
| response time (ms), 99th percentile | 5405 | 165.2 | -96.9% | -5593 to -4887 | better |
| time over the response line (% of samples) | 50.99 | 0 | -100.0% | -55.2 to -46.78 | better |
| failed requests (%) | 0.1415 | 0 | -100.0% | -0.1485 to -0.1345 | better |
| HPA replicas, mean | 9.952 | 9.951 | -0.0% | -0.01433 to +0.01248 | better (inside the noise) |
| pods started | 5 | 5 | +0.0% | +0 to +0 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.318e-15 to +3.095e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 2005 | 1992 | -0.6% | -26.58 to +2.121 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 2005 | 1992 | -0.6% | -26.58 to +2.121 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.839 | 3.634 | -5.3% | -0.3784 to -0.03194 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 60.66 | 60.06 | -1.0% | -3.166 to +1.972 | shown, not judged (more or less is not better by itself) |
| organism work | 1.293e+14 | 1.293e+14 | -0.0% | -7.813e+08 to -7.813e+08 | WORSE |
| organism energy (J) | 1.112e+16 | 1.107e+16 | -0.4% | -4.07e+13 to -4.07e+13 | better |
| organism time over the line (% of steps) | 2.585 | 2.567 | -0.7% | -0.01762 to -0.01762 | better |
| organism work per energy | 0.01163 | 0.01167 | +0.4% | +4.267e-05 to +4.267e-05 | better |
| organism behind its window (s) | 21.8 | 22.37 | +2.6% | -2.226 to +3.359 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
