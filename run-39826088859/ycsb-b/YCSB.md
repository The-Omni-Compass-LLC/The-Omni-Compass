# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,914 | +0.1% | -2.25 to 5.37 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,917 | +0.1% | -1.46 to 4.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.208 | 0.207 | -0.6% | -0.0399 to 0.0373 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.444 | +0.8% | -0.0811 to 0.0884 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.11 | 0.108 | -1.8% | -0.0126 to 0.0086 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | +0.0% | -4.01 to 4.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,768 | 61,844 | +0.1% | -219 to 372 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.126 | -13.0% | -0.108 to 0.0708 | EVEN, no difference beyond the noise |
| host CPU-seconds | 267 | 227 | -14.9% | -230 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.17 | -14.9% | -0.172 to 0.113 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
