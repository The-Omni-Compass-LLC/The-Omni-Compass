# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 100 | 94.5 | -5.5% | -34.6 to 23.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.8% | -0.949 to 4.02 | EVEN, no difference beyond the noise |
| queries a second | 3,917 | 3,948 | +0.8% | -19 to 80.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 563 | 626 | +11.2% | -412 to 538 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,709 | 1,980 | +15.8% | -1,444 to 1,984 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 118 | 133 | +12.2% | -58 to 87 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 147 | +15.1% | 14.8 to 23.9 | power given |
| pages holding data, mean (MB) | 122 | 140 | +14.7% | 11.3 to 24.5 | power given |
| pages read from disk into the pool (misses) | 1,658,388 | 1,581,631 | -4.6% | -121,502 to -32,011 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.214 | -0.2% | -0.00407 to 0.00307 | EVEN, no difference beyond the noise |
| host CPU-seconds | 382 | 382 | -0.2% | -6.12 to 4.48 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.49 | 8.85 | +4.2% | -2.07 to 2.77 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 4.7 to 13.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
