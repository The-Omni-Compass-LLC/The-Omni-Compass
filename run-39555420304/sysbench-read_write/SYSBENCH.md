# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | -0.3% | -0.994 to -0.0284 | LOSS |
| throughput (transactions a second) | 197 | 197 | -0.1% | -0.989 to 0.545 | EVEN, no difference beyond the noise |
| queries a second | 3,947 | 3,942 | -0.1% | -19.8 to 10.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.47 | 5.74 | +4.9% | 0.103 to 0.438 | LOSS |
| latency, 99th percentile (ms) | 9.06 | 9.57 | +5.6% | -0.249 to 1.27 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3 | 3.1 | +3.3% | -0.113 to 0.313 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 471 | -7.9% | -195 to 113 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 426 | -7.7% | -172 to 101 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,443 | 736,920 | +19.7% | -352,808 to 595,762 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.145 | +0.3% | -0.00922 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 257 | 257 | +0.3% | -16.5 to 18.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.87 | 2.88 | +0.6% | -0.178 to 0.213 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 12.5 to 20.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
