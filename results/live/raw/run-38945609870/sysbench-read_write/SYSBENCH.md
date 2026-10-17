# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | -0.1% | -3.8 to 3.49 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.1% | -3.71 to 3.25 | EVEN, no difference beyond the noise |
| queries a second | 3,906 | 3,901 | -0.1% | -74.3 to 65.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.63 | 7 | +5.5% | -0.437 to 1.17 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 10.1 | +0.0% | -0.457 to 0.457 | EVEN, the same |
| latency, mean (ms) | 3.87 | 3.91 | +0.9% | -0.278 to 0.349 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 433 | -15.5% | -118 to -39.9 | GAIN |
| pages holding data, mean (MB) | 460 | 389 | -15.4% | -86.8 to -55.1 | GAIN |
| pages read from disk into the pool (misses) | 615,649 | 839,244 | +36.3% | 160,195 to 286,995 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.17 | -0.5% | -0.00463 to 0.00281 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 309 | -0.4% | -7.93 to 5.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.48 | 3.46 | -0.4% | -0.11 to 0.0794 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 4.74 to 19.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
