# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 392 | 395 | +0.9% | -44.4 to 51.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 989 | 990 | +0.1% | -2.05 to 3.85 | EVEN, no difference beyond the noise |
| queries a second | 989 | 990 | +0.1% | -2.05 to 3.85 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.79 | 3.01 | +7.8% | -0.784 to 1.22 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 8.22 | +46.7% | -4.2 to 9.44 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.943 | 1.06 | +11.9% | -0.227 to 0.452 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 454 | 450 | -0.7% | -21.3 to 14.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,380 | 187,151 | -1.2% | -9,838 to 5,380 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.104 | -1.4% | -0.0127 to 0.0097 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 183 | -1.4% | -22.1 to 16.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.05 | 1.04 | -1.7% | -0.263 to 0.226 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
