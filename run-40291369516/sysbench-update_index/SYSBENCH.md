# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 73.5 | 76.6 | +4.2% | -11.4 to 17.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -4.33 to 2.74 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -4.33 to 2.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 153 | 134 | -12.6% | -72.4 to 34 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 420 | 295 | -29.8% | -324 to 74 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 29.4 | 23.6 | -19.7% | -17.1 to 5.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 455 | 451 | -0.9% | -15.1 to 6.67 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,085 | 188,631 | -0.8% | -9,848 to 6,940 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.136 | -3.4% | -0.0292 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 249 | 241 | -3.4% | -50 to 33.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 7.6 | 7.15 | -5.9% | -0.855 to -0.0392 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
