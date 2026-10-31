# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 282 | 344 | +22.0% | 30 to 94.1 | GAIN |
| throughput (transactions a second) | 988 | 989 | +0.1% | -8.4 to 9.58 | EVEN, no difference beyond the noise |
| queries a second | 988 | 989 | +0.1% | -8.4 to 9.58 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.01 | 3.45 | +14.7% | 0.287 to 0.595 | LOSS |
| latency, 99th percentile (ms) | 7.83 | 6.73 | -14.1% | -5.34 to 3.14 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.04 | -11.6% | -0.397 to 0.124 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,281 | +900.7% | 1,069 to 1,236 | power given |
| pages holding data, mean (MB) | 118 | 882 | +646.6% | 756 to 771 | power given |
| pages read from disk into the pool (misses) | 418,369 | 71,129 | -83.0% | -362,873 to -331,607 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.137 | -13.9% | -0.0353 to -0.00893 | GAIN |
| host CPU-seconds | 279 | 241 | -13.8% | -61.1 to -15.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.2 | 1.54 | -29.7% | -1.17 to -0.136 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
