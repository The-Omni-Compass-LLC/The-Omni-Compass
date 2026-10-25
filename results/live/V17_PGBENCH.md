# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40003718316 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 3 |
| B | 40022493643 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 3 |
| C | 40037187971 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |

> **Warning:** A, B and C are not all on the same engine.

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,523, 16,911, 16,367 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,269 | 7,267 | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.2) | +0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (transactions a second) | 7,269 | 7,267 | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.2) | +0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms, lag included) | 1.5 | 1.36 | -9.6% (-66.3 to +47.1) | -6.3% (-45.0 to +32.5) | -11.7% (-40.2 to +16.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 4.69 | 3.96 | -15.4% (-103.5 to +72.7) | -2.5% (-34.8 to +29.9) | -12.6% (-55.8 to +30.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.372 | 0.372 | +0.2% (-1.5 to +1.9) | +0.5% (-1.2 to +2.3) | +0.1% (-0.7 to +0.9) | STEADY, under the floor (the three runs' mean 0.27%) |
| latency, mean (ms) | 0.589 | 0.563 | -4.4% (-37.2 to +28.5) | -0.8% (-14.4 to +12.7) | -4.8% (-19.7 to +10.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.9 | 18.4 | -7.2% (-9.1 to -5.3) | -6.6% (-11.3 to -1.9) | -7.3% (-7.8 to -6.8) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.325 | 0.327 | +0.6% (-2.9 to +4.2) | +0.9% (-1.5 to +3.4) | +0.2% (-1.3 to +1.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 479.1 | 482.4 | +0.7% (-3.5 to +4.9) | +1.1% (-1.6 to +3.8) | +0.2% (-1.6 to +1.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.148 | +0.7% (-3.4 to +4.8) | +1.1% (-1.8 to +4.0) | +0.2% (-1.6 to +2.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.59 | 3.37 | +30.1% (+27.7 to +32.6) | +26.6% (+25.5 to +27.8) | +29.0% (+26.9 to +31.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.3% (-5.7 to -4.9) | -5.5% (-6.2 to -4.9) | -5.2% (-5.8 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,860, 3,802, 3,894 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,647 | 1,654 | +0.4% (-4.0 to +4.9) | +0.4% (-2.8 to +3.5) | -0.1% (-1.3 to +1.1) | STEADY, under the floor (the three runs' mean 0.23%) |
| throughput (transactions a second) | 1,696 | 1,699 | +0.1% (-0.6 to +0.9) | -0.1% (-0.2 to +0.1) | -0.2% (-1.0 to +0.6) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 9.82 | 8.51 | -13.4% (-84.1 to +57.4) | +2.9% (-58.5 to +64.3) | +2.0% (-5.2 to +9.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 210.5 | 189.1 | -10.2% (-126.9 to +106.6) | -11.2% (-84.1 to +61.7) | +2.1% (-57.0 to +61.2) | **the runs disagree** |
| latency, median (ms) | 1.57 | 1.58 | +0.4% (-0.5 to +1.3) | +2.4% (+0.5 to +4.3) | +0.0% (-2.7 to +2.8) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 7.49 | 6.84 | -8.7% (-116.5 to +99.1) | -9.5% (-94.6 to +75.5) | +1.3% (-56.4 to +59.0) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.2% (-9.9 to +3.4) | -3.8% (-9.4 to +1.8) | -1.6% (-5.1 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | +6.7% (-0.5 to +13.8) | +10.0% (+10.0 to +10.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.353 | 0.355 | +0.6% (-0.2 to +1.3) | +3.0% (+0.9 to +5.1) | +0.1% (-2.2 to +2.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 531.8 | 534.5 | +0.5% (-0.3 to +1.3) | +3.3% (+0.8 to +5.8) | +0.2% (-2.4 to +2.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.718 | 0.718 | +0.1% (-4.2 to +4.3) | +2.9% (+0.1 to +5.7) | +0.4% (-1.6 to +2.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.84 | +78.4% (+68.9 to +87.9) | +81.1% (+74.6 to +87.6) | +72.7% (+69.9 to +75.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.5% (-8.8 to +3.7) | -2.7% (-7.5 to +2.1) | -0.7% (-4.2 to +2.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 20 to 21 (12 trials, 1 allowed, 6 refused); acting: 19 to 21 (10 trials, 2 allowed, 5 refused); acting: 18 to 20 (11 trials, 2 allowed, 6 refused); run B: acting: 19 to 21 (13 trials, 2 allowed, 5 refused); acting: 19 to 20 (10 trials, 1 allowed, 6 refused); acting: 18 to 20 (12 trials, 2 allowed, 6 refused); run C: acting: 20 to 21 (12 trials, 1 allowed, 5 refused); acting: 19 to 21 (11 trials, 2 allowed, 3 refused); acting: 20 to 21 (10 trials, 1 allowed, 5 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,876, 2,882, 3,301 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 825.5 | 824.5 | -0.1% (-0.6 to +0.4) | +0.0% (-0.6 to +0.7) | +1.5% (-4.4 to +7.4) | STEADY, under the floor (the three runs' mean 0.48%) |
| throughput (transactions a second) | 825.5 | 824.5 | -0.1% (-0.6 to +0.3) | +0.1% (-0.4 to +0.6) | -0.0% (-0.5 to +0.4) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms, lag included) | 4.66 | 4.74 | +1.6% (-11.6 to +14.8) | +6.1% (-9.9 to +22.1) | -74.0% (-388.8 to +240.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 9.59 | 9.81 | +2.3% (-26.6 to +31.2) | +30.0% (-53.8 to +113.8) | -94.9% (-467.4 to +277.6) | **the runs disagree** |
| latency, median (ms) | 1.92 | 1.92 | +0.5% (-1.4 to +2.3) | +0.8% (+0.4 to +1.2) | +1.1% (+0.3 to +1.9) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, mean (ms) | 2.4 | 2.42 | +1.0% (-6.7 to +8.7) | +8.5% (-12.0 to +29.1) | -73.1% (-363.7 to +217.6) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.7 | 18.4 | -6.8% (-10.9 to -2.7) | -10.6% (-20.2 to -0.9) | -7.7% (-11.6 to -3.8) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +1.7% (-5.5 to +8.8) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.233 | 0.235 | +0.8% (-2.1 to +3.7) | +0.8% (+0.4 to +1.2) | +1.0% (+0.0 to +2.0) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 364.4 | 367.7 | +0.9% (-2.2 to +3.9) | +0.8% (+0.4 to +1.2) | +0.9% (+0.0 to +1.8) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.981 | 0.991 | +1.0% (-2.3 to +4.3) | +0.8% (-0.1 to +1.7) | -0.7% (-5.9 to +4.6) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.757 | 1.48 | +94.9% (+88.3 to +101.5) | +75.1% (+70.5 to +79.7) | +90.6% (+81.3 to +99.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.3% (-5.4 to -5.2) | -10.5% (-27.7 to +6.6) | -7.2% (-13.0 to -1.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 12 to 20 (11 trials, 8 allowed, 2 refused); acting: 16 to 21 (11 trials, 5 allowed, 5 refused); run C: acting: 19 to 20 (6 trials, 1 allowed, 5 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); acting: 15 to 20 (10 trials, 5 allowed, 3 refused).

**Across 3 workloads: 6 gauge-rows GAIN, 2 LOSS, 10 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 STEADY, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
