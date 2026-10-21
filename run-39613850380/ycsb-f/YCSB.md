# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,681 | 5,676 | -0.1% | -7.41 to -3.58 | LOSS |
| throughput (operations a second) | 5,698 | 5,693 | -0.1% | -5.29 to -4.36 | LOSS |
| latency, 95th percentile (ms) | 0.424 | 0.43 | +1.3% | -0.0118 to 0.0231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.646 | 0.656 | +1.5% | -0.0335 to 0.0535 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.243 | 0.246 | +1.2% | -0.00331 to 0.00901 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.79 to -1.46 | GAIN |
| bytes in the cache, mean (MB) | 417 | 414 | -0.5% | -5.46 to 0.964 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 685,823 | 690,012 | +0.6% | -23,883 to 32,263 | shown, not judged |
| host CPU busy (share of the run) | 0.326 | 0.33 | +1.1% | -0.0181 to 0.0256 | EVEN, no difference beyond the noise |
| host CPU-seconds | 593 | 599 | +1.1% | -45 to 57.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.224 | 0.226 | +1.1% | -0.017 to 0.0217 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
