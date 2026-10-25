# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39379929041 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| B | 39410600428 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| C | 39461498952 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,955 | 2,949 | -0.2% (-0.8 to +0.4) | -0.1% (-0.4 to +0.2) | +0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (transactions a second) | 2,962 | 2,961 | -0.0% (-0.6 to +0.5) | -0.1% (-0.5 to +0.3) | +0.0% (-0.2 to +0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| queries a second | 2,962 | 2,961 | -0.0% (-0.6 to +0.5) | -0.1% (-0.5 to +0.3) | +0.0% (-0.2 to +0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.214 | 0.212 | -1.2% (-6.6 to +4.1) | -1.2% (-10.7 to +8.3) | -3.6% (-42.2 to +35.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.363 | 0.365 | +0.6% (-6.4 to +7.5) | -0.1% (-4.7 to +4.5) | -2.3% (-16.2 to +11.6) | **the runs disagree** |
| latency, mean (ms) | 0.2 | 0.353 | +77.0% (-152.9 to +306.9) | +5.8% (-37.6 to +49.3) | +1.4% (-27.2 to +30.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 427.6 | -16.5% (-32.9 to -0.1) | -21.7% (-46.0 to +2.7) | -10.1% (-19.6 to -0.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pages holding data, mean (MB) | 463.5 | 391.2 | -15.6% (-31.4 to +0.2) | -20.9% (-42.1 to +0.3) | -9.5% (-18.9 to -0.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 365,322 | 461,733 | +26.4% (-6.0 to +58.8) | +36.5% (-14.7 to +87.7) | +16.6% (+3.3 to +29.9) | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.111 | +0.3% (-1.7 to +2.2) | +1.7% (-3.9 to +7.3) | +0.8% (-29.9 to +31.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 197.6 | 198.1 | +0.3% (-1.7 to +2.2) | +1.7% (-3.9 to +7.3) | +0.8% (-29.9 to +31.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.147 | +0.4% (-1.5 to +2.3) | +1.8% (-4.0 to +7.7) | +0.8% (-29.6 to +31.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 | +8.33 (+2.6 to +14.1) | +7 (-6.15 to +20.1) | +10.3 (+7.46 to +13.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (5 trials, 1 allowed, 2 refused); acting: 256 to 512 (4 trials, 2 allowed, 0 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused); run B: acting: 384 to 512 (6 trials, 1 allowed, 3 refused); acting: 256 to 512 (3 trials, 2 allowed, 0 refused); acting: 256 to 512 (3 trials, 2 allowed, 0 refused); run C: acting: 256 to 512 (6 trials, 2 allowed, 2 refused); acting: 256 to 512 (7 trials, 2 allowed, 3 refused); acting: 256 to 512 (6 trials, 2 allowed, 2 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291.8 | 293.1 | +0.4% (-1.3 to +2.2) | +0.7% (-7.7 to +9.1) | -0.4% (-3.2 to +2.4) | STEADY, under the floor (the three runs' mean 0.23%) |
| throughput (transactions a second) | 293.1 | 294.7 | +0.6% (-1.0 to +2.1) | -0.4% (-2.8 to +2.0) | -0.3% (-1.5 to +0.9) | STEADY, under the floor (the three runs' mean 0.03%) |
| queries a second | 4,689 | 4,716 | +0.6% (-1.0 to +2.1) | -0.4% (-2.8 to +2.0) | -0.3% (-1.5 to +0.9) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 5.31 | 5.25 | -1.2% (-3.8 to +1.4) | -37.5% (-213.4 to +138.4) | -1.3% (-14.8 to +12.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 7.34 | 7.57 | +3.0% (+0.4 to +5.6) | -35.6% (-369.4 to +298.3) | -59.1% (-404.7 to +286.6) | **the runs disagree** |
| latency, mean (ms) | 3.33 | 3.34 | +0.3% (-1.1 to +1.7) | -16.9% (-137.4 to +103.7) | -8.4% (-141.8 to +125.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 460.2 | -10.1% (-27.9 to +7.7) | -31.5% (-54.6 to -8.3) | -25.2% (-62.5 to +12.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 447.0 | 393.0 | -12.1% (-34.5 to +10.3) | -33.9% (-52.3 to -15.5) | -22.5% (-67.2 to +22.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 243,509 | 262,187 | +7.7% (-22.4 to +37.7) | +21.4% (-14.3 to +57.1) | +16.6% (-23.9 to +57.2) | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.196 | +1.6% (-2.6 to +5.8) | +0.2% (-3.2 to +3.6) | +1.7% (-5.6 to +8.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 106.3 | 108.0 | +1.7% (-3.1 to +6.4) | +0.2% (-3.1 to +3.5) | +1.7% (-5.8 to +9.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.41 | +1.3% (-1.8 to +4.5) | -0.5% (-9.1 to +8.0) | +2.1% (-6.7 to +10.8) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 | +8.33 (+4.54 to +12.1) | +3.67 (+2.23 to +5.1) | +5.33 (+0.162 to +10.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (5 trials, 0 allowed, 2 refused); left native (5 trials, 0 allowed, 1 refused); acting: 256 to 512 (3 trials, 2 allowed, 1 refused); run B: acting: 256 to 512 (4 trials, 2 allowed, 0 refused); acting: 384 to 512 (4 trials, 1 allowed, 0 refused); acting: 256 to 512 (3 trials, 2 allowed, 0 refused); run C: acting: 384 to 512 (4 trials, 1 allowed, 1 refused); acting: 256 to 640 (4 trials, 3 allowed, 0 refused); acting: 256 to 512 (4 trials, 2 allowed, 0 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.4 | 295.4 | -0.0% (-0.4 to +0.3) | -0.0% (-1.6 to +1.6) | +0.1% (-0.8 to +0.9) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (transactions a second) | 295.6 | 295.6 | +0.0% (-0.4 to +0.4) | +0.0% (-1.6 to +1.6) | +0.1% (-0.8 to +0.9) | STEADY, under the floor (the three runs' mean 0.03%) |
| queries a second | 4,730 | 4,730 | +0.0% (-0.4 to +0.4) | +0.0% (-1.6 to +1.6) | +0.1% (-0.8 to +0.9) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 1.88 | 1.93 | +2.5% (-9.1 to +14.0) | -1.8% (-6.3 to +2.7) | -1.8% (-6.3 to +2.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 3.64 | 3.66 | +0.7% (-19.9 to +21.2) | -1.8% (-6.2 to +2.7) | -0.6% (-3.2 to +2.0) | **the runs disagree** |
| latency, mean (ms) | 1.28 | 1.3 | +1.6% (-1.5 to +4.7) | -0.8% (-2.7 to +1.2) | -0.7% (-2.7 to +1.4) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 361.9 | -29.3% (-44.3 to -14.3) | -3.4% (-22.5 to +15.8) | -7.9% (-12.1 to -3.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pages holding data, mean (MB) | 461.7 | 333.7 | -27.7% (-46.7 to -8.8) | -3.5% (-18.4 to +11.4) | -8.4% (-11.9 to -4.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read from disk into the pool (misses) | 655,755 | 1,048,015 | +59.8% (+27.2 to +92.4) | +1.4% (-32.1 to +34.9) | +14.2% (+4.5 to +23.8) | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.104 | +2.3% (-4.9 to +9.4) | -0.6% (-4.3 to +3.1) | -0.4% (-1.7 to +0.9) | **the runs disagree** |
| host CPU-seconds | 182.4 | 186.5 | +2.3% (-4.8 to +9.3) | -0.6% (-4.3 to +3.1) | -0.4% (-1.7 to +0.9) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 1.36 | 1.39 | +2.2% (-5.0 to +9.5) | -0.6% (-2.8 to +1.6) | -0.5% (-2.0 to +1.0) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 | +11.3 (+0.131 to +22.5) | +16.7 (+10.4 to +22.9) | +16.3 (+12.5 to +20.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (6 trials, 2 allowed, 2 refused); acting: 256 to 512 (9 trials, 2 allowed, 3 refused); acting: 256 to 512 (5 trials, 2 allowed, 1 refused); run B: left native (13 trials, 0 allowed, 3 refused); acting: 256 to 512 (10 trials, 2 allowed, 4 refused); left native (12 trials, 0 allowed, 3 refused); run C: acting: 384 to 512 (10 trials, 1 allowed, 2 refused); acting: 256 to 512 (9 trials, 2 allowed, 4 refused); acting: 256 to 512 (11 trials, 2 allowed, 4 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192.9 | 191.3 | -0.8% (-3.1 to +1.5) | +0.1% (-0.2 to +0.5) | -0.6% (-2.5 to +1.4) | STEADY, under the floor (the three runs' mean 0.42%) |
| throughput (transactions a second) | 197.9 | 196.6 | -0.7% (-1.6 to +0.2) | +0.4% (-0.2 to +0.9) | -0.0% (-2.0 to +1.9) | STEADY, under the floor (the three runs' mean 0.11%) |
| queries a second | 3,959 | 3,932 | -0.7% (-1.6 to +0.2) | +0.4% (-0.2 to +0.9) | -0.0% (-2.0 to +1.9) | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms) | 6.74 | 7.11 | +5.5% (-46.7 to +57.7) | +1.2% (-5.7 to +8.2) | +3.8% (-14.9 to +22.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 22.5 | 26.5 | +17.6% (-135.4 to +170.5) | +3.0% (-8.3 to +14.3) | +634.4% (-2079.7 to +3348.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.54 | 3.74 | +5.5% (-34.7 to +45.6) | +0.4% (-0.2 to +1.0) | +77.7% (-246.6 to +402.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 434.6 | -15.1% (-23.2 to -7.0) | +3.1% (+1.1 to +5.1) | +5.5% (-19.7 to +30.8) | **the runs disagree** |
| pages holding data, mean (MB) | 461.8 | 392.1 | -15.1% (-23.7 to -6.5) | +2.2% (-1.0 to +5.4) | +5.0% (-17.1 to +27.1) | **the runs disagree** |
| pages read from disk into the pool (misses) | 618,586 | 811,497 | +31.2% (+20.4 to +42.0) | -4.8% (-20.3 to +10.7) | -9.1% (-44.1 to +25.9) | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.138 | +3.4% (-1.8 to +8.6) | +0.0% (-2.7 to +2.8) | +1.0% (+0.1 to +1.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 237.3 | 245.4 | +3.4% (-1.7 to +8.5) | +0.1% (-2.7 to +2.9) | +1.0% (-0.0 to +2.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.7 | 2.81 | +4.2% (+1.4 to +7.0) | -0.0% (-2.6 to +2.5) | +1.5% (-1.4 to +4.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 | +11.3 (+7.54 to +15.1) | +15.3 (+4.99 to +25.7) | +16.3 (-3.59 to +36.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (6 trials, 2 allowed, 2 refused); acting: 256 to 512 (7 trials, 2 allowed, 2 refused); acting: 256 to 512 (6 trials, 2 allowed, 3 refused); run B: left native (13 trials, 0 allowed, 4 refused); acting: 512 to 640 (11 trials, 1 allowed, 4 refused); left native (12 trials, 0 allowed, 4 refused); run C: left native (13 trials, 0 allowed, 3 refused); acting: 384 to 512 (12 trials, 1 allowed, 4 refused); acting: 512 to 640 (14 trials, 1 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 204.4 | 246.4 | +20.5% (-56.0 to +97.1) | +0 (+0 to +0) | +2.1% (-18.5 to +22.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 988.5 | 988.1 | -0.0% (-0.6 to +0.6) | -0.2% (-0.7 to +0.4) | +0.2% (-0.1 to +0.5) | STEADY, under the floor (the three runs' mean 0.01%) |
| queries a second | 988.5 | 988.1 | -0.0% (-0.6 to +0.6) | -0.2% (-0.7 to +0.4) | +0.2% (-0.1 to +0.5) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 2.87 | 2.7 | -6.1% (-39.4 to +27.3) | -2.0% (-17.9 to +13.9) | -2.7% (-22.2 to +16.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 6.56 | 5.31 | -19.0% (-107.5 to +69.4) | -4.5% (-41.7 to +32.7) | -1.3% (-10.7 to +8.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 1.08 | 1.02 | -5.7% (-34.8 to +23.3) | -1.1% (-11.1 to +8.9) | -0.6% (-7.9 to +6.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 450.2 | -12.1% (-19.6 to -4.6) | -0.9% (-24.5 to +22.7) | -2.9% (-9.9 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 452.5 | 380.5 | -15.9% (-18.3 to -13.5) | -4.6% (-26.5 to +17.2) | -5.3% (-13.0 to +2.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 189,515 | 230,352 | +21.5% (+7.3 to +35.8) | +4.9% (-23.6 to +33.4) | +6.5% (-13.2 to +26.2) | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.119 | -3.4% (-22.9 to +16.1) | -1.6% (-11.6 to +8.3) | -1.9% (-14.0 to +10.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 217.4 | 210.2 | -3.3% (-22.7 to +16.1) | -1.6% (-11.5 to +8.3) | -1.9% (-14.0 to +10.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 1.99 | -17.3% (-105.5 to +70.8) | -1.6% (-11.5 to +8.3) | -6.5% (-47.1 to +34.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 | +16.7 (+7.94 to +25.4) | +19 (+11.5 to +26.5) | +19.7 (+13.9 to +25.4) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (11 trials, 2 allowed, 4 refused); acting: 256 to 512 (9 trials, 2 allowed, 3 refused); acting: 384 to 512 (12 trials, 1 allowed, 3 refused); run B: acting: 384 to 512 (14 trials, 1 allowed, 3 refused); acting: 384 to 512 (12 trials, 1 allowed, 4 refused); acting: 384 to 640 (14 trials, 2 allowed, 3 refused); run C: left native (16 trials, 0 allowed, 3 refused); acting: 384 to 640 (15 trials, 2 allowed, 2 refused); acting: 384 to 512 (13 trials, 1 allowed, 4 refused).

**Across 4 untouched workloads: 15 gauge-rows GAIN, 3 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 STEADY, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
