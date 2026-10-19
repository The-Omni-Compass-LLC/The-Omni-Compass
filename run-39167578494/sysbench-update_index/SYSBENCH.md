# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 81.5 | 72.7 | -10.9% | -42.8 to 25.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 981 | 980 | -0.1% | -7.95 to 6.26 | EVEN, no difference beyond the noise |
| queries a second | 981 | 980 | -0.1% | -7.95 to 6.26 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.49 | 1.55 | +4.2% | -0.319 to 0.443 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.52 | 2.8 | +11.1% | -1.24 to 1.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.919 | 0.95 | +3.4% | -0.0707 to 0.134 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.0% | 5.14 to 17.9 | power given |
| pages holding data, mean (MB) | 119 | 128 | +7.7% | 1.87 to 16.4 | power given |
| pages read from disk into the pool (misses) | 415,233 | 407,814 | -1.8% | -13,232 to -1,607 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.211 | +5.3% | -0.0632 to 0.0845 | EVEN, no difference beyond the noise |
| host CPU-seconds | 356 | 375 | +5.3% | -112 to 150 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 10.1 | 11.3 | +12.1% | -6.88 to 9.33 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
