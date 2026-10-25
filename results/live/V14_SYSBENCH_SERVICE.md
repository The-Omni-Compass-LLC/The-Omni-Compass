# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39623235693 | `e32bbb605501` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |
| B | 39625624640 | `e32bbb605501` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |
| C | 39630651710 | `67b7cd6bf1e8` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,944 | -0.2% (-0.6 to +0.3) | -0.0% (-0.1 to +0.0) | -0.2% (-0.4 to +0.0) | STEADY, under the floor (the three runs' mean 0.13%) |
| throughput (transactions a second) | 2,955 | 2,953 | -0.1% (-0.4 to +0.2) | -0.0% (-0.1 to +0.0) | -0.1% (-0.2 to -0.0) | STEADY, under the floor (the three runs' mean 0.07%) |
| queries a second | 2,955 | 2,953 | -0.1% (-0.4 to +0.2) | -0.0% (-0.1 to +0.0) | -0.1% (-0.2 to -0.0) | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 0.34 | 0.332 | -2.4% (-19.2 to +14.3) | -5.2% (-13.4 to +3.1) | -1.2% (-7.9 to +5.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.465 | 0.473 | +1.8% (-17.6 to +21.2) | -4.1% (-10.4 to +2.2) | +1.2% (-4.0 to +6.4) | **the runs disagree** |
| latency, mean (ms) | 0.2 | 0.214 | +7.3% (-4.5 to +19.2) | +1.0% (-8.1 to +10.0) | +5.3% (-71.0 to +81.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 673.6 | +31.6% (+20.8 to +42.3) | -6.3% (-35.2 to +22.5) | +1.7% (-10.2 to +13.7) | **the runs disagree** |
| pages holding data, mean (MB) | 463.5 | 559.6 | +20.7% (+8.4 to +33.0) | -5.5% (-37.6 to +26.5) | +1.9% (-13.3 to +17.1) | **the runs disagree** |
| pages read from disk into the pool (misses) | 368,666 | 246,841 | -33.0% (-39.9 to -26.2) | +5.3% (-42.2 to +52.8) | -5.6% (-24.8 to +13.5) | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.164 | +1.3% (-10.5 to +13.2) | +0.3% (-1.6 to +2.2) | +2.1% (-7.2 to +11.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 284.3 | 288.1 | +1.3% (-10.4 to +13.1) | +0.3% (-1.6 to +2.1) | +2.0% (-7.4 to +11.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.211 | 0.214 | +1.5% (-10.7 to +13.6) | +0.3% (-1.5 to +2.2) | +2.2% (-7.2 to +11.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 18.0 | +18 (+4.85 to +31.1) | +8.33 (+3.16 to +13.5) | +8 (+5.52 to +10.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 1024 (11 trials, 5 allowed, 4 refused); acting: 384 to 1152 (11 trials, 6 allowed, 1 refused); acting: 384 to 1152 (10 trials, 6 allowed, 1 refused); run B: acting: 384 to 512 (5 trials, 1 allowed, 1 refused); acting: 384 to 768 (6 trials, 3 allowed, 1 refused); acting: 384 to 512 (4 trials, 1 allowed, 2 refused); run C: acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 768 (5 trials, 3 allowed, 2 refused); acting: 384 to 768 (5 trials, 3 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.0 | 292.2 | -0.3% (-2.9 to +2.3) | +0.6% (-1.4 to +2.7) | -0.4% (-1.3 to +0.6) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (transactions a second) | 294.4 | 293.9 | -0.2% (-1.5 to +1.1) | +0.1% (-2.7 to +2.9) | -0.3% (-1.4 to +0.8) | STEADY, under the floor (the three runs' mean 0.13%) |
| queries a second | 4,711 | 4,702 | -0.2% (-1.5 to +1.1) | +0.1% (-2.7 to +2.9) | -0.3% (-1.4 to +0.8) | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, 95th percentile (ms) | 5.25 | 5.31 | +1.1% (-25.1 to +27.3) | -12.4% (-83.9 to +59.1) | -0.0% (-4.5 to +4.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 7.45 | 7.58 | +1.8% (-37.5 to +41.1) | +7.7% (-46.3 to +61.6) | +1.8% (-2.7 to +6.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.31 | 3.31 | +0.1% (-5.5 to +5.7) | +4.9% (-37.1 to +47.0) | -0.6% (-3.6 to +2.4) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 520.1 | +1.6% (-18.9 to +22.1) | -11.1% (-26.1 to +3.9) | -0.5% (-5.9 to +4.8) | **the runs disagree** |
| pages holding data, mean (MB) | 449.1 | 459.3 | +2.3% (-22.4 to +27.0) | -9.1% (-27.5 to +9.4) | -8.8% (-29.4 to +11.8) | **the runs disagree** |
| pages read from disk into the pool (misses) | 245,185 | 232,589 | -5.1% (-26.1 to +15.8) | +5.3% (-12.0 to +22.7) | +0.8% (-21.2 to +22.7) | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.19 | +0.9% (-3.0 to +4.8) | +1.1% (-3.7 to +5.9) | -0.6% (-4.1 to +3.0) | **the runs disagree** |
| host CPU-seconds | 103.9 | 105.0 | +1.1% (-3.0 to +5.1) | +1.1% (-4.0 to +6.2) | -0.5% (-4.1 to +3.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.35 | +1.4% (-0.7 to +3.4) | +0.5% (-5.8 to +6.8) | -0.1% (-3.4 to +3.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 | +7.33 (-1.39 to +16.1) | +6.67 (+2.87 to +10.5) | +5.33 (-0.404 to +11.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (7 trials, 1 allowed, 0 refused); acting: 384 to 640 (5 trials, 2 allowed, 1 refused); acting: 512 to 640 (7 trials, 1 allowed, 0 refused); run B: acting: 384 to 512 (5 trials, 1 allowed, 1 refused); acting: 384 to 512 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); run C: left native (4 trials, 0 allowed, 1 refused); acting: 512 to 640 (4 trials, 1 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.0 | 294.5 | +0.2% (-0.3 to +0.7) | +0.0% (-0.4 to +0.4) | +0.0% (-1.0 to +1.0) | STEADY, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 294.5 | 295.1 | +0.2% (-0.3 to +0.7) | +0.0% (-0.4 to +0.4) | -0.1% (-0.7 to +0.5) | STEADY, under the floor (the three runs' mean 0.05%) |
| queries a second | 4,712 | 4,722 | +0.2% (-0.3 to +0.7) | +0.0% (-0.4 to +0.4) | -0.1% (-0.7 to +0.5) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 4.1 | 3.98 | -3.0% (-9.8 to +3.9) | +0.0% (+0.0 to +0.0) | -1.2% (-3.8 to +1.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 6.06 | 5.99 | -1.2% (-3.8 to +1.4) | +0.0% (-4.5 to +4.5) | -11.9% (-70.9 to +47.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.02 | 2.97 | -1.6% (-7.3 to +4.0) | +1.1% (-1.2 to +3.4) | -10.6% (-31.6 to +10.4) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 580.5 | +13.4% (-9.3 to +36.1) | -1.3% (-20.3 to +17.7) | +5.1% (-6.5 to +16.7) | **the runs disagree** |
| pages holding data, mean (MB) | 461.5 | 507.4 | +9.9% (-5.5 to +25.4) | -3.8% (-33.8 to +26.2) | +3.9% (-5.5 to +13.3) | **the runs disagree** |
| pages read from disk into the pool (misses) | 653,819 | 516,552 | -21.0% (-50.6 to +8.6) | +4.4% (-50.9 to +59.7) | -9.6% (-22.9 to +3.7) | shown, not judged |
| host CPU busy (share of the run) | 0.236 | 0.232 | -1.5% (-6.5 to +3.5) | +1.3% (-1.2 to +3.8) | +0.3% (-3.5 to +4.2) | **the runs disagree** |
| host CPU-seconds | 419.5 | 413.1 | -1.5% (-6.5 to +3.4) | +1.3% (-1.2 to +3.8) | +0.3% (-3.6 to +4.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 3.12 | 3.07 | -1.7% (-6.7 to +3.4) | +1.3% (-0.8 to +3.4) | +0.3% (-2.6 to +3.2) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 | +16.3 (+12.5 to +20.1) | +15.3 (+12.5 to +18.2) | +14 (+14 to +14) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (13 trials, 1 allowed, 4 refused); acting: 512 to 1024 (12 trials, 4 allowed, 2 refused); acting: 512 to 640 (9 trials, 1 allowed, 4 refused); run B: acting: 384 to 640 (9 trials, 2 allowed, 3 refused); acting: 512 to 768 (12 trials, 2 allowed, 2 refused); acting: 512 to 640 (12 trials, 1 allowed, 2 refused); run C: acting: 384 to 640 (7 trials, 2 allowed, 4 refused); left native (9 trials, 0 allowed, 4 refused); acting: 512 to 768 (9 trials, 2 allowed, 4 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190.6 | 192.6 | +1.0% (+0.4 to +1.6) | +0.3% (-1.6 to +2.2) | +0.2% (-0.8 to +1.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (transactions a second) | 196.0 | 197.1 | +0.6% (-0.5 to +1.6) | +0.0% (-1.3 to +1.3) | -0.0% (-1.1 to +1.1) | STEADY, under the floor (the three runs' mean 0.19%) |
| queries a second | 3,920 | 3,942 | +0.6% (-0.5 to +1.6) | +0.0% (-1.3 to +1.3) | -0.0% (-1.1 to +1.1) | STEADY, under the floor (the three runs' mean 0.19%) |
| latency, 95th percentile (ms) | 9.01 | 8.58 | -4.7% (-11.5 to +2.1) | -4.9% (-22.6 to +12.8) | +0.1% (-11.9 to +12.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 13.6 | 12.9 | -5.3% (-18.6 to +7.9) | -6.1% (-22.7 to +10.5) | -7.8% (-36.1 to +20.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 5.44 | 5.33 | -1.9% (-11.5 to +7.8) | -2.7% (-19.5 to +14.0) | +0.5% (-8.0 to +9.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 611.9 | +19.5% (+3.7 to +35.3) | +20.4% (-1.7 to +42.5) | +2.2% (-13.2 to +17.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 461.2 | 535.5 | +16.1% (+9.7 to +22.5) | +17.6% (+3.5 to +31.8) | +2.5% (-11.1 to +16.1) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read from disk into the pool (misses) | 616,755 | 471,366 | -23.6% (-39.5 to -7.7) | -27.0% (-56.0 to +2.1) | -4.9% (-31.5 to +21.6) | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.279 | -0.4% (-1.3 to +0.6) | -2.2% (-16.9 to +12.5) | -0.9% (-7.0 to +5.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 493.2 | 491.4 | -0.4% (-1.3 to +0.6) | -2.3% (-16.1 to +11.5) | -1.0% (-7.1 to +5.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 5.65 | 5.57 | -1.4% (-2.0 to -0.7) | -2.6% (-17.9 to +12.8) | -1.1% (-7.4 to +5.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 | +17.7 (+10.5 to +24.8) | +18 (+8.06 to +27.9) | +14.7 (+9.5 to +19.8) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 896 (13 trials, 3 allowed, 2 refused); acting: 512 to 640 (9 trials, 1 allowed, 4 refused); acting: 512 to 768 (14 trials, 2 allowed, 3 refused); run B: acting: 512 to 896 (14 trials, 3 allowed, 3 refused); acting: 512 to 640 (13 trials, 1 allowed, 4 refused); acting: 512 to 640 (7 trials, 1 allowed, 4 refused); run C: acting: 384 to 640 (7 trials, 2 allowed, 3 refused); acting: 384 to 640 (8 trials, 2 allowed, 3 refused); acting: 384 to 896 (11 trials, 4 allowed, 2 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 22.2 | 23.5 | +6.0% (-103.5 to +115.5) | +4.7% (-27.9 to +37.3) | +7.6% (+1.9 to +13.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (transactions a second) | 984.1 | 983.5 | -0.1% (-0.5 to +0.4) | -0.1% (-0.6 to +0.5) | -0.1% (-1.2 to +1.1) | STEADY, under the floor (the three runs' mean 0.06%) |
| queries a second | 984.1 | 983.5 | -0.1% (-0.5 to +0.4) | -0.1% (-0.6 to +0.5) | -0.1% (-1.2 to +1.1) | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms) | 1.57 | 1.61 | +2.3% (-38.9 to +43.4) | -0.8% (-16.7 to +15.2) | -0.7% (-15.0 to +13.6) | **the runs disagree** |
| latency, 99th percentile (ms) | 2.47 | 2.67 | +8.1% (-38.1 to +54.2) | -5.3% (-36.2 to +25.7) | -0.8% (-10.6 to +9.1) | **the runs disagree** |
| latency, mean (ms) | 0.982 | 1 | +2.3% (-15.7 to +20.3) | -19.8% (-106.9 to +67.4) | -9.4% (-42.9 to +24.1) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 559.8 | +9.3% (-20.9 to +39.6) | -8.4% (-21.2 to +4.4) | +2.6% (-3.3 to +8.6) | **the runs disagree** |
| pages holding data, mean (MB) | 452.7 | 469.6 | +3.7% (-21.9 to +29.3) | -16.7% (-36.2 to +2.8) | -6.3% (-17.1 to +4.6) | **the runs disagree** |
| pages read from disk into the pool (misses) | 189,883 | 184,595 | -2.8% (-44.0 to +38.4) | +32.3% (+1.5 to +63.1) | +11.9% (-19.2 to +43.0) | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.242 | +6.4% (-41.0 to +53.8) | -1.2% (-13.1 to +10.8) | +1.1% (-16.9 to +19.0) | **the runs disagree** |
| host CPU-seconds | 398.5 | 423.6 | +6.3% (-40.5 to +53.1) | -1.2% (-12.9 to +10.5) | +1.0% (-16.2 to +18.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 41.9 | 62.2 | +48.3% (-206.0 to +302.6) | -8.7% (-62.5 to +45.1) | -6.3% (-23.8 to +11.2) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 | +19.7 (+13.9 to +25.4) | +17 (+5.62 to +28.4) | +18.7 (+9.26 to +28.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 768 (20 trials, 2 allowed, 1 refused); acting: 384 to 768 (11 trials, 3 allowed, 4 refused); acting: 384 to 896 (15 trials, 4 allowed, 3 refused); run B: acting: 128 to 640 (8 trials, 4 allowed, 3 refused); acting: 256 to 768 (10 trials, 4 allowed, 3 refused); acting: 256 to 640 (8 trials, 3 allowed, 3 refused); run C: acting: 512 to 768 (9 trials, 2 allowed, 4 refused); acting: 256 to 768 (10 trials, 4 allowed, 2 refused); acting: 384 to 640 (12 trials, 2 allowed, 3 refused).

**Across 4 untouched workloads: 10 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 19 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
