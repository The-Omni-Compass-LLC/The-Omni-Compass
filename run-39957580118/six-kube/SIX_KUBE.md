# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3060 | 2062 | 3752 | 2368 | 3853 | 2474 | 3176 | 2710 | 2835 | 3337 |
| response time (ms), 99th percentile | 4977 | 4040 | 5656 | 4321 | 6169 | 4849 | 5454 | 5004 | 4661 | 5486 |
| time over the response line (% of samples) | 41.82 | 41.38 | 53.18 | 51.5 | 56.54 | 55.24 | 48.66 | 46.92 | 53.62 | 53.37 |
| failed requests (%) | 29.02 | 33.22 | 41.05 | 43.58 | 43.03 | 46.83 | 37.49 | 37.69 | 44.11 | 43.2 |
| HPA replicas, mean | 9.751 | 13.43 | 9.782 | 11.68 | 9.818 | 12.24 | 9.796 | 11.82 | 9.806 | 12 |
| pods started | 5.125 | 11.6 | 4.65 | 8.125 | 3.925 | 9.1 | 4.225 | 9.825 | 4.15 | 8.075 |
| worker nodes in service, mean | 5.996 | 6 | 6 | 6 | 6 | 5.995 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.7 | 275.6 | 276.3 | 276.6 | 276.8 | 275.5 | 275.7 | 276.3 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 275.7 | 275.6 | 276.3 | 276.6 | 276.7 | 275.5 | 275.7 | 276.3 | 276.8 |
| CPU used with Omni's own (cores), mean | 2.327 | 2.384 | 2.388 | 2.461 | 2.431 | 2.476 | 2.356 | 2.407 | 2.428 | 2.495 |
| host CPU busy, the real machine under kind (%) | 68.81 | 73.55 | 72.71 | 81.35 | 74.73 | 80.06 | 72.43 | 78.97 | 73.75 | 81.82 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.39 | 0.525 | 0.8725 | 1.198 | 0.615 | 0.4275 | 0.6975 | 0.4025 | 0.53 | 1.07 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 2

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3060 | 2062 | -32.6% | -1523 to -473.1 | GAIN |
| response time (ms), 99th percentile | 4977 | 4040 | -18.8% | -1498 to -377.2 | GAIN |
| time over the response line (% of samples) | 41.82 | 41.38 | -1.1% | -1.681 to +0.7912 | EVEN, inside the noise (cut) |
| failed requests (%) | 29.02 | 33.22 | +14.4% | +2.327 to +6.058 | LOSS |
| HPA replicas, mean | 9.751 | 13.43 | +37.8% | +3.277 to +4.088 | power given |
| pods started | 5.125 | 11.6 | +126.3% | +5.403 to +7.547 | power given |
| worker nodes in service, mean | 5.996 | 6 | +0.1% | -0.003618 to +0.01069 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.7 | +0.4% | +0.3667 to +1.831 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 275.7 | +0.4% | +0.3068 to +2.103 | power given |
| CPU used with Omni's own (cores), mean | 2.327 | 2.384 | +2.5% | +0.04469 to +0.07084 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.81 | 73.55 | +6.9% | +4.455 to +5.019 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.39 | 0.525 | +34.6% | +0.06879 to +0.2012 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), EVEN (inside the noise) on 0

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3752 | 2368 | -36.9% | -2048 to -720.3 | GAIN |
| response time (ms), 99th percentile | 5656 | 4321 | -23.6% | -2021 to -649 | GAIN |
| time over the response line (% of samples) | 53.18 | 51.5 | -3.2% | -3.348 to -0.01046 | GAIN |
| failed requests (%) | 41.05 | 43.58 | +6.2% | +0.9751 to +4.09 | LOSS |
| HPA replicas, mean | 9.782 | 11.68 | +19.4% | +1.179 to +2.608 | power given |
| pods started | 4.65 | 8.125 | +74.7% | +2.498 to +4.452 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.115e-15 to +4.896e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 276.3 | +0.2% | +0.01391 to +1.305 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 276.3 | +0.2% | +0.01391 to +1.305 | power given |
| CPU used with Omni's own (cores), mean | 2.388 | 2.461 | +3.1% | +0.04263 to +0.1035 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.71 | 81.35 | +11.9% | +7.884 to +9.408 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.8725 | 1.198 | +37.2% | +0.2284 to +0.4216 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3853 | 2474 | -35.8% | -1916 to -841.4 | GAIN |
| response time (ms), 99th percentile | 6169 | 4849 | -21.4% | -1966 to -674.4 | GAIN |
| time over the response line (% of samples) | 56.54 | 55.24 | -2.3% | -2.287 to -0.3209 | GAIN |
| failed requests (%) | 43.03 | 46.83 | +8.8% | +1.863 to +5.746 | LOSS |
| HPA replicas, mean | 9.818 | 12.24 | +24.6% | +1.898 to +2.938 | power given |
| pods started | 3.925 | 9.1 | +131.8% | +4.005 to +6.345 | power given |
| worker nodes in service, mean | 6 | 5.995 | -0.1% | -0.01251 to +0.002417 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 276.8 | +0.1% | -0.3699 to +0.8763 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.7 | +0.0% | -0.6627 to +0.8638 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.431 | 2.476 | +1.9% | +0.02704 to +0.06306 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.73 | 80.06 | +7.1% | +4.876 to +5.778 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.615 | 0.4275 | -30.5% | -0.252 to -0.123 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3176 | 2710 | -14.7% | -993.6 to +60.62 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5454 | 5004 | -8.3% | -1004 to +102.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 48.66 | 46.92 | -3.6% | -2.653 to -0.8286 | GAIN |
| failed requests (%) | 37.49 | 37.69 | +0.5% | -0.9682 to +1.35 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.796 | 11.82 | +20.6% | +1.358 to +2.684 | power given |
| pods started | 4.225 | 9.825 | +132.5% | +4.091 to +7.109 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0008848 to +0.0002994 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.7 | +0.1% | -0.3466 to +0.7878 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.7 | +0.1% | -0.3581 to +0.7816 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.356 | 2.407 | +2.2% | +0.02937 to +0.07421 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.43 | 78.97 | +9.0% | +5.895 to +7.183 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.6975 | 0.4025 | -42.3% | -0.3569 to -0.2331 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 6

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2835 | 3337 | +17.7% | -239.3 to +1242 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4661 | 5486 | +17.7% | +24.95 to +1625 | LOSS |
| time over the response line (% of samples) | 53.62 | 53.37 | -0.5% | -1.235 to +0.7376 | EVEN, inside the noise (cut) |
| failed requests (%) | 44.11 | 43.2 | -2.1% | -2.467 to +0.6572 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.806 | 12 | +22.4% | +1.418 to +2.975 | power given |
| pods started | 4.15 | 8.075 | +94.6% | +2.884 to +4.966 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002192 to +0.0004321 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.8 | +0.2% | -0.0427 to +1.133 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.8 | +0.2% | -0.07386 to +1.111 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.428 | 2.495 | +2.7% | +0.04269 to +0.09073 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.75 | 81.82 | +10.9% | +7.456 to +8.682 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.53 | 1.07 | +101.9% | +0.4459 to +0.6341 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
