# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 14.7 | 10.7 | -27.5% | -10 to 1.89 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.1% | -2.93 to 5.45 | EVEN, no difference beyond the noise |
| queries a second | 983 | 984 | +0.1% | -2.93 to 5.45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.2 | 2.54 | +15.7% | 0.000269 to 0.691 | LOSS |
| latency, 99th percentile (ms) | 3.89 | 4.5 | +15.7% | 0.0201 to 1.2 | LOSS |
| latency, mean (ms) | 1.13 | 1.2 | +6.9% | -0.0306 to 0.186 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.5% | 7.28 to 14.5 | power given |
| pages holding data, mean (MB) | 118 | 124 | +5.2% | 1.38 to 10.9 | power given |
| pages read from disk into the pool (misses) | 416,117 | 410,251 | -1.4% | -15,188 to 3,457 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.288 | +15.6% | -0.0217 to 0.0992 | EVEN, no difference beyond the noise |
| host CPU-seconds | 437 | 504 | +15.4% | -37.6 to 172 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 67.1 | 127 | +89.0% | -85.6 to 205 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 5.8 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
