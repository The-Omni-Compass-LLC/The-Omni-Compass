# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158 | 192 | +21.9% | -42.9 to 112 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 989 | +0.2% | -2.53 to 6.31 | EVEN, no difference beyond the noise |
| queries a second | 987 | 989 | +0.2% | -2.53 to 6.31 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.53 | 2.48 | -1.8% | -0.242 to 0.149 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.88 | 4.89 | +0.1% | -0.969 to 0.98 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.02 | 1.05 | +2.3% | -0.141 to 0.187 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 450 | -12.0% | -201 to 78.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 381 | -15.8% | -176 to 33.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,589 | 234,966 | +23.9% | -50,883 to 141,637 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.123 | -3.2% | -0.0175 to 0.00932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 217 | -3.2% | -30.8 to 16.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 2.51 | -19.3% | -1.69 to 0.493 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 9.43 to 22.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
