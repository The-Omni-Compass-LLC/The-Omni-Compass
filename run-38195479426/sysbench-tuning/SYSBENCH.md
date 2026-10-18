# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,941 | -0.2% | -16.9 to 4.84 | no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,947 | -0.1% | -21.1 to 14.1 | no difference beyond the noise |
| queries a second | 2,950 | 2,947 | -0.1% | -21.1 to 14.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.211 | 0.216 | +2.1% | -0.0114 to 0.0201 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.28 | 0.308 | +9.8% | -0.0678 to 0.122 | no difference beyond the noise |
| latency, mean (ms) | 0.081 | 0.0839 | +3.6% | -0.0181 to 0.0239 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 463 | -9.5% | -243 to 146 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 420 | -9.1% | -212 to 128 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 263,277 | 298,120 | +13.2% | -141,721 to 211,405 | shown, not judged |
| host CPU busy (share of the run) | 0.0652 | 0.0669 | +2.7% | -0.00267 to 0.00614 | no difference beyond the noise |
| host CPU-seconds | 78.4 | 80.5 | +2.6% | -3.26 to 7.32 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0872 | 0.0896 | +2.8% | -0.00362 to 0.0085 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -0.838 to 9.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
