# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149254727 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| B | 39157791268 | `5031411ae285` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| C | 39166378754 | `8472aaad2bf4` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,564, 16,586, 16,503 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,284 | 7,289 | +0.1% (-0.2 to +0.4) | -0.2% (-0.6 to +0.2) | -0.0% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 7,284 | 7,289 | +0.1% (-0.2 to +0.4) | -0.1% (-0.5 to +0.3) | -0.0% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms, lag included) | 1.51 | 1.46 | -3.3% (-36.7 to +30.2) | +73.3% (-208.6 to +355.2) | -3.4% (-22.5 to +15.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 4.63 | 4.21 | -9.0% (-59.0 to +41.0) | +79.2% (-217.7 to +376.1) | -10.7% (-62.6 to +41.2) | **the runs disagree** |
| latency, median (ms) | 0.373 | 0.373 | +0.0% (-1.2 to +1.2) | +1.3% (-4.2 to +6.7) | +0.0% (+0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.42%) |
| latency, mean (ms) | 0.597 | 0.577 | -3.3% (-24.2 to +17.5) | +29.6% (-75.9 to +135.0) | -2.6% (-17.3 to +12.1) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 18.4 | -5.9% (-13.6 to +1.7) | -5.3% (-7.6 to -2.9) | -7.1% (-10.3 to -3.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.327 | 0.328 | +0.2% (-1.4 to +1.8) | +1.2% (-6.3 to +8.6) | +0.1% (-0.5 to +0.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 482.2 | 483.4 | +0.3% (-1.4 to +2.0) | +1.5% (-6.7 to +9.7) | +0.1% (-0.9 to +1.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.147 | +0.2% (-1.3 to +1.7) | +1.7% (-6.8 to +10.1) | +0.1% (-0.9 to +1.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.36 | +28.7% (+22.5 to +34.9) | +30.8% (+22.1 to +39.4) | +26.7% (+19.5 to +33.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.3% (-5.6 to -5.0) | -4.8% (-5.5 to -4.1) | -5.4% (-6.1 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 18 to 20 (8 trials, 2 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); run C: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,791, 3,729, 3,823 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,625 | 1,624 | -0.1% (-3.6 to +3.4) | +0.5% (-2.4 to +3.4) | +0.4% (-1.6 to +2.4) | STEADY, under the floor (the three runs' mean 0.26%) |
| throughput (transactions a second) | 1,667 | 1,668 | +0.0% (-0.6 to +0.6) | +0.0% (-0.2 to +0.3) | -0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms, lag included) | 7.29 | 10.5 | +43.8% (-185.5 to +273.2) | -6.9% (-61.6 to +47.8) | -5.6% (-25.3 to +14.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 180.6 | 173.4 | -4.0% (-112.8 to +104.8) | -18.0% (-112.9 to +76.9) | -12.6% (-73.3 to +48.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.53 | 1.53 | +0.0% (-1.7 to +1.7) | +0.0% (-0.8 to +0.9) | -0.3% (-1.2 to +0.6) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, mean (ms) | 6.36 | 6.63 | +4.2% (-102.5 to +110.8) | -17.0% (-113.3 to +79.3) | -9.8% (-65.5 to +45.8) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.7% (-6.2 to -1.1) | -2.0% (-4.5 to +0.6) | -2.4% (-5.9 to +1.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | +10.0% (+10.0 to +10.0) | +10.0% (+10.0 to +10.0) | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.341 | 0.342 | +0.1% (-2.0 to +2.1) | +0.2% (-0.3 to +0.7) | -0.2% (-0.6 to +0.2) | STEADY, under the floor (the three runs' mean 0.01%) |
| host CPU-seconds | 513.6 | 514.2 | +0.1% (-2.3 to +2.5) | +0.2% (-0.4 to +0.8) | -0.3% (-0.6 to +0.1) | STEADY, under the floor (the three runs' mean 0.00%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.702 | 0.704 | +0.2% (-5.0 to +5.4) | -0.3% (-3.6 to +2.9) | -0.6% (-2.9 to +1.7) | STEADY, under the floor (the three runs' mean 0.26%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.81 | +77.4% (+75.3 to +79.6) | +75.1% (+71.6 to +78.5) | +76.5% (+68.7 to +84.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.5% (-6.1 to +1.1) | -1.0% (-3.4 to +1.5) | -1.7% (-5.4 to +2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 18 to 22 (12 trials, 4 allowed, 5 refused); acting: 20 to 21 (10 trials, 1 allowed, 4 refused); acting: 19 to 20 (10 trials, 1 allowed, 7 refused); run B: acting: 19 to 21 (11 trials, 2 allowed, 5 refused); acting: 20 to 21 (11 trials, 1 allowed, 4 refused); acting: 19 to 21 (12 trials, 2 allowed, 3 refused); run C: acting: 20 to 22 (11 trials, 2 allowed, 4 refused); acting: 19 to 21 (14 trials, 2 allowed, 5 refused); acting: 19 to 21 (12 trials, 2 allowed, 3 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,951, 1,910, 2,333 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,732 | 1,736 | +0.2% (-1.1 to +1.6) | -0.2% (-0.3 to -0.1) | -0.1% (-1.2 to +1.0) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (transactions a second) | 1,739 | 1,740 | +0.0% (-0.1 to +0.2) | -0.2% (-0.3 to -0.1) | -0.0% (-0.8 to +0.7) | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms, lag included) | 2.62 | 2.25 | -14.3% (-108.1 to +79.6) | +0.7% (-15.6 to +16.9) | +1.1% (-11.9 to +14.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 24.9 | 19.7 | -20.5% (-247.8 to +206.8) | +4.8% (-45.6 to +55.1) | -9.1% (-98.7 to +80.5) | **the runs disagree** |
| latency, median (ms) | 0.792 | 0.791 | -0.1% (-2.1 to +1.9) | -0.1% (-1.6 to +1.3) | +0.1% (-2.1 to +2.4) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 1.61 | 1.45 | -9.6% (-109.1 to +89.9) | +0.6% (-9.0 to +10.1) | +7.4% (-13.6 to +28.5) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.0 | -4.9% (-5.4 to -4.4) | -7.7% (-9.1 to -6.3) | -12.2% (-30.5 to +6.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (-7.4 to +17.4) | +0.0% (+0.0 to +0.0) | +1.7% (-5.5 to +8.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.244 | 0.244 | +0.0% (-2.6 to +2.7) | -0.5% (-3.3 to +2.2) | -0.2% (-2.3 to +2.0) | STEADY, under the floor (the three runs' mean 0.23%) |
| host CPU-seconds | 419.3 | 419.2 | -0.0% (-2.8 to +2.7) | -0.5% (-3.6 to +2.5) | -0.2% (-2.2 to +1.9) | STEADY, under the floor (the three runs' mean 0.25%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.538 | 0.537 | -0.2% (-4.3 to +3.8) | -0.4% (-3.5 to +2.8) | -0.1% (-3.1 to +2.8) | STEADY, under the floor (the three runs' mean 0.23%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.561 | 0.958 | +70.7% (+58.1 to +83.2) | +94.4% (+89.8 to +99.0) | +85.2% (+78.4 to +91.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.3% (-5.2 to -3.4) | -5.7% (-7.2 to -4.1) | -10.2% (-30.4 to +10.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 21 (8 trials, 2 allowed, 4 refused); acting: 17 to 20 (10 trials, 3 allowed, 3 refused); acting: 17 to 21 (10 trials, 4 allowed, 4 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); run C: acting: 17 to 20 (10 trials, 3 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 12 to 20 (12 trials, 8 allowed, 2 refused).

**Across 3 workloads: 4 gauge-rows GAIN, 0 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 19 STEADY, 8 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
