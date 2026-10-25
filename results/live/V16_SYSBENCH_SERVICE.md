# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39869901058 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| B | 39869925397 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| C | 39871679567 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,918 | 2,915 | -0.1% (-0.6 to +0.4) | -0.0% (-0.1 to +0.1) | -0.3% (-2.1 to +1.5) | STEADY, under the floor (the three runs' mean 0.14%) |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% (-0.1 to +0.1) | -0.1% (-0.3 to +0.1) | -0.1% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.05%) |
| queries a second | 2,953 | 2,953 | +0.0% (-0.1 to +0.1) | -0.1% (-0.3 to +0.1) | -0.1% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.413 | 0.428 | +3.7% (-12.3 to +19.7) | -7.4% (-20.8 to +6.0) | -1.1% (-20.8 to +18.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.638 | 0.657 | +3.0% (+0.7 to +5.4) | -5.7% (-15.5 to +4.1) | +13.8% (-65.6 to +93.2) | **the runs disagree** |
| latency, mean (ms) | 0.228 | 0.235 | +3.3% (-2.5 to +9.2) | -4.0% (-15.2 to +7.2) | +39.8% (-139.6 to +219.2) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 524.5 | +2.4% (+1.1 to +3.8) | +0.2% (-9.4 to +9.8) | +2.6% (-12.8 to +18.1) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 463.5 | 460.8 | -0.6% (-5.5 to +4.3) | -1.6% (-7.5 to +4.3) | -0.0% (-21.1 to +21.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 366,968 | 365,381 | -0.4% (-9.4 to +8.5) | +2.1% (-16.4 to +20.6) | -3.7% (-40.1 to +32.7) | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.121 | +4.5% (-3.8 to +12.8) | -8.1% (-28.1 to +11.9) | +0.3% (-2.2 to +2.8) | **the runs disagree** |
| host CPU-seconds | 191.7 | 200.5 | +4.6% (-3.8 to +12.9) | -8.2% (-28.5 to +12.1) | +0.4% (-2.2 to +2.9) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.15 | +4.7% (-4.1 to +13.4) | -8.2% (-28.4 to +12.0) | +0.7% (-3.6 to +4.9) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 16.0 | +16 (+6.06 to +25.9) | +11 (+4.43 to +17.6) | +12.7 (+1.19 to +24.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (7 trials, 0 allowed, 4 refused); acting: 384 to 640 (10 trials, 2 allowed, 3 refused); acting: 384 to 640 (7 trials, 2 allowed, 3 refused); run B: acting: 384 to 640 (5 trials, 2 allowed, 2 refused); acting: 512 to 640 (8 trials, 1 allowed, 3 refused); acting: 256 to 640 (7 trials, 3 allowed, 2 refused); run C: acting: 512 to 640 (6 trials, 1 allowed, 4 refused); acting: 384 to 768 (7 trials, 3 allowed, 1 refused); acting: 384 to 640 (8 trials, 2 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290.0 | 291.4 | +0.5% (-0.0 to +0.9) | +0.6% (-1.0 to +2.2) | +0.4% (-1.2 to +1.9) | STEADY, under the floor (the three runs' mean 0.49%) |
| throughput (transactions a second) | 292.6 | 293.2 | +0.2% (-0.9 to +1.3) | +0.5% (-0.3 to +1.3) | +0.4% (-1.3 to +2.1) | STEADY, under the floor (the three runs' mean 0.37%) |
| queries a second | 4,682 | 4,691 | +0.2% (-0.9 to +1.3) | +0.5% (-0.3 to +1.3) | +0.4% (-1.3 to +2.1) | STEADY, under the floor (the three runs' mean 0.37%) |
| latency, 95th percentile (ms) | 5.68 | 5.47 | -3.6% (-15.6 to +8.4) | -4.8% (-14.5 to +5.0) | +0.6% (-9.7 to +10.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 8.28 | 7.89 | -4.8% (-14.3 to +4.8) | -4.8% (-20.5 to +11.0) | -0.6% (-7.4 to +6.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.4 | 3.33 | -2.1% (-11.1 to +6.8) | -6.0% (-41.8 to +29.8) | +0.7% (-5.8 to +7.1) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 522.0 | +2.0% (-10.3 to +14.2) | -10.1% (-24.6 to +4.4) | -14.2% (-45.0 to +16.7) | **the runs disagree** |
| pages holding data, mean (MB) | 446.1 | 423.8 | -5.0% (-19.3 to +9.3) | -9.2% (-23.3 to +5.0) | -14.6% (-46.3 to +17.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 241,863 | 241,499 | -0.2% (-17.7 to +17.4) | +2.9% (-11.3 to +17.2) | +5.7% (-11.3 to +22.7) | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.188 | +1.6% (-1.3 to +4.4) | +0.7% (-6.3 to +7.7) | +0.7% (-7.3 to +8.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 102.0 | 103.7 | +1.7% (-1.2 to +4.5) | +0.6% (-6.2 to +7.5) | +0.6% (-7.6 to +8.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.33 | +1.2% (-1.3 to +3.7) | +0.0% (-6.6 to +6.7) | +0.3% (-7.1 to +7.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 | +6.33 (+4.9 to +7.77) | +6 (+6 to +6) | +4.67 (+3.23 to +6.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (5 trials, 1 allowed, 0 refused); left native (4 trials, 0 allowed, 1 refused); acting: 512 to 640 (5 trials, 1 allowed, 1 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); acting: 384 to 512 (4 trials, 1 allowed, 2 refused); run C: acting: 384 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.6 | 294.4 | -0.1% (-0.8 to +0.6) | +0.1% (-0.8 to +1.0) | -0.2% (-1.4 to +1.1) | STEADY, under the floor (the three runs' mean 0.07%) |
| throughput (transactions a second) | 294.8 | 294.7 | -0.0% (-0.9 to +0.8) | +0.1% (-0.9 to +1.1) | -0.1% (-1.3 to +1.1) | STEADY, under the floor (the three runs' mean 0.02%) |
| queries a second | 4,717 | 4,715 | -0.0% (-0.9 to +0.8) | +0.1% (-0.9 to +1.1) | -0.1% (-1.3 to +1.1) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 4.24 | 4.18 | -1.3% (-27.6 to +25.0) | -4.1% (-13.3 to +5.0) | -1.2% (-6.3 to +3.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.55 | 5.61 | +1.2% (-23.8 to +26.3) | -4.1% (-9.1 to +0.9) | +1.2% (-4.1 to +6.5) | **the runs disagree** |
| latency, mean (ms) | 3.22 | 3.19 | -0.9% (-13.7 to +12.0) | -1.9% (-11.3 to +7.6) | +0.1% (-3.1 to +3.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 567.1 | +10.8% (-23.5 to +45.0) | +13.2% (-24.5 to +51.0) | +11.9% (-12.8 to +36.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 462.0 | 491.4 | +6.3% (-27.5 to +40.2) | +8.9% (-15.9 to +33.6) | +11.3% (-17.3 to +39.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 653,899 | 556,781 | -14.9% (-76.9 to +47.2) | -16.5% (-68.1 to +35.2) | -24.8% (-69.2 to +19.6) | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.192 | -1.3% (-19.0 to +16.5) | -0.4% (-4.4 to +3.6) | -0.8% (-5.8 to +4.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 322.7 | 318.6 | -1.3% (-19.2 to +16.6) | -0.4% (-4.5 to +3.7) | -0.8% (-5.7 to +4.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.37 | -1.2% (-18.7 to +16.3) | -0.4% (-5.5 to +4.6) | -0.6% (-4.7 to +3.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 15.0 | +15 (+6.39 to +23.6) | +15.3 (+11.5 to +19.1) | +15.7 (+7.68 to +23.7) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 1024 (15 trials, 5 allowed, 1 refused); acting: 512 to 640 (14 trials, 1 allowed, 2 refused); acting: 512 to 640 (13 trials, 1 allowed, 3 refused); run B: acting: 512 to 1024 (15 trials, 4 allowed, 2 refused); left native (12 trials, 0 allowed, 4 refused); acting: 512 to 896 (12 trials, 3 allowed, 1 refused); run C: left native (12 trials, 0 allowed, 5 refused); acting: 512 to 768 (8 trials, 2 allowed, 3 refused); acting: 384 to 768 (10 trials, 3 allowed, 2 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.6 | 193.3 | +0.9% (-0.2 to +2.0) | +9.3% (-16.7 to +35.4) | -0.3% (-1.6 to +0.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 196.4 | 196.9 | +0.2% (-0.5 to +0.9) | -0.1% (-1.1 to +1.0) | -0.2% (-1.3 to +1.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| queries a second | 3,929 | 3,937 | +0.2% (-0.5 to +0.9) | -0.1% (-1.1 to +1.0) | -0.2% (-1.3 to +1.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 8.79 | 8.13 | -7.5% (-16.4 to +1.5) | -25.8% (-99.9 to +48.3) | -0.7% (-14.2 to +12.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 12.9 | 12.1 | -6.4% (-12.6 to -0.1) | -32.2% (-153.4 to +88.9) | +4.3% (-8.9 to +17.4) | **the runs disagree** |
| latency, mean (ms) | 5.48 | 5.4 | -1.4% (-5.3 to +2.6) | -31.6% (-129.3 to +66.1) | +1.9% (-13.0 to +16.8) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 691.9 | +35.1% (+3.2 to +67.0) | +11.8% (-17.7 to +41.3) | +8.4% (-34.0 to +50.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 462.1 | 575.7 | +24.6% (+3.5 to +45.7) | +9.3% (-17.6 to +36.2) | +5.3% (-22.9 to +33.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 616,615 | 413,218 | -33.0% (-68.2 to +2.2) | -14.5% (-60.1 to +31.2) | -5.0% (-48.8 to +38.7) | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.22 | -1.7% (-6.9 to +3.6) | -1.2% (-7.4 to +4.9) | -3.9% (-14.3 to +6.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 360.6 | 354.8 | -1.6% (-6.9 to +3.6) | -1.3% (-7.3 to +4.7) | -3.9% (-14.2 to +6.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 4.11 | 4.01 | -2.5% (-8.7 to +3.8) | -10.7% (-41.9 to +20.5) | -3.5% (-15.0 to +8.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 | +20.7 (+15.5 to +25.8) | +16.3 (+11.2 to +21.5) | +16.7 (+7.94 to +25.4) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 1152 (16 trials, 5 allowed, 1 refused); acting: 512 to 1024 (17 trials, 4 allowed, 2 refused); acting: 512 to 1024 (13 trials, 4 allowed, 2 refused); run B: acting: 512 to 768 (12 trials, 2 allowed, 3 refused); acting: 512 to 640 (7 trials, 1 allowed, 5 refused); acting: 384 to 640 (9 trials, 2 allowed, 3 refused); run C: acting: 384 to 640 (8 trials, 2 allowed, 4 refused); acting: 384 to 640 (6 trials, 2 allowed, 3 refused); acting: 512 to 896 (10 trials, 3 allowed, 2 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.21 | 3.87 | -8.1% (-252.4 to +236.1) | +38.9% (-69.3 to +147.1) | -28.0% (-85.2 to +29.2) | **the runs disagree** |
| throughput (transactions a second) | 984.2 | 983.8 | -0.0% (-0.1 to +0.1) | -0.1% (-0.5 to +0.3) | +0.0% (-1.3 to +1.3) | STEADY, under the floor (the three runs' mean 0.03%) |
| queries a second | 984.2 | 983.8 | -0.0% (-0.1 to +0.1) | -0.1% (-0.5 to +0.3) | +0.0% (-1.3 to +1.3) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 1.6 | 1.73 | +8.5% (-9.5 to +26.4) | -13.4% (-131.2 to +104.5) | +0.4% (-24.9 to +25.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 2.49 | 3.08 | +23.5% (-9.7 to +56.7) | -23.7% (-129.1 to +81.7) | +0.6% (-10.8 to +11.9) | **the runs disagree** |
| latency, mean (ms) | 1.03 | 1.1 | +7.5% (-1.7 to +16.7) | -20.9% (-145.3 to +103.6) | +0.8% (-8.8 to +10.5) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 552.6 | +7.9% (-6.2 to +22.1) | -3.5% (-15.5 to +8.5) | +14.2% (-32.7 to +61.1) | **the runs disagree** |
| pages holding data, mean (MB) | 453.9 | 461.4 | +1.6% (-23.4 to +26.7) | -5.6% (-22.4 to +11.2) | +4.8% (-20.5 to +30.2) | **the runs disagree** |
| pages read from disk into the pool (misses) | 188,900 | 187,171 | -0.9% (-23.3 to +21.5) | +6.6% (-15.4 to +28.6) | -5.6% (-26.9 to +15.7) | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.161 | +25.6% (-87.1 to +138.3) | -3.3% (-8.3 to +1.8) | +3.8% (-35.8 to +43.5) | **the runs disagree** |
| host CPU-seconds | 197.2 | 248.9 | +26.2% (-88.3 to +140.7) | -3.3% (-8.5 to +2.0) | +3.8% (-35.4 to +43.1) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 135.0 | 183.3 | +35.8% (-233.8 to +305.4) | -32.3% (-111.9 to +47.2) | +35.8% (-28.4 to +100.0) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 | +18.3 (+4.65 to +32) | +14.7 (+5.94 to +23.4) | +16.7 (+6.63 to +26.7) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 768 (14 trials, 3 allowed, 3 refused); acting: 512 to 768 (16 trials, 2 allowed, 2 refused); acting: 512 to 896 (10 trials, 3 allowed, 3 refused); run B: acting: 384 to 512 (8 trials, 1 allowed, 3 refused); acting: 512 to 640 (10 trials, 1 allowed, 4 refused); acting: 384 to 768 (11 trials, 3 allowed, 2 refused); run C: acting: 384 to 512 (11 trials, 1 allowed, 4 refused); acting: 512 to 1280 (17 trials, 6 allowed, 1 refused); acting: 512 to 768 (18 trials, 2 allowed, 1 refused).

**Across 4 untouched workloads: 12 gauge-rows GAIN, 0 LOSS, 7 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
