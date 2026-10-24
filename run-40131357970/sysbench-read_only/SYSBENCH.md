# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 293 | +0.9% | -0.198 to 5.51 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.4% | -1.45 to 3.95 | EVEN, no difference beyond the noise |
| queries a second | 4,681 | 4,701 | +0.4% | -23.2 to 63.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.86 | 2.86 | -0.0% | -0.128 to 0.128 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 54.2 | 4.74 | -91.3% | -262 to 163 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.46 | 2.32 | -48.0% | -11.6 to 7.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.2% | 3.08 to 10.2 | power given |
| pages holding data, mean (MB) | 120 | 132 | +10.1% | 5.92 to 18.3 | power given |
| pages read from disk into the pool (misses) | 1,974,271 | 1,925,685 | -2.5% | -122,673 to 25,501 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.165 | +0.3% | -0.0016 to 0.00255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 300 | 301 | +0.3% | -2.87 to 4.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.25 | 2.23 | -0.6% | -0.0643 to 0.0357 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
