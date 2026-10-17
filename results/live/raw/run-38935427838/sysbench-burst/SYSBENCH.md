# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.4% | -5.81 to 7.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -4.89 to 6.77 | EVEN, no difference beyond the noise |
| queries a second | 4,697 | 4,713 | +0.3% | -78.2 to 108 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.43 | 2.53 | +3.7% | -0.131 to 0.313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.89 | 4.06 | +4.4% | -0.0541 to 0.394 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.27 | +2.8% | -0.109 to 0.179 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 329 | -35.7% | -334 to -30.9 | GAIN |
| pages holding data, mean (MB) | 442 | 285 | -35.4% | -300 to -12.8 | GAIN |
| pages read from disk into the pool (misses) | 239,667 | 313,631 | +30.9% | -7,238 to 155,165 | shown, not judged |
| host CPU busy (share of the run) | 0.0917 | 0.093 | +1.5% | -0.00125 to 0.00396 | EVEN, no difference beyond the noise |
| host CPU-seconds | 55.1 | 55.8 | +1.4% | -0.775 to 2.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.23 | 1.25 | +1.1% | -0.0216 to 0.0483 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
