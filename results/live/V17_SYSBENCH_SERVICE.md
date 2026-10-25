# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40043207507 | `f22776e60a87` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| B | 40044589141 | `0d532c7a2dbd` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| C | 40045921684 | `e4a97f22dce1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,960 | -0.0% (-0.6 to +0.5) | -0.1% (-0.4 to +0.1) | +3.9% (-4.3 to +12.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 2,964 | 2,963 | -0.0% (-0.5 to +0.4) | -0.1% (-0.3 to +0.1) | -0.2% (-0.4 to +0.1) | STEADY, under the floor (the three runs' mean 0.10%) |
| queries a second | 2,964 | 2,963 | -0.0% (-0.5 to +0.4) | -0.1% (-0.3 to +0.1) | -0.2% (-0.4 to +0.1) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, 95th percentile (ms) | 0.153 | 0.161 | +5.2% (-63.5 to +73.9) | -5.4% (-10.4 to -0.4) | -99.7% (-406.4 to +207.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.327 | 0.332 | +1.6% (-15.1 to +18.4) | -4.1% (-11.1 to +3.0) | -84.3% (-192.9 to +24.2) | **the runs disagree** |
| latency, mean (ms) | 0.0898 | 0.0908 | +1.1% (-50.4 to +52.5) | +4.2% (-11.0 to +19.4) | -86.7% (-245.1 to +71.7) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 496.8 | -3.0% (-23.5 to +17.6) | -18.4% (-33.4 to -3.3) | +5.9% (-28.9 to +40.6) | **the runs disagree** |
| pages holding data, mean (MB) | 463.7 | 456.2 | -1.6% (-24.1 to +20.9) | -17.2% (-34.3 to -0.1) | +2.1% (-27.1 to +31.4) | **the runs disagree** |
| pages read from disk into the pool (misses) | 367,733 | 373,446 | +1.6% (-30.6 to +33.7) | +28.4% (+2.3 to +54.5) | -5.9% (-58.6 to +46.8) | shown, not judged |
| host CPU busy (share of the run) | 0.0696 | 0.0694 | -0.3% (-51.5 to +50.9) | +0.0% (-3.4 to +3.5) | -0.4% (-18.8 to +18.0) | STEADY, under the floor (the three runs' mean 0.22%) |
| host CPU-seconds | 124.6 | 124.3 | -0.2% (-51.0 to +50.6) | +0.0% (-3.3 to +3.3) | -0.4% (-18.4 to +17.6) | STEADY, under the floor (the three runs' mean 0.21%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.0924 | 0.0922 | -0.2% (-51.4 to +50.9) | +0.2% (-3.4 to +3.7) | -4.2% (-28.1 to +19.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 | +8.33 (+5.46 to +11.2) | +7.67 (-1.74 to +17.1) | +14.3 (+6.35 to +22.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 512 (3 trials, 1 allowed, 2 refused); acting: 384 to 640 (5 trials, 2 allowed, 2 refused); acting: 384 to 640 (5 trials, 2 allowed, 3 refused); run B: acting: 384 to 640 (3 trials, 2 allowed, 1 refused); acting: 384 to 640 (5 trials, 2 allowed, 3 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused); run C: acting: 512 to 768 (9 trials, 2 allowed, 3 refused); acting: 512 to 640 (6 trials, 1 allowed, 3 refused); acting: 384 to 640 (6 trials, 2 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.5 | 294.5 | +0.7% (-0.3 to +1.7) | +0.2% (-1.9 to +2.3) | +0.0% (-1.3 to +1.3) | STEADY, under the floor (the three runs' mean 0.30%) |
| throughput (transactions a second) | 293.4 | 295.4 | +0.7% (-0.3 to +1.7) | +0.5% (-0.5 to +1.5) | -0.1% (-1.4 to +1.1) | STEADY, under the floor (the three runs' mean 0.36%) |
| queries a second | 4,694 | 4,727 | +0.7% (-0.3 to +1.7) | +0.5% (-0.5 to +1.5) | -0.1% (-1.4 to +1.1) | STEADY, under the floor (the three runs' mean 0.36%) |
| latency, 95th percentile (ms) | 5.21 | 5.18 | -0.6% (-5.8 to +4.6) | +3.7% (-5.6 to +13.0) | -1.8% (-9.5 to +5.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 7.17 | 7.25 | +1.2% (-1.4 to +3.8) | +7.9% (-22.2 to +37.9) | -4.7% (-15.7 to +6.3) | **the runs disagree** |
| latency, mean (ms) | 3.35 | 3.34 | -0.3% (-0.9 to +0.2) | +4.5% (-10.9 to +19.9) | -0.9% (-4.9 to +3.0) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 513.9 | +0.4% (-9.9 to +10.7) | -7.5% (-33.9 to +18.9) | +3.2% (-14.0 to +20.4) | **the runs disagree** |
| pages holding data, mean (MB) | 446.9 | 420.5 | -5.9% (-23.3 to +11.5) | -9.8% (-35.1 to +15.4) | +6.4% (-7.6 to +20.4) | **the runs disagree** |
| pages read from disk into the pool (misses) | 244,473 | 242,899 | -0.6% (-20.1 to +18.8) | +6.4% (-20.9 to +33.8) | -6.9% (-28.1 to +14.4) | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.198 | +1.0% (+0.4 to +1.6) | +2.0% (-0.6 to +4.6) | -0.9% (-2.0 to +0.1) | **the runs disagree** |
| host CPU-seconds | 108.1 | 109.2 | +1.0% (+0.2 to +1.8) | +2.2% (-0.6 to +5.0) | -1.1% (-2.6 to +0.4) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.42 | +0.5% (-0.7 to +1.6) | +2.0% (-0.6 to +4.7) | -1.0% (-3.3 to +1.4) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 | +8.67 (+5.8 to +11.5) | +7 (+2.03 to +12) | +7 (+2.7 to +11.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (6 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 1 refused); acting: 512 to 640 (5 trials, 1 allowed, 0 refused); run B: left native (7 trials, 0 allowed, 1 refused); left native (7 trials, 0 allowed, 1 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused); run C: acting: 512 to 640 (5 trials, 1 allowed, 1 refused); acting: 512 to 640 (4 trials, 1 allowed, 2 refused); acting: 512 to 640 (7 trials, 1 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.4 | 295.6 | +0.1% (-0.2 to +0.3) | -0.2% (-1.0 to +0.7) | +0.2% (-0.7 to +1.1) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (transactions a second) | 295.4 | 295.8 | +0.1% (-0.1 to +0.4) | -0.1% (-1.0 to +0.7) | +0.2% (-0.8 to +1.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| queries a second | 4,727 | 4,732 | +0.1% (-0.1 to +0.4) | -0.1% (-1.0 to +0.7) | +0.2% (-0.8 to +1.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 3.91 | 3.82 | -2.4% (-5.0 to +0.2) | -1.8% (-6.2 to +2.6) | -1.8% (-10.5 to +7.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.15 | 5.09 | -1.2% (-3.8 to +1.4) | -2.4% (-7.5 to +2.7) | +0.1% (-7.8 to +8.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.07 | 3.05 | -0.5% (-1.7 to +0.8) | -0.8% (-2.7 to +1.0) | -2.9% (-8.2 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 576.5 | +12.6% (-5.9 to +31.0) | +17.0% (-9.7 to +43.8) | -14.7% (-32.0 to +2.7) | **the runs disagree** |
| pages holding data, mean (MB) | 461.9 | 500.3 | +8.3% (-6.2 to +22.8) | +12.3% (-7.0 to +31.6) | -14.3% (-29.0 to +0.4) | **the runs disagree** |
| pages read from disk into the pool (misses) | 655,960 | 541,886 | -17.4% (-54.2 to +19.4) | -24.6% (-70.1 to +20.9) | +23.0% (-16.8 to +62.7) | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.18 | -0.3% (-1.4 to +0.8) | -0.7% (-3.5 to +2.0) | -2.2% (-9.0 to +4.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 299.5 | 298.6 | -0.3% (-1.5 to +1.0) | -0.7% (-3.7 to +2.3) | -2.2% (-9.0 to +4.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.22 | 2.21 | -0.4% (-1.7 to +1.0) | -0.6% (-4.1 to +3.0) | -2.3% (-8.9 to +4.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 22.0 | +22 (+17.7 to +26.3) | +19 (+12.4 to +25.6) | +10.3 (-3.35 to +24) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 768 (11 trials, 3 allowed, 4 refused); acting: 384 to 640 (13 trials, 2 allowed, 3 refused); acting: 512 to 640 (12 trials, 1 allowed, 5 refused); run B: acting: 512 to 768 (14 trials, 2 allowed, 3 refused); acting: 384 to 768 (12 trials, 3 allowed, 4 refused); acting: 512 to 640 (14 trials, 1 allowed, 3 refused); run C: acting: 384 to 512 (8 trials, 1 allowed, 4 refused); acting: 384 to 640 (5 trials, 2 allowed, 2 refused); acting: 384 to 512 (3 trials, 1 allowed, 2 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 174.0 | 175.9 | +1.1% (-4.6 to +6.8) | +1.4% (+1.2 to +1.7) | +0.1% (-0.9 to +1.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (transactions a second) | 197.7 | 197.2 | -0.3% (-1.5 to +1.0) | +0.6% (-0.3 to +1.4) | -0.2% (-0.9 to +0.6) | STEADY, under the floor (the three runs' mean 0.05%) |
| queries a second | 3,954 | 3,943 | -0.3% (-1.5 to +1.0) | +0.6% (-0.3 to +1.4) | -0.2% (-0.9 to +0.6) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 58.9 | 43.7 | -25.7% (-147.2 to +95.7) | -6.4% (-11.1 to -1.7) | -3.0% (-8.0 to +2.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 245.6 | 152.6 | -37.8% (-176.1 to +100.5) | -9.0% (-20.7 to +2.6) | -2.4% (-9.0 to +4.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 14.3 | 10.3 | -27.8% (-149.4 to +93.7) | -7.2% (-13.0 to -1.5) | -0.8% (-8.6 to +6.9) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 549.1 | +7.2% (-29.9 to +44.4) | +20.5% (+8.0 to +33.1) | +19.4% (-4.7 to +43.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 461.9 | 489.5 | +6.0% (-25.6 to +37.6) | +16.1% (+3.6 to +28.6) | +15.5% (+2.2 to +28.9) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read from disk into the pool (misses) | 615,227 | 596,824 | -3.0% (-42.1 to +36.1) | -24.4% (-36.0 to -12.8) | -24.0% (-57.4 to +9.4) | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.181 | -0.6% (-5.8 to +4.6) | -2.7% (-5.2 to -0.3) | -3.0% (-7.2 to +1.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 322.8 | 320.8 | -0.6% (-5.7 to +4.5) | -2.7% (-5.6 to +0.1) | -3.0% (-7.5 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 4.08 | 4 | -1.8% (-13.0 to +9.4) | -4.1% (-7.0 to -1.2) | -3.1% (-7.0 to +0.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 | +13.7 (+9.87 to +17.5) | +19.3 (+14.2 to +24.5) | +17.3 (+9.74 to +24.9) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 896 (9 trials, 4 allowed, 2 refused); acting: 512 to 896 (10 trials, 3 allowed, 3 refused); acting: 256 to 512 (8 trials, 2 allowed, 3 refused); run B: acting: 512 to 640 (13 trials, 1 allowed, 4 refused); acting: 512 to 768 (13 trials, 2 allowed, 3 refused); acting: 512 to 768 (14 trials, 2 allowed, 2 refused); run C: acting: 512 to 768 (11 trials, 2 allowed, 4 refused); acting: 512 to 768 (14 trials, 2 allowed, 3 refused); acting: 512 to 640 (13 trials, 1 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 138.7 | 141.8 | +2.2% (-36.0 to +40.4) | -100.0% (-530.3 to +330.3) | +20.5% (-19.1 to +60.0) | **the runs disagree** |
| throughput (transactions a second) | 988.0 | 986.8 | -0.1% (-0.3 to +0.1) | +0.0% (-0.4 to +0.4) | -0.1% (-0.5 to +0.4) | STEADY, under the floor (the three runs' mean 0.05%) |
| queries a second | 988.0 | 986.8 | -0.1% (-0.3 to +0.1) | +0.0% (-0.4 to +0.4) | -0.1% (-0.5 to +0.4) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 86.4 | 136.1 | +57.5% (-76.6 to +191.6) | -0.7% (-15.3 to +13.9) | -3.0% (-5.9 to -0.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 212.5 | 358.4 | +68.7% (-38.4 to +175.7) | +1.4% (-35.8 to +38.5) | -6.6% (-35.3 to +22.0) | **the runs disagree** |
| latency, mean (ms) | 13.3 | 23.0 | +72.7% (-66.4 to +211.8) | -1.9% (-15.1 to +11.3) | -4.9% (-14.8 to +4.9) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 474.6 | -7.3% (-38.7 to +24.1) | +8.3% (-13.9 to +30.5) | +1.5% (+0.6 to +2.4) | **the runs disagree** |
| pages holding data, mean (MB) | 453.0 | 380.5 | -16.0% (-42.4 to +10.4) | +0.9% (-18.6 to +20.5) | -1.4% (-3.4 to +0.7) | **the runs disagree** |
| pages read from disk into the pool (misses) | 190,191 | 235,795 | +24.0% (+0.5 to +47.4) | -1.4% (-37.2 to +34.4) | +0.0% (-5.3 to +5.3) | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.136 | -2.1% (-13.3 to +9.0) | -0.5% (-9.7 to +8.7) | -4.1% (-28.2 to +20.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 245.8 | 241.0 | -1.9% (-12.8 to +9.0) | -0.5% (-9.6 to +8.6) | -4.1% (-27.4 to +19.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 3.98 | 3.8 | -4.6% (-51.4 to +42.2) | -0.5% (-9.6 to +8.6) | -29.4% (-134.9 to +76.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 17.0 | +17 (+9.55 to +24.5) | +21 (+16 to +26) | +16.3 (+8.35 to +24.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 256 to 640 (10 trials, 3 allowed, 3 refused); acting: 256 to 768 (8 trials, 4 allowed, 2 refused); acting: 384 to 640 (9 trials, 2 allowed, 4 refused); run B: acting: 512 to 768 (18 trials, 2 allowed, 2 refused); acting: 512 to 640 (11 trials, 1 allowed, 4 refused); acting: 384 to 640 (13 trials, 2 allowed, 2 refused); run C: left native (12 trials, 0 allowed, 4 refused); acting: 512 to 640 (13 trials, 1 allowed, 4 refused); acting: 512 to 640 (9 trials, 1 allowed, 4 refused).

**Across 4 untouched workloads: 16 gauge-rows GAIN, 0 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 16 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
