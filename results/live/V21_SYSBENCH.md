# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40258018856 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40281464587 | `fa6da97bbaa6` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40401032384 | `5e222aa21371` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,923 | 2,924 | +0.0% (-0.2 to +0.2) | +0.0% (-0.1 to +0.2) | +0.2% (-0.2 to +0.5) | EVEN, under the floor (the three runs' mean 0.07%) |
| throughput (transactions a second) | 2,931 | 2,932 | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | +0.1% (-0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.05%) |
| queries a second | 2,931 | 2,932 | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | +0.1% (-0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.228 | 0.222 | -2.5% (-11.8 to +6.8) | -19.9% (-50.8 to +11.0) | -2.4% (-4.9 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.482 | 0.476 | -1.2% (-6.6 to +4.1) | -9.8% (-25.2 to +5.7) | -2.9% (-9.5 to +3.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.185 | 0.175 | -5.5% (-126.1 to +115.0) | -6.1% (-33.7 to +21.6) | -3.1% (-49.8 to +43.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 519.5 | +1.5% (-24.1 to +27.0) | -12.1% (-46.8 to +22.6) | +11.1% (-12.4 to +34.5) | **the runs disagree** |
| pages holding data, mean (MB) | 463.1 | 465.0 | +0.4% (-23.9 to +24.7) | -11.3% (-50.2 to +27.6) | +10.9% (-3.7 to +25.5) | **the runs disagree** |
| pages read from disk into the pool (misses) | 367,533 | 349,101 | -5.0% (-41.7 to +31.7) | +19.1% (-43.5 to +81.6) | -19.2% (-46.5 to +8.1) | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.116 | -0.5% (-12.0 to +11.0) | -5.5% (-38.9 to +28.0) | -2.5% (-5.0 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 211.1 | 210.2 | -0.4% (-11.7 to +10.9) | -5.4% (-38.7 to +27.8) | -2.5% (-5.2 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.156 | -0.4% (-11.7 to +10.8) | -5.4% (-38.5 to +27.6) | -2.6% (-5.6 to +0.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 | +11.3 (-2.35 to +25) | +8.67 (-0.058 to +17.4) | +10 (+3.43 to +16.6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (5 trials, 1 allowed, 0 refused); acting: 384 to 512 (7 trials, 1 allowed, 1 refused); acting: 384 to 640 (10 trials, 2 allowed, 2 refused); run B: acting: 256 to 512 (4 trials, 2 allowed, 0 refused); acting: 256 to 512 (5 trials, 2 allowed, 2 refused); acting: 256 to 640 (7 trials, 3 allowed, 2 refused); run C: acting: 512 to 640 (8 trials, 1 allowed, 2 refused); acting: 384 to 640 (8 trials, 2 allowed, 0 refused); acting: 512 to 640 (6 trials, 1 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.9 | 293.0 | -0.3% (-1.4 to +0.8) | +0.5% (-1.5 to +2.5) | -0.7% (-3.2 to +1.9) | EVEN, under the floor (the three runs' mean 0.16%) |
| throughput (transactions a second) | 296.3 | 294.8 | -0.5% (-1.7 to +0.7) | +0.5% (-1.5 to +2.4) | -0.8% (-3.4 to +1.8) | EVEN, under the floor (the three runs' mean 0.27%) |
| queries a second | 4,740 | 4,716 | -0.5% (-1.7 to +0.7) | +0.5% (-1.5 to +2.4) | -0.8% (-3.4 to +1.8) | EVEN, under the floor (the three runs' mean 0.27%) |
| latency, 95th percentile (ms) | 5.6 | 5.5 | -1.8% (-9.6 to +6.0) | -3.5% (-11.1 to +4.0) | -2.4% (-12.9 to +8.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 8.18 | 7.84 | -4.1% (-9.1 to +0.9) | -4.1% (-10.8 to +2.6) | -2.4% (-4.8 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.33 | 3.32 | -0.4% (-1.6 to +0.8) | -0.2% (-3.1 to +2.8) | +0.9% (-6.8 to +8.5) | EVEN, under the floor (the three runs' mean 0.11%) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 436.5 | -14.8% (-15.1 to -14.4) | -16.8% (-22.9 to -10.6) | -4.0% (-4.4 to -3.7) | **GAIN in all three of our runs** |
| pages holding data, mean (MB) | 444.5 | 392.0 | -11.8% (-12.7 to -10.9) | -14.1% (-21.6 to -6.6) | -1.7% (-3.4 to +0.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read from disk into the pool (misses) | 245,210 | 258,690 | +5.5% (+0.0 to +11.0) | +6.9% (+1.9 to +11.9) | +1.8% (-1.2 to +4.9) | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.189 | -0.2% (-4.6 to +4.2) | +1.2% (-1.7 to +4.2) | +2.6% (-8.2 to +13.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 104.3 | 104.3 | -0.0% (-4.7 to +4.6) | +1.3% (-1.7 to +4.2) | +3.0% (-8.2 to +14.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.33 | +0.3% (-5.0 to +5.5) | +0.8% (-1.5 to +3.0) | +3.7% (-6.2 to +13.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 7 | +7 (+7 to +7) | +6 (+3.52 to +8.48) | +5 (+5 to +5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 640 (4 trials, 2 allowed, 1 refused); run B: acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused); acting: 256 to 640 (4 trials, 3 allowed, 0 refused); run C: acting: 384 to 640 (3 trials, 2 allowed, 0 refused); acting: 384 to 640 (3 trials, 2 allowed, 0 refused); acting: 384 to 640 (3 trials, 2 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.3 | 295.5 | +0.4% (-0.7 to +1.6) | -0.0% (-1.6 to +1.6) | -0.3% (-1.1 to +0.6) | EVEN, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 294.7 | 295.9 | +0.4% (-0.7 to +1.5) | +0.0% (-1.6 to +1.6) | -0.2% (-1.1 to +0.6) | EVEN, under the floor (the three runs' mean 0.06%) |
| queries a second | 4,715 | 4,734 | +0.4% (-0.7 to +1.5) | +0.0% (-1.6 to +1.6) | -0.2% (-1.1 to +0.6) | EVEN, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms) | 4.23 | 4.15 | -1.8% (-6.2 to +2.6) | +0.6% (-2.0 to +3.2) | +0.0% (-4.5 to +4.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 6.17 | 6.02 | -2.4% (-9.0 to +4.3) | -0.6% (-3.1 to +1.9) | -1.2% (-8.0 to +5.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.2 | 3.2 | -0.1% (-1.4 to +1.1) | +0.4% (-0.6 to +1.4) | +0.8% (-0.6 to +2.1) | EVEN, under the floor (the three runs' mean 0.36%) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 461.0 | -10.0% (-27.5 to +7.6) | -22.2% (-32.0 to -12.3) | -20.4% (-46.8 to +6.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 461.7 | 425.5 | -7.8% (-25.9 to +10.2) | -21.4% (-34.3 to -8.5) | -20.1% (-48.7 to +8.6) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 653,617 | 774,070 | +18.4% (-21.9 to +58.8) | +42.6% (+28.1 to +57.2) | +35.0% (-20.4 to +90.4) | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.192 | +1.5% (-0.1 to +3.0) | +2.0% (-0.2 to +4.3) | +0.5% (-0.1 to +1.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 312.6 | 317.8 | +1.7% (-0.1 to +3.4) | +2.4% (+0.0 to +4.7) | +0.5% (-0.0 to +1.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.35 | +1.2% (-1.2 to +3.6) | +2.4% (+0.5 to +4.2) | +0.8% (+0.5 to +1.0) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 | +12.3 (+9.46 to +15.2) | +9.67 (+6.8 to +12.5) | +5.33 (+3.9 to +6.77) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 640 (7 trials, 3 allowed, 1 refused); acting: 256 to 640 (7 trials, 3 allowed, 1 refused); acting: 256 to 512 (6 trials, 2 allowed, 1 refused); run B: acting: 256 to 512 (6 trials, 2 allowed, 1 refused); acting: 256 to 512 (6 trials, 2 allowed, 1 refused); acting: 256 to 512 (6 trials, 2 allowed, 1 refused); run C: acting: 256 to 512 (4 trials, 2 allowed, 0 refused); acting: 384 to 512 (4 trials, 1 allowed, 1 refused); acting: 256 to 512 (4 trials, 2 allowed, 0 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192.5 | 192.3 | -0.1% (-0.9 to +0.7) | +0.6% (-1.6 to +2.7) | +0.4% (-1.1 to +1.9) | EVEN, under the floor (the three runs' mean 0.30%) |
| throughput (transactions a second) | 196.7 | 196.2 | -0.2% (-1.1 to +0.6) | +0.6% (-1.3 to +2.4) | +0.3% (-0.8 to +1.5) | EVEN, under the floor (the three runs' mean 0.23%) |
| queries a second | 3,934 | 3,924 | -0.2% (-1.1 to +0.6) | +0.6% (-1.3 to +2.4) | +0.3% (-0.8 to +1.5) | EVEN, under the floor (the three runs' mean 0.23%) |
| latency, 95th percentile (ms) | 8.48 | 8.28 | -2.4% (-7.5 to +2.7) | -1.9% (-9.5 to +5.8) | +1.8% (-13.8 to +17.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 12.3 | 12.2 | -0.6% (-3.2 to +2.0) | -1.4% (-26.6 to +23.8) | -1.2% (-28.5 to +26.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 5.29 | 5.25 | -0.7% (-3.1 to +1.7) | +0.7% (-6.3 to +7.6) | -0.9% (-23.9 to +22.1) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 546.3 | +6.7% (-15.4 to +28.8) | +6.6% (-10.0 to +23.2) | -1.1% (-11.6 to +9.4) | **the runs disagree** |
| pages holding data, mean (MB) | 462.0 | 489.1 | +5.9% (-10.3 to +22.1) | +6.0% (-9.6 to +21.7) | +0.4% (-8.7 to +9.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 615,859 | 542,119 | -12.0% (-40.2 to +16.2) | -11.7% (-44.0 to +20.6) | -1.2% (-25.2 to +22.7) | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.212 | -1.1% (-5.9 to +3.8) | -2.4% (-11.7 to +6.8) | +2.7% (-11.6 to +17.0) | **the runs disagree** |
| host CPU-seconds | 344.6 | 341.5 | -0.9% (-5.9 to +4.1) | -2.4% (-11.6 to +6.7) | +2.7% (-11.5 to +16.9) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 3.91 | 3.88 | -0.9% (-6.5 to +4.8) | -3.0% (-10.0 to +4.1) | +2.3% (-12.7 to +17.3) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 | +20.7 (+17.8 to +23.5) | +15.7 (+2.92 to +28.4) | +8 (+3.03 to +13) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 640 (12 trials, 2 allowed, 3 refused); acting: 384 to 640 (11 trials, 2 allowed, 3 refused); acting: 384 to 512 (11 trials, 1 allowed, 4 refused); run B: acting: 512 to 640 (9 trials, 1 allowed, 2 refused); left native (8 trials, 0 allowed, 1 refused); acting: 384 to 640 (10 trials, 2 allowed, 2 refused); run C: acting: 384 to 640 (5 trials, 2 allowed, 2 refused); acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.09 | 3.24 | +196.6% (-172.3 to +565.4) | -1.7% (-41.9 to +38.5) | -25.9% (-167.4 to +115.5) | **the runs disagree** |
| throughput (transactions a second) | 983.1 | 983.1 | -0.0% (-0.3 to +0.3) | +0.0% (-0.3 to +0.3) | -1.2% (-6.3 to +3.8) | EVEN, under the floor (the three runs' mean 0.41%) |
| queries a second | 983.1 | 983.1 | -0.0% (-0.3 to +0.3) | +0.0% (-0.3 to +0.3) | -1.2% (-6.3 to +3.8) | EVEN, under the floor (the three runs' mean 0.41%) |
| latency, 95th percentile (ms) | 2.95 | 1.71 | -42.1% (-104.9 to +20.8) | -1.9% (-14.1 to +10.3) | +116.4% (-620.2 to +852.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 5.33 | 2.92 | -45.2% (-90.4 to +0.0) | -1.6% (-26.6 to +23.5) | +107.4% (-594.0 to +808.8) | **the runs disagree** |
| latency, mean (ms) | 1.5 | 1.07 | -28.6% (-59.3 to +2.1) | -1.1% (-10.7 to +8.4) | +115.4% (-519.3 to +750.1) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 512.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| pages holding data, mean (MB) | 455.0 | 451.2 | -0.8% (-3.1 to +1.5) | -0.6% (-3.5 to +2.2) | -0.6% (-3.7 to +2.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 188,970 | 186,964 | -1.1% (-4.9 to +2.7) | -1.3% (-6.6 to +4.0) | -2.5% (-10.0 to +4.9) | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.134 | -38.0% (-78.3 to +2.2) | -2.1% (-16.2 to +12.1) | -7.6% (-18.9 to +3.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 330.4 | 205.3 | -37.9% (-79.8 to +4.1) | -2.0% (-16.0 to +12.0) | -7.0% (-18.3 to +4.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 9,732 | 285.4 | -97.1% (-308.6 to +114.4) | -4.7% (-56.1 to +46.7) | +2.1% (-240.6 to +244.9) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

**Across 4 untouched workloads: 11 gauge-rows GAIN, 0 LOSS, 7 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 18 EVEN, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
