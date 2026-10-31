# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.4% | -3.1 to 4.63 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.0% | -4.02 to 4.08 | EVEN, no difference beyond the noise |
| queries a second | 3,919 | 3,919 | +0.0% | -80.5 to 81.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.83 | 5.54 | -18.9% | -1.56 to -1.02 | GAIN |
| latency, 99th percentile (ms) | 9.79 | 7.3 | -25.5% | -2.66 to -2.33 | GAIN |
| latency, mean (ms) | 4.36 | 4.09 | -6.1% | -0.386 to -0.144 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,076 | +110.3% | 376 to 753 | power given |
| pages holding data, mean (MB) | 463 | 931 | +101.0% | 302 to 634 | power given |
| pages read from disk into the pool (misses) | 622,118 | 134,276 | -78.4% | -520,654 to -455,029 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.227 | -7.0% | -0.0208 to -0.0134 | GAIN |
| host CPU-seconds | 444 | 412 | -7.0% | -38.7 to -23.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.95 | 4.59 | -7.4% | -0.484 to -0.247 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
