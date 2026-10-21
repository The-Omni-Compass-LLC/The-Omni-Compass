# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39108195807 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 5 |
| B | 39116281643 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 5 |
| C | 39123599130 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,937 | -0.0% (-0.3 to +0.2) | -0.1% (-0.3 to +0.1) | -0.1% (-0.5 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,954 | 2,952 | -0.0% (-0.4 to +0.3) | -0.1% (-0.3 to +0.1) | +0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,954 | 2,952 | -0.0% (-0.4 to +0.3) | -0.1% (-0.3 to +0.1) | +0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.35 | 0.352 | +0.6% (-1.9 to +3.0) | -1.8% (-13.6 to +10.0) | +0.6% (-6.4 to +7.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.543 | 0.54 | -0.6% (-2.9 to +1.8) | -2.4% (-11.7 to +6.9) | +1.3% (-9.7 to +12.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.217 | 0.22 | +1.3% (-3.2 to +5.8) | +0.1% (-9.6 to +9.7) | +3.9% (-6.2 to +14.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 483.2 | -5.6% (-19.8 to +8.5) | -5.6% (-14.0 to +2.8) | -4.4% (-9.3 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 463.6 | 432.5 | -6.7% (-19.1 to +5.6) | -5.0% (-16.0 to +6.0) | -4.2% (-7.3 to -1.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 367,376 | 398,934 | +8.6% (-29.0 to +46.2) | +7.0% (-22.7 to +36.7) | +5.5% (-8.7 to +19.8) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.114 | +2.2% (-6.9 to +11.3) | -0.1% (-16.9 to +16.8) | +4.7% (-7.1 to +16.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 185.4 | 189.7 | +2.3% (-6.8 to +11.4) | +0.0% (-16.9 to +17.0) | +4.8% (-7.1 to +16.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.138 | 0.141 | +2.4% (-6.5 to +11.2) | +0.1% (-16.8 to +17.0) | +4.9% (-7.2 to +16.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 | +13.7 (+8.5 to +18.8) | +12 (+1.17 to +22.8) | +12.3 (+10.9 to +13.8) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (8 trials, 1 allowed, 4 refused); acting: 384 to 512 (7 trials, 1 allowed, 3 refused); acting: 384 to 512 (6 trials, 1 allowed, 3 refused); run B: acting: 256 to 640 (7 trials, 3 allowed, 2 refused); acting: 384 to 512 (7 trials, 1 allowed, 3 refused); acting: 384 to 512 (8 trials, 1 allowed, 3 refused); run C: acting: 384 to 512 (8 trials, 1 allowed, 3 refused); acting: 256 to 640 (7 trials, 3 allowed, 3 refused); acting: 384 to 512 (8 trials, 1 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 | +0 (+0 to +0) | -0.7% (-2.9 to +1.6) | -0.0% (-1.5 to +1.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 82.0 | 80.4 | -2.0% (-9.3 to +5.3) | -0.6% (-2.2 to +1.0) | +0.0% (-1.6 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 1,313 | 1,286 | -2.0% (-9.3 to +5.3) | -0.6% (-2.2 to +1.0) | +0.0% (-1.6 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 19,427 | 19,661 | +1.2% (-5.7 to +8.1) | -0.0% (-7.8 to +7.8) | -2.4% (-4.9 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 21,131 | 21,515 | +1.8% (+1.7 to +1.9) | +1.8% (-14.6 to +18.3) | +0.6% (-2.0 to +3.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 10,468 | 10,529 | +0.6% (-4.5 to +5.6) | +6.5% (-22.9 to +35.8) | -0.5% (-0.9 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 512.0 | +0.0% (+0.0 to +0.0) | -0.6% (-14.0 to +12.7) | -2.6% (-19.4 to +14.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 433.8 | 433.0 | -0.2% (-1.6 to +1.2) | -2.6% (-25.5 to +20.3) | -2.7% (-19.7 to +14.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 83,295 | 81,408 | -2.3% (-4.1 to -0.4) | -4.1% (-20.9 to +12.6) | -3.2% (-18.7 to +12.2) | shown, not judged |
| host CPU busy (share of the run) | 0.898 | 0.889 | -0.9% (-13.7 to +11.9) | +0.5% (-0.9 to +2.0) | +1.5% (-0.2 to +3.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 149.0 | 147.0 | -1.3% (-5.7 to +3.1) | +0.7% (-0.6 to +2.0) | +1.8% (-0.3 to +3.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 148,997 | 147,020 | -1.3% (-5.7 to +3.1) | +1.4% (+0.3 to +2.4) | +1.8% (-1.6 to +5.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +7.67 (+6.23 to +9.1) | +8.67 (+4.87 to +12.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (5 trials, 0 allowed, 1 refused); left native (6 trials, 0 allowed, 2 refused); left native (7 trials, 0 allowed, 1 refused); run C: left native (6 trials, 0 allowed, 1 refused); left native (6 trials, 0 allowed, 2 refused); left native (6 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296.6 | 296.9 | +0.1% (-0.8 to +1.0) | +0.2% (-0.8 to +1.2) | -0.0% (-1.3 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 296.7 | 297.0 | +0.1% (-0.9 to +1.1) | +0.2% (-0.9 to +1.2) | -0.0% (-1.3 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,747 | 4,752 | +0.1% (-0.9 to +1.1) | +0.2% (-0.9 to +1.2) | -0.0% (-1.3 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 1.93 | 1.94 | +0.9% (-28.5 to +30.4) | -2.4% (-4.8 to +0.1) | -2.4% (-4.9 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 3.68 | 3.6 | -2.2% (-24.4 to +19.9) | -1.8% (-6.1 to +2.6) | -3.5% (-7.9 to +0.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.32 | 1.29 | -1.8% (-15.0 to +11.3) | -1.3% (-4.4 to +1.8) | -0.8% (-1.2 to -0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 417.3 | -18.5% (-49.1 to +12.1) | -6.6% (-24.5 to +11.3) | -2.8% (-13.5 to +7.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 461.9 | 381.1 | -17.5% (-49.3 to +14.3) | -6.0% (-20.7 to +8.7) | -3.2% (-10.8 to +4.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 656,468 | 895,813 | +36.5% (-32.5 to +105.5) | +9.5% (-29.0 to +47.9) | -1.3% (-12.6 to +10.0) | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.102 | -2.1% (-14.2 to +10.1) | -0.8% (-3.7 to +2.2) | -0.5% (-1.7 to +0.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 186.8 | 182.9 | -2.1% (-14.2 to +10.0) | -0.6% (-3.6 to +2.3) | -0.4% (-1.6 to +0.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 1.38 | 1.35 | -2.2% (-13.4 to +9.1) | -0.8% (-4.4 to +2.8) | -0.4% (-0.9 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 | +11.7 (+6.5 to +16.8) | +17 (+12.7 to +21.3) | +18.7 (+12.4 to +24.9) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (6 trials, 2 allowed, 2 refused); acting: 384 to 512 (7 trials, 1 allowed, 3 refused); acting: 256 to 512 (6 trials, 2 allowed, 3 refused); run B: acting: 256 to 512 (9 trials, 2 allowed, 3 refused); left native (13 trials, 0 allowed, 4 refused); acting: 384 to 512 (10 trials, 1 allowed, 4 refused); run C: acting: 384 to 512 (12 trials, 1 allowed, 5 refused); left native (13 trials, 0 allowed, 4 refused); acting: 384 to 512 (10 trials, 1 allowed, 4 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 186.3 | 186.9 | +0.3% (-2.0 to +2.6) | -0.1% (-0.9 to +0.8) | -0.3% (-1.8 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 195.7 | 195.5 | -0.1% (-1.3 to +1.2) | -0.1% (-1.3 to +1.1) | -0.4% (-1.2 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,913 | 3,910 | -0.1% (-1.3 to +1.2) | -0.1% (-1.3 to +1.1) | -0.4% (-1.2 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 10.6 | 10.2 | -3.6% (-19.2 to +12.0) | -1.8% (-9.5 to +5.9) | -0.6% (-10.0 to +8.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 199.5 | 163.3 | -18.2% (-96.7 to +60.4) | +0.6% (-6.3 to +7.5) | -2.9% (-17.1 to +11.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 9.46 | 8.25 | -12.8% (-54.5 to +28.9) | -1.3% (-3.4 to +0.8) | -1.8% (-9.3 to +5.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 541.6 | +5.8% (-3.3 to +14.8) | +3.8% (+2.1 to +5.6) | +2.9% (-16.7 to +22.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 460.8 | 485.0 | +5.2% (-1.6 to +12.1) | +2.8% (-0.1 to +5.6) | +1.4% (-13.6 to +16.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 615,152 | 554,486 | -9.9% (-33.3 to +13.6) | -6.2% (-12.4 to +0.0) | -3.0% (-28.6 to +22.7) | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.4% (-2.0 to -0.8) | -1.5% (-4.1 to +1.0) | -3.1% (-15.7 to +9.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 389.3 | 383.9 | -1.4% (-2.1 to -0.7) | -1.5% (-3.9 to +0.9) | -3.0% (-15.7 to +9.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 4.54 | 4.46 | -1.7% (-4.7 to +1.2) | -1.4% (-4.7 to +1.8) | -2.8% (-15.9 to +10.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 19.0 | +19 (+7.62 to +30.4) | +16.3 (+8.74 to +23.9) | +18 (+9.39 to +26.6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 640 (12 trials, 2 allowed, 4 refused); acting: 384 to 640 (13 trials, 2 allowed, 4 refused); left native (12 trials, 0 allowed, 4 refused); run B: left native (12 trials, 0 allowed, 4 refused); left native (11 trials, 0 allowed, 4 refused); acting: 384 to 640 (13 trials, 2 allowed, 4 refused); run C: acting: 384 to 640 (10 trials, 2 allowed, 4 refused); acting: 384 to 512 (12 trials, 1 allowed, 4 refused); left native (10 trials, 0 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 | +0 (+0 to +0) | -1.2% (-26.1 to +23.7) | +2.5% (-235.8 to +240.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 976.8 | 977.7 | +0.1% (-0.2 to +0.3) | -0.2% (-0.4 to +0.0) | +0.2% (-0.1 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 976.8 | 977.7 | +0.1% (-0.2 to +0.3) | -0.2% (-0.4 to +0.0) | +0.2% (-0.1 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 2.3 | 2.17 | -5.8% (-38.0 to +26.4) | +4.5% (-3.7 to +12.6) | -14.7% (-39.9 to +10.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 110.6 | 34.0 | -69.3% (-450.0 to +311.4) | +9.5% (-20.2 to +39.2) | -9.3% (-53.8 to +35.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 5.07 | 3.08 | -39.4% (-253.0 to +174.3) | +3.9% (-6.6 to +14.4) | -7.1% (-28.4 to +14.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 533.1 | +4.1% (-5.4 to +13.6) | -6.7% (-19.1 to +5.7) | -2.5% (-13.7 to +8.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 453.0 | 459.5 | +1.4% (-4.8 to +7.7) | -12.2% (-33.0 to +8.5) | -5.4% (-15.7 to +4.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 188,442 | 183,843 | -2.4% (-13.2 to +8.3) | +18.5% (-17.1 to +54.0) | +6.2% (-14.3 to +26.8) | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.202 | -2.2% (-11.8 to +7.4) | +23.1% (-62.4 to +108.6) | -8.7% (-31.4 to +14.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 368.0 | 360.0 | -2.2% (-11.9 to +7.5) | +23.4% (-63.7 to +110.6) | -8.5% (-30.8 to +13.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 367,983 | 360,007 | -2.2% (-11.9 to +7.5) | +24.0% (-47.9 to +95.9) | -11.0% (-257.1 to +235.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 | +16.7 (+6.63 to +26.7) | +21.3 (+2.36 to +40.3) | +16 (+13.5 to +18.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 512 to 640 (16 trials, 1 allowed, 3 refused); left native (16 trials, 0 allowed, 4 refused); left native (16 trials, 0 allowed, 3 refused); run B: acting: 256 to 640 (15 trials, 3 allowed, 4 refused); left native (13 trials, 0 allowed, 2 refused); acting: 256 to 512 (11 trials, 2 allowed, 4 refused); run C: acting: 384 to 512 (16 trials, 1 allowed, 3 refused); acting: 256 to 512 (13 trials, 2 allowed, 4 refused); left native (16 trials, 0 allowed, 4 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 48 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
