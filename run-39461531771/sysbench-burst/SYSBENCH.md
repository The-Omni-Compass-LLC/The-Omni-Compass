# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 291 | -0.5% | -20 to 16.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.2% | -13.6 to 12.4 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,709 | -0.2% | -218 to 198 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.52 | 4.46 | -1.3% | -0.782 to 0.663 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.88 | 21.4 | +140.9% | -51.7 to 76.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.95 | 3.4 | +15.1% | -1.5 to 2.39 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.7% | -0.692 to 20.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 135 | +12.1% | -5.62 to 34.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 577,964 | 557,367 | -3.6% | -61,191 to 19,998 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.204 | -1.9% | -0.0052 to -0.00278 | GAIN |
| host CPU-seconds | 124 | 122 | -1.9% | -2.76 to -1.97 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.78 | 2.74 | -1.4% | -0.2 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
