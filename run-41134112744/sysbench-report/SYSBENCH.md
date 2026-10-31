# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.0% | -6.85 to 6.94 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.0% | -7.86 to 8.02 | EVEN, no difference beyond the noise |
| queries a second | 4,697 | 4,698 | +0.0% | -126 to 128 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.74 | 4.71 | -0.6% | -0.354 to 0.294 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.75 | 6.71 | -0.7% | -0.804 to 0.714 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.11 | 3.08 | -0.9% | -0.109 to 0.0564 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 745 | +45.6% | 86.5 to 380 | power given |
| pages holding data, mean (MB) | 453 | 673 | +48.6% | 94.7 to 345 | power given |
| pages read from disk into the pool (misses) | 246,073 | 172,309 | -30.0% | -115,406 to -32,123 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.239 | -0.5% | -0.00479 to 0.00215 | EVEN, no difference beyond the noise |
| host CPU-seconds | 143 | 142 | -0.5% | -3 to 1.45 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.19 | 3.18 | -0.5% | -0.0566 to 0.0218 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.5% | -1.98 to 4.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.3% | 0.101 to 1.38 | GAIN |
| queries a second | 4,679 | 4,691 | +0.3% | 1.61 to 22.1 | GAIN |
| latency, 95th percentile (ms) | 2.91 | 3 | +3.0% | 0.0166 to 0.16 | LOSS |
| latency, 99th percentile (ms) | 15.4 | 4.97 | -67.8% | -56.4 to 35.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.49 | 2.31 | -33.9% | -6.45 to 4.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 738 | +44.1% | 212 to 239 | power given |
| pages holding data, mean (MB) | 463 | 647 | +39.9% | 172 to 197 | power given |
| pages read from disk into the pool (misses) | 652,196 | 317,340 | -51.3% | -346,937 to -322,775 | shown, not judged |
| host CPU busy (share of the run) | 0.174 | 0.176 | +1.2% | -0.00325 to 0.00742 | EVEN, no difference beyond the noise |
| host CPU-seconds | 319 | 323 | +1.2% | -5.56 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.4 | +0.7% | -0.0259 to 0.0587 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.5% | -0.0191 to 1.77 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.1% | -0.373 to 0.0151 | EVEN, no difference beyond the noise |
| queries a second | 3,932 | 3,929 | -0.1% | -7.46 to 0.303 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.63 | 5.81 | -12.4% | -1.52 to -0.124 | GAIN |
| latency, 99th percentile (ms) | 10.4 | 8.4 | -19.3% | -4.18 to 0.174 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.34 | 4.15 | -4.3% | -0.276 to -0.094 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 838 | +63.7% | 42.2 to 610 | power given |
| pages holding data, mean (MB) | 462 | 755 | +63.4% | 24.2 to 562 | power given |
| pages read from disk into the pool (misses) | 616,370 | 261,078 | -57.6% | -515,462 to -195,121 | shown, not judged |
| host CPU busy (share of the run) | 0.25 | 0.239 | -4.4% | -0.0131 to -0.00902 | GAIN |
| host CPU-seconds | 445 | 425 | -4.4% | -23.8 to -15.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.99 | 4.74 | -4.9% | -0.309 to -0.175 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,953 | +0.1% | -15.6 to 23.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,965 | +0.0% | -5.2 to 5.24 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,965 | +0.0% | -5.2 to 5.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.226 | 0.215 | -4.7% | -0.0258 to 0.00451 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.386 | -3.4% | -0.082 to 0.0547 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.327 | 0.281 | -14.1% | -0.345 to 0.253 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,195 | +133.4% | 617 to 749 | power given |
| pages holding data, mean (MB) | 464 | 922 | +98.8% | 445 to 471 | power given |
| pages read from disk into the pool (misses) | 367,264 | 76,805 | -79.1% | -302,030 to -278,886 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.112 | -0.8% | -0.00812 to 0.00638 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 199 | -0.8% | -14.5 to 11.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.148 | -0.9% | -0.0118 to 0.00915 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 163 | 179 | +9.8% | -66.7 to 98.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 989 | +0.1% | -0.168 to 1.54 | EVEN, no difference beyond the noise |
| queries a second | 988 | 989 | +0.1% | -0.168 to 1.54 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.66 | 8.07 | +73.0% | -11.7 to 18.5 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.8 | 24.1 | +63.0% | -40 to 58.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.68 | 2.31 | +37.2% | -3.18 to 4.44 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.5% | 699 to 749 | power given |
| pages holding data, mean (MB) | 455 | 889 | +95.6% | 402 to 467 | power given |
| pages read from disk into the pool (misses) | 192,139 | 71,482 | -62.8% | -129,330 to -111,984 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.117 | -4.3% | -0.0162 to 0.00579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 205 | -4.2% | -28.2 to 10.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.9 | 2.58 | -11.0% | -1.68 to 1.05 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
