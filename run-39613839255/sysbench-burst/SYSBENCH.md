# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 290 | -0.2% | -2.78 to 1.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 291 | -0.5% | -2.57 to -0.176 | LOSS |
| queries a second | 4,680 | 4,658 | -0.5% | -41.1 to -2.81 | LOSS |
| latency, 95th percentile (ms) | 3.73 | 3.53 | -5.3% | -0.37 to -0.0245 | GAIN |
| latency, 99th percentile (ms) | 17.2 | 6.14 | -64.3% | -59 to 36.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.02 | 2.17 | -28.0% | -3.88 to 2.19 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 380 | -25.8% | -335 to 70.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 441 | 321 | -27.3% | -262 to 21.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,172 | 291,691 | +19.5% | -33,425 to 128,461 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.163 | +0.0% | -0.00797 to 0.00807 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.5 | 99.6 | +0.1% | -5.2 to 5.35 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.23 | 2.23 | +0.3% | -0.0948 to 0.106 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | -1.5 to 8.84 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
