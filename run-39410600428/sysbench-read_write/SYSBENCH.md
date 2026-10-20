# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.1% | -0.441 to 0.869 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.4% | -0.304 to 1.84 | EVEN, no difference beyond the noise |
| queries a second | 3,936 | 3,951 | +0.4% | -6.07 to 36.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.33 | 8.43 | +1.2% | -0.478 to 0.681 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.4 | 12.8 | +3.0% | -1.02 to 1.77 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.28 | 5.3 | +0.4% | -0.00971 to 0.0507 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 528 | +3.1% | 5.84 to 26 | power given |
| pages holding data, mean (MB) | 462 | 472 | +2.2% | -4.62 to 24.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,658 | 586,919 | -4.8% | -125,453 to 65,974 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.214 | +0.0% | -0.00583 to 0.00591 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 344 | +0.1% | -9.3 to 9.87 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.89 | 3.89 | -0.0% | -0.1 to 0.0988 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 4.99 to 25.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
