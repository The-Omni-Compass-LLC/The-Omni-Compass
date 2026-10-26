# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 69.9 | 62.8 | -10.1% | -29.3 to 15.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 195 | -1.1% | -12.3 to 8.08 | EVEN, no difference beyond the noise |
| queries a second | 3,942 | 3,899 | -1.1% | -246 to 162 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 600 | 1,540 | +156.5% | -2,837 to 4,716 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,454 | 2,591 | +78.2% | -3,533 to 5,808 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 139 | 255 | +82.5% | -306 to 536 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 462 | 459 | -0.6% | -16.2 to 10.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,729 | 601,097 | -2.2% | -65,286 to 38,022 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.193 | -0.9% | -0.0134 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 349 | 346 | -0.6% | -21.3 to 16.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 11.2 | 12.4 | +10.9% | -2.73 to 5.16 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
