# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 289 | +0.0% | -7.21 to 7.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.1% | -2.09 to 2.86 | EVEN, no difference beyond the noise |
| queries a second | 4,678 | 4,684 | +0.1% | -33.4 to 45.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.65 | 6.18 | -7.0% | -3.31 to 2.38 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.61 | 8.71 | +1.1% | -4.55 to 4.73 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.27 | 3.84 | -10.2% | -1.78 to 0.91 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 918 | +617.2% | 486 to 1,095 | power given |
| pages holding data, mean (MB) | 120 | 819 | +580.6% | 452 to 945 | power given |
| pages read from disk into the pool (misses) | 585,871 | 117,732 | -79.9% | -563,270 to -373,007 | shown, not judged |
| host CPU busy (share of the run) | 0.321 | 0.291 | -9.3% | -0.127 to 0.0674 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 173 | -9.2% | -75.2 to 40 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.3 | 3.91 | -9.2% | -1.77 to 0.983 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
