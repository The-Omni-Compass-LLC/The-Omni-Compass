# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.2% | 0.158 to 1.03 | GAIN |
| throughput (transactions a second) | 296 | 296 | +0.3% | 0.506 to 0.989 | GAIN |
| queries a second | 4,730 | 4,742 | +0.3% | 8.1 to 15.8 | GAIN |
| latency, 95th percentile (ms) | 2.9 | 2.86 | -1.2% | -0.109 to 0.04 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.49 | 4.6 | +2.4% | -0.196 to 0.41 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.38 | +1.6% | -0.0979 to 0.142 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 403 | -21.2% | -344 to 127 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 444 | 356 | -19.7% | -310 to 134 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,730 | 285,543 | +17.6% | -57,645 to 143,271 | shown, not judged |
| host CPU busy (share of the run) | 0.099 | 0.1 | +1.2% | -0.00266 to 0.00507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 59.4 | 60.1 | +1.2% | -1.6 to 3.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.32 | 1.34 | +1.0% | -0.0361 to 0.0625 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -1.4 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
