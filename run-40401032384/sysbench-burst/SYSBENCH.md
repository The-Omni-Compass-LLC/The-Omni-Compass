# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 288 | -0.7% | -9.38 to 5.56 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 290 | -0.8% | -9.88 to 5.19 | EVEN, no difference beyond the noise |
| queries a second | 4,675 | 4,637 | -0.8% | -158 to 83 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.92 | 5.77 | -2.4% | -0.762 to 0.475 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.8 | 7.61 | -2.4% | -0.373 to 0.00533 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.56 | 3.6 | +0.9% | -0.242 to 0.304 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 491 | -4.0% | -22.3 to -18.7 | GAIN |
| pages holding data, mean (MB) | 442 | 435 | -1.7% | -15 to 0.208 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 168,383 | 171,480 | +1.8% | -2,032 to 8,224 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.219 | +2.6% | -0.0174 to 0.0286 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.3 | 81.6 | +3.0% | -6.5 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.65 | 2.74 | +3.7% | -0.165 to 0.359 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 5 to 5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
