# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39182906799 | `bc2eb38f4ca8` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| B | 39184157413 | `75478eb28444` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| C | 39184175254 | `75478eb28444` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,948 | -0.1% (-1.2 to +1.0) | +0.3% (-0.2 to +0.8) | -0.0% (-0.4 to +0.4) | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (transactions a second) | 2,964 | 2,966 | +0.0% (-0.0 to +0.1) | -0.0% (-0.3 to +0.3) | -0.0% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.00%) |
| queries a second | 2,964 | 2,966 | +0.0% (-0.0 to +0.1) | -0.0% (-0.3 to +0.3) | -0.0% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.24 | 0.244 | +1.8% (-6.0 to +9.6) | -8.1% (-28.4 to +12.2) | -1.2% (-6.5 to +4.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.388 | 0.407 | +5.0% (-14.2 to +24.2) | -10.2% (-35.8 to +15.4) | -1.3% (-4.0 to +1.5) | **the runs disagree** |
| latency, mean (ms) | 0.393 | 0.513 | +30.5% (-246.5 to +307.4) | -6.1% (-28.0 to +15.9) | +0.3% (-2.9 to +3.5) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 486.9 | -4.9% (-9.5 to -0.3) | +3.0% (-15.6 to +21.7) | +4.8% (-23.7 to +33.4) | **the runs disagree** |
| pages holding data, mean (MB) | 463.5 | 445.5 | -3.9% (-11.7 to +3.9) | +2.1% (-16.0 to +20.2) | -0.5% (-25.9 to +24.9) | **the runs disagree** |
| pages read from disk into the pool (misses) | 367,409 | 372,458 | +1.4% (-7.1 to +9.8) | -7.8% (-27.1 to +11.5) | -2.1% (-33.1 to +28.9) | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.119 | +1.6% (-6.8 to +9.9) | -7.9% (-37.8 to +21.9) | +1.3% (-0.6 to +3.3) | **the runs disagree** |
| host CPU-seconds | 207.9 | 211.3 | +1.7% (-6.4 to +9.7) | -7.9% (-38.0 to +22.2) | +1.5% (-0.5 to +3.5) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.155 | 0.157 | +1.7% (-5.3 to +8.8) | -8.1% (-38.4 to +22.2) | +1.5% (-0.2 to +3.2) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 | +6.67 (+0.929 to +12.4) | +8.33 (+2.08 to +14.6) | +11.3 (+4.16 to +18.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 512 (4 trials, 1 allowed, 2 refused); acting: 384 to 640 (5 trials, 2 allowed, 1 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused); run B: acting: 384 to 512 (5 trials, 1 allowed, 1 refused); acting: 512 to 640 (5 trials, 1 allowed, 3 refused); acting: 384 to 640 (7 trials, 2 allowed, 3 refused); run C: acting: 384 to 768 (8 trials, 3 allowed, 2 refused); acting: 384 to 896 (7 trials, 4 allowed, 2 refused); acting: 384 to 640 (5 trials, 2 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.6 | 294.7 | -0.3% (-0.6 to +0.0) | -0.6% (-6.9 to +5.6) | -0.0% (-1.4 to +1.4) | STEADY, under the floor (the three runs' mean 0.32%) |
| throughput (transactions a second) | 296.5 | 295.6 | -0.3% (-1.5 to +1.0) | -0.4% (-2.4 to +1.6) | -0.1% (-1.5 to +1.3) | STEADY, under the floor (the three runs' mean 0.26%) |
| queries a second | 4,743 | 4,729 | -0.3% (-1.5 to +1.0) | -0.4% (-2.4 to +1.6) | -0.1% (-1.5 to +1.3) | STEADY, under the floor (the three runs' mean 0.26%) |
| latency, 95th percentile (ms) | 3.01 | 3.01 | -0.0% (-29.1 to +29.1) | +0.6% (-41.7 to +42.9) | -3.0% (-5.5 to -0.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 4.75 | 4.78 | +0.7% (-41.1 to +42.5) | -7.5% (-193.9 to +178.9) | -1.2% (-3.8 to +1.4) | **the runs disagree** |
| latency, mean (ms) | 1.43 | 1.45 | +1.2% (-20.3 to +22.7) | -5.2% (-60.1 to +49.7) | -1.5% (-2.7 to -0.2) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 469.2 | -8.4% (-40.4 to +23.7) | -2.1% (-9.4 to +5.2) | -0.1% (-17.1 to +16.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 451.3 | 411.5 | -8.8% (-39.5 to +21.8) | +0.5% (-5.9 to +6.9) | -2.5% (-29.7 to +24.8) | **the runs disagree** |
| pages read from disk into the pool (misses) | 249,109 | 260,706 | +4.7% (-35.9 to +45.2) | -7.9% (-9.7 to -6.1) | -1.2% (-21.5 to +19.0) | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.104 | +2.7% (-2.7 to +8.2) | -0.7% (-5.0 to +3.5) | -0.9% (-3.1 to +1.3) | **the runs disagree** |
| host CPU-seconds | 60.9 | 62.5 | +2.7% (-2.8 to +8.2) | -0.9% (-5.0 to +3.2) | -0.8% (-3.3 to +1.6) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.39 | +3.0% (-2.3 to +8.4) | -0.2% (-5.3 to +5.0) | -0.8% (-3.2 to +1.7) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 | +6.33 (+1.16 to +11.5) | +8.33 (+6.9 to +9.77) | +7 (+0.427 to +13.6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 512 (3 trials, 1 allowed, 1 refused); acting: 512 to 640 (4 trials, 1 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 1 refused); run B: acting: 512 to 640 (4 trials, 1 allowed, 0 refused); acting: 384 to 512 (6 trials, 1 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); run C: left native (6 trials, 0 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); acting: 512 to 640 (7 trials, 1 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296.0 | 296.3 | +0.1% (-0.8 to +1.0) | +0.2% (-0.4 to +0.7) | -0.0% (-1.4 to +1.4) | STEADY, under the floor (the three runs' mean 0.07%) |
| throughput (transactions a second) | 296.1 | 296.4 | +0.1% (-0.8 to +1.0) | +0.2% (-0.5 to +0.8) | -0.0% (-1.4 to +1.3) | STEADY, under the floor (the three runs' mean 0.08%) |
| queries a second | 4,738 | 4,742 | +0.1% (-0.8 to +1.0) | +0.2% (-0.5 to +0.8) | -0.0% (-1.4 to +1.3) | STEADY, under the floor (the three runs' mean 0.08%) |
| latency, 95th percentile (ms) | 1.87 | 1.81 | -3.2% (-26.0 to +19.7) | -1.8% (-1.8 to -1.8) | -1.2% (-3.7 to +1.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 3.47 | 3.26 | -6.0% (-24.8 to +12.8) | -1.2% (-3.8 to +1.4) | -2.4% (-4.9 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 1.3 | 1.27 | -2.3% (-21.4 to +16.8) | -0.8% (-2.0 to +0.3) | -0.6% (-1.3 to -0.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 480.8 | -6.1% (-31.5 to +19.3) | +10.4% (-9.7 to +30.5) | +16.7% (-8.3 to +41.6) | **the runs disagree** |
| pages holding data, mean (MB) | 461.6 | 435.2 | -5.7% (-27.8 to +16.3) | +5.8% (-19.6 to +31.1) | +11.5% (-5.4 to +28.4) | **the runs disagree** |
| pages read from disk into the pool (misses) | 654,128 | 740,498 | +13.2% (-42.0 to +68.4) | -13.8% (-58.3 to +30.7) | -22.4% (-43.7 to -1.1) | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.102 | -1.8% (-22.3 to +18.7) | -0.6% (-2.9 to +1.7) | -0.8% (-1.6 to -0.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 186.1 | 182.7 | -1.8% (-22.1 to +18.6) | -0.6% (-3.0 to +1.8) | -0.8% (-1.5 to -0.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 1.38 | 1.35 | -1.9% (-21.3 to +17.5) | -0.7% (-2.7 to +1.3) | -0.8% (-1.6 to -0.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 13.0 | +13 (+6.43 to +19.6) | +16 (+11 to +21) | +16 (+4.62 to +27.4) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 640 (7 trials, 2 allowed, 3 refused); acting: 512 to 640 (5 trials, 1 allowed, 3 refused); acting: 256 to 512 (7 trials, 2 allowed, 4 refused); run B: left native (12 trials, 0 allowed, 4 refused); acting: 512 to 640 (13 trials, 1 allowed, 3 refused); acting: 384 to 896 (11 trials, 4 allowed, 2 refused); run C: acting: 512 to 768 (9 trials, 2 allowed, 3 refused); acting: 512 to 640 (13 trials, 1 allowed, 3 refused); acting: 512 to 1024 (13 trials, 4 allowed, 2 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.0 | 192.1 | +0.6% (-0.4 to +1.6) | +0.2% (-0.4 to +0.8) | -0.2% (-0.9 to +0.6) | STEADY, under the floor (the three runs' mean 0.21%) |
| throughput (transactions a second) | 196.5 | 196.6 | +0.0% (-0.3 to +0.3) | +0.1% (-0.9 to +1.1) | +0.2% (-1.1 to +1.5) | STEADY, under the floor (the three runs' mean 0.11%) |
| queries a second | 3,930 | 3,932 | +0.0% (-0.3 to +0.3) | +0.1% (-0.9 to +1.1) | +0.2% (-1.1 to +1.5) | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms) | 9.17 | 8.63 | -5.8% (-16.8 to +5.1) | -2.9% (-14.0 to +8.1) | +8.1% (-9.7 to +26.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 13.4 | 12.8 | -4.1% (-10.9 to +2.7) | -2.4% (-15.1 to +10.4) | -5.7% (-59.5 to +48.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 5.45 | 5.38 | -1.4% (-2.6 to -0.1) | -0.7% (-2.7 to +1.3) | -13.1% (-73.2 to +47.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 598.3 | +16.8% (+2.5 to +31.2) | +19.7% (-12.1 to +51.5) | +2.5% (-26.0 to +31.1) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 461.8 | 533.5 | +15.5% (+10.8 to +20.2) | +13.4% (-4.5 to +31.4) | +2.3% (-22.8 to +27.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 616,088 | 463,656 | -24.7% (-30.8 to -18.7) | -21.0% (-38.9 to -3.2) | -2.2% (-49.9 to +45.4) | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.207 | -2.5% (-5.9 to +0.8) | -1.2% (-2.9 to +0.5) | -0.5% (-9.6 to +8.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 341.8 | 333.5 | -2.4% (-5.7 to +0.8) | -1.2% (-2.9 to +0.6) | -0.5% (-9.5 to +8.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 3.91 | 3.79 | -3.0% (-5.3 to -0.7) | -1.4% (-2.5 to -0.2) | -0.3% (-8.8 to +8.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 | +17.7 (+13.9 to +21.5) | +20.7 (+6.54 to +34.8) | +12.3 (+6.08 to +18.6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 896 (13 trials, 3 allowed, 3 refused); acting: 512 to 640 (13 trials, 1 allowed, 3 refused); acting: 512 to 640 (13 trials, 1 allowed, 3 refused); run B: acting: 384 to 640 (11 trials, 2 allowed, 3 refused); acting: 512 to 896 (13 trials, 3 allowed, 2 refused); acting: 512 to 896 (14 trials, 3 allowed, 4 refused); run C: acting: 384 to 768 (9 trials, 3 allowed, 3 refused); acting: 512 to 640 (7 trials, 1 allowed, 4 refused); acting: 384 to 640 (6 trials, 2 allowed, 2 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.5 | 3.21 | -8.3% (-133.0 to +116.3) | +10.0% (-145.1 to +165.1) | -25.0% (-412.9 to +362.8) | **the runs disagree** |
| throughput (transactions a second) | 984.3 | 982.9 | -0.1% (-0.2 to -0.1) | -0.1% (-1.0 to +0.8) | -0.1% (-0.8 to +0.7) | STEADY, under the floor (the three runs' mean 0.10%) |
| queries a second | 984.3 | 982.9 | -0.1% (-0.2 to -0.1) | -0.1% (-1.0 to +0.8) | -0.1% (-0.8 to +0.7) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, 95th percentile (ms) | 1.9 | 1.85 | -2.6% (-26.8 to +21.7) | -3.6% (-11.9 to +4.6) | -8.1% (-54.1 to +37.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 4.3 | 3.73 | -13.2% (-80.3 to +53.9) | -6.1% (-37.7 to +25.6) | -32.8% (-210.0 to +144.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 1.45 | 1.17 | -19.4% (-109.0 to +70.3) | -3.7% (-75.7 to +68.4) | +2.1% (-24.0 to +28.3) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 574.7 | +12.3% (-15.7 to +40.2) | -3.3% (-32.8 to +26.2) | +8.5% (-17.9 to +35.0) | **the runs disagree** |
| pages holding data, mean (MB) | 453.8 | 484.6 | +6.8% (-3.1 to +16.7) | -4.8% (-35.4 to +25.9) | +4.7% (-14.6 to +24.0) | **the runs disagree** |
| pages read from disk into the pool (misses) | 189,348 | 174,146 | -8.0% (-22.5 to +6.5) | +7.9% (-24.5 to +40.3) | -5.7% (-22.1 to +10.7) | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.124 | -1.2% (-13.6 to +11.1) | -3.0% (-11.0 to +5.0) | -1.1% (-6.8 to +4.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 192.9 | 190.7 | -1.2% (-13.3 to +11.0) | -3.0% (-11.1 to +5.2) | -1.2% (-7.7 to +5.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 124.2 | 155.8 | +25.4% (-176.1 to +227.0) | -6.7% (-187.6 to +174.1) | +22.1% (-197.8 to +242.0) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 | +18.3 (-0.964 to +37.6) | +15.3 (+10.2 to +20.5) | +16.3 (-2.31 to +35) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 896 (19 trials, 3 allowed, 2 refused); acting: 512 to 640 (15 trials, 1 allowed, 2 refused); acting: 384 to 768 (15 trials, 3 allowed, 2 refused); run B: acting: 384 to 512 (7 trials, 1 allowed, 6 refused); acting: 384 to 640 (8 trials, 2 allowed, 3 refused); acting: 512 to 768 (10 trials, 2 allowed, 4 refused); run C: left native (16 trials, 0 allowed, 3 refused); left native (14 trials, 0 allowed, 3 refused); acting: 512 to 768 (19 trials, 2 allowed, 2 refused).

**Across 4 untouched workloads: 16 gauge-rows GAIN, 0 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 STEADY, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
