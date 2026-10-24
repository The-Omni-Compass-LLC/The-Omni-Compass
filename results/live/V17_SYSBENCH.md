# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40003726359 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| B | 40022500639 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| C | 40037193927 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,948 | -0.0% (-0.1 to +0.1) | +0.1% (-0.7 to +0.9) | -0.0% (-0.3 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| throughput (transactions a second) | 2,951 | 2,951 | -0.0% (-0.1 to +0.1) | -0.0% (-0.4 to +0.4) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.03%) |
| queries a second | 2,951 | 2,951 | -0.0% (-0.1 to +0.1) | -0.0% (-0.4 to +0.4) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.03%) |
| latency, 95th percentile (ms) | 0.328 | 0.312 | -4.9% (-23.0 to +13.3) | +5.8% (-23.3 to +34.8) | -5.4% (-32.3 to +21.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.44 | 0.429 | -2.5% (-11.6 to +6.6) | -1.3% (-19.8 to +17.3) | -0.6% (-17.3 to +16.1) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.201 | 0.195 | -3.1% (-14.1 to +8.0) | -76.5% (-418.3 to +265.3) | -0.9% (-23.9 to +22.0) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 471.8 | -7.9% (-24.1 to +8.4) | -18.9% (-39.9 to +2.2) | -10.9% (-27.0 to +5.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pages holding data, mean (MB) | 463.5 | 420.0 | -9.4% (-25.6 to +6.8) | -18.0% (-41.2 to +5.3) | -9.8% (-23.9 to +4.3) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pages read from disk into the pool (misses) | 366,730 | 423,747 | +15.5% (-23.5 to +54.6) | +32.6% (-2.1 to +67.3) | +14.7% (-23.2 to +52.7) | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0949 | -5.2% (-28.6 to +18.2) | +4.8% (-14.5 to +24.1) | +4.5% (-1.7 to +10.7) | **the runs disagree** |
| host CPU-seconds | 165.9 | 157.4 | -5.1% (-28.9 to +18.7) | +4.8% (-14.6 to +24.1) | +4.5% (-1.7 to +10.7) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.123 | 0.117 | -5.1% (-28.9 to +18.7) | +4.7% (-15.4 to +24.7) | +4.5% (-1.8 to +10.8) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 | +9.67 (+5.87 to +13.5) | +7.33 (-3.87 to +18.5) | +10 (+2.55 to +17.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (8 trials, 1 allowed, 3 refused); acting: 256 to 512 (5 trials, 2 allowed, 1 refused); acting: 256 to 512 (5 trials, 2 allowed, 2 refused); run B: acting: 256 to 512 (3 trials, 2 allowed, 0 refused); acting: 256 to 512 (8 trials, 2 allowed, 3 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused); run C: acting: 384 to 512 (6 trials, 1 allowed, 4 refused); acting: 256 to 512 (7 trials, 2 allowed, 2 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 285.1 | 283.0 | -0.7% (-3.3 to +1.8) | +0.3% (-0.5 to +1.0) | -1.2% (-2.2 to -0.1) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| throughput (transactions a second) | 294.8 | 294.2 | -0.2% (-1.1 to +0.7) | +0.3% (-0.5 to +1.0) | -1.2% (-2.3 to -0.0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| queries a second | 4,718 | 4,707 | -0.2% (-1.1 to +0.7) | +0.3% (-0.5 to +1.0) | -1.2% (-2.3 to -0.0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| latency, 95th percentile (ms) | 4.91 | 5.92 | +20.6% (-88.9 to +130.1) | -1.8% (-9.5 to +5.9) | +0.0% (+0.0 to +0.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 55.6 | 67.8 | +21.9% (-93.3 to +137.0) | -0.6% (-7.3 to +6.1) | -1.2% (-6.4 to +4.0) | **the runs disagree** |
| latency, mean (ms) | 3.69 | 4.14 | +12.3% (-42.4 to +67.0) | -0.8% (-4.5 to +3.0) | +0.7% (+0.1 to +1.4) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 359.0 | -29.9% (-71.5 to +11.7) | -6.2% (-20.6 to +8.3) | -1.5% (-11.2 to +8.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pages holding data, mean (MB) | 442.8 | 316.8 | -28.5% (-73.4 to +16.4) | -4.1% (-23.7 to +15.5) | -3.8% (-25.3 to +17.6) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| pages read from disk into the pool (misses) | 245,466 | 298,167 | +21.5% (-25.3 to +68.3) | +1.5% (-4.1 to +7.2) | +0.4% (-16.0 to +16.7) | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.164 | +0.1% (-3.4 to +3.6) | +0.6% (-11.2 to +12.5) | +0.2% (-3.7 to +4.0) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 98.0 | 98.1 | +0.1% (-3.4 to +3.6) | +0.9% (-12.0 to +13.7) | +0.4% (-3.6 to +4.4) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 2.26 | 2.28 | +0.8% (-3.8 to +5.4) | +0.5% (-11.8 to +12.8) | +1.6% (-1.5 to +4.6) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| buffer pool size changes written (the knob's moves) | 0 | 5 | +5 (+0.0313 to +9.97) | +6.67 (+1.5 to +11.8) | +6 (+1.03 to +11) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (4 trials, 1 allowed, 1 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused); acting: 256 to 512 (4 trials, 2 allowed, 0 refused); run B: acting: 384 to 512 (5 trials, 1 allowed, 1 refused); left native (6 trials, 0 allowed, 1 refused); left native (6 trials, 0 allowed, 1 refused); run C: left native (5 trials, 0 allowed, 1 refused); left native (7 trials, 0 allowed, 2 refused); left native (5 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.6 | 294.6 | +0.3% (-0.3 to +0.9) | -0.2% (-2.4 to +1.9) | +0.1% (-0.9 to +1.1) | EVEN, under the floor (every run under 0.5%; the largest 0.34%) |
| throughput (transactions a second) | 293.9 | 294.9 | +0.3% (-0.3 to +0.9) | -0.2% (-2.4 to +1.9) | +0.1% (-0.9 to +1.1) | EVEN, under the floor (every run under 0.5%; the largest 0.33%) |
| queries a second | 4,703 | 4,719 | +0.3% (-0.3 to +0.9) | -0.2% (-2.4 to +1.9) | +0.1% (-0.9 to +1.1) | EVEN, under the floor (every run under 0.5%; the largest 0.33%) |
| latency, 95th percentile (ms) | 4.25 | 4.18 | -1.8% (-1.8 to -1.7) | -1.2% (-3.7 to +1.4) | -3.0% (-8.0 to +2.1) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 5.81 | 5.67 | -2.4% (-5.0 to +0.2) | -2.9% (-7.9 to +2.0) | -1.2% (-8.0 to +5.6) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, mean (ms) | 3.27 | 3.25 | -0.8% (-2.4 to +0.9) | -0.4% (-4.0 to +3.3) | -1.5% (-3.8 to +0.7) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 558.2 | +9.0% (-10.0 to +28.0) | -0.8% (-7.3 to +5.7) | +0.1% (-7.9 to +8.2) | **the runs disagree** |
| pages holding data, mean (MB) | 461.9 | 500.7 | +8.4% (-4.3 to +21.1) | -0.1% (-5.6 to +5.4) | -1.3% (-2.5 to -0.2) | **the runs disagree** |
| pages read from disk into the pool (misses) | 652,231 | 529,367 | -18.8% (-52.6 to +15.0) | -3.5% (-16.1 to +9.2) | -3.1% (-13.4 to +7.3) | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.197 | -0.2% (-3.9 to +3.4) | +0.1% (-8.0 to +8.3) | -1.4% (-6.4 to +3.6) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 326.6 | 325.8 | -0.2% (-4.2 to +3.8) | +0.2% (-8.0 to +8.5) | -1.3% (-6.6 to +4.0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.42 | -0.6% (-5.1 to +4.0) | +0.5% (-5.7 to +6.6) | -1.4% (-5.7 to +2.8) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| buffer pool size changes written (the knob's moves) | 0 | 16.0 | +16 (+2.17 to +29.8) | +15.7 (+6.94 to +24.4) | +19 (+3.89 to +34.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 512 to 640 (16 trials, 1 allowed, 4 refused); left native (13 trials, 0 allowed, 3 refused); acting: 512 to 640 (14 trials, 1 allowed, 3 refused); run B: left native (12 trials, 0 allowed, 4 refused); acting: 384 to 512 (10 trials, 1 allowed, 4 refused); acting: 384 to 512 (11 trials, 1 allowed, 3 refused); run C: left native (14 trials, 0 allowed, 4 refused); acting: 512 to 640 (13 trials, 1 allowed, 4 refused); acting: 384 to 512 (11 trials, 1 allowed, 4 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194.0 | 194.1 | +0.1% (-1.5 to +1.6) | -0.5% (-1.9 to +0.8) | +0.1% (-0.9 to +1.1) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 196.7 | 197.1 | +0.2% (-1.0 to +1.5) | -0.4% (-1.9 to +1.1) | -0.1% (-0.7 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.39%) |
| queries a second | 3,933 | 3,943 | +0.2% (-1.0 to +1.5) | -0.4% (-1.9 to +1.1) | -0.1% (-0.7 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.39%) |
| latency, 95th percentile (ms) | 7.17 | 7.43 | +3.7% (-8.4 to +15.7) | +1.2% (-10.1 to +12.5) | -3.5% (-15.1 to +8.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 11.6 | 12.1 | +4.3% (-5.2 to +13.9) | +0.6% (-8.7 to +9.9) | -2.3% (-15.8 to +11.2) | **the runs disagree** |
| latency, mean (ms) | 4.64 | 4.65 | +0.2% (-4.0 to +4.5) | -0.5% (-2.9 to +1.9) | -1.6% (-6.2 to +3.0) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 507.4 | -0.9% (-17.2 to +15.4) | +0.9% (-4.4 to +6.3) | +13.1% (+6.3 to +19.8) | **the runs disagree** |
| pages holding data, mean (MB) | 461.9 | 454.7 | -1.6% (-21.9 to +18.8) | -0.2% (-8.1 to +7.7) | +9.9% (+1.0 to +18.7) | **the runs disagree** |
| pages read from disk into the pool (misses) | 615,792 | 627,293 | +1.9% (-22.3 to +26.1) | -0.5% (-15.9 to +14.8) | -15.3% (-17.1 to -13.6) | shown, not judged |
| host CPU busy (share of the run) | 0.25 | 0.248 | -0.5% (-4.9 to +3.8) | -1.8% (-3.3 to -0.3) | -2.8% (-8.9 to +3.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| host CPU-seconds | 440.6 | 438.1 | -0.6% (-5.1 to +3.9) | -1.7% (-3.6 to +0.2) | -2.8% (-9.1 to +3.5) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 4.96 | 4.93 | -0.6% (-5.5 to +4.3) | -1.2% (-4.4 to +2.0) | -2.9% (-10.1 to +4.4) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| buffer pool size changes written (the knob's moves) | 0 | 14.0 | +14 (+5.04 to +23) | +14.7 (+11.8 to +17.5) | +18.3 (+10.3 to +26.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (12 trials, 1 allowed, 4 refused); left native (13 trials, 0 allowed, 4 refused); left native (12 trials, 0 allowed, 3 refused); run B: acting: 384 to 640 (10 trials, 2 allowed, 3 refused); left native (11 trials, 0 allowed, 3 refused); acting: 512 to 640 (11 trials, 1 allowed, 4 refused); run C: acting: 512 to 640 (12 trials, 1 allowed, 4 refused); acting: 512 to 768 (15 trials, 2 allowed, 3 refused); acting: 384 to 640 (13 trials, 2 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.18 | 0.923 | -21.9% (-212.6 to +168.8) | -4.4% (-59.0 to +50.2) | -17.2% (-100.9 to +66.5) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 983.7 | 983.9 | +0.0% (-1.0 to +1.0) | -0.1% (-0.8 to +0.5) | +0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.12%) |
| queries a second | 983.7 | 983.9 | +0.0% (-1.0 to +1.0) | -0.1% (-0.8 to +0.5) | +0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.12%) |
| latency, 95th percentile (ms) | 2.1 | 2.13 | +1.7% (-10.4 to +13.8) | +11.9% (-331.7 to +355.5) | -3.8% (-38.8 to +31.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 4.91 | 5.06 | +3.0% (+0.5 to +5.6) | +9.4% (-126.9 to +145.7) | -8.8% (-25.8 to +8.2) | **the runs disagree** |
| latency, mean (ms) | 1.19 | 1.22 | +1.9% (-1.6 to +5.5) | +23.0% (-240.1 to +286.0) | -1.7% (-14.0 to +10.7) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 512.4 | +0.1% (-2.3 to +2.5) | -30.6% (-52.2 to -9.1) | -21.7% (-29.7 to -13.6) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 2 of 3 clear of the noise) |
| pages holding data, mean (MB) | 453.5 | 444.7 | -1.9% (-5.9 to +2.0) | -34.2% (-55.5 to -12.8) | -25.8% (-37.7 to -13.9) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| pages read from disk into the pool (misses) | 188,459 | 190,222 | +0.9% (-1.5 to +3.4) | +54.9% (+22.7 to +87.1) | +45.3% (+28.6 to +62.1) | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.127 | -2.3% (-27.0 to +22.4) | +2.0% (-13.5 to +17.5) | +0.6% (-11.3 to +12.4) | **the runs disagree** |
| host CPU-seconds | 199.1 | 194.8 | -2.1% (-26.2 to +21.9) | +2.0% (-13.5 to +17.4) | +0.5% (-11.3 to +12.4) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 534.8 | 463.2 | -13.4% (-165.8 to +139.0) | +6.2% (-57.9 to +70.4) | +9.3% (-115.8 to +134.4) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 | +14.3 (+10.5 to +18.1) | +11 (+8.52 to +13.5) | +17.3 (+7.29 to +27.4) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (14 trials, 0 allowed, 2 refused); left native (16 trials, 0 allowed, 4 refused); left native (14 trials, 0 allowed, 2 refused); run B: acting: 128 to 512 (6 trials, 3 allowed, 3 refused); acting: 128 to 512 (5 trials, 3 allowed, 1 refused); acting: 128 to 512 (5 trials, 3 allowed, 2 refused); run C: acting: 128 to 512 (7 trials, 3 allowed, 2 refused); acting: 128 to 512 (7 trials, 3 allowed, 4 refused); acting: 128 to 512 (9 trials, 3 allowed, 3 refused).

**Across 4 untouched workloads: 14 gauge-rows GAIN (0 in all three of our runs), 5 LOSS (0 in all three of our runs), 3 power given (0 in all three of our runs), 11 EVEN, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
