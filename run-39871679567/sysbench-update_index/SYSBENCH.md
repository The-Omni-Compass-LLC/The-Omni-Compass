# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 10.5 | 7.54 | -28.0% | -8.92 to 3.06 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | +0.0% | -12.7 to 13.3 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | +0.0% | -12.7 to 13.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.73 | 1.74 | +0.4% | -0.432 to 0.446 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.54 | 4.57 | +0.6% | -0.49 to 0.542 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.08 | 1.09 | +0.8% | -0.0952 to 0.113 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 585 | +14.2% | -167 to 313 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 475 | +4.8% | -92.9 to 137 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,426 | 178,835 | -5.6% | -50,905 to 29,723 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.121 | +3.8% | -0.0417 to 0.0507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 180 | 187 | +3.8% | -63.8 to 77.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 42 | 57.1 | +35.8% | -11.9 to 42.1 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 6.63 to 26.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
