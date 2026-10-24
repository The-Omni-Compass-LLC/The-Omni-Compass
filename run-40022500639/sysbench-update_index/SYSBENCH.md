# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 233 | 223 | -4.4% | -137 to 117 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -7.58 to 5.21 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -7.58 to 5.21 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 45.6 | 51 | +11.9% | -151 to 162 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 154 | 169 | +9.4% | -196 to 225 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 8.01 | 9.85 | +23.0% | -19.2 to 22.9 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 355 | -30.6% | -267 to -46.6 | GAIN |
| pages holding data, mean (MB) | 452 | 298 | -34.2% | -251 to -57.8 | GAIN |
| pages read from disk into the pool (misses) | 190,326 | 294,747 | +54.9% | 43,111 to 165,730 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.14 | +2.0% | -0.0186 to 0.0241 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 247 | +2.0% | -32.7 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.49 | +6.2% | -1.36 to 1.65 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 8.52 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
