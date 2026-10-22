# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | -0.1% | -4.1 to 3.35 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -4.1 to 3.51 | EVEN, no difference beyond the noise |
| queries a second | 4,743 | 4,738 | -0.1% | -65.6 to 56.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.83 | 1.85 | +0.6% | -0.197 to 0.221 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.86 | 3.73 | -3.6% | -0.48 to 0.203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.28 | +0.6% | -0.158 to 0.173 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | 1.61 to 13.3 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.6% | 8.64 to 21.7 | power given |
| pages read from disk into the pool (misses) | 1,979,125 | 1,914,811 | -3.2% | -148,143 to 19,513 | shown, not judged |
| host CPU busy (share of the run) | 0.0998 | 0.1 | +0.4% | -0.015 to 0.0157 | EVEN, no difference beyond the noise |
| host CPU-seconds | 179 | 180 | +0.4% | -26.8 to 28.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.33 | +0.5% | -0.18 to 0.193 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
