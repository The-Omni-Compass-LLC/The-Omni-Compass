# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39842347137 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| B | 39851575564 | `36cb1cc37947` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| C | 39860251731 | `15915c961cd2` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 38,790, 15,965, 25,605 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17,067 | 17,063 | -0.0% (-0.2 to +0.1) | +0.0% (-0.1 to +0.2) | -0.1% (-0.1 to -0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (transactions a second) | 17,067 | 17,063 | -0.0% (-0.2 to +0.1) | +0.0% (-0.1 to +0.2) | -0.1% (-0.1 to -0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 0.446 | 0.399 | -10.5% (-36.8 to +15.7) | +6.8% (+1.3 to +12.4) | +4.5% (-16.9 to +25.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 2.94 | 1.76 | -40.1% (-152.4 to +72.3) | +22.2% (+0.8 to +43.5) | +5.9% (-32.4 to +44.3) | **the runs disagree** |
| latency, median (ms) | 0.159 | 0.16 | +0.6% (-2.1 to +3.3) | +1.2% (+0.8 to +1.6) | +0.0% (-5.6 to +5.6) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 0.283 | 0.239 | -15.3% (-68.0 to +37.4) | +4.6% (+0.3 to +8.8) | +5.7% (-13.3 to +24.7) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.8 | 17.1 | -13.4% (-27.8 to +1.0) | -7.7% (-8.5 to -6.9) | -12.2% (-24.3 to -0.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +1.7% (-5.5 to +8.8) | +3.3% (-3.8 to +10.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.379 | 0.381 | +0.4% (-2.0 to +2.8) | +2.2% (+0.9 to +3.4) | -0.1% (-3.8 to +3.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 644.9 | 647.7 | +0.4% (-1.8 to +2.7) | +2.5% (+0.9 to +4.0) | -0.2% (-3.7 to +3.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.084 | 0.0843 | +0.5% (-1.9 to +2.8) | +2.4% (+0.8 to +4.0) | -0.1% (-3.6 to +3.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.15 | 3.66 | +16.0% (+10.9 to +21.2) | +29.4% (+22.9 to +35.8) | +18.2% (+14.1 to +22.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.6 | -12.2% (-28.4 to +4.0) | -5.0% (-6.0 to -4.0) | -13.1% (-26.3 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 12 to 20 (11 trials, 8 allowed, 2 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); run C: acting: 16 to 21 (10 trials, 5 allowed, 3 refused); acting: 13 to 20 (11 trials, 7 allowed, 3 refused); acting: 13 to 20 (10 trials, 7 allowed, 2 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 7,219, 3,837, 5,852 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,832 | 2,807 | -0.9% (-17.4 to +15.7) | -0.4% (-4.9 to +4.2) | -0.1% (-2.8 to +2.6) | STEADY, under the floor (the three runs' mean 0.43%) |
| throughput (transactions a second) | 3,166 | 3,163 | -0.1% (-1.4 to +1.2) | +0.0% (-0.1 to +0.2) | +0.1% (-0.2 to +0.4) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 420.9 | 408.5 | -3.0% (-293.1 to +287.2) | +140.8% (-493.8 to +775.3) | -2.2% (-114.6 to +110.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 1,467 | 953.8 | -35.0% (-282.0 to +212.0) | -4.7% (-123.9 to +114.4) | +14.2% (-29.6 to +58.1) | **the runs disagree** |
| latency, median (ms) | 0.756 | 0.754 | -0.2% (-20.1 to +19.7) | +0.2% (-3.2 to +3.7) | -0.4% (-1.9 to +1.1) | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, mean (ms) | 69.7 | 56.8 | -18.5% (-290.8 to +253.7) | +14.8% (-126.3 to +155.8) | +11.2% (-54.1 to +76.4) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.7% (-5.8 to +2.4) | -2.8% (-3.7 to -1.9) | -0.8% (-2.1 to +0.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | +8.3% (+1.2 to +15.5) | +10.0% (+10.0 to +10.0) | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.347 | 0.348 | +0.1% (-10.0 to +10.3) | +0.5% (-3.1 to +4.1) | +0.0% (-1.0 to +1.0) | STEADY, under the floor (the three runs' mean 0.21%) |
| host CPU-seconds | 590.5 | 591.1 | +0.1% (-10.7 to +10.9) | +0.6% (-3.6 to +4.9) | -0.0% (-1.1 to +1.1) | STEADY, under the floor (the three runs' mean 0.24%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.465 | 0.469 | +0.8% (-25.9 to +27.5) | +1.0% (-7.1 to +9.2) | +0.1% (-1.9 to +2.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.862 | 1.4 | +62.1% (+52.5 to +71.8) | +79.7% (+71.1 to +88.3) | +53.2% (+45.7 to +60.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.4% (-5.8 to +2.9) | -2.4% (-3.0 to -1.8) | -0.0% (-1.3 to +1.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 20 to 21 (20 trials, 1 allowed, 3 refused); acting: 19 to 20 (17 trials, 1 allowed, 4 refused); acting: 18 to 21 (18 trials, 3 allowed, 3 refused); run B: acting: 19 to 21 (11 trials, 2 allowed, 6 refused); acting: 18 to 21 (11 trials, 3 allowed, 7 refused); acting: 19 to 21 (12 trials, 2 allowed, 3 refused); run C: acting: 20 to 22 (12 trials, 2 allowed, 4 refused); acting: 20 to 21 (19 trials, 1 allowed, 4 refused); acting: 20 to 22 (17 trials, 2 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,179, 2,139, 1,863 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,324 | 1,237 | -6.5% (-23.4 to +10.3) | -1.3% (-27.8 to +25.2) | -0.1% (-1.3 to +1.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,394 | 1,393 | -0.1% (-0.1 to -0.0) | -0.6% (-3.0 to +1.7) | -0.1% (-1.0 to +0.8) | STEADY, under the floor (the three runs' mean 0.27%) |
| latency, 95th percentile (ms, lag included) | 56.5 | 299.9 | +430.3% (-716.0 to +1576.6) | +75.3% (-349.2 to +499.8) | -0.2% (-22.6 to +22.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 2,750 | 922.2 | -66.5% (-215.4 to +82.4) | +31.8% (-175.7 to +239.4) | +5.3% (-59.1 to +69.6) | **the runs disagree** |
| latency, median (ms) | 0.844 | 0.854 | +1.2% (-7.1 to +9.4) | -1.9% (-26.0 to +22.3) | +0.2% (-1.9 to +2.2) | **the runs disagree** |
| latency, mean (ms) | 71.4 | 51.0 | -28.6% (-234.4 to +177.3) | +39.7% (-197.2 to +276.6) | +0.1% (-50.2 to +50.3) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.4 | -2.9% (-7.1 to +1.2) | -1.4% (-7.9 to +5.2) | -5.9% (-15.3 to +3.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | +5.0% (+5.0 to +5.0) | +1.7% (-5.5 to +8.8) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.212 | 0.215 | +1.2% (-5.1 to +7.6) | -0.6% (-7.2 to +6.0) | +0.4% (-3.8 to +4.5) | **the runs disagree** |
| host CPU-seconds | 366.3 | 371.0 | +1.3% (-5.2 to +7.8) | -0.7% (-7.7 to +6.3) | +0.4% (-3.9 to +4.6) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.615 | 0.67 | +8.9% (-16.6 to +34.4) | +0.7% (-32.0 to +33.4) | +0.5% (-2.6 to +3.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.572 | 1.05 | +83.2% (+71.5 to +95.0) | +93.9% (+83.8 to +103.9) | +97.1% (+90.1 to +104.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.3% (-5.7 to +1.1) | -1.4% (-7.6 to +4.8) | -5.5% (-7.3 to -3.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (15 trials, 1 allowed, 4 refused); acting: 19 to 20 (16 trials, 1 allowed, 3 refused); acting: 19 to 20 (22 trials, 1 allowed, 4 refused); run B: left native (30 trials, 0 allowed, 0 refused); left native (23 trials, 0 allowed, 3 refused); acting: 17 to 20 (21 trials, 3 allowed, 1 refused); run C: acting: 19 to 20 (8 trials, 1 allowed, 6 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (9 trials, 3 allowed, 4 refused).

**Across 3 workloads: 3 gauge-rows GAIN, 3 LOSS, 8 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
