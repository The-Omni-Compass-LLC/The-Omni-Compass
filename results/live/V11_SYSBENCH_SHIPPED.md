# sysbench on MySQL, a database's buffer pool as shipped: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native (`docs/MYSQL_PREREGISTRATION.md`, amendment 5); omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39150486066 | `c1c1b59711b1` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| B | 39159004803 | `3cb376bb3284` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| C | 39167578494 | `e2d5958834f5` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,964 | 2,960 | -0.1% (-0.2 to -0.1) | -0.1% (-0.8 to +0.5) | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 2,968 | 2,965 | -0.1% (-0.4 to +0.1) | -0.1% (-0.5 to +0.3) | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,968 | 2,965 | -0.1% (-0.4 to +0.1) | -0.1% (-0.5 to +0.3) | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.192 | 0.194 | +1.4% (-55.4 to +58.1) | +1.2% (-16.0 to +18.4) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.312 | 0.311 | -0.5% (-7.4 to +6.3) | +2.5% (-9.1 to +14.0) | +0.6% (-1.9 to +3.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.0904 | 0.0879 | -2.7% (-23.6 to +18.2) | +2.9% (-8.6 to +14.5) | -0.4% (-1.2 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 135.4 | +5.8% (-2.1 to +13.6) | +8.7% (+0.6 to +16.7) | +8.1% (+3.2 to +13.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 121.2 | 132.5 | +9.3% (-2.4 to +21.0) | +10.4% (-1.7 to +22.4) | +10.6% (+6.0 to +15.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 1,029,216 | 1,011,793 | -1.7% (-4.2 to +0.8) | -2.9% (-4.5 to -1.4) | -3.3% (-6.5 to -0.2) | shown, not judged |
| host CPU busy (share of the run) | 0.0695 | 0.0679 | -2.2% (-25.7 to +21.3) | +3.4% (-9.0 to +15.8) | -0.7% (-1.9 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 124.5 | 121.7 | -2.2% (-25.8 to +21.3) | +3.3% (-8.7 to +15.3) | -0.8% (-2.0 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.0923 | 0.0903 | -2.1% (-25.6 to +21.5) | +3.4% (-9.1 to +15.9) | -0.8% (-1.7 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 | +4.67 (+1.8 to +7.54) | +7.33 (+4.46 to +10.2) | +6 (+6 to +6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 3 refused); run B: left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 3 refused); run C: left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.2 | 293.2 | -0.0% (-1.4 to +1.4) | +0.2% (-1.0 to +1.4) | -0.0% (-1.0 to +0.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 293.8 | 293.7 | -0.0% (-1.5 to +1.4) | +0.2% (-0.9 to +1.3) | +0.0% (-0.9 to +0.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,700 | 4,699 | -0.0% (-1.5 to +1.4) | +0.2% (-0.9 to +1.3) | +0.0% (-0.9 to +0.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.09 | 5.12 | +0.6% (-2.0 to +3.2) | +0.0% (+0.0 to +0.0) | +0.0% (-4.5 to +4.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 6.79 | 6.83 | +0.6% (-4.5 to +5.8) | +0.0% (-4.5 to +4.5) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.38 | 3.37 | -0.3% (-1.8 to +1.2) | -0.7% (-3.4 to +2.1) | -0.5% (-1.0 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 137.6 | +7.5% (-0.1 to +15.0) | +7.5% (-1.0 to +15.9) | +7.8% (+1.4 to +14.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 120.2 | 134.9 | +12.2% (+8.6 to +15.8) | +10.4% (+1.5 to +19.2) | +13.0% (+8.1 to +18.0) | **power given in all three of our runs** |
| pages read from disk into the pool (misses) | 572,588 | 543,189 | -5.1% (-16.5 to +6.2) | -6.8% (-10.5 to -3.0) | -4.4% (-10.8 to +2.1) | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.201 | -0.2% (-2.5 to +2.1) | -1.3% (-4.9 to +2.2) | -0.7% (-2.4 to +1.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 112.0 | 111.7 | -0.3% (-2.5 to +1.9) | -1.6% (-5.6 to +2.5) | -0.7% (-2.5 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.49 | -0.2% (-1.2 to +0.7) | -1.7% (-6.6 to +3.2) | -0.7% (-2.9 to +1.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +2.67 (-0.202 to +5.54) | +3 (+0.516 to +5.48) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.9 | 294.5 | -0.1% (-1.1 to +0.8) | -0.1% (-0.6 to +0.3) | +0.1% (-1.6 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 295.0 | 294.7 | -0.1% (-1.1 to +0.8) | -0.1% (-0.6 to +0.4) | +0.1% (-1.6 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,720 | 4,715 | -0.1% (-1.1 to +0.8) | -0.1% (-0.6 to +0.4) | +0.1% (-1.6 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 4.1 | 4.13 | +0.6% (-2.0 to +3.2) | +0.6% (-1.9 to +3.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.54 | 5.5 | -0.6% (-3.1 to +1.9) | +2.4% (-10.7 to +15.5) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.24 | 3.24 | +0.0% (-2.2 to +2.2) | +2.1% (-3.4 to +7.7) | -0.6% (-0.8 to -0.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 138.7 | +8.3% (+1.5 to +15.2) | +8.2% (+3.2 to +13.3) | +8.7% (+6.2 to +11.2) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 120.0 | 137.0 | +14.1% (+9.5 to +18.7) | +15.8% (+11.6 to +20.0) | +14.1% (+10.7 to +17.6) | **power given in all three of our runs** |
| pages read from disk into the pool (misses) | 1,975,999 | 1,905,467 | -3.6% (-7.8 to +0.7) | -3.8% (-12.4 to +4.8) | -4.9% (-9.2 to -0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.202 | +0.0% (-4.1 to +4.1) | +2.7% (-4.0 to +9.3) | +0.0% (-3.1 to +3.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 336.0 | 336.0 | +0.0% (-4.2 to +4.2) | +2.7% (-4.1 to +9.4) | +0.1% (-3.2 to +3.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.49 | 2.49 | +0.1% (-3.9 to +4.1) | +2.8% (-3.5 to +9.0) | -0.0% (-1.6 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 | +7.33 (+4.46 to +10.2) | +6 (+6 to +6) | +8.33 (+6.9 to +9.77) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 3 refused); left native (5 trials, 0 allowed, 4 refused); run B: left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused); run C: left native (4 trials, 0 allowed, 4 refused); left native (5 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195.4 | 195.7 | +0.2% (-2.0 to +2.4) | -2.6% (-9.7 to +4.6) | +0.4% (-2.0 to +2.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 197.7 | 197.9 | +0.1% (-2.0 to +2.2) | -0.4% (-2.4 to +1.6) | +0.0% (-1.8 to +1.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,955 | 3,959 | +0.1% (-2.0 to +2.2) | -0.4% (-2.4 to +1.6) | +0.0% (-1.8 to +1.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 7.89 | 7.84 | -0.6% (-3.2 to +2.0) | +40.9% (-159.6 to +241.3) | -1.8% (-6.2 to +2.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 11.2 | 11.1 | -0.6% (-3.2 to +2.0) | +11.2% (-23.6 to +46.0) | -55.5% (-201.1 to +90.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.97 | 4.01 | +1.1% (-2.6 to +4.7) | +13.1% (-7.3 to +33.6) | -15.5% (-46.3 to +15.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 135.0 | +5.5% (+2.1 to +8.9) | +6.8% (+4.6 to +9.0) | +7.2% (+4.4 to +10.0) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 122.1 | 127.3 | +4.2% (+2.6 to +5.9) | +5.4% (+1.3 to +9.5) | +6.9% (+4.9 to +9.0) | **power given in all three of our runs** |
| pages read from disk into the pool (misses) | 1,670,787 | 1,639,449 | -1.9% (-8.4 to +4.6) | -3.5% (-8.4 to +1.4) | -2.3% (-6.4 to +1.7) | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.201 | +0.1% (-2.8 to +2.9) | -0.8% (-2.8 to +1.2) | +1.6% (-6.1 to +9.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 356.1 | 356.3 | +0.1% (-2.6 to +2.8) | -0.7% (-2.6 to +1.1) | +1.6% (-6.3 to +9.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 4 | 3.99 | -0.1% (-1.6 to +1.4) | +1.8% (-5.1 to +8.8) | +1.2% (-5.1 to +7.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 | +5.33 (+2.46 to +8.2) | +6.67 (+3.8 to +9.54) | +7.33 (+4.46 to +10.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 3 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 3 refused); run B: left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 4 refused); left native (3 trials, 0 allowed, 3 refused); run C: left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.08 | 2.2 | -28.5% (-75.6 to +18.6) | -14.0% (-79.2 to +51.3) | -10.9% (-52.5 to +30.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 983.9 | 981.7 | -0.2% (-0.6 to +0.1) | -0.0% (-0.7 to +0.6) | -0.1% (-0.8 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 983.9 | 981.7 | -0.2% (-0.6 to +0.1) | -0.0% (-0.7 to +0.6) | -0.1% (-0.8 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 2.32 | 2.66 | +14.5% (-67.8 to +96.8) | +2.9% (-59.7 to +65.6) | +4.2% (-21.4 to +29.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 4.03 | 4.8 | +19.1% (-110.8 to +149.0) | +1.9% (-69.0 to +72.8) | +11.1% (-49.2 to +71.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.22 | 1.3 | +6.4% (-37.8 to +50.6) | +0.7% (-33.9 to +35.2) | +3.4% (-7.7 to +14.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 158.8 | +24.1% (-30.0 to +78.1) | +31.8% (-69.3 to +132.9) | +9.0% (+4.0 to +14.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 118.3 | 140.8 | +19.0% (-35.8 to +73.8) | +27.8% (-70.0 to +125.5) | +7.7% (+1.6 to +13.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 416,099 | 393,476 | -5.4% (-17.5 to +6.6) | -6.7% (-27.5 to +14.1) | -1.8% (-3.2 to -0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.266 | +30.8% (-114.9 to +176.4) | +23.7% (-155.0 to +202.4) | +5.3% (-31.5 to +42.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 313.7 | 412.5 | +31.5% (-116.9 to +179.9) | +23.9% (-156.3 to +204.1) | +5.3% (-31.5 to +42.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 251.3 | 432.0 | +71.9% (-170.4 to +314.2) | +13.3% (-230.1 to +256.6) | +12.1% (-68.2 to +92.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 | +10.7 (+7.8 to +13.5) | +8.67 (+2.93 to +14.4) | +8 (+8 to +8) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (5 trials, 0 allowed, 5 refused); left native (5 trials, 0 allowed, 5 refused); acting: 128 to 256 (7 trials, 1 allowed, 4 refused); run B: left native (3 trials, 0 allowed, 3 refused); acting: 128 to 256 (5 trials, 1 allowed, 3 refused); left native (5 trials, 0 allowed, 5 refused); run C: left native (4 trials, 0 allowed, 4 refused); left native (5 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 5 power given, 43 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
