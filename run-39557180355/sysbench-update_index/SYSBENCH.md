# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 13.6 | 16.3 | +19.2% | 2.42 to 2.82 | GAIN |
| throughput (transactions a second) | 984 | 983 | -0.1% | -3.25 to 1.13 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -3.25 to 1.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.97 | 2.07 | +4.9% | -0.0897 to 0.284 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.27 | 3.67 | +12.4% | -0.339 to 1.15 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.08 | 1.09 | +1.0% | -0.0213 to 0.0428 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.9% | 3.81 to 16.3 | power given |
| pages holding data, mean (MB) | 118 | 125 | +5.8% | 3.15 to 10.5 | power given |
| pages read from disk into the pool (misses) | 417,037 | 410,656 | -1.5% | -15,510 to 2,748 | shown, not judged |
| host CPU busy (share of the run) | 0.255 | 0.267 | +4.6% | -0.0165 to 0.0398 | EVEN, no difference beyond the noise |
| host CPU-seconds | 448 | 468 | +4.5% | -28.9 to 69.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 73.7 | 63.9 | -13.3% | -24.4 to 4.8 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
