# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.0% | -3.09 to 3.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -2.7 to 2.53 | EVEN, no difference beyond the noise |
| queries a second | 4,725 | 4,723 | -0.0% | -43.1 to 40.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.71 | 3.55 | -4.1% | -0.271 to -0.0368 | GAIN |
| latency, 99th percentile (ms) | 5.25 | 4.88 | -7.0% | -0.804 to 0.0669 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.8 | 2.74 | -2.1% | -0.144 to 0.029 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 496 | -3.1% | -76.6 to 45.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 451 | -2.4% | -67.8 to 45.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,123 | 652,963 | -0.5% | -76,234 to 69,915 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.215 | -1.9% | -0.00916 to 0.000869 | EVEN, no difference beyond the noise |
| host CPU-seconds | 392 | 384 | -1.9% | -16.3 to 1.52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.9 | 2.85 | -1.9% | -0.15 to 0.0398 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 14.9 to 17.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
