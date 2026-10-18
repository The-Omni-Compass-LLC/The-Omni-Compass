# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,918 | 2,918 | +0.0% | -5.64 to 6.06 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,921 | +0.0% | -5.43 to 5.88 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.23 | 0.228 | -0.9% | -0.00697 to 0.00297 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.391 | 0.391 | -0.1% | -0.00659 to 0.00592 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.151 | 0.15 | -0.6% | -0.022 to 0.0202 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -4.45 to 0.169 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 415 | -1.0% | -18.5 to 10.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 688,929 | 716,978 | +4.1% | -101,180 to 157,277 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.13 | -22.9% | -0.127 to 0.0493 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 229 | -26.5% | -269 to 104 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.171 | -26.5% | -0.201 to 0.0776 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
