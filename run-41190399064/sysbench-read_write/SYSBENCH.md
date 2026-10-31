# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 179 | 196 | +9.4% | 14.3 to 19.3 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | -2.44 to 3.55 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,934 | +0.3% | -48.9 to 71.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.9 | 7.39 | -42.8% | -5.98 to -5.06 | GAIN |
| latency, 99th percentile (ms) | 18.2 | 9.74 | -46.4% | -8.9 to -7.97 | GAIN |
| latency, mean (ms) | 6.29 | 5.1 | -18.9% | -1.35 to -1.03 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,060 | +728.3% | 788 to 1,077 | power given |
| pages holding data, mean (MB) | 121 | 936 | +674.7% | 737 to 893 | power given |
| pages read from disk into the pool (misses) | 1,663,808 | 169,958 | -89.8% | -1,648,515 to -1,339,185 | shown, not judged |
| host CPU busy (share of the run) | 0.315 | 0.272 | -13.8% | -0.055 to -0.0321 | GAIN |
| host CPU-seconds | 554 | 477 | -13.9% | -96.8 to -57.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.77 | 5.33 | -21.3% | -1.67 to -1.21 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
