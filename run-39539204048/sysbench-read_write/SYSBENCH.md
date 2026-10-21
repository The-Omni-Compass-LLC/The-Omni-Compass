# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | +0.0% | -0.966 to 1.08 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | -0.1% | -2.03 to 1.5 | EVEN, no difference beyond the noise |
| queries a second | 3,956 | 3,951 | -0.1% | -40.6 to 29.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.75 | 6.55 | -2.9% | -0.528 to 0.132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.4 | 10.7 | -6.7% | -2.82 to 1.3 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.26 | 3.13 | -4.0% | -0.158 to -0.105 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.6% | 6.66 to 17.9 | power given |
| pages holding data, mean (MB) | 121 | 133 | +10.1% | 5.98 to 18.5 | power given |
| pages read from disk into the pool (misses) | 1,670,485 | 1,605,603 | -3.9% | -198,811 to 69,047 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.147 | -3.4% | -0.0158 to 0.00544 | EVEN, no difference beyond the noise |
| host CPU-seconds | 271 | 262 | -3.4% | -28.1 to 9.88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.04 | 2.94 | -3.4% | -0.328 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
