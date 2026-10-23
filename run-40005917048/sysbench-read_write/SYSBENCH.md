# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 179 | +0.4% | -2.45 to 3.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.0% | -1.5 to 1.35 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,922 | -0.0% | -30 to 27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 13.1 | 12.9 | -1.1% | -1.59 to 1.31 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 18.6 | 18 | -3.4% | -2.76 to 1.49 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.56 | 6.46 | -1.5% | -0.602 to 0.403 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.6% | 11.5 to 15.5 | power given |
| pages holding data, mean (MB) | 122 | 134 | +10.1% | 11 to 13.6 | power given |
| pages read from disk into the pool (misses) | 1,665,825 | 1,591,692 | -4.5% | -156,928 to 8,663 | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.26 | -2.4% | -0.0317 to 0.019 | EVEN, no difference beyond the noise |
| host CPU-seconds | 429 | 419 | -2.4% | -49.6 to 29.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.27 | 5.13 | -2.7% | -0.709 to 0.428 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 8.9 to 11.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
