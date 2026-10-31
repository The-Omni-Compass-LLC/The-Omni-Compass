# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,952 | +0.3% | -41.7 to 59 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,966 | +0.1% | -11.4 to 15.8 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,966 | +0.1% | -11.4 to 15.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.27 | 0.249 | -7.9% | -0.0802 to 0.0376 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.9 | 0.383 | -92.2% | -24 to 15 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 0.397 | -66.8% | -4.86 to 3.26 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,148 | +797.0% | 948 to 1,092 | power given |
| pages holding data, mean (MB) | 121 | 909 | +650.2% | 774 to 802 | power given |
| pages read from disk into the pool (misses) | 1,033,469 | 97,579 | -90.6% | -975,155 to -896,624 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.12 | -6.8% | -0.0127 to -0.00484 | GAIN |
| host CPU-seconds | 228 | 213 | -6.8% | -22.2 to -8.86 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.17 | 0.158 | -7.0% | -0.0167 to -0.00724 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 3.5 to 13.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
