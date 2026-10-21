# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 191 | +0.5% | -3.8 to 5.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.1% | -2.61 to 2.87 | EVEN, no difference beyond the noise |
| queries a second | 3,921 | 3,924 | +0.1% | -52.1 to 57.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.23 | 8.74 | -5.3% | -1.21 to 0.233 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 13.2 | -4.8% | -2.22 to 0.894 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.49 | 5.37 | -2.1% | -0.22 to -0.0118 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 569 | +11.1% | -54.9 to 169 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 505 | +9.2% | -40.9 to 126 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,181 | 510,519 | -17.1% | -289,498 to 78,174 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.211 | -2.8% | -0.0126 to 0.000389 | EVEN, no difference beyond the noise |
| host CPU-seconds | 349 | 339 | -2.8% | -19.6 to 0.149 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.01 | 3.87 | -3.3% | -0.252 to -0.0123 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 7.35 to 23.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
