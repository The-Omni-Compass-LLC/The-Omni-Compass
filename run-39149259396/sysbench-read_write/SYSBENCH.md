# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 197 | 195 | -0.7% | -4.61 to 1.84 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | -0.3% | -3.09 to 1.91 | EVEN, no difference beyond the noise |
| queries a second | 3,965 | 3,954 | -0.3% | -61.9 to 38.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.8 | 5.34 | +11.4% | 0.332 to 0.761 | LOSS |
| latency, 99th percentile (ms) | 9.48 | 12.3 | +30.1% | -0.896 to 6.61 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.65 | 2.86 | +7.8% | 0.19 to 0.225 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 398 | -22.2% | -183 to -44.4 | GAIN |
| pages holding data, mean (MB) | 462 | 359 | -22.4% | -178 to -29.3 | GAIN |
| pages read from disk into the pool (misses) | 617,540 | 873,710 | +41.5% | 169,482 to 342,858 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.124 | +2.7% | -0.000131 to 0.00657 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 221 | +2.7% | -0.19 to 11.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.48 | +3.4% | 0.0541 to 0.11 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | -5.15 to 21.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
