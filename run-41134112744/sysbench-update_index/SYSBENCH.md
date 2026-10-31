# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 163 | 179 | +9.8% | -66.7 to 98.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 989 | +0.1% | -0.168 to 1.54 | EVEN, no difference beyond the noise |
| queries a second | 988 | 989 | +0.1% | -0.168 to 1.54 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.66 | 8.07 | +73.0% | -11.7 to 18.5 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.8 | 24.1 | +63.0% | -40 to 58.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.68 | 2.31 | +37.2% | -3.18 to 4.44 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.5% | 699 to 749 | power given |
| pages holding data, mean (MB) | 455 | 889 | +95.6% | 402 to 467 | power given |
| pages read from disk into the pool (misses) | 192,139 | 71,482 | -62.8% | -129,330 to -111,984 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.117 | -4.3% | -0.0162 to 0.00579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 205 | -4.2% | -28.2 to 10.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.9 | 2.58 | -11.0% | -1.68 to 1.05 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
