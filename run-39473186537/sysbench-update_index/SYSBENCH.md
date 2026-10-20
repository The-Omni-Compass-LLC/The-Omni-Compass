# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 95.9 | 107 | +12.0% | -11.2 to 34.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -3.4 to 1.8 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -3.4 to 1.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.32 | 1.35 | +2.4% | -0.163 to 0.225 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.6 | 12.3 | +16.0% | -29.4 to 32.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.1 | 1.12 | +2.1% | -0.667 to 0.713 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 479 | -6.4% | -67.9 to 2.41 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 408 | -9.8% | -52.8 to -36.1 | GAIN |
| pages read from disk into the pool (misses) | 189,769 | 216,798 | +14.2% | 2,353 to 51,706 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.195 | -2.5% | -0.0293 to 0.0194 | EVEN, no difference beyond the noise |
| host CPU-seconds | 346 | 338 | -2.5% | -50.2 to 33.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.2 | 6.93 | -15.4% | -5.02 to 2.49 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 8.43 to 21.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
