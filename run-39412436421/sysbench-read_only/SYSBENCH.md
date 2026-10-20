# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 293 | +0.7% | -5.85 to 9.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.5% | -2.5 to 5.68 | EVEN, no difference beyond the noise |
| queries a second | 4,729 | 4,755 | +0.5% | -40 to 90.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.84 | +0.6% | -0.129 to 0.163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 26.1 | 16.5 | -36.9% | -54.1 to 34.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3 | 2.76 | -8.3% | -1.17 to 0.677 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +4.6% | 2.16 to 9.54 | power given |
| pages holding data, mean (MB) | 120 | 131 | +9.5% | 5.85 to 16.8 | power given |
| pages read from disk into the pool (misses) | 1,975,286 | 1,933,564 | -2.1% | -94,019 to 10,576 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.166 | +0.6% | -0.00592 to 0.00792 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 297 | +0.6% | -10.7 to 14.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.22 | 2.22 | -0.1% | -0.0375 to 0.0318 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
