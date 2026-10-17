# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 190 | -0.4% | -1.41 to -0.154 | LOSS |
| throughput (transactions a second) | 197 | 196 | -0.4% | -1.22 to -0.232 | LOSS |
| queries a second | 3,935 | 3,920 | -0.4% | -24.4 to -4.65 | LOSS |
| latency, 95th percentile (ms) | 9.06 | 9 | -0.6% | -0.286 to 0.178 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.3 | 13.5 | +1.8% | -0.36 to 0.844 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.51 | 5.48 | -0.6% | -0.204 to 0.137 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 541 | +5.6% | -6.68 to 63.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 483 | +4.6% | 11 to 31.4 | power given |
| pages read from disk into the pool (misses) | 617,955 | 570,854 | -7.6% | -75,922 to -18,278 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.216 | -1.7% | -0.0106 to 0.00311 | EVEN, no difference beyond the noise |
| host CPU-seconds | 354 | 348 | -1.6% | -16.8 to 5.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.04 | 3.99 | -1.2% | -0.186 to 0.0891 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 4.06 to 23.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
