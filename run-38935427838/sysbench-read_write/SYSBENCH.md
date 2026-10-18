# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 191 | -0.4% | -4.14 to 2.68 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | +0.0% | -4.06 to 4.11 | EVEN, no difference beyond the noise |
| queries a second | 3,901 | 3,902 | +0.0% | -81.3 to 82.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.3 | 8.03 | +10.1% | 0.528 to 0.944 | LOSS |
| latency, 99th percentile (ms) | 12.6 | 14.6 | +15.3% | -8.07 to 11.9 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.08 | 4.37 | +7.3% | -0.307 to 0.899 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 405 | -20.9% | -122 to -91.5 | GAIN |
| pages holding data, mean (MB) | 461 | 367 | -20.3% | -107 to -79.9 | GAIN |
| pages read from disk into the pool (misses) | 616,349 | 922,398 | +49.7% | 188,714 to 423,384 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.174 | +2.0% | -0.00285 to 0.00967 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 315 | +1.9% | -5.03 to 17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.49 | 3.57 | +2.4% | -0.0597 to 0.226 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 |  | 11.5 to 17.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
