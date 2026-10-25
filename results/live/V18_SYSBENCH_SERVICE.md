# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40134818204 | `7743f2e82851` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| B | 40135957187 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| C | 40137084068 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,956 | 2,958 | +0.1% (-0.3 to +0.4) | +0.0% (-0.2 to +0.3) | +0.1% (-0.9 to +1.1) | EVEN, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 2,965 | 2,964 | -0.0% (-0.2 to +0.1) | +0.0% (-0.2 to +0.3) | -0.1% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| queries a second | 2,965 | 2,964 | -0.0% (-0.2 to +0.1) | +0.0% (-0.2 to +0.3) | -0.1% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.209 | 0.203 | -2.9% (-9.5 to +3.8) | -0.7% (-25.6 to +24.1) | -4.6% (-28.9 to +19.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.354 | 0.346 | -2.4% (-5.2 to +0.5) | +1.8% (-6.2 to +9.9) | -5.7% (-45.0 to +33.6) | **the runs disagree** |
| latency, mean (ms) | 0.271 | 0.173 | -36.3% (-163.9 to +91.3) | +3.2% (-4.5 to +10.9) | -68.7% (-370.9 to +233.5) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 408.6 | -20.2% (-41.8 to +1.4) | -4.8% (-19.0 to +9.4) | -1.6% (-12.6 to +9.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages holding data, mean (MB) | 463.4 | 373.9 | -19.3% (-39.1 to +0.5) | -4.0% (-17.3 to +9.4) | -4.8% (-15.2 to +5.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 368,147 | 495,478 | +34.6% (-10.1 to +79.3) | +4.0% (-19.2 to +27.1) | +3.6% (-12.0 to +19.2) | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.11 | -1.3% (-7.3 to +4.6) | +3.2% (-2.4 to +8.7) | -0.5% (-16.4 to +15.5) | **the runs disagree** |
| host CPU-seconds | 199.0 | 196.3 | -1.3% (-7.3 to +4.6) | +3.2% (-2.4 to +8.8) | -0.5% (-16.4 to +15.5) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.148 | 0.146 | -1.4% (-7.4 to +4.6) | +3.2% (-2.4 to +8.7) | -0.6% (-17.4 to +16.3) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 | +4.33 (-1.4 to +10.1) | +9 (+4.03 to +14) | +10.7 (-1.84 to +23.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 640 (4 trials, 2 allowed, 1 refused); acting: 384 to 512 (2 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 1 allowed, 1 refused); run B: left native (5 trials, 0 allowed, 2 refused); acting: 256 to 512 (4 trials, 2 allowed, 1 refused); acting: 384 to 640 (6 trials, 2 allowed, 3 refused); run C: left native (3 trials, 0 allowed, 2 refused); acting: 512 to 640 (6 trials, 1 allowed, 3 refused); acting: 384 to 640 (8 trials, 2 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.3 | 292.1 | -0.1% (-1.9 to +1.8) | +0.0% (-1.6 to +1.7) | +0.2% (-1.1 to +1.5) | EVEN, under the floor (the three runs' mean 0.05%) |
| throughput (transactions a second) | 293.2 | 293.2 | +0.0% (-1.7 to +1.7) | -0.0% (-1.4 to +1.3) | +0.1% (-0.6 to +0.7) | EVEN, under the floor (the three runs' mean 0.01%) |
| queries a second | 4,691 | 4,691 | +0.0% (-1.7 to +1.7) | -0.0% (-1.4 to +1.3) | +0.1% (-0.6 to +0.7) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 5.18 | 5.18 | +0.0% (-4.5 to +4.5) | -2.9% (-12.2 to +6.3) | -3.0% (-9.8 to +3.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 7.17 | 7.26 | +1.2% (-4.1 to +6.6) | -1.2% (-8.0 to +5.6) | +0.0% (-18.0 to +18.1) | **the runs disagree** |
| latency, mean (ms) | 3.31 | 3.31 | -0.0% (-2.0 to +2.0) | -0.4% (-3.1 to +2.3) | -4.7% (-10.5 to +1.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 528.3 | +3.2% (-10.5 to +16.9) | +2.3% (-10.4 to +15.1) | -23.3% (-67.7 to +21.1) | **the runs disagree** |
| pages holding data, mean (MB) | 447.5 | 444.7 | -0.6% (-23.1 to +21.9) | -1.4% (-26.9 to +24.1) | -23.5% (-71.7 to +24.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read from disk into the pool (misses) | 244,350 | 233,036 | -4.6% (-30.1 to +20.8) | -1.8% (-29.1 to +25.5) | +16.2% (-33.8 to +66.1) | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.193 | +2.1% (-3.4 to +7.5) | +0.7% (-6.5 to +7.9) | -0.7% (-2.7 to +1.4) | **the runs disagree** |
| host CPU-seconds | 104.4 | 106.9 | +2.4% (-3.2 to +8.0) | +0.7% (-7.7 to +9.2) | -0.7% (-2.8 to +1.4) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.39 | +2.3% (-1.5 to +6.1) | +0.8% (-8.6 to +10.2) | -0.9% (-2.6 to +0.9) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 | +7.33 (+4.46 to +10.2) | +6.67 (+2.87 to +10.5) | +5 (+0.0313 to +9.97) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (6 trials, 1 allowed, 0 refused); left native (4 trials, 0 allowed, 1 refused); acting: 512 to 640 (7 trials, 1 allowed, 0 refused); run B: acting: 512 to 640 (7 trials, 1 allowed, 0 refused); left native (7 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused); run C: left native (4 trials, 0 allowed, 2 refused); acting: 256 to 512 (3 trials, 2 allowed, 0 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.0 | 295.0 | +0.0% (-1.3 to +1.3) | -0.4% (-3.2 to +2.4) | -0.3% (-2.7 to +2.1) | EVEN, under the floor (the three runs' mean 0.25%) |
| throughput (transactions a second) | 295.4 | 295.4 | +0.0% (-1.3 to +1.3) | -0.1% (-0.9 to +0.7) | -0.3% (-2.6 to +2.1) | EVEN, under the floor (the three runs' mean 0.14%) |
| queries a second | 4,726 | 4,727 | +0.0% (-1.3 to +1.3) | -0.1% (-0.9 to +0.7) | -0.3% (-2.6 to +2.1) | EVEN, under the floor (the three runs' mean 0.14%) |
| latency, 95th percentile (ms) | 4.13 | 4.05 | -1.8% (-1.9 to -1.7) | -1.2% (-3.7 to +1.4) | -0.6% (-3.2 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 5.67 | 5.64 | -0.6% (-3.1 to +2.0) | +580.0% (-1978.8 to +3138.9) | -0.6% (-3.2 to +2.0) | **the runs disagree** |
| latency, mean (ms) | 3.19 | 3.16 | -1.1% (-3.1 to +0.9) | +66.0% (-279.4 to +411.4) | -0.2% (-1.0 to +0.6) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 581.3 | +13.5% (-18.4 to +45.5) | -3.9% (-24.9 to +17.2) | +17.8% (-13.3 to +49.0) | **the runs disagree** |
| pages holding data, mean (MB) | 462.3 | 501.1 | +8.4% (-12.5 to +29.3) | -4.6% (-32.5 to +23.2) | +12.5% (-7.8 to +32.8) | **the runs disagree** |
| pages read from disk into the pool (misses) | 653,391 | 546,293 | -16.4% (-61.1 to +28.4) | +5.8% (-33.6 to +45.2) | -26.1% (-63.7 to +11.5) | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.188 | -1.0% (-5.9 to +4.0) | -0.9% (-5.0 to +3.2) | -0.1% (-4.4 to +4.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 314.3 | 311.4 | -0.9% (-6.0 to +4.1) | -0.9% (-4.9 to +3.1) | -0.0% (-4.3 to +4.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.31 | -1.0% (-4.8 to +2.9) | -0.5% (-2.0 to +1.1) | +0.3% (-1.6 to +2.2) | EVEN, under the floor (the three runs' mean 0.38%) |
| buffer pool size changes written (the knob's moves) | 0 | 18.0 | +18 (+11.4 to +24.6) | +14.7 (+10.9 to +18.5) | +18 (+8.06 to +27.9) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 640 (9 trials, 2 allowed, 5 refused); acting: 512 to 896 (14 trials, 3 allowed, 3 refused); acting: 512 to 768 (11 trials, 2 allowed, 2 refused); run B: acting: 384 to 512 (8 trials, 1 allowed, 3 refused); acting: 384 to 512 (10 trials, 1 allowed, 4 refused); acting: 384 to 768 (9 trials, 3 allowed, 4 refused); run C: acting: 512 to 896 (10 trials, 3 allowed, 2 refused); acting: 512 to 768 (13 trials, 2 allowed, 3 refused); acting: 512 to 640 (9 trials, 1 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.6 | 192.3 | +0.4% (-0.9 to +1.6) | +1.1% (-0.4 to +2.6) | +0.4% (-1.5 to +2.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 196.5 | 196.6 | +0.0% (-1.2 to +1.3) | +0.5% (-0.5 to +1.5) | -0.3% (-1.7 to +1.2) | EVEN, under the floor (the three runs' mean 0.08%) |
| queries a second | 3,930 | 3,931 | +0.0% (-1.2 to +1.3) | +0.5% (-0.5 to +1.5) | -0.3% (-1.7 to +1.2) | EVEN, under the floor (the three runs' mean 0.08%) |
| latency, 95th percentile (ms) | 8.74 | 8.43 | -3.5% (-7.9 to +0.8) | -6.4% (-12.3 to -0.6) | -5.1% (-24.8 to +14.6) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 13.1 | 12.6 | -4.1% (-13.3 to +5.0) | -4.7% (-7.5 to -1.9) | -7.4% (-35.2 to +20.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 5.34 | 5.32 | -0.3% (-3.2 to +2.5) | -1.3% (-4.8 to +2.1) | -7.7% (-39.1 to +23.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 654.4 | +27.8% (+7.3 to +48.3) | +24.1% (+11.6 to +36.6) | +28.5% (-34.7 to +91.7) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pages holding data, mean (MB) | 461.7 | 557.1 | +20.7% (+1.8 to +39.6) | +19.8% (+13.5 to +26.1) | +20.3% (-22.7 to +63.4) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read from disk into the pool (misses) | 615,056 | 436,215 | -29.1% (-57.2 to -1.0) | -30.5% (-44.6 to -16.4) | -29.7% (-97.4 to +38.1) | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.21 | +0.7% (-2.5 to +3.9) | -1.0% (-3.8 to +1.9) | -2.1% (-9.7 to +5.5) | **the runs disagree** |
| host CPU-seconds | 335.2 | 338.3 | +0.9% (-2.1 to +4.0) | -1.0% (-4.2 to +2.3) | -2.0% (-9.5 to +5.4) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 3.82 | 3.84 | +0.5% (-2.7 to +3.8) | -2.0% (-6.6 to +2.5) | -2.4% (-11.4 to +6.6) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 23.0 | +23 (+18.7 to +27.3) | +19 (+9.06 to +28.9) | +20 (+7.09 to +32.9) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 768 (14 trials, 2 allowed, 2 refused); acting: 384 to 896 (15 trials, 4 allowed, 3 refused); acting: 512 to 1024 (14 trials, 4 allowed, 3 refused); run B: acting: 512 to 1024 (15 trials, 4 allowed, 1 refused); acting: 512 to 768 (15 trials, 2 allowed, 3 refused); acting: 512 to 768 (16 trials, 2 allowed, 3 refused); run C: acting: 512 to 1280 (17 trials, 6 allowed, 1 refused); left native (8 trials, 0 allowed, 4 refused); acting: 512 to 1024 (16 trials, 4 allowed, 2 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.91 | 3.84 | -21.7% (-177.1 to +133.7) | +2.6% (-64.6 to +69.9) | +0.6% (-193.8 to +195.0) | **the runs disagree** |
| throughput (transactions a second) | 983.9 | 983.6 | -0.0% (-0.6 to +0.5) | -0.0% (-0.5 to +0.4) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.03%) |
| queries a second | 983.9 | 983.6 | -0.0% (-0.6 to +0.5) | -0.0% (-0.5 to +0.4) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 1.84 | 1.99 | +8.0% (-31.1 to +47.2) | +52.9% (-259.3 to +365.1) | +1.2% (-36.6 to +39.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 3.86 | 4.21 | +9.0% (-22.0 to +40.0) | +13.5% (-105.2 to +132.2) | -2.5% (-27.5 to +22.6) | **the runs disagree** |
| latency, mean (ms) | 1.11 | 1.15 | +3.6% (-14.6 to +21.8) | +30.5% (-165.7 to +226.7) | -6.8% (-51.1 to +37.5) | **the runs disagree** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 564.5 | +10.3% (-12.5 to +33.0) | -11.2% (-50.0 to +27.7) | +14.0% (-15.2 to +43.1) | **the runs disagree** |
| pages holding data, mean (MB) | 453.7 | 464.2 | +2.3% (-9.7 to +14.3) | -14.6% (-61.7 to +32.5) | +5.8% (-3.1 to +14.6) | **the runs disagree** |
| pages read from disk into the pool (misses) | 188,569 | 187,818 | -0.4% (-16.4 to +15.6) | +24.5% (-41.0 to +90.0) | -6.3% (-15.4 to +2.7) | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.171 | +39.3% (-83.9 to +162.5) | -0.8% (-13.4 to +11.8) | +24.7% (-113.1 to +162.5) | **the runs disagree** |
| host CPU-seconds | 189.7 | 265.1 | +39.8% (-84.4 to +163.9) | -0.7% (-13.0 to +11.6) | +25.2% (-113.7 to +164.0) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 98.5 | 165.7 | +68.3% (-132.1 to +268.7) | -7.3% (-89.5 to +74.8) | +30.7% (-344.0 to +405.4) | **the runs disagree** |
| buffer pool size changes written (the knob's moves) | 0 | 22.7 | +22.7 (+8.98 to +36.3) | +12.7 (+11.2 to +14.1) | +19.7 (+5.98 to +33.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (15 trials, 0 allowed, 3 refused); acting: 512 to 640 (16 trials, 1 allowed, 3 refused); acting: 384 to 1024 (16 trials, 5 allowed, 2 refused); run B: acting: 128 to 640 (9 trials, 4 allowed, 2 refused); acting: 512 to 640 (8 trials, 1 allowed, 4 refused); acting: 256 to 640 (7 trials, 3 allowed, 3 refused); run C: acting: 512 to 896 (14 trials, 3 allowed, 1 refused); acting: 512 to 640 (18 trials, 1 allowed, 2 refused); acting: 512 to 896 (21 trials, 3 allowed, 2 refused).

**Across 4 untouched workloads: 10 gauge-rows GAIN, 1 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 EVEN, 20 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
