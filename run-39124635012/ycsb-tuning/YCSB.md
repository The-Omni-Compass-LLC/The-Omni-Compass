# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,931 | 2,929 | -0.1% | -3.69 to 0.665 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,935 | -0.1% | -3.46 to 0.278 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.225 | 0.23 | +2.2% | -0.0147 to 0.0247 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.395 | 0.398 | +0.6% | -0.0259 to 0.0306 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.105 | 0.104 | -1.3% | -0.00592 to 0.00324 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -18.8 to 5.55 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -0.9% | -14.5 to 6.56 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 688,175 | 701,871 | +2.0% | -11,949 to 39,342 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.13 | -10.0% | -0.0567 to 0.0278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 266 | 235 | -11.8% | -123 to 60.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.199 | 0.176 | -11.8% | -0.0921 to 0.0452 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
