# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 112 | 104 | -7.1% | -58.1 to 42.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.0% | -1.25 to 1.35 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,934 | +0.0% | -25 to 27.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 365 | 419 | +15.0% | -132 to 241 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 741 | 916 | +23.6% | -372 to 722 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 71.3 | 82.9 | +16.4% | -44.9 to 68.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 144 | +12.6% | 7.99 to 24.3 | power given |
| pages holding data, mean (MB) | 122 | 137 | +12.1% | 6.76 to 22.9 | power given |
| pages read from disk into the pool (misses) | 1,660,503 | 1,583,670 | -4.6% | -152,575 to -1,090 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.211 | -0.4% | -0.00279 to 0.000885 | EVEN, no difference beyond the noise |
| host CPU-seconds | 379 | 377 | -0.4% | -4.92 to 1.76 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 7.56 | 7.97 | +5.4% | -3.01 to 3.83 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 6.52 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
