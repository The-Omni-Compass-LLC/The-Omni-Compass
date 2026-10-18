# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -1.15 to 3.01 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.2% | -1.75 to 3.11 | EVEN, no difference beyond the noise |
| queries a second | 4,679 | 4,690 | +0.2% | -28 to 49.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.37 | 3.21 | -4.7% | -0.34 to 0.0217 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.18 | 4.91 | -5.2% | -0.488 to -0.0558 | GAIN |
| latency, mean (ms) | 1.87 | 1.85 | -0.7% | -0.0382 to 0.0119 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 428 | -16.5% | -157 to -11.7 | GAIN |
| pages holding data, mean (MB) | 445 | 360 | -19.1% | -144 to -25.6 | GAIN |
| pages read from disk into the pool (misses) | 245,342 | 268,684 | +9.5% | -10,130 to 56,813 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.142 | +0.9% | -0.0037 to 0.00633 | EVEN, no difference beyond the noise |
| host CPU-seconds | 85.7 | 86.5 | +0.9% | -2.43 to 4.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.91 | 1.92 | +0.6% | -0.0447 to 0.0677 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
