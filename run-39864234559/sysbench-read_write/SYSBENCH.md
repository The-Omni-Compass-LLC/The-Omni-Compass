# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 194 | +1.3% | -5.23 to 10.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.5% | -0.891 to 2.76 | EVEN, no difference beyond the noise |
| queries a second | 3,938 | 3,957 | +0.5% | -17.8 to 55.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.57 | 6.76 | -10.7% | -3.77 to 2.15 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 22.9 | 16.5 | -28.1% | -35.9 to 23 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.49 | 3.27 | -6.3% | -1.06 to 0.623 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 132 | +3.2% | -2.74 to 11 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 122 | 126 | +3.2% | -0.476 to 8.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,662,445 | 1,643,247 | -1.2% | -88,032 to 49,637 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.142 | -0.2% | -0.0225 to 0.0219 | EVEN, no difference beyond the noise |
| host CPU-seconds | 254 | 253 | -0.2% | -39.5 to 38.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.9 | 2.86 | -1.5% | -0.364 to 0.278 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | -2.4 to 9.07 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
