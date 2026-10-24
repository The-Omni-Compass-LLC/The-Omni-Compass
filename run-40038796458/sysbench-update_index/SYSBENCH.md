# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 96.6 | 95.2 | -1.5% | -50 to 47.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 980 | 981 | +0.0% | -5.04 to 5.07 | EVEN, no difference beyond the noise |
| queries a second | 980 | 981 | +0.0% | -5.04 to 5.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.45 | 1.38 | -5.1% | -0.355 to 0.207 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.39 | 2.11 | -11.8% | -1.61 to 1.05 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.926 | +4.1% | 0.0111 to 0.0616 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.9% | 4.86 to 15.4 | power given |
| pages holding data, mean (MB) | 119 | 124 | +4.2% | -0.458 to 10.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,004 | 409,794 | -1.3% | -11,893 to 1,473 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.195 | -1.8% | -0.023 to 0.0157 | EVEN, no difference beyond the noise |
| host CPU-seconds | 352 | 346 | -1.7% | -39.2 to 27 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.82 | 8.45 | -4.2% | -4.2 to 3.46 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
