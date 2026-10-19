# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 289 | +0.3% | -2.55 to 4.39 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.0% | -1.62 to 1.75 | EVEN, no difference beyond the noise |
| queries a second | 4,674 | 4,675 | +0.0% | -25.9 to 28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.43 | 4.38 | -1.2% | -0.46 to 0.358 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 93.7 | 10.9 | -88.4% | -387 to 221 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.69 | 2.89 | -38.2% | -6.93 to 3.35 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 474 | -7.4% | -230 to 154 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 442 | 424 | -4.0% | -212 to 177 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,372 | 252,893 | +3.9% | -78,384 to 97,425 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.176 | +0.5% | -0.00462 to 0.00643 | EVEN, no difference beyond the noise |
| host CPU-seconds | 106 | 107 | +0.5% | -3.05 to 4.17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.4 | +0.2% | -0.101 to 0.109 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | 2.54 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
