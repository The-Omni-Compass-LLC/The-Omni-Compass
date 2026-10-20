# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11 | 8.6 | -21.7% | -12.5 to 7.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 985 | +0.0% | -5.27 to 5.34 | EVEN, no difference beyond the noise |
| queries a second | 985 | 985 | +0.0% | -5.27 to 5.34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.12 | 2.33 | +9.8% | -1.13 to 1.55 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.19 | 5.33 | +2.7% | -7.41 to 7.69 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.19 | 1.23 | +3.6% | -0.509 to 0.595 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.8% | 5.31 to 22.3 | power given |
| pages holding data, mean (MB) | 119 | 128 | +7.7% | 3.28 to 14.9 | power given |
| pages read from disk into the pool (misses) | 416,168 | 407,051 | -2.2% | -19,806 to 1,572 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.272 | +48.3% | -0.182 to 0.36 | EVEN, no difference beyond the noise |
| host CPU-seconds | 285 | 424 | +48.9% | -285 to 564 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 84.4 | 111 | +31.6% | -178 to 231 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
