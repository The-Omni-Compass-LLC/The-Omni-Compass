# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 185 | 184 | -0.4% | -4.23 to 2.73 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.1% | -3.34 to 3.06 | EVEN, no difference beyond the noise |
| queries a second | 3,931 | 3,928 | -0.1% | -66.9 to 61.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.3 | 11.4 | +1.2% | -0.158 to 0.433 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.9 | 16.5 | +3.7% | -0.885 to 2.05 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.88 | 6.37 | +8.3% | -1.52 to 2.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.3% | 9.8 to 16.7 | power given |
| pages holding data, mean (MB) | 121 | 133 | +10.0% | 5.52 to 18.7 | power given |
| pages read from disk into the pool (misses) | 1,666,443 | 1,602,319 | -3.8% | -90,399 to -37,849 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.237 | -0.3% | -0.013 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 382 | 382 | -0.1% | -20.4 to 19.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.52 | 4.53 | +0.3% | -0.262 to 0.287 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
