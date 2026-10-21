# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 979 | 977 | -0.2% | -3.11 to -1.05 | LOSS |
| queries a second | 979 | 977 | -0.2% | -3.11 to -1.05 | LOSS |
| latency, 95th percentile (ms) | 2.27 | 2.25 | -0.8% | -0.449 to 0.412 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 42.9 | 17.9 | -58.3% | -168 to 118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 2.91 | -12.3% | -4.35 to 3.54 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 515 | +0.6% | -51.9 to 58.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 445 | -1.7% | -77.1 to 61.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,939 | 193,645 | +2.0% | -42,427 to 49,838 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.208 | +0.4% | -0.0229 to 0.0247 | EVEN, no difference beyond the noise |
| host CPU-seconds | 368 | 371 | +0.7% | -36.1 to 41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 368,497 | 370,953 | +0.7% | -36,053 to 40,967 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | -1.85 to 28.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
