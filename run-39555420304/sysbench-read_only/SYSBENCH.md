# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.65 to 2.27 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.1% | -1.64 to 2.22 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,728 | +0.1% | -26.3 to 35.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.33 | 4.25 | -1.8% | -0.27 to 0.115 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.32 | 6.28 | -0.6% | -0.203 to 0.127 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.27 | 3.21 | -1.6% | -0.136 to 0.031 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 500 | -2.3% | -29.6 to 6.46 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 452 | -2.1% | -31.2 to 11.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,799 | 662,501 | +1.0% | -48,162 to 61,565 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.191 | -2.1% | -0.0134 to 0.00532 | EVEN, no difference beyond the noise |
| host CPU-seconds | 323 | 317 | -2.1% | -22.2 to 8.95 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.35 | -2.1% | -0.151 to 0.0484 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 9.08 to 24.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
