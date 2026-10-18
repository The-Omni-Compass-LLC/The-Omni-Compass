# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 186 | 187 | +0.3% | -3.72 to 4.87 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.1% | -2.52 to 2.27 | EVEN, no difference beyond the noise |
| queries a second | 3,913 | 3,910 | -0.1% | -50.4 to 45.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 10.6 | 10.2 | -3.6% | -2.04 to 1.27 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 199 | 163 | -18.2% | -193 to 121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 9.46 | 8.25 | -12.8% | -5.15 to 2.73 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 542 | +5.8% | -16.8 to 76 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 485 | +5.2% | -7.25 to 55.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,152 | 554,486 | -9.9% | -204,990 to 83,659 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.4% | -0.00433 to -0.00182 | GAIN |
| host CPU-seconds | 389 | 384 | -1.4% | -8.14 to -2.72 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.54 | 4.46 | -1.7% | -0.212 to 0.0566 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 7.62 to 30.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
