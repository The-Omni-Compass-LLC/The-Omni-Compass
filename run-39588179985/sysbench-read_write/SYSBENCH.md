# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 169 | 170 | +0.6% | -5.27 to 7.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | +0.2% | -2.85 to 3.47 | EVEN, no difference beyond the noise |
| queries a second | 3,903 | 3,909 | +0.2% | -57.1 to 69.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 16.2 | 15.8 | -2.4% | -2.23 to 1.45 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 278 | 226 | -18.8% | -204 to 99.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 12.2 | 10.3 | -15.8% | -6.08 to 2.22 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.4% | 5.17 to 23.9 | power given |
| pages holding data, mean (MB) | 122 | 136 | +11.3% | 5.46 to 22.2 | power given |
| pages read from disk into the pool (misses) | 1,661,561 | 1,602,907 | -3.5% | -125,574 to 8,267 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.248 | -0.4% | -0.00592 to 0.00404 | EVEN, no difference beyond the noise |
| host CPU-seconds | 449 | 447 | -0.3% | -11.3 to 8.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.77 | 5.72 | -1.0% | -0.389 to 0.272 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 6.46 to 12.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
