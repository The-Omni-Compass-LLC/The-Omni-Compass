# sysbench on MySQL, a database's buffer pool as shipped: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native (`docs/MYSQL_PREREGISTRATION.md`, amendment 5); omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39826073316 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| B | 39846952545 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| C | 39864234559 | `681ff70efadd` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,958 | 2,957 | -0.0% (-0.2 to +0.1) | +0.0% (-0.9 to +0.9) | -0.2% (-0.7 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% (-0.2 to +0.1) | +0.0% (-0.8 to +0.9) | -0.2% (-0.6 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,965 | 2,963 | -0.1% (-0.2 to +0.1) | +0.0% (-0.8 to +0.9) | -0.2% (-0.6 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.226 | 0.214 | -5.5% (-28.9 to +18.0) | +0.0% (-47.6 to +47.6) | +0.0% (-8.7 to +8.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.352 | 0.334 | -5.2% (-19.7 to +9.3) | -0.5% (-6.0 to +4.9) | +0.1% (-4.5 to +4.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.0973 | 0.0941 | -3.3% (-22.0 to +15.3) | +1.4% (-3.1 to +6.0) | -0.2% (-8.2 to +7.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 134.5 | +5.1% (+0.1 to +10.1) | +6.0% (-3.1 to +15.1) | +5.9% (+5.8 to +6.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 121.2 | 132.4 | +9.2% (+2.6 to +15.9) | +8.6% (-0.1 to +17.3) | +8.6% (+8.2 to +9.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 1,029,333 | 1,009,497 | -1.9% (-4.3 to +0.5) | -1.9% (-6.5 to +2.7) | -2.7% (-3.0 to -2.3) | shown, not judged |
| host CPU busy (share of the run) | 0.0715 | 0.0699 | -2.3% (-14.4 to +9.8) | -2.0% (-20.9 to +16.8) | -0.9% (-11.0 to +9.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 127.5 | 124.7 | -2.3% (-14.3 to +9.8) | -2.0% (-20.9 to +16.9) | -0.9% (-11.0 to +9.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.0947 | 0.0926 | -2.3% (-14.3 to +9.8) | -2.1% (-21.6 to +17.5) | -0.7% (-11.3 to +9.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (-0.969 to +8.97) | +6 (+6 to +6) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (3 trials, 0 allowed, 3 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (4 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 3 refused).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289.5 | 289.6 | +0.1% (-1.8 to +1.9) | -0.1% (-0.6 to +0.4) | +0.5% (-1.9 to +2.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 292.2 | 292.4 | +0.1% (-1.5 to +1.6) | -0.1% (-0.9 to +0.7) | +0.4% (-1.5 to +2.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,675 | 4,678 | +0.1% (-1.5 to +1.6) | -0.1% (-0.9 to +0.7) | +0.4% (-1.5 to +2.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.77 | 5.71 | -1.2% (-3.7 to +1.4) | -9.1% (-38.6 to +20.3) | -3.0% (-13.2 to +7.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 8.28 | 8.28 | -0.0% (-4.5 to +4.5) | -9.0% (-47.8 to +29.8) | -4.1% (-26.8 to +18.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.38 | 3.34 | -1.2% (-2.5 to +0.1) | -7.2% (-28.0 to +13.7) | -2.1% (-9.9 to +5.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 142.0 | +10.9% (+10.1 to +11.8) | +8.0% (-22.2 to +38.1) | +5.9% (+5.9 to +5.9) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 120.2 | 140.4 | +16.8% (+10.6 to +22.9) | +8.9% (-25.4 to +43.3) | +10.2% (+2.8 to +17.7) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 578,671 | 531,485 | -8.2% (-13.9 to -2.4) | -2.2% (-18.5 to +14.2) | -3.3% (-6.9 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.248 | -1.0% (-2.0 to -0.1) | -8.9% (-28.4 to +10.6) | -1.3% (-3.8 to +1.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 150.3 | 147.6 | -1.8% (-4.5 to +0.9) | -9.0% (-27.9 to +10.0) | -1.4% (-3.8 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.37 | 3.33 | -1.1% (-2.1 to -0.0) | -8.7% (-28.2 to +10.8) | -1.8% (-2.5 to -1.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +1.67 (-3.5 to +6.84) | +2 (+2 to +2) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294.0 | 294.4 | +0.2% (-0.7 to +1.0) | -0.1% (-1.4 to +1.1) | -0.2% (-0.8 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 294.4 | 295.0 | +0.2% (-0.6 to +1.0) | -0.1% (-1.4 to +1.2) | -0.2% (-0.9 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,711 | 4,720 | +0.2% (-0.6 to +1.0) | -0.1% (-1.4 to +1.2) | -0.2% (-0.9 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.96 | 3.98 | +0.6% (-2.0 to +3.2) | +0.6% (-10.8 to +12.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.5 | 5.64 | +2.4% (-0.2 to +5.1) | -3.6% (-12.4 to +5.3) | +0.0% (-4.5 to +4.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 3.01 | 3.06 | +1.5% (-0.3 to +3.4) | +0.6% (-12.4 to +13.6) | -0.2% (-1.7 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 136.1 | +6.3% (+3.7 to +9.0) | +5.8% (+1.3 to +10.4) | +6.5% (+3.8 to +9.2) | **power given in all three of our runs** |
| pages holding data, mean (MB) | 120.1 | 133.4 | +11.1% (+9.5 to +12.7) | +12.6% (+7.2 to +18.1) | +11.6% (+8.7 to +14.5) | **power given in all three of our runs** |
| pages read from disk into the pool (misses) | 1,980,456 | 1,907,591 | -3.7% (-8.5 to +1.1) | -3.2% (-7.5 to +1.0) | -4.0% (-10.4 to +2.5) | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.238 | +1.5% (-1.4 to +4.5) | +0.4% (-15.0 to +15.7) | -0.2% (-1.9 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 417.8 | 424.0 | +1.5% (-1.4 to +4.4) | +0.4% (-15.0 to +15.7) | -0.2% (-2.0 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.15 | +1.3% (-0.7 to +3.4) | +0.5% (-13.6 to +14.5) | +0.1% (-1.4 to +1.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 | +6.67 (+3.8 to +9.54) | +6 (+1.03 to +11) | +6.67 (+3.8 to +9.54) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 3 refused); left native (3 trials, 0 allowed, 3 refused); run B: left native (4 trials, 0 allowed, 4 refused); left native (3 trials, 0 allowed, 3 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (4 trials, 0 allowed, 3 refused); left native (5 trials, 0 allowed, 4 refused); left native (3 trials, 0 allowed, 3 refused).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190.3 | 189.8 | -0.3% (-1.6 to +1.0) | -0.8% (-4.6 to +2.9) | +1.3% (-2.7 to +5.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 197.1 | 196.6 | -0.3% (-1.5 to +1.0) | +0.5% (+0.1 to +0.8) | +0.5% (-0.5 to +1.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queries a second | 3,942 | 3,932 | -0.3% (-1.5 to +1.0) | +0.5% (+0.1 to +0.8) | +0.5% (-0.5 to +1.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 9.79 | 9.73 | -0.6% (-3.1 to +2.0) | +11.3% (-25.4 to +48.0) | -10.7% (-49.8 to +28.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 13.6 | 13.7 | +0.6% (-2.0 to +3.2) | +143.1% (-407.0 to +693.2) | -28.1% (-156.7 to +100.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 4.97 | 4.98 | +0.1% (-0.7 to +0.9) | +16.7% (-37.6 to +70.9) | -6.3% (-30.5 to +17.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 141.8 | +10.8% (+5.8 to +15.8) | +5.9% (+1.0 to +10.8) | +3.2% (-2.1 to +8.6) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 118.1 | 133.5 | +13.0% (+4.0 to +22.0) | +5.7% (+1.0 to +10.5) | +3.2% (-0.4 to +6.8) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 1,671,308 | 1,593,176 | -4.7% (-8.8 to -0.5) | -2.0% (-5.1 to +1.1) | -1.2% (-5.3 to +3.0) | shown, not judged |
| host CPU busy (share of the run) | 0.282 | 0.281 | -0.4% (-3.0 to +2.2) | +0.7% (-4.1 to +5.6) | -0.2% (-15.8 to +15.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 500.4 | 498.4 | -0.4% (-3.0 to +2.2) | +0.7% (-4.1 to +5.6) | -0.2% (-15.6 to +15.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 5.75 | 5.74 | -0.1% (-1.5 to +1.3) | +1.6% (-2.5 to +5.6) | -1.5% (-12.6 to +9.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 10.0 | +10 (+10 to +10) | +6 (+1.03 to +11) | +3.33 (-2.4 to +9.07) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (6 trials, 0 allowed, 5 refused); left native (5 trials, 0 allowed, 5 refused); left native (5 trials, 0 allowed, 5 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 3 refused); left native (4 trials, 0 allowed, 4 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 3 refused).

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's pool as shipped 128 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158.6 | 172.3 | +8.6% (-38.8 to +56.1) | +17.8% (-77.9 to +113.5) | +0.2% (-73.9 to +74.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 987.2 | 989.8 | +0.3% (-0.1 to +0.7) | +0.1% (-0.1 to +0.3) | +0.1% (-0.0 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| queries a second | 987.2 | 989.8 | +0.3% (-0.1 to +0.7) | +0.1% (-0.1 to +0.3) | +0.1% (-0.0 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 2.59 | 3.24 | +24.8% (-37.0 to +86.6) | +4.8% (-35.7 to +45.2) | -8.0% (-14.5 to -1.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 7.76 | 13.3 | +72.0% (-96.3 to +240.4) | +11.4% (-77.3 to +100.1) | -17.0% (-311.6 to +277.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.11 | 1.34 | +21.1% (-22.5 to +64.6) | +16.4% (-59.8 to +92.7) | -5.9% (-172.3 to +160.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128.0 | 137.1 | +7.1% (-4.8 to +19.0) | +12.4% (+7.5 to +17.3) | +12.5% (+7.3 to +17.7) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 119.5 | 125.0 | +4.6% (-2.8 to +11.9) | +9.3% (+3.1 to +15.5) | +8.8% (+3.0 to +14.7) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages read from disk into the pool (misses) | 414,906 | 410,022 | -1.2% (-4.4 to +2.1) | -2.5% (-4.3 to -0.7) | -2.5% (-3.9 to -1.1) | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.137 | -2.3% (-16.2 to +11.7) | +23.7% (-71.2 to +118.5) | +0.9% (-5.9 to +7.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 247.0 | 241.7 | -2.2% (-16.0 to +11.7) | +24.1% (-72.1 to +120.4) | +0.9% (-6.5 to +8.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.47 | 3.22 | -7.5% (-48.8 to +33.9) | -5.2% (-101.5 to +91.1) | +5.7% (-67.1 to +78.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 6 | +6 (-2.61 to +14.6) | +8 (+8 to +8) | +8.67 (+5.8 to +11.5) | shown, not judged |

The buffer pool handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (4 trials, 0 allowed, 4 refused); left native (1 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 4 refused); run B: left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); run C: left native (5 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused); left native (4 trials, 0 allowed, 4 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 2 power given, 46 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
