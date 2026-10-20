# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 204 | 246 | +20.5% | -114 to 198 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -6.41 to 5.64 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -6.41 to 5.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.87 | 2.7 | -6.1% | -1.13 to 0.783 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.56 | 5.31 | -19.0% | -7.05 to 4.56 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.08 | 1.02 | -5.7% | -0.376 to 0.252 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 450 | -12.1% | -100 to -23.4 | GAIN |
| pages holding data, mean (MB) | 452 | 380 | -15.9% | -83 to -61.1 | GAIN |
| pages read from disk into the pool (misses) | 189,515 | 230,352 | +21.5% | 13,778 to 67,896 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.119 | -3.4% | -0.0282 to 0.0199 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 210 | -3.3% | -49.3 to 34.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 1.99 | -17.3% | -2.53 to 1.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 7.94 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
