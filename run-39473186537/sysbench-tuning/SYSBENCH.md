# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,958 | 2,962 | +0.1% | -3.68 to 11.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,962 | 2,966 | +0.1% | 1.41 to 4.82 | GAIN |
| queries a second | 2,962 | 2,966 | +0.1% | 1.41 to 4.82 | GAIN |
| latency, 95th percentile (ms) | 0.205 | 0.205 | -0.2% | -0.0161 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.35 | 0.35 | +0.0% | 0 to 0 | EVEN, the same |
| latency, mean (ms) | 0.139 | 0.153 | +9.8% | -0.0379 to 0.0652 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 454 | -11.4% | -148 to 31.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 414 | -10.8% | -146 to 46.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,983 | 440,264 | +19.6% | -79,762 to 224,324 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.11 | +1.0% | 5.51e-05 to 0.00217 | power given |
| host CPU-seconds | 193 | 195 | +1.0% | 0.323 to 3.58 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.144 | +0.9% | -0.000186 to 0.00269 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 3.43 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
