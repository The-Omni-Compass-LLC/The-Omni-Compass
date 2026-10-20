# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 189 | -1.4% | -18.7 to 13.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.1% | -1.42 to 1.8 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,952 | +0.1% | -28.4 to 36.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.11 | 11.4 | +61.1% | -10.1 to 18.8 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 28.2 | 47 | +66.7% | -72.9 to 111 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.6 | 4.44 | +23.1% | -2.78 to 4.45 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 555 | +8.4% | -89.5 to 176 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 460 | 497 | +8.0% | -76.2 to 150 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,199 | 545,094 | -11.5% | -330,758 to 188,548 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.14 | +1.3% | -0.0128 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 245 | 249 | +1.3% | -22.6 to 29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.81 | 2.89 | +2.8% | -0.236 to 0.395 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 12.5 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
