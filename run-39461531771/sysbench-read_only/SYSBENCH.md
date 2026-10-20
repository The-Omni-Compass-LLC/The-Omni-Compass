# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -1.5 to 0.526 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -1.66 to 0.773 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,713 | -0.1% | -26.5 to 12.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 3.84 | -4.1% | -0.266 to -0.0638 | GAIN |
| latency, 99th percentile (ms) | 5.54 | 5.44 | -1.8% | -0.35 to 0.149 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.06 | 2.97 | -3.1% | -0.129 to -0.0585 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.0% | 5.73 to 12.2 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.7% | 11.9 to 18.6 | power given |
| pages read from disk into the pool (misses) | 1,971,673 | 1,901,083 | -3.6% | -128,365 to -12,816 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.232 | -2.9% | -0.00959 to -0.00432 | GAIN |
| host CPU-seconds | 425 | 413 | -2.9% | -16.8 to -7.68 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.16 | 3.07 | -2.7% | -0.13 to -0.0401 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
