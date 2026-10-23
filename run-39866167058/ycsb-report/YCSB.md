# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7484 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,890 | -0.0% | -1.58 to 1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% | -1.45 to 0.882 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.304 | 0.31 | +2.1% | -0.02 to 0.0327 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.493 | 0.498 | +0.9% | -0.00902 to 0.0183 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.183 | +1.1% | -0.00673 to 0.0108 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,484 | 7,484 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.1% | -3.11 to 1.64 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,820 | 61,818 | -0.0% | -372 to 368 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.182 | +1.5% | -0.0157 to 0.0209 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 316 | +1.6% | -30.5 to 40.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.238 | +1.6% | -0.0229 to 0.0305 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,940 | 2,940 | -0.0% | -5.12 to 4.33 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,942 | -0.0% | -5.23 to 4.41 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.228 | 0.23 | +0.9% | -0.0159 to 0.0199 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.355 | 0.355 | +0.1% | -0.027 to 0.0277 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0697 | 0.0696 | -0.0% | -0.00233 to 0.00231 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,519 | 1,522 | +0.2% | -1.1 to 6.16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,714 | 77,738 | +0.0% | -86.4 to 134 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.0599 | -47.2% | -0.0812 to -0.0259 | GAIN |
| host CPU-seconds | 85.6 | 42.7 | -50.1% | -65.7 to -20.2 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.16 | 0.0797 | -50.1% | -0.123 to -0.0377 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,914 | 2,914 | -0.0% | -1.05 to 0.0185 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,917 | -0.0% | -1.78 to 1.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.175 | 0.175 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.351 | 0.356 | +1.3% | -0.0203 to 0.0297 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.125 | 0.126 | +0.2% | -0.0051 to 0.00561 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -2.06 to 3.13 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,618 | 61,654 | +0.1% | -182 to 255 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.129 | -0.6% | -0.152 to 0.15 | EVEN, no difference beyond the noise |
| host CPU-seconds | 233 | 231 | -1.2% | -310 to 305 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.175 | 0.173 | -1.1% | -0.232 to 0.228 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,663 | 5,673 | +0.2% | -24.4 to 44.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,675 | 5,684 | +0.2% | -22.4 to 39.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.41 | 0.405 | -1.2% | -0.0271 to 0.0171 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.621 | 0.605 | -2.7% | -0.0732 to 0.0398 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.23 | 0.228 | -1.0% | -0.0119 to 0.00746 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,360 | -0.2% | -9.14 to 4.64 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,867 | 62,922 | +0.1% | -887 to 998 | shown, not judged |
| host CPU busy (share of the run) | 0.31 | 0.291 | -6.3% | -0.0685 to 0.0297 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 523 | -8.4% | -168 to 71.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.197 | -8.5% | -0.0642 to 0.0273 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,921 | 2,920 | -0.0% | -3.16 to 1.36 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,924 | 2,923 | -0.0% | -2.8 to 1.17 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.212 | 0.217 | +2.4% | -0.0153 to 0.0253 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.437 | 0.442 | +1.1% | -0.0307 to 0.04 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.112 | 0.113 | +0.7% | -0.00157 to 0.00306 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | +0.0% | -9.26 to 10.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,451 | 63,146 | -0.5% | -1,711 to 1,101 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.142 | -2.1% | -0.0538 to 0.0478 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 256 | -2.7% | -117 to 103 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.191 | -2.7% | -0.0872 to 0.0768 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
