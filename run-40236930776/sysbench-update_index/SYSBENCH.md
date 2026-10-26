# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158 | 137 | -13.4% | -108 to 66 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -3.85 to 2.87 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -3.85 to 2.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.32 | 2.18 | -6.4% | -0.636 to 0.34 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.92 | 4.52 | -8.0% | -1.41 to 0.618 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.06 | +1.6% | -0.187 to 0.221 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 128 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 117 | 118 | +0.8% | -4.18 to 5.98 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,683 | 414,343 | -0.3% | -9,349 to 6,667 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.146 | +2.0% | -0.00894 to 0.0146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 252 | 257 | +2.0% | -15.8 to 25.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.62 | 4.22 | +16.7% | -1.98 to 3.18 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
