# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39379923601 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| B | 39410594381 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39459241206 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 15,932, 16,034, 39,368 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,008 | 7,009 | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | -0.2% (-1.1 to +0.7) | STEADY, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 7,008 | 7,009 | +0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.2) | -0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 1.1 | 1.09 | -0.9% (-31.2 to +29.5) | +0.2% (-6.8 to +7.1) | +5.6% (-4.9 to +16.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 2.97 | 2.59 | -12.7% (-78.6 to +53.2) | +1.7% (-49.7 to +53.2) | +175.8% (-341.1 to +692.7) | **the runs disagree** |
| latency, median (ms) | 0.363 | 0.363 | +0.1% (-3.7 to +3.9) | -0.1% (-1.7 to +1.5) | +0.7% (-1.1 to +2.5) | STEADY, under the floor (the three runs' mean 0.24%) |
| latency, mean (ms) | 0.504 | 0.496 | -1.6% (-19.2 to +16.1) | +9.5% (-45.4 to +64.5) | +143.2% (-359.8 to +646.1) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.3% (-10.5 to -4.2) | -7.0% (-12.5 to -1.4) | -9.2% (-21.3 to +2.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.306 | 0.306 | +0.2% (-6.5 to +7.0) | +0.1% (-0.6 to +0.8) | +0.6% (-3.4 to +4.5) | STEADY, under the floor (the three runs' mean 0.30%) |
| host CPU-seconds | 449.9 | 451.0 | +0.2% (-7.7 to +8.2) | +0.1% (-0.6 to +0.9) | +0.6% (-3.3 to +4.5) | STEADY, under the floor (the three runs' mean 0.33%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | +0.2% (-7.6 to +8.0) | +0.1% (-0.7 to +1.0) | +0.8% (-2.2 to +3.9) | STEADY, under the floor (the three runs' mean 0.40%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.5 | 3.22 | +29.0% (+20.3 to +37.7) | +28.4% (+23.7 to +33.0) | +16.0% (+11.0 to +21.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.8 | -5.9% (-8.6 to -3.2) | -5.9% (-7.9 to -3.8) | -8.7% (-19.9 to +2.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); run B: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); run C: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 18 to 20 (7 trials, 2 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,855, 3,143, 4,024 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,649 | 1,643 | -0.3% (-3.9 to +3.2) | +5.2% (-4.4 to +14.8) | -0.6% (-5.0 to +3.7) | **the runs disagree** |
| throughput (transactions a second) | 1,697 | 1,696 | -0.1% (-0.8 to +0.7) | +0.3% (-1.6 to +2.2) | -0.1% (-0.4 to +0.3) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms, lag included) | 7.62 | 10.2 | +33.7% (-195.4 to +262.8) | -35.9% (-37.8 to -34.0) | +248.7% (-834.8 to +1332.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 203.6 | 229.2 | +12.6% (-55.0 to +80.1) | -9.9% (-36.4 to +16.7) | +14.9% (-65.6 to +95.5) | **the runs disagree** |
| latency, median (ms) | 1.54 | 1.53 | -0.2% (-5.3 to +5.0) | -9.2% (-29.7 to +11.3) | +0.9% (-1.4 to +3.2) | **the runs disagree** |
| latency, mean (ms) | 7.08 | 8.05 | +13.6% (-97.8 to +125.1) | -27.8% (-35.4 to -20.2) | +21.9% (-106.8 to +150.6) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.5 | -2.4% (-5.1 to +0.2) | +1.3% (-1.6 to +4.1) | -4.5% (-8.3 to -0.7) | **the runs disagree** |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | +6.7% (-0.5 to +13.8) | +6.7% (-0.5 to +13.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.347 | 0.347 | -0.1% (-6.1 to +6.0) | +1.9% (-5.9 to +9.7) | +0.8% (+0.0 to +1.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 521.7 | 521.5 | -0.0% (-7.0 to +6.9) | +1.8% (-5.9 to +9.5) | +0.8% (+0.0 to +1.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.703 | 0.705 | +0.3% (-9.1 to +9.7) | -3.1% (-10.1 to +3.9) | +1.5% (-3.6 to +6.6) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.8 | +75.3% (+65.1 to +85.5) | +85.2% (+68.4 to +102.0) | +76.0% (+73.6 to +78.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.4% (-4.1 to +1.2) | +1.2% (-1.5 to +3.9) | -3.3% (-7.2 to +0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 21 (13 trials, 2 allowed, 5 refused); acting: 20 to 21 (11 trials, 1 allowed, 3 refused); acting: 19 to 20 (10 trials, 1 allowed, 7 refused); run B: left native (24 trials, 0 allowed, 0 refused); acting: 20 to 21 (24 trials, 1 allowed, 0 refused); acting: 20 to 21 (21 trials, 1 allowed, 1 refused); run C: acting: 19 to 21 (14 trials, 2 allowed, 7 refused); acting: 19 to 20 (12 trials, 1 allowed, 7 refused); acting: 17 to 20 (13 trials, 3 allowed, 5 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,519, 2,771, 1,635 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 688.7 | 655.3 | -4.9% (-34.0 to +24.3) | +0.0% (-0.6 to +0.7) | +12.6% (-8.5 to +33.8) | **the runs disagree** |
| throughput (transactions a second) | 1,061 | 1,058 | -0.3% (-13.0 to +12.5) | +0.0% (-0.6 to +0.7) | +1.1% (-2.3 to +4.5) | STEADY, under the floor (the three runs' mean 0.28%) |
| latency, 95th percentile (ms, lag included) | 3,366 | 4,090 | +21.5% (-173.5 to +216.5) | -2.0% (-35.1 to +31.0) | -61.0% (-322.0 to +200.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 4,497 | 5,767 | +28.2% (-134.5 to +191.0) | -15.5% (-126.7 to +95.7) | -53.7% (-270.9 to +163.5) | **the runs disagree** |
| latency, median (ms) | 4.36 | 26.6 | +510.3% (-1668.3 to +2688.8) | +0.6% (-6.0 to +7.3) | -84.5% (-214.2 to +45.3) | **the runs disagree** |
| latency, mean (ms) | 620.1 | 660.7 | +6.5% (-177.3 to +190.4) | -2.5% (-28.2 to +23.2) | -52.5% (-246.7 to +141.7) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.1 | +0.5% (-1.6 to +2.5) | -7.2% (-15.4 to +0.9) | +0.1% (-0.1 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | +0.0% (+0.0 to +0.0) | +3.3% (-3.8 to +10.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.265 | 0.266 | +0.7% (-11.7 to +13.0) | +0.5% (-5.1 to +6.1) | -1.3% (-9.0 to +6.5) | **the runs disagree** |
| host CPU-seconds | 461.5 | 464.8 | +0.7% (-11.2 to +12.7) | +0.4% (-5.2 to +6.1) | -1.6% (-9.4 to +6.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 1.52 | 1.66 | +9.1% (-28.2 to +46.5) | +0.4% (-4.9 to +5.7) | -13.0% (-30.6 to +4.6) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.645 | 1.22 | +88.9% (+72.4 to +105.4) | +74.6% (+72.9 to +76.3) | +96.9% (+89.3 to +104.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | +0.4% (-1.3 to +2.1) | -7.0% (-8.7 to -5.3) | +0.1% (-0.1 to +0.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 20 to 21 (23 trials, 1 allowed, 1 refused); left native (22 trials, 0 allowed, 0 refused); left native (30 trials, 0 allowed, 0 refused); run B: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 14 to 20 (9 trials, 6 allowed, 3 refused); run C: left native (23 trials, 0 allowed, 0 refused); left native (25 trials, 0 allowed, 0 refused); left native (25 trials, 0 allowed, 0 refused).

**Across 3 workloads: 2 gauge-rows GAIN, 0 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 12 STEADY, 18 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
