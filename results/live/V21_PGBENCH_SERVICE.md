# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40289615442 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| B | 40293188618 | `2d426169d766` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| C | 40295032874 | `c8b8e2af081f` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 37,388, 36,773, 16,496 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 16,450 | 16,452 | +0.0% (-0.0 to +0.0) | +2.0% (-6.8 to +10.8) | -0.0% (-0.1 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 16,450 | 16,452 | +0.0% (-0.0 to +0.0) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 0.791 | 0.505 | -36.2% (-232.2 to +159.7) | -99.2% (-520.9 to +322.5) | -11.2% (-46.3 to +23.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.2 | 3.77 | -27.5% (-224.2 to +169.3) | -99.3% (-516.9 to +318.3) | -18.7% (-62.5 to +25.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.163 | 0.162 | -0.6% (-3.7 to +2.4) | -1.9% (-12.1 to +8.3) | +0.1% (-0.7 to +0.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.363 | 0.321 | -11.7% (-116.2 to +92.8) | -96.8% (-505.0 to +311.4) | -5.3% (-21.1 to +10.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.3% (-15.4 to +6.9) | -8.9% (-11.3 to -6.6) | -21.0% (-37.5 to -4.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.374 | 0.373 | -0.5% (-3.9 to +3.0) | -1.9% (-12.7 to +8.8) | +0.1% (-1.7 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 648.5 | 645.6 | -0.5% (-4.2 to +3.3) | -2.1% (-13.3 to +9.2) | +0.1% (-2.0 to +2.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.0876 | 0.0872 | -0.5% (-4.3 to +3.3) | -4.0% (-17.7 to +9.7) | +0.1% (-2.0 to +2.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 10.3 | 10.9 | +5.7% (+3.2 to +8.1) | +4.6% (-3.6 to +12.9) | +9.6% (+2.2 to +17.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.5% (-13.4 to +6.4) | -7.5% (-10.5 to -4.5) | -20.5% (-40.3 to -0.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); left native (6 trials, 0 allowed, 5 refused); left native (6 trials, 0 allowed, 5 refused); run B: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); run C: acting: 12 to 20 (11 trials, 8 allowed, 3 refused); acting: 11 to 20 (12 trials, 9 allowed, 3 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 5,934, 3,884, 7,642 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,480 | 2,507 | +1.1% (-1.4 to +3.6) | -0.3% (-1.2 to +0.5) | +0.0% (-3.5 to +3.5) | EVEN, under the floor (the three runs' mean 0.25%) |
| throughput (transactions a second) | 2,610 | 2,610 | -0.0% (-0.7 to +0.7) | -0.3% (-0.6 to +0.0) | +0.1% (-0.1 to +0.3) | EVEN, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms, lag included) | 65.3 | 15.2 | -76.7% (-325.3 to +171.8) | -3.9% (-29.0 to +21.2) | +64.8% (-161.0 to +290.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 589.1 | 519.3 | -11.9% (-52.3 to +28.6) | +6.1% (-66.0 to +78.3) | +10.8% (-32.1 to +53.7) | **the runs disagree** |
| latency, median (ms) | 1.18 | 1.17 | -0.5% (-2.9 to +2.0) | -0.5% (-2.9 to +1.9) | -1.4% (-5.2 to +2.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 20.5 | 16.1 | -21.5% (-87.2 to +44.2) | +0.3% (-35.7 to +36.2) | +17.2% (-61.1 to +95.5) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.2% (-4.6 to -1.8) | -3.9% (-5.7 to -2.0) | -0.4% (-3.7 to +2.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | +6.7% (-0.5 to +13.8) | +15.0% (+15.0 to +15.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.406 | 0.408 | +0.5% (+0.1 to +0.8) | -0.4% (-3.0 to +2.1) | -1.2% (-4.7 to +2.3) | EVEN, under the floor (the three runs' mean 0.40%) |
| host CPU-seconds | 704.9 | 708.1 | +0.5% (-0.0 to +0.9) | -0.4% (-3.3 to +2.5) | -1.3% (-5.0 to +2.5) | EVEN, under the floor (the three runs' mean 0.41%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.632 | 0.628 | -0.6% (-3.3 to +2.0) | -0.1% (-3.4 to +3.2) | -1.3% (-8.5 to +5.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.78 | 3.35 | +20.5% (+19.0 to +22.1) | +32.6% (+32.0 to +33.3) | +21.2% (+15.1 to +27.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.4% (-3.8 to -1.1) | -3.0% (-5.5 to -0.5) | -0.2% (-2.8 to +2.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (13 trials, 1 allowed, 5 refused); acting: 19 to 21 (12 trials, 2 allowed, 6 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused); run B: acting: 19 to 21 (13 trials, 2 allowed, 3 refused); acting: 19 to 20 (12 trials, 1 allowed, 4 refused); acting: 19 to 20 (13 trials, 1 allowed, 5 refused); run C: acting: 18 to 22 (20 trials, 4 allowed, 4 refused); acting: 19 to 22 (19 trials, 3 allowed, 4 refused); acting: 19 to 22 (15 trials, 3 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,956, 1,967, 2,509 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 860.3 | 862.0 | +0.2% (-0.1 to +0.5) | -0.0% (-1.0 to +0.9) | +0.6% (-1.2 to +2.5) | EVEN, under the floor (the three runs' mean 0.27%) |
| throughput (transactions a second) | 860.5 | 862.1 | +0.2% (-0.2 to +0.5) | -0.0% (-1.0 to +0.9) | +0.2% (-0.4 to +0.7) | EVEN, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms, lag included) | 5.26 | 4.89 | -7.1% (-18.5 to +4.4) | -4.1% (-20.4 to +12.2) | -12.7% (-73.7 to +48.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 13.1 | 10.8 | -17.2% (-44.1 to +9.6) | -15.4% (-41.6 to +10.9) | -78.9% (-417.6 to +259.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.88 | 1.87 | -0.2% (-1.4 to +0.9) | -0.2% (-3.1 to +2.8) | +0.3% (-2.0 to +2.6) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 2.51 | 2.42 | -3.7% (-9.6 to +2.3) | -3.2% (-11.8 to +5.3) | -23.2% (-118.7 to +72.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 16.4 | -15.8% (-24.5 to -7.1) | -13.6% (-22.9 to -4.3) | -15.3% (-18.9 to -11.8) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +1.7% (-5.5 to +8.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.239 | 0.24 | +0.2% (-2.4 to +2.8) | -0.2% (-4.2 to +3.8) | +0.6% (-2.2 to +3.3) | EVEN, under the floor (the three runs' mean 0.19%) |
| host CPU-seconds | 373.0 | 373.6 | +0.2% (-2.4 to +2.8) | -0.3% (-4.2 to +3.7) | +0.5% (-2.3 to +3.4) | EVEN, under the floor (the three runs' mean 0.16%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.963 | 0.963 | -0.0% (-2.5 to +2.5) | -0.2% (-3.5 to +3.0) | -0.1% (-4.6 to +4.5) | EVEN, under the floor (the three runs' mean 0.11%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.5 | 2.21 | +47.5% (+44.1 to +51.0) | +47.0% (+45.6 to +48.4) | +40.4% (+37.2 to +43.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.2 | -13.9% (-21.7 to -6.1) | -13.0% (-14.9 to -11.2) | -12.5% (-15.2 to -9.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 14 to 20 (10 trials, 6 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run C: acting: 15 to 21 (11 trials, 6 allowed, 3 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused).

**Across 3 workloads: 16 gauge-rows GAIN, 0 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 EVEN, 3 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
