# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39869913163 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| B | 39871667274 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| C | 39873437772 | `a9694fbc7d2a` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,768, 16,404, 38,530 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,380 | 7,361 | -0.3% (-1.4 to +0.8) | -0.7% (-3.7 to +2.3) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.33%) |
| throughput (transactions a second) | 7,380 | 7,380 | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to -0.0) | +0.0% (-0.0 to +0.1) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms, lag included) | 1.38 | 1.62 | +17.8% (-19.9 to +55.5) | -7.2% (-54.3 to +39.9) | -18.6% (-48.9 to +11.6) | **the runs disagree** |
| latency, 99th percentile (ms) | 4.21 | 17.5 | +316.7% (-950.0 to +1583.4) | +965.7% (-3170.9 to +5102.3) | -56.3% (-223.4 to +110.8) | **the runs disagree** |
| latency, median (ms) | 0.368 | 0.371 | +0.8% (-2.9 to +4.6) | -1.1% (-8.3 to +6.2) | -2.7% (-4.6 to -0.9) | **the runs disagree** |
| latency, mean (ms) | 0.567 | 0.843 | +48.6% (-124.0 to +221.2) | +150.5% (-472.9 to +774.0) | -14.8% (-24.8 to -4.8) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.1 | 16.8 | -12.1% (-23.4 to -0.8) | -20.0% (-34.4 to -5.6) | -13.0% (-29.2 to +3.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.323 | 0.326 | +1.0% (-3.8 to +5.8) | -1.7% (-12.4 to +8.9) | -2.6% (-4.7 to -0.5) | **the runs disagree** |
| host CPU-seconds | 474.6 | 480.1 | +1.2% (-4.1 to +6.4) | -2.0% (-14.0 to +10.0) | -2.5% (-4.8 to -0.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.145 | +1.4% (-5.0 to +7.8) | -1.3% (-12.9 to +10.4) | -2.5% (-4.7 to -0.3) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.4 | +30.4% (+17.8 to +43.1) | +28.6% (+15.9 to +41.2) | +13.3% (+9.6 to +16.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.1 | -14.3% (-44.7 to +16.2) | -17.7% (-29.7 to -5.8) | -11.5% (-27.6 to +4.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 9 to 20 (13 trials, 11 allowed, 1 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused); run B: acting: 13 to 20 (11 trials, 7 allowed, 3 refused); acting: 15 to 20 (10 trials, 5 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused); run C: acting: 18 to 20 (7 trials, 2 allowed, 4 refused); acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 5,403, 3,838, 3,771 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,773 | 1,760 | -0.8% (-38.8 to +37.2) | +0.0% (-4.7 to +4.8) | +0.1% (-3.1 to +3.4) | STEADY, under the floor (the three runs' mean 0.21%) |
| throughput (transactions a second) | 2,341 | 2,324 | -0.8% (-5.3 to +3.8) | +0.0% (-0.5 to +0.5) | -0.3% (-0.6 to +0.0) | STEADY, under the floor (the three runs' mean 0.34%) |
| latency, 95th percentile (ms, lag included) | 1,604 | 1,724 | +7.5% (-190.7 to +205.6) | +4.0% (-88.3 to +96.3) | -7.3% (-43.8 to +29.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 2,711 | 5,055 | +86.5% (-6.5 to +179.4) | +3.2% (-123.2 to +129.5) | -21.2% (-129.7 to +87.3) | **the runs disagree** |
| latency, median (ms) | 1.19 | 1.15 | -3.3% (-40.0 to +33.3) | +0.5% (-1.6 to +2.6) | -0.0% (-0.5 to +0.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 233.2 | 273.3 | +17.2% (-189.9 to +224.3) | +4.7% (-137.7 to +147.2) | -12.8% (-94.8 to +69.2) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.2% (-4.2 to +3.9) | -4.4% (-9.8 to +1.1) | -4.8% (-12.7 to +3.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | +6.7% (-0.5 to +13.8) | +8.3% (+1.2 to +15.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.376 | 0.373 | -0.8% (-6.0 to +4.4) | +0.5% (-1.6 to +2.6) | -0.4% (-1.6 to +0.9) | **the runs disagree** |
| host CPU-seconds | 649.5 | 644.5 | -0.8% (-5.0 to +3.5) | +0.6% (-2.0 to +3.2) | -0.4% (-1.9 to +1.1) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.825 | 0.821 | -0.5% (-40.0 to +38.9) | +0.6% (-6.5 to +7.6) | -0.5% (-5.2 to +4.2) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.925 | 1.6 | +72.6% (+61.5 to +83.7) | +77.7% (+72.6 to +82.8) | +79.0% (+71.7 to +86.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.1% (-3.9 to +3.6) | -3.6% (-9.3 to +2.1) | -3.7% (-12.4 to +5.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 21 (15 trials, 2 allowed, 4 refused); acting: 19 to 21 (19 trials, 2 allowed, 3 refused); acting: 19 to 22 (20 trials, 3 allowed, 3 refused); run B: acting: 19 to 21 (14 trials, 2 allowed, 5 refused); acting: 19 to 20 (12 trials, 1 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 4 refused); run C: acting: 17 to 21 (15 trials, 4 allowed, 3 refused); acting: 19 to 21 (12 trials, 2 allowed, 6 refused); left native (12 trials, 0 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,649, 1,900, 1,888 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 722.2 | 695.6 | -3.7% (-19.0 to +11.6) | -0.0% (-0.5 to +0.4) | +0.0% (-1.1 to +1.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 724.2 | 724.9 | +0.1% (-0.1 to +0.3) | +0.0% (-0.2 to +0.3) | -0.0% (-0.9 to +0.9) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 7.65 | 79.5 | +939.0% (-2928.5 to +4806.5) | +2.1% (-11.8 to +16.0) | +2.0% (-7.7 to +11.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 26.5 | 127.6 | +380.9% (-1117.5 to +1879.2) | +21.9% (-4.4 to +48.2) | +5.5% (-54.3 to +65.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 2.15 | 2.22 | +3.3% (-14.9 to +21.5) | -0.1% (-2.8 to +2.6) | -0.2% (-1.0 to +0.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.34 | 10.7 | +220.1% (-669.7 to +1109.8) | +4.6% (-2.1 to +11.3) | -1.0% (-23.3 to +21.2) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.8 | 17.7 | -10.7% (-14.6 to -6.8) | -13.0% (-16.7 to -9.3) | -12.8% (-16.0 to -9.6) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +1.7% (-5.5 to +8.8) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.231 | 0.241 | +4.4% (-16.5 to +25.4) | +0.3% (-4.1 to +4.6) | -0.2% (-0.8 to +0.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 365.3 | 382.2 | +4.6% (-17.0 to +26.2) | +0.2% (-4.4 to +4.8) | -0.2% (-0.9 to +0.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 1.12 | 1.23 | +9.1% (-22.1 to +40.3) | +0.3% (-3.9 to +4.4) | -0.2% (-2.0 to +1.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.832 | 1.66 | +100.1% (+92.9 to +107.3) | +95.2% (+88.3 to +102.1) | +96.8% (+95.7 to +97.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.1 | -9.7% (-11.9 to -7.5) | -11.7% (-17.6 to -5.8) | -11.7% (-15.2 to -8.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 17 to 20 (9 trials, 3 allowed, 4 refused); run B: acting: 16 to 20 (10 trials, 4 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 4 refused); run C: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused).

**Across 3 workloads: 4 gauge-rows GAIN, 4 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 9 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
