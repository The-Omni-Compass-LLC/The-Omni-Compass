# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,932 | -0.0% | -4.58 to 3.35 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,935 | 2,934 | -0.0% | -4.75 to 3.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.229 | 0.228 | -0.4% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.377 | 0.377 | -0.2% | -0.0181 to 0.0168 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0814 | 0.0808 | -0.8% | -0.00215 to 0.000917 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,366 | -0.0% | -2.74 to 2.04 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,807 | 61,856 | +0.1% | -345 to 445 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.0877 | -16.1% | -0.0565 to 0.0228 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 157 | -17.7% | -112 to 44.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.143 | 0.118 | -17.6% | -0.0836 to 0.0332 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,911 | +0.4% | -49.5 to 75.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,903 | 2,917 | +0.5% | -47.6 to 75.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.225 | 0.224 | -0.4% | -0.0159 to 0.0139 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.405 | +1.3% | -0.0188 to 0.0295 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.168 | +3.9% | -0.0155 to 0.0282 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,344 | 1,345 | +0.1% | -3.96 to 5.48 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,674 | 61,685 | +0.0% | -125 to 147 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.132 | -10.1% | -0.104 to 0.0745 | EVEN, no difference beyond the noise |
| host CPU-seconds | 267 | 235 | -12.1% | -222 to 157 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.176 | -12.6% | -0.173 to 0.122 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
