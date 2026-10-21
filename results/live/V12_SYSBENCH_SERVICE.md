# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39468576581 | `80843e7684b3` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| B | 39473186537 | `ac0eeaef8ecc` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| C | 39477834359 | `fb90309cad0d` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,955 | 2,949 | -0.2% (-0.7 to +0.3) | +0.1% (-0.1 to +0.4) | +0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,965 | 2,964 | -0.0% (-0.1 to +0.1) | +0.1% (+0.0 to +0.2) | +0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queries a second | 2,965 | 2,964 | -0.0% (-0.1 to +0.1) | +0.1% (+0.0 to +0.2) | +0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.213 | 0.221 | +3.6% (-8.5 to +15.7) | -0.2% (-7.8 to +7.5) | -3.0% (-5.6 to -0.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 0.35 | 0.365 | +4.4% (-8.8 to +17.5) | +0.0% (+0.0 to +0.0) | -2.4% (-5.0 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.254 | 0.273 | +7.9% (-32.6 to +48.3) | +9.8% (-27.2 to +46.7) | +1.4% (-4.3 to +7.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 510.9 | -0.2% (-14.2 to +13.8) | -11.4% (-29.0 to +6.2) | +16.6% (-10.3 to +43.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 463.4 | 464.4 | +0.2% (-12.8 to +13.2) | -10.8% (-31.6 to +10.0) | +14.4% (-1.7 to +30.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 367,299 | 353,785 | -3.7% (-24.5 to +17.1) | +19.6% (-21.7 to +61.0) | -25.7% (-54.5 to +3.1) | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.114 | +3.7% (+0.9 to +6.6) | +1.0% (+0.1 to +2.0) | -1.2% (-4.5 to +2.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| host CPU-seconds | 194.9 | 202.4 | +3.9% (+1.0 to +6.7) | +1.0% (+0.2 to +1.9) | -1.2% (-4.5 to +2.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.151 | +3.9% (+0.6 to +7.3) | +0.9% (-0.1 to +1.9) | -1.2% (-4.7 to +2.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 7 | +7 (+0.427 to +13.6) | +10 (+3.43 to +16.6) | +10.7 (+5.5 to +15.8) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 640 (7 trials, 2 allowed, 2 refused); acting: 384 to 512 (3 trials, 1 allowed, 1 refused); acting: 384 to 768 (5 trials, 3 allowed, 1 refused); run B: acting: 384 to 640 (5 trials, 2 allowed, 2 refused); acting: 384 to 768 (7 trials, 3 allowed, 3 refused); acting: 384 to 512 (4 trials, 1 allowed, 2 refused); run C: acting: 384 to 768 (8 trials, 3 allowed, 2 refused); acting: 512 to 640 (7 trials, 1 allowed, 2 refused); acting: 512 to 896 (6 trials, 3 allowed, 2 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.5 | 292.4 | -0.4% (-1.1 to +0.4) | -0.3% (-1.3 to +0.7) | -0.5% (-1.5 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 294.8 | 293.7 | -0.4% (-1.1 to +0.3) | -0.3% (-1.4 to +0.9) | -0.4% (-1.6 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,718 | 4,699 | -0.4% (-1.1 to +0.3) | -0.3% (-1.4 to +0.9) | -0.4% (-1.6 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.25 | 5.28 | +0.6% (-6.2 to +7.4) | -1.2% (-15.5 to +13.1) | -1.2% (-6.2 to +3.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 7.39 | 7.34 | -0.6% (-3.2 to +2.0) | +0.7% (-29.4 to +30.7) | -0.6% (-3.2 to +2.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.36 | 3.36 | +0.1% (-2.4 to +2.6) | +0.4% (-13.5 to +14.3) | -0.5% (-5.7 to +4.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 520.4 | +1.6% (-12.2 to +15.4) | -8.9% (-13.2 to -4.5) | -3.1% (-6.1 to -0.2) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 447.9 | 433.9 | -3.1% (-22.7 to +16.5) | -10.5% (-22.0 to +1.0) | -13.2% (-14.6 to -11.9) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 245,612 | 235,727 | -4.0% (-27.2 to +19.2) | +4.5% (-8.4 to +17.4) | +5.3% (+4.7 to +5.9) | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.196 | +0.6% (-3.2 to +4.3) | +1.3% (+0.3 to +2.4) | -0.4% (-5.1 to +4.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 107.5 | 108.3 | +0.7% (-3.3 to +4.7) | +1.3% (+0.3 to +2.4) | -0.4% (-5.2 to +4.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.42 | +1.1% (-2.9 to +5.1) | +1.6% (-0.4 to +3.6) | +0.1% (-4.9 to +5.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 7 | +7 (+4.52 to +9.48) | +6 (+1.03 to +11) | +6 (+1.03 to +11) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (7 trials, 0 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); acting: 512 to 640 (5 trials, 1 allowed, 1 refused); run B: acting: 384 to 512 (5 trials, 1 allowed, 0 refused); left native (5 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (4 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.6 | 294.5 | +0.7% (-0.8 to +2.1) | +0.1% (-0.8 to +0.9) | -0.1% (-1.3 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 295.5 | 296.2 | +0.3% (-1.1 to +1.6) | +0.1% (-1.1 to +1.3) | -0.0% (-1.2 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,727 | 4,740 | +0.3% (-1.1 to +1.6) | +0.1% (-1.1 to +1.3) | -0.0% (-1.2 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.09 | 3.07 | -0.6% (-3.1 to +2.0) | -3.5% (-11.1 to +4.1) | -1.2% (-3.8 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 11.3 | 5.74 | -49.3% (-230.7 to +132.1) | -3.4% (-85.0 to +78.2) | -0.6% (-7.4 to +6.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.81 | 2.57 | -8.7% (-20.2 to +2.8) | +1.1% (-35.8 to +38.0) | -0.2% (-0.8 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 555.2 | +8.4% (-12.5 to +29.4) | +2.2% (-6.3 to +10.7) | +14.2% (-10.6 to +39.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 462.3 | 490.7 | +6.1% (-17.5 to +29.7) | +2.3% (-5.2 to +9.9) | +12.0% (-8.9 to +32.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 655,415 | 557,458 | -14.9% (-53.7 to +23.8) | -9.8% (-25.1 to +5.6) | -24.1% (-64.8 to +16.7) | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.188 | +0.8% (-1.0 to +2.5) | -1.9% (-7.4 to +3.7) | +0.1% (-1.6 to +1.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 333.8 | 336.2 | +0.7% (-1.0 to +2.4) | -1.9% (-7.4 to +3.7) | +0.2% (-1.5 to +1.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.5 | +0.1% (-0.7 to +0.9) | -1.9% (-8.0 to +4.2) | +0.3% (-0.3 to +0.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 | +14.3 (+9.16 to +19.5) | +14.7 (+7.08 to +22.3) | +18.7 (+4.11 to +33.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (12 trials, 1 allowed, 3 refused); acting: 512 to 640 (9 trials, 1 allowed, 3 refused); acting: 512 to 896 (8 trials, 3 allowed, 2 refused); run B: acting: 512 to 640 (10 trials, 1 allowed, 3 refused); acting: 384 to 512 (9 trials, 1 allowed, 4 refused); acting: 384 to 640 (8 trials, 2 allowed, 3 refused); run C: acting: 384 to 640 (12 trials, 2 allowed, 3 refused); acting: 512 to 896 (16 trials, 3 allowed, 2 refused); acting: 512 to 640 (12 trials, 1 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.6 | 191.8 | +0.1% (-1.6 to +1.8) | -1.4% (-9.8 to +6.9) | +0.9% (-2.0 to +3.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 196.3 | 195.8 | -0.2% (-1.0 to +0.5) | +0.1% (-0.7 to +0.9) | +0.7% (-0.1 to +1.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,925 | 3,916 | -0.2% (-1.0 to +0.5) | +0.1% (-0.7 to +0.9) | +0.7% (-0.1 to +1.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 8.64 | 8.28 | -4.1% (-16.8 to +8.5) | +61.1% (-142.2 to +264.4) | -2.4% (-17.9 to +13.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 12.8 | 12.4 | -3.6% (-12.4 to +5.3) | +66.7% (-258.5 to +391.9) | +3.8% (-45.7 to +53.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 5.28 | 5.18 | -1.9% (-7.3 to +3.4) | +23.1% (-77.1 to +123.3) | +1.1% (-21.1 to +23.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 609.2 | +19.0% (+6.3 to +31.7) | +8.4% (-17.5 to +34.3) | +16.7% (+5.5 to +27.9) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 462.0 | 513.6 | +11.2% (+3.0 to +19.3) | +8.0% (-16.6 to +32.5) | +13.7% (+9.7 to +17.7) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 612,637 | 505,974 | -17.4% (-24.9 to -10.0) | -11.5% (-53.7 to +30.6) | -22.7% (-29.1 to -16.3) | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.276 | -2.6% (-5.6 to +0.4) | +1.3% (-9.3 to +11.9) | -1.0% (-3.2 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 497.9 | 485.1 | -2.6% (-5.5 to +0.4) | +1.3% (-9.2 to +11.8) | -1.0% (-3.2 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 5.67 | 5.52 | -2.7% (-7.1 to +1.8) | +2.8% (-8.4 to +14.1) | -1.9% (-3.2 to -0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 18.0 | +18 (+9.04 to +27) | +15 (+12.5 to +17.5) | +16.3 (+9.16 to +23.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 768 (12 trials, 3 allowed, 3 refused); acting: 512 to 768 (12 trials, 2 allowed, 3 refused); acting: 384 to 896 (14 trials, 4 allowed, 3 refused); run B: acting: 384 to 768 (10 trials, 3 allowed, 3 refused); acting: 384 to 640 (8 trials, 2 allowed, 3 refused); acting: 384 to 768 (11 trials, 3 allowed, 2 refused); run C: acting: 512 to 640 (12 trials, 1 allowed, 3 refused); acting: 512 to 896 (11 trials, 3 allowed, 2 refused); acting: 512 to 640 (12 trials, 1 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 157.6 | 192.1 | +21.9% (-27.2 to +71.1) | +12.0% (-11.7 to +35.6) | -4.7% (-60.3 to +51.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 986.9 | 988.8 | +0.2% (-0.3 to +0.6) | -0.1% (-0.3 to +0.2) | -0.2% (-0.8 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 986.9 | 988.8 | +0.2% (-0.3 to +0.6) | -0.1% (-0.3 to +0.2) | -0.2% (-0.8 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 2.53 | 2.48 | -1.8% (-9.6 to +5.9) | +2.4% (-12.4 to +17.1) | -4.3% (-52.1 to +43.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 4.88 | 4.89 | +0.1% (-19.8 to +20.1) | +16.0% (-276.4 to +308.4) | -13.4% (-90.9 to +64.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.02 | 1.05 | +2.3% (-13.7 to +18.2) | +2.1% (-60.8 to +64.9) | -6.5% (-30.4 to +17.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 450.5 | -12.0% (-39.3 to +15.3) | -6.4% (-13.3 to +0.5) | -13.3% (-44.1 to +17.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 452.3 | 381.0 | -15.8% (-39.0 to +7.5) | -9.8% (-11.7 to -8.0) | -15.2% (-45.0 to +14.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 189,589 | 234,966 | +23.9% (-26.8 to +74.7) | +14.2% (+1.2 to +27.2) | +29.7% (-38.6 to +97.9) | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.123 | -3.2% (-13.8 to +7.3) | -2.5% (-14.7 to +9.7) | -0.4% (-17.3 to +16.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 223.7 | 216.5 | -3.2% (-13.8 to +7.4) | -2.5% (-14.5 to +9.6) | -0.4% (-17.2 to +16.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 2.51 | -19.3% (-54.4 to +15.8) | -15.4% (-61.2 to +30.4) | -1.0% (-84.7 to +82.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 16.0 | +16 (+9.43 to +22.6) | +15 (+8.43 to +21.6) | +14.7 (+7.49 to +21.8) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 384 to 512 (9 trials, 1 allowed, 3 refused); acting: 128 to 512 (7 trials, 3 allowed, 2 refused); acting: 256 to 640 (9 trials, 3 allowed, 5 refused); run B: acting: 256 to 640 (11 trials, 3 allowed, 3 refused); acting: 256 to 640 (12 trials, 3 allowed, 1 refused); acting: 384 to 512 (10 trials, 1 allowed, 4 refused); run C: acting: 512 to 640 (9 trials, 1 allowed, 3 refused); acting: 128 to 640 (7 trials, 4 allowed, 2 refused); acting: 128 to 640 (7 trials, 4 allowed, 2 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 48 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
