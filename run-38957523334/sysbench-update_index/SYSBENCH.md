# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 978 | 977 | -0.1% | -7.71 to 6.02 | EVEN, no difference beyond the noise |
| queries a second | 978 | 977 | -0.1% | -7.71 to 6.02 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 2.12 | -1.5% | -0.488 to 0.424 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.3 | 3.49 | -34.2% | -12.1 to 8.52 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.55 | 1.49 | -3.6% | -0.427 to 0.315 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -61 to 56.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 446 | -1.8% | -58.1 to 41.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,024 | 189,944 | +0.5% | -31,901 to 33,742 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.226 | -0.9% | -0.0243 to 0.0203 | EVEN, no difference beyond the noise |
| host CPU-seconds | 406 | 402 | -0.9% | -42.7 to 35.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 405,730 | 402,197 | -0.9% | -42,747 to 35,680 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 11.2 to 14.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
