# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.000724 | 0 | -100.0% | -0.00384 to 0.00239 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 978 | 978 | +0.0% | -3.47 to 4.19 | EVEN, no difference beyond the noise |
| queries a second | 978 | 978 | +0.0% | -3.47 to 4.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.05 | 2.03 | -0.7% | -0.314 to 0.285 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.29 | 3.33 | +1.4% | -1.18 to 1.27 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.38 | -1.9% | -0.213 to 0.159 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 555 | +8.3% | -71.2 to 156 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 458 | +0.9% | -84.2 to 92.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,700 | 187,033 | -1.4% | -70,634 to 65,301 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.208 | -0.5% | -0.0202 to 0.0181 | EVEN, no difference beyond the noise |
| host CPU-seconds | 373 | 371 | -0.5% | -35.9 to 32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 373,167 | 371,203 | -0.5% | -35,916 to 31,989 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
