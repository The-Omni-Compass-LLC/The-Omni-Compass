# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.5% | -5.52 to 8.23 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -4.37 to 6.86 | EVEN, no difference beyond the noise |
| queries a second | 4,723 | 4,743 | +0.4% | -69.9 to 110 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.74 | -3.0% | -0.372 to 0.204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.55 | 4.36 | -4.1% | -1.22 to 0.845 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.31 | 1.28 | -2.1% | -0.129 to 0.0756 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +5.9% | 7.53 to 7.53 | power given |
| pages holding data, mean (MB) | 120 | 132 | +10.2% | 3.33 to 21.2 | power given |
| pages read from disk into the pool (misses) | 568,453 | 549,846 | -3.3% | -39,401 to 2,187 | shown, not judged |
| host CPU busy (share of the run) | 0.0943 | 0.0931 | -1.3% | -0.00354 to 0.00111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 56.6 | 55.8 | -1.4% | -2.17 to 0.639 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.26 | 1.24 | -1.8% | -0.0312 to -0.014 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
