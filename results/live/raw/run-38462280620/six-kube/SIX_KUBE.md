# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3473 | 3706 | 3986 | 4756 | 5104 | 3879 | 2220 | 2322 |
| response time (ms), 99th percentile | 5365 | 5522 | 6267 | 7012 | 6871 | 6062 | 3475 | 3480 |
| time over the response line (% of samples) | 53.22 | 52.6 | 62.23 | 60.32 | 66.46 | 64.85 | 23.1 | 27.79 |
| failed requests (%) | 41.18 | 42.26 | 48.87 | 48.83 | 51.23 | 53.63 | 14.86 | 20.58 |
| HPA replicas, mean | 9.865 | 15.11 | 9.853 | 14.37 | 9.894 | 15.24 | 9.729 | 13.58 |
| pods started | 3 | 9 | 3.2 | 8 | 2.5 | 8.4 | 5.2 | 10.2 |
| worker nodes in service, mean | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 277 | 277 | 277.6 | 277.9 | 278.4 | 272.4 | 273.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 277 | 277 | 277.6 | 277.9 | 278.4 | 272.4 | 273.7 |
| CPU used with Omni's own (cores), mean | 2.423 | 2.476 | 2.485 | 2.525 | 2.543 | 2.575 | 2.187 | 2.263 |
| host CPU busy, the real machine under kind (%) | 74.25 | 82.11 | 76.24 | 81.24 | 78.64 | 83.95 | 65.5 | 73.18 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.96 | 1.33 | 0.43 | 0.79 | 0.82 | 0.88 | 0.44 | 0.95 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: lower on 2 (organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3473 | 3706 | +6.7% | -628.7 to +1095 | higher (inside the noise) |
| response time (ms), 99th percentile | 5365 | 5522 | +2.9% | -818.6 to +1133 | higher (inside the noise) |
| time over the response line (% of samples) | 53.22 | 52.6 | -1.2% | -1.629 to +0.3978 | lower (inside the noise) |
| failed requests (%) | 41.18 | 42.26 | +2.6% | -0.4124 to +2.573 | higher (inside the noise) |
| HPA replicas, mean | 9.865 | 15.11 | +53.2% | +4.746 to +5.751 | higher |
| pods started | 3 | 9 | +200.0% | +4.988 to +7.012 | higher |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.003135 to +0.008104 | higher (inside the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 277 | +0.3% | -0.4211 to +2.284 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 277 | +0.4% | -0.3252 to +2.338 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.423 | 2.476 | +2.2% | +0.02118 to +0.08457 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.25 | 82.11 | +10.6% | +6.915 to +8.793 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | higher |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | lower |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | lower |
| organism behind its window (s) | 0.96 | 1.33 | +38.5% | +0.1131 to +0.6269 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: lower on 3 (time over the response line (% of samples); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3986 | 4756 | +19.3% | -512.6 to +2053 | higher (inside the noise) |
| response time (ms), 99th percentile | 6267 | 7012 | +11.9% | -684 to +2175 | higher (inside the noise) |
| time over the response line (% of samples) | 62.23 | 60.32 | -3.1% | -3.565 to -0.2541 | lower |
| failed requests (%) | 48.87 | 48.83 | -0.1% | -1.602 to +1.505 | lower (inside the noise) |
| HPA replicas, mean | 9.853 | 14.37 | +45.8% | +2.968 to +6.059 | higher |
| pods started | 3.2 | 8 | +150.0% | +3.226 to +6.374 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.622e-15 to +1.355e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.6 | +0.2% | -0.3599 to +1.577 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.6 | +0.2% | -0.3599 to +1.577 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.485 | 2.525 | +1.6% | +0.02204 to +0.05756 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.24 | 81.24 | +6.6% | +4.7 to +5.299 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | higher |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | lower |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | lower |
| organism behind its window (s) | 0.43 | 0.79 | +83.7% | +0.2202 to +0.4998 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: lower on 1 (organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5104 | 3879 | -24.0% | -2786 to +337 | lower (inside the noise) |
| response time (ms), 99th percentile | 6871 | 6062 | -11.8% | -2763 to +1144 | lower (inside the noise) |
| time over the response line (% of samples) | 66.46 | 64.85 | -2.4% | -3.514 to +0.2941 | lower (inside the noise) |
| failed requests (%) | 51.23 | 53.63 | +4.7% | -1.575 to +6.373 | higher (inside the noise) |
| HPA replicas, mean | 9.894 | 15.24 | +54.0% | +4.885 to +5.806 | higher |
| pods started | 2.5 | 8.4 | +236.0% | +4.618 to +7.182 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.594e-16 to +7.818e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.9 | 278.4 | +0.2% | -0.9419 to +1.903 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.9 | 278.4 | +0.2% | -0.9419 to +1.903 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.543 | 2.575 | +1.3% | +0.0201 to +0.04415 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.64 | 83.95 | +6.8% | +5.097 to +5.531 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | lower |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.82 | 0.88 | +7.3% | -0.05778 to +0.1778 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: lower on 2 (organism time over the line (% of steps); organism work per energy), higher on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2220 | 2322 | +4.6% | -810.1 to +1015 | higher (inside the noise) |
| response time (ms), 99th percentile | 3475 | 3480 | +0.1% | -290.2 to +300.2 | higher (inside the noise) |
| time over the response line (% of samples) | 23.1 | 27.79 | +20.3% | -3.409 to +12.8 | higher (inside the noise) |
| failed requests (%) | 14.86 | 20.58 | +38.4% | -2.212 to +13.64 | higher (inside the noise) |
| HPA replicas, mean | 9.729 | 13.58 | +39.5% | +2.204 to +5.489 | higher |
| pods started | 5.2 | 10.2 | +96.2% | +3.281 to +6.719 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.066e-15 to +1e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 273.7 | +0.5% | +0.6051 to +2.104 | higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 273.7 | +0.5% | +0.6051 to +2.104 | higher |
| CPU used with Omni's own (cores), mean | 2.187 | 2.263 | +3.5% | +0.05402 to +0.09916 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.5 | 73.18 | +11.7% | +6.936 to +8.439 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | higher |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | lower |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | lower |
| organism behind its window (s) | 0.44 | 0.95 | +115.9% | +0.4694 to +0.5506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
