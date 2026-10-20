# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | -0.3% | -3.74 to 2.09 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 291 | -0.3% | -4.18 to 2.5 | EVEN, no difference beyond the noise |
| queries a second | 4,670 | 4,657 | -0.3% | -66.9 to 40 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.75 | 3.7 | -1.2% | -0.583 to 0.492 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.92 | 5.96 | +0.7% | -1.74 to 1.82 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.08 | 2.09 | +0.4% | -0.281 to 0.297 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 467 | -8.9% | -67.6 to -23.2 | GAIN |
| pages holding data, mean (MB) | 446 | 399 | -10.5% | -98.2 to 4.51 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 247,182 | 258,301 | +4.5% | -20,872 to 43,109 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.167 | +1.3% | 0.000519 to 0.00391 | power given |
| host CPU-seconds | 102 | 103 | +1.3% | 0.296 to 2.46 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.31 | +1.6% | -0.00887 to 0.0823 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
