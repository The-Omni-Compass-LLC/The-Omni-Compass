# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -4.73 to 4.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -4.62 to 4.73 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,725 | +0.0% | -73.9 to 75.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.03 | 3.96 | -1.8% | -0.252 to 0.108 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.6 | -1.8% | -0.355 to 0.152 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.03 | 3.01 | -0.8% | -0.0828 to 0.0372 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.4% | -115 to 80.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 446 | -3.5% | -84.9 to 52.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,207 | 664,503 | +1.4% | -210,202 to 228,794 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.238 | -0.6% | -0.0104 to 0.00744 | EVEN, no difference beyond the noise |
| host CPU-seconds | 425 | 423 | -0.6% | -18.5 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.15 | 3.13 | -0.6% | -0.0887 to 0.0498 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 10.4 to 22.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
