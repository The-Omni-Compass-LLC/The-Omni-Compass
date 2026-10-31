# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 123 | 167 | +35.4% | 20.8 to 66.2 | GAIN |
| throughput (transactions a second) | 986 | 987 | +0.1% | -1.76 to 4.44 | EVEN, no difference beyond the noise |
| queries a second | 986 | 987 | +0.1% | -1.76 to 4.44 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.35 | 1.13 | -16.1% | -0.415 to -0.018 | GAIN |
| latency, 99th percentile (ms) | 2.15 | 1.63 | -24.0% | -1.29 to 0.261 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.844 | 0.805 | -4.7% | -0.143 to 0.0646 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,240 | +868.7% | 986 to 1,238 | power given |
| pages holding data, mean (MB) | 118 | 869 | +633.6% | 730 to 771 | power given |
| pages read from disk into the pool (misses) | 419,320 | 84,063 | -80.0% | -375,443 to -295,072 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.209 | -11.7% | -0.048 to -0.0072 | GAIN |
| host CPU-seconds | 419 | 370 | -11.7% | -84.4 to -13.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 7.6 | 4.9 | -35.5% | -5.37 to -0.0223 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
