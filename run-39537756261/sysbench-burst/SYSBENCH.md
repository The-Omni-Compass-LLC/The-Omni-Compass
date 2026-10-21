# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.6% | -4.85 to 1.52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.6% | -3.93 to 0.479 | EVEN, no difference beyond the noise |
| queries a second | 4,710 | 4,682 | -0.6% | -62.9 to 7.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.18 | -2.4% | -0.484 to 0.232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.17 | -2.3% | -1.2 to 0.858 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.35 | 3.33 | -0.6% | -0.068 to 0.0255 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 496 | -3.1% | -46.1 to 14.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 416 | -7.0% | -114 to 50.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,031 | 251,269 | +3.0% | -14,194 to 28,669 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.195 | +0.4% | -0.00101 to 0.00253 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 108 | +0.6% | -0.42 to 1.75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.41 | +1.2% | -0.000432 to 0.0569 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
