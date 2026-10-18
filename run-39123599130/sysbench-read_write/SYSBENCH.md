# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | -0.3% | -3.48 to 2.48 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.4% | -2.44 to 0.772 | EVEN, no difference beyond the noise |
| queries a second | 3,939 | 3,922 | -0.4% | -48.9 to 15.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.13 | 8.08 | -0.6% | -0.81 to 0.71 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.2 | 11.8 | -2.9% | -2.08 to 1.37 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.22 | 5.13 | -1.8% | -0.485 to 0.297 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 527 | +2.9% | -85.4 to 116 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 469 | +1.4% | -63 to 76 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,440 | 596,237 | -3.0% | -175,700 to 139,296 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.207 | -3.1% | -0.0336 to 0.0202 | EVEN, no difference beyond the noise |
| host CPU-seconds | 343 | 333 | -3.0% | -53.8 to 33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.88 | 3.77 | -2.8% | -0.616 to 0.401 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 9.39 to 26.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
