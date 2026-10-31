# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.68 | 14.6 | +90.5% | 3.86 to 10 | GAIN |
| throughput (transactions a second) | 984 | 984 | +0.1% | -5.73 to 7.25 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | +0.1% | -5.73 to 7.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.82 | 1.5 | -18.0% | -0.486 to -0.172 | GAIN |
| latency, 99th percentile (ms) | 2.76 | 2.2 | -20.4% | -0.776 to -0.352 | GAIN |
| latency, mean (ms) | 1.06 | 0.979 | -7.7% | -0.129 to -0.0347 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,257 | +882.4% | 1,032 to 1,227 | power given |
| pages holding data, mean (MB) | 117 | 862 | +636.0% | 716 to 774 | power given |
| pages read from disk into the pool (misses) | 418,080 | 87,632 | -79.0% | -379,077 to -281,820 | shown, not judged |
| host CPU busy (share of the run) | 0.262 | 0.231 | -11.9% | -0.0546 to -0.00788 | GAIN |
| host CPU-seconds | 459 | 404 | -12.0% | -95.4 to -14.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 131 | 60.8 | -53.5% | -84.8 to -55.3 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
