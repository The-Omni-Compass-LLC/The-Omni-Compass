# sysbench on MySQL, a database's buffer pool as shipped: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native (`docs/MYSQL_PREREGISTRATION.md`, amendment 5); omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39382990197 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| B | 39412436421 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| C | 39461531771 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,958 | 2,960 | +0.1% (-0.2 to +0.3) | +0.0% (-0.4 to +0.4) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.06%) |
| throughput (transactions a second) | 2,966 | 2,967 | +0.0% (-0.2 to +0.3) | -0.0% (-0.5 to +0.4) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| queries a second | 2,966 | 2,967 | +0.0% (-0.2 to +0.3) | -0.0% (-0.5 to +0.4) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| latency, 95th percentile (ms) | 0.21 | 0.208 | -1.0% (-36.9 to +35.0) | +2.3% (-2.7 to +7.3) | -0.6% (-5.6 to +4.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.336 | 0.33 | -1.8% (-25.3 to +21.7) | +0.7% (-4.5 to +5.9) | +1.8% (-7.2 to +10.8) | **the runs disagree** |
| latency, mean (ms) | 0.0971 | 0.0961 | -1.1% (-37.7 to +35.5) | -14.6% (-59.4 to +30.2) | +0.3% (-5.3 to +5.8) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 140.2 | +9.5% (-2.9 to +21.9) | +2.6% (-4.9 to +10.1) | +9.4% (-2.5 to +21.3) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| pages holding data, mean (MB) | 121.2 | 136.2 | +12.3% (+0.5 to +24.2) | +4.6% (-7.8 to +16.9) | +12.0% (+0.7 to +23.2) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pages read from disk into the pool (misses) | 1,029,529 | 999,577 | -2.9% (-7.4 to +1.6) | -1.1% (-3.9 to +1.8) | -3.4% (-8.3 to +1.4) | shown, not judged |
| host CPU busy (share of the run) | 0.0752 | 0.0754 | +0.3% (-36.1 to +36.7) | +1.9% (-1.7 to +5.5) | +0.3% (-6.5 to +7.2) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 134.8 | 135.1 | +0.2% (-35.9 to +36.3) | +1.9% (-1.6 to +5.4) | +0.2% (-6.6 to +7.1) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 0.1 | 0.1 | +0.2% (-35.9 to +36.2) | +1.9% (-1.3 to +5.1) | +0.3% (-6.8 to +7.4) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 | +5.67 (+1.87 to +9.46) | +2.67 (-4.92 to +10.3) | +6 (+1.03 to +11) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 3 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (3 trials, 0 allowed, 3 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (3 trials, 0 allowed, 3 refused); left native (2 trials, 0 allowed, 2 refused); left native (4 trials, 0 allowed, 4 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.0 | 292.4 | -0.2% (-2.4 to +2.0) | -0.5% (-2.4 to +1.3) | -0.5% (-6.8 to +5.8) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 295.0 | 294.0 | -0.3% (-2.3 to +1.7) | -0.5% (-2.4 to +1.4) | -0.2% (-4.6 to +4.2) | EVEN, under the floor (every run under 0.5%; the largest 0.49%) |
| queries a second | 4,719 | 4,704 | -0.3% (-2.3 to +1.7) | -0.5% (-2.4 to +1.4) | -0.2% (-4.6 to +4.2) | EVEN, under the floor (every run under 0.5%; the largest 0.49%) |
| latency, 95th percentile (ms) | 5.67 | 5.6 | -1.2% (-3.7 to +1.4) | -0.6% (-7.4 to +6.2) | -1.3% (-17.3 to +14.7) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 7.84 | 7.7 | -1.8% (-6.3 to +2.7) | +0.0% (-4.5 to +4.5) | +140.9% (-582.3 to +864.2) | **the runs disagree** |
| latency, mean (ms) | 3.57 | 3.53 | -1.1% (-2.4 to +0.2) | -1.7% (-3.5 to +0.1) | +15.1% (-50.7 to +80.9) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 139.4 | +8.9% (+2.1 to +15.7) | +9.1% (+2.1 to +16.1) | +7.7% (-0.5 to +15.9) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pages holding data, mean (MB) | 120.3 | 137.1 | +13.9% (-0.0 to +27.9) | +13.9% (+5.3 to +22.4) | +12.1% (-4.7 to +28.9) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| pages read from disk into the pool (misses) | 580,528 | 555,558 | -4.3% (-8.7 to +0.1) | -8.0% (-17.0 to +1.1) | -3.6% (-10.6 to +3.5) | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.215 | -0.3% (-7.6 to +7.1) | -1.9% (-4.0 to +0.3) | -1.9% (-2.5 to -1.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| host CPU-seconds | 120.0 | 119.9 | -0.1% (-8.0 to +7.8) | -1.9% (-4.1 to +0.3) | -1.9% (-2.2 to -1.6) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 2.67 | 2.67 | -0.0% (-5.4 to +5.4) | -1.4% (-4.1 to +1.3) | -1.4% (-7.2 to +4.4) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 | +3.33 (+1.9 to +4.77) | +3.33 (+0.465 to +6.2) | +2.67 (-0.202 to +5.54) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.5 | 294.6 | +0.0% (-0.7 to +0.8) | +0.7% (-2.0 to +3.4) | -0.2% (-0.5 to +0.2) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 294.9 | 294.9 | +0.0% (-0.6 to +0.6) | +0.5% (-0.8 to +1.9) | -0.1% (-0.6 to +0.3) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| queries a second | 4,718 | 4,719 | +0.0% (-0.6 to +0.6) | +0.5% (-0.8 to +1.9) | -0.1% (-0.6 to +0.3) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, 95th percentile (ms) | 4.33 | 4.25 | -1.8% (-1.8 to -1.7) | +0.6% (-4.6 to +5.8) | -4.1% (-6.6 to -1.6) | **the runs disagree** |
| latency, 99th percentile (ms) | 6.21 | 6.06 | -2.4% (-9.1 to +4.4) | -36.9% (-207.2 to +133.4) | -1.8% (-6.3 to +2.7) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, mean (ms) | 3.28 | 3.24 | -1.4% (-3.1 to +0.3) | -8.3% (-39.0 to +22.5) | -3.1% (-4.2 to -1.9) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 137.0 | +7.0% (+1.7 to +12.4) | +4.6% (+1.7 to +7.4) | +7.0% (+4.5 to +9.5) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 120.1 | 135.4 | +12.7% (+7.6 to +17.8) | +9.5% (+4.9 to +14.0) | +12.7% (+10.0 to +15.5) | **power given in all three of our runs** |
| pages read from disk into the pool (misses) | 1,979,239 | 1,908,468 | -3.6% (-5.7 to -1.5) | -2.1% (-4.8 to +0.5) | -3.6% (-6.5 to -0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.199 | -1.5% (-4.7 to +1.7) | +0.6% (-3.6 to +4.8) | -2.9% (-4.0 to -1.8) | **the runs disagree** |
| host CPU-seconds | 337.6 | 332.6 | -1.5% (-4.7 to +1.7) | +0.6% (-3.6 to +4.8) | -2.9% (-4.0 to -1.8) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.47 | -1.5% (-4.1 to +1.1) | -0.1% (-1.7 to +1.4) | -2.7% (-4.1 to -1.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 | +6.67 (+3.8 to +9.54) | +4.67 (+1.8 to +7.54) | +7.33 (+4.46 to +10.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 3 refused); left native (5 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 3 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 2 refused); run C: left native (5 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 111.8 | 103.8 | -7.1% (-52.0 to +37.8) | -0.1% (-2.2 to +2.0) | +0.7% (-0.1 to +1.4) | **the runs disagree** |
| throughput (transactions a second) | 196.6 | 196.7 | +0.0% (-0.6 to +0.7) | -0.3% (-1.5 to +0.9) | -0.1% (-1.1 to +0.9) | EVEN, under the floor (every run under 0.5%; the largest 0.31%) |
| queries a second | 3,933 | 3,934 | +0.0% (-0.6 to +0.7) | -0.3% (-1.5 to +0.9) | -0.1% (-1.1 to +0.9) | EVEN, under the floor (every run under 0.5%; the largest 0.31%) |
| latency, 95th percentile (ms) | 364.7 | 419.3 | +15.0% (-36.2 to +66.1) | -1.2% (-3.8 to +1.4) | -7.7% (-26.7 to +11.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 741.5 | 916.1 | +23.6% (-50.2 to +97.3) | +0.6% (-6.2 to +7.5) | -41.0% (-144.9 to +63.0) | **the runs disagree** |
| latency, mean (ms) | 71.3 | 82.9 | +16.4% (-63.0 to +95.7) | +0.1% (-2.9 to +3.0) | -6.1% (-15.4 to +3.3) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 144.2 | +12.6% (+6.2 to +19.0) | +10.3% (+8.1 to +12.5) | +3.3% (-6.9 to +13.5) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pages holding data, mean (MB) | 122.0 | 136.8 | +12.1% (+5.5 to +18.7) | +10.6% (+8.9 to +12.3) | +3.1% (-9.1 to +15.3) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pages read from disk into the pool (misses) | 1,660,503 | 1,583,670 | -4.6% (-9.2 to -0.1) | -4.2% (-9.5 to +1.0) | -2.0% (-5.6 to +1.6) | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.211 | -0.4% (-1.3 to +0.4) | -1.2% (-2.4 to +0.0) | -0.3% (-4.1 to +3.6) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 378.7 | 377.1 | -0.4% (-1.3 to +0.5) | -1.3% (-2.6 to +0.1) | -0.3% (-4.0 to +3.5) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 7.56 | 7.97 | +5.4% (-39.9 to +50.6) | -1.1% (-4.6 to +2.3) | -0.9% (-5.3 to +3.5) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 9 | +9 (+6.52 to +11.5) | +10.7 (+7.8 to +13.5) | +3.33 (-7.01 to +13.7) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (5 trials, 0 allowed, 4 refused); left native (5 trials, 0 allowed, 4 refused); left native (5 trials, 0 allowed, 5 refused); run B: left native (6 trials, 0 allowed, 6 refused); left native (5 trials, 0 allowed, 5 refused); left native (5 trials, 0 allowed, 5 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11.0 | 8.6 | -21.7% (-113.4 to +70.0) | -1.1% (-57.2 to +55.0) | -38.2% (-84.3 to +7.9) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 984.5 | 984.5 | +0.0% (-0.5 to +0.5) | +0.1% (-0.3 to +0.4) | -0.1% (-0.3 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.12%) |
| queries a second | 984.5 | 984.5 | +0.0% (-0.5 to +0.5) | +0.1% (-0.3 to +0.4) | -0.1% (-0.3 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.12%) |
| latency, 95th percentile (ms) | 2.12 | 2.33 | +9.8% (-53.2 to +72.8) | -2.3% (-188.0 to +183.3) | +13.8% (-4.2 to +31.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 5.19 | 5.33 | +2.7% (-142.9 to +148.3) | -7.6% (-180.4 to +165.2) | +23.8% (-30.4 to +78.0) | **the runs disagree** |
| latency, mean (ms) | 1.19 | 1.23 | +3.6% (-42.7 to +49.9) | -15.7% (-217.0 to +185.5) | +12.4% (-37.7 to +62.4) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 141.8 | +10.8% (+4.2 to +17.4) | +7.9% (+0.3 to +15.5) | +7.5% (+2.4 to +12.6) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 118.6 | 127.7 | +7.7% (+2.8 to +12.6) | +5.1% (-0.4 to +10.5) | +5.9% (+4.6 to +7.1) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| pages read from disk into the pool (misses) | 416,168 | 407,051 | -2.2% (-4.8 to +0.4) | -1.8% (-2.9 to -0.7) | -1.4% (-4.4 to +1.7) | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.272 | +48.3% (-99.3 to +196.0) | -1.8% (-11.2 to +7.6) | +11.9% (-12.9 to +36.8) | **the runs disagree** |
| host CPU-seconds | 284.6 | 423.9 | +48.9% (-100.3 to +198.2) | -1.8% (-11.0 to +7.5) | +11.8% (-12.9 to +36.5) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 84.4 | 111.1 | +31.6% (-210.3 to +273.4) | -10.9% (-93.7 to +72.0) | +95.1% (-70.7 to +260.8) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 8 | +8 (+8 to +8) | +6.67 (+3.8 to +9.54) | +7.33 (+1.6 to +13.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); run B: left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 4 refused); left native (3 trials, 0 allowed, 3 refused); run C: left native (5 trials, 0 allowed, 5 refused); left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused).

**Across 4 untouched workloads: 12 gauge-rows GAIN (0 in all three of our runs), 2 LOSS (0 in all three of our runs), 8 power given (3 in all three of our runs), 10 EVEN, 16 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
