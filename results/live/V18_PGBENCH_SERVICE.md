# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40135948429 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| B | 40137076834 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| C | 40138213124 | `96ebf29137fe` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,879, 16,623, 16,353 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,422 | 7,355 | -0.9% (-4.7 to +2.9) | -0.3% (-0.8 to +0.2) | -0.2% (-1.0 to +0.6) | EVEN, under the floor (the three runs' mean 0.47%) |
| throughput (transactions a second) | 7,422 | 7,424 | +0.0% (-0.3 to +0.4) | -0.1% (-0.3 to +0.1) | +0.1% (-0.1 to +0.3) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms, lag included) | 1.85 | 2.45 | +32.1% (-68.1 to +132.3) | +31.3% (-142.9 to +205.5) | -31.9% (-127.8 to +63.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 5.4 | 52.3 | +868.9% (-2847.1 to +4585.0) | +100.7% (-295.6 to +497.1) | +121.6% (-418.0 to +661.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.378 | 0.376 | -0.4% (-2.7 to +1.9) | +0.7% (-2.4 to +3.9) | -2.0% (-8.0 to +4.0) | **the runs disagree** |
| latency, mean (ms) | 0.646 | 1.88 | +190.6% (-610.3 to +991.5) | +51.2% (-84.2 to +186.7) | +29.4% (-69.0 to +127.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.2 | 15.6 | -18.8% (-36.8 to -0.8) | -13.4% (-28.0 to +1.1) | -24.9% (-35.0 to -14.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.339 | 0.337 | -0.5% (-3.9 to +3.0) | +0.9% (-3.0 to +4.7) | -2.8% (-11.2 to +5.5) | **the runs disagree** |
| host CPU-seconds | 501.4 | 498.7 | -0.5% (-4.4 to +3.3) | +1.1% (-3.4 to +5.6) | -3.2% (-12.8 to +6.3) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.151 | +0.4% (-2.0 to +2.8) | +1.4% (-3.2 to +6.0) | -3.0% (-12.5 to +6.4) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.69 | 3.43 | +27.3% (+18.4 to +36.1) | +32.2% (+27.6 to +36.7) | +29.9% (+26.9 to +32.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.2 | -18.8% (-30.8 to -6.9) | -13.5% (-22.1 to -4.9) | -22.1% (-37.9 to -6.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 14 to 20 (10 trials, 6 allowed, 3 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused); acting: 11 to 20 (12 trials, 9 allowed, 2 refused); run B: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused); run C: acting: 11 to 20 (12 trials, 9 allowed, 3 refused); acting: 16 to 20 (9 trials, 4 allowed, 5 refused); acting: 11 to 20 (12 trials, 9 allowed, 2 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 5,535, 6,705, 3,913 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,376 | 2,367 | -0.4% (-1.8 to +1.0) | +0.6% (-1.4 to +2.6) | -0.1% (-3.6 to +3.4) | EVEN, under the floor (the three runs' mean 0.04%) |
| throughput (transactions a second) | 2,434 | 2,433 | -0.0% (-0.1 to +0.1) | -0.1% (-0.7 to +0.5) | +0.0% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 4.19 | 4.16 | -0.8% (-46.5 to +44.9) | -72.4% (-277.8 to +133.0) | +13.0% (-103.3 to +129.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 185.7 | 207.0 | +11.4% (-30.7 to +53.6) | -9.1% (-13.1 to -5.1) | +13.2% (-49.9 to +76.2) | **the runs disagree** |
| latency, median (ms) | 1.06 | 1.04 | -2.2% (-7.6 to +3.2) | -2.2% (-14.2 to +9.8) | +0.2% (-1.0 to +1.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 5.47 | 6.18 | +12.9% (-41.2 to +67.1) | -13.3% (-37.3 to +10.6) | +10.8% (-83.4 to +104.9) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.7% (-5.4 to -4.0) | -2.0% (-6.8 to +2.9) | -5.8% (-9.5 to -2.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | +8.3% (+1.2 to +15.5) | +6.7% (-0.5 to +13.8) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.416 | 0.411 | -1.3% (-4.7 to +2.2) | -2.0% (-12.3 to +8.2) | +0.3% (+0.0 to +0.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 721.6 | 712.3 | -1.3% (-4.7 to +2.2) | -2.0% (-12.2 to +8.2) | +0.3% (-0.1 to +0.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.675 | 0.669 | -0.9% (-3.5 to +1.7) | -2.6% (-13.9 to +8.6) | +0.5% (-3.1 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.08 | 1.66 | +54.6% (+50.7 to +58.5) | +60.1% (+58.9 to +61.4) | +77.0% (+73.8 to +80.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -3.8% (-4.1 to -3.5) | -1.6% (-6.7 to +3.4) | -4.6% (-7.5 to -1.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 21 (16 trials, 2 allowed, 5 refused); acting: 19 to 20 (14 trials, 1 allowed, 5 refused); acting: 19 to 20 (17 trials, 1 allowed, 4 refused); run B: acting: 19 to 21 (18 trials, 2 allowed, 4 refused); acting: 19 to 20 (15 trials, 1 allowed, 5 refused); acting: 19 to 21 (15 trials, 2 allowed, 4 refused); run C: acting: 18 to 21 (16 trials, 3 allowed, 4 refused); acting: 17 to 20 (13 trials, 3 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,440, 1,832, 1,192 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,505 | 1,507 | +0.2% (-1.7 to +2.0) | -5.3% (-9.0 to -1.6) | +7.8% (-25.5 to +41.0) | **the runs disagree** |
| throughput (transactions a second) | 1,513 | 1,512 | -0.0% (-0.4 to +0.4) | -1.4% (-5.1 to +2.3) | +0.4% (-0.9 to +1.6) | EVEN, under the floor (the three runs' mean 0.35%) |
| latency, 95th percentile (ms, lag included) | 2.43 | 2.14 | -12.0% (-81.2 to +57.2) | +242.6% (-293.6 to +778.7) | +39.8% (-233.2 to +312.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 25.0 | 20.4 | -18.6% (-343.2 to +306.0) | -6.5% (-66.6 to +53.6) | +44.0% (-262.5 to +350.4) | **the runs disagree** |
| latency, median (ms) | 0.862 | 0.847 | -1.8% (-10.2 to +6.5) | +4.8% (-6.2 to +15.9) | +13.2% (-230.0 to +256.3) | **the runs disagree** |
| latency, mean (ms) | 1.75 | 1.65 | -5.7% (-147.1 to +135.7) | +77.5% (-75.3 to +230.3) | +11.2% (-185.2 to +207.7) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.5 | -11.6% (-18.6 to -4.7) | -0.2% (-1.1 to +0.8) | -0.0% (-0.0 to +0.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | +5.0% (+5.0 to +5.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.234 | 0.23 | -1.4% (-9.2 to +6.4) | -1.1% (-5.3 to +3.1) | -1.2% (-6.9 to +4.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 402.3 | 396.8 | -1.4% (-9.1 to +6.4) | -1.0% (-5.5 to +3.5) | -1.2% (-7.2 to +4.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.594 | 0.585 | -1.5% (-10.8 to +7.7) | +4.5% (+1.1 to +8.0) | -7.4% (-39.4 to +24.7) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.6 | 1.13 | +87.6% (+75.5 to +99.8) | +94.2% (+89.9 to +98.5) | +100.7% (+97.2 to +104.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -11.0% (-18.1 to -3.8) | -0.2% (-0.8 to +0.3) | -0.0% (-0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 21 (9 trials, 3 allowed, 4 refused); acting: 15 to 20 (12 trials, 5 allowed, 4 refused); acting: 15 to 21 (11 trials, 6 allowed, 2 refused); run B: left native (22 trials, 0 allowed, 0 refused); left native (23 trials, 0 allowed, 0 refused); left native (25 trials, 0 allowed, 2 refused); run C: left native (19 trials, 0 allowed, 0 refused); left native (23 trials, 0 allowed, 0 refused); left native (30 trials, 0 allowed, 0 refused).

**Across 3 workloads: 9 gauge-rows GAIN, 2 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 9 EVEN, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
