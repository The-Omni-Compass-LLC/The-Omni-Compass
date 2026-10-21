# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 272 | 275 | +1.3% | -13.8 to 21.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 297 | +0.6% | -6.12 to 9.44 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,750 | +0.6% | -97.8 to 151 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 68.8 | 41.3 | -40.0% | -152 to 96.9 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 844 | 326 | -61.4% | -3,206 to 2,171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 27.9 | 13 | -53.6% | -94 to 64 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.8% | -1.56 to 29.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 135 | +12.2% | -2.09 to 31.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 575,201 | 537,335 | -6.6% | -50,351 to -25,381 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.176 | +1.3% | -0.0017 to 0.00617 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 105 | +1.3% | -1.1 to 3.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.51 | -0.2% | -0.17 to 0.161 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
