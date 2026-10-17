# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,935 | 2,934 | -0.1% | -6.99 to 3.96 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,940 | 2,939 | -0.1% | -7.68 to 4.54 | EVEN, no difference beyond the noise |
| queries a second | 2,940 | 2,939 | -0.1% | -7.68 to 4.54 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.284 | 0.279 | -1.6% | -0.0283 to 0.0189 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.445 | -2.3% | -0.041 to 0.0197 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.186 | +1.5% | -0.00512 to 0.0106 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 462 | -9.7% | -121 to 21.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 423 | -8.8% | -102 to 20.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,298 | 413,907 | +12.7% | -48,953 to 142,170 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.146 | +0.0% | -0.0042 to 0.00431 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 263 | -0.0% | -7.46 to 7.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.195 | 0.196 | +0.1% | -0.00516 to 0.0054 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 2.74 to 17.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
