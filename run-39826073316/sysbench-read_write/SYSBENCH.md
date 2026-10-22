# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 190 | -0.3% | -2.98 to 1.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.3% | -3.01 to 1.97 | EVEN, no difference beyond the noise |
| queries a second | 3,942 | 3,932 | -0.3% | -60.2 to 39.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.79 | 9.73 | -0.6% | -0.308 to 0.192 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.6 | 13.7 | +0.6% | -0.274 to 0.44 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.97 | 4.98 | +0.1% | -0.0343 to 0.0468 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.8% | 7.36 to 20.3 | power given |
| pages holding data, mean (MB) | 118 | 133 | +13.0% | 4.78 to 26 | power given |
| pages read from disk into the pool (misses) | 1,671,308 | 1,593,176 | -4.7% | -147,658 to -8,606 | shown, not judged |
| host CPU busy (share of the run) | 0.282 | 0.281 | -0.4% | -0.00854 to 0.00614 | EVEN, no difference beyond the noise |
| host CPU-seconds | 500 | 498 | -0.4% | -15 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.75 | 5.74 | -0.1% | -0.0884 to 0.0764 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
