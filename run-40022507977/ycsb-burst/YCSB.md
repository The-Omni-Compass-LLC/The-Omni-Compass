# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,873 | 2,872 | -0.0% | -6.5 to 4.91 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -5.18 to 3.33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.508 | 0.512 | +0.9% | -0.0159 to 0.0246 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.719 | 0.736 | +2.4% | -0.0368 to 0.0708 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.227 | -0.4% | -0.00268 to 0.00101 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -20.8 to 0.529 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 394 | -1.7% | -11.8 to -2.01 | GAIN |
| pages read into the cache (misses) | 271,757 | 275,222 | +1.3% | -50,244 to 57,174 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.2 | -4.6% | -0.0983 to 0.079 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 140 | -6.1% | -88 to 69.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.264 | -6.1% | -0.166 to 0.131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
