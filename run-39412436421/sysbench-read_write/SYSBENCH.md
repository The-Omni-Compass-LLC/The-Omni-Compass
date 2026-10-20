# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 170 | 170 | -0.1% | -3.73 to 3.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 195 | -0.3% | -2.91 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 3,914 | 3,902 | -0.3% | -58.2 to 34.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 15.1 | 14.9 | -1.2% | -0.567 to 0.207 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 20.5 | 20.6 | +0.6% | -1.28 to 1.53 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.16 | 6.17 | +0.1% | -0.177 to 0.183 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.3% | 10.3 to 16 | power given |
| pages holding data, mean (MB) | 121 | 134 | +10.6% | 10.7 to 14.9 | power given |
| pages read from disk into the pool (misses) | 1,668,284 | 1,597,946 | -4.2% | -158,008 to 17,333 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.274 | -1.2% | -0.00658 to 8.48e-05 | EVEN, no difference beyond the noise |
| host CPU-seconds | 509 | 503 | -1.3% | -13.2 to 0.449 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.49 | 6.42 | -1.1% | -0.296 to 0.149 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
