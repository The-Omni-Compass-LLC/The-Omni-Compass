# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.2% | -4.29 to 3.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 292 | -0.3% | -3.08 to 1.1 | EVEN, no difference beyond the noise |
| queries a second | 4,695 | 4,679 | -0.3% | -49.3 to 17.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.79 | -1.2% | -0.179 to 0.111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.38 | 4.23 | -3.6% | -0.551 to 0.237 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.79 | 2.14 | -23.4% | -3.4 to 2.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.3% | 5.52 to 10.5 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.6% | 10.4 to 17.3 | power given |
| pages read from disk into the pool (misses) | 1,973,356 | 1,913,137 | -3.1% | -79,074 to -41,363 | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.175 | -0.5% | -0.00354 to 0.00168 | EVEN, no difference beyond the noise |
| host CPU-seconds | 322 | 320 | -0.5% | -6.66 to 3.25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.38 | -0.3% | -0.035 to 0.0195 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
