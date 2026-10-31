# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,945 | +0.1% | -4.6 to 7.62 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,953 | +0.1% | -5.43 to 11 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,953 | +0.1% | -5.43 to 11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.352 | 0.348 | -1.2% | -0.0282 to 0.0195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.47 | +2.5% | -0.0314 to 0.0541 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.208 | -4.0% | -0.0244 to 0.00706 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 574 | +348.8% | -25.3 to 918 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 516 | +325.6% | 19.2 to 770 | power given |
| pages read from disk into the pool (misses) | 1,029,862 | 335,919 | -67.4% | -1,163,981 to -223,904 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.166 | -3.7% | -0.0196 to 0.00695 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 293 | -3.7% | -34.7 to 12.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.226 | 0.217 | -3.7% | -0.0262 to 0.00947 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | -0.535 to 5.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
