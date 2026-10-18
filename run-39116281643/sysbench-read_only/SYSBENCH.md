# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -2.43 to 3.53 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -2.54 to 3.61 | EVEN, no difference beyond the noise |
| queries a second | 4,713 | 4,722 | +0.2% | -40.6 to 57.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.15 | -2.4% | -0.203 to 0.00223 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.06 | 5.95 | -1.8% | -0.37 to 0.156 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.23 | 3.19 | -1.3% | -0.142 to 0.058 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 478 | -6.6% | -126 to 57.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 434 | -6.0% | -95.8 to 40.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,806 | 715,824 | +9.5% | -189,353 to 313,389 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.191 | -0.8% | -0.00714 to 0.00417 | EVEN, no difference beyond the noise |
| host CPU-seconds | 319 | 317 | -0.6% | -11.4 to 7.42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.35 | -0.8% | -0.104 to 0.067 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 12.7 to 21.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
