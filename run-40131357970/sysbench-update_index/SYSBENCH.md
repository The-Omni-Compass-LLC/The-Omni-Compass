# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 160 | 204 | +27.5% | -47.8 to 136 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -6.86 to 6.82 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -6.86 to 6.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 26.2 | +356.1% | -82.6 to 123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,128 | 112 | -90.1% | -5,867 to 3,835 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 24.6 | 5.69 | -76.9% | -124 to 86.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.1% | 1.78 to 13.9 | power given |
| pages holding data, mean (MB) | 119 | 124 | +4.3% | 1.92 to 8.17 | power given |
| pages read from disk into the pool (misses) | 417,345 | 413,205 | -1.0% | -5,262 to -3,019 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.166 | -9.6% | -0.0429 to 0.0075 | EVEN, no difference beyond the noise |
| host CPU-seconds | 323 | 292 | -9.5% | -78.4 to 17.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.92 | 3.18 | -35.4% | -5.52 to 2.04 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
