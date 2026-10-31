# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11.9 | 17.9 | +50.8% | -3.32 to 15.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 985 | +0.0% | -1.48 to 1.87 | EVEN, no difference beyond the noise |
| queries a second | 984 | 985 | +0.0% | -1.48 to 1.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.8 | 1.76 | -2.1% | -0.467 to 0.391 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.57 | 3.55 | -0.7% | -0.539 to 0.492 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.04 | -1.9% | -0.153 to 0.113 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.3% | 703 to 745 | power given |
| pages holding data, mean (MB) | 458 | 888 | +94.0% | 408 to 453 | power given |
| pages read from disk into the pool (misses) | 193,005 | 71,691 | -62.9% | -129,293 to -113,335 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.224 | -3.9% | -0.0348 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 394 | -3.9% | -60.6 to 28.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 78.5 | 49.5 | -36.9% | -82.7 to 24.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
