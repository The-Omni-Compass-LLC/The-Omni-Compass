# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 164 | -7.8% | -99 to 71 | no difference beyond the noise |
| throughput (transactions a second) | 979 | 980 | +0.1% | -13.9 to 16.3 | no difference beyond the noise |
| queries a second | 979 | 980 | +0.1% | -13.9 to 16.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 95.3 | 111 | +16.2% | -164 to 195 | no difference beyond the noise |
| latency, 99th percentile (ms) | 217 | 237 | +9.5% | -353 to 394 | no difference beyond the noise |
| latency, mean (ms) | 14.8 | 17.7 | +19.7% | -27.1 to 32.9 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 391 | -23.6% | -269 to 27.1 | no difference beyond the noise |
| pages holding data, mean (MB) | 450 | 318 | -29.2% | -315 to 52.2 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 140,032 | 191,350 | +36.6% | -13,303 to 115,940 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.144 | +1.3% | -0.0229 to 0.0266 | no difference beyond the noise |
| host CPU-seconds | 168 | 170 | +1.4% | -27.2 to 31.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.18 | 3.42 | +7.5% | -1.67 to 2.14 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 6.08 to 21.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
