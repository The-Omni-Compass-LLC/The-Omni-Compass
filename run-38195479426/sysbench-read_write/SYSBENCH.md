# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 191 | +0.1% | -1.93 to 2.17 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.0% | -0.383 to 0.354 | no difference beyond the noise |
| queries a second | 3,906 | 3,906 | -0.0% | -7.67 to 7.08 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.74 | 8.63 | -1.2% | -1.35 to 1.14 | no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 12.8 | -0.6% | -1.27 to 1.12 | no difference beyond the noise |
| latency, mean (ms) | 5.42 | 5.42 | +0.0% | -0.0843 to 0.0877 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 558 | +9.0% | -39.3 to 132 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 494 | +7.1% | -65.8 to 131 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 434,666 | 391,266 | -10.0% | -161,165 to 74,366 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.226 | +0.1% | -0.0099 to 0.0104 | no difference beyond the noise |
| host CPU-seconds | 245 | 246 | +0.2% | -10.3 to 11.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.17 | 4.18 | +0.1% | -0.136 to 0.147 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 7.16 to 17.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
