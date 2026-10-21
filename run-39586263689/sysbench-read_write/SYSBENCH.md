# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +1.1% | -3.06 to 7.09 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.4% | -0.275 to 1.81 | EVEN, no difference beyond the noise |
| queries a second | 3,929 | 3,945 | +0.4% | -5.51 to 36.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.35 | 8.75 | -6.5% | -3 to 1.79 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 13.2 | -4.9% | -4.86 to 3.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.55 | 5.39 | -2.9% | -1.18 to 0.858 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 554 | +8.2% | -52.4 to 136 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 495 | +7.5% | -45.4 to 114 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,311 | 539,670 | -12.3% | -261,326 to 110,044 | shown, not judged |
| host CPU busy (share of the run) | 0.29 | 0.284 | -2.1% | -0.047 to 0.0351 | EVEN, no difference beyond the noise |
| host CPU-seconds | 511 | 500 | -2.1% | -82.6 to 61.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.86 | 5.68 | -3.1% | -1.16 to 0.798 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 7.46 to 29.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
