# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -4.5 to 4.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -4.41 to 4.49 | EVEN, no difference beyond the noise |
| queries a second | 4,716 | 4,717 | +0.0% | -70.5 to 71.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.98 | 3.93 | -1.2% | -0.247 to 0.154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.41 | 5.47 | +1.2% | -0.0757 to 0.207 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.09 | 3 | -3.0% | -0.231 to 0.0424 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 729 | +469.4% | 476 to 726 | power given |
| pages holding data, mean (MB) | 120 | 658 | +447.0% | 437 to 638 | power given |
| pages read from disk into the pool (misses) | 1,994,149 | 319,312 | -84.0% | -1,893,443 to -1,456,231 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.238 | -2.6% | -0.0203 to 0.00753 | EVEN, no difference beyond the noise |
| host CPU-seconds | 434 | 423 | -2.6% | -35.5 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.22 | 3.14 | -2.6% | -0.216 to 0.0476 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 1.87 to 9.46 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
