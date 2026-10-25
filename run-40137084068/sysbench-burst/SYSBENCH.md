# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -3.25 to 4.38 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.1% | -1.7 to 2.12 | EVEN, no difference beyond the noise |
| queries a second | 4,729 | 4,732 | +0.1% | -27.2 to 33.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.09 | 3 | -3.0% | -0.303 to 0.119 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.82 | 4.83 | +0.0% | -0.868 to 0.872 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.55 | 1.48 | -4.7% | -0.162 to 0.0171 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 393 | -23.3% | -347 to 108 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 442 | 338 | -23.5% | -317 to 109 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,371 | 285,033 | +16.2% | -82,833 to 162,157 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.107 | -0.7% | -0.00294 to 0.0015 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.8 | 64.3 | -0.7% | -1.78 to 0.883 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.44 | 1.43 | -0.9% | -0.0381 to 0.0126 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 0.0313 to 9.97 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
