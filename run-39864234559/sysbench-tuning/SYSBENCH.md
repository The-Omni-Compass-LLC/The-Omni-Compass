# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,943 | -0.2% | -22 to 11.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,952 | -0.2% | -18.3 to 8.9 | EVEN, no difference beyond the noise |
| queries a second | 2,956 | 2,952 | -0.2% | -18.3 to 8.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.342 | +0.0% | -0.0298 to 0.0298 | EVEN, the same |
| latency, 99th percentile (ms) | 0.459 | 0.459 | +0.1% | -0.0208 to 0.0215 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.208 | -0.2% | -0.0171 to 0.0163 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +5.9% | 7.41 to 7.62 | power given |
| pages holding data, mean (MB) | 121 | 132 | +8.6% | 9.97 to 11 | power given |
| pages read from disk into the pool (misses) | 1,031,154 | 1,003,551 | -2.7% | -31,012 to -24,195 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.11 | -0.9% | -0.0121 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 183 | -0.9% | -20.3 to 16.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.137 | 0.136 | -0.7% | -0.0155 to 0.0135 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
