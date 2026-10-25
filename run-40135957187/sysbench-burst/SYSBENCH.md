# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | +0.0% | -4.75 to 4.89 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -4.13 to 3.87 | EVEN, no difference beyond the noise |
| queries a second | 4,719 | 4,717 | -0.0% | -66 to 62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.06 | 5.88 | -2.9% | -0.737 to 0.38 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.69 | 8.58 | -1.2% | -0.692 to 0.486 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.49 | 3.48 | -0.4% | -0.109 to 0.0786 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 524 | +2.3% | -53.4 to 77.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 442 | -1.4% | -121 to 108 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,517 | 238,167 | -1.8% | -70,607 to 61,907 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.201 | +0.7% | -0.0129 to 0.0158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 111 | +0.7% | -8.53 to 10.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.47 | 2.49 | +0.8% | -0.212 to 0.253 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 2.87 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
