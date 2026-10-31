# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 155 | 159 | +2.3% | -10.6 to 17.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.0% | -1.64 to 1.54 | EVEN, no difference beyond the noise |
| queries a second | 3,950 | 3,949 | -0.0% | -32.9 to 30.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 183 | 116 | -36.7% | -238 to 104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 529 | 433 | -18.3% | -289 to 95.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 34.9 | 26.1 | -25.4% | -31.1 to 13.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,239 | +867.6% | 976 to 1,245 | power given |
| pages holding data, mean (MB) | 121 | 1,011 | +735.2% | 841 to 939 | power given |
| pages read from disk into the pool (misses) | 1,667,004 | 140,148 | -91.6% | -1,804,172 to -1,249,540 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.175 | -17.6% | -0.0452 to -0.0297 | GAIN |
| host CPU-seconds | 377 | 310 | -17.7% | -80 to -53 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.34 | 4.31 | -19.4% | -1.23 to -0.847 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 6.04 to 24 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 11.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
