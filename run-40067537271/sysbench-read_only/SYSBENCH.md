# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.1% | -4.68 to 4.03 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -4.66 to 3.91 | EVEN, no difference beyond the noise |
| queries a second | 4,747 | 4,741 | -0.1% | -74.6 to 62.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.66 | 1.63 | -1.8% | -0.181 to 0.12 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.93 | 2.84 | -3.0% | -0.366 to 0.188 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.18 | -1.6% | -0.0887 to 0.0501 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 132 | +3.3% | 0.622 to 7.73 | power given |
| pages holding data, mean (MB) | 120 | 129 | +7.9% | 2.59 to 16.4 | power given |
| pages read from disk into the pool (misses) | 1,995,522 | 1,983,039 | -0.6% | -140,842 to 115,876 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.0947 | -1.2% | -0.00514 to 0.00283 | EVEN, no difference beyond the noise |
| host CPU-seconds | 172 | 170 | -1.2% | -9.37 to 5.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.28 | 1.26 | -1.1% | -0.0769 to 0.0492 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
