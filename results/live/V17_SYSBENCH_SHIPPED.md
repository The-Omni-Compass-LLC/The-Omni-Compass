# sysbench on MySQL, a database's buffer pool as shipped: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native (`docs/MYSQL_PREREGISTRATION.md`, amendment 5); omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40005917048 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| B | 40024472453 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| C | 40038796458 | `d02c7052ae50` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,941 | 2,938 | -0.1% (-0.2 to -0.0) | -0.1% (-0.4 to +0.3) | -0.0% (-0.6 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 2,954 | 2,949 | -0.2% (-0.3 to -0.0) | -0.0% (-0.2 to +0.2) | -0.0% (-0.6 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queries a second | 2,954 | 2,949 | -0.2% (-0.3 to -0.0) | -0.0% (-0.2 to +0.2) | -0.0% (-0.6 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.357 | 0.34 | -4.7% (-11.4 to +2.1) | +1.2% (-5.5 to +8.0) | -1.9% (-16.7 to +13.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.53 | 0.52 | -1.8% (-9.7 to +6.0) | +2.4% (-8.0 to +12.9) | -0.5% (-6.9 to +6.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.215 | 0.209 | -3.0% (-6.1 to +0.1) | +0.5% (-2.7 to +3.7) | -1.4% (-8.2 to +5.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 134.6 | +5.2% (+2.5 to +7.8) | +4.6% (+1.8 to +7.4) | +6.2% (+0.9 to +11.6) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 121.3 | 129.7 | +7.0% (+1.1 to +12.8) | +7.8% (+2.5 to +13.1) | +8.0% (-2.6 to +18.6) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 1,029,843 | 1,005,526 | -2.4% (-3.6 to -1.1) | -1.7% (-2.6 to -0.8) | -2.3% (-5.0 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.108 | -3.9% (-7.0 to -0.9) | +0.2% (-2.3 to +2.7) | -1.2% (-8.1 to +5.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 187.7 | 180.3 | -3.9% (-6.9 to -1.0) | +0.2% (-2.3 to +2.7) | -1.2% (-8.1 to +5.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.134 | -3.8% (-6.8 to -0.8) | +0.3% (-2.5 to +3.0) | -1.2% (-7.7 to +5.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 | +5.33 (+2.46 to +8.2) | +4.67 (+1.8 to +7.54) | +3.67 (+2.23 to +5.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 3 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 3 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.7 | 293.0 | +0.1% (-1.0 to +1.1) | +0.3% (-0.9 to +1.6) | -0.6% (-2.1 to +1.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 294.0 | 294.4 | +0.1% (-0.9 to +1.2) | +0.3% (-0.8 to +1.4) | -0.8% (-1.4 to -0.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queries a second | 4,704 | 4,710 | +0.1% (-0.9 to +1.2) | +0.3% (-0.8 to +1.4) | -0.8% (-1.4 to -0.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.31 | 5.28 | -0.6% (-3.2 to +2.0) | -1.2% (-3.8 to +1.4) | -5.0% (-30.9 to +20.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 7.21 | 7.21 | +0.0% (-4.5 to +4.5) | -1.2% (-8.0 to +5.6) | -7.7% (-44.6 to +29.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.44 | 3.42 | -0.8% (-2.2 to +0.7) | -1.1% (-2.2 to -0.0) | -3.6% (-26.2 to +19.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 146.6 | +14.6% (+0.0 to +29.1) | +8.4% (+1.3 to +15.5) | +3.9% (-4.5 to +12.4) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 120.4 | 142.1 | +18.0% (-0.6 to +36.6) | +13.4% (+12.3 to +14.5) | +4.8% (-5.2 to +14.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 583,300 | 534,041 | -8.4% (-19.7 to +2.8) | -4.8% (-12.2 to +2.7) | -3.5% (-17.1 to +10.1) | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.205 | -0.4% (-3.0 to +2.1) | -1.0% (-5.4 to +3.3) | -0.3% (-14.5 to +13.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 114.7 | 114.1 | -0.5% (-3.0 to +2.1) | -1.2% (-5.7 to +3.3) | -0.3% (-14.6 to +14.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.55 | -0.6% (-2.1 to +0.9) | -1.5% (-5.0 to +2.0) | +0.3% (-14.8 to +15.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3 (+0.516 to +5.48) | +1.33 (-1.54 to +4.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.6 | 295.1 | +0.2% (-1.6 to +2.0) | -0.1% (-1.3 to +1.0) | -0.1% (-0.9 to +0.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 294.8 | 295.3 | +0.2% (-1.6 to +2.0) | -0.1% (-1.2 to +1.0) | -0.2% (-1.1 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,716 | 4,724 | +0.2% (-1.6 to +2.0) | -0.1% (-1.2 to +1.0) | -0.2% (-1.1 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 4.2 | 4.15 | -1.2% (-3.8 to +1.4) | -3.0% (-9.7 to +3.8) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.57 | 5.44 | -2.4% (-5.0 to +0.3) | -1.8% (-1.9 to -1.7) | -1.2% (-18.0 to +15.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 3.3 | 3.28 | -0.8% (-1.1 to -0.5) | -2.7% (-9.0 to +3.7) | -24.6% (-146.3 to +97.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 138.5 | +8.2% (+1.2 to +15.1) | +5.8% (+5.5 to +6.1) | +7.6% (+3.5 to +11.6) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 120.1 | 136.4 | +13.6% (+4.8 to +22.4) | +12.0% (+10.3 to +13.8) | +11.9% (+5.9 to +17.9) | **power given in all three of our runs** |
| pages read from disk into the pool (misses) | 1,979,103 | 1,897,963 | -4.1% (-5.8 to -2.4) | -2.4% (-9.7 to +4.9) | -3.1% (-9.5 to +3.2) | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.205 | -0.5% (-2.3 to +1.3) | -2.6% (-8.8 to +3.7) | -0.1% (-1.7 to +1.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 344.7 | 342.9 | -0.5% (-2.4 to +1.4) | -2.5% (-8.7 to +3.6) | -0.1% (-1.8 to +1.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.54 | -0.7% (-2.5 to +1.1) | -2.4% (-8.6 to +3.8) | -0.0% (-0.7 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 | +7.33 (+4.46 to +10.2) | +6 (+6 to +6) | +6.67 (+3.8 to +9.54) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (4 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 4 refused); left native (5 trials, 0 allowed, 4 refused); run B: left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused); run C: left native (4 trials, 0 allowed, 4 refused); left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 177.8 | 178.5 | +0.4% (-1.4 to +2.2) | -0.4% (-2.3 to +1.5) | -0.2% (-0.9 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 196.2 | 196.1 | -0.0% (-0.8 to +0.7) | -0.1% (-1.7 to +1.6) | -0.4% (-0.9 to -0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queries a second | 3,923 | 3,922 | -0.0% (-0.8 to +0.7) | -0.1% (-1.7 to +1.6) | -0.4% (-0.9 to -0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 13.1 | 12.9 | -1.1% (-12.2 to +10.0) | +1.2% (-1.4 to +3.8) | -2.4% (-4.9 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 18.6 | 18.0 | -3.4% (-14.8 to +8.0) | +3.7% (-5.6 to +12.9) | -1.8% (-9.5 to +5.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 6.56 | 6.46 | -1.5% (-9.2 to +6.1) | +8.3% (-25.8 to +42.5) | -1.0% (-2.6 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 141.5 | +10.6% (+9.0 to +12.1) | +10.3% (+7.7 to +13.0) | +10.4% (+8.1 to +12.6) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 121.8 | 134.1 | +10.1% (+9.0 to +11.2) | +10.0% (+4.6 to +15.4) | +10.0% (+2.6 to +17.4) | **power given in all three of our runs** |
| pages read from disk into the pool (misses) | 1,665,825 | 1,591,692 | -4.5% (-9.4 to +0.5) | -3.8% (-5.4 to -2.3) | -4.2% (-7.2 to -1.2) | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.26 | -2.4% (-11.9 to +7.1) | -0.3% (-5.5 to +4.9) | -1.1% (-2.4 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 429.4 | 419.3 | -2.4% (-11.6 to +6.8) | -0.1% (-5.3 to +5.1) | -1.1% (-2.3 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 5.27 | 5.13 | -2.7% (-13.4 to +8.1) | +0.3% (-5.8 to +6.4) | -0.9% (-2.7 to +1.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 | +10.3 (+8.9 to +11.8) | +10.7 (+7.8 to +13.5) | +10.7 (+7.8 to +13.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (6 trials, 0 allowed, 5 refused); left native (6 trials, 0 allowed, 5 refused); left native (6 trials, 0 allowed, 5 refused); run B: left native (5 trials, 0 allowed, 5 refused); left native (5 trials, 0 allowed, 5 refused); left native (6 trials, 0 allowed, 6 refused); run C: left native (5 trials, 0 allowed, 5 refused); left native (6 trials, 0 allowed, 5 refused); left native (6 trials, 0 allowed, 6 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 109.3 | 94.5 | -13.5% (-75.3 to +48.2) | -17.6% (-45.8 to +10.6) | -1.5% (-51.7 to +48.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 988.5 | 988.0 | -0.1% (-0.4 to +0.3) | -0.1% (-0.5 to +0.4) | +0.0% (-0.5 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 988.5 | 988.0 | -0.1% (-0.4 to +0.3) | -0.1% (-0.5 to +0.4) | +0.0% (-0.5 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 186.5 | 137.8 | -26.1% (-165.6 to +113.4) | +34.8% (-43.8 to +113.3) | -5.1% (-24.5 to +14.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 771.5 | 273.1 | -64.6% (-290.4 to +161.2) | +70.7% (-182.3 to +323.8) | -11.8% (-67.3 to +43.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 40.8 | 24.6 | -39.7% (-217.7 to +138.2) | +32.7% (-29.3 to +94.7) | +4.1% (+1.2 to +6.9) | EVEN, no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 144.1 | +12.6% (+8.0 to +17.1) | +25.3% (-13.9 to +64.4) | +7.9% (+3.8 to +12.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 118.8 | 129.4 | +8.9% (+3.6 to +14.2) | +21.9% (-10.7 to +54.6) | +4.2% (-0.4 to +8.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 418,440 | 408,999 | -2.3% (-4.7 to +0.2) | -5.8% (-17.2 to +5.6) | -1.3% (-2.9 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.161 | -1.1% (-15.2 to +13.1) | +6.7% (-3.4 to +16.8) | -1.8% (-11.6 to +7.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 287.7 | 284.8 | -1.0% (-14.9 to +12.9) | +7.1% (-2.6 to +16.8) | -1.7% (-11.1 to +7.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 6.57 | 6.74 | +2.6% (-76.9 to +82.1) | +32.0% (-27.9 to +91.9) | -4.2% (-47.7 to +39.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 8 | +8 (+8 to +8) | +11 (+2.04 to +20) | +7 (+2.7 to +11.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); run B: acting: 128 to 256 (7 trials, 1 allowed, 4 refused); left native (5 trials, 0 allowed, 5 refused); left native (4 trials, 0 allowed, 4 refused); run C: left native (5 trials, 0 allowed, 4 refused); left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 4 power given, 44 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
