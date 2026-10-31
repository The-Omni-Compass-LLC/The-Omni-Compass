# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.5% | -1.98 to 4.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.3% | 0.101 to 1.38 | GAIN |
| queries a second | 4,679 | 4,691 | +0.3% | 1.61 to 22.1 | GAIN |
| latency, 95th percentile (ms) | 2.91 | 3 | +3.0% | 0.0166 to 0.16 | LOSS |
| latency, 99th percentile (ms) | 15.4 | 4.97 | -67.8% | -56.4 to 35.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.49 | 2.31 | -33.9% | -6.45 to 4.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 738 | +44.1% | 212 to 239 | power given |
| pages holding data, mean (MB) | 463 | 647 | +39.9% | 172 to 197 | power given |
| pages read from disk into the pool (misses) | 652,196 | 317,340 | -51.3% | -346,937 to -322,775 | shown, not judged |
| host CPU busy (share of the run) | 0.174 | 0.176 | +1.2% | -0.00325 to 0.00742 | EVEN, no difference beyond the noise |
| host CPU-seconds | 319 | 323 | +1.2% | -5.56 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.4 | +0.7% | -0.0259 to 0.0587 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
