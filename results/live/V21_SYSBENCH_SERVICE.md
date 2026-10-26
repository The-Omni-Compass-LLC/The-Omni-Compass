# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40286351408 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40291369516 | `f70084ae1bb3` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40293202427 | `2d426169d766` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,924 | 2,924 | -0.0% (-0.5 to +0.5) | -0.1% (-0.3 to +0.1) | +0.1% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (transactions a second) | 2,939 | 2,940 | +0.0% (-0.3 to +0.3) | -0.0% (-0.2 to +0.2) | +0.1% (-0.0 to +0.2) | EVEN, under the floor (the three runs' mean 0.04%) |
| queries a second | 2,939 | 2,940 | +0.0% (-0.3 to +0.3) | -0.0% (-0.2 to +0.2) | +0.1% (-0.0 to +0.2) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 0.32 | 0.312 | -2.5% (-5.2 to +0.2) | -0.2% (-4.6 to +4.2) | -0.6% (-3.3 to +2.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.473 | 0.467 | -1.2% (-6.4 to +4.0) | -0.6% (-3.1 to +1.9) | -1.2% (-3.7 to +1.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.185 | 0.185 | +0.2% (-3.8 to +4.3) | +67.0% (-184.8 to +318.9) | +0.9% (-1.4 to +3.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 524.2 | +2.4% (+1.2 to +3.6) | +4.3% (-62.2 to +70.7) | +10.6% (-19.4 to +40.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 463.6 | 460.5 | -0.7% (-5.5 to +4.1) | +2.6% (-55.9 to +61.0) | +5.3% (-14.8 to +25.5) | **the runs disagree** |
| pages read from disk into the pool (misses) | 366,700 | 354,019 | -3.5% (-6.7 to -0.2) | -4.4% (-106.0 to +97.3) | -11.5% (-44.3 to +21.2) | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.143 | -1.3% (-3.8 to +1.2) | +0.4% (-2.0 to +2.8) | +1.9% (-3.0 to +6.8) | **the runs disagree** |
| host CPU-seconds | 260.3 | 257.0 | -1.2% (-3.6 to +1.2) | +0.4% (-2.0 to +2.8) | +2.0% (-3.0 to +7.0) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.194 | 0.191 | -1.2% (-3.8 to +1.4) | +0.5% (-1.7 to +2.7) | +1.9% (-3.2 to +7.1) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 | +15.3 (+9.6 to +21.1) | +11.3 (-7.64 to +30.3) | +12.7 (-4.78 to +30.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (8 trials, 1 allowed, 2 refused); acting: 384 to 640 (11 trials, 2 allowed, 2 refused); acting: 512 to 640 (8 trials, 1 allowed, 2 refused); run B: acting: 384 to 640 (7 trials, 2 allowed, 4 refused); acting: 512 to 768 (10 trials, 2 allowed, 3 refused); acting: 384 to 512 (2 trials, 1 allowed, 1 refused); run C: acting: 512 to 768 (8 trials, 2 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused); acting: 512 to 896 (11 trials, 3 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 278.6 | 282.3 | +1.4% (-3.4 to +6.1) | +0.6% (-1.0 to +2.3) | +0.1% (-0.5 to +0.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 294.4 | 295.3 | +0.3% (-0.6 to +1.2) | +0.7% (-1.0 to +2.3) | +0.1% (-0.6 to +0.8) | EVEN, under the floor (the three runs' mean 0.35%) |
| queries a second | 4,710 | 4,725 | +0.3% (-0.6 to +1.2) | +0.7% (-1.0 to +2.3) | +0.1% (-0.6 to +0.8) | EVEN, under the floor (the three runs' mean 0.35%) |
| latency, 95th percentile (ms) | 14.6 | 7.57 | -48.1% (-317.1 to +220.8) | -3.5% (-8.0 to +0.9) | -1.8% (-6.2 to +2.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 114.2 | 103.6 | -9.3% (-248.1 to +229.5) | +0.6% (-4.6 to +5.8) | -2.4% (-4.9 to +0.1) | **the runs disagree** |
| latency, mean (ms) | 6.39 | 5.44 | -14.9% (-201.9 to +172.1) | +0.9% (-4.4 to +6.3) | +0.2% (-0.9 to +1.3) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 489.1 | -4.5% (-33.3 to +24.4) | -2.1% (-4.9 to +0.7) | -2.5% (-2.8 to -2.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 444.9 | 431.0 | -3.1% (-28.1 to +21.8) | -1.8% (-3.4 to -0.3) | -2.1% (-3.4 to -0.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read from disk into the pool (misses) | 245,091 | 241,710 | -1.4% (-24.6 to +21.8) | -4.8% (-8.3 to -1.2) | -5.4% (-5.6 to -5.2) | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.164 | +0.9% (-2.7 to +4.5) | +1.7% (-3.0 to +6.4) | +2.6% (-1.2 to +6.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 97.4 | 98.4 | +1.0% (-3.0 to +5.0) | +1.7% (-2.9 to +6.3) | +3.0% (-1.4 to +7.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.29 | -0.4% (-7.7 to +6.9) | +1.0% (-4.6 to +6.6) | +2.8% (-0.6 to +6.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 6 | +6 (+3.52 to +8.48) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (4 trials, 1 allowed, 1 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused); acting: 512 to 640 (5 trials, 1 allowed, 0 refused); run B: acting: 512 to 640 (3 trials, 1 allowed, 1 refused); acting: 512 to 640 (3 trials, 1 allowed, 1 refused); acting: 512 to 640 (3 trials, 1 allowed, 1 refused); run C: acting: 512 to 640 (3 trials, 1 allowed, 1 refused); acting: 512 to 640 (3 trials, 1 allowed, 1 refused); acting: 512 to 640 (3 trials, 1 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296.4 | 296.1 | -0.1% (-0.4 to +0.2) | -0.2% (-1.5 to +1.2) | +0.1% (-0.6 to +0.8) | EVEN, under the floor (the three runs' mean 0.07%) |
| throughput (transactions a second) | 296.5 | 296.3 | -0.1% (-0.2 to +0.1) | -0.2% (-1.5 to +1.2) | +0.1% (-0.7 to +0.8) | EVEN, under the floor (the three runs' mean 0.07%) |
| queries a second | 4,745 | 4,741 | -0.1% (-0.2 to +0.1) | -0.2% (-1.5 to +1.2) | +0.1% (-0.7 to +0.8) | EVEN, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 2.04 | 1.97 | -3.8% (-28.1 to +20.5) | -1.2% (-3.8 to +1.4) | -1.8% (-6.3 to +2.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 3.82 | 3.66 | -4.0% (-17.1 to +9.1) | -2.4% (-4.9 to +0.1) | -3.0% (-5.5 to -0.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 1.35 | 1.32 | -1.7% (-13.1 to +9.7) | -0.3% (-0.9 to +0.2) | -0.6% (-1.9 to +0.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 483.6 | -5.6% (-47.6 to +36.5) | +11.0% (+0.6 to +21.4) | +5.9% (-18.2 to +30.0) | **the runs disagree** |
| pages holding data, mean (MB) | 462.0 | 437.8 | -5.2% (-49.6 to +39.2) | +12.3% (+4.1 to +20.5) | +6.4% (-21.2 to +34.1) | **the runs disagree** |
| pages read from disk into the pool (misses) | 655,264 | 698,919 | +6.7% (-76.4 to +89.7) | -26.5% (-37.8 to -15.2) | -16.6% (-61.0 to +27.9) | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.104 | -2.5% (-14.5 to +9.5) | -0.4% (-1.3 to +0.4) | -0.1% (-3.4 to +3.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 191.0 | 186.2 | -2.5% (-14.4 to +9.4) | -0.4% (-1.1 to +0.3) | -0.1% (-3.4 to +3.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 1.41 | 1.38 | -2.4% (-14.2 to +9.4) | -0.2% (-1.0 to +0.5) | -0.1% (-2.8 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 | +9.33 (-6.83 to +25.5) | +14.7 (+11.8 to +17.5) | +13.3 (+8.16 to +18.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 512 (3 trials, 1 allowed, 1 refused); acting: 512 to 640 (7 trials, 1 allowed, 4 refused); acting: 512 to 640 (5 trials, 1 allowed, 3 refused); run B: acting: 384 to 768 (8 trials, 3 allowed, 2 refused); acting: 384 to 896 (9 trials, 4 allowed, 1 refused); acting: 384 to 768 (7 trials, 3 allowed, 2 refused); run C: acting: 512 to 640 (6 trials, 1 allowed, 2 refused); acting: 384 to 768 (8 trials, 3 allowed, 2 refused); acting: 512 to 768 (7 trials, 2 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195.0 | 195.6 | +0.3% (-0.9 to +1.6) | -10.1% (-41.9 to +21.7) | +0.7% (-0.4 to +1.8) | **the runs disagree** |
| throughput (transactions a second) | 196.8 | 196.9 | +0.1% (-0.6 to +0.8) | -1.1% (-6.2 to +4.1) | -0.0% (-0.4 to +0.4) | EVEN, under the floor (the three runs' mean 0.33%) |
| queries a second | 3,935 | 3,939 | +0.1% (-0.6 to +0.8) | -1.1% (-6.2 to +4.1) | -0.0% (-0.4 to +0.4) | EVEN, under the floor (the three runs' mean 0.33%) |
| latency, 95th percentile (ms) | 5.78 | 5.71 | -1.2% (-19.7 to +17.3) | +156.5% (-472.6 to +785.5) | -5.8% (-12.4 to +0.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 10.6 | 9.29 | -12.0% (-67.1 to +43.1) | +78.2% (-243.0 to +399.5) | -6.9% (-15.6 to +1.7) | **the runs disagree** |
| latency, mean (ms) | 3.74 | 3.63 | -2.8% (-24.4 to +18.8) | +82.5% (-219.2 to +384.2) | -2.4% (-8.1 to +3.2) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 549.0 | +7.2% (-24.9 to +39.3) | +0.0% (+0.0 to +0.0) | +23.1% (+15.6 to +30.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 461.2 | 497.9 | +8.0% (-22.1 to +38.0) | -0.6% (-3.5 to +2.4) | +19.9% (+14.7 to +25.2) | **the runs disagree** |
| pages read from disk into the pool (misses) | 614,325 | 542,358 | -11.7% (-48.7 to +25.2) | -2.2% (-10.6 to +6.2) | -29.9% (-44.8 to -15.0) | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.18 | +0.0% (-1.8 to +1.9) | -0.9% (-6.9 to +5.2) | -2.7% (-7.3 to +1.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 318.4 | 318.6 | +0.1% (-2.2 to +2.3) | -0.6% (-6.1 to +4.9) | -2.7% (-7.2 to +1.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 3.58 | 3.57 | -0.3% (-2.1 to +1.6) | +10.9% (-24.5 to +46.2) | -3.4% (-8.4 to +1.6) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 12.0 | +12 (+3.04 to +21) | +0 (+0 to +0) | +18.7 (+13.5 to +23.8) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 640 (5 trials, 2 allowed, 3 refused); acting: 384 to 640 (5 trials, 2 allowed, 3 refused); acting: 384 to 1024 (9 trials, 5 allowed, 3 refused); run B: left native (6 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused); run C: acting: 512 to 896 (12 trials, 3 allowed, 3 refused); acting: 512 to 896 (12 trials, 3 allowed, 3 refused); acting: 512 to 896 (10 trials, 3 allowed, 2 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.32 | 6.23 | -1.4% (-43.4 to +40.5) | +4.2% (-15.5 to +23.8) | -3.5% (-31.8 to +24.8) | **the runs disagree** |
| throughput (transactions a second) | 983.8 | 982.9 | -0.1% (-0.7 to +0.5) | -0.1% (-0.4 to +0.3) | +0.3% (-0.3 to +0.8) | EVEN, under the floor (the three runs' mean 0.03%) |
| queries a second | 983.8 | 982.9 | -0.1% (-0.7 to +0.5) | -0.1% (-0.4 to +0.3) | +0.3% (-0.3 to +0.8) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 1.84 | 1.87 | +1.6% (-14.5 to +17.7) | -12.6% (-47.4 to +22.3) | -2.0% (-18.8 to +14.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 3.73 | 3.84 | +3.0% (-1.8 to +7.7) | -29.8% (-77.2 to +17.6) | -0.6% (-7.6 to +6.3) | **the runs disagree** |
| latency, mean (ms) | 1.22 | 1.1 | -10.0% (-45.6 to +25.5) | -19.7% (-58.0 to +18.7) | -1.1% (-8.8 to +6.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 512.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| pages holding data, mean (MB) | 454.4 | 451.0 | -0.7% (-3.3 to +1.8) | -0.9% (-3.3 to +1.5) | -0.7% (-3.3 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 187,953 | 187,323 | -0.3% (-8.3 to +7.7) | -0.8% (-5.2 to +3.7) | -1.3% (-5.7 to +3.2) | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.115 | -5.0% (-32.7 to +22.8) | -3.4% (-20.7 to +14.0) | -4.1% (-28.4 to +20.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 185.9 | 177.0 | -4.8% (-32.5 to +22.8) | -3.4% (-20.0 to +13.3) | -4.1% (-27.8 to +19.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 70.4 | 67.7 | -3.9% (-46.8 to +39.0) | -5.9% (-11.3 to -0.5) | -4.4% (-63.6 to +54.8) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

**Across 4 untouched workloads: 17 gauge-rows GAIN, 0 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 EVEN, 13 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
