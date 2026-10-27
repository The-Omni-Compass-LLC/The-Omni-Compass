# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40258014810 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| B | 40281459100 | `fa6da97bbaa6` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| C | 40400963499 | `5e222aa21371` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,493, 16,085, 16,753 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,256 | 7,259 | +0.0% (-0.3 to +0.4) | +0.1% (-0.2 to +0.4) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| throughput (transactions a second) | 7,256 | 7,259 | +0.0% (-0.3 to +0.4) | +0.1% (-0.2 to +0.4) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 1.41 | 1.44 | +2.1% (-23.5 to +27.7) | +5.1% (-9.5 to +19.7) | -13.2% (-72.7 to +46.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 4.05 | 3.94 | -2.8% (-49.4 to +43.7) | +5.4% (-53.7 to +64.5) | -11.9% (-59.1 to +35.2) | **the runs disagree** |
| latency, median (ms) | 0.371 | 0.372 | +0.3% (-1.5 to +2.0) | +0.8% (-0.4 to +2.0) | +0.1% (-0.3 to +0.5) | EVEN, under the floor (the three runs' mean 0.39%) |
| latency, mean (ms) | 0.565 | 0.57 | +0.8% (-14.9 to +16.5) | +3.0% (-10.7 to +16.7) | -4.8% (-21.7 to +12.2) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 18.4 | -7.2% (-12.5 to -2.0) | -7.2% (-9.4 to -5.0) | -6.0% (-11.0 to -1.0) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.325 | 0.326 | +0.5% (-2.3 to +3.4) | +1.3% (-0.8 to +3.4) | +0.4% (-0.7 to +1.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 486.9 | 489.6 | +0.6% (-2.7 to +3.8) | +1.4% (-0.9 to +3.8) | +0.4% (-0.9 to +1.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.15 | +0.5% (-3.1 to +4.1) | +1.3% (-1.2 to +3.9) | +0.5% (-0.7 to +1.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.37 | 9.13 | +9.2% (+1.1 to +17.2) | +10.0% (+6.5 to +13.5) | +9.4% (+5.7 to +13.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.7% (-9.9 to -1.4) | -5.2% (-6.1 to -4.2) | -5.7% (-6.0 to -5.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 3 refused); run B: acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 16 to 20 (6 trials, 4 allowed, 2 refused); acting: 16 to 20 (7 trials, 4 allowed, 2 refused); acting: 16 to 20 (7 trials, 4 allowed, 2 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,839, 3,911, 3,754 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,658 | 1,657 | -0.0% (-0.8 to +0.7) | -0.2% (-1.5 to +1.1) | -0.2% (-0.9 to +0.5) | EVEN, under the floor (the three runs' mean 0.14%) |
| throughput (transactions a second) | 1,690 | 1,689 | -0.0% (-0.5 to +0.4) | +0.0% (-0.2 to +0.2) | -0.1% (-0.5 to +0.3) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 6.05 | 5.93 | -2.0% (-11.3 to +7.3) | -5.0% (-25.0 to +15.1) | +3.9% (-5.5 to +13.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 146.0 | 148.4 | +1.6% (-61.6 to +64.8) | +12.2% (-91.8 to +116.3) | -1.5% (-18.7 to +15.7) | **the runs disagree** |
| latency, median (ms) | 1.48 | 1.48 | +0.0% (-0.8 to +0.8) | -0.1% (-3.3 to +3.1) | +0.1% (-2.1 to +2.3) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 5.02 | 4.91 | -2.2% (-41.4 to +37.0) | +3.7% (-39.3 to +46.7) | -0.2% (-23.4 to +23.0) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.2% (-6.4 to +0.0) | -1.3% (-4.7 to +2.0) | -1.2% (-2.0 to -0.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | +8.3% (+1.2 to +15.5) | +8.3% (+1.2 to +15.5) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.333 | 0.334 | +0.2% (+0.1 to +0.3) | -0.0% (-3.3 to +3.2) | -0.2% (-0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.01%) |
| host CPU-seconds | 501.1 | 502.2 | +0.2% (-0.1 to +0.5) | -0.1% (-3.7 to +3.5) | -0.2% (-0.7 to +0.3) | EVEN, under the floor (the three runs' mean 0.03%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.672 | 0.673 | +0.2% (-0.7 to +1.2) | +0.1% (-4.3 to +4.6) | -0.0% (-1.2 to +1.1) | EVEN, under the floor (the three runs' mean 0.11%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.4 | 3.15 | +30.9% (+24.9 to +36.8) | +31.9% (+28.2 to +35.6) | +34.3% (+32.9 to +35.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.6 | -2.0% (-3.5 to -0.5) | -0.8% (-4.4 to +2.8) | -0.3% (-0.6 to +0.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (12 trials, 0 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 7 refused); acting: 18 to 21 (12 trials, 3 allowed, 6 refused); run B: acting: 19 to 20 (11 trials, 1 allowed, 7 refused); acting: 19 to 21 (12 trials, 2 allowed, 4 refused); acting: 20 to 22 (13 trials, 2 allowed, 4 refused); run C: acting: 19 to 21 (9 trials, 2 allowed, 3 refused); acting: 20 to 21 (7 trials, 1 allowed, 4 refused); acting: 20 to 21 (6 trials, 1 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,219, 1,916, 1,821 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,317 | 1,325 | +0.6% (-22.9 to +24.0) | +0.1% (-0.3 to +0.6) | -0.0% (-0.5 to +0.4) | EVEN, under the floor (the three runs' mean 0.23%) |
| throughput (transactions a second) | 1,415 | 1,404 | -0.8% (-3.8 to +2.3) | +0.1% (-0.3 to +0.6) | -0.0% (-0.5 to +0.4) | EVEN, under the floor (the three runs' mean 0.22%) |
| latency, 95th percentile (ms, lag included) | 242.4 | 86.6 | -64.3% (-455.5 to +327.0) | +0.0% (-7.0 to +7.1) | -2.3% (-18.2 to +13.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 1,180 | 407.7 | -65.5% (-404.4 to +273.4) | -0.0% (-13.9 to +13.8) | +0.8% (-26.7 to +28.4) | **the runs disagree** |
| latency, median (ms) | 0.847 | 0.845 | -0.2% (-10.8 to +10.3) | +0.0% (-1.1 to +1.1) | -0.7% (-3.8 to +2.4) | EVEN, under the floor (the three runs' mean 0.30%) |
| latency, mean (ms) | 50.3 | 28.5 | -43.3% (-452.6 to +366.0) | -0.2% (-2.5 to +2.1) | -0.7% (-8.4 to +7.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.6 | -1.7% (-3.9 to +0.6) | -7.5% (-9.7 to -5.3) | -5.1% (-15.0 to +4.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.2% (-10.0 to +7.7) | +0.4% (-2.2 to +3.1) | -0.6% (-4.7 to +3.6) | EVEN, under the floor (the three runs' mean 0.45%) |
| host CPU-seconds | 373.2 | 368.9 | -1.1% (-10.1 to +7.8) | +0.4% (-2.4 to +3.3) | -0.6% (-4.9 to +3.7) | EVEN, under the floor (the three runs' mean 0.44%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.63 | 0.62 | -1.6% (-32.0 to +28.8) | +0.3% (-2.2 to +2.7) | -0.6% (-5.2 to +4.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.18 | 1.63 | +38.1% (+26.1 to +50.0) | +45.2% (+44.7 to +45.7) | +49.8% (+46.0 to +53.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.3% (-2.2 to -0.4) | -5.5% (-6.8 to -4.2) | -5.4% (-5.7 to -5.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 18 to 20 (19 trials, 2 allowed, 2 refused); acting: 19 to 21 (18 trials, 2 allowed, 2 refused); acting: 17 to 21 (14 trials, 4 allowed, 4 refused); run B: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 18 to 20 (6 trials, 2 allowed, 3 refused); acting: 17 to 20 (6 trials, 3 allowed, 2 refused); acting: 17 to 20 (6 trials, 3 allowed, 2 refused).

**Across 3 workloads: 6 gauge-rows GAIN, 0 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 18 EVEN, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
