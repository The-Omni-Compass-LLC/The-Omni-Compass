# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 285 | 283 | -0.7% | -9.41 to 5.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.2% | -3.35 to 2.08 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,707 | -0.2% | -53.7 to 33.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.91 | 5.92 | +20.6% | -4.36 to 6.38 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 55.6 | 67.8 | +21.9% | -51.9 to 76.2 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.69 | 4.14 | +12.3% | -1.56 to 2.47 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 359 | -29.9% | -366 to 59.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 443 | 317 | -28.5% | -325 to 72.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,466 | 298,167 | +21.5% | -62,141 to 167,543 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.164 | +0.1% | -0.00561 to 0.00597 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98 | 98.1 | +0.1% | -3.3 to 3.48 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.26 | 2.28 | +0.8% | -0.0849 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 0.0313 to 9.97 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
