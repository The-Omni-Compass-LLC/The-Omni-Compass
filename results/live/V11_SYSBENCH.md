# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149259396 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| B | 39157795408 | `5031411ae285` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| C | 39166382450 | `8472aaad2bf4` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,948 | -0.0% (-0.2 to +0.1) | +0.1% (-0.1 to +0.2) | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,955 | 2,954 | -0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,955 | 2,954 | -0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.334 | 0.328 | -1.8% (-22.2 to +18.7) | -4.6% (-10.7 to +1.4) | -1.2% (-3.7 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.456 | 0.443 | -3.0% (-16.6 to +10.6) | -4.1% (-6.3 to -1.8) | -1.7% (-1.7 to -1.7) | EVEN, no difference beyond the noise (1 of 3 runs) |
| latency, mean (ms) | 0.204 | 0.204 | +0.2% (-14.9 to +15.2) | -2.4% (-4.8 to -0.0) | -0.2% (-5.4 to +5.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 437.3 | -14.6% (-33.2 to +4.1) | -4.0% (-23.0 to +15.0) | -12.0% (-19.4 to -4.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 463.6 | 393.9 | -15.0% (-31.2 to +1.1) | -5.0% (-21.4 to +11.5) | -10.9% (-20.1 to -1.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 367,361 | 473,934 | +29.0% (-20.9 to +78.9) | +6.4% (-30.9 to +43.7) | +17.8% (-6.1 to +41.7) | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.102 | -1.5% (-29.8 to +26.8) | -4.2% (-9.7 to +1.3) | +0.5% (-0.4 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 171.5 | 169.0 | -1.4% (-30.1 to +27.2) | -4.2% (-10.0 to +1.7) | +0.5% (-0.4 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.127 | 0.125 | -1.4% (-30.2 to +27.4) | -4.2% (-9.9 to +1.5) | +0.5% (-0.7 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 13.0 | +13 (+6.43 to +19.6) | +9 (+4.03 to +14) | +9.33 (+4.16 to +14.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (8 trials, 2 allowed, 3 refused); acting: 128 to 512 (7 trials, 3 allowed, 3 refused); acting: 256 to 512 (6 trials, 2 allowed, 2 refused); run B: left native (7 trials, 0 allowed, 2 refused); acting: 384 to 512 (6 trials, 1 allowed, 2 refused); acting: 384 to 512 (7 trials, 1 allowed, 3 refused); run C: acting: 256 to 512 (4 trials, 2 allowed, 1 refused); acting: 256 to 512 (5 trials, 2 allowed, 2 refused); acting: 256 to 512 (6 trials, 2 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295.2 | 295.8 | +0.2% (+0.1 to +0.3) | +0.4% (-0.4 to +1.1) | +0.3% (-0.9 to +1.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 295.6 | 296.4 | +0.3% (+0.2 to +0.3) | +0.3% (-0.5 to +1.0) | +0.0% (-0.6 to +0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queries a second | 4,730 | 4,742 | +0.3% (+0.2 to +0.3) | +0.3% (-0.5 to +1.0) | +0.0% (-0.6 to +0.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 2.9 | 2.86 | -1.2% (-3.8 to +1.4) | -4.1% (-6.7 to -1.5) | -1.2% (-10.4 to +8.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 4.49 | 4.6 | +2.4% (-4.4 to +9.1) | -4.7% (-7.3 to -2.1) | -88.4% (-413.2 to +236.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.36 | 1.38 | +1.6% (-7.2 to +10.5) | -1.9% (-5.6 to +1.8) | -38.2% (-147.9 to +71.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 403.4 | -21.2% (-67.2 to +24.8) | -6.5% (-24.1 to +11.1) | -7.4% (-44.9 to +30.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 443.8 | 356.2 | -19.7% (-69.8 to +30.3) | -10.1% (-26.7 to +6.6) | -4.0% (-48.0 to +40.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 242,730 | 285,543 | +17.6% (-23.7 to +59.0) | +5.2% (-17.1 to +27.6) | +3.9% (-32.2 to +40.0) | shown, not judged |
| host CPU busy (share of the run) | 0.099 | 0.1 | +1.2% (-2.7 to +5.1) | -0.7% (-7.6 to +6.1) | +0.5% (-2.6 to +3.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 59.4 | 60.1 | +1.2% (-2.7 to +5.1) | -0.7% (-7.5 to +6.1) | +0.5% (-2.9 to +3.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 1.32 | 1.34 | +1.0% (-2.7 to +4.7) | -1.0% (-7.1 to +5.0) | +0.2% (-4.2 to +4.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 | +4.33 (-1.4 to +10.1) | +8 (+5.52 to +10.5) | +6.33 (+2.54 to +10.1) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (3 trials, 1 allowed, 0 refused); acting: 384 to 512 (4 trials, 1 allowed, 1 refused); acting: 256 to 512 (3 trials, 2 allowed, 0 refused); run B: left native (6 trials, 0 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); run C: acting: 384 to 512 (5 trials, 1 allowed, 1 refused); acting: 384 to 512 (5 trials, 1 allowed, 0 refused); acting: 512 to 640 (6 trials, 1 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.5 | 294.1 | -0.2% (-1.3 to +1.0) | -0.1% (-0.8 to +0.6) | -0.5% (-1.8 to +0.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 294.7 | 294.2 | -0.2% (-1.3 to +1.0) | -0.1% (-0.7 to +0.6) | -0.5% (-1.7 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,715 | 4,708 | -0.2% (-1.3 to +1.0) | -0.1% (-0.7 to +0.6) | -0.5% (-1.7 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 4.15 | 4.05 | -2.4% (-4.9 to +0.2) | -2.4% (-4.9 to +0.1) | -4.7% (-7.1 to -2.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 5.6 | 5.5 | -1.8% (-6.1 to +2.6) | -3.0% (-5.5 to -0.4) | -3.5% (-7.8 to +0.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 3.21 | 3.17 | -1.1% (-3.3 to +1.1) | -1.4% (-2.8 to -0.0) | -2.8% (-4.2 to -1.3) | EVEN, no difference beyond the noise (1 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 549.1 | +7.2% (-10.9 to +25.4) | -0.3% (-18.5 to +17.9) | -5.4% (-34.8 to +23.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 461.6 | 492.0 | +6.6% (-12.4 to +25.6) | -1.7% (-24.8 to +21.5) | -5.6% (-38.3 to +27.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 654,463 | 538,468 | -17.7% (-53.6 to +18.2) | -2.1% (-53.2 to +49.0) | +7.7% (-52.6 to +68.1) | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.191 | -1.3% (-6.5 to +3.9) | -1.6% (-3.3 to +0.2) | -3.7% (-5.0 to -2.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 319.9 | 315.8 | -1.3% (-6.6 to +4.0) | -1.6% (-3.4 to +0.3) | -3.5% (-4.8 to -2.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.35 | -1.1% (-5.3 to +3.1) | -1.5% (-3.7 to +0.8) | -3.0% (-4.7 to -1.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 | +16.3 (+5.13 to +27.5) | +18.7 (+11.1 to +26.3) | +15.3 (+12.5 to +18.2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 512 to 640 (14 trials, 1 allowed, 3 refused); left native (12 trials, 0 allowed, 4 refused); acting: 512 to 640 (14 trials, 1 allowed, 3 refused); run B: acting: 384 to 640 (12 trials, 2 allowed, 3 refused); left native (14 trials, 0 allowed, 4 refused); acting: 512 to 640 (14 trials, 1 allowed, 2 refused); run C: acting: 384 to 512 (10 trials, 1 allowed, 4 refused); left native (13 trials, 0 allowed, 4 refused); acting: 384 to 512 (11 trials, 1 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196.7 | 195.3 | -0.7% (-2.3 to +0.9) | -0.4% (-7.3 to +6.4) | -0.1% (-12.3 to +12.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 198.3 | 197.7 | -0.3% (-1.6 to +1.0) | -0.9% (-2.2 to +0.5) | -0.1% (-1.4 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,965 | 3,954 | -0.3% (-1.6 to +1.0) | -0.9% (-2.2 to +0.5) | -0.1% (-1.4 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 4.8 | 5.34 | +11.4% (+6.9 to +15.9) | -3.6% (-57.6 to +50.4) | +0.2% (-76.5 to +76.9) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 9.48 | 12.3 | +30.1% (-9.4 to +69.7) | +6.5% (-136.3 to +149.4) | -6.3% (-35.8 to +23.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.65 | 2.86 | +7.8% (+7.2 to +8.5) | +0.4% (-37.7 to +38.5) | -4.9% (-52.1 to +42.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 398.1 | -22.2% (-35.8 to -8.7) | +13.5% (-13.3 to +40.2) | +11.9% (-6.5 to +30.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 462.3 | 358.6 | -22.4% (-38.5 to -6.3) | +11.3% (-12.1 to +34.7) | +11.3% (-8.9 to +31.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 617,540 | 873,710 | +41.5% (+27.4 to +55.5) | -18.9% (-58.0 to +20.1) | -18.7% (-42.7 to +5.3) | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.124 | +2.7% (-0.1 to +5.4) | -6.0% (-23.7 to +11.8) | -3.1% (-13.6 to +7.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 215.1 | 220.9 | +2.7% (-0.1 to +5.5) | -5.9% (-24.2 to +12.3) | -3.1% (-14.5 to +8.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.48 | +3.4% (+2.3 to +4.6) | -5.4% (-30.3 to +19.4) | -3.3% (-25.8 to +19.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 8 | +8 (-5.15 to +21.1) | +16 (+11 to +21) | +12.3 (+4.35 to +20.3) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 256 to 512 (3 trials, 2 allowed, 0 refused); acting: 256 to 512 (7 trials, 2 allowed, 2 refused); acting: 128 to 512 (5 trials, 3 allowed, 2 refused); run B: acting: 512 to 640 (14 trials, 1 allowed, 4 refused); acting: 512 to 768 (16 trials, 2 allowed, 3 refused); left native (14 trials, 0 allowed, 4 refused); run C: left native (14 trials, 0 allowed, 3 refused); acting: 512 to 640 (15 trials, 1 allowed, 2 refused); acting: 512 to 640 (15 trials, 1 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.76 | 6.23 | -7.9% (-131.1 to +115.3) | -16.3% (-96.7 to +64.2) | +1.9% (-27.5 to +31.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 982.9 | 982.8 | -0.0% (-0.2 to +0.1) | +0.3% (+0.2 to +0.3) | -0.4% (-0.6 to -0.1) | **the runs disagree** |
| queries a second | 982.9 | 982.8 | -0.0% (-0.2 to +0.1) | +0.3% (+0.2 to +0.3) | -0.4% (-0.6 to -0.1) | **the runs disagree** |
| latency, 95th percentile (ms) | 1.84 | 1.86 | +1.4% (-12.2 to +14.9) | +7.3% (-32.8 to +47.4) | -0.7% (-11.4 to +9.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 3.67 | 3.77 | +2.9% (-6.2 to +12.1) | +5.5% (-30.1 to +41.0) | +1.2% (-24.0 to +26.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.08 | 1.3 | +20.1% (-71.2 to +111.3) | -2.2% (-38.2 to +33.8) | -1.2% (-5.1 to +2.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 514.8 | +0.5% (-22.6 to +23.7) | -2.4% (-26.5 to +21.6) | -7.1% (-22.3 to +8.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 453.2 | 428.4 | -5.5% (-23.9 to +12.9) | -9.0% (-16.9 to -1.0) | -10.0% (-25.2 to +5.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 188,581 | 204,771 | +8.6% (-8.3 to +25.5) | +16.0% (+4.4 to +27.5) | +13.3% (-20.5 to +47.0) | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.16 | +28.7% (-63.7 to +121.0) | +32.2% (-137.0 to +201.5) | -1.9% (-22.7 to +18.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 191.5 | 247.5 | +29.2% (-65.5 to +123.9) | +32.7% (-138.1 to +203.5) | -1.7% (-22.2 to +18.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 85.6 | 97.5 | +14.0% (-121.8 to +149.8) | +35.0% (-191.3 to +261.4) | -0.1% (-15.8 to +15.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 21.3 | +21.3 (+11 to +31.7) | +19.7 (-0.414 to +39.7) | +18 (+8.06 to +27.9) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (14 trials, 1 allowed, 4 refused); acting: 384 to 512 (14 trials, 1 allowed, 4 refused); acting: 384 to 768 (14 trials, 3 allowed, 3 refused); run B: acting: 256 to 512 (11 trials, 2 allowed, 4 refused); acting: 384 to 512 (11 trials, 1 allowed, 4 refused); acting: 256 to 768 (17 trials, 4 allowed, 3 refused); run C: left native (15 trials, 0 allowed, 3 refused); acting: 256 to 512 (12 trials, 2 allowed, 4 refused); acting: 384 to 512 (13 trials, 1 allowed, 3 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 46 EVEN, 2 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
