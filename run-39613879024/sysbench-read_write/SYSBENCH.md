# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 178 | +0.4% | -2.62 to 4.03 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.9 to 3.47 | EVEN, no difference beyond the noise |
| queries a second | 3,930 | 3,936 | +0.1% | -58.1 to 69.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 13.3 | 12.9 | -3.0% | -0.732 to -0.0533 | GAIN |
| latency, 99th percentile (ms) | 20.1 | 18.5 | -8.1% | -2.25 to -1 | GAIN |
| latency, mean (ms) | 7.38 | 6.5 | -11.9% | -3.34 to 1.59 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +11.1% | 10.7 to 17.6 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.5% | 9.62 to 18.2 | power given |
| pages read from disk into the pool (misses) | 1,666,212 | 1,595,762 | -4.2% | -116,264 to -24,637 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.256 | +0.8% | -0.00204 to 0.006 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 413 | +0.9% | -2.84 to 9.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.03 | 5.06 | +0.5% | -0.12 to 0.166 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 8.46 to 14.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
