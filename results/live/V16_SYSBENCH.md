# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39823802516 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| B | 39842355356 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| C | 39862234914 | `15915c961cd2` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,939 | 2,937 | -0.0% (-0.3 to +0.2) | +0.0% (-0.3 to +0.4) | -0.1% (-0.7 to +0.4) | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (transactions a second) | 2,940 | 2,940 | -0.0% (-0.2 to +0.2) | +0.0% (-0.4 to +0.4) | -0.1% (-0.6 to +0.4) | STEADY, under the floor (the three runs' mean 0.04%) |
| queries a second | 2,940 | 2,940 | -0.0% (-0.2 to +0.2) | +0.0% (-0.4 to +0.4) | -0.1% (-0.6 to +0.4) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 0.267 | 0.252 | -5.9% (-15.0 to +3.3) | -0.6% (-7.7 to +6.5) | -4.2% (-13.5 to +5.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.414 | 0.407 | -1.9% (-6.4 to +2.6) | -1.2% (-12.6 to +10.3) | -1.2% (-7.8 to +5.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.17 | 0.174 | +2.0% (-0.5 to +4.5) | +2.1% (-2.4 to +6.6) | +2.3% (-0.3 to +5.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 447.1 | -12.7% (-34.4 to +9.1) | -0.4% (-3.8 to +2.9) | -9.2% (-17.4 to -1.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 463.8 | 406.5 | -12.4% (-38.9 to +14.1) | -1.4% (-3.8 to +0.9) | -9.8% (-24.2 to +4.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 366,053 | 434,236 | +18.6% (-22.8 to +60.1) | -1.4% (-9.5 to +6.6) | +15.6% (-7.6 to +38.7) | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.147 | +0.4% (-2.0 to +2.9) | +3.7% (-3.8 to +11.2) | +1.5% (+0.1 to +2.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 263.9 | 265.2 | +0.5% (-2.0 to +2.9) | +3.8% (-3.5 to +11.2) | +1.5% (+0.1 to +2.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.196 | 0.197 | +0.5% (-2.0 to +3.0) | +3.8% (-3.6 to +11.2) | +1.6% (+0.8 to +2.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 11.0 | +11 (+3.55 to +18.5) | +13 (+6.43 to +19.6) | +14 (+9.7 to +18.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (4 trials, 1 allowed, 1 refused); acting: 384 to 512 (7 trials, 1 allowed, 2 refused); acting: 256 to 512 (7 trials, 2 allowed, 3 refused); run B: acting: 384 to 512 (9 trials, 1 allowed, 4 refused); acting: 384 to 512 (10 trials, 1 allowed, 4 refused); acting: 384 to 512 (9 trials, 1 allowed, 3 refused); run C: acting: 256 to 512 (8 trials, 2 allowed, 3 refused); acting: 384 to 512 (7 trials, 1 allowed, 3 refused); acting: 384 to 512 (8 trials, 1 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.1 | 293.1 | -0.3% (-1.3 to +0.7) | -0.3% (-1.2 to +0.7) | -0.3% (-2.3 to +1.6) | STEADY, under the floor (the three runs' mean 0.30%) |
| throughput (transactions a second) | 294.7 | 293.5 | -0.4% (-1.3 to +0.5) | -0.2% (-1.2 to +0.8) | -0.4% (-2.2 to +1.4) | STEADY, under the floor (the three runs' mean 0.34%) |
| queries a second | 4,716 | 4,696 | -0.4% (-1.3 to +0.5) | -0.2% (-1.2 to +0.8) | -0.4% (-2.2 to +1.4) | STEADY, under the floor (the three runs' mean 0.34%) |
| latency, 95th percentile (ms) | 2.99 | 2.97 | -0.6% (-22.8 to +21.6) | -1.2% (-6.3 to +3.9) | +0.6% (-6.3 to +7.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 4.65 | 4.68 | +0.7% (-12.8 to +14.1) | +1.8% (-2.8 to +6.4) | -0.6% (-3.2 to +2.0) | **the runs disagree** |
| latency, mean (ms) | 1.41 | 1.4 | -0.6% (-10.9 to +9.6) | -0.0% (-1.8 to +1.7) | +0.4% (-2.3 to +3.2) | STEADY, under the floor (the three runs' mean 0.07%) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 368.6 | -28.0% (-78.3 to +22.3) | -1.4% (-8.9 to +6.1) | -10.3% (-20.5 to -0.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 446.5 | 319.6 | -28.4% (-74.9 to +18.0) | -1.8% (-27.8 to +24.1) | -14.6% (-25.5 to -3.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 245,749 | 293,337 | +19.4% (-35.3 to +74.0) | +0.2% (-14.7 to +15.0) | +6.2% (-8.6 to +20.9) | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.101 | +0.5% (-8.9 to +10.0) | +0.8% (-6.5 to +8.1) | +1.6% (+0.0 to +3.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 60.4 | 60.8 | +0.5% (-8.9 to +9.9) | +0.9% (-6.8 to +8.5) | +1.9% (+0.4 to +3.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.36 | +0.9% (-9.5 to +11.2) | +1.1% (-5.8 to +8.1) | +2.2% (+0.5 to +3.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 | +7.33 (-3.87 to +18.5) | +5 (+2.52 to +7.48) | +7.33 (+5.9 to +8.77) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (4 trials, 2 allowed, 0 refused); left native (6 trials, 0 allowed, 2 refused); acting: 256 to 512 (5 trials, 2 allowed, 1 refused); run B: left native (4 trials, 0 allowed, 2 refused); left native (5 trials, 0 allowed, 1 refused); left native (6 trials, 0 allowed, 1 refused); run C: acting: 384 to 512 (4 trials, 1 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.1 | 295.1 | +0.0% (-1.0 to +1.1) | +0.6% (+0.1 to +1.0) | -0.3% (-1.0 to +0.5) | STEADY, under the floor (the three runs' mean 0.11%) |
| throughput (transactions a second) | 295.3 | 295.2 | -0.0% (-0.9 to +0.9) | +0.6% (+0.1 to +1.1) | -0.2% (-1.0 to +0.5) | STEADY, under the floor (the three runs' mean 0.11%) |
| queries a second | 4,725 | 4,723 | -0.0% (-0.9 to +0.9) | +0.6% (+0.1 to +1.1) | -0.2% (-1.0 to +0.5) | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms) | 3.71 | 3.55 | -4.1% (-7.3 to -1.0) | -0.6% (-3.2 to +2.0) | -1.2% (-3.8 to +1.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 5.25 | 4.88 | -7.0% (-15.3 to +1.3) | -0.6% (-5.8 to +4.6) | -0.6% (-3.1 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 2.8 | 2.74 | -2.1% (-5.1 to +1.0) | +0.1% (-1.2 to +1.4) | +0.2% (-2.1 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 496.2 | -3.1% (-15.0 to +8.8) | -2.8% (-14.4 to +8.9) | -16.8% (-29.8 to -3.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 461.9 | 450.7 | -2.4% (-14.7 to +9.8) | -3.8% (-17.3 to +9.7) | -17.8% (-30.6 to -5.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 656,123 | 652,963 | -0.5% (-11.6 to +10.7) | +4.3% (-20.3 to +28.9) | +33.9% (+4.0 to +63.9) | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.215 | -1.9% (-4.2 to +0.4) | +1.5% (-0.9 to +3.9) | +0.1% (-2.7 to +2.8) | **the runs disagree** |
| host CPU-seconds | 391.7 | 384.3 | -1.9% (-4.2 to +0.4) | +1.6% (-1.0 to +4.1) | +0.1% (-2.6 to +2.8) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 2.9 | 2.85 | -1.9% (-5.2 to +1.4) | +1.0% (-2.0 to +4.0) | +0.3% (-1.7 to +2.4) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 | +16.3 (+14.9 to +17.8) | +14.7 (+8.41 to +20.9) | +17 (+12 to +22) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (11 trials, 1 allowed, 3 refused); left native (11 trials, 0 allowed, 3 refused); left native (14 trials, 0 allowed, 4 refused); run B: acting: 384 to 512 (11 trials, 1 allowed, 4 refused); left native (12 trials, 0 allowed, 3 refused); left native (11 trials, 0 allowed, 3 refused); run C: acting: 384 to 512 (10 trials, 1 allowed, 4 refused); acting: 256 to 640 (9 trials, 3 allowed, 2 refused); acting: 384 to 512 (10 trials, 1 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 157.3 | 148.3 | -5.7% (-10.5 to -0.9) | +0.0% (-1.2 to +1.3) | -0.2% (-0.6 to +0.1) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (transactions a second) | 196.8 | 197.3 | +0.2% (-1.0 to +1.5) | +0.0% (-0.3 to +0.3) | +0.1% (-0.8 to +0.9) | STEADY, under the floor (the three runs' mean 0.11%) |
| queries a second | 3,936 | 3,945 | +0.2% (-1.0 to +1.5) | +0.0% (-0.3 to +0.3) | +0.1% (-0.8 to +0.9) | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms) | 104.4 | 134.4 | +28.8% (+18.2 to +39.4) | -0.6% (-5.7 to +4.6) | +14.9% (+2.7 to +27.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 266.7 | 316.3 | +18.6% (-31.8 to +68.9) | -0.5% (-13.5 to +12.5) | +27.5% (-55.4 to +110.4) | **the runs disagree** |
| latency, mean (ms) | 20.1 | 25.8 | +28.5% (+7.8 to +49.3) | -0.1% (-4.1 to +3.8) | +6.9% (-0.4 to +14.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 513.5 | +0.3% (-25.5 to +26.1) | +5.7% (-8.4 to +19.9) | -19.1% (-58.6 to +20.5) | **the runs disagree** |
| pages holding data, mean (MB) | 461.1 | 461.3 | +0.0% (-25.1 to +25.2) | +4.0% (-9.8 to +17.9) | -20.2% (-64.3 to +23.8) | **the runs disagree** |
| pages read from disk into the pool (misses) | 616,332 | 610,100 | -1.0% (-31.4 to +29.3) | -6.7% (-37.4 to +24.0) | +39.0% (-49.7 to +127.8) | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.215 | -2.6% (-6.1 to +0.9) | -0.5% (-6.4 to +5.3) | +3.0% (-2.4 to +8.5) | **the runs disagree** |
| host CPU-seconds | 391.8 | 382.5 | -2.4% (-6.1 to +1.4) | -0.5% (-6.2 to +5.3) | +3.0% (-2.2 to +8.3) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 5.45 | 5.65 | +3.6% (-4.4 to +11.5) | -0.5% (-7.3 to +6.2) | +3.3% (-2.0 to +8.6) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 19.0 | +19 (+9.06 to +28.9) | +16.7 (+6.63 to +26.7) | +10.7 (+7.8 to +13.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (9 trials, 1 allowed, 3 refused); acting: 384 to 640 (12 trials, 2 allowed, 3 refused); acting: 384 to 512 (12 trials, 1 allowed, 4 refused); run B: acting: 512 to 640 (13 trials, 1 allowed, 3 refused); left native (12 trials, 0 allowed, 4 refused); acting: 384 to 640 (13 trials, 2 allowed, 4 refused); run C: acting: 256 to 512 (6 trials, 2 allowed, 2 refused); acting: 128 to 512 (5 trials, 3 allowed, 2 refused); acting: 256 to 512 (8 trials, 2 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 24.5 | 26.2 | +7.2% (-37.0 to +51.4) | +11.5% (-47.2 to +70.3) | -4.6% (-60.7 to +51.5) | **the runs disagree** |
| throughput (transactions a second) | 984.8 | 984.4 | -0.0% (-0.6 to +0.5) | -0.1% (-0.5 to +0.3) | +0.1% (-0.4 to +0.5) | STEADY, under the floor (the three runs' mean 0.02%) |
| queries a second | 984.8 | 984.4 | -0.0% (-0.6 to +0.5) | -0.1% (-0.5 to +0.3) | +0.1% (-0.4 to +0.5) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 1.57 | 1.54 | -2.0% (-14.3 to +10.4) | -4.1% (-33.6 to +25.3) | +1.0% (-13.8 to +15.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 2.95 | 2.99 | +1.5% (-38.3 to +41.3) | -4.9% (-36.0 to +26.2) | +5.5% (+1.4 to +9.7) | **the runs disagree** |
| latency, mean (ms) | 1.15 | 1.13 | -2.0% (-55.9 to +51.9) | -2.2% (-17.1 to +12.6) | +1.2% (-5.2 to +7.6) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 484.7 | -5.3% (-13.6 to +3.0) | -2.2% (-12.8 to +8.5) | -2.0% (-8.9 to +4.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 452.2 | 407.7 | -9.8% (-22.2 to +2.6) | -4.5% (-17.0 to +8.0) | -5.5% (-15.9 to +5.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 189,942 | 215,288 | +13.3% (-7.4 to +34.1) | +3.7% (-8.1 to +15.6) | +7.3% (-13.3 to +27.8) | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.217 | -1.8% (-15.6 to +12.0) | -2.7% (-20.6 to +15.3) | +7.3% (-43.4 to +58.1) | **the runs disagree** |
| host CPU-seconds | 387.1 | 380.2 | -1.8% (-15.6 to +12.1) | -2.6% (-20.6 to +15.4) | +7.5% (-43.3 to +58.3) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 36.4 | 32.1 | -11.7% (-72.8 to +49.5) | -17.2% (-104.5 to +70.0) | +16.7% (-4.3 to +37.7) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 21.0 | +21 (+16 to +26) | +16.3 (+9.16 to +23.5) | +18.3 (+13.2 to +23.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (14 trials, 1 allowed, 4 refused); acting: 256 to 512 (12 trials, 2 allowed, 4 refused); acting: 384 to 640 (15 trials, 2 allowed, 3 refused); run B: acting: 384 to 512 (15 trials, 1 allowed, 3 refused); acting: 384 to 512 (15 trials, 1 allowed, 3 refused); left native (17 trials, 0 allowed, 4 refused); run C: left native (15 trials, 0 allowed, 3 refused); acting: 512 to 640 (15 trials, 1 allowed, 3 refused); acting: 256 to 512 (13 trials, 2 allowed, 4 refused).

**Across 4 untouched workloads: 9 gauge-rows GAIN, 2 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 STEADY, 19 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
