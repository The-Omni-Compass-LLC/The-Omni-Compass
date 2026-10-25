# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40043218026 | `f22776e60a87` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| B | 40044599601 | `0d532c7a2dbd` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| C | 40045930230 | `e4a97f22dce1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,287, 16,340, 39,049 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,161 | 7,166 | +0.1% (-0.2 to +0.4) | -0.7% (-2.6 to +1.2) | -0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.22%) |
| throughput (transactions a second) | 7,161 | 7,166 | +0.1% (-0.2 to +0.4) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 1.26 | 1.29 | +2.3% (-2.9 to +7.5) | +27.3% (-25.1 to +79.7) | -27.0% (-112.0 to +57.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 3.79 | 4.01 | +5.8% (-12.6 to +24.2) | +501.8% (-1164.7 to +2168.4) | -41.1% (-128.4 to +46.2) | **the runs disagree** |
| latency, median (ms) | 0.368 | 0.368 | +0.0% (-0.7 to +0.7) | +1.3% (+0.2 to +2.3) | +0.2% (-3.7 to +4.1) | STEADY, under the floor (the three runs' mean 0.49%) |
| latency, mean (ms) | 0.547 | 0.582 | +6.3% (-4.8 to +17.4) | +105.1% (-147.4 to +357.6) | -23.0% (-72.8 to +26.9) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.2 | 15.0 | -21.9% (-34.5 to -9.3) | -22.2% (-38.1 to -6.2) | -9.1% (-18.7 to +0.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.316 | 0.317 | +0.2% (-0.5 to +0.9) | +1.9% (+0.7 to +3.2) | +0.2% (-4.2 to +4.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 466.0 | 467.1 | +0.2% (-0.8 to +1.2) | +2.3% (+0.7 to +3.8) | +0.1% (-4.4 to +4.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.145 | +0.2% (-1.0 to +1.3) | +3.0% (+0.5 to +5.4) | +0.2% (-4.5 to +4.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.56 | 3.34 | +30.6% (+22.1 to +39.0) | +32.4% (+27.5 to +37.3) | +16.5% (+14.0 to +18.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 15.7 | -21.3% (-28.4 to -14.2) | -20.0% (-38.2 to -1.7) | -8.9% (-20.0 to +2.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 12 to 20 (12 trials, 8 allowed, 3 refused); acting: 13 to 20 (11 trials, 7 allowed, 4 refused); acting: 12 to 20 (11 trials, 8 allowed, 3 refused); run B: acting: 13 to 20 (10 trials, 7 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 10 to 20 (13 trials, 10 allowed, 2 refused); run C: acting: 16 to 20 (9 trials, 4 allowed, 3 refused); acting: 17 to 20 (9 trials, 3 allowed, 3 refused); acting: 19 to 20 (6 trials, 1 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,849, 5,315, 4,536 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,645 | 1,639 | -0.4% (-4.1 to +3.3) | +4.1% (-21.7 to +29.9) | -19.1% (-92.9 to +54.8) | **the runs disagree** |
| throughput (transactions a second) | 1,695 | 1,690 | -0.3% (-0.8 to +0.2) | +1.9% (-6.0 to +9.9) | -2.0% (-5.9 to +1.9) | **the runs disagree** |
| latency, 95th percentile (ms, lag included) | 7.68 | 9.43 | +22.8% (-101.6 to +147.3) | -47.7% (-122.7 to +27.3) | +242.6% (-43.4 to +528.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 206.8 | 202.8 | -1.9% (-75.3 to +71.4) | -45.7% (-232.9 to +141.5) | +208.0% (-89.4 to +505.5) | **the runs disagree** |
| latency, median (ms) | 1.52 | 1.52 | +0.3% (-0.7 to +1.2) | +37.2% (-177.8 to +252.3) | +1776.0% (-2882.0 to +6434.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 7.16 | 7.3 | +1.9% (-87.8 to +91.6) | -42.1% (-118.6 to +34.5) | +191.7% (-119.7 to +503.2) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 18.6 | -6.9% (-9.5 to -4.4) | +4.5% (-4.5 to +13.5) | +1.5% (-2.4 to +5.5) | **the runs disagree** |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | +13.3% (-12.5 to +39.2) | +6.7% (-0.5 to +13.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.342 | 0.342 | +0.1% (-1.7 to +2.0) | +2.2% (-4.0 to +8.4) | -3.1% (-10.2 to +4.1) | **the runs disagree** |
| host CPU-seconds | 513.7 | 514.3 | +0.1% (-1.7 to +1.9) | +2.3% (-4.9 to +9.4) | -2.8% (-8.8 to +3.3) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.694 | 0.697 | +0.5% (-1.5 to +2.5) | -1.4% (-33.8 to +31.0) | +22.2% (-63.9 to +108.4) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.81 | +78.3% (+75.1 to +81.5) | +73.6% (+66.4 to +80.9) | +70.1% (+54.3 to +85.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.5% (-9.1 to -1.9) | +4.1% (-4.3 to +12.5) | +1.3% (-2.3 to +4.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 17 to 20 (14 trials, 3 allowed, 5 refused); acting: 18 to 21 (13 trials, 3 allowed, 4 refused); acting: 19 to 20 (14 trials, 1 allowed, 3 refused); run B: acting: 19 to 21 (18 trials, 2 allowed, 3 refused); acting: 20 to 24 (21 trials, 4 allowed, 1 refused); left native (19 trials, 0 allowed, 2 refused); run C: left native (25 trials, 0 allowed, 0 refused); left native (24 trials, 0 allowed, 0 refused); acting: 20 to 21 (20 trials, 1 allowed, 2 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,293, 1,912, 1,531 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,007 | 1,007 | -0.0% (-1.8 to +1.7) | +0.0% (-0.1 to +0.2) | -3.4% (-13.1 to +6.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,010 | 1,008 | -0.2% (-0.5 to +0.0) | -0.0% (-0.3 to +0.2) | -0.0% (-0.7 to +0.7) | STEADY, under the floor (the three runs' mean 0.09%) |
| latency, 95th percentile (ms, lag included) | 2.96 | 2.84 | -4.1% (-27.8 to +19.5) | -3.3% (-19.4 to +12.9) | +8.0% (-32.4 to +48.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 18.7 | 5.52 | -70.5% (-394.9 to +253.9) | -4.3% (-79.8 to +71.1) | -30.8% (-87.7 to +26.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.35 | 1.34 | -1.0% (-4.7 to +2.6) | -0.3% (-0.9 to +0.2) | +2.3% (-8.0 to +12.6) | **the runs disagree** |
| latency, mean (ms) | 1.99 | 1.74 | -12.6% (-103.9 to +78.8) | -3.1% (-16.4 to +10.2) | -4.1% (-21.7 to +13.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.7 | 17.4 | -12.0% (-25.1 to +1.0) | -15.5% (-18.5 to -12.5) | -0.4% (-1.0 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +5.0% (+5.0 to +5.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.239 | 0.237 | -0.9% (-5.2 to +3.3) | -0.1% (-1.5 to +1.4) | +0.6% (-1.2 to +2.4) | **the runs disagree** |
| host CPU-seconds | 419.2 | 415.4 | -0.9% (-5.0 to +3.2) | -0.1% (-1.7 to +1.5) | +0.6% (-1.2 to +2.4) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.925 | 0.917 | -0.9% (-3.3 to +1.6) | -0.1% (-1.8 to +1.6) | +4.5% (-8.4 to +17.4) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.629 | 1.17 | +85.8% (+83.2 to +88.4) | +97.4% (+90.9 to +104.0) | +97.0% (+95.1 to +98.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -10.9% (-26.3 to +4.6) | -13.3% (-15.5 to -11.1) | -0.3% (-0.9 to +0.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 16 to 20 (10 trials, 4 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 15 to 20 (9 trials, 5 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); run C: left native (25 trials, 0 allowed, 1 refused); left native (21 trials, 0 allowed, 1 refused); left native (28 trials, 0 allowed, 1 refused).

**Across 3 workloads: 4 gauge-rows GAIN, 2 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 8 STEADY, 17 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
