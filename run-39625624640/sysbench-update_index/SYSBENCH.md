# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 127 | 133 | +4.7% | -35.4 to 47.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 981 | 980 | -0.1% | -5.72 to 4.51 | EVEN, no difference beyond the noise |
| queries a second | 981 | 980 | -0.1% | -5.72 to 4.51 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.35 | 1.34 | -0.8% | -0.226 to 0.206 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.06 | 1.95 | -5.3% | -0.744 to 0.528 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.846 | -19.8% | -1.13 to 0.71 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 469 | -8.4% | -108 to 22.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 377 | -16.7% | -164 to 12.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,127 | 251,540 | +32.3% | 2,861 to 119,965 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.178 | -1.2% | -0.0236 to 0.0194 | EVEN, no difference beyond the noise |
| host CPU-seconds | 320 | 316 | -1.2% | -41.2 to 33.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.72 | 5.22 | -8.7% | -3.57 to 2.58 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 5.62 to 28.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
