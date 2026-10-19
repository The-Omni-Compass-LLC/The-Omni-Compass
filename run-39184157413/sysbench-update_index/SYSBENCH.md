# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.0145 | 0.0159 | +10.0% | -0.021 to 0.0239 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 975 | 975 | -0.1% | -9.35 to 8.25 | EVEN, no difference beyond the noise |
| queries a second | 975 | 975 | -0.1% | -9.35 to 8.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.88 | 1.81 | -3.6% | -0.224 to 0.087 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.55 | 3.33 | -6.1% | -1.34 to 0.907 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.52 | 1.47 | -3.7% | -1.15 to 1.04 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.3% | -168 to 134 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 432 | -4.8% | -161 to 117 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,661 | 204,620 | +7.9% | -46,472 to 76,390 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.159 | -3.0% | -0.018 to 0.00825 | EVEN, no difference beyond the noise |
| host CPU-seconds | 294 | 285 | -3.0% | -32.6 to 15.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 48,677 | 45,413 | -6.7% | -91,296 to 84,768 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 10.2 to 20.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
