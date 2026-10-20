# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.4% | -3.26 to 1.15 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.4% | -3.15 to 0.83 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,699 | -0.4% | -50.5 to 13.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.28 | +0.6% | -0.327 to 0.388 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.34 | -0.6% | -0.239 to 0.149 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.36 | 3.36 | +0.1% | -0.0816 to 0.0882 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 520 | +1.6% | -62.4 to 79.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 434 | -3.1% | -102 to 73.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,612 | 235,727 | -4.0% | -66,842 to 47,072 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.196 | +0.6% | -0.00624 to 0.00841 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 108 | +0.7% | -3.51 to 5.08 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.42 | +1.1% | -0.0686 to 0.122 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
