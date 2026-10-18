# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -12.8 to 11.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,894 | -0.0% | -10.5 to 9.28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.514 | 0.509 | -0.9% | -0.0147 to 0.00537 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.681 | 0.675 | -1.0% | -0.0468 to 0.0335 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.232 | -1.2% | -0.00757 to 0.00175 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -16.5 to -2.86 | GAIN |
| bytes in the cache, mean (MB) | 403 | 393 | -2.5% | -23.2 to 3.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 265,838 | 273,648 | +2.9% | -12,225 to 27,843 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.155 | -8.9% | -0.0838 to 0.0535 | EVEN, no difference beyond the noise |
| host CPU-seconds | 115 | 103 | -10.3% | -66.5 to 42.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.194 | -10.3% | -0.126 to 0.0811 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
