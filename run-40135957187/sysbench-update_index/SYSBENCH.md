# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 198 | +2.6% | -125 to 135 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -4.97 to 4.07 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -4.97 to 4.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 34.1 | 52.1 | +52.9% | -88.4 to 124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 146 | 165 | +13.5% | -153 to 192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.07 | 9.23 | +30.5% | -11.7 to 16 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 455 | -11.2% | -256 to 142 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 387 | -14.6% | -280 to 147 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,211 | 236,794 | +24.5% | -78,021 to 171,188 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.136 | -0.8% | -0.0185 to 0.0162 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 241 | -0.7% | -31.6 to 28.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.89 | 2.68 | -7.3% | -2.59 to 2.17 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 11.2 to 14.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
