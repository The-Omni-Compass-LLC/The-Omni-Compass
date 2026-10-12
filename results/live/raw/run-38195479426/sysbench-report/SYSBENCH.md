# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 285 | 285 | -0.1% | -6.32 to 5.54 | no difference beyond the noise |
| throughput (transactions a second) | 290 | 291 | +0.1% | -6.59 to 7.46 | no difference beyond the noise |
| queries a second | 4,645 | 4,651 | +0.1% | -105 to 119 | no difference beyond the noise |
| latency, 95th percentile (ms) | 6.79 | 6.83 | +0.6% | -0.135 to 0.217 | no difference beyond the noise |
| latency, 99th percentile (ms) | 9 | 9.22 | +2.4% | -0.022 to 0.461 | no difference beyond the noise |
| latency, mean (ms) | 3.68 | 3.69 | +0.5% | -0.0348 to 0.0734 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 518 | +1.1% | -6.59 to 18.1 | no difference beyond the noise |
| pages holding data, mean (MB) | 444 | 448 | +1.0% | -37.6 to 46.8 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 168,534 | 163,109 | -3.2% | -18,244 to 7,394 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.213 | +2.0% | -0.00222 to 0.0107 | no difference beyond the noise |
| host CPU-seconds | 77.6 | 79.2 | +2.0% | -1.13 to 4.25 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.64 | 2.7 | +2.1% | 0.014 to 0.0986 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.0% | -3.58 to 3.72 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.0% | -3.46 to 3.72 | no difference beyond the noise |
| queries a second | 4,677 | 4,679 | +0.0% | -55.4 to 59.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.2 | -0.6% | -0.134 to 0.0837 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.5 | -2.4% | -0.278 to 0.0102 | no difference beyond the noise |
| latency, mean (ms) | 3.21 | 3.17 | -1.3% | -0.053 to -0.0307 | better |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 484 | -5.4% | -188 to 132 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 436 | -5.6% | -162 to 111 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 455,882 | 492,555 | +8.0% | -219,971 to 293,317 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.196 | -1.3% | -0.00696 to 0.00187 | no difference beyond the noise |
| host CPU-seconds | 221 | 218 | -1.3% | -7.63 to 2.04 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.46 | 2.43 | -1.3% | -0.0566 to -0.00677 | better |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | 10.5 to 20.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 191 | +0.1% | -1.93 to 2.17 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.0% | -0.383 to 0.354 | no difference beyond the noise |
| queries a second | 3,906 | 3,906 | -0.0% | -7.67 to 7.08 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.74 | 8.63 | -1.2% | -1.35 to 1.14 | no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 12.8 | -0.6% | -1.27 to 1.12 | no difference beyond the noise |
| latency, mean (ms) | 5.42 | 5.42 | +0.0% | -0.0843 to 0.0877 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 558 | +9.0% | -39.3 to 132 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 494 | +7.1% | -65.8 to 131 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 434,666 | 391,266 | -10.0% | -161,165 to 74,366 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.226 | +0.1% | -0.0099 to 0.0104 | no difference beyond the noise |
| host CPU-seconds | 245 | 246 | +0.2% | -10.3 to 11.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.17 | 4.18 | +0.1% | -0.136 to 0.147 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 7.16 to 17.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,941 | -0.2% | -16.9 to 4.84 | no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,947 | -0.1% | -21.1 to 14.1 | no difference beyond the noise |
| queries a second | 2,950 | 2,947 | -0.1% | -21.1 to 14.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.211 | 0.216 | +2.1% | -0.0114 to 0.0201 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.28 | 0.308 | +9.8% | -0.0678 to 0.122 | no difference beyond the noise |
| latency, mean (ms) | 0.081 | 0.0839 | +3.6% | -0.0181 to 0.0239 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 463 | -9.5% | -243 to 146 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 420 | -9.1% | -212 to 128 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 263,277 | 298,120 | +13.2% | -141,721 to 211,405 | shown, not judged |
| host CPU busy (share of the run) | 0.0652 | 0.0669 | +2.7% | -0.00267 to 0.00614 | no difference beyond the noise |
| host CPU-seconds | 78.4 | 80.5 | +2.6% | -3.26 to 7.32 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0872 | 0.0896 | +2.8% | -0.00362 to 0.0085 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -0.838 to 9.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 164 | -7.8% | -99 to 71 | no difference beyond the noise |
| throughput (transactions a second) | 979 | 980 | +0.1% | -13.9 to 16.3 | no difference beyond the noise |
| queries a second | 979 | 980 | +0.1% | -13.9 to 16.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 95.3 | 111 | +16.2% | -164 to 195 | no difference beyond the noise |
| latency, 99th percentile (ms) | 217 | 237 | +9.5% | -353 to 394 | no difference beyond the noise |
| latency, mean (ms) | 14.8 | 17.7 | +19.7% | -27.1 to 32.9 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 391 | -23.6% | -269 to 27.1 | no difference beyond the noise |
| pages holding data, mean (MB) | 450 | 318 | -29.2% | -315 to 52.2 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 140,032 | 191,350 | +36.6% | -13,303 to 115,940 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.144 | +1.3% | -0.0229 to 0.0266 | no difference beyond the noise |
| host CPU-seconds | 168 | 170 | +1.4% | -27.2 to 31.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.18 | 3.42 | +7.5% | -1.67 to 2.14 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 6.08 to 21.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
