# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 291 | -1.2% | -6.62 to -0.283 | LOSS |
| throughput (transactions a second) | 295 | 292 | -1.2% | -6.9 to -0.0355 | LOSS |
| queries a second | 4,723 | 4,667 | -1.2% | -110 to -0.569 | LOSS |
| latency, 95th percentile (ms) | 4.88 | 4.88 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 6.63 | 6.55 | -1.2% | -0.424 to 0.264 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.26 | 3.29 | +0.7% | 0.00256 to 0.045 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -57.5 to 41.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 430 | -3.8% | -113 to 78.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,140 | 245,019 | +0.4% | -39,080 to 40,838 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.191 | +0.2% | -0.007 to 0.00769 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 105 | +0.4% | -3.83 to 4.66 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.36 | +1.6% | -0.034 to 0.106 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
