# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | +0.2% | -3.02 to 3.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.2% | -3.03 to 3.74 | EVEN, no difference beyond the noise |
| queries a second | 3,954 | 3,961 | +0.2% | -60.7 to 74.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.55 | 6.71 | +2.4% | -0.0143 to 0.333 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.3 | 10.4 | +1.2% | -0.142 to 0.386 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.05 | 3.23 | +6.0% | -0.0635 to 0.427 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.1% | -4.24 to 20 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 122 | 128 | +4.9% | -4.77 to 16.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,668,306 | 1,616,831 | -3.1% | -154,325 to 51,373 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.154 | +4.7% | 0.0046 to 0.00931 | power given |
| host CPU-seconds | 261 | 274 | +4.7% | 8.31 to 16.3 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.93 | 3.06 | +4.5% | 0.124 to 0.139 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
