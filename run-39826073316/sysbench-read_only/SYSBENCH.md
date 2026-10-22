# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.2% | -1.96 to 2.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.2% | -1.76 to 2.93 | EVEN, no difference beyond the noise |
| queries a second | 4,711 | 4,720 | +0.2% | -28.1 to 46.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.96 | 3.98 | +0.6% | -0.0793 to 0.127 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.5 | 5.64 | +2.4% | -0.0102 to 0.278 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.01 | 3.06 | +1.5% | -0.0101 to 0.102 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.3% | 4.74 to 11.5 | power given |
| pages holding data, mean (MB) | 120 | 133 | +11.1% | 11.4 to 15.3 | power given |
| pages read from disk into the pool (misses) | 1,980,456 | 1,907,591 | -3.7% | -167,873 to 22,142 | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.238 | +1.5% | -0.00331 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 418 | 424 | +1.5% | -5.81 to 18.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.15 | +1.3% | -0.0223 to 0.105 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
