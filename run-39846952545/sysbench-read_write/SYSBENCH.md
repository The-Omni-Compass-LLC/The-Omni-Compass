# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 191 | -0.8% | -8.84 to 5.66 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.5% | 0.213 to 1.66 | GAIN |
| queries a second | 3,938 | 3,957 | +0.5% | 4.26 to 33.2 | GAIN |
| latency, 95th percentile (ms) | 8.38 | 9.32 | +11.3% | -2.13 to 4.02 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.4 | 35.1 | +143.1% | -58.8 to 100 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.25 | 4.96 | +16.7% | -1.6 to 3.02 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +5.9% | 1.3 to 13.9 | power given |
| pages holding data, mean (MB) | 121 | 128 | +5.7% | 1.18 to 12.7 | power given |
| pages read from disk into the pool (misses) | 1,663,472 | 1,630,116 | -2.0% | -85,584 to 18,872 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.204 | +0.7% | -0.00836 to 0.0113 | EVEN, no difference beyond the noise |
| host CPU-seconds | 358 | 361 | +0.7% | -14.8 to 19.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.08 | 4.14 | +1.6% | -0.102 to 0.23 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
