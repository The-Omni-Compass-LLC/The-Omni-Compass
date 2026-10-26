# sysbench on MySQL, a database's buffer pool as shipped: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native (`docs/MYSQL_PREREGISTRATION.md`, amendment 5); omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40236930776 | `23c7e8eb27be` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40259317345 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40283015397 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,947 | +0.1% (+0.0 to +0.1) | -0.1% (-0.3 to +0.1) | +0.1% (-0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.02%) |
| throughput (transactions a second) | 2,951 | 2,954 | +0.1% (+0.0 to +0.2) | -0.1% (-0.2 to +0.1) | +0.1% (-0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.04%) |
| queries a second | 2,951 | 2,954 | +0.1% (+0.0 to +0.2) | -0.1% (-0.2 to +0.1) | +0.1% (-0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 0.346 | 0.348 | +0.6% (-6.0 to +7.2) | +8.0% (+2.9 to +13.1) | -1.1% (-3.6 to +1.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.451 | 0.453 | +0.6% (-2.0 to +3.1) | +7.4% (-1.0 to +15.8) | -1.2% (-3.6 to +1.3) | **the runs disagree** |
| latency, mean (ms) | 0.209 | 0.212 | +1.1% (-4.2 to +6.4) | +8.8% (-6.4 to +24.0) | -0.9% (-1.5 to -0.4) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 130.4 | +1.9% (+1.6 to +2.2) | +1.2% (-3.9 to +6.2) | +2.6% (-0.2 to +5.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 121.2 | 124.3 | +2.5% (-0.0 to +5.0) | +2.2% (-7.0 to +11.3) | +4.6% (-1.8 to +11.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 1,028,019 | 1,020,820 | -0.7% (-0.8 to -0.6) | -0.3% (-1.1 to +0.6) | -0.9% (-1.3 to -0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.114 | +1.8% (-7.2 to +10.7) | +11.4% (-0.2 to +22.9) | -1.1% (-2.6 to +0.3) | **the runs disagree** |
| host CPU-seconds | 187.3 | 190.5 | +1.7% (-7.3 to +10.7) | +11.3% (-0.2 to +22.8) | -1.1% (-2.6 to +0.3) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.139 | 0.141 | +1.6% (-7.3 to +10.6) | +11.4% (-0.3 to +23.1) | -1.2% (-2.8 to +0.4) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +0.667 (-2.2 to +3.54) | +2.67 (-0.202 to +5.54) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291.2 | 293.0 | +0.6% (-0.4 to +1.6) | -1.3% (-3.1 to +0.6) | +0.4% (-2.3 to +3.2) | **the runs disagree** |
| throughput (transactions a second) | 293.7 | 295.5 | +0.6% (-0.0 to +1.3) | +0.3% (-1.5 to +2.1) | +0.5% (-2.2 to +3.2) | EVEN, under the floor (the three runs' mean 0.46%) |
| queries a second | 4,698 | 4,727 | +0.6% (-0.0 to +1.3) | +0.3% (-1.5 to +2.1) | +0.5% (-2.2 to +3.2) | EVEN, under the floor (the three runs' mean 0.46%) |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.0% (+0.0 to +0.0) | +255.1% (-554.4 to +1064.6) | +0.6% (-2.0 to +3.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 8.08 | 8.03 | -0.6% (-7.4 to +6.2) | +155.2% (-338.0 to +648.5) | +2.4% (-2.8 to +7.7) | **the runs disagree** |
| latency, mean (ms) | 3.44 | 3.41 | -0.9% (-5.9 to +4.1) | +116.8% (-252.2 to +485.8) | -0.0% (-0.3 to +0.3) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 134.9 | +5.4% (+4.4 to +6.4) | +9.0% (-5.9 to +23.9) | +5.4% (+4.5 to +6.3) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pages holding data, mean (MB) | 120.0 | 129.5 | +8.0% (+6.7 to +9.2) | +9.5% (-3.8 to +22.8) | +8.1% (+5.6 to +10.7) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read from disk into the pool (misses) | 572,987 | 560,449 | -2.2% (-4.1 to -0.3) | -6.7% (-13.5 to +0.1) | -4.1% (-10.9 to +2.6) | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.2 | +1.8% (-2.2 to +5.9) | +0.7% (+0.4 to +1.0) | +1.2% (-0.5 to +2.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 109.3 | 111.5 | +1.9% (-2.4 to +6.3) | +0.8% (+0.4 to +1.1) | +1.2% (-0.5 to +2.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.48 | +1.2% (-3.9 to +6.3) | +2.1% (+0.1 to +4.0) | +0.8% (-0.4 to +2.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| buffer pool size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +2 (+2 to +2) | +2 (+2 to +2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); acting: 128 to 256 (2 trials, 1 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.1 | 294.9 | -0.0% (-1.8 to +1.8) | -0.0% (-0.8 to +0.7) | -0.1% (-0.7 to +0.6) | EVEN, under the floor (the three runs' mean 0.05%) |
| throughput (transactions a second) | 295.5 | 295.3 | -0.0% (-1.8 to +1.7) | +0.0% (-0.7 to +0.7) | -0.1% (-0.7 to +0.6) | EVEN, under the floor (the three runs' mean 0.03%) |
| queries a second | 4,727 | 4,725 | -0.0% (-1.8 to +1.7) | +0.0% (-0.7 to +0.7) | -0.1% (-0.7 to +0.6) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 3.91 | 3.89 | -0.6% (-5.8 to +4.6) | +0.0% (+0.0 to +0.0) | +0.6% (-2.0 to +3.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 5.54 | 5.47 | -1.2% (-8.1 to +5.7) | -1.6% (-46.6 to +43.3) | -0.0% (-4.5 to +4.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.05 | 3.04 | -0.4% (-4.6 to +3.9) | +8.7% (-40.0 to +57.4) | -0.1% (-1.7 to +1.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 131.2 | +2.5% (-0.2 to +5.2) | +2.6% (-0.2 to +5.5) | +3.2% (+0.5 to +5.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages holding data, mean (MB) | 120.2 | 125.8 | +4.7% (-5.2 to +14.6) | +6.7% (+2.4 to +10.9) | +6.6% (-1.4 to +14.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 1,988,214 | 2,036,938 | +2.5% (-1.4 to +6.3) | +2.5% (-4.0 to +9.0) | +2.2% (-3.5 to +7.9) | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.185 | +0.0% (-5.4 to +5.4) | -0.5% (-1.6 to +0.6) | +0.3% (-2.6 to +3.1) | EVEN, under the floor (the three runs' mean 0.07%) |
| host CPU-seconds | 308.7 | 308.9 | +0.1% (-5.3 to +5.4) | -0.5% (-1.7 to +0.6) | +0.3% (-2.6 to +3.3) | EVEN, under the floor (the three runs' mean 0.04%) |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.29 | +0.1% (-5.6 to +5.8) | -0.5% (-0.9 to -0.1) | +0.4% (-2.4 to +3.2) | EVEN, under the floor (the three runs' mean 0.00%) |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +2.67 (-0.202 to +5.54) | +3.33 (+0.465 to +6.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193.9 | 194.1 | +0.1% (-4.2 to +4.4) | +0.3% (-1.0 to +1.6) | +0.2% (-1.5 to +1.9) | EVEN, under the floor (the three runs' mean 0.18%) |
| throughput (transactions a second) | 197.4 | 197.4 | +0.0% (-1.2 to +1.2) | -0.2% (-2.0 to +1.6) | +0.2% (-1.5 to +1.9) | EVEN, under the floor (the three runs' mean 0.01%) |
| queries a second | 3,948 | 3,948 | +0.0% (-1.2 to +1.2) | -0.2% (-2.0 to +1.6) | +0.2% (-1.5 to +1.9) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 6.66 | 6.66 | +0.0% (-53.9 to +53.9) | -1.2% (-7.9 to +5.6) | +2.4% (-0.2 to +5.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 18.0 | 17.0 | -5.5% (-264.0 to +252.9) | -1.2% (-3.8 to +1.4) | +1.2% (-1.4 to +3.8) | **the runs disagree** |
| latency, mean (ms) | 3.19 | 3.15 | -1.1% (-49.3 to +47.1) | -0.5% (-2.9 to +1.9) | +6.0% (-2.1 to +14.0) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 146.1 | +14.1% (+0.5 to +27.7) | +14.2% (+9.0 to +19.4) | +6.1% (-3.3 to +15.6) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pages holding data, mean (MB) | 121.7 | 138.1 | +13.5% (-3.0 to +30.0) | +14.8% (+12.7 to +16.9) | +4.9% (-3.9 to +13.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read from disk into the pool (misses) | 1,665,755 | 1,573,790 | -5.5% (-14.4 to +3.4) | -5.1% (-9.8 to -0.5) | -3.1% (-9.3 to +3.1) | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.135 | -1.9% (-6.4 to +2.5) | -0.9% (-2.4 to +0.6) | +4.7% (+3.1 to +6.3) | **the runs disagree** |
| host CPU-seconds | 245.6 | 240.8 | -2.0% (-6.6 to +2.6) | -0.9% (-2.1 to +0.4) | +4.7% (+3.2 to +6.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 2.78 | 2.72 | -2.0% (-8.8 to +4.7) | -1.2% (-3.4 to +1.1) | +4.5% (+4.2 to +4.7) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 | +8.67 (+7.23 to +10.1) | +10 (+10 to +10) | +4.33 (+0.538 to +8.13) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (5 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); left native (5 trials, 0 allowed, 4 refused); run B: left native (5 trials, 0 allowed, 5 refused); left native (5 trials, 0 allowed, 5 refused); left native (5 trials, 0 allowed, 5 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158.4 | 137.3 | -13.4% (-68.4 to +41.6) | -15.4% (-127.1 to +96.4) | +10.1% (-0.8 to +20.9) | **the runs disagree** |
| throughput (transactions a second) | 988.3 | 987.8 | -0.0% (-0.4 to +0.3) | +0.0% (-0.6 to +0.7) | +0.1% (-0.3 to +0.6) | EVEN, under the floor (the three runs' mean 0.03%) |
| queries a second | 988.3 | 987.8 | -0.0% (-0.4 to +0.3) | +0.0% (-0.6 to +0.7) | +0.1% (-0.3 to +0.6) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 2.32 | 2.18 | -6.4% (-27.4 to +14.6) | -3.2% (-32.5 to +26.1) | +2.8% (-12.9 to +18.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 4.92 | 4.52 | -8.0% (-28.6 to +12.6) | -10.4% (-108.0 to +87.2) | +8.8% (-40.1 to +57.6) | **the runs disagree** |
| latency, mean (ms) | 1.05 | 1.06 | +1.6% (-17.8 to +21.1) | +2.8% (-22.6 to +28.2) | +2.2% (-4.1 to +8.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 128.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| pages holding data, mean (MB) | 117.2 | 118.1 | +0.8% (-3.6 to +5.1) | -1.0% (-2.2 to +0.3) | -0.4% (-5.7 to +4.8) | **the runs disagree** |
| pages read from disk into the pool (misses) | 415,683 | 414,343 | -0.3% (-2.2 to +1.6) | -0.2% (-2.5 to +2.0) | -0.1% (-2.3 to +2.1) | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.146 | +2.0% (-6.2 to +10.2) | +0.2% (-13.3 to +13.7) | +5.9% (-18.2 to +29.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 252.3 | 257.4 | +2.0% (-6.2 to +10.2) | +0.2% (-13.1 to +13.6) | +5.9% (-18.3 to +30.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 3.62 | 4.22 | +16.7% (-54.6 to +87.9) | +4.0% (-129.9 to +137.8) | -2.3% (-30.7 to +26.2) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

**Across 4 untouched workloads: 1 gauge-rows GAIN, 3 LOSS, 11 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 18 EVEN, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
