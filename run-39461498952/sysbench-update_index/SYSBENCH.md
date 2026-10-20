# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 22.1 | 22.5 | +2.1% | -4.08 to 5.02 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 986 | +0.2% | -0.651 to 5.16 | EVEN, no difference beyond the noise |
| queries a second | 983 | 986 | +0.2% | -0.651 to 5.16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.71 | 1.67 | -2.7% | -0.38 to 0.288 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.55 | 3.51 | -1.3% | -0.382 to 0.292 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.03 | 1.02 | -0.6% | -0.0811 to 0.0693 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 497 | -2.9% | -50.5 to 20.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 428 | -5.3% | -59 to 10.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,975 | 202,325 | +6.5% | -25,138 to 49,838 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.216 | -1.9% | -0.031 to 0.0226 | EVEN, no difference beyond the noise |
| host CPU-seconds | 387 | 380 | -1.9% | -54.1 to 39.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 39.8 | 37.3 | -6.5% | -18.8 to 13.6 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 13.9 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
