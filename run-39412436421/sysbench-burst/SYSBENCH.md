# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.5% | -6.95 to 3.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.5% | -6.97 to 4.09 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,692 | -0.5% | -112 to 65.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.34 | 5.31 | -0.6% | -0.393 to 0.33 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.39 | +0.0% | -0.332 to 0.334 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.35 | 3.3 | -1.7% | -0.117 to 0.00178 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.1% | 2.69 to 20.6 | power given |
| pages holding data, mean (MB) | 120 | 137 | +13.9% | 6.41 to 26.9 | power given |
| pages read from disk into the pool (misses) | 581,384 | 535,133 | -8.0% | -99,099 to 6,597 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.251 | -1.9% | -0.0103 to 0.000684 | EVEN, no difference beyond the noise |
| host CPU-seconds | 152 | 149 | -1.9% | -6.27 to 0.384 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.39 | 3.34 | -1.4% | -0.139 to 0.0453 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
