# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | -0.3% | -3.74 to 2.09 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 291 | -0.3% | -4.18 to 2.5 | EVEN, no difference beyond the noise |
| queries a second | 4,670 | 4,657 | -0.3% | -66.9 to 40 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.75 | 3.7 | -1.2% | -0.583 to 0.492 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.92 | 5.96 | +0.7% | -1.74 to 1.82 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.08 | 2.09 | +0.4% | -0.281 to 0.297 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 467 | -8.9% | -67.6 to -23.2 | GAIN |
| pages holding data, mean (MB) | 446 | 399 | -10.5% | -98.2 to 4.51 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 247,182 | 258,301 | +4.5% | -20,872 to 43,109 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.167 | +1.3% | 0.000519 to 0.00391 | power given |
| host CPU-seconds | 102 | 103 | +1.3% | 0.296 to 2.46 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.31 | +1.6% | -0.00887 to 0.0823 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -2.27 to 2.78 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.1% | -3.33 to 3.93 | EVEN, no difference beyond the noise |
| queries a second | 4,735 | 4,740 | +0.1% | -53.2 to 62.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3 | 2.9 | -3.5% | -0.334 to 0.122 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.52 | 6.3 | -3.4% | -5.54 to 5.1 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.72 | 2.75 | +1.1% | -0.975 to 1.03 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 523 | +2.2% | -32 to 55 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 472 | +2.3% | -24.1 to 45.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,221 | 590,389 | -9.8% | -164,144 to 36,481 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.175 | -1.9% | -0.0133 to 0.00667 | EVEN, no difference beyond the noise |
| host CPU-seconds | 320 | 314 | -1.9% | -23.8 to 11.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.34 | -1.9% | -0.192 to 0.1 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 7.08 to 22.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 189 | -1.4% | -18.7 to 13.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.1% | -1.42 to 1.8 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,952 | +0.1% | -28.4 to 36.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.11 | 11.4 | +61.1% | -10.1 to 18.8 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 28.2 | 47 | +66.7% | -72.9 to 111 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.6 | 4.44 | +23.1% | -2.78 to 4.45 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 555 | +8.4% | -89.5 to 176 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 460 | 497 | +8.0% | -76.2 to 150 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,199 | 545,094 | -11.5% | -330,758 to 188,548 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.14 | +1.3% | -0.0128 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 245 | 249 | +1.3% | -22.6 to 29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.81 | 2.89 | +2.8% | -0.236 to 0.395 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 12.5 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,958 | 2,962 | +0.1% | -3.68 to 11.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,962 | 2,966 | +0.1% | 1.41 to 4.82 | GAIN |
| queries a second | 2,962 | 2,966 | +0.1% | 1.41 to 4.82 | GAIN |
| latency, 95th percentile (ms) | 0.205 | 0.205 | -0.2% | -0.0161 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.35 | 0.35 | +0.0% | 0 to 0 | EVEN, the same |
| latency, mean (ms) | 0.139 | 0.153 | +9.8% | -0.0379 to 0.0652 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 454 | -11.4% | -148 to 31.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 414 | -10.8% | -146 to 46.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,983 | 440,264 | +19.6% | -79,762 to 224,324 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.11 | +1.0% | 5.51e-05 to 0.00217 | power given |
| host CPU-seconds | 193 | 195 | +1.0% | 0.323 to 3.58 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.144 | +0.9% | -0.000186 to 0.00269 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 3.43 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 95.9 | 107 | +12.0% | -11.2 to 34.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -3.4 to 1.8 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -3.4 to 1.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.32 | 1.35 | +2.4% | -0.163 to 0.225 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.6 | 12.3 | +16.0% | -29.4 to 32.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.1 | 1.12 | +2.1% | -0.667 to 0.713 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 479 | -6.4% | -67.9 to 2.41 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 408 | -9.8% | -52.8 to -36.1 | GAIN |
| pages read from disk into the pool (misses) | 189,769 | 216,798 | +14.2% | 2,353 to 51,706 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.195 | -2.5% | -0.0293 to 0.0194 | EVEN, no difference beyond the noise |
| host CPU-seconds | 346 | 338 | -2.5% | -50.2 to 33.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.2 | 6.93 | -15.4% | -5.02 to 2.49 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 8.43 to 21.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
