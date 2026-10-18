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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
